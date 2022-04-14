""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List, Iterable
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
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AutoMeshResults.

        Parameters
        ----------
        model: Model
            Model to create a AutoMeshResults object with default parameters.
        error_code: ErrorCode, optional
            Provides error message when automesh fails.
        json_data: dict, optional
            JSON dictionary to create a AutoMeshResults object with provided parameters.

        Examples
        --------
        >>> auto_mesh_results = prime.AutoMeshResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "AutoMeshResults")["AutoMeshResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( AutoMeshResults._default_params["error_code"] if "error_code" in AutoMeshResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Sets the default values of AutoMeshResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Provides error message when automesh fails.
        """
        args = locals()
        [AutoMeshResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of AutoMeshResults.

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
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
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
        """Sets the default values of TetParams.

        Parameters
        ----------
        quadratic: bool, optional
            Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        """
        args = locals()
        [TetParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of TetParams.

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
            tet: TetParams,
            volume_control_ids: Iterable[int]):
        self._size_field_type = SizeFieldType(size_field_type)
        self._max_size = max_size
        self._prism_control_ids = prism_control_ids if isinstance(prism_control_ids, np.ndarray) else np.array(prism_control_ids, dtype=np.int32)
        self._volume_fill_type = VolumeFillType(volume_fill_type)
        self._tet = tet
        self._volume_control_ids = volume_control_ids if isinstance(volume_control_ids, np.ndarray) else np.array(volume_control_ids, dtype=np.int32)

    def __init__(
            self,
            model: CommunicationManager=None,
            size_field_type: SizeFieldType = None,
            max_size: float = None,
            prism_control_ids: Iterable[int] = None,
            volume_fill_type: VolumeFillType = None,
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
                TetParams(model = model, json_data = json_data["tet"]),
                json_data["volumeControlIds"])
        else:
            all_field_specified = all(arg is not None for arg in [size_field_type, max_size, prism_control_ids, volume_fill_type, tet, volume_control_ids])
            if all_field_specified:
                self.__initialize(
                    size_field_type,
                    max_size,
                    prism_control_ids,
                    volume_fill_type,
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
            tet: TetParams = None,
            volume_control_ids: Iterable[int] = None):
        """Sets the default values of AutoMeshParams.

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
        tet: TetParams, optional
            Parameters to control tetrahedral mesh generation.
        volume_control_ids: Iterable[int], optional
            Ids of the volume controls.
        """
        args = locals()
        [AutoMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of AutoMeshParams.

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
        json_data["tet"] = self._tet._jsonify()
        json_data["volumeControlIds"] = self._volume_control_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "size_field_type :  %s\nmax_size :  %s\nprism_control_ids :  %s\nvolume_fill_type :  %s\ntet :  %s\nvolume_control_ids :  %s" % (self._size_field_type, self._max_size, self._prism_control_ids, self._volume_fill_type, '{ ' + str(self._tet) + ' }', self._volume_control_ids)
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
