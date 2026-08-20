# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Process the mesh for visualization in the GUI."""

import enum
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

import numpy as np
import pyvista as pv
from ansys.tools.visualization_interface import MeshObjectPlot

import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.meshinfo import MeshInfo
from ansys.meshing.prime.autogen.meshinfostructs import (
    EdgeConnectivityResults,
    FaceAndEdgeConnectivityParams,
    FaceConnectivityResults,
)
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.internals.comm_manager import CommunicationManager


class ColorByType(enum.IntEnum):
    """Contains the zone types to display."""

    ZONE = 0
    ZONELET = 1
    PART = 2


color_matrix = np.array(
    [
        [155, 186, 126],
        [242, 236, 175],
        [255, 187, 131],
        [194, 187, 97],
        [159, 131, 169],
        [157, 190, 139],
        [233, 218, 158],
        [254, 252, 196],
        [246, 210, 148],
        [215, 208, 198],
        [196, 235, 145],
    ]
)


class DisplayMeshType(enum.IntEnum):
    """Contains the mesh types to display."""

    TOPOFACE = 0
    TOPOEDGE = 1
    FACEZONELET = 2
    EDGEZONELET = 3
    SPLINECONTROLPOINTS = 4
    SPLINESURFACE = 5


@dataclass(frozen=True)
class DisplayEntityKey:
    """Uniquely identify one displayed Prime entity."""

    part_id: int
    display_mesh_type: "DisplayMeshType"
    entity_id: int


#: Batch-local render entity ID (not assumed unique across parts or types).
RENDER_ENTITY_ID_ARRAY = "prime_render_entity_id"

#: Prime part ID owning each rendered cell.
PART_ID_ARRAY = "prime_part_id"

#: Original Prime entity ID, such as a topo-face ID or face-zonelet ID.
ENTITY_ID_ARRAY = "prime_entity_id"

#: :class:`DisplayMeshType` value associated with each rendered cell.
ENTITY_TYPE_ARRAY = "prime_entity_type"

#: Prime zone ID associated with each rendered cell.
ZONE_ID_ARRAY = "prime_zone_id"

#: RGB color currently applied to each rendered cell.
ENTITY_COLOR_ARRAY = "colors"


REQUIRED_PICKING_ARRAYS = (
    RENDER_ENTITY_ID_ARRAY,
    PART_ID_ARRAY,
    ENTITY_ID_ARRAY,
    ENTITY_TYPE_ARRAY,
    ZONE_ID_ARRAY,
)


class DisplayMeshInfo:
    """Contains the mesh information to display.

    Parameters
    ----------
    id : int, default: 0
        ID of the mesh.
    part_id : int, default: 0
        ID of the part.
    part_name : str, default: None
        Name of the part.
    zone_id : int, default: 0
        ID of the zone.
    zone_name : str, default: None
        Name of the zone.
    display_mesh_type : DisplayMeshType, default: FACEZONELET
        Type of mesh to display.
    render_mesh : pv.PolyData, default: None
        Triangulated geometry to shade in place of the facets themselves. This is
        set only for zonelets that VTK cannot tessellate acceptably on its own. For
        more information, see :func:`Mesh.get_face_polydata`.
    element_edges : pv.PolyData, default: None
        Element outlines to draw as separate line geometry. This is set only for
        zonelets whose outlines cannot be drawn by the face actor itself. For more
        information, see :func:`Mesh.get_face_polydata`.
    """

    def __init__(
        self,
        id=0,
        part_id=0,
        part_name=None,
        zone_id=0,
        zone_name=None,
        display_mesh_type=DisplayMeshType.FACEZONELET,
        has_mesh=False,
        render_mesh=None,
        element_edges=None,
    ) -> None:
        """Initialize display mesh information."""
        self.id = int(id)
        self.part_id = int(part_id)
        self.zone_id = int(zone_id)
        self.part_name = part_name
        self.zone_name = zone_name
        self.display_mesh_type = DisplayMeshType(display_mesh_type)
        self.has_mesh = bool(has_mesh)
        self.render_mesh = render_mesh
        self.element_edges = element_edges

    @property
    def key(self) -> DisplayEntityKey:
        """Return the model-unique key of this display entity."""
        return DisplayEntityKey(
            part_id=self.part_id,
            display_mesh_type=self.display_mesh_type,
            entity_id=self.id,
        )


class RenderBatch:
    """Geometry for one persistent actor grouped by display entity type.

    A render batch spans all parts contributing the same display entity type.
    Entity ownership is retained in cell-data arrays for picking, coloring,
    and visibility.
    """

    def __init__(
        self,
        mesh: "pv.PolyData",
        infos: Mapping[int, DisplayMeshInfo],
        display_mesh_type: DisplayMeshType,
        pickable: bool = True,
    ) -> None:
        """Initialize the render batch."""
        self.mesh = mesh
        self.infos = dict(infos)
        self.display_mesh_type = DisplayMeshType(display_mesh_type)
        self.pickable = bool(pickable)
        self._validate()

    def _validate(self) -> None:
        """Validate the geometry and ownership metadata."""
        if self.mesh is None:
            raise ValueError("A render batch requires a mesh.")
        missing = [
            array_name
            for array_name in REQUIRED_PICKING_ARRAYS
            if array_name not in self.mesh.cell_data
        ]
        if missing:
            raise ValueError(
                "The render batch is missing required cell arrays: " + ", ".join(missing)
            )
        render_ids = np.asarray(
            self.mesh.cell_data[RENDER_ENTITY_ID_ARRAY],
            dtype=np.int64,
        )
        unknown_ids = set(np.unique(render_ids)).difference(self.infos)
        if unknown_ids:
            raise ValueError(
                "The render batch contains render entity IDs without "
                f"DisplayMeshInfo entries: {sorted(unknown_ids)}"
            )
        entity_types = np.asarray(
            self.mesh.cell_data[ENTITY_TYPE_ARRAY],
            dtype=np.int64,
        )
        expected_type = int(self.display_mesh_type)
        if entity_types.size and np.any(entity_types != expected_type):
            raise ValueError("A render batch may contain only one DisplayMeshType.")

    @property
    def render_entity_ids(self) -> np.ndarray:
        """Batch-local render entity ID of every cell."""
        return np.asarray(
            self.mesh.cell_data[RENDER_ENTITY_ID_ARRAY],
            dtype=np.int64,
        )

    @property
    def entity_ids(self) -> np.ndarray:
        """Original Prime entity ID of every cell."""
        return np.asarray(
            self.mesh.cell_data[ENTITY_ID_ARRAY],
            dtype=np.int64,
        )

    @property
    def part_ids(self) -> np.ndarray:
        """Prime part ID of every cell."""
        return np.asarray(
            self.mesh.cell_data[PART_ID_ARRAY],
            dtype=np.int64,
        )

    def info_for_render_id(self, render_entity_id: int) -> DisplayMeshInfo:
        """Return display information for a batch-local render entity ID."""
        return self.infos[int(render_entity_id)]

    def apply_colors(self, color_type: Optional[ColorByType] = None) -> None:
        """Color all cells using their owning display entity."""
        self.mesh.cell_data[ENTITY_COLOR_ARRAY] = compute_entity_colors(
            self.infos,
            self.render_entity_ids,
            color_type,
        )
        self.mesh.set_active_scalars(
            ENTITY_COLOR_ARRAY,
            preference="cell",
        )


@dataclass
class ModelRenderData:
    """Model-wide render geometry grouped by entity type."""

    batches: Dict[str, Dict[DisplayMeshType, RenderBatch]]
    ctrlpts: List = field(default_factory=list)
    splines: List = field(default_factory=list)


# Backward-compatible alias for callers that imported PartRenderData.
PartRenderData = ModelRenderData


def _edge_lines_from_list(edge_list: np.ndarray) -> "tuple[np.ndarray, int]":
    """Turn a Prime edge list into VTK line connectivity.

    Parameters
    ----------
    edge_list : np.ndarray
        Flat edge list from the server.

    Returns
    -------
    tuple[np.ndarray, int]
        VTK line connectivity and the number of line cells.
    """
    segments = []
    cursor = 0
    size = int(edge_list.size)
    while cursor < size:
        nnodes = int(edge_list[cursor])
        nodes = edge_list[cursor + 1 : cursor + 1 + nnodes]
        if nnodes == 3:
            segments.append((int(nodes[0]), int(nodes[1])))
            segments.append((int(nodes[1]), int(nodes[2])))
        else:
            segments.append((int(nodes[0]), int(nodes[1])))
        cursor += 1 + nnodes
    if not segments:
        return np.empty((0, 3), dtype=np.int64), 0
    cells = np.full((len(segments), 3), 2, dtype=np.int64)
    cells[:, 1:] = segments
    return cells, len(segments)


def _polydata_polygon_piece(poly: "pv.PolyData", entity_id: int):
    """Extract an array-level polygon piece from a PolyData.

    Parameters
    ----------
    poly : pv.PolyData
        Polygon mesh of one entity.
    entity_id : int
        Entity the cells belong to.

    Returns
    -------
    tuple
        ``(points, connectivity, n_cells, entity_id)`` for :func:`_assemble_pieces`.
    """
    faces = np.asarray(poly.faces)
    return poly.points.copy(), faces, int(poly.n_cells), int(entity_id)


def _polydata_line_piece(poly: "pv.PolyData", entity_id: int):
    """Extract an array-level line piece from a PolyData.

    Parameters
    ----------
    poly : pv.PolyData
        Line mesh of one entity.
    entity_id : int
        Entity the cells belong to.

    Returns
    -------
    tuple
        ``(points, connectivity, n_cells, entity_id)`` for :func:`_assemble_pieces`.
    """
    lines = np.asarray(poly.lines)
    if lines.ndim == 1:
        lines = lines.reshape(-1, 3)
    return poly.points.copy(), lines, int(poly.n_cells), int(entity_id)


def _assemble_colored_line_pieces(pieces: List) -> "pv.PolyData":
    """Merge line pieces that already carry per-cell colors.

    Parameters
    ----------
    pieces : List
        ``(points, connectivity, colors)`` tuples.

    Returns
    -------
    pv.PolyData
        Merged lines, or ``None`` when empty.
    """
    if not pieces:
        return None
    assembled = []
    colors = []
    point_offset = 0
    for points, connectivity, piece_colors in pieces:
        line_cells = np.asarray(connectivity)
        if line_cells.ndim == 1:
            line_cells = line_cells.reshape(-1, 3)
        else:
            line_cells = line_cells.copy()
        line_cells[:, 1:] += point_offset
        assembled.append(
            (
                points,
                line_cells,
                int(piece_colors.shape[0]),
                0,
            )
        )
        colors.append(np.asarray(piece_colors, dtype=np.uint8))
        point_offset += points.shape[0]
    mesh = _assemble_pieces(assembled, lines=True)
    if mesh is not None:
        mesh.cell_data[ENTITY_COLOR_ARRAY] = np.concatenate(colors, axis=0)
    return mesh


def default_color_key(info: DisplayMeshInfo) -> int:
    """Get the property a display entity is colored by before a color mode is chosen.

    Which property this is depends on the type of the entity: mesh faces are colored
    by part and topology edges by their own ID, while everything else is colored by
    zone.

    Parameters
    ----------
    info : DisplayMeshInfo
        Display information of the entity.

    Returns
    -------
    int
        Value to take the color from.
    """
    mesh_type = info.display_mesh_type
    if mesh_type == DisplayMeshType.TOPOEDGE:
        return info.id
    if mesh_type == DisplayMeshType.FACEZONELET:
        return info.part_id
    return info.zone_id


def entity_color(info: DisplayMeshInfo, color_type: ColorByType = None):
    """Get the color of a display entity for the given color mode.

    Parameters
    ----------
    info : DisplayMeshInfo
        Display information of the entity.
    color_type : ColorByType, default: None
        Entity property to take the color from. When this is ``None``, the property
        is chosen by :func:`default_color_key`.

    Returns
    -------
    np.ndarray
        RGB color of the entity.
    """
    num_colors = int(color_matrix.size / 3)
    if color_type is None:
        key = default_color_key(info)
    elif color_type == ColorByType.ZONELET:
        key = info.id
    elif color_type == ColorByType.PART:
        key = info.part_id
    else:
        key = info.zone_id
    return color_matrix[key % num_colors]


def compute_entity_colors(
    infos: Mapping[int, DisplayMeshInfo],
    render_entity_ids: np.ndarray,
    color_type: Optional[ColorByType] = None,
) -> np.ndarray:
    """Compute per-cell colors for a merged entity-type mesh."""
    render_entity_ids = np.asarray(render_entity_ids, dtype=np.int64)
    if render_entity_ids.size == 0:
        return np.empty((0, 3), dtype=np.uint8)

    unique_ids, inverse = np.unique(render_entity_ids, return_inverse=True)
    missing = [int(render_id) for render_id in unique_ids if int(render_id) not in infos]
    if missing:
        raise KeyError(f"No DisplayMeshInfo exists for render entity IDs {missing}.")

    palette = np.asarray(
        [entity_color(infos[int(render_id)], color_type) for render_id in unique_ids],
        dtype=np.uint8,
    )
    return palette[inverse]


def _as_polydata(mesh: "pv.DataSet") -> "pv.PolyData":
    """Return render geometry as PolyData without merging points."""
    if isinstance(mesh, pv.PolyData):
        return mesh.copy(deep=False)
    return mesh.extract_surface(nonlinear_subdivision=0, progress_bar=False)


def _attach_entity_metadata(
    mesh: "pv.PolyData",
    info: DisplayMeshInfo,
    render_entity_id: int,
) -> "pv.PolyData":
    """Attach Prime ownership metadata to every cell of a geometry piece."""
    output = _as_polydata(mesh)
    number_of_cells = output.n_cells
    output.cell_data[RENDER_ENTITY_ID_ARRAY] = np.full(
        number_of_cells, int(render_entity_id), dtype=np.int64
    )
    output.cell_data[PART_ID_ARRAY] = np.full(number_of_cells, info.part_id, dtype=np.int64)
    output.cell_data[ENTITY_ID_ARRAY] = np.full(number_of_cells, info.id, dtype=np.int64)
    output.cell_data[ENTITY_TYPE_ARRAY] = np.full(
        number_of_cells, int(info.display_mesh_type), dtype=np.int16
    )
    output.cell_data[ZONE_ID_ARRAY] = np.full(number_of_cells, info.zone_id, dtype=np.int64)
    return output


def _validate_merged_metadata(mesh: "pv.PolyData") -> None:
    """Ensure a merge has preserved all picking arrays."""
    missing = [
        array_name for array_name in REQUIRED_PICKING_ARRAYS if array_name not in mesh.cell_data
    ]
    if missing:
        raise RuntimeError(
            "PyVista discarded required Prime picking metadata while "
            "merging geometry: " + ", ".join(missing)
        )
    for array_name in REQUIRED_PICKING_ARRAYS:
        if len(mesh.cell_data[array_name]) != mesh.n_cells:
            raise RuntimeError(f"Cell array {array_name!r} does not match the merged cell count.")


def _finalize_typed_batches(
    grouped: Dict[DisplayMeshType, List[Tuple["pv.PolyData", DisplayMeshInfo]]],
    pickable: bool = True,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Merge grouped geometry pieces into one batch per display entity type."""
    batches: Dict[DisplayMeshType, RenderBatch] = {}
    for display_mesh_type, items in grouped.items():
        infos: Dict[int, DisplayMeshInfo] = {}
        pieces: List[pv.PolyData] = []
        for render_entity_id, (geometry, info) in enumerate(items):
            infos[render_entity_id] = info
            pieces.append(_attach_entity_metadata(geometry, info, render_entity_id))
        merged = _merge_geometry(pieces)
        if merged is None:
            continue
        _validate_merged_metadata(merged)
        batch = RenderBatch(
            mesh=merged,
            infos=infos,
            display_mesh_type=display_mesh_type,
            pickable=pickable,
        )
        if pickable:
            batch.apply_colors()
        elif ENTITY_COLOR_ARRAY in merged.cell_data:
            merged.set_active_scalars(ENTITY_COLOR_ARRAY, preference="cell")
        batches[display_mesh_type] = batch
    return batches


def _merge_render_batch_dicts(
    *batch_dicts: Dict[DisplayMeshType, RenderBatch],
) -> Dict[DisplayMeshType, RenderBatch]:
    """Merge render batches that share the same display entity type."""
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)

    for batch_dict in batch_dicts:
        for display_mesh_type, batch in batch_dict.items():
            for render_entity_id, info in batch.infos.items():
                mask = batch.render_entity_ids == render_entity_id
                if not mask.any():
                    continue
                piece = batch.mesh.extract_cells(np.flatnonzero(mask))
                grouped[display_mesh_type].append((piece, info))

    merged: Dict[DisplayMeshType, RenderBatch] = {}
    for display_mesh_type, items in grouped.items():
        pickable = display_mesh_type in (
            DisplayMeshType.TOPOFACE,
            DisplayMeshType.FACEZONELET,
        )
        merged.update(_finalize_typed_batches({display_mesh_type: items}, pickable=pickable))
    return merged


def _build_batches_from_raw_faces(
    grouped_raw: Dict[DisplayMeshType, List[Tuple[np.ndarray, np.ndarray, int, DisplayMeshInfo]]],
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build face batches from array-level connectivity grouped by entity type."""
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)
    for display_mesh_type, raw_pieces in grouped_raw.items():
        for render_entity_id, (vertices, block, n_cells, info) in enumerate(raw_pieces):
            mesh = _assemble_entity_mesh(
                vertices,
                block,
                n_cells,
                info,
                render_entity_id,
                lines=False,
            )
            if mesh is not None:
                grouped[display_mesh_type].append((mesh, info))
    return _finalize_typed_batches(grouped, pickable=True)


def build_face_render_batches(
    face_entries: Iterable,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build one face actor batch per display entity type."""
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)
    for entry in face_entries:
        if entry is None:
            continue
        mesh_object, info = entry
        geometry = info.render_mesh if info.render_mesh is not None else mesh_object.mesh
        if geometry is None or geometry.n_cells == 0:
            continue
        grouped[info.display_mesh_type].append((geometry, info))
    return _finalize_typed_batches(grouped, pickable=True)


def build_element_edge_batches(
    face_entries: Iterable,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build one element-outline batch per owning face entity type."""
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)
    for entry in face_entries:
        if entry is None:
            continue
        mesh_object, info = entry
        if not info.has_mesh or info.element_edges is None:
            continue
        if info.element_edges is not None:
            outlines = info.element_edges
        elif mesh_object.mesh is not None:
            outlines = mesh_object.mesh.extract_all_edges(progress_bar=False)
        else:
            outlines = None
        if outlines is None or outlines.n_cells == 0:
            continue
        grouped[info.display_mesh_type].append((outlines, info))
    return _finalize_typed_batches(grouped, pickable=False)


def build_element_edge_mesh(face_entries: Iterable) -> "pv.PolyData":
    """Return all element outlines as one compatibility mesh."""
    batches = build_element_edge_batches(face_entries)
    return _merge_geometry([batch.mesh for batch in batches.values()])


def build_edge_render_batches(
    edge_entries: Iterable,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build one persistent edge batch per edge display entity type."""
    grouped = defaultdict(list)
    for entry in edge_entries:
        if entry is None:
            continue
        if isinstance(entry, tuple):
            mesh_object, info = entry
        else:
            mesh_object = entry
            info = None
        geometry = mesh_object.mesh
        if geometry is None or geometry.n_cells == 0:
            continue
        required = (
            PART_ID_ARRAY,
            ENTITY_ID_ARRAY,
            ENTITY_TYPE_ARRAY,
            ZONE_ID_ARRAY,
        )
        missing = [name for name in required if name not in geometry.cell_data]
        if missing:
            raise ValueError(
                "Edge geometry is missing Prime identity arrays: " + ", ".join(missing)
            )
        part_ids = np.unique(np.asarray(geometry.cell_data[PART_ID_ARRAY]))
        entity_ids = np.unique(np.asarray(geometry.cell_data[ENTITY_ID_ARRAY]))
        entity_types = np.unique(np.asarray(geometry.cell_data[ENTITY_TYPE_ARRAY]))
        zone_ids = np.unique(np.asarray(geometry.cell_data[ZONE_ID_ARRAY]))
        if (
            len(part_ids) != 1
            or len(entity_ids) != 1
            or len(entity_types) != 1
            or len(zone_ids) != 1
        ):
            raise ValueError("One edge entry must represent exactly one Prime edge entity.")
        if info is None:
            part = mesh_object.custom_object
            info = DisplayMeshInfo(
                id=int(entity_ids[0]),
                part_id=int(part_ids[0]),
                part_name=getattr(part, "name", None),
                zone_id=int(zone_ids[0]),
                zone_name=None,
                display_mesh_type=DisplayMeshType(int(entity_types[0])),
                has_mesh=False,
            )
        grouped[info.display_mesh_type].append((geometry, info))
    return _finalize_typed_batches(dict(grouped), pickable=False)


def build_edge_render_mesh(edge_entries: Iterable) -> "pv.PolyData":
    """Return all edge batches as a compatibility mesh."""
    batches = build_edge_render_batches(edge_entries)
    return _merge_geometry([batch.mesh for batch in batches.values()])


def _merge_geometry(
    pieces: Sequence["pv.PolyData"],
) -> Optional["pv.PolyData"]:
    """Concatenate geometry without merging points."""
    valid_pieces = [
        _as_polydata(piece) for piece in pieces if piece is not None and piece.n_cells > 0
    ]
    if not valid_pieces:
        return None
    if len(valid_pieces) == 1:
        return valid_pieces[0].copy(deep=False)
    merged = pv.merge(valid_pieces, merge_points=False)
    if not isinstance(merged, pv.PolyData):
        merged = merged.extract_surface(nonlinear_subdivision=0, progress_bar=False)
    return merged


def _prefix_offsets(counts: np.ndarray) -> np.ndarray:
    """Start index of each block once equal-length blocks are laid end to end.

    Parameters
    ----------
    counts : np.ndarray
        Length of each block.

    Returns
    -------
    np.ndarray
        Start index of each block, so ``offsets[i]`` is the sum of the counts
        before block ``i``.
    """
    offsets = np.zeros(len(counts), dtype=np.int64)
    if len(counts) > 1:
        np.cumsum(counts[:-1], out=offsets[1:])
    return offsets


def _scan_cell_block(block: np.ndarray) -> "tuple[int, int]":
    """Count the cells of a VTK connectivity block and the widest cell in it.

    A block is a flat ``[n, i0..i(n-1), m, j0..]`` VTK connectivity array. The
    common case of a block whose cells all have the same number of nodes is read
    without walking it; a mixed block falls back to a stride walk.

    Parameters
    ----------
    block : np.ndarray
        VTK connectivity of one entity.

    Returns
    -------
    tuple[int, int]
        Number of cells and the largest node count of any cell.
    """
    if block.size == 0:
        return 0, 0
    first = int(block[0])
    stride = first + 1
    if stride > 0 and block.size % stride == 0:
        view = block.reshape(-1, stride)
        if np.all(view[:, 0] == first):
            return int(view.shape[0]), first
    n_cells = 0
    widest = 0
    cursor = 0
    size = int(block.size)
    while cursor < size:
        count = int(block[cursor])
        if count > widest:
            widest = count
        n_cells += 1
        cursor += count + 1
    return n_cells, widest


def _offset_cell_ids(block: np.ndarray, offset: int) -> np.ndarray:
    """Shift the point ids of a VTK connectivity block by a constant.

    Only the id entries are shifted; the per-cell node counts are left alone. A
    block whose cells all have the same size is shifted with a reshape, and a
    mixed block with a stride walk.

    Parameters
    ----------
    block : np.ndarray
        VTK connectivity of one entity, with point ids local to that entity.
    offset : int
        Value to add to every point id.

    Returns
    -------
    np.ndarray
        Connectivity with the point ids shifted into the merged point array.
    """
    if offset == 0:
        return block
    first = int(block[0])
    stride = first + 1
    if stride > 0 and block.size % stride == 0:
        view = block.reshape(-1, stride)
        if np.all(view[:, 0] == first):
            shifted = view.copy()
            shifted[:, 1:] += offset
            return shifted.ravel()
    shifted = block.copy()
    cursor = 0
    size = int(shifted.size)
    while cursor < size:
        count = int(shifted[cursor])
        shifted[cursor + 1 : cursor + 1 + count] += offset
        cursor += count + 1
    return shifted


def _assemble_entity_mesh(
    points: np.ndarray,
    block: np.ndarray,
    n_cells: int,
    info: DisplayMeshInfo,
    render_entity_id: int,
    lines: bool = False,
) -> Optional["pv.PolyData"]:
    """Build one entity mesh from array-level connectivity with picking metadata."""
    mesh = _assemble_pieces([(points, block, n_cells, 0)], lines=lines)
    if mesh is None:
        return None
    return _attach_entity_metadata(mesh, info, render_entity_id)


def _assemble_pieces(pieces: List, lines: bool) -> "pv.PolyData":
    """Lay entity geometry end to end into one mesh without metadata."""
    if not pieces:
        return None
    points_list = []
    blocks = []
    point_offset = 0
    for points, block, n_cells, _entity_id in pieces:
        points_list.append(points)
        if lines:
            line_cells = np.asarray(block)
            if line_cells.ndim == 1:
                line_cells = line_cells.reshape(-1, 3)
            else:
                line_cells = line_cells.copy()
            line_cells[:, 1:] += point_offset
            blocks.append(line_cells)
        else:
            blocks.append(_offset_cell_ids(np.asarray(block), point_offset))
        point_offset += points.shape[0]

    points = np.concatenate(points_list, axis=0)
    if lines:
        mesh = pv.PolyData()
        mesh.points = points
        mesh.lines = np.vstack(blocks)
    else:
        connectivity = np.concatenate(blocks)
        mesh = pv.PolyData(points, connectivity)
    return mesh


def compute_distance(point1, point2) -> float:
    """Compute the distance between two points.

    Parameters
    ----------
    point1 : list
        List with the coordinates of the first point.
    point2 : list
        List with the coordinates of the second point.

    Returns
    -------
    float
        Distance between the two points.
    """
    dist = np.linalg.norm(np.array(point2) - np.array(point1))
    return dist


def compute_face_list_from_structured_nodes(dim):
    """Compute the distances from the nodes.

    Parameters
    ----------
    dim : List[int]
        List with the number of elements in each dimension.

    Returns
    -------
    List
        List with the faces.
    """
    flist = []
    for w in range(dim[2]):
        for u in range(dim[0] - 1):
            for v in range(dim[1] - 1):
                flist.append(4)
                flist.append(u + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + (v + 1) * dim[0] + w * dim[0] * dim[1])
                flist.append(u + (v + 1) * dim[0] + w * dim[0] * dim[1])

    for v in range(dim[1]):
        for u in range(dim[0] - 1):
            for w in range(dim[2] - 1):
                flist.append(4)
                flist.append(u + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + v * dim[0] + (w + 1) * dim[0] * dim[1])
                flist.append(u + v * dim[0] + (w + 1) * dim[0] * dim[1])

    for u in range(dim[0]):
        for v in range(dim[1] - 1):
            for w in range(dim[2] - 1):
                flist.append(4)
                flist.append(u + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + (v + 1) * dim[0] + w * dim[0] * dim[1])
                flist.append(u + (v + 1) * dim[0] + (w + 1) * dim[0] * dim[1])
                flist.append(u + v * dim[0] + (w + 1) * dim[0] * dim[1])
    return flist


class Mesh(MeshInfo):
    """Processes the mesh for visualization in the GUI.

    Parameters
    ----------
    model : CommunicationManager
        Model to process.
    """

    def __init__(self, model: CommunicationManager):
        """Initialize the mesh object."""
        super().__init__(model)
        self._model = model
        self._unfreeze()
        self._parts_polydata = {}
        self._model_render_data = None
        self._render_data_part_ids = None
        self._freeze()

    @property
    def model(self):
        """Model."""
        return self._model

    def get_face_color(self, part: Part, model_type: ColorByType = ColorByType.ZONE):
        """Get the colors of faces.

        Returns
        -------
        List
            List of colors for faces.
        """
        num_colors = int(color_matrix.size / 3)
        if model_type == ColorByType.ZONELET:
            return color_matrix[part.id % num_colors].tolist()
        elif model_type == ColorByType.PART:
            return color_matrix[part.id % num_colors].tolist()
        else:
            return color_matrix[part.id % num_colors].tolist()

    def get_edge_color(self, edge_results: EdgeConnectivityResults, index: int):
        """Get the colors of edges.

        Returns
        -------
        List
            List of colors for edges.
        """
        mesh_type = DisplayMeshType.EDGEZONELET
        if edge_results.topo_edge_ids[index] > 0:
            mesh_type = DisplayMeshType.TOPOEDGE
        num_colors = int(color_matrix.size / 3)
        if mesh_type == DisplayMeshType.EDGEZONELET:
            return color_matrix[index % num_colors].tolist()
        elif mesh_type == DisplayMeshType.TOPOEDGE:
            if edge_results.topo_edge_types[index] == 1:
                return [255, 0, 0]
            elif edge_results.topo_edge_types[index] == 2:
                return [0, 0, 0]
            elif edge_results.topo_edge_types[index] == 3:
                return [0, 255, 255]
            elif edge_results.topo_edge_types[index] == 4:
                return [255, 0, 255]
            elif edge_results.topo_edge_types[index] == 5:
                return [255, 255, 0]
            elif edge_results.topo_edge_types[index] == 6:
                return [128, 0, 128]
            else:
                return color_matrix[edge_results.id % num_colors].tolist()

    def _get_vertices_and_surf_faces(
        self, connectivity_results: FaceConnectivityResults, index
    ) -> Union[np.ndarray, np.ndarray]:
        """Calculate the vertices and faces of the mesh.

        Parameters
        ----------
        connectivity_results : Union[FaceConnectivityResults, EdgeConnectivityResults]
            Results of the connectivity operations.
        index : _type_
            Index of the mesh.

        Returns
        -------
        Union[np.ndarray, np.ndarray]
            Vertices and faces of the mesh.
        """
        node_start = 3 * np.sum(connectivity_results.num_nodes_per_face_zonelet[0:index])
        num_node_coords = 3 * connectivity_results.num_nodes_per_face_zonelet[index]
        face_list_start = np.sum(connectivity_results.num_face_list_per_face_zonelet[0:index])
        num_face_list = connectivity_results.num_face_list_per_face_zonelet[index]
        vertices = connectivity_results.node_coords[
            node_start : node_start + num_node_coords
        ].reshape((-1, 3))
        faces = connectivity_results.face_list[face_list_start : face_list_start + num_face_list]
        return vertices, faces

    def _get_vertices_and_surf_edges(
        self, connectivity_results: EdgeConnectivityResults, index: int
    ) -> Union[np.ndarray, np.ndarray]:
        """Calculate the vertices and faces of the mesh.

        Parameters
        ----------
        connectivity_results : Union[FaceConnectivityResults, EdgeConnectivityResults]
            Results of the connectivity operations.
        index : int
            Index of the mesh.

        Returns
        -------
        Union[np.ndarray, np.ndarray]
            Vertices and faces of the mesh.
        """
        node_start = 3 * np.sum(connectivity_results.num_nodes_per_edge_zonelet[0:index])
        num_node_coords = 3 * connectivity_results.num_nodes_per_edge_zonelet[index]
        edge_list_start = np.sum(connectivity_results.num_edge_list_per_edge_zonelet[0:index])
        num_edge_list = connectivity_results.num_edge_list_per_edge_zonelet[index]
        vertices = connectivity_results.node_coords[
            node_start : node_start + num_node_coords
        ].reshape((-1, 3))
        faces = connectivity_results.edge_list[edge_list_start : edge_list_start + num_edge_list]
        return vertices, faces

    def get_face_polydata(
        self, part_id: int, face_facet_res: FaceConnectivityResults, index: int
    ) -> MeshObjectPlot:
        """Get the polydata object of the faces.

        Parameters
        ----------
        part_id : int
            ID of the part to get the polydata from.
        face_facet_res : FaceConnectivityResults
            Results of the face connectivity.
        index : int
            Index of the face.

        Returns
        -------
        MeshObjectPlot, DisplayMeshInfo
            Mesh to be plotted and information of the mesh to display.

        Notes
        -----
        Quadratic and polygonal facets reach the renderer as polygons of more than
        four nodes. VTK tessellates such a polygon at draw time by fanning it from
        its first node, which on a curved facet swallows the element outlines behind
        the shaded surface when viewed head on, and leaves bright slivers along them
        at oblique angles. Those zonelets are therefore given an explicit
        triangulation to shade, together with the outlines of the original polygons
        for the plotter to draw as independent line geometry.
        """
        part = self._model.get_part(part_id)

        vertices, faces = self._get_vertices_and_surf_faces(face_facet_res, index)
        surf = pv.PolyData(vertices, faces)
        fcolor = np.array(self.get_face_color(part, ColorByType.ZONE))
        colors = np.tile(fcolor, (surf.n_faces_strict, 1))
        surf["colors"] = colors
        has_mesh = True
        if face_facet_res.topo_face_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOFACE
            id = face_facet_res.topo_face_ids[index]
            has_mesh = bool(face_facet_res.mesh_face_ids[index] > 0)
        else:
            display_mesh_type = DisplayMeshType.FACEZONELET
            id = face_facet_res.face_zonelet_ids[index]

        render_mesh = None
        element_edges = None
        if has_mesh and surf.n_cells > 0 and surf.GetPolys().GetMaxCellSize() > 4:
            render_mesh = surf.triangulate(progress_bar=False)
            element_edges = surf.extract_all_edges(progress_bar=False)

        if surf.n_points > 0:
            return MeshObjectPlot(part, surf), DisplayMeshInfo(
                id=id,
                part_id=part_id,
                zone_id=face_facet_res.face_zone_ids[index],
                display_mesh_type=display_mesh_type,
                part_name=part.name,
                zone_name=face_facet_res.face_zone_names[index],
                has_mesh=has_mesh,
                render_mesh=render_mesh,
                element_edges=element_edges,
            )

    def get_edge_polydata(
        self, part_id: int, edge_facet_res: EdgeConnectivityResults, index: int
    ) -> MeshObjectPlot:
        """Get the polydata object of the edges.

        Parameters
        ----------
        part_id : int
            ID of the part to get the polydata from.
        edge_facet_res : EdgeConnectivityResults
            Results of the edge connectivity.
        index : int
            Index of the edge.

        Returns
        -------
        MeshObjectPlot
            Mesh to be displayed.
        """
        part = self._model.get_part(part_id)
        vertices, faces = self._get_vertices_and_surf_edges(edge_facet_res, index)
        edge = pv.PolyData()
        edge.points = vertices
        segments = []
        j = 0
        while j < len(faces):
            nnodes = faces[j]
            nodes = faces[j + 1 : j + 1 + nnodes]
            if nnodes == 3:
                # a quadratic edge arrives as (start, mid, end); drawing it as a
                # single start to end segment cuts across the curve the mid-side
                # node describes, so draw both halves instead
                segments.append((nodes[0], nodes[1]))
                segments.append((nodes[1], nodes[2]))
            else:
                segments.append((nodes[0], nodes[1]))
            j += 1 + nnodes
        cells = np.full((len(segments), 3), 2, dtype=np.int_)
        if segments:
            cells[:, 1:] = segments
        edge.lines = cells
        ecolor = np.array(self.get_edge_color(edge_facet_res, index))
        colors = np.tile(ecolor, (len(segments), 1))
        # a closed edge has as many points as segments, so the colors have to name
        # the association they belong to rather than let it be inferred from length
        edge.cell_data[ENTITY_COLOR_ARRAY] = colors

        if edge_facet_res.topo_edge_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOEDGE
            entity_id = int(edge_facet_res.topo_edge_ids[index])
        else:
            display_mesh_type = DisplayMeshType.EDGEZONELET
            entity_id = int(edge_facet_res.edge_zonelet_ids[index])

        zone_ids = getattr(edge_facet_res, "edge_zone_ids", None)
        zone_id = int(zone_ids[index]) if zone_ids is not None and len(zone_ids) > index else 0

        if edge.n_cells > 0:
            edge.cell_data[PART_ID_ARRAY] = np.full(edge.n_cells, part_id, dtype=np.int64)
            edge.cell_data[ENTITY_ID_ARRAY] = np.full(edge.n_cells, entity_id, dtype=np.int64)
            edge.cell_data[ENTITY_TYPE_ARRAY] = np.full(
                edge.n_cells, int(display_mesh_type), dtype=np.int16
            )
            edge.cell_data[ZONE_ID_ARRAY] = np.full(edge.n_cells, zone_id, dtype=np.int64)
            edge.set_active_scalars(ENTITY_COLOR_ARRAY, preference="cell")

        if edge.n_points > 0:
            zone_names = getattr(edge_facet_res, "edge_zone_names", None)
            zone_name = (
                zone_names[index] if zone_names is not None and len(zone_names) > index else None
            )
            return MeshObjectPlot(part, edge)

    def get_spline_cp_polydata(self, part_id: int, spline_id: int) -> MeshObjectPlot:
        """Get the polydata object of the spline control points.

        Parameters
        ----------
        part_id : int
            ID of the part to get the polydata from.
        spline_id : int
            ID of the spline.

        Returns
        -------
        MeshObjectPlot
            Mesh to be displayed.
        """
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)
        dim = spline.control_points_count
        vertices = spline.control_points
        faces = self.compute_face_list_from_structured_nodes(dim)
        surf = pv.PolyData(vertices, faces)
        fcolor = np.array([0, 0, 255])
        colors = np.tile(fcolor, (surf.n_faces_strict, 1))
        surf["colors"] = colors
        if surf.n_points > 0:
            return MeshObjectPlot(part, surf)

    def get_spline_surface_polydata(self, part_id: int, spline_id: int) -> MeshObjectPlot:
        """Get the polydata object of the spline surface.

        Parameters
        ----------
        part_id : int
            ID of the part to get the polydata from.
        spline_id : int
            ID of the spline.

        Returns
        -------
        MeshObjectPlot
            Mesh to be displayed.
        """
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)
        dim = spline.spline_points_count
        vertices = spline.spline_points
        faces = self.compute_face_list_from_structured_nodes(dim)
        surf = pv.PolyData(vertices, faces)
        fcolor = np.array(color_matrix[1])
        colors = np.tile(fcolor, (surf.n_faces_strict, 1))
        surf["colors"] = colors
        if surf.n_points > 0:
            return MeshObjectPlot(part, surf)

    def get_scoped_polydata(self, scope: "prime.ScopeDefinition", update: bool = False):
        """Get the polydata object of the scoped mesh.

        Parameters
        ----------
        scope : prime.ScopeDefinition
            Scope to get the mesh from.

        Returns
        -------
        pv.PolyData
            PyVista mesh object.
        """
        self.as_polydata(update=update)
        parts = self._model.control_data.get_scope_parts(scope)

        # Update the polydata if any part is not in the dictionary
        if len(set(parts).intersection(set(self._parts_polydata.keys()))) != len(parts):
            self.update_pd(parts)
        scoped_pd = {}
        for part_id in parts:
            part = self._model.get_part(part_id)
            # narrow the query to this part without rewriting the caller's scope;
            # mutating part_expression on the input silently changes later plots
            # that reuse the same ScopeDefinition
            part_scope = prime.ScopeDefinition(
                model=self._model,
                entity_type=scope.entity_type,
                evaluation_type=scope.evaluation_type,
                part_expression=part.name,
                label_expression=scope.label_expression,
                zone_expression=scope.zone_expression,
            )
            disp_data = None
            disp_ids = []
            if scope.entity_type == prime.ScopeEntity.FACEZONELETS:
                disp_ids = self._model.control_data.get_scope_face_zonelets(
                    scope=part_scope, params=prime.ScopeZoneletParams(model=self._model)
                )
                disp_data = self._parts_polydata[part_id]["faces"]

            if disp_data is not None:
                temp_pd = []
                for disp_mesh in disp_data:
                    if disp_mesh[1].id in disp_ids:
                        temp_pd.append(disp_mesh)
                temp_key = {}
                if len(temp_pd) > 0:
                    temp_key["faces"] = temp_pd
                    scoped_pd[part_id] = temp_key

        # in case the scoped_pd is empty, the mesh must be reinitialized
        # to get the updated changes from the backend
        if len(scoped_pd) == 0:
            self.__init__(self._model)
            return self.get_scoped_polydata(scope, update=True)
        return scoped_pd

    def update_pd(self, part_ids) -> Dict[int, Dict[str, list[(pv.PolyData, Part)]]]:
        """Update the polydata object of the mesh.

        Parameters
        ----------
        part_ids : List[int]
            List of part IDs to update.

        Returns
        -------
        Dict[int, Dict[str, List[(pv.PolyData, Part)]]
            Dictionary with the polydata objects.
        """
        with prime.numpy_array_optimization_enabled():
            facet_result = self.get_face_and_edge_connectivity(
                part_ids, FaceAndEdgeConnectivityParams(model=self._model)
            )
        self._parts_polydata = {}
        for i, part_id in enumerate(facet_result.part_ids):
            part = self._model.get_part(part_id)
            splines = part.get_splines()
            part_polydata = {}
            face_polydata_list = [
                self.get_face_polydata(
                    part_id, facet_result.face_connectivity_result_per_part[i], j
                )
                for j in range(
                    0, len(facet_result.face_connectivity_result_per_part[i].face_zonelet_ids)
                )
            ]

            edge_polydata_list = [
                self.get_edge_polydata(
                    part_id, facet_result.edge_connectivity_result_per_part[i], j
                )
                for j in range(
                    0, len(facet_result.edge_connectivity_result_per_part[i].edge_zonelet_ids)
                )
            ]

            spline_cp_polydata_list = [self.get_spline_cp_polydata(part_ids[i], j) for j in splines]

            spline_surface_polydata_list = [
                self.get_spline_surface_polydata(part_ids[i], j) for j in splines
            ]

            part_polydata["faces"] = face_polydata_list
            part_polydata["edges"] = edge_polydata_list
            part_polydata["ctrlpts"] = spline_cp_polydata_list
            part_polydata["splinesurf"] = spline_surface_polydata_list
            self._parts_polydata[part_id] = part_polydata
        return self._parts_polydata

    def _build_edge_mesh_object(
        self,
        part_id: int,
        edge_res: EdgeConnectivityResults,
        index: int,
    ) -> Optional[MeshObjectPlot]:
        """Build one edge mesh object with Prime identity metadata."""
        part = self._model.get_part(part_id)
        vertices, edge_list = self._get_vertices_and_surf_edges(edge_res, index)
        if vertices.size == 0:
            return None
        lines, n_cells = _edge_lines_from_list(np.asarray(edge_list))
        if n_cells == 0:
            return None

        edge = pv.PolyData()
        edge.points = vertices
        edge.lines = lines
        color = np.array(self.get_edge_color(edge_res, index), dtype=np.uint8)
        edge.cell_data[ENTITY_COLOR_ARRAY] = np.tile(color, (n_cells, 1))

        if edge_res.topo_edge_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOEDGE
            entity_id = int(edge_res.topo_edge_ids[index])
        else:
            display_mesh_type = DisplayMeshType.EDGEZONELET
            entity_id = int(edge_res.edge_zonelet_ids[index])

        zone_ids = getattr(edge_res, "edge_zone_ids", None)
        zone_id = int(zone_ids[index]) if zone_ids is not None and len(zone_ids) > index else 0

        edge.cell_data[PART_ID_ARRAY] = np.full(n_cells, part_id, dtype=np.int64)
        edge.cell_data[ENTITY_ID_ARRAY] = np.full(n_cells, entity_id, dtype=np.int64)
        edge.cell_data[ENTITY_TYPE_ARRAY] = np.full(n_cells, int(display_mesh_type), dtype=np.int16)
        edge.cell_data[ZONE_ID_ARRAY] = np.full(n_cells, zone_id, dtype=np.int64)
        edge.set_active_scalars(ENTITY_COLOR_ARRAY, preference="cell")
        return MeshObjectPlot(part, edge)

    def _build_model_batches_from_connectivity(
        self,
        facet_result,
        entity_filters: Optional[Dict[int, set]] = None,
    ) -> Dict[str, Dict[DisplayMeshType, RenderBatch]]:
        """Build model-wide entity-type batches from connectivity arrays."""
        grouped_raw: Dict[
            DisplayMeshType,
            List[Tuple[np.ndarray, np.ndarray, int, DisplayMeshInfo]],
        ] = defaultdict(list)
        slow_entries = []
        fast_outline_entries = []
        edge_entries = []

        for index, part_id in enumerate(facet_result.part_ids):
            face_res = facet_result.face_connectivity_result_per_part[index]
            edge_res = facet_result.edge_connectivity_result_per_part[index]
            part = self._model.get_part(part_id)
            entity_filter = None if entity_filters is None else entity_filters.get(part_id)

            for face_index in range(len(face_res.face_zonelet_ids)):
                vertices, faces = self._get_vertices_and_surf_faces(face_res, face_index)
                if vertices.size == 0:
                    continue

                has_mesh = True
                if face_res.topo_face_ids[face_index] > 0:
                    display_mesh_type = DisplayMeshType.TOPOFACE
                    entity_id = int(face_res.topo_face_ids[face_index])
                    has_mesh = bool(face_res.mesh_face_ids[face_index] > 0)
                else:
                    display_mesh_type = DisplayMeshType.FACEZONELET
                    entity_id = int(face_res.face_zonelet_ids[face_index])

                if entity_filter is not None and entity_id not in entity_filter:
                    continue

                block = np.asarray(faces)
                n_cells, max_size = _scan_cell_block(block)
                if n_cells == 0:
                    continue

                info = DisplayMeshInfo(
                    id=entity_id,
                    part_id=part_id,
                    zone_id=int(face_res.face_zone_ids[face_index]),
                    display_mesh_type=display_mesh_type,
                    part_name=part.name,
                    zone_name=face_res.face_zone_names[face_index],
                    has_mesh=has_mesh,
                )

                if has_mesh and max_size > 4:
                    slow_entries.append(self.get_face_polydata(part_id, face_res, face_index))
                    continue

                grouped_raw[display_mesh_type].append((vertices, block, n_cells, info))
                if has_mesh:
                    mesh = _assemble_entity_mesh(vertices, block, n_cells, info, 0, lines=False)
                    if mesh is not None:
                        fast_outline_entries.append((MeshObjectPlot(part, mesh), info))

            for edge_index in range(len(edge_res.edge_zonelet_ids)):
                edge_entry = self._build_edge_mesh_object(part_id, edge_res, edge_index)
                if edge_entry is not None:
                    edge_entries.append(edge_entry)

        face_batches = _build_batches_from_raw_faces(grouped_raw)
        if slow_entries:
            slow_batches = build_face_render_batches(
                entry for entry in slow_entries if entry is not None
            )
            face_batches = _merge_render_batch_dicts(face_batches, slow_batches)

        outline_entries = [
            entry for entry in slow_entries if entry is not None
        ] + fast_outline_entries

        return {
            "faces": face_batches,
            "edges": build_edge_render_batches(edge_entries),
            "element_edges": build_element_edge_batches(outline_entries),
        }

    def build_render_data(
        self,
        part_ids: List[int] = None,
        update: bool = False,
    ) -> ModelRenderData:
        """Build merged render geometry for the plotter."""
        if part_ids is None:
            part_ids = [part.id for part in self._model.parts]
        cache_key = frozenset(part_ids)
        if (
            not update
            and self._model_render_data is not None
            and self._render_data_part_ids == cache_key
        ):
            return self._model_render_data

        with prime.numpy_array_optimization_enabled():
            facet_result = self.get_face_and_edge_connectivity(
                part_ids, FaceAndEdgeConnectivityParams(model=self._model)
            )

        batches = self._build_model_batches_from_connectivity(facet_result)
        ctrlpts = []
        splines = []
        for part_id in facet_result.part_ids:
            part = self._model.get_part(part_id)
            for spline_id in part.get_splines():
                ctrlpts.append(self.get_spline_cp_polydata(part_id, spline_id))
                splines.append(self.get_spline_surface_polydata(part_id, spline_id))

        self._model_render_data = ModelRenderData(
            batches=batches,
            ctrlpts=[entry for entry in ctrlpts if entry is not None],
            splines=[entry for entry in splines if entry is not None],
        )
        self._render_data_part_ids = cache_key
        return self._model_render_data

    def get_scoped_render_data(
        self, scope: "prime.ScopeDefinition", update: bool = False
    ) -> ModelRenderData:
        """Build render data for the entities matched by a scope."""
        parts = self._model.control_data.get_scope_parts(scope)
        entity_filters = {}
        for part_id in parts:
            part = self._model.get_part(part_id)
            part_scope = prime.ScopeDefinition(
                model=self._model,
                entity_type=scope.entity_type,
                evaluation_type=scope.evaluation_type,
                part_expression=part.name,
                label_expression=scope.label_expression,
                zone_expression=scope.zone_expression,
            )
            if scope.entity_type != prime.ScopeEntity.FACEZONELETS:
                return self.build_render_data(parts, update=update)
            disp_ids = set(
                self._model.control_data.get_scope_face_zonelets(
                    scope=part_scope,
                    params=prime.ScopeZoneletParams(model=self._model),
                )
            )
            if disp_ids:
                entity_filters[part_id] = disp_ids

        if not entity_filters:
            self.__init__(self._model)
            return self.get_scoped_render_data(scope, update=True)

        with prime.numpy_array_optimization_enabled():
            facet_result = self.get_face_and_edge_connectivity(
                list(entity_filters.keys()),
                FaceAndEdgeConnectivityParams(model=self._model),
            )

        return ModelRenderData(
            batches=self._build_model_batches_from_connectivity(
                facet_result,
                entity_filters=entity_filters,
            )
        )

    def iter_polydata_entries(
        self,
        polydata=None,
        key: str = "faces",
    ):
        """Iterate entries of one geometry category across all parts."""
        source = self.as_polydata() if polydata is None else polydata
        for part_data in source.values():
            for entry in part_data.get(key, []):
                if entry is not None:
                    yield entry

    def get_render_batches(
        self,
        scope: Optional["prime.ScopeDefinition"] = None,
        update: bool = False,
    ) -> Dict[str, Dict[DisplayMeshType, RenderBatch]]:
        """Build model-wide batches suitable for actor-per-type rendering."""
        if scope is None and not update and self._model_render_data is not None:
            return self._model_render_data.batches
        if scope is None:
            return self.build_render_data(update=update).batches

        source = self.get_scoped_polydata(scope, update=update)
        face_entries = list(self.iter_polydata_entries(source, "faces"))
        edge_entries = list(self.iter_polydata_entries(source, "edges"))
        return {
            "faces": build_face_render_batches(face_entries),
            "edges": build_edge_render_batches(edge_entries),
            "element_edges": build_element_edge_batches(face_entries),
        }

    def as_polydata(
        self,
        update: bool = False,
    ) -> Dict[int, Dict[str, List[tuple[pv.PolyData, Part]]]]:
        """Return the mesh as a ``pv.PolyData`` object.

        Parameters
        ----------
        update : bool, default: False
            Update the polydata.

        Returns
        -------
        Dict[int, Dict[str, List[(pv.PolyData, Part)]]
            Dictionary with the polydata objects.
        """
        if not self._parts_polydata or update:
            part_ids = [part.id for part in self._model.parts]
            self.update_pd(part_ids)
        return self._parts_polydata

    @property
    def id(self):
        """Return the ID of the mesh.

        Returns
        -------
        int
            ID of the mesh.
        """
        return self._id

    @property
    def part_id(self):
        """Return the part ID of the mesh.

        Returns
        -------
        int
            Part ID of the mesh.
        """
        return self._part_id

    @property
    def zone_id(self):
        """Return the zone ID of the mesh.

        Returns
        -------
        int
            Zone ID of the mesh.
        """
        return self._zone_id


class FaceGeometry:
    """Intermediate DTO for face geometry extracted from connectivity results.

    Parameters
    ----------
    points : np.ndarray
        Array of vertex coordinates (N, 3).
    face_vertex_indices : np.ndarray
        Flattened array of vertex indices for all faces.
    face_vertex_counts : np.ndarray
        Number of vertices per face.
    color : list
        RGB color [0-255] for this geometry.
    part_id : int
        ID of the part this geometry belongs to.
    zone_id : int
        ID of the zone.
    zone_name : str
        Name of the zone.
    mesh_id : int
        Mesh/zonelet ID.
    display_mesh_type : DisplayMeshType
        Type of mesh entity.
    has_mesh : bool
        Whether this face has actual mesh elements.
    """

    def __init__(
        self,
        points,
        face_vertex_indices,
        face_vertex_counts,
        color,
        part_id,
        zone_id,
        zone_name,
        mesh_id,
        display_mesh_type,
        has_mesh,
    ):
        """Initialize face geometry."""
        self.points = points
        self.face_vertex_indices = face_vertex_indices
        self.face_vertex_counts = face_vertex_counts
        self.color = color
        self.part_id = part_id
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.mesh_id = mesh_id
        self.display_mesh_type = display_mesh_type
        self.has_mesh = has_mesh


class EdgeGeometry:
    """Intermediate DTO for edge geometry extracted from connectivity results.

    Parameters
    ----------
    points : np.ndarray
        Array of vertex coordinates (N, 3).
    edge_vertex_indices : np.ndarray
        Flattened array of vertex indices for all edges.
    edge_vertex_counts : np.ndarray
        Number of vertices per edge.
    color : list
        RGB color [0-255] for this geometry.
    part_id : int
        ID of the part this geometry belongs to.
    mesh_id : int
        Edge zonelet ID.
    display_mesh_type : DisplayMeshType
        Type of mesh entity (typically EDGEZONELET or TOPOEDGE).
    """

    def __init__(
        self,
        points,
        edge_vertex_indices,
        edge_vertex_counts,
        color,
        part_id,
        mesh_id,
        display_mesh_type,
    ):
        """Initialize edge geometry."""
        self.points = points
        self.edge_vertex_indices = edge_vertex_indices
        self.edge_vertex_counts = edge_vertex_counts
        self.color = color
        self.part_id = part_id
        self.mesh_id = mesh_id
        self.display_mesh_type = display_mesh_type


class SplineGeometry:
    """Intermediate DTO for spline geometry (control points or surface).

    Parameters
    ----------
    points : np.ndarray
        Array of control/spline point coordinates (N, 3).
    color : list
        RGB color [0-255].
    part_id : int
        ID of the part.
    spline_id : int
        ID of the spline.
    geom_type : DisplayMeshType
        Either SPLINECONTROLPOINTS or SPLINESURFACE.
    """

    def __init__(self, points, color, part_id, spline_id, geom_type):
        """Initialize spline geometry."""
        self.points = points
        self.color = color
        self.part_id = part_id
        self.spline_id = spline_id
        self.geom_type = geom_type


class MeshUSD(MeshInfo):
    """Processes the mesh for USD export and serialization.

    This class reads from the same connectivity source as Mesh but outputs
    OpenUSD geometry instead of PyVista PolyData. It provides parallel APIs
    for exporting to USD stages.

    Parameters
    ----------
    model : CommunicationManager
        Model to process.
    """

    def __init__(self, model: CommunicationManager):
        """Initialize the USD mesh object."""
        super().__init__(model)
        self._model = model
        self._unfreeze()
        self._parts_usd_geom = {}
        self._freeze()

    @property
    def model(self):
        """Model."""
        return self._model

    def _extract_face_geometry(
        self, part_id: int, face_facet_res: FaceConnectivityResults, index: int
    ) -> FaceGeometry:
        """Extract face geometry from connectivity results.

        Parameters
        ----------
        part_id : int
            ID of the part.
        face_facet_res : FaceConnectivityResults
            Face connectivity results.
        index : int
            Index of the face zonelet.

        Returns
        -------
        FaceGeometry
            Extracted face geometry DTO.
        """
        part = self._model.get_part(part_id)
        vertices, faces = self._get_vertices_and_surf_faces(face_facet_res, index)

        # Convert VTK-style packed face list to USD format
        face_vertex_counts = []
        face_vertex_indices = []
        i = 0
        while i < len(faces):
            count = int(faces[i])
            face_vertex_counts.append(count)
            for j in range(1, count + 1):
                face_vertex_indices.append(int(faces[i + j]))
            i += count + 1

        fcolor = np.array(self.get_face_color(part, ColorByType.ZONE))
        color = fcolor.tolist()

        has_mesh = True
        if face_facet_res.topo_face_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOFACE
            mesh_id = face_facet_res.topo_face_ids[index]
            has_mesh = bool(face_facet_res.mesh_face_ids[index] > 0)
        else:
            display_mesh_type = DisplayMeshType.FACEZONELET
            mesh_id = face_facet_res.face_zonelet_ids[index]

        return FaceGeometry(
            points=vertices,
            face_vertex_indices=np.array(face_vertex_indices, dtype=np.uint32),
            face_vertex_counts=np.array(face_vertex_counts, dtype=np.uint32),
            color=color,
            part_id=part_id,
            zone_id=face_facet_res.face_zone_ids[index],
            zone_name=face_facet_res.face_zone_names[index],
            mesh_id=mesh_id,
            display_mesh_type=display_mesh_type,
            has_mesh=has_mesh,
        )

    def _extract_edge_geometry(
        self, part_id: int, edge_facet_res: EdgeConnectivityResults, index: int
    ) -> EdgeGeometry:
        """Extract edge geometry from connectivity results.

        Parameters
        ----------
        part_id : int
            ID of the part.
        edge_facet_res : EdgeConnectivityResults
            Edge connectivity results.
        index : int
            Index of the edge zonelet.

        Returns
        -------
        EdgeGeometry
            Extracted edge geometry DTO.
        """
        vertices, edges = self._get_vertices_and_surf_edges(edge_facet_res, index)

        # Convert edge list to USD format
        edge_vertex_counts = []
        edge_vertex_indices = []
        i = 0
        while i < len(edges):
            count = int(edges[i])
            edge_vertex_counts.append(count)
            for j in range(1, count + 1):
                edge_vertex_indices.append(int(edges[i + j]))
            i += count + 1

        ecolor = np.array(self.get_edge_color(edge_facet_res, index))
        color = ecolor.tolist()

        mesh_type = DisplayMeshType.EDGEZONELET
        if edge_facet_res.topo_edge_ids[index] > 0:
            mesh_type = DisplayMeshType.TOPOEDGE

        return EdgeGeometry(
            points=vertices,
            edge_vertex_indices=np.array(edge_vertex_indices, dtype=np.uint32),
            edge_vertex_counts=np.array(edge_vertex_counts, dtype=np.uint32),
            color=color,
            part_id=part_id,
            mesh_id=edge_facet_res.edge_zonelet_ids[index],
            display_mesh_type=mesh_type,
        )

    def _extract_spline_geometry(
        self, part_id: int, spline_id: int, geom_type: DisplayMeshType
    ) -> SplineGeometry:
        """Extract spline geometry (control points or surface).

        Parameters
        ----------
        part_id : int
            ID of the part.
        spline_id : int
            ID of the spline.
        geom_type : DisplayMeshType
            Type of spline geometry (SPLINECONTROLPOINTS or SPLINESURFACE).

        Returns
        -------
        SplineGeometry
            Extracted spline geometry DTO.
        """
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)

        if geom_type == DisplayMeshType.SPLINECONTROLPOINTS:
            points = spline.control_points
            color = [0, 0, 255]
        else:
            points = spline.spline_points
            color = color_matrix[1].tolist()

        return SplineGeometry(
            points=np.array(points),
            color=color,
            part_id=part_id,
            spline_id=spline_id,
            geom_type=geom_type,
        )

    def get_face_color(self, part: Part, model_type: ColorByType = ColorByType.ZONE):
        """Get the colors of faces (same logic as Mesh).

        Returns
        -------
        List
            List of colors for faces.
        """
        num_colors = int(color_matrix.size / 3)
        return color_matrix[part.id % num_colors].tolist()

    def get_edge_color(self, edge_results: EdgeConnectivityResults, index: int):
        """Get the colors of edges (same logic as Mesh).

        Returns
        -------
        List
            List of colors for edges.
        """
        mesh_type = DisplayMeshType.EDGEZONELET
        if edge_results.topo_edge_ids[index] > 0:
            mesh_type = DisplayMeshType.TOPOEDGE
        num_colors = int(color_matrix.size / 3)
        if mesh_type == DisplayMeshType.EDGEZONELET:
            return color_matrix[index % num_colors].tolist()
        elif mesh_type == DisplayMeshType.TOPOEDGE:
            if edge_results.topo_edge_types[index] == 1:
                return [255, 0, 0]
            elif edge_results.topo_edge_types[index] == 2:
                return [0, 0, 0]
            elif edge_results.topo_edge_types[index] == 3:
                return [0, 255, 255]
            elif edge_results.topo_edge_types[index] == 4:
                return [255, 0, 255]
            elif edge_results.topo_edge_types[index] == 5:
                return [255, 255, 0]
            elif edge_results.topo_edge_types[index] == 6:
                return [128, 0, 128]
            else:
                return color_matrix[edge_results.id % num_colors].tolist()

    def _get_vertices_and_surf_faces(
        self, connectivity_results: FaceConnectivityResults, index
    ) -> Union[np.ndarray, np.ndarray]:
        """Calculate the vertices and faces of the mesh.

        Parameters
        ----------
        connectivity_results : FaceConnectivityResults
            Results of the connectivity operations.
        index : int
            Index of the mesh.

        Returns
        -------
        Union[np.ndarray, np.ndarray]
            Vertices and faces of the mesh.
        """
        node_start = 3 * np.sum(connectivity_results.num_nodes_per_face_zonelet[0:index])
        num_node_coords = 3 * connectivity_results.num_nodes_per_face_zonelet[index]
        face_list_start = np.sum(connectivity_results.num_face_list_per_face_zonelet[0:index])
        num_face_list = connectivity_results.num_face_list_per_face_zonelet[index]
        vertices = connectivity_results.node_coords[
            node_start : node_start + num_node_coords
        ].reshape((-1, 3))
        faces = connectivity_results.face_list[face_list_start : face_list_start + num_face_list]
        return vertices, faces

    def _get_vertices_and_surf_edges(
        self, connectivity_results: EdgeConnectivityResults, index: int
    ) -> Union[np.ndarray, np.ndarray]:
        """Calculate the vertices and edges of the mesh.

        Parameters
        ----------
        connectivity_results : EdgeConnectivityResults
            Results of the connectivity operations.
        index : int
            Index of the mesh.

        Returns
        -------
        Union[np.ndarray, np.ndarray]
            Vertices and edges of the mesh.
        """
        node_start = 3 * np.sum(connectivity_results.num_nodes_per_edge_zonelet[0:index])
        num_node_coords = 3 * connectivity_results.num_nodes_per_edge_zonelet[index]
        edge_list_start = np.sum(connectivity_results.num_edge_list_per_edge_zonelet[0:index])
        num_edge_list = connectivity_results.num_edge_list_per_edge_zonelet[index]
        vertices = connectivity_results.node_coords[
            node_start : node_start + num_node_coords
        ].reshape((-1, 3))
        edges = connectivity_results.edge_list[edge_list_start : edge_list_start + num_edge_list]
        return vertices, edges

    def update_usd(self, part_ids: List[int]) -> Dict[int, Dict[str, list]]:
        """Update the USD geometry for the given parts.

        Parameters
        ----------
        part_ids : List[int]
            List of part IDs to update.

        Returns
        -------
        Dict[int, Dict[str, list]]
            Dictionary mapping part_id -> {"faces": [...], "edges": [...],
            "ctrlpts": [...], "splinesurf": [...]}
        """
        with prime.numpy_array_optimization_enabled():
            facet_result = self.get_face_and_edge_connectivity(
                part_ids, FaceAndEdgeConnectivityParams(model=self._model)
            )
        self._parts_usd_geom = {}
        for i, part_id in enumerate(facet_result.part_ids):
            part = self._model.get_part(part_id)
            splines = part.get_splines()
            part_usd_geom = {}

            face_geom_list = [
                self._extract_face_geometry(
                    part_id, facet_result.face_connectivity_result_per_part[i], j
                )
                for j in range(
                    0, len(facet_result.face_connectivity_result_per_part[i].face_zonelet_ids)
                )
            ]

            edge_geom_list = [
                self._extract_edge_geometry(
                    part_id, facet_result.edge_connectivity_result_per_part[i], j
                )
                for j in range(
                    0, len(facet_result.edge_connectivity_result_per_part[i].edge_zonelet_ids)
                )
            ]

            spline_cp_geom_list = [
                self._extract_spline_geometry(
                    part_id, spline_id, DisplayMeshType.SPLINECONTROLPOINTS
                )
                for spline_id in splines
            ]

            spline_surface_geom_list = [
                self._extract_spline_geometry(part_id, spline_id, DisplayMeshType.SPLINESURFACE)
                for spline_id in splines
            ]

            part_usd_geom["faces"] = face_geom_list
            part_usd_geom["edges"] = edge_geom_list
            part_usd_geom["ctrlpts"] = spline_cp_geom_list
            part_usd_geom["splinesurf"] = spline_surface_geom_list
            self._parts_usd_geom[part_id] = part_usd_geom

        return self._parts_usd_geom

    def as_usd(self, update: bool = False) -> Dict[int, Dict[str, list]]:
        """Return the mesh as USD geometry DTOs.

        Parameters
        ----------
        update : bool, default: False
            Update the USD geometry.

        Returns
        -------
        Dict[int, Dict[str, list]]
            Dictionary mapping part_id -> {"faces": [...], "edges": [...],
            "ctrlpts": [...], "splinesurf": [...]}
        """
        if not self._parts_usd_geom or update:
            part_ids = [part.id for part in self._model.parts]
            self.update_usd(part_ids)
        return self._parts_usd_geom

    def get_scoped_usd(self, scope: "prime.ScopeDefinition", update: bool = False):
        """Get the USD geometry for a scoped mesh.

        Parameters
        ----------
        scope : prime.ScopeDefinition
            Scope to get the mesh from.
        update : bool, default: False
            Update the USD geometry.

        Returns
        -------
        Dict[int, Dict[str, list]]
            Dictionary mapping part_id -> {"faces": [...], "edges": [...], ...}
        """
        self.as_usd(update=update)
        parts = self._model.control_data.get_scope_parts(scope)

        if len(set(parts).intersection(set(self._parts_usd_geom.keys()))) != len(parts):
            self.update_usd(parts)

        scoped_usd = {}
        for part_id in parts:
            part = self._model.get_part(part_id)
            part_scope = prime.ScopeDefinition(
                model=self._model,
                entity_type=scope.entity_type,
                evaluation_type=scope.evaluation_type,
                part_expression=part.name,
                label_expression=scope.label_expression,
                zone_expression=scope.zone_expression,
            )
            disp_data = None
            disp_ids = []
            if scope.entity_type == prime.ScopeEntity.FACEZONELETS:
                disp_ids = self._model.control_data.get_scope_face_zonelets(
                    scope=part_scope, params=prime.ScopeZoneletParams(model=self._model)
                )
                disp_data = self._parts_usd_geom[part_id]["faces"]

            if disp_data is not None:
                temp_geom = []
                for geom in disp_data:
                    if geom.mesh_id in disp_ids:
                        temp_geom.append(geom)
                temp_key = {}
                if len(temp_geom) > 0:
                    temp_key["faces"] = temp_geom
                    scoped_usd[part_id] = temp_key

        if len(scoped_usd) == 0:
            self.__init__(self._model)
            return self.get_scoped_usd(scope, update=True)

        return scoped_usd
