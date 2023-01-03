""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class CopyZoneletsParams(CoreObject):
    """Parameters to copy zonelets. This is for internal use only.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CopyZoneletsParams.

        Parameters
        ----------
        model: Model
            Model to create a CopyZoneletsParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a CopyZoneletsParams object with provided parameters.

        Examples
        --------
        >>> copy_zonelets_params = prime.CopyZoneletsParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "CopyZoneletsParams")["CopyZoneletsParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of CopyZoneletsParams.

        """
        args = locals()
        [CopyZoneletsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CopyZoneletsParams.

        Examples
        --------
        >>> CopyZoneletsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CopyZoneletsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class CopyZoneletsResults(CoreObject):
    """Result structure associated with copying zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            copied_zonelets: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._copied_zonelets = copied_zonelets if isinstance(copied_zonelets, np.ndarray) else np.array(copied_zonelets, dtype=np.int32)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            copied_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CopyZoneletsResults.

        Parameters
        ----------
        model: Model
            Model to create a CopyZoneletsResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        copied_zonelets: Iterable[int], optional
            Copied zonelet ids.
        json_data: dict, optional
            JSON dictionary to create a CopyZoneletsResults object with provided parameters.

        Examples
        --------
        >>> copy_zonelets_results = prime.CopyZoneletsResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["copiedZonelets"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, copied_zonelets])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    copied_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "CopyZoneletsResults")["CopyZoneletsResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( CopyZoneletsResults._default_params["error_code"] if "error_code" in CopyZoneletsResults._default_params else ErrorCode(json_data["errorCode"])),
                        copied_zonelets if copied_zonelets is not None else ( CopyZoneletsResults._default_params["copied_zonelets"] if "copied_zonelets" in CopyZoneletsResults._default_params else json_data["copiedZonelets"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            copied_zonelets: Iterable[int] = None):
        """Set the default values of CopyZoneletsResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        copied_zonelets: Iterable[int], optional
            Copied zonelet ids.
        """
        args = locals()
        [CopyZoneletsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CopyZoneletsResults.

        Examples
        --------
        >>> CopyZoneletsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CopyZoneletsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["copiedZonelets"] = self._copied_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\ncopied_zonelets :  %s" % (self._error_code, self._copied_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def copied_zonelets(self) -> Iterable[int]:
        """Copied zonelet ids.
        """
        return self._copied_zonelets

    @copied_zonelets.setter
    def copied_zonelets(self, value: Iterable[int]):
        self._copied_zonelets = value

class FillHolesAtPlaneParams(CoreObject):
    """Parameters to fill holes at given plane.
    """
    _default_params = {}

    def __initialize(
            self,
            create_zone: bool,
            suggested_zone_name: str):
        self._create_zone = create_zone
        self._suggested_zone_name = suggested_zone_name

    def __init__(
            self,
            model: CommunicationManager=None,
            create_zone: bool = None,
            suggested_zone_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FillHolesAtPlaneParams.

        Parameters
        ----------
        model: Model
            Model to create a FillHolesAtPlaneParams object with default parameters.
        create_zone: bool, optional
            Option to create a face zone for the zonelets created to fill holes.
        suggested_zone_name: str, optional
            Suggested name to be set on merged part. Default name will be used if empty name is suggested.
        json_data: dict, optional
            JSON dictionary to create a FillHolesAtPlaneParams object with provided parameters.

        Examples
        --------
        >>> fill_holes_at_plane_params = prime.FillHolesAtPlaneParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["createZone"],
                json_data["suggestedZoneName"])
        else:
            all_field_specified = all(arg is not None for arg in [create_zone, suggested_zone_name])
            if all_field_specified:
                self.__initialize(
                    create_zone,
                    suggested_zone_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "FillHolesAtPlaneParams")["FillHolesAtPlaneParams"]
                    self.__initialize(
                        create_zone if create_zone is not None else ( FillHolesAtPlaneParams._default_params["create_zone"] if "create_zone" in FillHolesAtPlaneParams._default_params else json_data["createZone"]),
                        suggested_zone_name if suggested_zone_name is not None else ( FillHolesAtPlaneParams._default_params["suggested_zone_name"] if "suggested_zone_name" in FillHolesAtPlaneParams._default_params else json_data["suggestedZoneName"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            create_zone: bool = None,
            suggested_zone_name: str = None):
        """Set the default values of FillHolesAtPlaneParams.

        Parameters
        ----------
        create_zone: bool, optional
            Option to create a face zone for the zonelets created to fill holes.
        suggested_zone_name: str, optional
            Suggested name to be set on merged part. Default name will be used if empty name is suggested.
        """
        args = locals()
        [FillHolesAtPlaneParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FillHolesAtPlaneParams.

        Examples
        --------
        >>> FillHolesAtPlaneParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FillHolesAtPlaneParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["createZone"] = self._create_zone
        json_data["suggestedZoneName"] = self._suggested_zone_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "create_zone :  %s\nsuggested_zone_name :  %s" % (self._create_zone, self._suggested_zone_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def create_zone(self) -> bool:
        """Option to create a face zone for the zonelets created to fill holes.
        """
        return self._create_zone

    @create_zone.setter
    def create_zone(self, value: bool):
        self._create_zone = value

    @property
    def suggested_zone_name(self) -> str:
        """Suggested name to be set on merged part. Default name will be used if empty name is suggested.
        """
        return self._suggested_zone_name

    @suggested_zone_name.setter
    def suggested_zone_name(self, value: str):
        self._suggested_zone_name = value

class FillHolesAtPlaneResults(CoreObject):
    """Results associated with fill holes at given plane.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode],
            created_face_zonelets: Iterable[int],
            assigned_zone_name: str,
            created_zone_id: int):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes
        self._created_face_zonelets = created_face_zonelets if isinstance(created_face_zonelets, np.ndarray) else np.array(created_face_zonelets, dtype=np.int32)
        self._assigned_zone_name = assigned_zone_name
        self._created_zone_id = created_zone_id

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            created_face_zonelets: Iterable[int] = None,
            assigned_zone_name: str = None,
            created_zone_id: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FillHolesAtPlaneResults.

        Parameters
        ----------
        model: Model
            Model to create a FillHolesAtPlaneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with operation.
        created_face_zonelets: Iterable[int], optional
            Ids of face zonelets created to fill the holes.
        assigned_zone_name: str, optional
            Name assigned to zone created. Suffix is added to suggested name if the name not available.
        created_zone_id: int, optional
            Id assigned to zone created.
        json_data: dict, optional
            JSON dictionary to create a FillHolesAtPlaneResults object with provided parameters.

        Examples
        --------
        >>> fill_holes_at_plane_results = prime.FillHolesAtPlaneResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                [WarningCode(data) for data in json_data["warningCodes"]],
                json_data["createdFaceZonelets"],
                json_data["assignedZoneName"],
                json_data["createdZoneId"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes, created_face_zonelets, assigned_zone_name, created_zone_id])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes,
                    created_face_zonelets,
                    assigned_zone_name,
                    created_zone_id)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "FillHolesAtPlaneResults")["FillHolesAtPlaneResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( FillHolesAtPlaneResults._default_params["error_code"] if "error_code" in FillHolesAtPlaneResults._default_params else ErrorCode(json_data["errorCode"])),
                        warning_codes if warning_codes is not None else ( FillHolesAtPlaneResults._default_params["warning_codes"] if "warning_codes" in FillHolesAtPlaneResults._default_params else [WarningCode(data) for data in json_data["warningCodes"]]),
                        created_face_zonelets if created_face_zonelets is not None else ( FillHolesAtPlaneResults._default_params["created_face_zonelets"] if "created_face_zonelets" in FillHolesAtPlaneResults._default_params else json_data["createdFaceZonelets"]),
                        assigned_zone_name if assigned_zone_name is not None else ( FillHolesAtPlaneResults._default_params["assigned_zone_name"] if "assigned_zone_name" in FillHolesAtPlaneResults._default_params else json_data["assignedZoneName"]),
                        created_zone_id if created_zone_id is not None else ( FillHolesAtPlaneResults._default_params["created_zone_id"] if "created_zone_id" in FillHolesAtPlaneResults._default_params else json_data["createdZoneId"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            created_face_zonelets: Iterable[int] = None,
            assigned_zone_name: str = None,
            created_zone_id: int = None):
        """Set the default values of FillHolesAtPlaneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with operation.
        created_face_zonelets: Iterable[int], optional
            Ids of face zonelets created to fill the holes.
        assigned_zone_name: str, optional
            Name assigned to zone created. Suffix is added to suggested name if the name not available.
        created_zone_id: int, optional
            Id assigned to zone created.
        """
        args = locals()
        [FillHolesAtPlaneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FillHolesAtPlaneResults.

        Examples
        --------
        >>> FillHolesAtPlaneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FillHolesAtPlaneResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["warningCodes"] = [data for data in self._warning_codes]
        json_data["createdFaceZonelets"] = self._created_face_zonelets
        json_data["assignedZoneName"] = self._assigned_zone_name
        json_data["createdZoneId"] = self._created_zone_id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s\ncreated_face_zonelets :  %s\nassigned_zone_name :  %s\ncreated_zone_id :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._created_face_zonelets, self._assigned_zone_name, self._created_zone_id)
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

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def created_face_zonelets(self) -> Iterable[int]:
        """Ids of face zonelets created to fill the holes.
        """
        return self._created_face_zonelets

    @created_face_zonelets.setter
    def created_face_zonelets(self, value: Iterable[int]):
        self._created_face_zonelets = value

    @property
    def assigned_zone_name(self) -> str:
        """Name assigned to zone created. Suffix is added to suggested name if the name not available.
        """
        return self._assigned_zone_name

    @assigned_zone_name.setter
    def assigned_zone_name(self, value: str):
        self._assigned_zone_name = value

    @property
    def created_zone_id(self) -> int:
        """Id assigned to zone created.
        """
        return self._created_zone_id

    @created_zone_id.setter
    def created_zone_id(self, value: int):
        self._created_zone_id = value

class CreateCapParams(CoreObject):
    """Parameters to create cap on face zonelets.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateCapParams.

        Parameters
        ----------
        model: Model
            Model to create a CreateCapParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a CreateCapParams object with provided parameters.

        Examples
        --------
        >>> create_cap_params = prime.CreateCapParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "CreateCapParams")["CreateCapParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of CreateCapParams.

        """
        args = locals()
        [CreateCapParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateCapParams.

        Examples
        --------
        >>> CreateCapParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateCapParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class CreateCapResults(CoreObject):
    """Results associated with create cap on face zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            created_face_zonelets: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._created_face_zonelets = created_face_zonelets if isinstance(created_face_zonelets, np.ndarray) else np.array(created_face_zonelets, dtype=np.int32)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            created_face_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateCapResults.

        Parameters
        ----------
        model: Model
            Model to create a CreateCapResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        created_face_zonelets: Iterable[int], optional
            Ids of cap face zonelets created.
        json_data: dict, optional
            JSON dictionary to create a CreateCapResults object with provided parameters.

        Examples
        --------
        >>> create_cap_results = prime.CreateCapResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["createdFaceZonelets"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, created_face_zonelets])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    created_face_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "CreateCapResults")["CreateCapResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( CreateCapResults._default_params["error_code"] if "error_code" in CreateCapResults._default_params else ErrorCode(json_data["errorCode"])),
                        created_face_zonelets if created_face_zonelets is not None else ( CreateCapResults._default_params["created_face_zonelets"] if "created_face_zonelets" in CreateCapResults._default_params else json_data["createdFaceZonelets"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            created_face_zonelets: Iterable[int] = None):
        """Set the default values of CreateCapResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        created_face_zonelets: Iterable[int], optional
            Ids of cap face zonelets created.
        """
        args = locals()
        [CreateCapResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateCapResults.

        Examples
        --------
        >>> CreateCapResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateCapResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["createdFaceZonelets"] = self._created_face_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\ncreated_face_zonelets :  %s" % (self._error_code, self._created_face_zonelets)
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

    @property
    def created_face_zonelets(self) -> Iterable[int]:
        """Ids of cap face zonelets created.
        """
        return self._created_face_zonelets

    @created_face_zonelets.setter
    def created_face_zonelets(self, value: Iterable[int]):
        self._created_face_zonelets = value

class DeleteUnwettedParams(CoreObject):
    """DeleteUnwettedParams defines parameters for delete unwetted surfaces operation.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteUnwettedParams.

        Parameters
        ----------
        model: Model
            Model to create a DeleteUnwettedParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a DeleteUnwettedParams object with provided parameters.

        Examples
        --------
        >>> delete_unwetted_params = prime.DeleteUnwettedParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "DeleteUnwettedParams")["DeleteUnwettedParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of DeleteUnwettedParams.

        """
        args = locals()
        [DeleteUnwettedParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteUnwettedParams.

        Examples
        --------
        >>> DeleteUnwettedParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteUnwettedParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class DeleteUnwettedResult(CoreObject):
    """Results structure associated with delete unwetted surfaces operation.
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
        """Initializes the DeleteUnwettedResult.

        Parameters
        ----------
        model: Model
            Model to create a DeleteUnwettedResult object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with delete unwetted surfaces operation.
        json_data: dict, optional
            JSON dictionary to create a DeleteUnwettedResult object with provided parameters.

        Examples
        --------
        >>> delete_unwetted_result = prime.DeleteUnwettedResult(model = model)
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
                    json_data = model._communicator.initialize_params(model, "DeleteUnwettedResult")["DeleteUnwettedResult"]
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteUnwettedResult._default_params["error_code"] if "error_code" in DeleteUnwettedResult._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of DeleteUnwettedResult.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with delete unwetted surfaces operation.
        """
        args = locals()
        [DeleteUnwettedResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteUnwettedResult.

        Examples
        --------
        >>> DeleteUnwettedResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteUnwettedResult._default_params.items())
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
        """Error code associated with delete unwetted surfaces operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ResolveIntersectionsParams(CoreObject):
    """ResolveIntersectionsParams define parameters for resolve intersections.
    """
    _default_params = {}

    def __initialize(
            self,
            number_of_threads: int):
        self._number_of_threads = number_of_threads

    def __init__(
            self,
            model: CommunicationManager=None,
            number_of_threads: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ResolveIntersectionsParams.

        Parameters
        ----------
        model: Model
            Model to create a ResolveIntersectionsParams object with default parameters.
        number_of_threads: int, optional
            Number of threads for resolve intersections multithreaded operation.
        json_data: dict, optional
            JSON dictionary to create a ResolveIntersectionsParams object with provided parameters.

        Examples
        --------
        >>> resolve_intersections_params = prime.ResolveIntersectionsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["numberOfThreads"])
        else:
            all_field_specified = all(arg is not None for arg in [number_of_threads])
            if all_field_specified:
                self.__initialize(
                    number_of_threads)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "ResolveIntersectionsParams")["ResolveIntersectionsParams"]
                    self.__initialize(
                        number_of_threads if number_of_threads is not None else ( ResolveIntersectionsParams._default_params["number_of_threads"] if "number_of_threads" in ResolveIntersectionsParams._default_params else json_data["numberOfThreads"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            number_of_threads: int = None):
        """Set the default values of ResolveIntersectionsParams.

        Parameters
        ----------
        number_of_threads: int, optional
            Number of threads for resolve intersections multithreaded operation.
        """
        args = locals()
        [ResolveIntersectionsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ResolveIntersectionsParams.

        Examples
        --------
        >>> ResolveIntersectionsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ResolveIntersectionsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["numberOfThreads"] = self._number_of_threads
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "number_of_threads :  %s" % (self._number_of_threads)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def number_of_threads(self) -> int:
        """Number of threads for resolve intersections multithreaded operation.
        """
        return self._number_of_threads

    @number_of_threads.setter
    def number_of_threads(self, value: int):
        self._number_of_threads = value

class ResolveIntersectionResult(CoreObject):
    """Result structure associated with resolve intersections operation.
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
        """Initializes the ResolveIntersectionResult.

        Parameters
        ----------
        model: Model
            Model to create a ResolveIntersectionResult object with default parameters.
        error_code: ErrorCode, optional
            Errror code associated with a resolve intersections operation.
        json_data: dict, optional
            JSON dictionary to create a ResolveIntersectionResult object with provided parameters.

        Examples
        --------
        >>> resolve_intersection_result = prime.ResolveIntersectionResult(model = model)
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
                    json_data = model._communicator.initialize_params(model, "ResolveIntersectionResult")["ResolveIntersectionResult"]
                    self.__initialize(
                        error_code if error_code is not None else ( ResolveIntersectionResult._default_params["error_code"] if "error_code" in ResolveIntersectionResult._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of ResolveIntersectionResult.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Errror code associated with a resolve intersections operation.
        """
        args = locals()
        [ResolveIntersectionResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ResolveIntersectionResult.

        Examples
        --------
        >>> ResolveIntersectionResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ResolveIntersectionResult._default_params.items())
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
        """Errror code associated with a resolve intersections operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class SmoothDihedralFaceNodesParams(CoreObject):
    """Parameters to smooth dihedral face nodes. This is for internal use only.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SmoothDihedralFaceNodesParams.

        Parameters
        ----------
        model: Model
            Model to create a SmoothDihedralFaceNodesParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SmoothDihedralFaceNodesParams object with provided parameters.

        Examples
        --------
        >>> smooth_dihedral_face_nodes_params = prime.SmoothDihedralFaceNodesParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SmoothDihedralFaceNodesParams")["SmoothDihedralFaceNodesParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SmoothDihedralFaceNodesParams.

        """
        args = locals()
        [SmoothDihedralFaceNodesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SmoothDihedralFaceNodesParams.

        Examples
        --------
        >>> SmoothDihedralFaceNodesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SmoothDihedralFaceNodesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SmoothDihedralFaceNodesResults(CoreObject):
    """Results structure associated with smooth dihedral face nodes. This is for internal use only.
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SmoothDihedralFaceNodesResults.

        Parameters
        ----------
        model: Model
            Model to create a SmoothDihedralFaceNodesResults object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SmoothDihedralFaceNodesResults object with provided parameters.

        Examples
        --------
        >>> smooth_dihedral_face_nodes_results = prime.SmoothDihedralFaceNodesResults(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SmoothDihedralFaceNodesResults")["SmoothDihedralFaceNodesResults"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SmoothDihedralFaceNodesResults.

        """
        args = locals()
        [SmoothDihedralFaceNodesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SmoothDihedralFaceNodesResults.

        Examples
        --------
        >>> SmoothDihedralFaceNodesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SmoothDihedralFaceNodesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class RefineAtContactsParams(CoreObject):
    """Parameters to refine face elements in contact.
    """
    _default_params = {}

    def __initialize(
            self,
            contact_tolerance: float,
            relative_tolerance: bool,
            refine_max_size: float,
            project_on_geometry: bool):
        self._contact_tolerance = contact_tolerance
        self._relative_tolerance = relative_tolerance
        self._refine_max_size = refine_max_size
        self._project_on_geometry = project_on_geometry

    def __init__(
            self,
            model: CommunicationManager=None,
            contact_tolerance: float = None,
            relative_tolerance: bool = None,
            refine_max_size: float = None,
            project_on_geometry: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RefineAtContactsParams.

        Parameters
        ----------
        model: Model
            Model to create a RefineAtContactsParams object with default parameters.
        contact_tolerance: float, optional
            Maximum tolerance used to identify face elements as contacts.
        relative_tolerance: bool, optional
            Option to specify the contact tolerance is relative or absolute.
        refine_max_size: float, optional
            Maximum size used to refine contact face elements.
        project_on_geometry: bool, optional
            Project on geometry on remesh.
        json_data: dict, optional
            JSON dictionary to create a RefineAtContactsParams object with provided parameters.

        Examples
        --------
        >>> refine_at_contacts_params = prime.RefineAtContactsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["contactTolerance"],
                json_data["relativeTolerance"],
                json_data["refineMaxSize"],
                json_data["projectOnGeometry"])
        else:
            all_field_specified = all(arg is not None for arg in [contact_tolerance, relative_tolerance, refine_max_size, project_on_geometry])
            if all_field_specified:
                self.__initialize(
                    contact_tolerance,
                    relative_tolerance,
                    refine_max_size,
                    project_on_geometry)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "RefineAtContactsParams")["RefineAtContactsParams"]
                    self.__initialize(
                        contact_tolerance if contact_tolerance is not None else ( RefineAtContactsParams._default_params["contact_tolerance"] if "contact_tolerance" in RefineAtContactsParams._default_params else json_data["contactTolerance"]),
                        relative_tolerance if relative_tolerance is not None else ( RefineAtContactsParams._default_params["relative_tolerance"] if "relative_tolerance" in RefineAtContactsParams._default_params else json_data["relativeTolerance"]),
                        refine_max_size if refine_max_size is not None else ( RefineAtContactsParams._default_params["refine_max_size"] if "refine_max_size" in RefineAtContactsParams._default_params else json_data["refineMaxSize"]),
                        project_on_geometry if project_on_geometry is not None else ( RefineAtContactsParams._default_params["project_on_geometry"] if "project_on_geometry" in RefineAtContactsParams._default_params else json_data["projectOnGeometry"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            contact_tolerance: float = None,
            relative_tolerance: bool = None,
            refine_max_size: float = None,
            project_on_geometry: bool = None):
        """Set the default values of RefineAtContactsParams.

        Parameters
        ----------
        contact_tolerance: float, optional
            Maximum tolerance used to identify face elements as contacts.
        relative_tolerance: bool, optional
            Option to specify the contact tolerance is relative or absolute.
        refine_max_size: float, optional
            Maximum size used to refine contact face elements.
        project_on_geometry: bool, optional
            Project on geometry on remesh.
        """
        args = locals()
        [RefineAtContactsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RefineAtContactsParams.

        Examples
        --------
        >>> RefineAtContactsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RefineAtContactsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["contactTolerance"] = self._contact_tolerance
        json_data["relativeTolerance"] = self._relative_tolerance
        json_data["refineMaxSize"] = self._refine_max_size
        json_data["projectOnGeometry"] = self._project_on_geometry
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "contact_tolerance :  %s\nrelative_tolerance :  %s\nrefine_max_size :  %s\nproject_on_geometry :  %s" % (self._contact_tolerance, self._relative_tolerance, self._refine_max_size, self._project_on_geometry)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def contact_tolerance(self) -> float:
        """Maximum tolerance used to identify face elements as contacts.
        """
        return self._contact_tolerance

    @contact_tolerance.setter
    def contact_tolerance(self, value: float):
        self._contact_tolerance = value

    @property
    def relative_tolerance(self) -> bool:
        """Option to specify the contact tolerance is relative or absolute.
        """
        return self._relative_tolerance

    @relative_tolerance.setter
    def relative_tolerance(self, value: bool):
        self._relative_tolerance = value

    @property
    def refine_max_size(self) -> float:
        """Maximum size used to refine contact face elements.
        """
        return self._refine_max_size

    @refine_max_size.setter
    def refine_max_size(self, value: float):
        self._refine_max_size = value

    @property
    def project_on_geometry(self) -> bool:
        """Project on geometry on remesh.
        """
        return self._project_on_geometry

    @project_on_geometry.setter
    def project_on_geometry(self, value: bool):
        self._project_on_geometry = value

class RefineAtContactsResults(CoreObject):
    """Results structure associated with refine face elements in contact.
    """
    _default_params = {}

    def __initialize(
            self,
            n_refined: int,
            size_field_id: int,
            error_code: ErrorCode):
        self._n_refined = n_refined
        self._size_field_id = size_field_id
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_refined: int = None,
            size_field_id: int = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RefineAtContactsResults.

        Parameters
        ----------
        model: Model
            Model to create a RefineAtContactsResults object with default parameters.
        n_refined: int, optional
            Number of face elements identified for refinement.
        size_field_id: int, optional
            Id of size field created to refine at contacts.
        error_code: ErrorCode, optional
            ErrorCode associated with the refine contacts operation.
        json_data: dict, optional
            JSON dictionary to create a RefineAtContactsResults object with provided parameters.

        Examples
        --------
        >>> refine_at_contacts_results = prime.RefineAtContactsResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nRefined"],
                json_data["sizeFieldId"],
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [n_refined, size_field_id, error_code])
            if all_field_specified:
                self.__initialize(
                    n_refined,
                    size_field_id,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "RefineAtContactsResults")["RefineAtContactsResults"]
                    self.__initialize(
                        n_refined if n_refined is not None else ( RefineAtContactsResults._default_params["n_refined"] if "n_refined" in RefineAtContactsResults._default_params else json_data["nRefined"]),
                        size_field_id if size_field_id is not None else ( RefineAtContactsResults._default_params["size_field_id"] if "size_field_id" in RefineAtContactsResults._default_params else json_data["sizeFieldId"]),
                        error_code if error_code is not None else ( RefineAtContactsResults._default_params["error_code"] if "error_code" in RefineAtContactsResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_refined: int = None,
            size_field_id: int = None,
            error_code: ErrorCode = None):
        """Set the default values of RefineAtContactsResults.

        Parameters
        ----------
        n_refined: int, optional
            Number of face elements identified for refinement.
        size_field_id: int, optional
            Id of size field created to refine at contacts.
        error_code: ErrorCode, optional
            ErrorCode associated with the refine contacts operation.
        """
        args = locals()
        [RefineAtContactsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RefineAtContactsResults.

        Examples
        --------
        >>> RefineAtContactsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RefineAtContactsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["nRefined"] = self._n_refined
        json_data["sizeFieldId"] = self._size_field_id
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_refined :  %s\nsize_field_id :  %s\nerror_code :  %s" % (self._n_refined, self._size_field_id, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_refined(self) -> int:
        """Number of face elements identified for refinement.
        """
        return self._n_refined

    @n_refined.setter
    def n_refined(self, value: int):
        self._n_refined = value

    @property
    def size_field_id(self) -> int:
        """Id of size field created to refine at contacts.
        """
        return self._size_field_id

    @size_field_id.setter
    def size_field_id(self, value: int):
        self._size_field_id = value

    @property
    def error_code(self) -> ErrorCode:
        """ErrorCode associated with the refine contacts operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class AddThicknessParams(CoreObject):
    """Parameters to add thickness for a given plane.
    """
    _default_params = {}

    def __initialize(
            self,
            thickness: float,
            reverse_face_normal: bool,
            suggested_part_name: str,
            fix_intersections: bool):
        self._thickness = thickness
        self._reverse_face_normal = reverse_face_normal
        self._suggested_part_name = suggested_part_name
        self._fix_intersections = fix_intersections

    def __init__(
            self,
            model: CommunicationManager=None,
            thickness: float = None,
            reverse_face_normal: bool = None,
            suggested_part_name: str = None,
            fix_intersections: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AddThicknessParams.

        Parameters
        ----------
        model: Model
            Model to create a AddThicknessParams object with default parameters.
        thickness: float, optional
            To assign the offset distance of inflation.
        reverse_face_normal: bool, optional
            To assign the direction of inflation.
        suggested_part_name: str, optional
            Suggested part name for created patching surfaces.
        fix_intersections: bool, optional
            Fix intersections in concave regions.
        json_data: dict, optional
            JSON dictionary to create a AddThicknessParams object with provided parameters.

        Examples
        --------
        >>> add_thickness_params = prime.AddThicknessParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["thickness"],
                json_data["reverseFaceNormal"],
                json_data["suggestedPartName"],
                json_data["fixIntersections"])
        else:
            all_field_specified = all(arg is not None for arg in [thickness, reverse_face_normal, suggested_part_name, fix_intersections])
            if all_field_specified:
                self.__initialize(
                    thickness,
                    reverse_face_normal,
                    suggested_part_name,
                    fix_intersections)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "AddThicknessParams")["AddThicknessParams"]
                    self.__initialize(
                        thickness if thickness is not None else ( AddThicknessParams._default_params["thickness"] if "thickness" in AddThicknessParams._default_params else json_data["thickness"]),
                        reverse_face_normal if reverse_face_normal is not None else ( AddThicknessParams._default_params["reverse_face_normal"] if "reverse_face_normal" in AddThicknessParams._default_params else json_data["reverseFaceNormal"]),
                        suggested_part_name if suggested_part_name is not None else ( AddThicknessParams._default_params["suggested_part_name"] if "suggested_part_name" in AddThicknessParams._default_params else json_data["suggestedPartName"]),
                        fix_intersections if fix_intersections is not None else ( AddThicknessParams._default_params["fix_intersections"] if "fix_intersections" in AddThicknessParams._default_params else json_data["fixIntersections"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            thickness: float = None,
            reverse_face_normal: bool = None,
            suggested_part_name: str = None,
            fix_intersections: bool = None):
        """Set the default values of AddThicknessParams.

        Parameters
        ----------
        thickness: float, optional
            To assign the offset distance of inflation.
        reverse_face_normal: bool, optional
            To assign the direction of inflation.
        suggested_part_name: str, optional
            Suggested part name for created patching surfaces.
        fix_intersections: bool, optional
            Fix intersections in concave regions.
        """
        args = locals()
        [AddThicknessParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AddThicknessParams.

        Examples
        --------
        >>> AddThicknessParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AddThicknessParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["thickness"] = self._thickness
        json_data["reverseFaceNormal"] = self._reverse_face_normal
        json_data["suggestedPartName"] = self._suggested_part_name
        json_data["fixIntersections"] = self._fix_intersections
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "thickness :  %s\nreverse_face_normal :  %s\nsuggested_part_name :  %s\nfix_intersections :  %s" % (self._thickness, self._reverse_face_normal, self._suggested_part_name, self._fix_intersections)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def thickness(self) -> float:
        """To assign the offset distance of inflation.
        """
        return self._thickness

    @thickness.setter
    def thickness(self, value: float):
        self._thickness = value

    @property
    def reverse_face_normal(self) -> bool:
        """To assign the direction of inflation.
        """
        return self._reverse_face_normal

    @reverse_face_normal.setter
    def reverse_face_normal(self, value: bool):
        self._reverse_face_normal = value

    @property
    def suggested_part_name(self) -> str:
        """Suggested part name for created patching surfaces.
        """
        return self._suggested_part_name

    @suggested_part_name.setter
    def suggested_part_name(self, value: str):
        self._suggested_part_name = value

    @property
    def fix_intersections(self) -> bool:
        """Fix intersections in concave regions.
        """
        return self._fix_intersections

    @fix_intersections.setter
    def fix_intersections(self, value: bool):
        self._fix_intersections = value

class AddThicknessResults(CoreObject):
    """Result structure associated with add thickness zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            part_id: int):
        self._error_code = ErrorCode(error_code)
        self._part_id = part_id

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            part_id: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AddThicknessResults.

        Parameters
        ----------
        model: Model
            Model to create a AddThicknessResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        part_id: int, optional
            The created thickness part id.
        json_data: dict, optional
            JSON dictionary to create a AddThicknessResults object with provided parameters.

        Examples
        --------
        >>> add_thickness_results = prime.AddThicknessResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["partId"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, part_id])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    part_id)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "AddThicknessResults")["AddThicknessResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( AddThicknessResults._default_params["error_code"] if "error_code" in AddThicknessResults._default_params else ErrorCode(json_data["errorCode"])),
                        part_id if part_id is not None else ( AddThicknessResults._default_params["part_id"] if "part_id" in AddThicknessResults._default_params else json_data["partId"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            part_id: int = None):
        """Set the default values of AddThicknessResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        part_id: int, optional
            The created thickness part id.
        """
        args = locals()
        [AddThicknessResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AddThicknessResults.

        Examples
        --------
        >>> AddThicknessResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AddThicknessResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["partId"] = self._part_id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\npart_id :  %s" % (self._error_code, self._part_id)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def part_id(self) -> int:
        """The created thickness part id.
        """
        return self._part_id

    @part_id.setter
    def part_id(self, value: int):
        self._part_id = value
