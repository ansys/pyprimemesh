""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class VolumeFillType(enum.IntEnum):
    """Types of volume fill options.
    """
    TET = 0
    """Volume fill using tetrahedral cells."""
    POLY = 1
    """Volume fill using polyhedral cells."""
    HEXCORETET = 2
    """Volume fill using hexahedral cells in the core and tetrahedral cells near the boundary."""
    HEXCOREPOLY = 3
    """Volume fill using hexahedral cells in the core and polyhedral cells near the boundary."""

class AutoMeshResults(CoreObject):
    """Results of volume meshing.
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
        """Initializes the AutoMeshResults.

        Parameters
        ----------
        model: Model
            Model to create a AutoMeshResults object with default parameters.
        error_code: ErrorCode, optional
            Provides error message when automesh fails.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        json_data: dict, optional
            JSON dictionary to create a AutoMeshResults object with provided parameters.

        Examples
        --------
        >>> auto_mesh_results = prime.AutoMeshResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                [WarningCode(data) for data in json_data["warningCodes"]])
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
                    json_data = model._communicator.initialize_params(model, "AutoMeshResults")["AutoMeshResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( AutoMeshResults._default_params["error_code"] if "error_code" in AutoMeshResults._default_params else ErrorCode(json_data["errorCode"])),
                        warning_codes if warning_codes is not None else ( AutoMeshResults._default_params["warning_codes"] if "warning_codes" in AutoMeshResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]))
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
        """Set the default values of AutoMeshResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Provides error message when automesh fails.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [AutoMeshResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AutoMeshResults.

        Examples
        --------
        >>> AutoMeshResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AutoMeshResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Provides error message when automesh fails.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class PrismParams(CoreObject):
    """Parameters to control prism mesh generation.
    """
    _default_params = {}

    def __initialize(
            self,
            no_imprint_zonelets: Iterable[int]):
        self._no_imprint_zonelets = no_imprint_zonelets if isinstance(no_imprint_zonelets, np.ndarray) else np.array(no_imprint_zonelets, dtype=np.int32)

    def __init__(
            self,
            model: CommunicationManager=None,
            no_imprint_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PrismParams.

        Parameters
        ----------
        model: Model
            Model to create a PrismParams object with default parameters.
        no_imprint_zonelets: Iterable[int], optional
            Option to specify zonelets to skip prism imprint.
        json_data: dict, optional
            JSON dictionary to create a PrismParams object with provided parameters.

        Examples
        --------
        >>> prism_params = prime.PrismParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["noImprintZonelets"])
        else:
            all_field_specified = all(arg is not None for arg in [no_imprint_zonelets])
            if all_field_specified:
                self.__initialize(
                    no_imprint_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "PrismParams")["PrismParams"]
                    self.__initialize(
                        no_imprint_zonelets if no_imprint_zonelets is not None else ( PrismParams._default_params["no_imprint_zonelets"] if "no_imprint_zonelets" in PrismParams._default_params else json_data["noImprintZonelets"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            no_imprint_zonelets: Iterable[int] = None):
        """Set the default values of PrismParams.

        Parameters
        ----------
        no_imprint_zonelets: Iterable[int], optional
            Option to specify zonelets to skip prism imprint.
        """
        args = locals()
        [PrismParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PrismParams.

        Examples
        --------
        >>> PrismParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PrismParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["noImprintZonelets"] = self._no_imprint_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "no_imprint_zonelets :  %s" % (self._no_imprint_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def no_imprint_zonelets(self) -> Iterable[int]:
        """Option to specify zonelets to skip prism imprint.
        """
        return self._no_imprint_zonelets

    @no_imprint_zonelets.setter
    def no_imprint_zonelets(self, value: Iterable[int]):
        self._no_imprint_zonelets = value

class TetParams(CoreObject):
    """Parameters to control tetrahedral mesh generation.
    """
    _default_params = {}

    def __initialize(
            self,
            quadratic: bool):
        self._quadratic = quadratic

    def __init__(
            self,
            model: CommunicationManager=None,
            quadratic: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the TetParams.

        Parameters
        ----------
        model: Model
            Model to create a TetParams object with default parameters.
        quadratic: bool, optional
            Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        json_data: dict, optional
            JSON dictionary to create a TetParams object with provided parameters.

        Examples
        --------
        >>> tet_params = prime.TetParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["quadratic"])
        else:
            all_field_specified = all(arg is not None for arg in [quadratic])
            if all_field_specified:
                self.__initialize(
                    quadratic)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "TetParams")["TetParams"]
                    self.__initialize(
                        quadratic if quadratic is not None else ( TetParams._default_params["quadratic"] if "quadratic" in TetParams._default_params else json_data["quadratic"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            quadratic: bool = None):
        """Set the default values of TetParams.

        Parameters
        ----------
        quadratic: bool, optional
            Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        """
        args = locals()
        [TetParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of TetParams.

        Examples
        --------
        >>> TetParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TetParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["quadratic"] = self._quadratic
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "quadratic :  %s" % (self._quadratic)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def quadratic(self) -> bool:
        """Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        """
        return self._quadratic

    @quadratic.setter
    def quadratic(self, value: bool):
        self._quadratic = value

class AutoMeshParams(CoreObject):
    """Parameters for volume meshing.
    """
    _default_params = {}

    def __initialize(
            self,
            size_field_type: SizeFieldType,
            max_size: float,
            prism_control_ids: Iterable[int],
            volume_fill_type: VolumeFillType,
            prism: PrismParams,
            tet: TetParams,
            volume_control_ids: Iterable[int]):
        self._size_field_type = SizeFieldType(size_field_type)
        self._max_size = max_size
        self._prism_control_ids = prism_control_ids if isinstance(prism_control_ids, np.ndarray) else np.array(prism_control_ids, dtype=np.int32)
        self._volume_fill_type = VolumeFillType(volume_fill_type)
        self._prism = prism
        self._tet = tet
        self._volume_control_ids = volume_control_ids if isinstance(volume_control_ids, np.ndarray) else np.array(volume_control_ids, dtype=np.int32)

    def __init__(
            self,
            model: CommunicationManager=None,
            size_field_type: SizeFieldType = None,
            max_size: float = None,
            prism_control_ids: Iterable[int] = None,
            volume_fill_type: VolumeFillType = None,
            prism: PrismParams = None,
            tet: TetParams = None,
            volume_control_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AutoMeshParams.

        Parameters
        ----------
        model: Model
            Model to create a AutoMeshParams object with default parameters.
        size_field_type: SizeFieldType, optional
            Type of sizing to be used to generate volume mesh.
        max_size: float, optional
            Maximum cell size.
        prism_control_ids: Iterable[int], optional
            Set prism control ids.
        volume_fill_type: VolumeFillType, optional
            Option to fill volume.
        prism: PrismParams, optional
            Prism control parameters.
        tet: TetParams, optional
            Parameters to control tetrahedral mesh generation.
        volume_control_ids: Iterable[int], optional
            Ids of the volume controls.
        json_data: dict, optional
            JSON dictionary to create a AutoMeshParams object with provided parameters.

        Examples
        --------
        >>> auto_mesh_params = prime.AutoMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["sizeFieldType"]),
                json_data["maxSize"],
                json_data["prismControlIds"],
                VolumeFillType(json_data["volumeFillType"]),
                PrismParams(model = model, json_data = json_data["prism"]),
                TetParams(model = model, json_data = json_data["tet"]),
                json_data["volumeControlIds"])
        else:
            all_field_specified = all(arg is not None for arg in [size_field_type, max_size, prism_control_ids, volume_fill_type, prism, tet, volume_control_ids])
            if all_field_specified:
                self.__initialize(
                    size_field_type,
                    max_size,
                    prism_control_ids,
                    volume_fill_type,
                    prism,
                    tet,
                    volume_control_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "AutoMeshParams")["AutoMeshParams"]
                    self.__initialize(
                        size_field_type if size_field_type is not None else ( AutoMeshParams._default_params["size_field_type"] if "size_field_type" in AutoMeshParams._default_params else SizeFieldType(json_data["sizeFieldType"])),
                        max_size if max_size is not None else ( AutoMeshParams._default_params["max_size"] if "max_size" in AutoMeshParams._default_params else json_data["maxSize"]),
                        prism_control_ids if prism_control_ids is not None else ( AutoMeshParams._default_params["prism_control_ids"] if "prism_control_ids" in AutoMeshParams._default_params else json_data["prismControlIds"]),
                        volume_fill_type if volume_fill_type is not None else ( AutoMeshParams._default_params["volume_fill_type"] if "volume_fill_type" in AutoMeshParams._default_params else VolumeFillType(json_data["volumeFillType"])),
                        prism if prism is not None else ( AutoMeshParams._default_params["prism"] if "prism" in AutoMeshParams._default_params else PrismParams(model = model, json_data = json_data["prism"])),
                        tet if tet is not None else ( AutoMeshParams._default_params["tet"] if "tet" in AutoMeshParams._default_params else TetParams(model = model, json_data = json_data["tet"])),
                        volume_control_ids if volume_control_ids is not None else ( AutoMeshParams._default_params["volume_control_ids"] if "volume_control_ids" in AutoMeshParams._default_params else json_data["volumeControlIds"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            size_field_type: SizeFieldType = None,
            max_size: float = None,
            prism_control_ids: Iterable[int] = None,
            volume_fill_type: VolumeFillType = None,
            prism: PrismParams = None,
            tet: TetParams = None,
            volume_control_ids: Iterable[int] = None):
        """Set the default values of AutoMeshParams.

        Parameters
        ----------
        size_field_type: SizeFieldType, optional
            Type of sizing to be used to generate volume mesh.
        max_size: float, optional
            Maximum cell size.
        prism_control_ids: Iterable[int], optional
            Set prism control ids.
        volume_fill_type: VolumeFillType, optional
            Option to fill volume.
        prism: PrismParams, optional
            Prism control parameters.
        tet: TetParams, optional
            Parameters to control tetrahedral mesh generation.
        volume_control_ids: Iterable[int], optional
            Ids of the volume controls.
        """
        args = locals()
        [AutoMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AutoMeshParams.

        Examples
        --------
        >>> AutoMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AutoMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["sizeFieldType"] = self._size_field_type
        json_data["maxSize"] = self._max_size
        json_data["prismControlIds"] = self._prism_control_ids
        json_data["volumeFillType"] = self._volume_fill_type
        json_data["prism"] = self._prism._jsonify()
        json_data["tet"] = self._tet._jsonify()
        json_data["volumeControlIds"] = self._volume_control_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "size_field_type :  %s\nmax_size :  %s\nprism_control_ids :  %s\nvolume_fill_type :  %s\nprism :  %s\ntet :  %s\nvolume_control_ids :  %s" % (self._size_field_type, self._max_size, self._prism_control_ids, self._volume_fill_type, '{ ' + str(self._prism) + ' }', '{ ' + str(self._tet) + ' }', self._volume_control_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def size_field_type(self) -> SizeFieldType:
        """Type of sizing to be used to generate volume mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def max_size(self) -> float:
        """Maximum cell size.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def prism_control_ids(self) -> Iterable[int]:
        """Set prism control ids.
        """
        return self._prism_control_ids

    @prism_control_ids.setter
    def prism_control_ids(self, value: Iterable[int]):
        self._prism_control_ids = value

    @property
    def volume_fill_type(self) -> VolumeFillType:
        """Option to fill volume.
        """
        return self._volume_fill_type

    @volume_fill_type.setter
    def volume_fill_type(self, value: VolumeFillType):
        self._volume_fill_type = value

    @property
    def prism(self) -> PrismParams:
        """Prism control parameters.
        """
        return self._prism

    @prism.setter
    def prism(self, value: PrismParams):
        self._prism = value

    @property
    def tet(self) -> TetParams:
        """Parameters to control tetrahedral mesh generation.
        """
        return self._tet

    @tet.setter
    def tet(self, value: TetParams):
        self._tet = value

    @property
    def volume_control_ids(self) -> Iterable[int]:
        """Ids of the volume controls.
        """
        return self._volume_control_ids

    @volume_control_ids.setter
    def volume_control_ids(self, value: Iterable[int]):
        self._volume_control_ids = value
