""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class PartZonelets(CoreObject):
    """A structure containing some or all face zonelet ids available in a part.
    """
    _default_params = {}

    def __initialize(
            self,
            part_id: int,
            face_zonelets: Iterable[int]):
        self._part_id = part_id
        self._face_zonelets = face_zonelets if isinstance(face_zonelets, np.ndarray) else np.array(face_zonelets, dtype=np.int32) if face_zonelets is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            part_id: int = None,
            face_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PartZonelets.

        Parameters
        ----------
        model: Model
            Model to create a PartZonelets object with default parameters.
        part_id: int, optional
            Id of part.
        face_zonelets: Iterable[int], optional
            List of face zonelet ids available in the part.
        json_data: dict, optional
            JSON dictionary to create a PartZonelets object with provided parameters.

        Examples
        --------
        >>> part_zonelets = prime.PartZonelets(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["partID"] if "partID" in json_data else None,
                json_data["faceZonelets"] if "faceZonelets" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [part_id, face_zonelets])
            if all_field_specified:
                self.__initialize(
                    part_id,
                    face_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "PartZonelets")
                    json_data = param_json["PartZonelets"] if "PartZonelets" in param_json else {}
                    self.__initialize(
                        part_id if part_id is not None else ( PartZonelets._default_params["part_id"] if "part_id" in PartZonelets._default_params else (json_data["partID"] if "partID" in json_data else None)),
                        face_zonelets if face_zonelets is not None else ( PartZonelets._default_params["face_zonelets"] if "face_zonelets" in PartZonelets._default_params else (json_data["faceZonelets"] if "faceZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            part_id: int = None,
            face_zonelets: Iterable[int] = None):
        """Set the default values of PartZonelets.

        Parameters
        ----------
        part_id: int, optional
            Id of part.
        face_zonelets: Iterable[int], optional
            List of face zonelet ids available in the part.
        """
        args = locals()
        [PartZonelets._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PartZonelets.

        Examples
        --------
        >>> PartZonelets.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartZonelets._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._part_id is not None:
            json_data["partID"] = self._part_id
        if self._face_zonelets is not None:
            json_data["faceZonelets"] = self._face_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "part_id :  %s\nface_zonelets :  %s" % (self._part_id, self._face_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def part_id(self) -> int:
        """Id of part.
        """
        return self._part_id

    @part_id.setter
    def part_id(self, value: int):
        self._part_id = value

    @property
    def face_zonelets(self) -> Iterable[int]:
        """List of face zonelet ids available in the part.
        """
        return self._face_zonelets

    @face_zonelets.setter
    def face_zonelets(self, value: Iterable[int]):
        self._face_zonelets = value

class SetNameResults(CoreObject):
    """Results associated with the set name.
    """
    _default_params = {}

    def __initialize(
            self,
            warning_code: WarningCode,
            assigned_name: str,
            error_code: ErrorCode):
        self._warning_code = WarningCode(warning_code)
        self._assigned_name = assigned_name
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            warning_code: WarningCode = None,
            assigned_name: str = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetNameResults.

        Parameters
        ----------
        model: Model
            Model to create a SetNameResults object with default parameters.
        warning_code: WarningCode, optional
            Warning code associated with the set name of given entity.
        assigned_name: str, optional
            Assigned name of given entity.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a SetNameResults object with provided parameters.

        Examples
        --------
        >>> set_name_results = prime.SetNameResults(model = model)
        """
        if json_data:
            self.__initialize(
                WarningCode(json_data["warningCode"] if "warningCode" in json_data else None),
                json_data["assignedName"] if "assignedName" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [warning_code, assigned_name, error_code])
            if all_field_specified:
                self.__initialize(
                    warning_code,
                    assigned_name,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SetNameResults")
                    json_data = param_json["SetNameResults"] if "SetNameResults" in param_json else {}
                    self.__initialize(
                        warning_code if warning_code is not None else ( SetNameResults._default_params["warning_code"] if "warning_code" in SetNameResults._default_params else WarningCode(json_data["warningCode"] if "warningCode" in json_data else None)),
                        assigned_name if assigned_name is not None else ( SetNameResults._default_params["assigned_name"] if "assigned_name" in SetNameResults._default_params else (json_data["assignedName"] if "assignedName" in json_data else None)),
                        error_code if error_code is not None else ( SetNameResults._default_params["error_code"] if "error_code" in SetNameResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            warning_code: WarningCode = None,
            assigned_name: str = None,
            error_code: ErrorCode = None):
        """Set the default values of SetNameResults.

        Parameters
        ----------
        warning_code: WarningCode, optional
            Warning code associated with the set name of given entity.
        assigned_name: str, optional
            Assigned name of given entity.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [SetNameResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SetNameResults.

        Examples
        --------
        >>> SetNameResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetNameResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._warning_code is not None:
            json_data["warningCode"] = self._warning_code
        if self._assigned_name is not None:
            json_data["assignedName"] = self._assigned_name
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "warning_code :  %s\nassigned_name :  %s\nerror_code :  %s" % (self._warning_code, self._assigned_name, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def warning_code(self) -> WarningCode:
        """Warning code associated with the set name of given entity.
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, value: WarningCode):
        self._warning_code = value

    @property
    def assigned_name(self) -> str:
        """Assigned name of given entity.
        """
        return self._assigned_name

    @assigned_name.setter
    def assigned_name(self, value: str):
        self._assigned_name = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class DeleteResults(CoreObject):
    """Results associated with the deletion of items.
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
        """Initializes the DeleteResults.

        Parameters
        ----------
        model: Model
            Model to create a DeleteResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        json_data: dict, optional
            JSON dictionary to create a DeleteResults object with provided parameters.

        Examples
        --------
        >>> delete_results = prime.DeleteResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "DeleteResults")
                    json_data = param_json["DeleteResults"] if "DeleteResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteResults._default_params["error_code"] if "error_code" in DeleteResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of DeleteResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [DeleteResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteResults.

        Examples
        --------
        >>> DeleteResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteResults._default_params.items())
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
