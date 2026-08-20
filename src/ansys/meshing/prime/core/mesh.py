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
from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

import numpy as np
import pyvista as pv
from ansys.tools.visualization_interface import MeshObjectPlot

import ansys.meshing.prime as prime
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.autogen.meshinfo import MeshInfo
from ansys.meshing.prime.autogen.meshinfostructs import (
    EdgeConnectivityResults,
    FaceAndEdgeConnectivityParams,
    FaceConnectivityResults,
)
from ansys.meshing.prime.core.part import Part


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
    """Uniquely identify one displayed Prime entity.

    Parameters
    ----------
    part_id : int
        ID of the owning Prime part.
    display_mesh_type : DisplayMeshType
        Display entity classification.
    entity_id : int
        Original Prime entity ID.
    """

    part_id: int
    display_mesh_type: DisplayMeshType
    entity_id: int


#: Internal ID that uniquely identifies one rendered Prime entity within one batch.
#:
#: This value is deliberately different from the Prime entity ID. Prime entity IDs
#: are not assumed to be globally unique across parts or display entity types.
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
    """Contain information about one displayed Prime entity.

    Parameters
    ----------
    id : int, default: 0
        Original Prime entity ID.
    part_id : int, default: 0
        ID of the owning part.
    part_name : str, optional
        Name of the owning part.
    zone_id : int, default: 0
        ID of the owning zone.
    zone_name : str, optional
        Name of the owning zone.
    display_mesh_type : DisplayMeshType, default: DisplayMeshType.FACEZONELET
        Type of displayed entity.
    has_mesh : bool, default: False
        Whether the displayed topology entity has mesh elements.
    render_mesh : pv.PolyData, optional
        Explicit triangulation used for shaded rendering.
    element_edges : pv.PolyData, optional
        Explicit element-edge geometry.
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
    """Contain geometry for one persistent actor.

    A render batch spans all parts contributing the same display entity type.
    It therefore creates one actor per entity type rather than one actor per
    part or one actor per Prime entity.

    Entity ownership is retained in cell-data arrays so that picking remains
    capable of resolving the original part, zone, and Prime entity.

    Parameters
    ----------
    mesh : pv.PolyData
        Merged geometry.
    infos : Mapping[int, DisplayMeshInfo]
        Display information keyed by the batch-local render entity ID.
    display_mesh_type : DisplayMeshType
        Entity type represented by this batch.
    pickable : bool, default: True
        Whether the resulting actor should participate in picking.
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
                "The render batch is missing required cell arrays: "
                + ", ".join(missing)
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
            raise ValueError(
                "A render batch may contain only one DisplayMeshType."
            )

    @property
    def render_entity_ids(self) -> np.ndarray:
        """Return the batch-local render entity ID of every cell."""
        return np.asarray(
            self.mesh.cell_data[RENDER_ENTITY_ID_ARRAY],
            dtype=np.int64,
        )

    @property
    def entity_ids(self) -> np.ndarray:
        """Return the original Prime entity ID of every cell."""
        return np.asarray(
            self.mesh.cell_data[ENTITY_ID_ARRAY],
            dtype=np.int64,
        )

    @property
    def part_ids(self) -> np.ndarray:
        """Return the Prime part ID of every cell."""
        return np.asarray(
            self.mesh.cell_data[PART_ID_ARRAY],
            dtype=np.int64,
        )

    def info_for_render_id(self, render_entity_id: int) -> DisplayMeshInfo:
        """Return display information for a batch-local render entity ID."""
        return self.infos[int(render_entity_id)]

    def apply_colors(
        self,
        color_type: Optional[ColorByType] = None,
    ) -> None:
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
    """Compute per-cell colors for a merged entity-type mesh.

    Parameters
    ----------
    infos : Mapping[int, DisplayMeshInfo]
        Display information keyed by batch-local render entity ID.
    render_entity_ids : np.ndarray
        Batch-local render entity ID for every rendered cell.
    color_type : ColorByType, optional
        Property from which colors are derived.

    Returns
    -------
    np.ndarray
        Unsigned 8-bit RGB value for every rendered cell.
    """
    render_entity_ids = np.asarray(
        render_entity_ids,
        dtype=np.int64,
    )

    if render_entity_ids.size == 0:
        return np.empty((0, 3), dtype=np.uint8)

    unique_ids, inverse = np.unique(
        render_entity_ids,
        return_inverse=True,
    )

    missing = [
        int(render_id)
        for render_id in unique_ids
        if int(render_id) not in infos
    ]
    if missing:
        raise KeyError(
            "No DisplayMeshInfo exists for render entity IDs "
            f"{missing}."
        )

    palette = np.asarray(
        [
            entity_color(infos[int(render_id)], color_type)
            for render_id in unique_ids
        ],
        dtype=np.uint8,
    )

    return palette[inverse]


def _as_polydata(mesh: "pv.DataSet") -> "pv.PolyData":
    """Return render geometry as PolyData without merging points."""
    if isinstance(mesh, pv.PolyData):
        return mesh.copy(deep=False)

    return mesh.extract_surface(
        nonlinear_subdivision=0,
        progress_bar=False,
    )


def _attach_entity_metadata(
    mesh: "pv.PolyData",
    info: DisplayMeshInfo,
    render_entity_id: int,
) -> "pv.PolyData":
    """Attach Prime ownership metadata to every cell of a geometry piece."""
    output = _as_polydata(mesh)

    number_of_cells = output.n_cells
    output.cell_data[RENDER_ENTITY_ID_ARRAY] = np.full(
        number_of_cells,
        int(render_entity_id),
        dtype=np.int64,
    )
    output.cell_data[PART_ID_ARRAY] = np.full(
        number_of_cells,
        info.part_id,
        dtype=np.int64,
    )
    output.cell_data[ENTITY_ID_ARRAY] = np.full(
        number_of_cells,
        info.id,
        dtype=np.int64,
    )
    output.cell_data[ENTITY_TYPE_ARRAY] = np.full(
        number_of_cells,
        int(info.display_mesh_type),
        dtype=np.int16,
    )
    output.cell_data[ZONE_ID_ARRAY] = np.full(
        number_of_cells,
        info.zone_id,
        dtype=np.int64,
    )

    return output


def _validate_merged_metadata(mesh: "pv.PolyData") -> None:
    """Ensure a merge has preserved all picking arrays."""
    missing = [
        array_name
        for array_name in REQUIRED_PICKING_ARRAYS
        if array_name not in mesh.cell_data
    ]
    if missing:
        raise RuntimeError(
            "PyVista discarded required Prime picking metadata while "
            "merging geometry: "
            + ", ".join(missing)
        )

    for array_name in REQUIRED_PICKING_ARRAYS:
        if len(mesh.cell_data[array_name]) != mesh.n_cells:
            raise RuntimeError(
                f"Cell array {array_name!r} does not match the merged "
                "cell count."
            )


def resolve_picked_entity(
    batch: RenderBatch,
    cell_id: int,
) -> DisplayMeshInfo:
    """Resolve a picked render cell to its Prime display entity.

    Parameters
    ----------
    batch : RenderBatch
        Batch containing the picked cell.
    cell_id : int
        Cell index returned by the picker.

    Returns
    -------
    DisplayMeshInfo
        Information for the owning Prime entity.
    """
    if cell_id < 0 or cell_id >= batch.mesh.n_cells:
        raise IndexError(
            f"Picked cell ID {cell_id} is outside a mesh containing "
            f"{batch.mesh.n_cells} cells."
        )

    render_entity_id = int(
        batch.mesh.cell_data[RENDER_ENTITY_ID_ARRAY][cell_id]
    )
    return batch.info_for_render_id(render_entity_id)


def selected_entity_keys(
    mesh: "pv.DataSet",
) -> set:
    """Return unique Prime entity keys represented by selected cells."""
    if mesh is None or mesh.n_cells == 0:
        return set()

    required = (
        PART_ID_ARRAY,
        ENTITY_ID_ARRAY,
        ENTITY_TYPE_ARRAY,
    )
    missing = [
        name for name in required if name not in mesh.cell_data
    ]
    if missing:
        raise ValueError(
            "Selected geometry is missing Prime ownership arrays: "
            + ", ".join(missing)
        )

    part_ids = np.asarray(mesh.cell_data[PART_ID_ARRAY])
    entity_ids = np.asarray(mesh.cell_data[ENTITY_ID_ARRAY])
    entity_types = np.asarray(mesh.cell_data[ENTITY_TYPE_ARRAY])

    return {
        DisplayEntityKey(
            part_id=int(part_id),
            display_mesh_type=DisplayMeshType(int(entity_type)),
            entity_id=int(entity_id),
        )
        for part_id, entity_type, entity_id in zip(
            part_ids,
            entity_types,
            entity_ids,
        )
    }


def build_face_render_batches(
    face_entries: Iterable,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build one face actor batch per display entity type.

    Entries may originate from any number of parts. Geometry is grouped only
    by :class:`DisplayMeshType`, which makes actor count independent of part
    count.

    Parameters
    ----------
    face_entries : Iterable
        ``(MeshObjectPlot, DisplayMeshInfo)`` pairs from all included parts.

    Returns
    -------
    Dict[DisplayMeshType, RenderBatch]
        At most one batch for each face display entity type.
    """
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)

    for entry in face_entries:
        if entry is None:
            continue

        mesh_object, info = entry
        geometry = (
            info.render_mesh
            if info.render_mesh is not None
            else mesh_object.mesh
        )

        if geometry is None or geometry.n_cells == 0:
            continue

        grouped[info.display_mesh_type].append(
            (geometry, info)
        )

    batches: Dict[DisplayMeshType, RenderBatch] = {}

    for display_mesh_type, items in grouped.items():
        infos: Dict[int, DisplayMeshInfo] = {}
        pieces: List[pv.PolyData] = []

        for render_entity_id, (geometry, info) in enumerate(items):
            infos[render_entity_id] = info
            pieces.append(
                _attach_entity_metadata(
                    geometry,
                    info,
                    render_entity_id,
                )
            )

        merged = _merge_geometry(pieces)
        if merged is None:
            continue

        _validate_merged_metadata(merged)

        batch = RenderBatch(
            mesh=merged,
            infos=infos,
            display_mesh_type=display_mesh_type,
            pickable=True,
        )
        batch.apply_colors()
        batches[display_mesh_type] = batch

    return batches


def build_element_edge_batches(
    face_entries: Iterable,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build one element-outline batch per owning face entity type.

    Explicit stored outlines are used when available. Otherwise, outlines are
    extracted from meshed face geometry.

    Parameters
    ----------
    face_entries : Iterable
        ``(MeshObjectPlot, DisplayMeshInfo)`` pairs from all included parts.

    Returns
    -------
    Dict[DisplayMeshType, RenderBatch]
        Element-outline batches grouped by owning face entity type.
    """
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)

    for entry in face_entries:
        if entry is None:
            continue

        mesh_object, info = entry
        if not info.has_mesh:
            continue

        if info.element_edges is not None:
            outlines = info.element_edges
        elif mesh_object.mesh is not None:
            outlines = mesh_object.mesh.extract_all_edges(
                progress_bar=False
            )
        else:
            outlines = None

        if outlines is None or outlines.n_cells == 0:
            continue

        grouped[info.display_mesh_type].append(
            (outlines, info)
        )

    batches: Dict[DisplayMeshType, RenderBatch] = {}

    for display_mesh_type, items in grouped.items():
        infos: Dict[int, DisplayMeshInfo] = {}
        pieces: List[pv.PolyData] = []

        for render_entity_id, (geometry, info) in enumerate(items):
            infos[render_entity_id] = info
            pieces.append(
                _attach_entity_metadata(
                    geometry,
                    info,
                    render_entity_id,
                )
            )

        merged = _merge_geometry(pieces)
        if merged is None:
            continue

        _validate_merged_metadata(merged)

        batches[display_mesh_type] = RenderBatch(
            mesh=merged,
            infos=infos,
            display_mesh_type=display_mesh_type,
            pickable=False,
        )

    return batches


def build_element_edge_mesh(face_entries: Iterable) -> "pv.PolyData":
    """Return all element outlines as one compatibility mesh.

    This compatibility wrapper can be removed after plotter callers have been
    converted to :func:`build_element_edge_batches`.
    """
    batches = build_element_edge_batches(face_entries)
    meshes = [batch.mesh for batch in batches.values()]
    return _merge_geometry(meshes)


def build_edge_render_batches(
    edge_entries: Iterable,
) -> Dict[DisplayMeshType, RenderBatch]:
    """Build one persistent edge batch per edge display entity type.

    Each entry may be either a ``MeshObjectPlot`` for backward compatibility
    or a ``(MeshObjectPlot, DisplayMeshInfo)`` pair. Entries without display
    information are rendered but cannot resolve a Prime edge entity when
    picked.

    Parameters
    ----------
    edge_entries : Iterable
        Edge plot objects or ``(MeshObjectPlot, DisplayMeshInfo)`` pairs.

    Returns
    -------
    Dict[DisplayMeshType, RenderBatch]
        Edge batches grouped by display entity type.
    """
    grouped: Dict[
        DisplayMeshType,
        List[Tuple["pv.PolyData", DisplayMeshInfo]],
    ] = defaultdict(list)

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

        if info is None:
            part = mesh_object.custom_object
            info = DisplayMeshInfo(
                id=-1,
                part_id=part.id,
                part_name=getattr(part, "name", None),
                display_mesh_type=DisplayMeshType.EDGEZONELET,
            )

        grouped[info.display_mesh_type].append(
            (geometry, info)
        )

    batches: Dict[DisplayMeshType, RenderBatch] = {}

    for display_mesh_type, items in grouped.items():
        infos: Dict[int, DisplayMeshInfo] = {}
        pieces: List[pv.PolyData] = []

        for render_entity_id, (geometry, info) in enumerate(items):
            infos[render_entity_id] = info
            pieces.append(
                _attach_entity_metadata(
                    geometry,
                    info,
                    render_entity_id,
                )
            )

        merged = _merge_geometry(pieces)
        if merged is None:
            continue

        _validate_merged_metadata(merged)

        batch = RenderBatch(
            mesh=merged,
            infos=infos,
            display_mesh_type=display_mesh_type,
            pickable=False,
        )

        # Edge pieces already carry their type-specific RGB colors.
        if ENTITY_COLOR_ARRAY in merged.cell_data:
            merged.set_active_scalars(
                ENTITY_COLOR_ARRAY,
                preference="cell",
            )

        batches[display_mesh_type] = batch

    return batches


def build_edge_render_mesh(edge_entries: Iterable) -> "pv.PolyData":
    """Return all edge batches as a compatibility mesh."""
    batches = build_edge_render_batches(edge_entries)
    return _merge_geometry(
        [batch.mesh for batch in batches.values()]
    )


def _merge_geometry(
    pieces: Sequence["pv.PolyData"],
) -> Optional["pv.PolyData"]:
    """Concatenate geometry without merging points.

    Cell order and cell-data arrays are preserved. This is necessary because
    picking metadata is attached before the pieces are merged.

    Parameters
    ----------
    pieces : Sequence[pv.PolyData]
        Geometry pieces to concatenate.

    Returns
    -------
    pv.PolyData or None
        Concatenated geometry, or ``None`` for an empty input.
    """
    valid_pieces = [
        _as_polydata(piece)
        for piece in pieces
        if piece is not None and piece.n_cells > 0
    ]

    if not valid_pieces:
        return None

    if len(valid_pieces) == 1:
        return valid_pieces[0].copy(deep=False)

    merged = pv.merge(
        valid_pieces,
        merge_points=False,
    )

    if not isinstance(merged, pv.PolyData):
        merged = merged.extract_surface(
            nonlinear_subdivision=0,
            progress_bar=False,
        )

    return merged


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
        if segments:
            edge.set_active_scalars(ENTITY_COLOR_ARRAY, preference="cell")
        if edge.n_points > 0:
            if edge_facet_res.topo_edge_ids[index] > 0:
                display_mesh_type = DisplayMeshType.TOPOEDGE
                entity_id = edge_facet_res.topo_edge_ids[index]
            else:
                display_mesh_type = DisplayMeshType.EDGEZONELET
                entity_id = edge_facet_res.edge_zonelet_ids[index]
        
            zone_ids = getattr(edge_facet_res, "edge_zone_ids", None)
            zone_names = getattr(edge_facet_res, "edge_zone_names", None)
        
            zone_id = (
                int(zone_ids[index])
                if zone_ids is not None and len(zone_ids) > index
                else 0
            )
            zone_name = (
                zone_names[index]
                if zone_names is not None and len(zone_names) > index
                else None
            )
        
            return MeshObjectPlot(part, edge), DisplayMeshInfo(
                id=entity_id,
                part_id=part_id,
                part_name=part.name,
                zone_id=zone_id,
                zone_name=zone_name,
                display_mesh_type=display_mesh_type,
                has_mesh=False,
            )

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
        faces = compute_face_list_from_structured_nodes(dim)
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
        faces = compute_face_list_from_structured_nodes(dim)
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

    def iter_polydata_entries(
        self,
        polydata=None,
        key: str = "faces",
    ):
        """Iterate entries of one geometry category across all parts.

        Parameters
        ----------
        polydata : dict, optional
            Part-organized data returned by :meth:`as_polydata` or
            :meth:`get_scoped_polydata`. The complete model is used when
            omitted.
        key : str, default: "faces"
            Geometry category to iterate.

        Yields
        ------
        object
            Individual stored plot entry.
        """
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
        """Build model-wide batches suitable for actor-per-type rendering.

        Parameters
        ----------
        scope : prime.ScopeDefinition, optional
            Scope restricting the displayed entities.
        update : bool, default: False
            Refresh connectivity before building batches.

        Returns
        -------
        Dict[str, Dict[DisplayMeshType, RenderBatch]]
            Face, edge, and element-outline batches.
        """
        if scope is None:
            source = self.as_polydata(update=update)
        else:
            source = self.get_scoped_polydata(
                scope,
                update=update,
            )

        face_entries = list(
            self.iter_polydata_entries(source, "faces")
        )
        edge_entries = list(
            self.iter_polydata_entries(source, "edges")
        )

        return {
            "faces": build_face_render_batches(face_entries),
            "edges": build_edge_render_batches(edge_entries),
            "element_edges": build_element_edge_batches(
                face_entries
            ),
        }

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
        scope_def = scope
        for part_id in parts:
            part = self._model.get_part(part_id)
            scope_def.part_expression = part.name
            disp_data = None
            disp_ids = []
            if scope.entity_type == prime.ScopeEntity.FACEZONELETS:
                disp_ids = self._model.control_data.get_scope_face_zonelets(
                    scope=scope_def, params=prime.ScopeZoneletParams(model=self._model)
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
