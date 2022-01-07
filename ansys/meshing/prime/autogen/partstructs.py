""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class PartSummaryParams(CoreObject):
    """Parameters to control part summary results.
    """
    default_params = {}

    def __initialize(
            self,
            print_id: bool,
            print_mesh: bool):
        self._print_id = print_id
        self._print_mesh = print_mesh

    def __init__(
            self,
            model: CommunicationManager=None,
            print_id: bool = None,
            print_mesh: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes PartSummaryParams

        Parameters
        ----------
        model: Model
            Model to create a PartSummaryParams object with default parameters.
        print_id: bool, optional
            Boolean to control print ids. The default is false.
        print_mesh: bool, optional
            Boolean to control print mesh info. The default is true.
        json_data: dict, optional
            JSON dictionary to create a PartSummaryParams object with provided parameters.

        Examples
        --------
        >>> part_summary_params = PartSummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["printId"],
                json_data["printMesh"])
        else:
            all_field_specified = all(arg is not None for arg in [print_id, print_mesh])
            if all_field_specified:
                self.__initialize(
                    print_id,
                    print_mesh)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("PartSummaryParams")["PartSummaryParams"]
                    self.__initialize(
                        print_id if print_id is not None else ( PartSummaryParams.default_params["print_id"] if "print_id" in PartSummaryParams.default_params else json_data["printId"]),
                        print_mesh if print_mesh is not None else ( PartSummaryParams.default_params["print_mesh"] if "print_mesh" in PartSummaryParams.default_params else json_data["printMesh"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            print_id: bool = None,
            print_mesh: bool = None):
        args = locals()
        [PartSummaryParams.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartSummaryParams.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["printId"] = self._print_id
        json_data["printMesh"] = self._print_mesh
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "print_id :  %s\nprint_mesh :  %s" % (self._print_id, self._print_mesh)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def print_id(self) -> bool:
        """Boolean to control print ids. The default is false.
        """
        return self._print_id

    @print_id.setter
    def print_id(self, value: bool):
        self._print_id = value

    @property
    def print_mesh(self) -> bool:
        """Boolean to control print mesh info. The default is true.
        """
        return self._print_mesh

    @print_mesh.setter
    def print_mesh(self, value: bool):
        self._print_mesh = value

class PartSummaryResults(CoreObject):
    """Results of part summary.
    """
    default_params = {}

    def __initialize(
            self,
            message: str,
            n_topo_edges: int,
            n_topo_faces: int,
            n_topo_volumes: int,
            n_edge_zonelets: int,
            n_face_zonelets: int,
            n_cell_zonelets: int,
            n_edge_zones: int,
            n_face_zones: int,
            n_volume_zones: int,
            n_labels: int,
            n_nodes: int,
            n_faces: int,
            n_cells: int,
            n_tri_faces: int,
            n_poly_faces: int,
            n_quad_faces: int,
            n_tet_cells: int,
            n_pyra_cells: int,
            n_prism_cells: int,
            n_poly_cells: int,
            n_hex_cells: int,
            n_unmeshed_topo_faces: int):
        self._message = message
        self._n_topo_edges = n_topo_edges
        self._n_topo_faces = n_topo_faces
        self._n_topo_volumes = n_topo_volumes
        self._n_edge_zonelets = n_edge_zonelets
        self._n_face_zonelets = n_face_zonelets
        self._n_cell_zonelets = n_cell_zonelets
        self._n_edge_zones = n_edge_zones
        self._n_face_zones = n_face_zones
        self._n_volume_zones = n_volume_zones
        self._n_labels = n_labels
        self._n_nodes = n_nodes
        self._n_faces = n_faces
        self._n_cells = n_cells
        self._n_tri_faces = n_tri_faces
        self._n_poly_faces = n_poly_faces
        self._n_quad_faces = n_quad_faces
        self._n_tet_cells = n_tet_cells
        self._n_pyra_cells = n_pyra_cells
        self._n_prism_cells = n_prism_cells
        self._n_poly_cells = n_poly_cells
        self._n_hex_cells = n_hex_cells
        self._n_unmeshed_topo_faces = n_unmeshed_topo_faces

    def __init__(
            self,
            model: CommunicationManager=None,
            message: str = None,
            n_topo_edges: int = None,
            n_topo_faces: int = None,
            n_topo_volumes: int = None,
            n_edge_zonelets: int = None,
            n_face_zonelets: int = None,
            n_cell_zonelets: int = None,
            n_edge_zones: int = None,
            n_face_zones: int = None,
            n_volume_zones: int = None,
            n_labels: int = None,
            n_nodes: int = None,
            n_faces: int = None,
            n_cells: int = None,
            n_tri_faces: int = None,
            n_poly_faces: int = None,
            n_quad_faces: int = None,
            n_tet_cells: int = None,
            n_pyra_cells: int = None,
            n_prism_cells: int = None,
            n_poly_cells: int = None,
            n_hex_cells: int = None,
            n_unmeshed_topo_faces: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes PartSummaryResults

        Parameters
        ----------
        model: Model
            Model to create a PartSummaryResults object with default parameters.
        message: str, optional
            Part summary text.
        n_topo_edges: int, optional
            Number of topo edges.
        n_topo_faces: int, optional
            Number of topo faces.
        n_topo_volumes: int, optional
            Number of topo volumes.
        n_edge_zonelets: int, optional
            Number of edge zonelets.
        n_face_zonelets: int, optional
            Number of face zonelets.
        n_cell_zonelets: int, optional
            Number of cell zonelets.
        n_edge_zones: int, optional
            Number of edge zones.
        n_face_zones: int, optional
            Number of face zones.
        n_volume_zones: int, optional
            Number of volume zones.
        n_labels: int, optional
            Number of labels.
        n_nodes: int, optional
            Number of nodes.
        n_faces: int, optional
            Number of faces.
        n_cells: int, optional
            Number of cells.
        n_tri_faces: int, optional
            Number of triangular faces.
        n_poly_faces: int, optional
            Number of polygonal faces.
        n_quad_faces: int, optional
            Number of quadrilateral faces.
        n_tet_cells: int, optional
            Number of tetrahedral cells.
        n_pyra_cells: int, optional
            Number of pyramid cells.
        n_prism_cells: int, optional
            Number of prism cells.
        n_poly_cells: int, optional
            Number of polyhedral cells.
        n_hex_cells: int, optional
            Number of hexahedral cells.
        n_unmeshed_topo_faces: int, optional
            Number of unmeshed topo faces.
        json_data: dict, optional
            JSON dictionary to create a PartSummaryResults object with provided parameters.

        Examples
        --------
        >>> part_summary_results = PartSummaryResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["message"],
                json_data["nTopoEdges"],
                json_data["nTopoFaces"],
                json_data["nTopoVolumes"],
                json_data["nEdgeZonelets"],
                json_data["nFaceZonelets"],
                json_data["nCellZonelets"],
                json_data["nEdgeZones"],
                json_data["nFaceZones"],
                json_data["nVolumeZones"],
                json_data["nLabels"],
                json_data["nNodes"],
                json_data["nFaces"],
                json_data["nCells"],
                json_data["nTriFaces"],
                json_data["nPolyFaces"],
                json_data["nQuadFaces"],
                json_data["nTetCells"],
                json_data["nPyraCells"],
                json_data["nPrismCells"],
                json_data["nPolyCells"],
                json_data["nHexCells"],
                json_data["nUnmeshedTopoFaces"])
        else:
            all_field_specified = all(arg is not None for arg in [message, n_topo_edges, n_topo_faces, n_topo_volumes, n_edge_zonelets, n_face_zonelets, n_cell_zonelets, n_edge_zones, n_face_zones, n_volume_zones, n_labels, n_nodes, n_faces, n_cells, n_tri_faces, n_poly_faces, n_quad_faces, n_tet_cells, n_pyra_cells, n_prism_cells, n_poly_cells, n_hex_cells, n_unmeshed_topo_faces])
            if all_field_specified:
                self.__initialize(
                    message,
                    n_topo_edges,
                    n_topo_faces,
                    n_topo_volumes,
                    n_edge_zonelets,
                    n_face_zonelets,
                    n_cell_zonelets,
                    n_edge_zones,
                    n_face_zones,
                    n_volume_zones,
                    n_labels,
                    n_nodes,
                    n_faces,
                    n_cells,
                    n_tri_faces,
                    n_poly_faces,
                    n_quad_faces,
                    n_tet_cells,
                    n_pyra_cells,
                    n_prism_cells,
                    n_poly_cells,
                    n_hex_cells,
                    n_unmeshed_topo_faces)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("PartSummaryResults")["PartSummaryResults"]
                    self.__initialize(
                        message if message is not None else ( PartSummaryResults.default_params["message"] if "message" in PartSummaryResults.default_params else json_data["message"]),
                        n_topo_edges if n_topo_edges is not None else ( PartSummaryResults.default_params["n_topo_edges"] if "n_topo_edges" in PartSummaryResults.default_params else json_data["nTopoEdges"]),
                        n_topo_faces if n_topo_faces is not None else ( PartSummaryResults.default_params["n_topo_faces"] if "n_topo_faces" in PartSummaryResults.default_params else json_data["nTopoFaces"]),
                        n_topo_volumes if n_topo_volumes is not None else ( PartSummaryResults.default_params["n_topo_volumes"] if "n_topo_volumes" in PartSummaryResults.default_params else json_data["nTopoVolumes"]),
                        n_edge_zonelets if n_edge_zonelets is not None else ( PartSummaryResults.default_params["n_edge_zonelets"] if "n_edge_zonelets" in PartSummaryResults.default_params else json_data["nEdgeZonelets"]),
                        n_face_zonelets if n_face_zonelets is not None else ( PartSummaryResults.default_params["n_face_zonelets"] if "n_face_zonelets" in PartSummaryResults.default_params else json_data["nFaceZonelets"]),
                        n_cell_zonelets if n_cell_zonelets is not None else ( PartSummaryResults.default_params["n_cell_zonelets"] if "n_cell_zonelets" in PartSummaryResults.default_params else json_data["nCellZonelets"]),
                        n_edge_zones if n_edge_zones is not None else ( PartSummaryResults.default_params["n_edge_zones"] if "n_edge_zones" in PartSummaryResults.default_params else json_data["nEdgeZones"]),
                        n_face_zones if n_face_zones is not None else ( PartSummaryResults.default_params["n_face_zones"] if "n_face_zones" in PartSummaryResults.default_params else json_data["nFaceZones"]),
                        n_volume_zones if n_volume_zones is not None else ( PartSummaryResults.default_params["n_volume_zones"] if "n_volume_zones" in PartSummaryResults.default_params else json_data["nVolumeZones"]),
                        n_labels if n_labels is not None else ( PartSummaryResults.default_params["n_labels"] if "n_labels" in PartSummaryResults.default_params else json_data["nLabels"]),
                        n_nodes if n_nodes is not None else ( PartSummaryResults.default_params["n_nodes"] if "n_nodes" in PartSummaryResults.default_params else json_data["nNodes"]),
                        n_faces if n_faces is not None else ( PartSummaryResults.default_params["n_faces"] if "n_faces" in PartSummaryResults.default_params else json_data["nFaces"]),
                        n_cells if n_cells is not None else ( PartSummaryResults.default_params["n_cells"] if "n_cells" in PartSummaryResults.default_params else json_data["nCells"]),
                        n_tri_faces if n_tri_faces is not None else ( PartSummaryResults.default_params["n_tri_faces"] if "n_tri_faces" in PartSummaryResults.default_params else json_data["nTriFaces"]),
                        n_poly_faces if n_poly_faces is not None else ( PartSummaryResults.default_params["n_poly_faces"] if "n_poly_faces" in PartSummaryResults.default_params else json_data["nPolyFaces"]),
                        n_quad_faces if n_quad_faces is not None else ( PartSummaryResults.default_params["n_quad_faces"] if "n_quad_faces" in PartSummaryResults.default_params else json_data["nQuadFaces"]),
                        n_tet_cells if n_tet_cells is not None else ( PartSummaryResults.default_params["n_tet_cells"] if "n_tet_cells" in PartSummaryResults.default_params else json_data["nTetCells"]),
                        n_pyra_cells if n_pyra_cells is not None else ( PartSummaryResults.default_params["n_pyra_cells"] if "n_pyra_cells" in PartSummaryResults.default_params else json_data["nPyraCells"]),
                        n_prism_cells if n_prism_cells is not None else ( PartSummaryResults.default_params["n_prism_cells"] if "n_prism_cells" in PartSummaryResults.default_params else json_data["nPrismCells"]),
                        n_poly_cells if n_poly_cells is not None else ( PartSummaryResults.default_params["n_poly_cells"] if "n_poly_cells" in PartSummaryResults.default_params else json_data["nPolyCells"]),
                        n_hex_cells if n_hex_cells is not None else ( PartSummaryResults.default_params["n_hex_cells"] if "n_hex_cells" in PartSummaryResults.default_params else json_data["nHexCells"]),
                        n_unmeshed_topo_faces if n_unmeshed_topo_faces is not None else ( PartSummaryResults.default_params["n_unmeshed_topo_faces"] if "n_unmeshed_topo_faces" in PartSummaryResults.default_params else json_data["nUnmeshedTopoFaces"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            message: str = None,
            n_topo_edges: int = None,
            n_topo_faces: int = None,
            n_topo_volumes: int = None,
            n_edge_zonelets: int = None,
            n_face_zonelets: int = None,
            n_cell_zonelets: int = None,
            n_edge_zones: int = None,
            n_face_zones: int = None,
            n_volume_zones: int = None,
            n_labels: int = None,
            n_nodes: int = None,
            n_faces: int = None,
            n_cells: int = None,
            n_tri_faces: int = None,
            n_poly_faces: int = None,
            n_quad_faces: int = None,
            n_tet_cells: int = None,
            n_pyra_cells: int = None,
            n_prism_cells: int = None,
            n_poly_cells: int = None,
            n_hex_cells: int = None,
            n_unmeshed_topo_faces: int = None):
        args = locals()
        [PartSummaryResults.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartSummaryResults.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["message"] = self._message
        json_data["nTopoEdges"] = self._n_topo_edges
        json_data["nTopoFaces"] = self._n_topo_faces
        json_data["nTopoVolumes"] = self._n_topo_volumes
        json_data["nEdgeZonelets"] = self._n_edge_zonelets
        json_data["nFaceZonelets"] = self._n_face_zonelets
        json_data["nCellZonelets"] = self._n_cell_zonelets
        json_data["nEdgeZones"] = self._n_edge_zones
        json_data["nFaceZones"] = self._n_face_zones
        json_data["nVolumeZones"] = self._n_volume_zones
        json_data["nLabels"] = self._n_labels
        json_data["nNodes"] = self._n_nodes
        json_data["nFaces"] = self._n_faces
        json_data["nCells"] = self._n_cells
        json_data["nTriFaces"] = self._n_tri_faces
        json_data["nPolyFaces"] = self._n_poly_faces
        json_data["nQuadFaces"] = self._n_quad_faces
        json_data["nTetCells"] = self._n_tet_cells
        json_data["nPyraCells"] = self._n_pyra_cells
        json_data["nPrismCells"] = self._n_prism_cells
        json_data["nPolyCells"] = self._n_poly_cells
        json_data["nHexCells"] = self._n_hex_cells
        json_data["nUnmeshedTopoFaces"] = self._n_unmeshed_topo_faces
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "message :  %s\nn_topo_edges :  %s\nn_topo_faces :  %s\nn_topo_volumes :  %s\nn_edge_zonelets :  %s\nn_face_zonelets :  %s\nn_cell_zonelets :  %s\nn_edge_zones :  %s\nn_face_zones :  %s\nn_volume_zones :  %s\nn_labels :  %s\nn_nodes :  %s\nn_faces :  %s\nn_cells :  %s\nn_tri_faces :  %s\nn_poly_faces :  %s\nn_quad_faces :  %s\nn_tet_cells :  %s\nn_pyra_cells :  %s\nn_prism_cells :  %s\nn_poly_cells :  %s\nn_hex_cells :  %s\nn_unmeshed_topo_faces :  %s" % (self._message, self._n_topo_edges, self._n_topo_faces, self._n_topo_volumes, self._n_edge_zonelets, self._n_face_zonelets, self._n_cell_zonelets, self._n_edge_zones, self._n_face_zones, self._n_volume_zones, self._n_labels, self._n_nodes, self._n_faces, self._n_cells, self._n_tri_faces, self._n_poly_faces, self._n_quad_faces, self._n_tet_cells, self._n_pyra_cells, self._n_prism_cells, self._n_poly_cells, self._n_hex_cells, self._n_unmeshed_topo_faces)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def message(self) -> str:
        """Part summary text.
        """
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

    @property
    def n_topo_edges(self) -> int:
        """Number of topo edges.
        """
        return self._n_topo_edges

    @n_topo_edges.setter
    def n_topo_edges(self, value: int):
        self._n_topo_edges = value

    @property
    def n_topo_faces(self) -> int:
        """Number of topo faces.
        """
        return self._n_topo_faces

    @n_topo_faces.setter
    def n_topo_faces(self, value: int):
        self._n_topo_faces = value

    @property
    def n_topo_volumes(self) -> int:
        """Number of topo volumes.
        """
        return self._n_topo_volumes

    @n_topo_volumes.setter
    def n_topo_volumes(self, value: int):
        self._n_topo_volumes = value

    @property
    def n_edge_zonelets(self) -> int:
        """Number of edge zonelets.
        """
        return self._n_edge_zonelets

    @n_edge_zonelets.setter
    def n_edge_zonelets(self, value: int):
        self._n_edge_zonelets = value

    @property
    def n_face_zonelets(self) -> int:
        """Number of face zonelets.
        """
        return self._n_face_zonelets

    @n_face_zonelets.setter
    def n_face_zonelets(self, value: int):
        self._n_face_zonelets = value

    @property
    def n_cell_zonelets(self) -> int:
        """Number of cell zonelets.
        """
        return self._n_cell_zonelets

    @n_cell_zonelets.setter
    def n_cell_zonelets(self, value: int):
        self._n_cell_zonelets = value

    @property
    def n_edge_zones(self) -> int:
        """Number of edge zones.
        """
        return self._n_edge_zones

    @n_edge_zones.setter
    def n_edge_zones(self, value: int):
        self._n_edge_zones = value

    @property
    def n_face_zones(self) -> int:
        """Number of face zones.
        """
        return self._n_face_zones

    @n_face_zones.setter
    def n_face_zones(self, value: int):
        self._n_face_zones = value

    @property
    def n_volume_zones(self) -> int:
        """Number of volume zones.
        """
        return self._n_volume_zones

    @n_volume_zones.setter
    def n_volume_zones(self, value: int):
        self._n_volume_zones = value

    @property
    def n_labels(self) -> int:
        """Number of labels.
        """
        return self._n_labels

    @n_labels.setter
    def n_labels(self, value: int):
        self._n_labels = value

    @property
    def n_nodes(self) -> int:
        """Number of nodes.
        """
        return self._n_nodes

    @n_nodes.setter
    def n_nodes(self, value: int):
        self._n_nodes = value

    @property
    def n_faces(self) -> int:
        """Number of faces.
        """
        return self._n_faces

    @n_faces.setter
    def n_faces(self, value: int):
        self._n_faces = value

    @property
    def n_cells(self) -> int:
        """Number of cells.
        """
        return self._n_cells

    @n_cells.setter
    def n_cells(self, value: int):
        self._n_cells = value

    @property
    def n_tri_faces(self) -> int:
        """Number of triangular faces.
        """
        return self._n_tri_faces

    @n_tri_faces.setter
    def n_tri_faces(self, value: int):
        self._n_tri_faces = value

    @property
    def n_poly_faces(self) -> int:
        """Number of polygonal faces.
        """
        return self._n_poly_faces

    @n_poly_faces.setter
    def n_poly_faces(self, value: int):
        self._n_poly_faces = value

    @property
    def n_quad_faces(self) -> int:
        """Number of quadrilateral faces.
        """
        return self._n_quad_faces

    @n_quad_faces.setter
    def n_quad_faces(self, value: int):
        self._n_quad_faces = value

    @property
    def n_tet_cells(self) -> int:
        """Number of tetrahedral cells.
        """
        return self._n_tet_cells

    @n_tet_cells.setter
    def n_tet_cells(self, value: int):
        self._n_tet_cells = value

    @property
    def n_pyra_cells(self) -> int:
        """Number of pyramid cells.
        """
        return self._n_pyra_cells

    @n_pyra_cells.setter
    def n_pyra_cells(self, value: int):
        self._n_pyra_cells = value

    @property
    def n_prism_cells(self) -> int:
        """Number of prism cells.
        """
        return self._n_prism_cells

    @n_prism_cells.setter
    def n_prism_cells(self, value: int):
        self._n_prism_cells = value

    @property
    def n_poly_cells(self) -> int:
        """Number of polyhedral cells.
        """
        return self._n_poly_cells

    @n_poly_cells.setter
    def n_poly_cells(self, value: int):
        self._n_poly_cells = value

    @property
    def n_hex_cells(self) -> int:
        """Number of hexahedral cells.
        """
        return self._n_hex_cells

    @n_hex_cells.setter
    def n_hex_cells(self, value: int):
        self._n_hex_cells = value

    @property
    def n_unmeshed_topo_faces(self) -> int:
        """Number of unmeshed topo faces.
        """
        return self._n_unmeshed_topo_faces

    @n_unmeshed_topo_faces.setter
    def n_unmeshed_topo_faces(self, value: int):
        self._n_unmeshed_topo_faces = value
