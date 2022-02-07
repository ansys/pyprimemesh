""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class SurferParams(CoreObject):
    """Parameters used to generate surface mesh.
    """
    _default_params = {}

    def __initialize(
            self,
            size_field_type: SizeFieldType,
            constant_size: float,
            generate_quads: bool,
            enable_multi_threading: bool):
        self._size_field_type = SizeFieldType(size_field_type)
        self._constant_size = constant_size
        self._generate_quads = generate_quads
        self._enable_multi_threading = enable_multi_threading

    def __init__(
            self,
            model: CommunicationManager=None,
            size_field_type: SizeFieldType = None,
            constant_size: float = None,
            generate_quads: bool = None,
            enable_multi_threading: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurferParams.

        Parameters
        ----------
        model: Model
            Model to create a SurferParams object with default parameters.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        constant_size: float, optional
            Size used in constant size surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        enable_multi_threading: bool, optional
            Option to perform surface meshing in parallel using multi threads.
        json_data: dict, optional
            JSON dictionary to create a SurferParams object with provided parameters.

        Examples
        --------
        >>> surfer_params = prime.SurferParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["sizeFieldType"]),
                json_data["constantSize"],
                json_data["generateQuads"],
                json_data["enableMultiThreading"])
        else:
            all_field_specified = all(arg is not None for arg in [size_field_type, constant_size, generate_quads, enable_multi_threading])
            if all_field_specified:
                self.__initialize(
                    size_field_type,
                    constant_size,
                    generate_quads,
                    enable_multi_threading)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params("SurferParams", model._object_id)["SurferParams"]
                    self.__initialize(
                        size_field_type if size_field_type is not None else ( SurferParams._default_params["size_field_type"] if "size_field_type" in SurferParams._default_params else SizeFieldType(json_data["sizeFieldType"])),
                        constant_size if constant_size is not None else ( SurferParams._default_params["constant_size"] if "constant_size" in SurferParams._default_params else json_data["constantSize"]),
                        generate_quads if generate_quads is not None else ( SurferParams._default_params["generate_quads"] if "generate_quads" in SurferParams._default_params else json_data["generateQuads"]),
                        enable_multi_threading if enable_multi_threading is not None else ( SurferParams._default_params["enable_multi_threading"] if "enable_multi_threading" in SurferParams._default_params else json_data["enableMultiThreading"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            size_field_type: SizeFieldType = None,
            constant_size: float = None,
            generate_quads: bool = None,
            enable_multi_threading: bool = None):
        """Sets the default values of SurferParams.

        Parameters
        ----------
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        constant_size: float, optional
            Size used in constant size surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        enable_multi_threading: bool, optional
            Option to perform surface meshing in parallel using multi threads.
        """
        args = locals()
        [SurferParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of SurferParams.

        Examples
        --------
        >>> SurferParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurferParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["sizeFieldType"] = self._size_field_type
        json_data["constantSize"] = self._constant_size
        json_data["generateQuads"] = self._generate_quads
        json_data["enableMultiThreading"] = self._enable_multi_threading
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "size_field_type :  %s\nconstant_size :  %s\ngenerate_quads :  %s\nenable_multi_threading :  %s" % (self._size_field_type, self._constant_size, self._generate_quads, self._enable_multi_threading)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def size_field_type(self) -> SizeFieldType:
        """Size field type used to generate surface mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def constant_size(self) -> float:
        """Size used in constant size surface meshing.
        """
        return self._constant_size

    @constant_size.setter
    def constant_size(self, value: float):
        self._constant_size = value

    @property
    def generate_quads(self) -> bool:
        """Option to generate quadrilateral surface mesh.
        """
        return self._generate_quads

    @generate_quads.setter
    def generate_quads(self, value: bool):
        self._generate_quads = value

    @property
    def enable_multi_threading(self) -> bool:
        """Option to perform surface meshing in parallel using multi threads.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value

class SurferResults(CoreObject):
    """Results associated with the surface mesh.
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
        """Initializes the SurferResults.

        Parameters
        ----------
        model: Model
            Model to create a SurferResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a SurferResults object with provided parameters.

        Examples
        --------
        >>> surfer_results = prime.SurferResults(model = model)
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
                    json_data = model._communicator.initialize_params("SurferResults")["SurferResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( SurferResults._default_params["error_code"] if "error_code" in SurferResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Sets the default values of SurferResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [SurferResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of SurferResults.

        Examples
        --------
        >>> SurferResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurferResults._default_params.items())
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
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
