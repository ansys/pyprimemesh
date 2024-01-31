"""Process the mesh for visualization in the GUI."""

import enum

import numpy as np
import pyvista as pv
from beartype.typing import Dict, List, Union

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

    def compute_face_list_from_structured_nodes(self, dim):
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

    def _get_vertices_and_faces(
        self, connectivity_results: Union[FaceConnectivityResults, EdgeConnectivityResults], index
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Calculates the vertices and faces of the mesh.

        Parameters
        ----------
        connectivity_results : Union[FaceConnectivityResults, EdgeConnectivityResults]
            _description_
        index : _type_
            _description_

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            _description_
        """
        node_start = 3 * np.sum(connectivity_results.num_nodes_per_face_zonelet[0:index])
        num_node_coords = 3 * connectivity_results.num_nodes_per_face_zonelet[index]
        face_list_start = np.sum(connectivity_results.num_face_list_per_face_zonelet[0:index])
        num_face_list = connectivity_results.num_face_list_per_face_zonelet[index]
        vertices = connectivity_results.node_coords[
            node_start : node_start + num_node_coords
        ].reshape((-1, 3))
        faces = connectivity_results.edge_list[face_list_start : face_list_start + num_face_list]
        return vertices, faces

    def get_face_polydata(self, part_id: int, face_facet_res: FaceConnectivityResults, index: int):
        """Get the polydata object of the faces.

        Parameters
        ----------
        part_id : int
            _description_
        face_facet_res : FaceConnectivityResults
            _description_
        index : int
            _description_

        Returns
        -------
        _type_
            _description_
        """

        vertices, faces = self._get_vertices_and_faces(face_facet_res, index)
        if face_facet_res.topo_face_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOFACE
        else:
            display_mesh_type = DisplayMeshType.FACEZONELET

        if (
            display_mesh_type == DisplayMeshType.TOPOFACE
            or display_mesh_type == DisplayMeshType.FACEZONELET
        ):
            surf = pv.PolyData(vertices, faces)
            fcolor = np.array(self.get_face_color(ColorByType.PART))
            colors = np.tile(fcolor, (surf.n_faces, 1))
            surf["colors"] = colors
            surf.disp_mesh = self
            if surf.n_points > 0:
                return surf

    def get_edge_polydata(self, part_id: int, edge_facet_res: EdgeConnectivityResults, index: int):
        """Get the polydata object of the edges.

        Parameters
        ----------
        part_id : int
            _description_
        edge_facet_res : EdgeConnectivityResults
            _description_
        index : int
            _description_

        Returns
        -------
        _type_
            _description_
        """
        vertices, facet_list = self._get_vertices_and_faces(edge_facet_res, index)
        edge = pv.PolyData()
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
        if edge.n_points > 0:
            return edge

    def get_spline_cp_polydata(self, part_id: int, spline_id: int):
        """Get the polydata object of the spline control points.

        Parameters
        ----------
        part_id : int
            _description_
        spline_id : int
            _description_

        Returns
        -------
        _type_
            _description_
        """
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)
        dim = spline.control_points_count
        vertices = spline.control_points
        faces = self.compute_face_list_from_structured_nodes(dim)
        surf = pv.PolyData(vertices, faces)
        fcolor = np.array([0, 0, 255])
        colors = np.tile(fcolor, (surf.n_faces, 1))
        surf["colors"] = colors
        surf.disp_mesh = self
        if surf.n_points > 0:
            return surf

    def get_spline_surface_polydata(self, part_id: int, spline_id: int):
        """Get the polydata object of the spline surface.

        Parameters
        ----------
        part_id : int
            _description_
        spline_id : int
            _description_

        Returns
        -------
        _type_
            _description_
        """
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)
        dim = spline.spline_points_count
        vertices = spline.spline_points
        faces = self.compute_face_list_from_structured_nodes(dim)
        surf = pv.PolyData(vertices, faces)
        fcolor = np.array(color_matrix[1])
        colors = np.tile(fcolor, (surf.n_faces, 1))
        surf["colors"] = colors
        surf.disp_mesh = self
        if surf.n_points > 0:
            return surf

    def as_polydata(self) -> Dict[int, Dict[str, List[pv.PolyData]]]:
        """Return the mesh as a ``pv.PolyData`` object."""
        part_ids = [part.id for part in self._model.parts]
        facet_result = self.get_face_and_edge_connectivity(
            part_ids, FaceAndEdgeConnectivityParams(model=self._model)
        )
        parts_polydata = []
        for i, part_id in enumerate(self._facet_result.part_ids):
            part = self._model.get_part(part_id)
            splines = part.get_splines()
            part_polydata = {}
            face_polydata_list = [
                self.get_face_polydata(part_id, face_fet_result, j)
                for face_fet_result in facet_result.face_connectivity_results_per_part
                for j in range(0, len(face_fet_result.face_zonelet_ids))
            ]

            edge_polydata_list = [
                self.get_edge_polydata(part_id, facet_result.edge_connectivity_results_per_part, j)
                for edge_facet_result in facet_result.edge_connectivity_results_per_part
                for j in range(0, len(edge_facet_result.edge_zonelet_ids))
            ]

            spline_cp_polydata_list = [self.get_spline_cp_polydata(part_ids[i], j) for j in splines]

            spline_surface_polydata_list = [
                self.get_spline_surface_polydata(part_ids[i], j) for j in splines
            ]

            part_polydata["faces"] = face_polydata_list
            part_polydata["edges"] = edge_polydata_list
            part_polydata["ctrlpts"] = spline_cp_polydata_list
            part_polydata["splinesurf"] = spline_surface_polydata_list
            parts_polydata[part_id] = part_polydata
        return parts_polydata
