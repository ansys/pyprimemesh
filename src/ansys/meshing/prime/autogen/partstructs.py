""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class CellZoneletType(enum.IntEnum):
    """Types of cell zonelet.
    """
    DEAD = 0
    """Cell zonelet type is dead."""
    FLUID = 1
    """Cell zonelet type is fluid."""
    SOLID = 17
    """Cell zonelet type is solid."""

class ZoneType(enum.IntEnum):
    """ZoneType decides the type of zone.
    """
    EDGE = 1
    """Denotes the zone is edge zone."""
    FACE = 2
    """Denotes the zone is face zone."""
    VOLUME = 3
    """Denotes the zone is volume zone."""

class VolumeNamingType(enum.IntEnum):
    """Indicate source types used to name volumes.
    """
    BYFACELABEL = 1
    """Option to use face label name as source to name volumes."""
    BYFACEZONE = 2
    """Option to use face zone name as source to name volumes."""

class CreateVolumeZonesType(enum.IntEnum):
    """Indicate type to create volume zones for volumes.
    """
    NONE = 0
    """Option to not create volume zones."""
    PERVOLUME = 1
    """Option to create volume zone per volume. Suffix is added to volume zone name, if same name is identified for different volumes using face zonelets."""
    PERNAMESOURCE = 2
    """Option to create zone per name computed from face zonelets of volume. Single zone is created for multiple volumes if same zone name is identified using face zonelets for the volumes."""

class BoundingBox(CoreObject):
    """Provides information about the definition of a bounding box.
    """
    _default_params = {}

    def __initialize(
            self,
            xmin: float,
            ymin: float,
            zmin: float,
            xmax: float,
            ymax: float,
            zmax: float):
        self._xmin = xmin
        self._ymin = ymin
        self._zmin = zmin
        self._xmax = xmax
        self._ymax = ymax
        self._zmax = zmax

    def __init__(
            self,
            model: CommunicationManager=None,
            xmin: float = None,
            ymin: float = None,
            zmin: float = None,
            xmax: float = None,
            ymax: float = None,
            zmax: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the BoundingBox.

        Parameters
        ----------
        model: Model
            Model to create a BoundingBox object with default parameters.
        xmin: float, optional
            Minimal X coordinate of the bounding box.
        ymin: float, optional
            Minimal Y coordinate of the bounding box.
        zmin: float, optional
            Minimal Z coordinate of the bounding box.
        xmax: float, optional
            Maximal X coordinate of the bounding box.
        ymax: float, optional
            Maximal Y coordinate of the bounding box.
        zmax: float, optional
            Maximal Z coordinate of the bounding box.
        json_data: dict, optional
            JSON dictionary to create a BoundingBox object with provided parameters.

        Examples
        --------
        >>> bounding_box = prime.BoundingBox(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["xmin"] if "xmin" in json_data else None,
                json_data["ymin"] if "ymin" in json_data else None,
                json_data["zmin"] if "zmin" in json_data else None,
                json_data["xmax"] if "xmax" in json_data else None,
                json_data["ymax"] if "ymax" in json_data else None,
                json_data["zmax"] if "zmax" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [xmin, ymin, zmin, xmax, ymax, zmax])
            if all_field_specified:
                self.__initialize(
                    xmin,
                    ymin,
                    zmin,
                    xmax,
                    ymax,
                    zmax)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "BoundingBox")
                    json_data = param_json["BoundingBox"] if "BoundingBox" in param_json else {}
                    self.__initialize(
                        xmin if xmin is not None else ( BoundingBox._default_params["xmin"] if "xmin" in BoundingBox._default_params else (json_data["xmin"] if "xmin" in json_data else None)),
                        ymin if ymin is not None else ( BoundingBox._default_params["ymin"] if "ymin" in BoundingBox._default_params else (json_data["ymin"] if "ymin" in json_data else None)),
                        zmin if zmin is not None else ( BoundingBox._default_params["zmin"] if "zmin" in BoundingBox._default_params else (json_data["zmin"] if "zmin" in json_data else None)),
                        xmax if xmax is not None else ( BoundingBox._default_params["xmax"] if "xmax" in BoundingBox._default_params else (json_data["xmax"] if "xmax" in json_data else None)),
                        ymax if ymax is not None else ( BoundingBox._default_params["ymax"] if "ymax" in BoundingBox._default_params else (json_data["ymax"] if "ymax" in json_data else None)),
                        zmax if zmax is not None else ( BoundingBox._default_params["zmax"] if "zmax" in BoundingBox._default_params else (json_data["zmax"] if "zmax" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            xmin: float = None,
            ymin: float = None,
            zmin: float = None,
            xmax: float = None,
            ymax: float = None,
            zmax: float = None):
        """Set the default values of BoundingBox.

        Parameters
        ----------
        xmin: float, optional
            Minimal X coordinate of the bounding box.
        ymin: float, optional
            Minimal Y coordinate of the bounding box.
        zmin: float, optional
            Minimal Z coordinate of the bounding box.
        xmax: float, optional
            Maximal X coordinate of the bounding box.
        ymax: float, optional
            Maximal Y coordinate of the bounding box.
        zmax: float, optional
            Maximal Z coordinate of the bounding box.
        """
        args = locals()
        [BoundingBox._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of BoundingBox.

        Examples
        --------
        >>> BoundingBox.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in BoundingBox._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._xmin is not None:
            json_data["xmin"] = self._xmin
        if self._ymin is not None:
            json_data["ymin"] = self._ymin
        if self._zmin is not None:
            json_data["zmin"] = self._zmin
        if self._xmax is not None:
            json_data["xmax"] = self._xmax
        if self._ymax is not None:
            json_data["ymax"] = self._ymax
        if self._zmax is not None:
            json_data["zmax"] = self._zmax
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "xmin :  %s\nymin :  %s\nzmin :  %s\nxmax :  %s\nymax :  %s\nzmax :  %s" % (self._xmin, self._ymin, self._zmin, self._xmax, self._ymax, self._zmax)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def xmin(self) -> float:
        """Minimal X coordinate of the bounding box.
        """
        return self._xmin

    @xmin.setter
    def xmin(self, value: float):
        self._xmin = value

    @property
    def ymin(self) -> float:
        """Minimal Y coordinate of the bounding box.
        """
        return self._ymin

    @ymin.setter
    def ymin(self, value: float):
        self._ymin = value

    @property
    def zmin(self) -> float:
        """Minimal Z coordinate of the bounding box.
        """
        return self._zmin

    @zmin.setter
    def zmin(self, value: float):
        self._zmin = value

    @property
    def xmax(self) -> float:
        """Maximal X coordinate of the bounding box.
        """
        return self._xmax

    @xmax.setter
    def xmax(self, value: float):
        self._xmax = value

    @property
    def ymax(self) -> float:
        """Maximal Y coordinate of the bounding box.
        """
        return self._ymax

    @ymax.setter
    def ymax(self, value: float):
        self._ymax = value

    @property
    def zmax(self) -> float:
        """Maximal Z coordinate of the bounding box.
        """
        return self._zmax

    @zmax.setter
    def zmax(self, value: float):
        self._zmax = value

class MergeZoneletsResults(CoreObject):
    """Results associated with merge zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            merged_zonelets: Iterable[int],
            error_code: ErrorCode):
        self._merged_zonelets = merged_zonelets if isinstance(merged_zonelets, np.ndarray) else np.array(merged_zonelets, dtype=np.int32) if merged_zonelets is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            merged_zonelets: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergeZoneletsResults.

        Parameters
        ----------
        model: Model
            Model to create a MergeZoneletsResults object with default parameters.
        merged_zonelets: Iterable[int], optional
            Ids of zonelets to which input zonelets are merged.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a MergeZoneletsResults object with provided parameters.

        Examples
        --------
        >>> merge_zonelets_results = prime.MergeZoneletsResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["mergedZonelets"] if "mergedZonelets" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [merged_zonelets, error_code])
            if all_field_specified:
                self.__initialize(
                    merged_zonelets,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergeZoneletsResults")
                    json_data = param_json["MergeZoneletsResults"] if "MergeZoneletsResults" in param_json else {}
                    self.__initialize(
                        merged_zonelets if merged_zonelets is not None else ( MergeZoneletsResults._default_params["merged_zonelets"] if "merged_zonelets" in MergeZoneletsResults._default_params else (json_data["mergedZonelets"] if "mergedZonelets" in json_data else None)),
                        error_code if error_code is not None else ( MergeZoneletsResults._default_params["error_code"] if "error_code" in MergeZoneletsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            merged_zonelets: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of MergeZoneletsResults.

        Parameters
        ----------
        merged_zonelets: Iterable[int], optional
            Ids of zonelets to which input zonelets are merged.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [MergeZoneletsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergeZoneletsResults.

        Examples
        --------
        >>> MergeZoneletsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergeZoneletsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._merged_zonelets is not None:
            json_data["mergedZonelets"] = self._merged_zonelets
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "merged_zonelets :  %s\nerror_code :  %s" % (self._merged_zonelets, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def merged_zonelets(self) -> Iterable[int]:
        """Ids of zonelets to which input zonelets are merged.
        """
        return self._merged_zonelets

    @merged_zonelets.setter
    def merged_zonelets(self, value: Iterable[int]):
        self._merged_zonelets = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class MergeZoneletsParams(CoreObject):
    """Parameters to merge zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            merge_small_zonelets_with_neighbors: bool,
            element_count_limit: int):
        self._merge_small_zonelets_with_neighbors = merge_small_zonelets_with_neighbors
        self._element_count_limit = element_count_limit

    def __init__(
            self,
            model: CommunicationManager=None,
            merge_small_zonelets_with_neighbors: bool = None,
            element_count_limit: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergeZoneletsParams.

        Parameters
        ----------
        model: Model
            Model to create a MergeZoneletsParams object with default parameters.
        merge_small_zonelets_with_neighbors: bool, optional
            Merge zonelets with element count smaller than the given element count limit to neighboring zonelets sharing manifold face edges. Notes: Works better if zonelets are separated by region.
        element_count_limit: int, optional
            Element count limit to identify small zonelets.
        json_data: dict, optional
            JSON dictionary to create a MergeZoneletsParams object with provided parameters.

        Examples
        --------
        >>> merge_zonelets_params = prime.MergeZoneletsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["mergeSmallZoneletsWithNeighbors"] if "mergeSmallZoneletsWithNeighbors" in json_data else None,
                json_data["elementCountLimit"] if "elementCountLimit" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [merge_small_zonelets_with_neighbors, element_count_limit])
            if all_field_specified:
                self.__initialize(
                    merge_small_zonelets_with_neighbors,
                    element_count_limit)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergeZoneletsParams")
                    json_data = param_json["MergeZoneletsParams"] if "MergeZoneletsParams" in param_json else {}
                    self.__initialize(
                        merge_small_zonelets_with_neighbors if merge_small_zonelets_with_neighbors is not None else ( MergeZoneletsParams._default_params["merge_small_zonelets_with_neighbors"] if "merge_small_zonelets_with_neighbors" in MergeZoneletsParams._default_params else (json_data["mergeSmallZoneletsWithNeighbors"] if "mergeSmallZoneletsWithNeighbors" in json_data else None)),
                        element_count_limit if element_count_limit is not None else ( MergeZoneletsParams._default_params["element_count_limit"] if "element_count_limit" in MergeZoneletsParams._default_params else (json_data["elementCountLimit"] if "elementCountLimit" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            merge_small_zonelets_with_neighbors: bool = None,
            element_count_limit: int = None):
        """Set the default values of MergeZoneletsParams.

        Parameters
        ----------
        merge_small_zonelets_with_neighbors: bool, optional
            Merge zonelets with element count smaller than the given element count limit to neighboring zonelets sharing manifold face edges. Notes: Works better if zonelets are separated by region.
        element_count_limit: int, optional
            Element count limit to identify small zonelets.
        """
        args = locals()
        [MergeZoneletsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergeZoneletsParams.

        Examples
        --------
        >>> MergeZoneletsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergeZoneletsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._merge_small_zonelets_with_neighbors is not None:
            json_data["mergeSmallZoneletsWithNeighbors"] = self._merge_small_zonelets_with_neighbors
        if self._element_count_limit is not None:
            json_data["elementCountLimit"] = self._element_count_limit
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "merge_small_zonelets_with_neighbors :  %s\nelement_count_limit :  %s" % (self._merge_small_zonelets_with_neighbors, self._element_count_limit)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def merge_small_zonelets_with_neighbors(self) -> bool:
        """Merge zonelets with element count smaller than the given element count limit to neighboring zonelets sharing manifold face edges. Notes: Works better if zonelets are separated by region.
        """
        return self._merge_small_zonelets_with_neighbors

    @merge_small_zonelets_with_neighbors.setter
    def merge_small_zonelets_with_neighbors(self, value: bool):
        self._merge_small_zonelets_with_neighbors = value

    @property
    def element_count_limit(self) -> int:
        """Element count limit to identify small zonelets.
        """
        return self._element_count_limit

    @element_count_limit.setter
    def element_count_limit(self, value: int):
        self._element_count_limit = value

class ComputeVolumesResults(CoreObject):
    """Results associated with compute volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            error_locations: Iterable[float],
            volumes: Iterable[int],
            material_point_volumes: Iterable[int],
            external_open_face_zonelets: Iterable[int],
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._error_locations = error_locations if isinstance(error_locations, np.ndarray) else np.array(error_locations, dtype=np.double) if error_locations is not None else None
        self._volumes = volumes if isinstance(volumes, np.ndarray) else np.array(volumes, dtype=np.int32) if volumes is not None else None
        self._material_point_volumes = material_point_volumes if isinstance(material_point_volumes, np.ndarray) else np.array(material_point_volumes, dtype=np.int32) if material_point_volumes is not None else None
        self._external_open_face_zonelets = external_open_face_zonelets if isinstance(external_open_face_zonelets, np.ndarray) else np.array(external_open_face_zonelets, dtype=np.int32) if external_open_face_zonelets is not None else None
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            volumes: Iterable[int] = None,
            material_point_volumes: Iterable[int] = None,
            external_open_face_zonelets: Iterable[int] = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ComputeVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a ComputeVolumesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        volumes: Iterable[int], optional
            Ids of computed volumes.
        material_point_volumes: Iterable[int], optional
            Ids of computed volumes enclosing material points.
        external_open_face_zonelets: Iterable[int], optional
            Face zonelet ids that are in external space and not part of any computed volumes.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute volumes.
        json_data: dict, optional
            JSON dictionary to create a ComputeVolumesResults object with provided parameters.

        Examples
        --------
        >>> compute_volumes_results = prime.ComputeVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["errorLocations"] if "errorLocations" in json_data else None,
                json_data["volumes"] if "volumes" in json_data else None,
                json_data["materialPointVolumes"] if "materialPointVolumes" in json_data else None,
                json_data["externalOpenFaceZonelets"] if "externalOpenFaceZonelets" in json_data else None,
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, error_locations, volumes, material_point_volumes, external_open_face_zonelets, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    error_locations,
                    volumes,
                    material_point_volumes,
                    external_open_face_zonelets,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ComputeVolumesResults")
                    json_data = param_json["ComputeVolumesResults"] if "ComputeVolumesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ComputeVolumesResults._default_params["error_code"] if "error_code" in ComputeVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        error_locations if error_locations is not None else ( ComputeVolumesResults._default_params["error_locations"] if "error_locations" in ComputeVolumesResults._default_params else (json_data["errorLocations"] if "errorLocations" in json_data else None)),
                        volumes if volumes is not None else ( ComputeVolumesResults._default_params["volumes"] if "volumes" in ComputeVolumesResults._default_params else (json_data["volumes"] if "volumes" in json_data else None)),
                        material_point_volumes if material_point_volumes is not None else ( ComputeVolumesResults._default_params["material_point_volumes"] if "material_point_volumes" in ComputeVolumesResults._default_params else (json_data["materialPointVolumes"] if "materialPointVolumes" in json_data else None)),
                        external_open_face_zonelets if external_open_face_zonelets is not None else ( ComputeVolumesResults._default_params["external_open_face_zonelets"] if "external_open_face_zonelets" in ComputeVolumesResults._default_params else (json_data["externalOpenFaceZonelets"] if "externalOpenFaceZonelets" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ComputeVolumesResults._default_params["warning_codes"] if "warning_codes" in ComputeVolumesResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            volumes: Iterable[int] = None,
            material_point_volumes: Iterable[int] = None,
            external_open_face_zonelets: Iterable[int] = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of ComputeVolumesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        volumes: Iterable[int], optional
            Ids of computed volumes.
        material_point_volumes: Iterable[int], optional
            Ids of computed volumes enclosing material points.
        external_open_face_zonelets: Iterable[int], optional
            Face zonelet ids that are in external space and not part of any computed volumes.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute volumes.
        """
        args = locals()
        [ComputeVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ComputeVolumesResults.

        Examples
        --------
        >>> ComputeVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ComputeVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._error_locations is not None:
            json_data["errorLocations"] = self._error_locations
        if self._volumes is not None:
            json_data["volumes"] = self._volumes
        if self._material_point_volumes is not None:
            json_data["materialPointVolumes"] = self._material_point_volumes
        if self._external_open_face_zonelets is not None:
            json_data["externalOpenFaceZonelets"] = self._external_open_face_zonelets
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nerror_locations :  %s\nvolumes :  %s\nmaterial_point_volumes :  %s\nexternal_open_face_zonelets :  %s\nwarning_codes :  %s" % (self._error_code, self._error_locations, self._volumes, self._material_point_volumes, self._external_open_face_zonelets, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def error_locations(self) -> Iterable[float]:
        """Coordinates of problematic locations in the surface mesh.
        """
        return self._error_locations

    @error_locations.setter
    def error_locations(self, value: Iterable[float]):
        self._error_locations = value

    @property
    def volumes(self) -> Iterable[int]:
        """Ids of computed volumes.
        """
        return self._volumes

    @volumes.setter
    def volumes(self, value: Iterable[int]):
        self._volumes = value

    @property
    def material_point_volumes(self) -> Iterable[int]:
        """Ids of computed volumes enclosing material points.
        """
        return self._material_point_volumes

    @material_point_volumes.setter
    def material_point_volumes(self, value: Iterable[int]):
        self._material_point_volumes = value

    @property
    def external_open_face_zonelets(self) -> Iterable[int]:
        """Face zonelet ids that are in external space and not part of any computed volumes.
        """
        return self._external_open_face_zonelets

    @external_open_face_zonelets.setter
    def external_open_face_zonelets(self, value: Iterable[int]):
        self._external_open_face_zonelets = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the compute volumes.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ComputeTopoVolumesResults(CoreObject):
    """Results associated with compute topovolumes.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            error_locations: Iterable[float],
            topo_volumes: Iterable[int],
            material_point_topo_volumes: Iterable[int],
            external_open_topo_faces: Iterable[int],
            new_topo_volumes: Iterable[int],
            deleted_topo_volumes: Iterable[int],
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._error_locations = error_locations if isinstance(error_locations, np.ndarray) else np.array(error_locations, dtype=np.double) if error_locations is not None else None
        self._topo_volumes = topo_volumes if isinstance(topo_volumes, np.ndarray) else np.array(topo_volumes, dtype=np.int32) if topo_volumes is not None else None
        self._material_point_topo_volumes = material_point_topo_volumes if isinstance(material_point_topo_volumes, np.ndarray) else np.array(material_point_topo_volumes, dtype=np.int32) if material_point_topo_volumes is not None else None
        self._external_open_topo_faces = external_open_topo_faces if isinstance(external_open_topo_faces, np.ndarray) else np.array(external_open_topo_faces, dtype=np.int32) if external_open_topo_faces is not None else None
        self._new_topo_volumes = new_topo_volumes if isinstance(new_topo_volumes, np.ndarray) else np.array(new_topo_volumes, dtype=np.int32) if new_topo_volumes is not None else None
        self._deleted_topo_volumes = deleted_topo_volumes if isinstance(deleted_topo_volumes, np.ndarray) else np.array(deleted_topo_volumes, dtype=np.int32) if deleted_topo_volumes is not None else None
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            topo_volumes: Iterable[int] = None,
            material_point_topo_volumes: Iterable[int] = None,
            external_open_topo_faces: Iterable[int] = None,
            new_topo_volumes: Iterable[int] = None,
            deleted_topo_volumes: Iterable[int] = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ComputeTopoVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a ComputeTopoVolumesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        topo_volumes: Iterable[int], optional
            Ids of all topovolumes computed.
        material_point_topo_volumes: Iterable[int], optional
            Ids of topovolumes enclosing material points.
        external_open_topo_faces: Iterable[int], optional
            Topoface ids that are in external space and not part of any topovolumes.
        new_topo_volumes: Iterable[int], optional
            Ids of new topovolumes computed.
        deleted_topo_volumes: Iterable[int], optional
            Ids of existing topovolumes that got deleted.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute topovolumes.
        json_data: dict, optional
            JSON dictionary to create a ComputeTopoVolumesResults object with provided parameters.

        Examples
        --------
        >>> compute_topo_volumes_results = prime.ComputeTopoVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["errorLocations"] if "errorLocations" in json_data else None,
                json_data["topoVolumes"] if "topoVolumes" in json_data else None,
                json_data["materialPointTopoVolumes"] if "materialPointTopoVolumes" in json_data else None,
                json_data["externalOpenTopoFaces"] if "externalOpenTopoFaces" in json_data else None,
                json_data["newTopoVolumes"] if "newTopoVolumes" in json_data else None,
                json_data["deletedTopoVolumes"] if "deletedTopoVolumes" in json_data else None,
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, error_locations, topo_volumes, material_point_topo_volumes, external_open_topo_faces, new_topo_volumes, deleted_topo_volumes, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    error_locations,
                    topo_volumes,
                    material_point_topo_volumes,
                    external_open_topo_faces,
                    new_topo_volumes,
                    deleted_topo_volumes,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ComputeTopoVolumesResults")
                    json_data = param_json["ComputeTopoVolumesResults"] if "ComputeTopoVolumesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ComputeTopoVolumesResults._default_params["error_code"] if "error_code" in ComputeTopoVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        error_locations if error_locations is not None else ( ComputeTopoVolumesResults._default_params["error_locations"] if "error_locations" in ComputeTopoVolumesResults._default_params else (json_data["errorLocations"] if "errorLocations" in json_data else None)),
                        topo_volumes if topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["topo_volumes"] if "topo_volumes" in ComputeTopoVolumesResults._default_params else (json_data["topoVolumes"] if "topoVolumes" in json_data else None)),
                        material_point_topo_volumes if material_point_topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["material_point_topo_volumes"] if "material_point_topo_volumes" in ComputeTopoVolumesResults._default_params else (json_data["materialPointTopoVolumes"] if "materialPointTopoVolumes" in json_data else None)),
                        external_open_topo_faces if external_open_topo_faces is not None else ( ComputeTopoVolumesResults._default_params["external_open_topo_faces"] if "external_open_topo_faces" in ComputeTopoVolumesResults._default_params else (json_data["externalOpenTopoFaces"] if "externalOpenTopoFaces" in json_data else None)),
                        new_topo_volumes if new_topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["new_topo_volumes"] if "new_topo_volumes" in ComputeTopoVolumesResults._default_params else (json_data["newTopoVolumes"] if "newTopoVolumes" in json_data else None)),
                        deleted_topo_volumes if deleted_topo_volumes is not None else ( ComputeTopoVolumesResults._default_params["deleted_topo_volumes"] if "deleted_topo_volumes" in ComputeTopoVolumesResults._default_params else (json_data["deletedTopoVolumes"] if "deletedTopoVolumes" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ComputeTopoVolumesResults._default_params["warning_codes"] if "warning_codes" in ComputeTopoVolumesResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            error_locations: Iterable[float] = None,
            topo_volumes: Iterable[int] = None,
            material_point_topo_volumes: Iterable[int] = None,
            external_open_topo_faces: Iterable[int] = None,
            new_topo_volumes: Iterable[int] = None,
            deleted_topo_volumes: Iterable[int] = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of ComputeTopoVolumesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        error_locations: Iterable[float], optional
            Coordinates of problematic locations in the surface mesh.
        topo_volumes: Iterable[int], optional
            Ids of all topovolumes computed.
        material_point_topo_volumes: Iterable[int], optional
            Ids of topovolumes enclosing material points.
        external_open_topo_faces: Iterable[int], optional
            Topoface ids that are in external space and not part of any topovolumes.
        new_topo_volumes: Iterable[int], optional
            Ids of new topovolumes computed.
        deleted_topo_volumes: Iterable[int], optional
            Ids of existing topovolumes that got deleted.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute topovolumes.
        """
        args = locals()
        [ComputeTopoVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ComputeTopoVolumesResults.

        Examples
        --------
        >>> ComputeTopoVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ComputeTopoVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._error_locations is not None:
            json_data["errorLocations"] = self._error_locations
        if self._topo_volumes is not None:
            json_data["topoVolumes"] = self._topo_volumes
        if self._material_point_topo_volumes is not None:
            json_data["materialPointTopoVolumes"] = self._material_point_topo_volumes
        if self._external_open_topo_faces is not None:
            json_data["externalOpenTopoFaces"] = self._external_open_topo_faces
        if self._new_topo_volumes is not None:
            json_data["newTopoVolumes"] = self._new_topo_volumes
        if self._deleted_topo_volumes is not None:
            json_data["deletedTopoVolumes"] = self._deleted_topo_volumes
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nerror_locations :  %s\ntopo_volumes :  %s\nmaterial_point_topo_volumes :  %s\nexternal_open_topo_faces :  %s\nnew_topo_volumes :  %s\ndeleted_topo_volumes :  %s\nwarning_codes :  %s" % (self._error_code, self._error_locations, self._topo_volumes, self._material_point_topo_volumes, self._external_open_topo_faces, self._new_topo_volumes, self._deleted_topo_volumes, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def error_locations(self) -> Iterable[float]:
        """Coordinates of problematic locations in the surface mesh.
        """
        return self._error_locations

    @error_locations.setter
    def error_locations(self, value: Iterable[float]):
        self._error_locations = value

    @property
    def topo_volumes(self) -> Iterable[int]:
        """Ids of all topovolumes computed.
        """
        return self._topo_volumes

    @topo_volumes.setter
    def topo_volumes(self, value: Iterable[int]):
        self._topo_volumes = value

    @property
    def material_point_topo_volumes(self) -> Iterable[int]:
        """Ids of topovolumes enclosing material points.
        """
        return self._material_point_topo_volumes

    @material_point_topo_volumes.setter
    def material_point_topo_volumes(self, value: Iterable[int]):
        self._material_point_topo_volumes = value

    @property
    def external_open_topo_faces(self) -> Iterable[int]:
        """Topoface ids that are in external space and not part of any topovolumes.
        """
        return self._external_open_topo_faces

    @external_open_topo_faces.setter
    def external_open_topo_faces(self, value: Iterable[int]):
        self._external_open_topo_faces = value

    @property
    def new_topo_volumes(self) -> Iterable[int]:
        """Ids of new topovolumes computed.
        """
        return self._new_topo_volumes

    @new_topo_volumes.setter
    def new_topo_volumes(self, value: Iterable[int]):
        self._new_topo_volumes = value

    @property
    def deleted_topo_volumes(self) -> Iterable[int]:
        """Ids of existing topovolumes that got deleted.
        """
        return self._deleted_topo_volumes

    @deleted_topo_volumes.setter
    def deleted_topo_volumes(self, value: Iterable[int]):
        self._deleted_topo_volumes = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the compute topovolumes.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ExtractVolumesResults(CoreObject):
    """Results associated with compute volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            volumes: Iterable[int],
            warning_codes: List[WarningCode],
            assigned_zone_name: str,
            face_zonelets_without_volumes: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._volumes = volumes if isinstance(volumes, np.ndarray) else np.array(volumes, dtype=np.int32) if volumes is not None else None
        self._warning_codes = warning_codes
        self._assigned_zone_name = assigned_zone_name
        self._face_zonelets_without_volumes = face_zonelets_without_volumes if isinstance(face_zonelets_without_volumes, np.ndarray) else np.array(face_zonelets_without_volumes, dtype=np.int32) if face_zonelets_without_volumes is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            volumes: Iterable[int] = None,
            warning_codes: List[WarningCode] = None,
            assigned_zone_name: str = None,
            face_zonelets_without_volumes: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a ExtractVolumesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        volumes: Iterable[int], optional
            Ids of computed volumes.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute volumes.
        assigned_zone_name: str, optional
            Assigned name of zone for extracted flow volumes.
        face_zonelets_without_volumes: Iterable[int], optional
            Ids of face zonelets for which volumes were not extracted.
        json_data: dict, optional
            JSON dictionary to create a ExtractVolumesResults object with provided parameters.

        Examples
        --------
        >>> extract_volumes_results = prime.ExtractVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["volumes"] if "volumes" in json_data else None,
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None,
                json_data["assignedZoneName"] if "assignedZoneName" in json_data else None,
                json_data["faceZoneletsWithoutVolumes"] if "faceZoneletsWithoutVolumes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, volumes, warning_codes, assigned_zone_name, face_zonelets_without_volumes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    volumes,
                    warning_codes,
                    assigned_zone_name,
                    face_zonelets_without_volumes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractVolumesResults")
                    json_data = param_json["ExtractVolumesResults"] if "ExtractVolumesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ExtractVolumesResults._default_params["error_code"] if "error_code" in ExtractVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        volumes if volumes is not None else ( ExtractVolumesResults._default_params["volumes"] if "volumes" in ExtractVolumesResults._default_params else (json_data["volumes"] if "volumes" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ExtractVolumesResults._default_params["warning_codes"] if "warning_codes" in ExtractVolumesResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]),
                        assigned_zone_name if assigned_zone_name is not None else ( ExtractVolumesResults._default_params["assigned_zone_name"] if "assigned_zone_name" in ExtractVolumesResults._default_params else (json_data["assignedZoneName"] if "assignedZoneName" in json_data else None)),
                        face_zonelets_without_volumes if face_zonelets_without_volumes is not None else ( ExtractVolumesResults._default_params["face_zonelets_without_volumes"] if "face_zonelets_without_volumes" in ExtractVolumesResults._default_params else (json_data["faceZoneletsWithoutVolumes"] if "faceZoneletsWithoutVolumes" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            volumes: Iterable[int] = None,
            warning_codes: List[WarningCode] = None,
            assigned_zone_name: str = None,
            face_zonelets_without_volumes: Iterable[int] = None):
        """Set the default values of ExtractVolumesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        volumes: Iterable[int], optional
            Ids of computed volumes.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the compute volumes.
        assigned_zone_name: str, optional
            Assigned name of zone for extracted flow volumes.
        face_zonelets_without_volumes: Iterable[int], optional
            Ids of face zonelets for which volumes were not extracted.
        """
        args = locals()
        [ExtractVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractVolumesResults.

        Examples
        --------
        >>> ExtractVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._volumes is not None:
            json_data["volumes"] = self._volumes
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        if self._assigned_zone_name is not None:
            json_data["assignedZoneName"] = self._assigned_zone_name
        if self._face_zonelets_without_volumes is not None:
            json_data["faceZoneletsWithoutVolumes"] = self._face_zonelets_without_volumes
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nvolumes :  %s\nwarning_codes :  %s\nassigned_zone_name :  %s\nface_zonelets_without_volumes :  %s" % (self._error_code, self._volumes, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._assigned_zone_name, self._face_zonelets_without_volumes)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def volumes(self) -> Iterable[int]:
        """Ids of computed volumes.
        """
        return self._volumes

    @volumes.setter
    def volumes(self, value: Iterable[int]):
        self._volumes = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the compute volumes.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def assigned_zone_name(self) -> str:
        """Assigned name of zone for extracted flow volumes.
        """
        return self._assigned_zone_name

    @assigned_zone_name.setter
    def assigned_zone_name(self, value: str):
        self._assigned_zone_name = value

    @property
    def face_zonelets_without_volumes(self) -> Iterable[int]:
        """Ids of face zonelets for which volumes were not extracted.
        """
        return self._face_zonelets_without_volumes

    @face_zonelets_without_volumes.setter
    def face_zonelets_without_volumes(self, value: Iterable[int]):
        self._face_zonelets_without_volumes = value

class ComputeVolumesParams(CoreObject):
    """Parameters to compute volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            volume_naming_type: VolumeNamingType,
            create_zones_type: CreateVolumeZonesType,
            priority_ordered_names: List[str],
            material_point_names: List[str]):
        self._volume_naming_type = VolumeNamingType(volume_naming_type)
        self._create_zones_type = CreateVolumeZonesType(create_zones_type)
        self._priority_ordered_names = priority_ordered_names
        self._material_point_names = material_point_names

    def __init__(
            self,
            model: CommunicationManager=None,
            volume_naming_type: VolumeNamingType = None,
            create_zones_type: CreateVolumeZonesType = None,
            priority_ordered_names: List[str] = None,
            material_point_names: List[str] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ComputeVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a ComputeVolumesParams object with default parameters.
        volume_naming_type: VolumeNamingType, optional
            Indicates source type used to compute zone name for volumes.
        create_zones_type: CreateVolumeZonesType, optional
            Option to control volume zone creation for volumes.
        priority_ordered_names: List[str], optional
            Zone names for volumes are identified based on the priority in the list. Position index of name in the list determines its priority. Lower the index, higher the priority. Name with highest priority among names from volumeNamingType of face zonelets is identified as zone name for volume. Lowest priority is assigned to all names that are not in the list. When all names identified are of lowest priority, names having higher surface area of faces zonelets are identified as zone name for volume.
        material_point_names: List[str], optional
            Material point names provided to identify volumes. Material point names will have precedence over the volume names.
        json_data: dict, optional
            JSON dictionary to create a ComputeVolumesParams object with provided parameters.

        Examples
        --------
        >>> compute_volumes_params = prime.ComputeVolumesParams(model = model)
        """
        if json_data:
            self.__initialize(
                VolumeNamingType(json_data["volumeNamingType"] if "volumeNamingType" in json_data else None),
                CreateVolumeZonesType(json_data["createZonesType"] if "createZonesType" in json_data else None),
                json_data["priorityOrderedNames"] if "priorityOrderedNames" in json_data else None,
                json_data["materialPointNames"] if "materialPointNames" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [volume_naming_type, create_zones_type, priority_ordered_names, material_point_names])
            if all_field_specified:
                self.__initialize(
                    volume_naming_type,
                    create_zones_type,
                    priority_ordered_names,
                    material_point_names)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ComputeVolumesParams")
                    json_data = param_json["ComputeVolumesParams"] if "ComputeVolumesParams" in param_json else {}
                    self.__initialize(
                        volume_naming_type if volume_naming_type is not None else ( ComputeVolumesParams._default_params["volume_naming_type"] if "volume_naming_type" in ComputeVolumesParams._default_params else VolumeNamingType(json_data["volumeNamingType"] if "volumeNamingType" in json_data else None)),
                        create_zones_type if create_zones_type is not None else ( ComputeVolumesParams._default_params["create_zones_type"] if "create_zones_type" in ComputeVolumesParams._default_params else CreateVolumeZonesType(json_data["createZonesType"] if "createZonesType" in json_data else None)),
                        priority_ordered_names if priority_ordered_names is not None else ( ComputeVolumesParams._default_params["priority_ordered_names"] if "priority_ordered_names" in ComputeVolumesParams._default_params else (json_data["priorityOrderedNames"] if "priorityOrderedNames" in json_data else None)),
                        material_point_names if material_point_names is not None else ( ComputeVolumesParams._default_params["material_point_names"] if "material_point_names" in ComputeVolumesParams._default_params else (json_data["materialPointNames"] if "materialPointNames" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            volume_naming_type: VolumeNamingType = None,
            create_zones_type: CreateVolumeZonesType = None,
            priority_ordered_names: List[str] = None,
            material_point_names: List[str] = None):
        """Set the default values of ComputeVolumesParams.

        Parameters
        ----------
        volume_naming_type: VolumeNamingType, optional
            Indicates source type used to compute zone name for volumes.
        create_zones_type: CreateVolumeZonesType, optional
            Option to control volume zone creation for volumes.
        priority_ordered_names: List[str], optional
            Zone names for volumes are identified based on the priority in the list. Position index of name in the list determines its priority. Lower the index, higher the priority. Name with highest priority among names from volumeNamingType of face zonelets is identified as zone name for volume. Lowest priority is assigned to all names that are not in the list. When all names identified are of lowest priority, names having higher surface area of faces zonelets are identified as zone name for volume.
        material_point_names: List[str], optional
            Material point names provided to identify volumes. Material point names will have precedence over the volume names.
        """
        args = locals()
        [ComputeVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ComputeVolumesParams.

        Examples
        --------
        >>> ComputeVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ComputeVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._volume_naming_type is not None:
            json_data["volumeNamingType"] = self._volume_naming_type
        if self._create_zones_type is not None:
            json_data["createZonesType"] = self._create_zones_type
        if self._priority_ordered_names is not None:
            json_data["priorityOrderedNames"] = self._priority_ordered_names
        if self._material_point_names is not None:
            json_data["materialPointNames"] = self._material_point_names
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "volume_naming_type :  %s\ncreate_zones_type :  %s\npriority_ordered_names :  %s\nmaterial_point_names :  %s" % (self._volume_naming_type, self._create_zones_type, self._priority_ordered_names, self._material_point_names)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def volume_naming_type(self) -> VolumeNamingType:
        """Indicates source type used to compute zone name for volumes.
        """
        return self._volume_naming_type

    @volume_naming_type.setter
    def volume_naming_type(self, value: VolumeNamingType):
        self._volume_naming_type = value

    @property
    def create_zones_type(self) -> CreateVolumeZonesType:
        """Option to control volume zone creation for volumes.
        """
        return self._create_zones_type

    @create_zones_type.setter
    def create_zones_type(self, value: CreateVolumeZonesType):
        self._create_zones_type = value

    @property
    def priority_ordered_names(self) -> List[str]:
        """Zone names for volumes are identified based on the priority in the list. Position index of name in the list determines its priority. Lower the index, higher the priority. Name with highest priority among names from volumeNamingType of face zonelets is identified as zone name for volume. Lowest priority is assigned to all names that are not in the list. When all names identified are of lowest priority, names having higher surface area of faces zonelets are identified as zone name for volume.
        """
        return self._priority_ordered_names

    @priority_ordered_names.setter
    def priority_ordered_names(self, value: List[str]):
        self._priority_ordered_names = value

    @property
    def material_point_names(self) -> List[str]:
        """Material point names provided to identify volumes. Material point names will have precedence over the volume names.
        """
        return self._material_point_names

    @material_point_names.setter
    def material_point_names(self, value: List[str]):
        self._material_point_names = value

class ExtractVolumesParams(CoreObject):
    """Parameters to extract flow volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            create_zone: bool,
            suggested_zone_name: str):
        self._create_zone = create_zone
        self._suggested_zone_name = suggested_zone_name

    def __init__(
            self,
            model: CommunicationManager=None,
            create_zone: bool = None,
            suggested_zone_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a ExtractVolumesParams object with default parameters.
        create_zone: bool, optional
            Option to create zone for flow volumes extracted.
        suggested_zone_name: str, optional
            Name to be used as suggestion to name zone created. If there is a volume zone existing with suggested name, then extracted flow volumes will be added to it.
        json_data: dict, optional
            JSON dictionary to create a ExtractVolumesParams object with provided parameters.

        Examples
        --------
        >>> extract_volumes_params = prime.ExtractVolumesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["createZone"] if "createZone" in json_data else None,
                json_data["suggestedZoneName"] if "suggestedZoneName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [create_zone, suggested_zone_name])
            if all_field_specified:
                self.__initialize(
                    create_zone,
                    suggested_zone_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractVolumesParams")
                    json_data = param_json["ExtractVolumesParams"] if "ExtractVolumesParams" in param_json else {}
                    self.__initialize(
                        create_zone if create_zone is not None else ( ExtractVolumesParams._default_params["create_zone"] if "create_zone" in ExtractVolumesParams._default_params else (json_data["createZone"] if "createZone" in json_data else None)),
                        suggested_zone_name if suggested_zone_name is not None else ( ExtractVolumesParams._default_params["suggested_zone_name"] if "suggested_zone_name" in ExtractVolumesParams._default_params else (json_data["suggestedZoneName"] if "suggestedZoneName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            create_zone: bool = None,
            suggested_zone_name: str = None):
        """Set the default values of ExtractVolumesParams.

        Parameters
        ----------
        create_zone: bool, optional
            Option to create zone for flow volumes extracted.
        suggested_zone_name: str, optional
            Name to be used as suggestion to name zone created. If there is a volume zone existing with suggested name, then extracted flow volumes will be added to it.
        """
        args = locals()
        [ExtractVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractVolumesParams.

        Examples
        --------
        >>> ExtractVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._create_zone is not None:
            json_data["createZone"] = self._create_zone
        if self._suggested_zone_name is not None:
            json_data["suggestedZoneName"] = self._suggested_zone_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "create_zone :  %s\nsuggested_zone_name :  %s" % (self._create_zone, self._suggested_zone_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def create_zone(self) -> bool:
        """Option to create zone for flow volumes extracted.
        """
        return self._create_zone

    @create_zone.setter
    def create_zone(self, value: bool):
        self._create_zone = value

    @property
    def suggested_zone_name(self) -> str:
        """Name to be used as suggestion to name zone created. If there is a volume zone existing with suggested name, then extracted flow volumes will be added to it.
        """
        return self._suggested_zone_name

    @suggested_zone_name.setter
    def suggested_zone_name(self, value: str):
        self._suggested_zone_name = value

class ExtractTopoVolumesParams(CoreObject):
    """Parameters to extract flow topovolumes.
    """
    _default_params = {}

    def __initialize(
            self,
            zone_name: str):
        self._zone_name = zone_name

    def __init__(
            self,
            model: CommunicationManager=None,
            zone_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractTopoVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a ExtractTopoVolumesParams object with default parameters.
        zone_name: str, optional
            Specifies zone name to associate extracted flow topovolumes.
        json_data: dict, optional
            JSON dictionary to create a ExtractTopoVolumesParams object with provided parameters.

        Examples
        --------
        >>> extract_topo_volumes_params = prime.ExtractTopoVolumesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["zoneName"] if "zoneName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [zone_name])
            if all_field_specified:
                self.__initialize(
                    zone_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractTopoVolumesParams")
                    json_data = param_json["ExtractTopoVolumesParams"] if "ExtractTopoVolumesParams" in param_json else {}
                    self.__initialize(
                        zone_name if zone_name is not None else ( ExtractTopoVolumesParams._default_params["zone_name"] if "zone_name" in ExtractTopoVolumesParams._default_params else (json_data["zoneName"] if "zoneName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            zone_name: str = None):
        """Set the default values of ExtractTopoVolumesParams.

        Parameters
        ----------
        zone_name: str, optional
            Specifies zone name to associate extracted flow topovolumes.
        """
        args = locals()
        [ExtractTopoVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractTopoVolumesParams.

        Examples
        --------
        >>> ExtractTopoVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractTopoVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._zone_name is not None:
            json_data["zoneName"] = self._zone_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "zone_name :  %s" % (self._zone_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def zone_name(self) -> str:
        """Specifies zone name to associate extracted flow topovolumes.
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value: str):
        self._zone_name = value

class ExtractTopoVolumesResults(CoreObject):
    """Parameters to extract flow topovolumes.
    """
    _default_params = {}

    def __initialize(
            self,
            volumes: Iterable[int],
            error_code: ErrorCode):
        self._volumes = volumes if isinstance(volumes, np.ndarray) else np.array(volumes, dtype=np.int32) if volumes is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            volumes: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractTopoVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a ExtractTopoVolumesResults object with default parameters.
        volumes: Iterable[int], optional
            Ids of extracted flow topovolumes.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a ExtractTopoVolumesResults object with provided parameters.

        Examples
        --------
        >>> extract_topo_volumes_results = prime.ExtractTopoVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["volumes"] if "volumes" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [volumes, error_code])
            if all_field_specified:
                self.__initialize(
                    volumes,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractTopoVolumesResults")
                    json_data = param_json["ExtractTopoVolumesResults"] if "ExtractTopoVolumesResults" in param_json else {}
                    self.__initialize(
                        volumes if volumes is not None else ( ExtractTopoVolumesResults._default_params["volumes"] if "volumes" in ExtractTopoVolumesResults._default_params else (json_data["volumes"] if "volumes" in json_data else None)),
                        error_code if error_code is not None else ( ExtractTopoVolumesResults._default_params["error_code"] if "error_code" in ExtractTopoVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            volumes: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of ExtractTopoVolumesResults.

        Parameters
        ----------
        volumes: Iterable[int], optional
            Ids of extracted flow topovolumes.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [ExtractTopoVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractTopoVolumesResults.

        Examples
        --------
        >>> ExtractTopoVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractTopoVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._volumes is not None:
            json_data["volumes"] = self._volumes
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "volumes :  %s\nerror_code :  %s" % (self._volumes, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def volumes(self) -> Iterable[int]:
        """Ids of extracted flow topovolumes.
        """
        return self._volumes

    @volumes.setter
    def volumes(self, value: Iterable[int]):
        self._volumes = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class NamePatternParams(CoreObject):
    """Parameters to be used to match name pattern with names.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the NamePatternParams.

        Parameters
        ----------
        model: Model
            Model to create a NamePatternParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a NamePatternParams object with provided parameters.

        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "NamePatternParams")
                    json_data = param_json["NamePatternParams"] if "NamePatternParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of NamePatternParams.

        """
        args = locals()
        [NamePatternParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of NamePatternParams.

        Examples
        --------
        >>> NamePatternParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in NamePatternParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class PartSummaryParams(CoreObject):
    """Parameters to control part summary results.
    """
    _default_params = {}

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
        """Initializes the PartSummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a PartSummaryParams object with default parameters.
        print_id: bool, optional
            Boolean to control print ids. The default is false.
        print_mesh: bool, optional
            Boolean to control print mesh information. The default is true.
        json_data: dict, optional
            JSON dictionary to create a PartSummaryParams object with provided parameters.

        Examples
        --------
        >>> part_summary_params = prime.PartSummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["printId"] if "printId" in json_data else None,
                json_data["printMesh"] if "printMesh" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "PartSummaryParams")
                    json_data = param_json["PartSummaryParams"] if "PartSummaryParams" in param_json else {}
                    self.__initialize(
                        print_id if print_id is not None else ( PartSummaryParams._default_params["print_id"] if "print_id" in PartSummaryParams._default_params else (json_data["printId"] if "printId" in json_data else None)),
                        print_mesh if print_mesh is not None else ( PartSummaryParams._default_params["print_mesh"] if "print_mesh" in PartSummaryParams._default_params else (json_data["printMesh"] if "printMesh" in json_data else None)))
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
        """Set the default values of PartSummaryParams.

        Parameters
        ----------
        print_id: bool, optional
            Boolean to control print ids. The default is false.
        print_mesh: bool, optional
            Boolean to control print mesh information. The default is true.
        """
        args = locals()
        [PartSummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PartSummaryParams.

        Examples
        --------
        >>> PartSummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartSummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._print_id is not None:
            json_data["printId"] = self._print_id
        if self._print_mesh is not None:
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
        """Boolean to control print mesh information. The default is true.
        """
        return self._print_mesh

    @print_mesh.setter
    def print_mesh(self, value: bool):
        self._print_mesh = value

class PartSummaryResults(CoreObject):
    """Results of part summary.
    """
    _default_params = {}

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
        """Initializes the PartSummaryResults.

        Parameters
        ----------
        model: Model
            Model to create a PartSummaryResults object with default parameters.
        message: str, optional
            Part summary text.
        n_topo_edges: int, optional
            Number of topoedges.
        n_topo_faces: int, optional
            Number of topofaces.
        n_topo_volumes: int, optional
            Number of topovolumes.
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
            Number of unmeshed topofaces.
        json_data: dict, optional
            JSON dictionary to create a PartSummaryResults object with provided parameters.

        Examples
        --------
        >>> part_summary_results = prime.PartSummaryResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["message"] if "message" in json_data else None,
                json_data["nTopoEdges"] if "nTopoEdges" in json_data else None,
                json_data["nTopoFaces"] if "nTopoFaces" in json_data else None,
                json_data["nTopoVolumes"] if "nTopoVolumes" in json_data else None,
                json_data["nEdgeZonelets"] if "nEdgeZonelets" in json_data else None,
                json_data["nFaceZonelets"] if "nFaceZonelets" in json_data else None,
                json_data["nCellZonelets"] if "nCellZonelets" in json_data else None,
                json_data["nEdgeZones"] if "nEdgeZones" in json_data else None,
                json_data["nFaceZones"] if "nFaceZones" in json_data else None,
                json_data["nVolumeZones"] if "nVolumeZones" in json_data else None,
                json_data["nLabels"] if "nLabels" in json_data else None,
                json_data["nNodes"] if "nNodes" in json_data else None,
                json_data["nFaces"] if "nFaces" in json_data else None,
                json_data["nCells"] if "nCells" in json_data else None,
                json_data["nTriFaces"] if "nTriFaces" in json_data else None,
                json_data["nPolyFaces"] if "nPolyFaces" in json_data else None,
                json_data["nQuadFaces"] if "nQuadFaces" in json_data else None,
                json_data["nTetCells"] if "nTetCells" in json_data else None,
                json_data["nPyraCells"] if "nPyraCells" in json_data else None,
                json_data["nPrismCells"] if "nPrismCells" in json_data else None,
                json_data["nPolyCells"] if "nPolyCells" in json_data else None,
                json_data["nHexCells"] if "nHexCells" in json_data else None,
                json_data["nUnmeshedTopoFaces"] if "nUnmeshedTopoFaces" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "PartSummaryResults")
                    json_data = param_json["PartSummaryResults"] if "PartSummaryResults" in param_json else {}
                    self.__initialize(
                        message if message is not None else ( PartSummaryResults._default_params["message"] if "message" in PartSummaryResults._default_params else (json_data["message"] if "message" in json_data else None)),
                        n_topo_edges if n_topo_edges is not None else ( PartSummaryResults._default_params["n_topo_edges"] if "n_topo_edges" in PartSummaryResults._default_params else (json_data["nTopoEdges"] if "nTopoEdges" in json_data else None)),
                        n_topo_faces if n_topo_faces is not None else ( PartSummaryResults._default_params["n_topo_faces"] if "n_topo_faces" in PartSummaryResults._default_params else (json_data["nTopoFaces"] if "nTopoFaces" in json_data else None)),
                        n_topo_volumes if n_topo_volumes is not None else ( PartSummaryResults._default_params["n_topo_volumes"] if "n_topo_volumes" in PartSummaryResults._default_params else (json_data["nTopoVolumes"] if "nTopoVolumes" in json_data else None)),
                        n_edge_zonelets if n_edge_zonelets is not None else ( PartSummaryResults._default_params["n_edge_zonelets"] if "n_edge_zonelets" in PartSummaryResults._default_params else (json_data["nEdgeZonelets"] if "nEdgeZonelets" in json_data else None)),
                        n_face_zonelets if n_face_zonelets is not None else ( PartSummaryResults._default_params["n_face_zonelets"] if "n_face_zonelets" in PartSummaryResults._default_params else (json_data["nFaceZonelets"] if "nFaceZonelets" in json_data else None)),
                        n_cell_zonelets if n_cell_zonelets is not None else ( PartSummaryResults._default_params["n_cell_zonelets"] if "n_cell_zonelets" in PartSummaryResults._default_params else (json_data["nCellZonelets"] if "nCellZonelets" in json_data else None)),
                        n_edge_zones if n_edge_zones is not None else ( PartSummaryResults._default_params["n_edge_zones"] if "n_edge_zones" in PartSummaryResults._default_params else (json_data["nEdgeZones"] if "nEdgeZones" in json_data else None)),
                        n_face_zones if n_face_zones is not None else ( PartSummaryResults._default_params["n_face_zones"] if "n_face_zones" in PartSummaryResults._default_params else (json_data["nFaceZones"] if "nFaceZones" in json_data else None)),
                        n_volume_zones if n_volume_zones is not None else ( PartSummaryResults._default_params["n_volume_zones"] if "n_volume_zones" in PartSummaryResults._default_params else (json_data["nVolumeZones"] if "nVolumeZones" in json_data else None)),
                        n_labels if n_labels is not None else ( PartSummaryResults._default_params["n_labels"] if "n_labels" in PartSummaryResults._default_params else (json_data["nLabels"] if "nLabels" in json_data else None)),
                        n_nodes if n_nodes is not None else ( PartSummaryResults._default_params["n_nodes"] if "n_nodes" in PartSummaryResults._default_params else (json_data["nNodes"] if "nNodes" in json_data else None)),
                        n_faces if n_faces is not None else ( PartSummaryResults._default_params["n_faces"] if "n_faces" in PartSummaryResults._default_params else (json_data["nFaces"] if "nFaces" in json_data else None)),
                        n_cells if n_cells is not None else ( PartSummaryResults._default_params["n_cells"] if "n_cells" in PartSummaryResults._default_params else (json_data["nCells"] if "nCells" in json_data else None)),
                        n_tri_faces if n_tri_faces is not None else ( PartSummaryResults._default_params["n_tri_faces"] if "n_tri_faces" in PartSummaryResults._default_params else (json_data["nTriFaces"] if "nTriFaces" in json_data else None)),
                        n_poly_faces if n_poly_faces is not None else ( PartSummaryResults._default_params["n_poly_faces"] if "n_poly_faces" in PartSummaryResults._default_params else (json_data["nPolyFaces"] if "nPolyFaces" in json_data else None)),
                        n_quad_faces if n_quad_faces is not None else ( PartSummaryResults._default_params["n_quad_faces"] if "n_quad_faces" in PartSummaryResults._default_params else (json_data["nQuadFaces"] if "nQuadFaces" in json_data else None)),
                        n_tet_cells if n_tet_cells is not None else ( PartSummaryResults._default_params["n_tet_cells"] if "n_tet_cells" in PartSummaryResults._default_params else (json_data["nTetCells"] if "nTetCells" in json_data else None)),
                        n_pyra_cells if n_pyra_cells is not None else ( PartSummaryResults._default_params["n_pyra_cells"] if "n_pyra_cells" in PartSummaryResults._default_params else (json_data["nPyraCells"] if "nPyraCells" in json_data else None)),
                        n_prism_cells if n_prism_cells is not None else ( PartSummaryResults._default_params["n_prism_cells"] if "n_prism_cells" in PartSummaryResults._default_params else (json_data["nPrismCells"] if "nPrismCells" in json_data else None)),
                        n_poly_cells if n_poly_cells is not None else ( PartSummaryResults._default_params["n_poly_cells"] if "n_poly_cells" in PartSummaryResults._default_params else (json_data["nPolyCells"] if "nPolyCells" in json_data else None)),
                        n_hex_cells if n_hex_cells is not None else ( PartSummaryResults._default_params["n_hex_cells"] if "n_hex_cells" in PartSummaryResults._default_params else (json_data["nHexCells"] if "nHexCells" in json_data else None)),
                        n_unmeshed_topo_faces if n_unmeshed_topo_faces is not None else ( PartSummaryResults._default_params["n_unmeshed_topo_faces"] if "n_unmeshed_topo_faces" in PartSummaryResults._default_params else (json_data["nUnmeshedTopoFaces"] if "nUnmeshedTopoFaces" in json_data else None)))
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
        """Set the default values of PartSummaryResults.

        Parameters
        ----------
        message: str, optional
            Part summary text.
        n_topo_edges: int, optional
            Number of topoedges.
        n_topo_faces: int, optional
            Number of topofaces.
        n_topo_volumes: int, optional
            Number of topovolumes.
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
            Number of unmeshed topofaces.
        """
        args = locals()
        [PartSummaryResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PartSummaryResults.

        Examples
        --------
        >>> PartSummaryResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartSummaryResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._message is not None:
            json_data["message"] = self._message
        if self._n_topo_edges is not None:
            json_data["nTopoEdges"] = self._n_topo_edges
        if self._n_topo_faces is not None:
            json_data["nTopoFaces"] = self._n_topo_faces
        if self._n_topo_volumes is not None:
            json_data["nTopoVolumes"] = self._n_topo_volumes
        if self._n_edge_zonelets is not None:
            json_data["nEdgeZonelets"] = self._n_edge_zonelets
        if self._n_face_zonelets is not None:
            json_data["nFaceZonelets"] = self._n_face_zonelets
        if self._n_cell_zonelets is not None:
            json_data["nCellZonelets"] = self._n_cell_zonelets
        if self._n_edge_zones is not None:
            json_data["nEdgeZones"] = self._n_edge_zones
        if self._n_face_zones is not None:
            json_data["nFaceZones"] = self._n_face_zones
        if self._n_volume_zones is not None:
            json_data["nVolumeZones"] = self._n_volume_zones
        if self._n_labels is not None:
            json_data["nLabels"] = self._n_labels
        if self._n_nodes is not None:
            json_data["nNodes"] = self._n_nodes
        if self._n_faces is not None:
            json_data["nFaces"] = self._n_faces
        if self._n_cells is not None:
            json_data["nCells"] = self._n_cells
        if self._n_tri_faces is not None:
            json_data["nTriFaces"] = self._n_tri_faces
        if self._n_poly_faces is not None:
            json_data["nPolyFaces"] = self._n_poly_faces
        if self._n_quad_faces is not None:
            json_data["nQuadFaces"] = self._n_quad_faces
        if self._n_tet_cells is not None:
            json_data["nTetCells"] = self._n_tet_cells
        if self._n_pyra_cells is not None:
            json_data["nPyraCells"] = self._n_pyra_cells
        if self._n_prism_cells is not None:
            json_data["nPrismCells"] = self._n_prism_cells
        if self._n_poly_cells is not None:
            json_data["nPolyCells"] = self._n_poly_cells
        if self._n_hex_cells is not None:
            json_data["nHexCells"] = self._n_hex_cells
        if self._n_unmeshed_topo_faces is not None:
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
        """Number of topoedges.
        """
        return self._n_topo_edges

    @n_topo_edges.setter
    def n_topo_edges(self, value: int):
        self._n_topo_edges = value

    @property
    def n_topo_faces(self) -> int:
        """Number of topofaces.
        """
        return self._n_topo_faces

    @n_topo_faces.setter
    def n_topo_faces(self, value: int):
        self._n_topo_faces = value

    @property
    def n_topo_volumes(self) -> int:
        """Number of topovolumes.
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
        """Number of unmeshed topofaces.
        """
        return self._n_unmeshed_topo_faces

    @n_unmeshed_topo_faces.setter
    def n_unmeshed_topo_faces(self, value: int):
        self._n_unmeshed_topo_faces = value

class DeleteTopoEntitiesParams(CoreObject):
    """Parameters to control delete topoentities.
    """
    _default_params = {}

    def __initialize(
            self,
            delete_geom_zonelets: bool,
            delete_mesh_zonelets: bool):
        self._delete_geom_zonelets = delete_geom_zonelets
        self._delete_mesh_zonelets = delete_mesh_zonelets

    def __init__(
            self,
            model: CommunicationManager=None,
            delete_geom_zonelets: bool = None,
            delete_mesh_zonelets: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteTopoEntitiesParams.

        Parameters
        ----------
        model: Model
            Model to create a DeleteTopoEntitiesParams object with default parameters.
        delete_geom_zonelets: bool, optional
            Option to delete geometry zonelets of topology.
        delete_mesh_zonelets: bool, optional
            Option to delete mesh zonelets of topology.
        json_data: dict, optional
            JSON dictionary to create a DeleteTopoEntitiesParams object with provided parameters.

        Examples
        --------
        >>> delete_topo_entities_params = prime.DeleteTopoEntitiesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["deleteGeomZonelets"] if "deleteGeomZonelets" in json_data else None,
                json_data["deleteMeshZonelets"] if "deleteMeshZonelets" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [delete_geom_zonelets, delete_mesh_zonelets])
            if all_field_specified:
                self.__initialize(
                    delete_geom_zonelets,
                    delete_mesh_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteTopoEntitiesParams")
                    json_data = param_json["DeleteTopoEntitiesParams"] if "DeleteTopoEntitiesParams" in param_json else {}
                    self.__initialize(
                        delete_geom_zonelets if delete_geom_zonelets is not None else ( DeleteTopoEntitiesParams._default_params["delete_geom_zonelets"] if "delete_geom_zonelets" in DeleteTopoEntitiesParams._default_params else (json_data["deleteGeomZonelets"] if "deleteGeomZonelets" in json_data else None)),
                        delete_mesh_zonelets if delete_mesh_zonelets is not None else ( DeleteTopoEntitiesParams._default_params["delete_mesh_zonelets"] if "delete_mesh_zonelets" in DeleteTopoEntitiesParams._default_params else (json_data["deleteMeshZonelets"] if "deleteMeshZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            delete_geom_zonelets: bool = None,
            delete_mesh_zonelets: bool = None):
        """Set the default values of DeleteTopoEntitiesParams.

        Parameters
        ----------
        delete_geom_zonelets: bool, optional
            Option to delete geometry zonelets of topology.
        delete_mesh_zonelets: bool, optional
            Option to delete mesh zonelets of topology.
        """
        args = locals()
        [DeleteTopoEntitiesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteTopoEntitiesParams.

        Examples
        --------
        >>> DeleteTopoEntitiesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteTopoEntitiesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._delete_geom_zonelets is not None:
            json_data["deleteGeomZonelets"] = self._delete_geom_zonelets
        if self._delete_mesh_zonelets is not None:
            json_data["deleteMeshZonelets"] = self._delete_mesh_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "delete_geom_zonelets :  %s\ndelete_mesh_zonelets :  %s" % (self._delete_geom_zonelets, self._delete_mesh_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def delete_geom_zonelets(self) -> bool:
        """Option to delete geometry zonelets of topology.
        """
        return self._delete_geom_zonelets

    @delete_geom_zonelets.setter
    def delete_geom_zonelets(self, value: bool):
        self._delete_geom_zonelets = value

    @property
    def delete_mesh_zonelets(self) -> bool:
        """Option to delete mesh zonelets of topology.
        """
        return self._delete_mesh_zonelets

    @delete_mesh_zonelets.setter
    def delete_mesh_zonelets(self, value: bool):
        self._delete_mesh_zonelets = value

class DeleteTopoEntitiesResults(CoreObject):
    """Results associated with delete topoentities.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteTopoEntitiesResults.

        Parameters
        ----------
        model: Model
            Model to create a DeleteTopoEntitiesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with delete topoentities.
        json_data: dict, optional
            JSON dictionary to create a DeleteTopoEntitiesResults object with provided parameters.

        Examples
        --------
        >>> delete_topo_entities_results = prime.DeleteTopoEntitiesResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteTopoEntitiesResults")
                    json_data = param_json["DeleteTopoEntitiesResults"] if "DeleteTopoEntitiesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteTopoEntitiesResults._default_params["error_code"] if "error_code" in DeleteTopoEntitiesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of DeleteTopoEntitiesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with delete topoentities.
        """
        args = locals()
        [DeleteTopoEntitiesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteTopoEntitiesResults.

        Examples
        --------
        >>> DeleteTopoEntitiesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteTopoEntitiesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with delete topoentities.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class AddToZoneResults(CoreObject):
    """Results associated with the add to zone operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AddToZoneResults.

        Parameters
        ----------
        model: Model
            Model to create a AddToZoneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the add to zone operation.
        json_data: dict, optional
            JSON dictionary to create a AddToZoneResults object with provided parameters.

        Examples
        --------
        >>> add_to_zone_results = prime.AddToZoneResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "AddToZoneResults")
                    json_data = param_json["AddToZoneResults"] if "AddToZoneResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( AddToZoneResults._default_params["error_code"] if "error_code" in AddToZoneResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( AddToZoneResults._default_params["warning_codes"] if "warning_codes" in AddToZoneResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of AddToZoneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the add to zone operation.
        """
        args = locals()
        [AddToZoneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AddToZoneResults.

        Examples
        --------
        >>> AddToZoneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AddToZoneResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the add to zone operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class RemoveZoneResults(CoreObject):
    """Results associated with the remove zone operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RemoveZoneResults.

        Parameters
        ----------
        model: Model
            Model to create a RemoveZoneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the remove zone operation.
        json_data: dict, optional
            JSON dictionary to create a RemoveZoneResults object with provided parameters.

        Examples
        --------
        >>> remove_zone_results = prime.RemoveZoneResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "RemoveZoneResults")
                    json_data = param_json["RemoveZoneResults"] if "RemoveZoneResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( RemoveZoneResults._default_params["error_code"] if "error_code" in RemoveZoneResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( RemoveZoneResults._default_params["warning_codes"] if "warning_codes" in RemoveZoneResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of RemoveZoneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the remove zone operation.
        """
        args = locals()
        [RemoveZoneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RemoveZoneResults.

        Examples
        --------
        >>> RemoveZoneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RemoveZoneResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the remove zone operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class AddLabelResults(CoreObject):
    """Results associated with the add label operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AddLabelResults.

        Parameters
        ----------
        model: Model
            Model to create a AddLabelResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the add label operation.
        json_data: dict, optional
            JSON dictionary to create a AddLabelResults object with provided parameters.

        Examples
        --------
        >>> add_label_results = prime.AddLabelResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "AddLabelResults")
                    json_data = param_json["AddLabelResults"] if "AddLabelResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( AddLabelResults._default_params["error_code"] if "error_code" in AddLabelResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of AddLabelResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the add label operation.
        """
        args = locals()
        [AddLabelResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AddLabelResults.

        Examples
        --------
        >>> AddLabelResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AddLabelResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the add label operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class RemoveLabelResults(CoreObject):
    """Results associated with the remove label operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RemoveLabelResults.

        Parameters
        ----------
        model: Model
            Model to create a RemoveLabelResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the remove label operation.
        json_data: dict, optional
            JSON dictionary to create a RemoveLabelResults object with provided parameters.

        Examples
        --------
        >>> remove_label_results = prime.RemoveLabelResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "RemoveLabelResults")
                    json_data = param_json["RemoveLabelResults"] if "RemoveLabelResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( RemoveLabelResults._default_params["error_code"] if "error_code" in RemoveLabelResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of RemoveLabelResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the remove label operation.
        """
        args = locals()
        [RemoveLabelResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RemoveLabelResults.

        Examples
        --------
        >>> RemoveLabelResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RemoveLabelResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the remove label operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class DeleteVolumesParams(CoreObject):
    """Parameters to delete volumes.
    """
    _default_params = {}

    def __initialize(
            self,
            delete_small_volumes: bool,
            volume_limit: float):
        self._delete_small_volumes = delete_small_volumes
        self._volume_limit = volume_limit

    def __init__(
            self,
            model: CommunicationManager=None,
            delete_small_volumes: bool = None,
            volume_limit: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a DeleteVolumesParams object with default parameters.
        delete_small_volumes: bool, optional
            Option to delete only volumes smaller than provided volume limit.
        volume_limit: float, optional
            Maximum volume limit to identify smaller volumes to be deleted.
        json_data: dict, optional
            JSON dictionary to create a DeleteVolumesParams object with provided parameters.

        Examples
        --------
        >>> delete_volumes_params = prime.DeleteVolumesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["deleteSmallVolumes"] if "deleteSmallVolumes" in json_data else None,
                json_data["volumeLimit"] if "volumeLimit" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [delete_small_volumes, volume_limit])
            if all_field_specified:
                self.__initialize(
                    delete_small_volumes,
                    volume_limit)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteVolumesParams")
                    json_data = param_json["DeleteVolumesParams"] if "DeleteVolumesParams" in param_json else {}
                    self.__initialize(
                        delete_small_volumes if delete_small_volumes is not None else ( DeleteVolumesParams._default_params["delete_small_volumes"] if "delete_small_volumes" in DeleteVolumesParams._default_params else (json_data["deleteSmallVolumes"] if "deleteSmallVolumes" in json_data else None)),
                        volume_limit if volume_limit is not None else ( DeleteVolumesParams._default_params["volume_limit"] if "volume_limit" in DeleteVolumesParams._default_params else (json_data["volumeLimit"] if "volumeLimit" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            delete_small_volumes: bool = None,
            volume_limit: float = None):
        """Set the default values of DeleteVolumesParams.

        Parameters
        ----------
        delete_small_volumes: bool, optional
            Option to delete only volumes smaller than provided volume limit.
        volume_limit: float, optional
            Maximum volume limit to identify smaller volumes to be deleted.
        """
        args = locals()
        [DeleteVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteVolumesParams.

        Examples
        --------
        >>> DeleteVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._delete_small_volumes is not None:
            json_data["deleteSmallVolumes"] = self._delete_small_volumes
        if self._volume_limit is not None:
            json_data["volumeLimit"] = self._volume_limit
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "delete_small_volumes :  %s\nvolume_limit :  %s" % (self._delete_small_volumes, self._volume_limit)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def delete_small_volumes(self) -> bool:
        """Option to delete only volumes smaller than provided volume limit.
        """
        return self._delete_small_volumes

    @delete_small_volumes.setter
    def delete_small_volumes(self, value: bool):
        self._delete_small_volumes = value

    @property
    def volume_limit(self) -> float:
        """Maximum volume limit to identify smaller volumes to be deleted.
        """
        return self._volume_limit

    @volume_limit.setter
    def volume_limit(self, value: float):
        self._volume_limit = value

class DeleteVolumesResults(CoreObject):
    """Results associated with delete volumes operation.
    """
    _default_params = {}

    def __initialize(
            self,
            deleted_volumes: Iterable[int],
            error_code: ErrorCode):
        self._deleted_volumes = deleted_volumes if isinstance(deleted_volumes, np.ndarray) else np.array(deleted_volumes, dtype=np.int32) if deleted_volumes is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            deleted_volumes: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a DeleteVolumesResults object with default parameters.
        deleted_volumes: Iterable[int], optional
            Ids of deleted volumes.
        error_code: ErrorCode, optional
            Error code associated with the volume deletion operation.
        json_data: dict, optional
            JSON dictionary to create a DeleteVolumesResults object with provided parameters.

        Examples
        --------
        >>> delete_volumes_results = prime.DeleteVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["deletedVolumes"] if "deletedVolumes" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [deleted_volumes, error_code])
            if all_field_specified:
                self.__initialize(
                    deleted_volumes,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteVolumesResults")
                    json_data = param_json["DeleteVolumesResults"] if "DeleteVolumesResults" in param_json else {}
                    self.__initialize(
                        deleted_volumes if deleted_volumes is not None else ( DeleteVolumesResults._default_params["deleted_volumes"] if "deleted_volumes" in DeleteVolumesResults._default_params else (json_data["deletedVolumes"] if "deletedVolumes" in json_data else None)),
                        error_code if error_code is not None else ( DeleteVolumesResults._default_params["error_code"] if "error_code" in DeleteVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            deleted_volumes: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of DeleteVolumesResults.

        Parameters
        ----------
        deleted_volumes: Iterable[int], optional
            Ids of deleted volumes.
        error_code: ErrorCode, optional
            Error code associated with the volume deletion operation.
        """
        args = locals()
        [DeleteVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteVolumesResults.

        Examples
        --------
        >>> DeleteVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._deleted_volumes is not None:
            json_data["deletedVolumes"] = self._deleted_volumes
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "deleted_volumes :  %s\nerror_code :  %s" % (self._deleted_volumes, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def deleted_volumes(self) -> Iterable[int]:
        """Ids of deleted volumes.
        """
        return self._deleted_volumes

    @deleted_volumes.setter
    def deleted_volumes(self, value: Iterable[int]):
        self._deleted_volumes = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the volume deletion operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class MergeVolumesParams(CoreObject):
    """Parameters to merge volumes.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergeVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a MergeVolumesParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a MergeVolumesParams object with provided parameters.

        Examples
        --------
        >>> merge_volumes_params = prime.MergeVolumesParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergeVolumesParams")
                    json_data = param_json["MergeVolumesParams"] if "MergeVolumesParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of MergeVolumesParams.

        """
        args = locals()
        [MergeVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergeVolumesParams.

        Examples
        --------
        >>> MergeVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergeVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class MergeVolumesResults(CoreObject):
    """Results associated with merge volumes operation.
    """
    _default_params = {}

    def __initialize(
            self,
            merged_volumes: Iterable[int],
            error_code: ErrorCode):
        self._merged_volumes = merged_volumes if isinstance(merged_volumes, np.ndarray) else np.array(merged_volumes, dtype=np.int32) if merged_volumes is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            merged_volumes: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergeVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a MergeVolumesResults object with default parameters.
        merged_volumes: Iterable[int], optional
            Ids of volumes to which input volumes are merged.
        error_code: ErrorCode, optional
            Error code associated with the volume merge operation.
        json_data: dict, optional
            JSON dictionary to create a MergeVolumesResults object with provided parameters.

        Examples
        --------
        >>> merge_volumes_results = prime.MergeVolumesResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["mergedVolumes"] if "mergedVolumes" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [merged_volumes, error_code])
            if all_field_specified:
                self.__initialize(
                    merged_volumes,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergeVolumesResults")
                    json_data = param_json["MergeVolumesResults"] if "MergeVolumesResults" in param_json else {}
                    self.__initialize(
                        merged_volumes if merged_volumes is not None else ( MergeVolumesResults._default_params["merged_volumes"] if "merged_volumes" in MergeVolumesResults._default_params else (json_data["mergedVolumes"] if "mergedVolumes" in json_data else None)),
                        error_code if error_code is not None else ( MergeVolumesResults._default_params["error_code"] if "error_code" in MergeVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            merged_volumes: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of MergeVolumesResults.

        Parameters
        ----------
        merged_volumes: Iterable[int], optional
            Ids of volumes to which input volumes are merged.
        error_code: ErrorCode, optional
            Error code associated with the volume merge operation.
        """
        args = locals()
        [MergeVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergeVolumesResults.

        Examples
        --------
        >>> MergeVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergeVolumesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._merged_volumes is not None:
            json_data["mergedVolumes"] = self._merged_volumes
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "merged_volumes :  %s\nerror_code :  %s" % (self._merged_volumes, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def merged_volumes(self) -> Iterable[int]:
        """Ids of volumes to which input volumes are merged.
        """
        return self._merged_volumes

    @merged_volumes.setter
    def merged_volumes(self, value: Iterable[int]):
        self._merged_volumes = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the volume merge operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
