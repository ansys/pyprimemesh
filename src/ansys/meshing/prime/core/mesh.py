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
from typing import Dict, List, Union

import numpy as np
import pyvista as pv
from ansys.tools.visualization_interface import MeshObjectPlot

import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.coreobject import CommunicationManager
from ansys.meshing.prime.autogen.meshinfo import MeshInfo
from ansys.meshing.prime.autogen.meshinfostructs import (
    EdgeConnectivityResults,
    FaceAndEdgeConnectivityParams,
    FaceConnectivityResults,
)
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import CommunicationManager


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
    ) -> None:
        """Initialize display mesh information."""
        self.id = id
        self.part_id = part_id
        self.zone_id = zone_id
        self.part_name = part_name
        self.zone_name = zone_name
        self.display_mesh_type = display_mesh_type
        self.has_mesh = has_mesh


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

        if surf.n_points > 0:
            return MeshObjectPlot(part, surf), DisplayMeshInfo(
                id=id,
                part_id=part_id,
                zone_id=face_facet_res.face_zone_ids[index],
                display_mesh_type=display_mesh_type,
                part_name=part.name,
                zone_name=face_facet_res.face_zone_names[index],
                has_mesh=has_mesh,
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
        n_edges = edge_facet_res.num_edges_per_edge_zonelet[index]
        edge.points = vertices
        cells = np.full((n_edges, 3), 2, dtype=np.int_)
        i = 0
        j = 0
        while j < len(faces):
            nnodes = faces[j]
            j += 1
            cells[i, 1] = faces[j]
            if nnodes == 2:
                cells[i, 2] = faces[j + 1]
            elif nnodes == 3:
                cells[i, 2] = faces[j + 2]
            j += nnodes
            i += 1
        edge.lines = cells
        ecolor = np.array(self.get_edge_color(edge_facet_res, index))
        colors = np.tile(ecolor, (n_edges, 1))
        edge["colors"] = colors
        if edge.n_points > 0:
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
