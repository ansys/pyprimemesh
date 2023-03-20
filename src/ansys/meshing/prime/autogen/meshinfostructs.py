""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class CellStatisticsParams(CoreObject):
    """Parameters used to calculate cell statistics.
    """
    _default_params = {}

    def __initialize(
            self,
            get_volume: bool):
        self._get_volume = get_volume

    def __init__(
            self,
            model: CommunicationManager=None,
            get_volume: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CellStatisticsParams.

        Parameters
        ----------
        model: Model
            Model to create a CellStatisticsParams object with default parameters.
        get_volume: bool, optional
            Provides option to compute and get cumulative cell volume.
        json_data: dict, optional
            JSON dictionary to create a CellStatisticsParams object with provided parameters.

        Examples
        --------
        >>> cell_statistics_params = prime.CellStatisticsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["getVolume"] if "getVolume" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [get_volume])
            if all_field_specified:
                self.__initialize(
                    get_volume)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CellStatisticsParams")
                    json_data = param_json["CellStatisticsParams"] if "CellStatisticsParams" in param_json else {}
                    self.__initialize(
                        get_volume if get_volume is not None else ( CellStatisticsParams._default_params["get_volume"] if "get_volume" in CellStatisticsParams._default_params else (json_data["getVolume"] if "getVolume" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            get_volume: bool = None):
        """Set the default values of CellStatisticsParams.

        Parameters
        ----------
        get_volume: bool, optional
            Provides option to compute and get cumulative cell volume.
        """
        args = locals()
        [CellStatisticsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CellStatisticsParams.

        Examples
        --------
        >>> CellStatisticsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CellStatisticsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._get_volume is not None:
            json_data["getVolume"] = self._get_volume
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "get_volume :  %s" % (self._get_volume)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def get_volume(self) -> bool:
        """Provides option to compute and get cumulative cell volume.
        """
        return self._get_volume

    @get_volume.setter
    def get_volume(self, value: bool):
        self._get_volume = value

class CellStatisticsResults(CoreObject):
    """Results of cell statistics information.
    """
    _default_params = {}

    def __initialize(
            self,
            volume: float,
            error_code: ErrorCode):
        self._volume = volume
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            volume: float = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CellStatisticsResults.

        Parameters
        ----------
        model: Model
            Model to create a CellStatisticsResults object with default parameters.
        volume: float, optional
            Cumulative volume of all the cell elements of selected entities.
        error_code: ErrorCode, optional
            Error code associated with the cell statistics function.
        json_data: dict, optional
            JSON dictionary to create a CellStatisticsResults object with provided parameters.

        Examples
        --------
        >>> cell_statistics_results = prime.CellStatisticsResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["volume"] if "volume" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [volume, error_code])
            if all_field_specified:
                self.__initialize(
                    volume,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CellStatisticsResults")
                    json_data = param_json["CellStatisticsResults"] if "CellStatisticsResults" in param_json else {}
                    self.__initialize(
                        volume if volume is not None else ( CellStatisticsResults._default_params["volume"] if "volume" in CellStatisticsResults._default_params else (json_data["volume"] if "volume" in json_data else None)),
                        error_code if error_code is not None else ( CellStatisticsResults._default_params["error_code"] if "error_code" in CellStatisticsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            volume: float = None,
            error_code: ErrorCode = None):
        """Set the default values of CellStatisticsResults.

        Parameters
        ----------
        volume: float, optional
            Cumulative volume of all the cell elements of selected entities.
        error_code: ErrorCode, optional
            Error code associated with the cell statistics function.
        """
        args = locals()
        [CellStatisticsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CellStatisticsResults.

        Examples
        --------
        >>> CellStatisticsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CellStatisticsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._volume is not None:
            json_data["volume"] = self._volume
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "volume :  %s\nerror_code :  %s" % (self._volume, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def volume(self) -> float:
        """Cumulative volume of all the cell elements of selected entities.
        """
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the cell statistics function.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class FaceConnectivityResults(CoreObject):
    """Result of the face connectivity information.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            face_zonelet_ids: Iterable[int],
            topo_face_ids: Iterable[int],
            mesh_face_ids: Iterable[int],
            face_zone_ids: Iterable[int],
            face_zone_names: List[str],
            num_nodes_per_face_zonelet: Iterable[int],
            node_coords: Iterable[float],
            num_face_list_per_face_zonelet: Iterable[int],
            face_list: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._face_zonelet_ids = face_zonelet_ids if isinstance(face_zonelet_ids, np.ndarray) else np.array(face_zonelet_ids, dtype=np.int32) if face_zonelet_ids is not None else None
        self._topo_face_ids = topo_face_ids if isinstance(topo_face_ids, np.ndarray) else np.array(topo_face_ids, dtype=np.int32) if topo_face_ids is not None else None
        self._mesh_face_ids = mesh_face_ids if isinstance(mesh_face_ids, np.ndarray) else np.array(mesh_face_ids, dtype=np.int32) if mesh_face_ids is not None else None
        self._face_zone_ids = face_zone_ids if isinstance(face_zone_ids, np.ndarray) else np.array(face_zone_ids, dtype=np.int32) if face_zone_ids is not None else None
        self._face_zone_names = face_zone_names
        self._num_nodes_per_face_zonelet = num_nodes_per_face_zonelet if isinstance(num_nodes_per_face_zonelet, np.ndarray) else np.array(num_nodes_per_face_zonelet, dtype=np.int32) if num_nodes_per_face_zonelet is not None else None
        self._node_coords = node_coords if isinstance(node_coords, np.ndarray) else np.array(node_coords, dtype=np.double) if node_coords is not None else None
        self._num_face_list_per_face_zonelet = num_face_list_per_face_zonelet if isinstance(num_face_list_per_face_zonelet, np.ndarray) else np.array(num_face_list_per_face_zonelet, dtype=np.int32) if num_face_list_per_face_zonelet is not None else None
        self._face_list = face_list if isinstance(face_list, np.ndarray) else np.array(face_list, dtype=np.int32) if face_list is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            face_zonelet_ids: Iterable[int] = None,
            topo_face_ids: Iterable[int] = None,
            mesh_face_ids: Iterable[int] = None,
            face_zone_ids: Iterable[int] = None,
            face_zone_names: List[str] = None,
            num_nodes_per_face_zonelet: Iterable[int] = None,
            node_coords: Iterable[float] = None,
            num_face_list_per_face_zonelet: Iterable[int] = None,
            face_list: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FaceConnectivityResults.

        Parameters
        ----------
        model: Model
            Model to create a FaceConnectivityResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the get face connectivity operation.
        face_zonelet_ids: Iterable[int], optional
            Face zonelet ids for which connectivity data is available.
        topo_face_ids: Iterable[int], optional
            TopoFace ids corresponding to each face zonelet id for topology based mesh.
        mesh_face_ids: Iterable[int], optional
            Mesh face ids corresponding to each topoface.
        face_zone_ids: Iterable[int], optional
            Face zone id corresponding to each topoface or face zonelet.
        face_zone_names: List[str], optional
            Face zone name corresponding to each topoface or face zonelet.
        num_nodes_per_face_zonelet: Iterable[int], optional
            Number of nodes per face zonelet.
        node_coords: Iterable[float], optional
            Node coordinates describing faces of face zonelet.
        num_face_list_per_face_zonelet: Iterable[int], optional
            Number of face list per face zonelet.
        face_list: Iterable[int], optional
            Face list describing connectivity of node coordinates.
        json_data: dict, optional
            JSON dictionary to create a FaceConnectivityResults object with provided parameters.

        Examples
        --------
        >>> face_connectivity_results = prime.FaceConnectivityResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["faceZoneletIDs"] if "faceZoneletIDs" in json_data else None,
                json_data["topoFaceIDs"] if "topoFaceIDs" in json_data else None,
                json_data["meshFaceIDs"] if "meshFaceIDs" in json_data else None,
                json_data["faceZoneIDs"] if "faceZoneIDs" in json_data else None,
                json_data["faceZoneNames"] if "faceZoneNames" in json_data else None,
                json_data["numNodesPerFaceZonelet"] if "numNodesPerFaceZonelet" in json_data else None,
                json_data["nodeCoords"] if "nodeCoords" in json_data else None,
                json_data["numFaceListPerFaceZonelet"] if "numFaceListPerFaceZonelet" in json_data else None,
                json_data["faceList"] if "faceList" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, face_zonelet_ids, topo_face_ids, mesh_face_ids, face_zone_ids, face_zone_names, num_nodes_per_face_zonelet, node_coords, num_face_list_per_face_zonelet, face_list])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    face_zonelet_ids,
                    topo_face_ids,
                    mesh_face_ids,
                    face_zone_ids,
                    face_zone_names,
                    num_nodes_per_face_zonelet,
                    node_coords,
                    num_face_list_per_face_zonelet,
                    face_list)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "FaceConnectivityResults")
                    json_data = param_json["FaceConnectivityResults"] if "FaceConnectivityResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FaceConnectivityResults._default_params["error_code"] if "error_code" in FaceConnectivityResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        face_zonelet_ids if face_zonelet_ids is not None else ( FaceConnectivityResults._default_params["face_zonelet_ids"] if "face_zonelet_ids" in FaceConnectivityResults._default_params else (json_data["faceZoneletIDs"] if "faceZoneletIDs" in json_data else None)),
                        topo_face_ids if topo_face_ids is not None else ( FaceConnectivityResults._default_params["topo_face_ids"] if "topo_face_ids" in FaceConnectivityResults._default_params else (json_data["topoFaceIDs"] if "topoFaceIDs" in json_data else None)),
                        mesh_face_ids if mesh_face_ids is not None else ( FaceConnectivityResults._default_params["mesh_face_ids"] if "mesh_face_ids" in FaceConnectivityResults._default_params else (json_data["meshFaceIDs"] if "meshFaceIDs" in json_data else None)),
                        face_zone_ids if face_zone_ids is not None else ( FaceConnectivityResults._default_params["face_zone_ids"] if "face_zone_ids" in FaceConnectivityResults._default_params else (json_data["faceZoneIDs"] if "faceZoneIDs" in json_data else None)),
                        face_zone_names if face_zone_names is not None else ( FaceConnectivityResults._default_params["face_zone_names"] if "face_zone_names" in FaceConnectivityResults._default_params else (json_data["faceZoneNames"] if "faceZoneNames" in json_data else None)),
                        num_nodes_per_face_zonelet if num_nodes_per_face_zonelet is not None else ( FaceConnectivityResults._default_params["num_nodes_per_face_zonelet"] if "num_nodes_per_face_zonelet" in FaceConnectivityResults._default_params else (json_data["numNodesPerFaceZonelet"] if "numNodesPerFaceZonelet" in json_data else None)),
                        node_coords if node_coords is not None else ( FaceConnectivityResults._default_params["node_coords"] if "node_coords" in FaceConnectivityResults._default_params else (json_data["nodeCoords"] if "nodeCoords" in json_data else None)),
                        num_face_list_per_face_zonelet if num_face_list_per_face_zonelet is not None else ( FaceConnectivityResults._default_params["num_face_list_per_face_zonelet"] if "num_face_list_per_face_zonelet" in FaceConnectivityResults._default_params else (json_data["numFaceListPerFaceZonelet"] if "numFaceListPerFaceZonelet" in json_data else None)),
                        face_list if face_list is not None else ( FaceConnectivityResults._default_params["face_list"] if "face_list" in FaceConnectivityResults._default_params else (json_data["faceList"] if "faceList" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            face_zonelet_ids: Iterable[int] = None,
            topo_face_ids: Iterable[int] = None,
            mesh_face_ids: Iterable[int] = None,
            face_zone_ids: Iterable[int] = None,
            face_zone_names: List[str] = None,
            num_nodes_per_face_zonelet: Iterable[int] = None,
            node_coords: Iterable[float] = None,
            num_face_list_per_face_zonelet: Iterable[int] = None,
            face_list: Iterable[int] = None):
        """Set the default values of FaceConnectivityResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the get face connectivity operation.
        face_zonelet_ids: Iterable[int], optional
            Face zonelet ids for which connectivity data is available.
        topo_face_ids: Iterable[int], optional
            TopoFace ids corresponding to each face zonelet id for topology based mesh.
        mesh_face_ids: Iterable[int], optional
            Mesh face ids corresponding to each topoface.
        face_zone_ids: Iterable[int], optional
            Face zone id corresponding to each topoface or face zonelet.
        face_zone_names: List[str], optional
            Face zone name corresponding to each topoface or face zonelet.
        num_nodes_per_face_zonelet: Iterable[int], optional
            Number of nodes per face zonelet.
        node_coords: Iterable[float], optional
            Node coordinates describing faces of face zonelet.
        num_face_list_per_face_zonelet: Iterable[int], optional
            Number of face list per face zonelet.
        face_list: Iterable[int], optional
            Face list describing connectivity of node coordinates.
        """
        args = locals()
        [FaceConnectivityResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FaceConnectivityResults.

        Examples
        --------
        >>> FaceConnectivityResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FaceConnectivityResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._face_zonelet_ids is not None:
            json_data["faceZoneletIDs"] = self._face_zonelet_ids
        if self._topo_face_ids is not None:
            json_data["topoFaceIDs"] = self._topo_face_ids
        if self._mesh_face_ids is not None:
            json_data["meshFaceIDs"] = self._mesh_face_ids
        if self._face_zone_ids is not None:
            json_data["faceZoneIDs"] = self._face_zone_ids
        if self._face_zone_names is not None:
            json_data["faceZoneNames"] = self._face_zone_names
        if self._num_nodes_per_face_zonelet is not None:
            json_data["numNodesPerFaceZonelet"] = self._num_nodes_per_face_zonelet
        if self._node_coords is not None:
            json_data["nodeCoords"] = self._node_coords
        if self._num_face_list_per_face_zonelet is not None:
            json_data["numFaceListPerFaceZonelet"] = self._num_face_list_per_face_zonelet
        if self._face_list is not None:
            json_data["faceList"] = self._face_list
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nface_zonelet_ids :  %s\ntopo_face_ids :  %s\nmesh_face_ids :  %s\nface_zone_ids :  %s\nface_zone_names :  %s\nnum_nodes_per_face_zonelet :  %s\nnode_coords :  %s\nnum_face_list_per_face_zonelet :  %s\nface_list :  %s" % (self._error_code, self._face_zonelet_ids, self._topo_face_ids, self._mesh_face_ids, self._face_zone_ids, self._face_zone_names, self._num_nodes_per_face_zonelet, self._node_coords, self._num_face_list_per_face_zonelet, self._face_list)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the get face connectivity operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def face_zonelet_ids(self) -> Iterable[int]:
        """Face zonelet ids for which connectivity data is available.
        """
        return self._face_zonelet_ids

    @face_zonelet_ids.setter
    def face_zonelet_ids(self, value: Iterable[int]):
        self._face_zonelet_ids = value

    @property
    def topo_face_ids(self) -> Iterable[int]:
        """TopoFace ids corresponding to each face zonelet id for topology based mesh.
        """
        return self._topo_face_ids

    @topo_face_ids.setter
    def topo_face_ids(self, value: Iterable[int]):
        self._topo_face_ids = value

    @property
    def mesh_face_ids(self) -> Iterable[int]:
        """Mesh face ids corresponding to each topoface.
        """
        return self._mesh_face_ids

    @mesh_face_ids.setter
    def mesh_face_ids(self, value: Iterable[int]):
        self._mesh_face_ids = value

    @property
    def face_zone_ids(self) -> Iterable[int]:
        """Face zone id corresponding to each topoface or face zonelet.
        """
        return self._face_zone_ids

    @face_zone_ids.setter
    def face_zone_ids(self, value: Iterable[int]):
        self._face_zone_ids = value

    @property
    def face_zone_names(self) -> List[str]:
        """Face zone name corresponding to each topoface or face zonelet.
        """
        return self._face_zone_names

    @face_zone_names.setter
    def face_zone_names(self, value: List[str]):
        self._face_zone_names = value

    @property
    def num_nodes_per_face_zonelet(self) -> Iterable[int]:
        """Number of nodes per face zonelet.
        """
        return self._num_nodes_per_face_zonelet

    @num_nodes_per_face_zonelet.setter
    def num_nodes_per_face_zonelet(self, value: Iterable[int]):
        self._num_nodes_per_face_zonelet = value

    @property
    def node_coords(self) -> Iterable[float]:
        """Node coordinates describing faces of face zonelet.
        """
        return self._node_coords

    @node_coords.setter
    def node_coords(self, value: Iterable[float]):
        self._node_coords = value

    @property
    def num_face_list_per_face_zonelet(self) -> Iterable[int]:
        """Number of face list per face zonelet.
        """
        return self._num_face_list_per_face_zonelet

    @num_face_list_per_face_zonelet.setter
    def num_face_list_per_face_zonelet(self, value: Iterable[int]):
        self._num_face_list_per_face_zonelet = value

    @property
    def face_list(self) -> Iterable[int]:
        """Face list describing connectivity of node coordinates.
        """
        return self._face_list

    @face_list.setter
    def face_list(self, value: Iterable[int]):
        self._face_list = value

class EdgeConnectivityResults(CoreObject):
    """Result of the edge connectivity information.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            edge_zonelet_ids: Iterable[int],
            topo_edge_ids: Iterable[int],
            mesh_edge_ids: Iterable[int],
            topo_edge_types: Iterable[int],
            num_nodes_per_edge_zonelet: Iterable[int],
            node_coords: Iterable[float],
            num_edge_list_per_edge_zonelet: Iterable[int],
            edge_list: Iterable[int],
            num_edges_per_edge_zonelet: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._edge_zonelet_ids = edge_zonelet_ids if isinstance(edge_zonelet_ids, np.ndarray) else np.array(edge_zonelet_ids, dtype=np.int32) if edge_zonelet_ids is not None else None
        self._topo_edge_ids = topo_edge_ids if isinstance(topo_edge_ids, np.ndarray) else np.array(topo_edge_ids, dtype=np.int32) if topo_edge_ids is not None else None
        self._mesh_edge_ids = mesh_edge_ids if isinstance(mesh_edge_ids, np.ndarray) else np.array(mesh_edge_ids, dtype=np.int32) if mesh_edge_ids is not None else None
        self._topo_edge_types = topo_edge_types if isinstance(topo_edge_types, np.ndarray) else np.array(topo_edge_types, dtype=np.int32) if topo_edge_types is not None else None
        self._num_nodes_per_edge_zonelet = num_nodes_per_edge_zonelet if isinstance(num_nodes_per_edge_zonelet, np.ndarray) else np.array(num_nodes_per_edge_zonelet, dtype=np.int32) if num_nodes_per_edge_zonelet is not None else None
        self._node_coords = node_coords if isinstance(node_coords, np.ndarray) else np.array(node_coords, dtype=np.double) if node_coords is not None else None
        self._num_edge_list_per_edge_zonelet = num_edge_list_per_edge_zonelet if isinstance(num_edge_list_per_edge_zonelet, np.ndarray) else np.array(num_edge_list_per_edge_zonelet, dtype=np.int32) if num_edge_list_per_edge_zonelet is not None else None
        self._edge_list = edge_list if isinstance(edge_list, np.ndarray) else np.array(edge_list, dtype=np.int32) if edge_list is not None else None
        self._num_edges_per_edge_zonelet = num_edges_per_edge_zonelet if isinstance(num_edges_per_edge_zonelet, np.ndarray) else np.array(num_edges_per_edge_zonelet, dtype=np.int32) if num_edges_per_edge_zonelet is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            edge_zonelet_ids: Iterable[int] = None,
            topo_edge_ids: Iterable[int] = None,
            mesh_edge_ids: Iterable[int] = None,
            topo_edge_types: Iterable[int] = None,
            num_nodes_per_edge_zonelet: Iterable[int] = None,
            node_coords: Iterable[float] = None,
            num_edge_list_per_edge_zonelet: Iterable[int] = None,
            edge_list: Iterable[int] = None,
            num_edges_per_edge_zonelet: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the EdgeConnectivityResults.

        Parameters
        ----------
        model: Model
            Model to create a EdgeConnectivityResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the get edge connectivity operation.
        edge_zonelet_ids: Iterable[int], optional
            Edge zonelet ids for which connectivity data is available.
        topo_edge_ids: Iterable[int], optional
            TopoEdge ids corresponding to each edge zonelet id for topology based mesh.
        mesh_edge_ids: Iterable[int], optional
            Mesh edge ids corresponding to each topoedge.
        topo_edge_types: Iterable[int], optional
            TopoEdge type corresponding to each topoedge.
        num_nodes_per_edge_zonelet: Iterable[int], optional
            Number of nodes per edge zonelet.
        node_coords: Iterable[float], optional
            Node coordinates describing edges of edge zonelet.
        num_edge_list_per_edge_zonelet: Iterable[int], optional
            Number of edge list per edge zonelet.
        edge_list: Iterable[int], optional
            Edge list describing connectivity of node coordinates.
        num_edges_per_edge_zonelet: Iterable[int], optional
            Number of edges per edge zonelet.
        json_data: dict, optional
            JSON dictionary to create a EdgeConnectivityResults object with provided parameters.

        Examples
        --------
        >>> edge_connectivity_results = prime.EdgeConnectivityResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["edgeZoneletIDs"] if "edgeZoneletIDs" in json_data else None,
                json_data["topoEdgeIDs"] if "topoEdgeIDs" in json_data else None,
                json_data["meshEdgeIDs"] if "meshEdgeIDs" in json_data else None,
                json_data["topoEdgeTypes"] if "topoEdgeTypes" in json_data else None,
                json_data["numNodesPerEdgeZonelet"] if "numNodesPerEdgeZonelet" in json_data else None,
                json_data["nodeCoords"] if "nodeCoords" in json_data else None,
                json_data["numEdgeListPerEdgeZonelet"] if "numEdgeListPerEdgeZonelet" in json_data else None,
                json_data["edgeList"] if "edgeList" in json_data else None,
                json_data["numEdgesPerEdgeZonelet"] if "numEdgesPerEdgeZonelet" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, edge_zonelet_ids, topo_edge_ids, mesh_edge_ids, topo_edge_types, num_nodes_per_edge_zonelet, node_coords, num_edge_list_per_edge_zonelet, edge_list, num_edges_per_edge_zonelet])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    edge_zonelet_ids,
                    topo_edge_ids,
                    mesh_edge_ids,
                    topo_edge_types,
                    num_nodes_per_edge_zonelet,
                    node_coords,
                    num_edge_list_per_edge_zonelet,
                    edge_list,
                    num_edges_per_edge_zonelet)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "EdgeConnectivityResults")
                    json_data = param_json["EdgeConnectivityResults"] if "EdgeConnectivityResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( EdgeConnectivityResults._default_params["error_code"] if "error_code" in EdgeConnectivityResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        edge_zonelet_ids if edge_zonelet_ids is not None else ( EdgeConnectivityResults._default_params["edge_zonelet_ids"] if "edge_zonelet_ids" in EdgeConnectivityResults._default_params else (json_data["edgeZoneletIDs"] if "edgeZoneletIDs" in json_data else None)),
                        topo_edge_ids if topo_edge_ids is not None else ( EdgeConnectivityResults._default_params["topo_edge_ids"] if "topo_edge_ids" in EdgeConnectivityResults._default_params else (json_data["topoEdgeIDs"] if "topoEdgeIDs" in json_data else None)),
                        mesh_edge_ids if mesh_edge_ids is not None else ( EdgeConnectivityResults._default_params["mesh_edge_ids"] if "mesh_edge_ids" in EdgeConnectivityResults._default_params else (json_data["meshEdgeIDs"] if "meshEdgeIDs" in json_data else None)),
                        topo_edge_types if topo_edge_types is not None else ( EdgeConnectivityResults._default_params["topo_edge_types"] if "topo_edge_types" in EdgeConnectivityResults._default_params else (json_data["topoEdgeTypes"] if "topoEdgeTypes" in json_data else None)),
                        num_nodes_per_edge_zonelet if num_nodes_per_edge_zonelet is not None else ( EdgeConnectivityResults._default_params["num_nodes_per_edge_zonelet"] if "num_nodes_per_edge_zonelet" in EdgeConnectivityResults._default_params else (json_data["numNodesPerEdgeZonelet"] if "numNodesPerEdgeZonelet" in json_data else None)),
                        node_coords if node_coords is not None else ( EdgeConnectivityResults._default_params["node_coords"] if "node_coords" in EdgeConnectivityResults._default_params else (json_data["nodeCoords"] if "nodeCoords" in json_data else None)),
                        num_edge_list_per_edge_zonelet if num_edge_list_per_edge_zonelet is not None else ( EdgeConnectivityResults._default_params["num_edge_list_per_edge_zonelet"] if "num_edge_list_per_edge_zonelet" in EdgeConnectivityResults._default_params else (json_data["numEdgeListPerEdgeZonelet"] if "numEdgeListPerEdgeZonelet" in json_data else None)),
                        edge_list if edge_list is not None else ( EdgeConnectivityResults._default_params["edge_list"] if "edge_list" in EdgeConnectivityResults._default_params else (json_data["edgeList"] if "edgeList" in json_data else None)),
                        num_edges_per_edge_zonelet if num_edges_per_edge_zonelet is not None else ( EdgeConnectivityResults._default_params["num_edges_per_edge_zonelet"] if "num_edges_per_edge_zonelet" in EdgeConnectivityResults._default_params else (json_data["numEdgesPerEdgeZonelet"] if "numEdgesPerEdgeZonelet" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            edge_zonelet_ids: Iterable[int] = None,
            topo_edge_ids: Iterable[int] = None,
            mesh_edge_ids: Iterable[int] = None,
            topo_edge_types: Iterable[int] = None,
            num_nodes_per_edge_zonelet: Iterable[int] = None,
            node_coords: Iterable[float] = None,
            num_edge_list_per_edge_zonelet: Iterable[int] = None,
            edge_list: Iterable[int] = None,
            num_edges_per_edge_zonelet: Iterable[int] = None):
        """Set the default values of EdgeConnectivityResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the get edge connectivity operation.
        edge_zonelet_ids: Iterable[int], optional
            Edge zonelet ids for which connectivity data is available.
        topo_edge_ids: Iterable[int], optional
            TopoEdge ids corresponding to each edge zonelet id for topology based mesh.
        mesh_edge_ids: Iterable[int], optional
            Mesh edge ids corresponding to each topoedge.
        topo_edge_types: Iterable[int], optional
            TopoEdge type corresponding to each topoedge.
        num_nodes_per_edge_zonelet: Iterable[int], optional
            Number of nodes per edge zonelet.
        node_coords: Iterable[float], optional
            Node coordinates describing edges of edge zonelet.
        num_edge_list_per_edge_zonelet: Iterable[int], optional
            Number of edge list per edge zonelet.
        edge_list: Iterable[int], optional
            Edge list describing connectivity of node coordinates.
        num_edges_per_edge_zonelet: Iterable[int], optional
            Number of edges per edge zonelet.
        """
        args = locals()
        [EdgeConnectivityResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of EdgeConnectivityResults.

        Examples
        --------
        >>> EdgeConnectivityResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in EdgeConnectivityResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._edge_zonelet_ids is not None:
            json_data["edgeZoneletIDs"] = self._edge_zonelet_ids
        if self._topo_edge_ids is not None:
            json_data["topoEdgeIDs"] = self._topo_edge_ids
        if self._mesh_edge_ids is not None:
            json_data["meshEdgeIDs"] = self._mesh_edge_ids
        if self._topo_edge_types is not None:
            json_data["topoEdgeTypes"] = self._topo_edge_types
        if self._num_nodes_per_edge_zonelet is not None:
            json_data["numNodesPerEdgeZonelet"] = self._num_nodes_per_edge_zonelet
        if self._node_coords is not None:
            json_data["nodeCoords"] = self._node_coords
        if self._num_edge_list_per_edge_zonelet is not None:
            json_data["numEdgeListPerEdgeZonelet"] = self._num_edge_list_per_edge_zonelet
        if self._edge_list is not None:
            json_data["edgeList"] = self._edge_list
        if self._num_edges_per_edge_zonelet is not None:
            json_data["numEdgesPerEdgeZonelet"] = self._num_edges_per_edge_zonelet
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nedge_zonelet_ids :  %s\ntopo_edge_ids :  %s\nmesh_edge_ids :  %s\ntopo_edge_types :  %s\nnum_nodes_per_edge_zonelet :  %s\nnode_coords :  %s\nnum_edge_list_per_edge_zonelet :  %s\nedge_list :  %s\nnum_edges_per_edge_zonelet :  %s" % (self._error_code, self._edge_zonelet_ids, self._topo_edge_ids, self._mesh_edge_ids, self._topo_edge_types, self._num_nodes_per_edge_zonelet, self._node_coords, self._num_edge_list_per_edge_zonelet, self._edge_list, self._num_edges_per_edge_zonelet)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the get edge connectivity operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def edge_zonelet_ids(self) -> Iterable[int]:
        """Edge zonelet ids for which connectivity data is available.
        """
        return self._edge_zonelet_ids

    @edge_zonelet_ids.setter
    def edge_zonelet_ids(self, value: Iterable[int]):
        self._edge_zonelet_ids = value

    @property
    def topo_edge_ids(self) -> Iterable[int]:
        """TopoEdge ids corresponding to each edge zonelet id for topology based mesh.
        """
        return self._topo_edge_ids

    @topo_edge_ids.setter
    def topo_edge_ids(self, value: Iterable[int]):
        self._topo_edge_ids = value

    @property
    def mesh_edge_ids(self) -> Iterable[int]:
        """Mesh edge ids corresponding to each topoedge.
        """
        return self._mesh_edge_ids

    @mesh_edge_ids.setter
    def mesh_edge_ids(self, value: Iterable[int]):
        self._mesh_edge_ids = value

    @property
    def topo_edge_types(self) -> Iterable[int]:
        """TopoEdge type corresponding to each topoedge.
        """
        return self._topo_edge_types

    @topo_edge_types.setter
    def topo_edge_types(self, value: Iterable[int]):
        self._topo_edge_types = value

    @property
    def num_nodes_per_edge_zonelet(self) -> Iterable[int]:
        """Number of nodes per edge zonelet.
        """
        return self._num_nodes_per_edge_zonelet

    @num_nodes_per_edge_zonelet.setter
    def num_nodes_per_edge_zonelet(self, value: Iterable[int]):
        self._num_nodes_per_edge_zonelet = value

    @property
    def node_coords(self) -> Iterable[float]:
        """Node coordinates describing edges of edge zonelet.
        """
        return self._node_coords

    @node_coords.setter
    def node_coords(self, value: Iterable[float]):
        self._node_coords = value

    @property
    def num_edge_list_per_edge_zonelet(self) -> Iterable[int]:
        """Number of edge list per edge zonelet.
        """
        return self._num_edge_list_per_edge_zonelet

    @num_edge_list_per_edge_zonelet.setter
    def num_edge_list_per_edge_zonelet(self, value: Iterable[int]):
        self._num_edge_list_per_edge_zonelet = value

    @property
    def edge_list(self) -> Iterable[int]:
        """Edge list describing connectivity of node coordinates.
        """
        return self._edge_list

    @edge_list.setter
    def edge_list(self, value: Iterable[int]):
        self._edge_list = value

    @property
    def num_edges_per_edge_zonelet(self) -> Iterable[int]:
        """Number of edges per edge zonelet.
        """
        return self._num_edges_per_edge_zonelet

    @num_edges_per_edge_zonelet.setter
    def num_edges_per_edge_zonelet(self, value: Iterable[int]):
        self._num_edges_per_edge_zonelet = value

class FaceAndEdgeConnectivityResults(CoreObject):
    """Result of the face and edge connectivity information.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            part_ids: Iterable[int],
            face_connectivity_result_per_part: List[FaceConnectivityResults],
            edge_connectivity_result_per_part: List[EdgeConnectivityResults]):
        self._error_code = ErrorCode(error_code)
        self._part_ids = part_ids if isinstance(part_ids, np.ndarray) else np.array(part_ids, dtype=np.int32) if part_ids is not None else None
        self._face_connectivity_result_per_part = face_connectivity_result_per_part
        self._edge_connectivity_result_per_part = edge_connectivity_result_per_part

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            part_ids: Iterable[int] = None,
            face_connectivity_result_per_part: List[FaceConnectivityResults] = None,
            edge_connectivity_result_per_part: List[EdgeConnectivityResults] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FaceAndEdgeConnectivityResults.

        Parameters
        ----------
        model: Model
            Model to create a FaceAndEdgeConnectivityResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the get face and edge connectivity operation.
        part_ids: Iterable[int], optional
            Part ids for which face and edge connectivity data is available.
        face_connectivity_result_per_part: List[FaceConnectivityResults], optional
            Face connectivity result per part.
        edge_connectivity_result_per_part: List[EdgeConnectivityResults], optional
            Edge connectivity result per part.
        json_data: dict, optional
            JSON dictionary to create a FaceAndEdgeConnectivityResults object with provided parameters.

        Examples
        --------
        >>> face_and_edge_connectivity_results = prime.FaceAndEdgeConnectivityResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["partIDs"] if "partIDs" in json_data else None,
                [FaceConnectivityResults(model = model, json_data = data) for data in json_data["faceConnectivityResultPerPart"]] if "faceConnectivityResultPerPart" in json_data else None,
                [EdgeConnectivityResults(model = model, json_data = data) for data in json_data["edgeConnectivityResultPerPart"]] if "edgeConnectivityResultPerPart" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, part_ids, face_connectivity_result_per_part, edge_connectivity_result_per_part])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    part_ids,
                    face_connectivity_result_per_part,
                    edge_connectivity_result_per_part)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "FaceAndEdgeConnectivityResults")
                    json_data = param_json["FaceAndEdgeConnectivityResults"] if "FaceAndEdgeConnectivityResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FaceAndEdgeConnectivityResults._default_params["error_code"] if "error_code" in FaceAndEdgeConnectivityResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        part_ids if part_ids is not None else ( FaceAndEdgeConnectivityResults._default_params["part_ids"] if "part_ids" in FaceAndEdgeConnectivityResults._default_params else (json_data["partIDs"] if "partIDs" in json_data else None)),
                        face_connectivity_result_per_part if face_connectivity_result_per_part is not None else ( FaceAndEdgeConnectivityResults._default_params["face_connectivity_result_per_part"] if "face_connectivity_result_per_part" in FaceAndEdgeConnectivityResults._default_params else [FaceConnectivityResults(model = model, json_data = data) for data in (json_data["faceConnectivityResultPerPart"] if "faceConnectivityResultPerPart" in json_data else None)]),
                        edge_connectivity_result_per_part if edge_connectivity_result_per_part is not None else ( FaceAndEdgeConnectivityResults._default_params["edge_connectivity_result_per_part"] if "edge_connectivity_result_per_part" in FaceAndEdgeConnectivityResults._default_params else [EdgeConnectivityResults(model = model, json_data = data) for data in (json_data["edgeConnectivityResultPerPart"] if "edgeConnectivityResultPerPart" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            part_ids: Iterable[int] = None,
            face_connectivity_result_per_part: List[FaceConnectivityResults] = None,
            edge_connectivity_result_per_part: List[EdgeConnectivityResults] = None):
        """Set the default values of FaceAndEdgeConnectivityResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the get face and edge connectivity operation.
        part_ids: Iterable[int], optional
            Part ids for which face and edge connectivity data is available.
        face_connectivity_result_per_part: List[FaceConnectivityResults], optional
            Face connectivity result per part.
        edge_connectivity_result_per_part: List[EdgeConnectivityResults], optional
            Edge connectivity result per part.
        """
        args = locals()
        [FaceAndEdgeConnectivityResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FaceAndEdgeConnectivityResults.

        Examples
        --------
        >>> FaceAndEdgeConnectivityResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FaceAndEdgeConnectivityResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._part_ids is not None:
            json_data["partIDs"] = self._part_ids
        if self._face_connectivity_result_per_part is not None:
            json_data["faceConnectivityResultPerPart"] = [data._jsonify() for data in self._face_connectivity_result_per_part]
        if self._edge_connectivity_result_per_part is not None:
            json_data["edgeConnectivityResultPerPart"] = [data._jsonify() for data in self._edge_connectivity_result_per_part]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\npart_ids :  %s\nface_connectivity_result_per_part :  %s\nedge_connectivity_result_per_part :  %s" % (self._error_code, self._part_ids, '[' + ''.join('\n' + str(data) for data in self._face_connectivity_result_per_part) + ']', '[' + ''.join('\n' + str(data) for data in self._edge_connectivity_result_per_part) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the get face and edge connectivity operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def part_ids(self) -> Iterable[int]:
        """Part ids for which face and edge connectivity data is available.
        """
        return self._part_ids

    @part_ids.setter
    def part_ids(self, value: Iterable[int]):
        self._part_ids = value

    @property
    def face_connectivity_result_per_part(self) -> List[FaceConnectivityResults]:
        """Face connectivity result per part.
        """
        return self._face_connectivity_result_per_part

    @face_connectivity_result_per_part.setter
    def face_connectivity_result_per_part(self, value: List[FaceConnectivityResults]):
        self._face_connectivity_result_per_part = value

    @property
    def edge_connectivity_result_per_part(self) -> List[EdgeConnectivityResults]:
        """Edge connectivity result per part.
        """
        return self._edge_connectivity_result_per_part

    @edge_connectivity_result_per_part.setter
    def edge_connectivity_result_per_part(self, value: List[EdgeConnectivityResults]):
        self._edge_connectivity_result_per_part = value

class FaceAndEdgeConnectivityParams(CoreObject):
    """Parameters to get face and edge connectivity information.
    """
    _default_params = {}

    def __initialize(
            self,
            reorder_face_zonelets_mid_nodes: bool,
            reorder_edge_zonelets_mid_nodes: bool):
        self._reorder_face_zonelets_mid_nodes = reorder_face_zonelets_mid_nodes
        self._reorder_edge_zonelets_mid_nodes = reorder_edge_zonelets_mid_nodes

    def __init__(
            self,
            model: CommunicationManager=None,
            reorder_face_zonelets_mid_nodes: bool = None,
            reorder_edge_zonelets_mid_nodes: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FaceAndEdgeConnectivityParams.

        Parameters
        ----------
        model: Model
            Model to create a FaceAndEdgeConnectivityParams object with default parameters.
        reorder_face_zonelets_mid_nodes: bool, optional
            Option to reorder mid nodes for quadratic faces.
        reorder_edge_zonelets_mid_nodes: bool, optional
            Option to reorder mid nodes for quadratic edges.
        json_data: dict, optional
            JSON dictionary to create a FaceAndEdgeConnectivityParams object with provided parameters.

        Examples
        --------
        >>> face_and_edge_connectivity_params = prime.FaceAndEdgeConnectivityParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["reorderFaceZoneletsMidNodes"] if "reorderFaceZoneletsMidNodes" in json_data else None,
                json_data["reorderEdgeZoneletsMidNodes"] if "reorderEdgeZoneletsMidNodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [reorder_face_zonelets_mid_nodes, reorder_edge_zonelets_mid_nodes])
            if all_field_specified:
                self.__initialize(
                    reorder_face_zonelets_mid_nodes,
                    reorder_edge_zonelets_mid_nodes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "FaceAndEdgeConnectivityParams")
                    json_data = param_json["FaceAndEdgeConnectivityParams"] if "FaceAndEdgeConnectivityParams" in param_json else {}
                    self.__initialize(
                        reorder_face_zonelets_mid_nodes if reorder_face_zonelets_mid_nodes is not None else ( FaceAndEdgeConnectivityParams._default_params["reorder_face_zonelets_mid_nodes"] if "reorder_face_zonelets_mid_nodes" in FaceAndEdgeConnectivityParams._default_params else (json_data["reorderFaceZoneletsMidNodes"] if "reorderFaceZoneletsMidNodes" in json_data else None)),
                        reorder_edge_zonelets_mid_nodes if reorder_edge_zonelets_mid_nodes is not None else ( FaceAndEdgeConnectivityParams._default_params["reorder_edge_zonelets_mid_nodes"] if "reorder_edge_zonelets_mid_nodes" in FaceAndEdgeConnectivityParams._default_params else (json_data["reorderEdgeZoneletsMidNodes"] if "reorderEdgeZoneletsMidNodes" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            reorder_face_zonelets_mid_nodes: bool = None,
            reorder_edge_zonelets_mid_nodes: bool = None):
        """Set the default values of FaceAndEdgeConnectivityParams.

        Parameters
        ----------
        reorder_face_zonelets_mid_nodes: bool, optional
            Option to reorder mid nodes for quadratic faces.
        reorder_edge_zonelets_mid_nodes: bool, optional
            Option to reorder mid nodes for quadratic edges.
        """
        args = locals()
        [FaceAndEdgeConnectivityParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FaceAndEdgeConnectivityParams.

        Examples
        --------
        >>> FaceAndEdgeConnectivityParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FaceAndEdgeConnectivityParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._reorder_face_zonelets_mid_nodes is not None:
            json_data["reorderFaceZoneletsMidNodes"] = self._reorder_face_zonelets_mid_nodes
        if self._reorder_edge_zonelets_mid_nodes is not None:
            json_data["reorderEdgeZoneletsMidNodes"] = self._reorder_edge_zonelets_mid_nodes
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "reorder_face_zonelets_mid_nodes :  %s\nreorder_edge_zonelets_mid_nodes :  %s" % (self._reorder_face_zonelets_mid_nodes, self._reorder_edge_zonelets_mid_nodes)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def reorder_face_zonelets_mid_nodes(self) -> bool:
        """Option to reorder mid nodes for quadratic faces.
        """
        return self._reorder_face_zonelets_mid_nodes

    @reorder_face_zonelets_mid_nodes.setter
    def reorder_face_zonelets_mid_nodes(self, value: bool):
        self._reorder_face_zonelets_mid_nodes = value

    @property
    def reorder_edge_zonelets_mid_nodes(self) -> bool:
        """Option to reorder mid nodes for quadratic edges.
        """
        return self._reorder_edge_zonelets_mid_nodes

    @reorder_edge_zonelets_mid_nodes.setter
    def reorder_edge_zonelets_mid_nodes(self, value: bool):
        self._reorder_edge_zonelets_mid_nodes = value
