""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class VolumetricSizeFieldComputeResults(CoreObject):
    """Results associated with the compute volumetric size field operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            size_field_id: int):
        self._error_code = ErrorCode(error_code)
        self._size_field_id = size_field_id

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            size_field_id: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumetricSizeFieldComputeResults.

        Parameters
        ----------
        model: Model
            Model to create a VolumetricSizeFieldComputeResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the compute volumetric size field operation.
        size_field_id: int, optional
            Id of the computed size field.
        json_data: dict, optional
            JSON dictionary to create a VolumetricSizeFieldComputeResults object with provided parameters.

        Examples
        --------
        >>> volumetric_size_field_compute_results = prime.VolumetricSizeFieldComputeResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["sizeFieldId"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, size_field_id])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    size_field_id)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "VolumetricSizeFieldComputeResults")["VolumetricSizeFieldComputeResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( VolumetricSizeFieldComputeResults._default_params["error_code"] if "error_code" in VolumetricSizeFieldComputeResults._default_params else ErrorCode(json_data["errorCode"])),
                        size_field_id if size_field_id is not None else ( VolumetricSizeFieldComputeResults._default_params["size_field_id"] if "size_field_id" in VolumetricSizeFieldComputeResults._default_params else json_data["sizeFieldId"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            size_field_id: int = None):
        """Set the default values of VolumetricSizeFieldComputeResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the compute volumetric size field operation.
        size_field_id: int, optional
            Id of the computed size field.
        """
        args = locals()
        [VolumetricSizeFieldComputeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumetricSizeFieldComputeResults.

        Examples
        --------
        >>> VolumetricSizeFieldComputeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumetricSizeFieldComputeResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["sizeFieldId"] = self._size_field_id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nsize_field_id :  %s" % (self._error_code, self._size_field_id)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the compute volumetric size field operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def size_field_id(self) -> int:
        """Id of the computed size field.
        """
        return self._size_field_id

    @size_field_id.setter
    def size_field_id(self, value: int):
        self._size_field_id = value

class VolumetricSizeFieldComputeParams(CoreObject):
    """Parameters associated with the compute volumetric size field operation.
    """
    _default_params = {}

    def __initialize(
            self,
            enable_multi_threading: bool):
        self._enable_multi_threading = enable_multi_threading

    def __init__(
            self,
            model: CommunicationManager=None,
            enable_multi_threading: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumetricSizeFieldComputeParams.

        Parameters
        ----------
        model: Model
            Model to create a VolumetricSizeFieldComputeParams object with default parameters.
        enable_multi_threading: bool, optional
            Option to compute volumetric sizefield in parallel using multithreads.
        json_data: dict, optional
            JSON dictionary to create a VolumetricSizeFieldComputeParams object with provided parameters.

        Examples
        --------
        >>> volumetric_size_field_compute_params = prime.VolumetricSizeFieldComputeParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["enableMultiThreading"])
        else:
            all_field_specified = all(arg is not None for arg in [enable_multi_threading])
            if all_field_specified:
                self.__initialize(
                    enable_multi_threading)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "VolumetricSizeFieldComputeParams")["VolumetricSizeFieldComputeParams"]
                    self.__initialize(
                        enable_multi_threading if enable_multi_threading is not None else ( VolumetricSizeFieldComputeParams._default_params["enable_multi_threading"] if "enable_multi_threading" in VolumetricSizeFieldComputeParams._default_params else json_data["enableMultiThreading"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            enable_multi_threading: bool = None):
        """Set the default values of VolumetricSizeFieldComputeParams.

        Parameters
        ----------
        enable_multi_threading: bool, optional
            Option to compute volumetric sizefield in parallel using multithreads.
        """
        args = locals()
        [VolumetricSizeFieldComputeParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumetricSizeFieldComputeParams.

        Examples
        --------
        >>> VolumetricSizeFieldComputeParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumetricSizeFieldComputeParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["enableMultiThreading"] = self._enable_multi_threading
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "enable_multi_threading :  %s" % (self._enable_multi_threading)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def enable_multi_threading(self) -> bool:
        """Option to compute volumetric sizefield in parallel using multithreads.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value
