""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class TransformResults(CoreObject):
    """Results associated with the transformation.
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
        """Initializes the TransformResults.

        Parameters
        ----------
        model: Model
            Model to create a TransformResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a TransformResults object with provided parameters.

        Examples
        --------
        >>> transform_results = prime.TransformResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "TransformResults")
                    json_data = param_json["TransformResults"] if "TransformResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( TransformResults._default_params["error_code"] if "error_code" in TransformResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of TransformResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [TransformResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of TransformResults.

        Examples
        --------
        >>> TransformResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TransformResults._default_params.items())
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
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class TransformParams(CoreObject):
    """Parameters to transform given entities.
    """
    _default_params = {}

    def __initialize(
            self,
            transformation_matrix: Iterable[float]):
        self._transformation_matrix = transformation_matrix if isinstance(transformation_matrix, np.ndarray) else np.array(transformation_matrix, dtype=np.double) if transformation_matrix is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            transformation_matrix: Iterable[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the TransformParams.

        Parameters
        ----------
        model: Model
            Model to create a TransformParams object with default parameters.
        transformation_matrix: Iterable[float], optional
            Transformation matrix(4x4) to be used to transform.
        json_data: dict, optional
            JSON dictionary to create a TransformParams object with provided parameters.

        Examples
        --------
        >>> transform_params = prime.TransformParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["transformationMatrix"] if "transformationMatrix" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [transformation_matrix])
            if all_field_specified:
                self.__initialize(
                    transformation_matrix)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "TransformParams")
                    json_data = param_json["TransformParams"] if "TransformParams" in param_json else {}
                    self.__initialize(
                        transformation_matrix if transformation_matrix is not None else ( TransformParams._default_params["transformation_matrix"] if "transformation_matrix" in TransformParams._default_params else (json_data["transformationMatrix"] if "transformationMatrix" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            transformation_matrix: Iterable[float] = None):
        """Set the default values of TransformParams.

        Parameters
        ----------
        transformation_matrix: Iterable[float], optional
            Transformation matrix(4x4) to be used to transform.
        """
        args = locals()
        [TransformParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of TransformParams.

        Examples
        --------
        >>> TransformParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TransformParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._transformation_matrix is not None:
            json_data["transformationMatrix"] = self._transformation_matrix
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "transformation_matrix :  %s" % (self._transformation_matrix)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def transformation_matrix(self) -> Iterable[float]:
        """Transformation matrix(4x4) to be used to transform.
        """
        return self._transformation_matrix

    @transformation_matrix.setter
    def transformation_matrix(self, value: Iterable[float]):
        self._transformation_matrix = value
