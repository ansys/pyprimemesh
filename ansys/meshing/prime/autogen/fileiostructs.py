""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class FileReadResults(CoreObject):
    """Results of file read operation.
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
        """Initializes the FileReadResults.

        Parameters
        ----------
        model: Model
            Model to create a FileReadResults object with default parameters.
        error_code: ErrorCode, optional
            Error code if file read operation was unsuccessful.
        json_data: dict, optional
            JSON dictionary to create a FileReadResults object with provided parameters.

        Examples
        --------
        >>> file_read_results = prime.FileReadResults(model = model)
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
                    json_data = model._communicator.initialize_params("FileReadResults")["FileReadResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( FileReadResults._default_params["error_code"] if "error_code" in FileReadResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Sets the default values of FileReadResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if file read operation was unsuccessful.
        """
        args = locals()
        [FileReadResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of FileReadResults.

        Examples
        --------
        >>> FileReadResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileReadResults._default_params.items())
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
        """Error code if file read operation was unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class FileWriteResults(CoreObject):
    """Results of file write operation.
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
        """Initializes the FileWriteResults.

        Parameters
        ----------
        model: Model
            Model to create a FileWriteResults object with default parameters.
        error_code: ErrorCode, optional
            Error code if file write operation is unsuccessful.
        json_data: dict, optional
            JSON dictionary to create a FileWriteResults object with provided parameters.

        Examples
        --------
        >>> file_write_results = prime.FileWriteResults(model = model)
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
                    json_data = model._communicator.initialize_params("FileWriteResults")["FileWriteResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( FileWriteResults._default_params["error_code"] if "error_code" in FileWriteResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Sets the default values of FileWriteResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if file write operation is unsuccessful.
        """
        args = locals()
        [FileWriteResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of FileWriteResults.

        Examples
        --------
        >>> FileWriteResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileWriteResults._default_params.items())
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
        """Error code if file write operation is unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ExportBoundaryFittedSplineParams(CoreObject):
    """Parameters for exporting boundary fitted splines.
    """
    _default_params = {}

    def __initialize(
            self,
            id_offset: int,
            id_start: int):
        self._id_offset = id_offset
        self._id_start = id_start

    def __init__(
            self,
            model: CommunicationManager=None,
            id_offset: int = None,
            id_start: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExportBoundaryFittedSplineParams.

        Parameters
        ----------
        model: Model
            Model to create a ExportBoundaryFittedSplineParams object with default parameters.
        id_offset: int, optional
            Offset value for IGA entity ids between parts.
        id_start: int, optional
            Start ids for IGA entities.
        json_data: dict, optional
            JSON dictionary to create a ExportBoundaryFittedSplineParams object with provided parameters.

        Examples
        --------
        >>> export_boundary_fitted_spline_params = prime.ExportBoundaryFittedSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["idOffset"],
                json_data["idStart"])
        else:
            all_field_specified = all(arg is not None for arg in [id_offset, id_start])
            if all_field_specified:
                self.__initialize(
                    id_offset,
                    id_start)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params("ExportBoundaryFittedSplineParams")["ExportBoundaryFittedSplineParams"]
                    self.__initialize(
                        id_offset if id_offset is not None else ( ExportBoundaryFittedSplineParams._default_params["id_offset"] if "id_offset" in ExportBoundaryFittedSplineParams._default_params else json_data["idOffset"]),
                        id_start if id_start is not None else ( ExportBoundaryFittedSplineParams._default_params["id_start"] if "id_start" in ExportBoundaryFittedSplineParams._default_params else json_data["idStart"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            id_offset: int = None,
            id_start: int = None):
        """Sets the default values of ExportBoundaryFittedSplineParams.

        Parameters
        ----------
        id_offset: int, optional
            Offset value for IGA entity ids between parts.
        id_start: int, optional
            Start ids for IGA entities.
        """
        args = locals()
        [ExportBoundaryFittedSplineParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of ExportBoundaryFittedSplineParams.

        Examples
        --------
        >>> ExportBoundaryFittedSplineParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportBoundaryFittedSplineParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["idOffset"] = self._id_offset
        json_data["idStart"] = self._id_start
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "id_offset :  %s\nid_start :  %s" % (self._id_offset, self._id_start)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def id_offset(self) -> int:
        """Offset value for IGA entity ids between parts.
        """
        return self._id_offset

    @id_offset.setter
    def id_offset(self, value: int):
        self._id_offset = value

    @property
    def id_start(self) -> int:
        """Start ids for IGA entities.
        """
        return self._id_start

    @id_start.setter
    def id_start(self, value: int):
        self._id_start = value
