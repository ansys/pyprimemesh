""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class FileReadResults(CoreObject):
    """Results of file read.
    """
    default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = error_code

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes FileReadResults

        Parameters
        ----------
        model: Model
            Model to create a FileReadResults object with default parameters.
        error_code: ErrorCode, optional
            Appropriate error code is set if the read was unsuccessful.
        json_data: dict, optional
            JSON dictionary to create a FileReadResults object with provided parameters.

        Examples
        --------
        >>> file_read_results = FileReadResults(model = model)
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
                    json_data = model.communicator.initialize_params("FileReadResults")["FileReadResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( FileReadResults.default_params["error_code"] if "error_code" in FileReadResults.default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        args = locals()
        [FileReadResults.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileReadResults.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
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
        """Appropriate error code is set if the read was unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class FileWriteResults(CoreObject):
    """    """
    default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = error_code

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes FileWriteResults

        Parameters
        ----------
        model: Model
            Model to create a FileWriteResults object with default parameters.
        error_code: ErrorCode, optional
        json_data: dict, optional
            JSON dictionary to create a FileWriteResults object with provided parameters.

        Examples
        --------
        >>> file_write_results = FileWriteResults(model = model)
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
                    json_data = model.communicator.initialize_params("FileWriteResults")["FileWriteResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( FileWriteResults.default_params["error_code"] if "error_code" in FileWriteResults.default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        args = locals()
        [FileWriteResults.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileWriteResults.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
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
        """
        Error code if file export operation is unsuccessful
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ExportBoundaryFittedSplineParams(CoreObject):
    """    """
    default_params = {}

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
        """Initializes ExportBoundaryFittedSplineParams

        Parameters
        ----------
        model: Model
            Model to create a ExportBoundaryFittedSplineParams object with default parameters.
        id_offset: int, optional
        id_start: int, optional
        json_data: dict, optional
            JSON dictionary to create a ExportBoundaryFittedSplineParams object with provided parameters.

        Examples
        --------
        >>> export_boundary_fitted_spline_params = ExportBoundaryFittedSplineParams(model = model)
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
                    json_data = model.communicator.initialize_params("ExportBoundaryFittedSplineParams")["ExportBoundaryFittedSplineParams"]
                    self.__initialize(
                        id_offset if id_offset is not None else ( ExportBoundaryFittedSplineParams.default_params["id_offset"] if "id_offset" in ExportBoundaryFittedSplineParams.default_params else json_data["idOffset"]),
                        id_start if id_start is not None else ( ExportBoundaryFittedSplineParams.default_params["id_start"] if "id_start" in ExportBoundaryFittedSplineParams.default_params else json_data["idStart"]))
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
        args = locals()
        [ExportBoundaryFittedSplineParams.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportBoundaryFittedSplineParams.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
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
        """        """
        return self._id_offset

    @id_offset.setter
    def id_offset(self, value: int):
        self._id_offset = value

    @property
    def id_start(self) -> int:
        """        """
        return self._id_start

    @id_start.setter
    def id_start(self, value: int):
        self._id_start = value
