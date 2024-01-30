"""Process the mesh for visualization in the GUI."""

import enum

import numpy as np
import pyvista as pv

from ansys.meshing.prime.autogen.coreobject import CommunicationManager
from ansys.meshing.prime.autogen.meshinfo import MeshInfo
from ansys.meshing.prime.autogen.meshinfostructs import (
    EdgeConnectivityResults,
    FaceAndEdgeConnectivityParams,
    FaceConnectivityResults,
)
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


class Mesh(MeshInfo):
    def __init__(self, model: CommunicationManager):
        super().__init__(model)
        self._model = model

    @property
    def model(self):
        return self._model

    def get_face_color(self, model_type: ColorByType):
        """Get the colors of faces.

        Returns
        -------
        List
            List of colors for faces.
        """
        num_colors = int(color_matrix.size / 3)
        if model_type == ColorByType.ZONELET:
            return color_matrix[self._id % num_colors].tolist()
        elif model_type == ColorByType.PART:
            return color_matrix[self._part_id % num_colors].tolist()
        else:
            return color_matrix[self._zone_id % num_colors].tolist()

    def get_edge_color(self):
        """Get the colors of edges.

        Returns
        -------
        List
            List of colors for edges.
        """
        num_colors = int(color_matrix.size / 3)
        if self._type == DisplayMeshType.EDGEZONELET:
            return color_matrix[self._id % num_colors].tolist()
        elif self._type == DisplayMeshType.TOPOEDGE:
            if self._topo_edge_type == 1:
                return [255, 0, 0]
            elif self._topo_edge_type == 2:
                return [0, 0, 0]
            elif self._topo_edge_type == 3:
                return [0, 255, 255]
            elif self._topo_edge_type == 4:
                return [255, 0, 255]
            elif self._topo_edge_type == 5:
                return [255, 255, 0]
            elif self._topo_edge_type == 6:
                return [128, 0, 128]
            else:
                return color_matrix[self._id % num_colors].tolist()

    def get_face_polydata(self, part_id: int, face_facet_res: FaceConnectivityResults, index: int):
        part = self._model.get_part(part_id)
        node_start = 3 * np.sum(face_facet_res.num_nodes_per_face_zonelet[0:index])
        num_node_coords = 3 * face_facet_res.num_nodes_per_face_zonelet[index]
        face_list_start = np.sum(face_facet_res.num_face_list_per_face_zonelet[0:index])
        num_face_list = face_facet_res.num_face_list_per_face_zonelet[index]
        has_mesh = True
        if face_facet_res.topo_face_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOFACE
            id = face_facet_res.topo_face_ids[index]
            has_mesh = face_facet_res.mesh_face_ids[index] > 0
        else:
            display_mesh_type = DisplayMeshType.FACEZONELET
            id = face_facet_res.face_zonelet_ids[index]

        vertices = face_facet_res.node_coords[node_start : node_start + num_node_coords].reshape(
            (-1, 3)
        )
        faces = face_facet_res.edge_list[face_list_start : face_list_start + num_face_list]

        if (
            display_mesh_type == DisplayMeshType.TOPOFACE
            or display_mesh_type == DisplayMeshType.FACEZONELET
        ):
            surf = pv.PolyData(vertices, faces)
            fcolor = np.array(self.get_face_color())
            colors = np.tile(fcolor, (surf.n_faces, 1))
            surf["colors"] = colors
            surf.disp_mesh = self
            if surf.n_points > 0:
                return surf

    def get_edge_polydata(self, part_id: int, edge_facet_res: EdgeConnectivityResults, index: int):
        part = self._model.get_part(part_id)
        node_start = 3 * np.sum(edge_facet_res.num_nodes_per_edge_zonelet[0:index])
        num_node_coords = 3 * edge_facet_res.num_nodes_per_edge_zonelet[index]
        edge_list_start = np.sum(edge_facet_res.num_edge_list_per_edge_zonelet[0:index])
        num_edge_list = edge_facet_res.num_edge_list_per_edge_zonelet[index]
        has_mesh = True
        if edge_facet_res.topo_edge_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOEDGE
            id = edge_facet_res.topo_edge_ids[index]
            has_mesh = edge_facet_res.mesh_edge_ids[index] > 0
        else:
            display_mesh_type = DisplayMeshType.EDGEZONELET
            id = edge_facet_res.edge_zonelet_ids[index]
        edge = pv.PolyData()
        vertices = edge_facet_res.node_coords[node_start : node_start + num_node_coords].reshape(
            (-1, 3)
        )
        faces = edge_facet_res.edge_list[edge_list_start : edge_list_start + num_edge_list]
        n_edges = edge_facet_res.num_edges_per_edge_zonelet[index]
        edge.points = vertices
        cells = np.full((n_edges, 3), 2, dtype=np.int_)
        i = 0
        j = 0
        while j < len(facet_list):
            nnodes = self._facet_list[j]
            j += 1
            cells[i, 1] = self._facet_list[j]
            if nnodes == 2:
                cells[i, 2] = self._facet_list[j + 1]
            elif nnodes == 3:
                cells[i, 2] = self._facet_list[j + 2]
            j += nnodes
            i += 1
        edge.lines = cells
        ecolor = np.array(self.get_edge_color())
        colors = np.tile(ecolor, (n_edges, 1))
        edge["colors"] = colors
        edge.disp_mesh = self
        if self._poly_data.n_points > 0:
            return edge

    def as_polydata(self):
        """Return the mesh as a ``pv.PolyData`` object."""
        part_ids = [part.id for part in self._model.parts]
        facet_result = self.get_face_and_edge_connectivity(
            part_ids, FaceAndEdgeConnectivityParams(model=self._model)
        )
        edge_list = []
        face_list = []
        spline_points_list = []
        spline_surface_list = []

        for i, part_id in enumerate(self._facet_result.part_ids):
            part = self._model.get_part(part_id)
            face_list.append(
                self.get_face_polydata(part_id, facet_result.face_connectivity_results, i)
            )
