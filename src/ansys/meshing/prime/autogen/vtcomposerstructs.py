""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class VTComposerParams(CoreObject):
    """Parameters to control VTComposer operations.
    """
    _default_params = {}

    def __initialize(
            self,
            thin_stripes_tol: float):
        self._thin_stripes_tol = thin_stripes_tol

    def __init__(
            self,
            model: CommunicationManager=None,
            thin_stripes_tol: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VTComposerParams.

        Parameters
        ----------
        model: Model
            Model to create a VTComposerParams object with default parameters.
        thin_stripes_tol: float, optional
            This parameter is a Beta. Parameter behavior and name may change in future.
        json_data: dict, optional
            JSON dictionary to create a VTComposerParams object with provided parameters.

        Examples
        --------
        >>> v_tcomposer_params = prime.VTComposerParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["thinStripesTol"] if "thinStripesTol" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [thin_stripes_tol])
            if all_field_specified:
                self.__initialize(
                    thin_stripes_tol)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VTComposerParams")
                    json_data = param_json["VTComposerParams"] if "VTComposerParams" in param_json else {}
                    self.__initialize(
                        thin_stripes_tol if thin_stripes_tol is not None else ( VTComposerParams._default_params["thin_stripes_tol"] if "thin_stripes_tol" in VTComposerParams._default_params else (json_data["thinStripesTol"] if "thinStripesTol" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            thin_stripes_tol: float = None):
        """Set the default values of VTComposerParams.

        Parameters
        ----------
        thin_stripes_tol: float, optional
        """
        args = locals()
        [VTComposerParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VTComposerParams.

        Examples
        --------
        >>> VTComposerParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VTComposerParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._thin_stripes_tol is not None:
            json_data["thinStripesTol"] = self._thin_stripes_tol
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "thin_stripes_tol :  %s" % (self._thin_stripes_tol)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def thin_stripes_tol(self) -> float:
        """        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._thin_stripes_tol

    @thin_stripes_tol.setter
    def thin_stripes_tol(self, value: float):
        self._thin_stripes_tol = value

class VTComposerResults(CoreObject):
    """Result struct associated to VTComposer operations.
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
        """Initializes the VTComposerResults.

        Parameters
        ----------
        model: Model
            Model to create a VTComposerResults object with default parameters.
        error_code: ErrorCode, optional
            This parameter is a Beta. Parameter behavior and name may change in future.
        json_data: dict, optional
            JSON dictionary to create a VTComposerResults object with provided parameters.

        Examples
        --------
        >>> v_tcomposer_results = prime.VTComposerResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "VTComposerResults")
                    json_data = param_json["VTComposerResults"] if "VTComposerResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( VTComposerResults._default_params["error_code"] if "error_code" in VTComposerResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of VTComposerResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
        """
        args = locals()
        [VTComposerResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VTComposerResults.

        Examples
        --------
        >>> VTComposerResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VTComposerResults._default_params.items())
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
        """        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
