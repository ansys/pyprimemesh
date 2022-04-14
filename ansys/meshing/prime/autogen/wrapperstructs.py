""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class WrapRegion(enum.IntEnum):
    """Indicates source type to extract wrapper region.
    """
    MATERIALPOINT = 0
    """Option to use live material points to extract wrapper region."""
    EXTERNAL = 1
    """Option to extract exterior wrapper region."""
    LARGESTINTERNAL = 2
    """Option to extract largest internal wrapper region."""

class WrapParams(CoreObject):
    """WrapParams defines parameters for wrapping.
    """
    _default_params = {}

    def __initialize(
            self,
            sizing_method: SizeFieldType,
            base_size: float,
            size_control_ids: Iterable[int],
            size_field_ids: Iterable[int],
            wrap_region: WrapRegion,
            number_of_threads: int,
            imprint_relative_range: float,
            imprint_iterations: int):
        self._sizing_method = SizeFieldType(sizing_method)
        self._base_size = base_size
        self._size_control_ids = size_control_ids if isinstance(size_control_ids, np.ndarray) else np.array(size_control_ids, dtype=np.int32)
        self._size_field_ids = size_field_ids if isinstance(size_field_ids, np.ndarray) else np.array(size_field_ids, dtype=np.int32)
        self._wrap_region = WrapRegion(wrap_region)
        self._number_of_threads = number_of_threads
        self._imprint_relative_range = imprint_relative_range
        self._imprint_iterations = imprint_iterations

    def __init__(
            self,
            model: CommunicationManager=None,
            sizing_method: SizeFieldType = None,
            base_size: float = None,
            size_control_ids: Iterable[int] = None,
            size_field_ids: Iterable[int] = None,
            wrap_region: WrapRegion = None,
            number_of_threads: int = None,
            imprint_relative_range: float = None,
            imprint_iterations: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the WrapParams.

        Parameters
        ----------
        model: Model
            Model to create a WrapParams object with default parameters.
        sizing_method: SizeFieldType, optional
            Used to define sizing method for wrapping.
        base_size: float, optional
            Base size to define octree.
        size_control_ids: Iterable[int], optional
            Used to construct geodesic sizes for octree refinement.
        size_field_ids: Iterable[int], optional
            Used to define size field based octree refinement.
        wrap_region: WrapRegion, optional
            Indicates source type to extract wrapper region.
        number_of_threads: int, optional
            Number of threads for multithreading.
        imprint_relative_range: float, optional
            Used to define relative range in imprinting in wrapping.
        imprint_iterations: int, optional
            Used to define number of imprint iterations in wrapping.
        json_data: dict, optional
            JSON dictionary to create a WrapParams object with provided parameters.

        Examples
        --------
        >>> wrap_params = prime.WrapParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["sizingMethod"]),
                json_data["baseSize"],
                json_data["sizeControlIDs"],
                json_data["sizeFieldIDs"],
                WrapRegion(json_data["wrapRegion"]),
                json_data["numberOfThreads"],
                json_data["imprintRelativeRange"],
                json_data["imprintIterations"])
        else:
            all_field_specified = all(arg is not None for arg in [sizing_method, base_size, size_control_ids, size_field_ids, wrap_region, number_of_threads, imprint_relative_range, imprint_iterations])
            if all_field_specified:
                self.__initialize(
                    sizing_method,
                    base_size,
                    size_control_ids,
                    size_field_ids,
                    wrap_region,
                    number_of_threads,
                    imprint_relative_range,
                    imprint_iterations)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "WrapParams")["WrapParams"]
                    self.__initialize(
                        sizing_method if sizing_method is not None else ( WrapParams._default_params["sizing_method"] if "sizing_method" in WrapParams._default_params else SizeFieldType(json_data["sizingMethod"])),
                        base_size if base_size is not None else ( WrapParams._default_params["base_size"] if "base_size" in WrapParams._default_params else json_data["baseSize"]),
                        size_control_ids if size_control_ids is not None else ( WrapParams._default_params["size_control_ids"] if "size_control_ids" in WrapParams._default_params else json_data["sizeControlIDs"]),
                        size_field_ids if size_field_ids is not None else ( WrapParams._default_params["size_field_ids"] if "size_field_ids" in WrapParams._default_params else json_data["sizeFieldIDs"]),
                        wrap_region if wrap_region is not None else ( WrapParams._default_params["wrap_region"] if "wrap_region" in WrapParams._default_params else WrapRegion(json_data["wrapRegion"])),
                        number_of_threads if number_of_threads is not None else ( WrapParams._default_params["number_of_threads"] if "number_of_threads" in WrapParams._default_params else json_data["numberOfThreads"]),
                        imprint_relative_range if imprint_relative_range is not None else ( WrapParams._default_params["imprint_relative_range"] if "imprint_relative_range" in WrapParams._default_params else json_data["imprintRelativeRange"]),
                        imprint_iterations if imprint_iterations is not None else ( WrapParams._default_params["imprint_iterations"] if "imprint_iterations" in WrapParams._default_params else json_data["imprintIterations"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            sizing_method: SizeFieldType = None,
            base_size: float = None,
            size_control_ids: Iterable[int] = None,
            size_field_ids: Iterable[int] = None,
            wrap_region: WrapRegion = None,
            number_of_threads: int = None,
            imprint_relative_range: float = None,
            imprint_iterations: int = None):
        """Sets the default values of WrapParams.

        Parameters
        ----------
        sizing_method: SizeFieldType, optional
            Used to define sizing method for wrapping.
        base_size: float, optional
            Base size to define octree.
        size_control_ids: Iterable[int], optional
            Used to construct geodesic sizes for octree refinement.
        size_field_ids: Iterable[int], optional
            Used to define size field based octree refinement.
        wrap_region: WrapRegion, optional
            Indicates source type to extract wrapper region.
        number_of_threads: int, optional
            Number of threads for multithreading.
        imprint_relative_range: float, optional
            Used to define relative range in imprinting in wrapping.
        imprint_iterations: int, optional
            Used to define number of imprint iterations in wrapping.
        """
        args = locals()
        [WrapParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of WrapParams.

        Examples
        --------
        >>> WrapParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in WrapParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["sizingMethod"] = self._sizing_method
        json_data["baseSize"] = self._base_size
        json_data["sizeControlIDs"] = self._size_control_ids
        json_data["sizeFieldIDs"] = self._size_field_ids
        json_data["wrapRegion"] = self._wrap_region
        json_data["numberOfThreads"] = self._number_of_threads
        json_data["imprintRelativeRange"] = self._imprint_relative_range
        json_data["imprintIterations"] = self._imprint_iterations
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "sizing_method :  %s\nbase_size :  %s\nsize_control_ids :  %s\nsize_field_ids :  %s\nwrap_region :  %s\nnumber_of_threads :  %s\nimprint_relative_range :  %s\nimprint_iterations :  %s" % (self._sizing_method, self._base_size, self._size_control_ids, self._size_field_ids, self._wrap_region, self._number_of_threads, self._imprint_relative_range, self._imprint_iterations)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def sizing_method(self) -> SizeFieldType:
        """Used to define sizing method for wrapping.
        """
        return self._sizing_method

    @sizing_method.setter
    def sizing_method(self, value: SizeFieldType):
        self._sizing_method = value

    @property
    def base_size(self) -> float:
        """Base size to define octree.
        """
        return self._base_size

    @base_size.setter
    def base_size(self, value: float):
        self._base_size = value

    @property
    def size_control_ids(self) -> Iterable[int]:
        """Used to construct geodesic sizes for octree refinement.
        """
        return self._size_control_ids

    @size_control_ids.setter
    def size_control_ids(self, value: Iterable[int]):
        self._size_control_ids = value

    @property
    def size_field_ids(self) -> Iterable[int]:
        """Used to define size field based octree refinement.
        """
        return self._size_field_ids

    @size_field_ids.setter
    def size_field_ids(self, value: Iterable[int]):
        self._size_field_ids = value

    @property
    def wrap_region(self) -> WrapRegion:
        """Indicates source type to extract wrapper region.
        """
        return self._wrap_region

    @wrap_region.setter
    def wrap_region(self, value: WrapRegion):
        self._wrap_region = value

    @property
    def number_of_threads(self) -> int:
        """Number of threads for multithreading.
        """
        return self._number_of_threads

    @number_of_threads.setter
    def number_of_threads(self, value: int):
        self._number_of_threads = value

    @property
    def imprint_relative_range(self) -> float:
        """Used to define relative range in imprinting in wrapping.
        """
        return self._imprint_relative_range

    @imprint_relative_range.setter
    def imprint_relative_range(self, value: float):
        self._imprint_relative_range = value

    @property
    def imprint_iterations(self) -> int:
        """Used to define number of imprint iterations in wrapping.
        """
        return self._imprint_iterations

    @imprint_iterations.setter
    def imprint_iterations(self, value: int):
        self._imprint_iterations = value

class WrapResult(CoreObject):
    """Result structure associated to Wrap operation.
    """
    _default_params = {}

    def __initialize(
            self,
            warning_codes: List[WarningCode],
            error_code: ErrorCode,
            id: int,
            name: str):
        self._warning_codes = warning_codes
        self._error_code = ErrorCode(error_code)
        self._id = id
        self._name = name

    def __init__(
            self,
            model: CommunicationManager=None,
            warning_codes: List[WarningCode] = None,
            error_code: ErrorCode = None,
            id: int = None,
            name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the WrapResult.

        Parameters
        ----------
        model: Model
            Model to create a WrapResult object with default parameters.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the wrap operation.
        error_code: ErrorCode, optional
            Error code associated with a wrap operation.
        id: int, optional
            Id of the wrapper part created.
        name: str, optional
            Name of wrapper part created.
        json_data: dict, optional
            JSON dictionary to create a WrapResult object with provided parameters.

        Examples
        --------
        >>> wrap_result = prime.WrapResult(model = model)
        """
        if json_data:
            self.__initialize(
                [WarningCode(data) for data in json_data["warningCodes"]],
                ErrorCode(json_data["errorCode"]),
                json_data["id"],
                json_data["name"])
        else:
            all_field_specified = all(arg is not None for arg in [warning_codes, error_code, id, name])
            if all_field_specified:
                self.__initialize(
                    warning_codes,
                    error_code,
                    id,
                    name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "WrapResult")["WrapResult"]
                    self.__initialize(
                        warning_codes if warning_codes is not None else ( WrapResult._default_params["warning_codes"] if "warning_codes" in WrapResult._default_params else [WarningCode(data) for data in json_data["warningCodes"]]),
                        error_code if error_code is not None else ( WrapResult._default_params["error_code"] if "error_code" in WrapResult._default_params else ErrorCode(json_data["errorCode"])),
                        id if id is not None else ( WrapResult._default_params["id"] if "id" in WrapResult._default_params else json_data["id"]),
                        name if name is not None else ( WrapResult._default_params["name"] if "name" in WrapResult._default_params else json_data["name"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            warning_codes: List[WarningCode] = None,
            error_code: ErrorCode = None,
            id: int = None,
            name: str = None):
        """Sets the default values of WrapResult.

        Parameters
        ----------
        warning_codes: List[WarningCode], optional
            Warning codes associated with the wrap operation.
        error_code: ErrorCode, optional
            Error code associated with a wrap operation.
        id: int, optional
            Id of the wrapper part created.
        name: str, optional
            Name of wrapper part created.
        """
        args = locals()
        [WrapResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of WrapResult.

        Examples
        --------
        >>> WrapResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in WrapResult._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["warningCodes"] = [data for data in self._warning_codes]
        json_data["errorCode"] = self._error_code
        json_data["id"] = self._id
        json_data["name"] = self._name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "warning_codes :  %s\nerror_code :  %s\nid :  %s\nname :  %s" % ('[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._error_code, self._id, self._name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the wrap operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with a wrap operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def id(self) -> int:
        """Id of the wrapper part created.
        """
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def name(self) -> str:
        """Name of wrapper part created.
        """
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

class WrapperImproveQualityParams(CoreObject):
    """WrapperImproveQualityParams defines parameters to improve wrapper part.
    """
    _default_params = {}

    def __initialize(
            self,
            target_skewness: float,
            island_count: int,
            island_tol: float,
            overlap_count: int,
            overlap_tol: float,
            resolve_spikes: bool,
            resolve_intersections: bool,
            inflate_dihedral_face_nodes: bool,
            number_of_threads: int):
        self._target_skewness = target_skewness
        self._island_count = island_count
        self._island_tol = island_tol
        self._overlap_count = overlap_count
        self._overlap_tol = overlap_tol
        self._resolve_spikes = resolve_spikes
        self._resolve_intersections = resolve_intersections
        self._inflate_dihedral_face_nodes = inflate_dihedral_face_nodes
        self._number_of_threads = number_of_threads

    def __init__(
            self,
            model: CommunicationManager=None,
            target_skewness: float = None,
            island_count: int = None,
            island_tol: float = None,
            overlap_count: int = None,
            overlap_tol: float = None,
            resolve_spikes: bool = None,
            resolve_intersections: bool = None,
            inflate_dihedral_face_nodes: bool = None,
            number_of_threads: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the WrapperImproveQualityParams.

        Parameters
        ----------
        model: Model
            Model to create a WrapperImproveQualityParams object with default parameters.
        target_skewness: float, optional
            Target skewness.
        island_count: int, optional
            Face count of smallest island.
        island_tol: float, optional
            Relative face count of smallest island.
        overlap_count: int, optional
            Face count of non-manifold overlap.
        overlap_tol: float, optional
            Relative face count of non-manifold overlap.
        resolve_spikes: bool, optional
            Control to perform removing spikes or not.
        resolve_intersections: bool, optional
            Control to resolve face intersections or not.
        inflate_dihedral_face_nodes: bool, optional
            Control to resolve face dihedral angle by inflating opposite nodes or not.
        number_of_threads: int, optional
            Number of threads for multithreading.
        json_data: dict, optional
            JSON dictionary to create a WrapperImproveQualityParams object with provided parameters.

        Examples
        --------
        >>> wrapper_improve_quality_params = prime.WrapperImproveQualityParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["targetSkewness"],
                json_data["islandCount"],
                json_data["islandTol"],
                json_data["overlapCount"],
                json_data["overlapTol"],
                json_data["resolveSpikes"],
                json_data["resolveIntersections"],
                json_data["inflateDihedralFaceNodes"],
                json_data["numberOfThreads"])
        else:
            all_field_specified = all(arg is not None for arg in [target_skewness, island_count, island_tol, overlap_count, overlap_tol, resolve_spikes, resolve_intersections, inflate_dihedral_face_nodes, number_of_threads])
            if all_field_specified:
                self.__initialize(
                    target_skewness,
                    island_count,
                    island_tol,
                    overlap_count,
                    overlap_tol,
                    resolve_spikes,
                    resolve_intersections,
                    inflate_dihedral_face_nodes,
                    number_of_threads)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "WrapperImproveQualityParams")["WrapperImproveQualityParams"]
                    self.__initialize(
                        target_skewness if target_skewness is not None else ( WrapperImproveQualityParams._default_params["target_skewness"] if "target_skewness" in WrapperImproveQualityParams._default_params else json_data["targetSkewness"]),
                        island_count if island_count is not None else ( WrapperImproveQualityParams._default_params["island_count"] if "island_count" in WrapperImproveQualityParams._default_params else json_data["islandCount"]),
                        island_tol if island_tol is not None else ( WrapperImproveQualityParams._default_params["island_tol"] if "island_tol" in WrapperImproveQualityParams._default_params else json_data["islandTol"]),
                        overlap_count if overlap_count is not None else ( WrapperImproveQualityParams._default_params["overlap_count"] if "overlap_count" in WrapperImproveQualityParams._default_params else json_data["overlapCount"]),
                        overlap_tol if overlap_tol is not None else ( WrapperImproveQualityParams._default_params["overlap_tol"] if "overlap_tol" in WrapperImproveQualityParams._default_params else json_data["overlapTol"]),
                        resolve_spikes if resolve_spikes is not None else ( WrapperImproveQualityParams._default_params["resolve_spikes"] if "resolve_spikes" in WrapperImproveQualityParams._default_params else json_data["resolveSpikes"]),
                        resolve_intersections if resolve_intersections is not None else ( WrapperImproveQualityParams._default_params["resolve_intersections"] if "resolve_intersections" in WrapperImproveQualityParams._default_params else json_data["resolveIntersections"]),
                        inflate_dihedral_face_nodes if inflate_dihedral_face_nodes is not None else ( WrapperImproveQualityParams._default_params["inflate_dihedral_face_nodes"] if "inflate_dihedral_face_nodes" in WrapperImproveQualityParams._default_params else json_data["inflateDihedralFaceNodes"]),
                        number_of_threads if number_of_threads is not None else ( WrapperImproveQualityParams._default_params["number_of_threads"] if "number_of_threads" in WrapperImproveQualityParams._default_params else json_data["numberOfThreads"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            target_skewness: float = None,
            island_count: int = None,
            island_tol: float = None,
            overlap_count: int = None,
            overlap_tol: float = None,
            resolve_spikes: bool = None,
            resolve_intersections: bool = None,
            inflate_dihedral_face_nodes: bool = None,
            number_of_threads: int = None):
        """Sets the default values of WrapperImproveQualityParams.

        Parameters
        ----------
        target_skewness: float, optional
            Target skewness.
        island_count: int, optional
            Face count of smallest island.
        island_tol: float, optional
            Relative face count of smallest island.
        overlap_count: int, optional
            Face count of non-manifold overlap.
        overlap_tol: float, optional
            Relative face count of non-manifold overlap.
        resolve_spikes: bool, optional
            Control to perform removing spikes or not.
        resolve_intersections: bool, optional
            Control to resolve face intersections or not.
        inflate_dihedral_face_nodes: bool, optional
            Control to resolve face dihedral angle by inflating opposite nodes or not.
        number_of_threads: int, optional
            Number of threads for multithreading.
        """
        args = locals()
        [WrapperImproveQualityParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of WrapperImproveQualityParams.

        Examples
        --------
        >>> WrapperImproveQualityParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in WrapperImproveQualityParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["targetSkewness"] = self._target_skewness
        json_data["islandCount"] = self._island_count
        json_data["islandTol"] = self._island_tol
        json_data["overlapCount"] = self._overlap_count
        json_data["overlapTol"] = self._overlap_tol
        json_data["resolveSpikes"] = self._resolve_spikes
        json_data["resolveIntersections"] = self._resolve_intersections
        json_data["inflateDihedralFaceNodes"] = self._inflate_dihedral_face_nodes
        json_data["numberOfThreads"] = self._number_of_threads
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "target_skewness :  %s\nisland_count :  %s\nisland_tol :  %s\noverlap_count :  %s\noverlap_tol :  %s\nresolve_spikes :  %s\nresolve_intersections :  %s\ninflate_dihedral_face_nodes :  %s\nnumber_of_threads :  %s" % (self._target_skewness, self._island_count, self._island_tol, self._overlap_count, self._overlap_tol, self._resolve_spikes, self._resolve_intersections, self._inflate_dihedral_face_nodes, self._number_of_threads)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def target_skewness(self) -> float:
        """Target skewness.
        """
        return self._target_skewness

    @target_skewness.setter
    def target_skewness(self, value: float):
        self._target_skewness = value

    @property
    def island_count(self) -> int:
        """Face count of smallest island.
        """
        return self._island_count

    @island_count.setter
    def island_count(self, value: int):
        self._island_count = value

    @property
    def island_tol(self) -> float:
        """Relative face count of smallest island.
        """
        return self._island_tol

    @island_tol.setter
    def island_tol(self, value: float):
        self._island_tol = value

    @property
    def overlap_count(self) -> int:
        """Face count of non-manifold overlap.
        """
        return self._overlap_count

    @overlap_count.setter
    def overlap_count(self, value: int):
        self._overlap_count = value

    @property
    def overlap_tol(self) -> float:
        """Relative face count of non-manifold overlap.
        """
        return self._overlap_tol

    @overlap_tol.setter
    def overlap_tol(self, value: float):
        self._overlap_tol = value

    @property
    def resolve_spikes(self) -> bool:
        """Control to perform removing spikes or not.
        """
        return self._resolve_spikes

    @resolve_spikes.setter
    def resolve_spikes(self, value: bool):
        self._resolve_spikes = value

    @property
    def resolve_intersections(self) -> bool:
        """Control to resolve face intersections or not.
        """
        return self._resolve_intersections

    @resolve_intersections.setter
    def resolve_intersections(self, value: bool):
        self._resolve_intersections = value

    @property
    def inflate_dihedral_face_nodes(self) -> bool:
        """Control to resolve face dihedral angle by inflating opposite nodes or not.
        """
        return self._inflate_dihedral_face_nodes

    @inflate_dihedral_face_nodes.setter
    def inflate_dihedral_face_nodes(self, value: bool):
        self._inflate_dihedral_face_nodes = value

    @property
    def number_of_threads(self) -> int:
        """Number of threads for multithreading.
        """
        return self._number_of_threads

    @number_of_threads.setter
    def number_of_threads(self, value: int):
        self._number_of_threads = value

class WrapperImproveResult(CoreObject):
    """Results structure associated to improve quality.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            n_skew_found: int,
            remaining_skew_faces: int,
            n_face_intersections_found: int,
            unresolved_face_intersections: int):
        self._error_code = ErrorCode(error_code)
        self._n_skew_found = n_skew_found
        self._remaining_skew_faces = remaining_skew_faces
        self._n_face_intersections_found = n_face_intersections_found
        self._unresolved_face_intersections = unresolved_face_intersections

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            n_skew_found: int = None,
            remaining_skew_faces: int = None,
            n_face_intersections_found: int = None,
            unresolved_face_intersections: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the WrapperImproveResult.

        Parameters
        ----------
        model: Model
            Model to create a WrapperImproveResult object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with a wrapper operation.
        n_skew_found: int, optional
            Number of skewed faces found.
        remaining_skew_faces: int, optional
            Number of remaining skew faces.
        n_face_intersections_found: int, optional
            Number of self intersections found.
        unresolved_face_intersections: int, optional
            Number of remaining self intersections.
        json_data: dict, optional
            JSON dictionary to create a WrapperImproveResult object with provided parameters.

        Examples
        --------
        >>> wrapper_improve_result = prime.WrapperImproveResult(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["nSkewFound"],
                json_data["remainingSkewFaces"],
                json_data["nFaceIntersectionsFound"],
                json_data["unresolvedFaceIntersections"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, n_skew_found, remaining_skew_faces, n_face_intersections_found, unresolved_face_intersections])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    n_skew_found,
                    remaining_skew_faces,
                    n_face_intersections_found,
                    unresolved_face_intersections)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "WrapperImproveResult")["WrapperImproveResult"]
                    self.__initialize(
                        error_code if error_code is not None else ( WrapperImproveResult._default_params["error_code"] if "error_code" in WrapperImproveResult._default_params else ErrorCode(json_data["errorCode"])),
                        n_skew_found if n_skew_found is not None else ( WrapperImproveResult._default_params["n_skew_found"] if "n_skew_found" in WrapperImproveResult._default_params else json_data["nSkewFound"]),
                        remaining_skew_faces if remaining_skew_faces is not None else ( WrapperImproveResult._default_params["remaining_skew_faces"] if "remaining_skew_faces" in WrapperImproveResult._default_params else json_data["remainingSkewFaces"]),
                        n_face_intersections_found if n_face_intersections_found is not None else ( WrapperImproveResult._default_params["n_face_intersections_found"] if "n_face_intersections_found" in WrapperImproveResult._default_params else json_data["nFaceIntersectionsFound"]),
                        unresolved_face_intersections if unresolved_face_intersections is not None else ( WrapperImproveResult._default_params["unresolved_face_intersections"] if "unresolved_face_intersections" in WrapperImproveResult._default_params else json_data["unresolvedFaceIntersections"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            n_skew_found: int = None,
            remaining_skew_faces: int = None,
            n_face_intersections_found: int = None,
            unresolved_face_intersections: int = None):
        """Sets the default values of WrapperImproveResult.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with a wrapper operation.
        n_skew_found: int, optional
            Number of skewed faces found.
        remaining_skew_faces: int, optional
            Number of remaining skew faces.
        n_face_intersections_found: int, optional
            Number of self intersections found.
        unresolved_face_intersections: int, optional
            Number of remaining self intersections.
        """
        args = locals()
        [WrapperImproveResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of WrapperImproveResult.

        Examples
        --------
        >>> WrapperImproveResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in WrapperImproveResult._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["nSkewFound"] = self._n_skew_found
        json_data["remainingSkewFaces"] = self._remaining_skew_faces
        json_data["nFaceIntersectionsFound"] = self._n_face_intersections_found
        json_data["unresolvedFaceIntersections"] = self._unresolved_face_intersections
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nn_skew_found :  %s\nremaining_skew_faces :  %s\nn_face_intersections_found :  %s\nunresolved_face_intersections :  %s" % (self._error_code, self._n_skew_found, self._remaining_skew_faces, self._n_face_intersections_found, self._unresolved_face_intersections)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with a wrapper operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def n_skew_found(self) -> int:
        """Number of skewed faces found.
        """
        return self._n_skew_found

    @n_skew_found.setter
    def n_skew_found(self, value: int):
        self._n_skew_found = value

    @property
    def remaining_skew_faces(self) -> int:
        """Number of remaining skew faces.
        """
        return self._remaining_skew_faces

    @remaining_skew_faces.setter
    def remaining_skew_faces(self, value: int):
        self._remaining_skew_faces = value

    @property
    def n_face_intersections_found(self) -> int:
        """Number of self intersections found.
        """
        return self._n_face_intersections_found

    @n_face_intersections_found.setter
    def n_face_intersections_found(self, value: int):
        self._n_face_intersections_found = value

    @property
    def unresolved_face_intersections(self) -> int:
        """Number of remaining self intersections.
        """
        return self._unresolved_face_intersections

    @unresolved_face_intersections.setter
    def unresolved_face_intersections(self, value: int):
        self._unresolved_face_intersections = value
