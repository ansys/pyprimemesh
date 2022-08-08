""" Auto-generated file. DO NOT MODIFY """
# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
import enum
from typing import Dict, Any, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

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

class SubtractZoneletsParams(CoreObject):
    """Parameters to use when subtracting zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            retain_cutter: bool,
            extract_edges: bool,
            trace_edges: bool):
        self._retain_cutter = retain_cutter
        self._extract_edges = extract_edges
        self._trace_edges = trace_edges

    def __init__(
            self,
            model: CommunicationManager=None,
            retain_cutter: bool = None,
            extract_edges: bool = None,
            trace_edges: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SubtractZoneletsParams.

        Parameters
        ----------
        model: Model
            Model to create a SubtractZoneletsParams object with default parameters.
        retain_cutter: bool, optional
            Retain the zonelets used for removal.
        extract_edges: bool, optional
            Extract edges of intersection during subtract.
        trace_edges: bool, optional
            Trace edges of intersection on target. Only works if extractEdges is true.
        json_data: dict, optional
            JSON dictionary to create a SubtractZoneletsParams object with provided parameters.

        Examples
        --------
        >>> subtract_zonelets_params = prime.SubtractZoneletsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["retainCutter"],
                json_data["extractEdges"],
                json_data["traceEdges"])
        else:
            all_field_specified = all(arg is not None for arg in [retain_cutter, extract_edges, trace_edges])
            if all_field_specified:
                self.__initialize(
                    retain_cutter,
                    extract_edges,
                    trace_edges)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SubtractZoneletsParams")["SubtractZoneletsParams"]
                    self.__initialize(
                        retain_cutter if retain_cutter is not None else ( SubtractZoneletsParams._default_params["retain_cutter"] if "retain_cutter" in SubtractZoneletsParams._default_params else json_data["retainCutter"]),
                        extract_edges if extract_edges is not None else ( SubtractZoneletsParams._default_params["extract_edges"] if "extract_edges" in SubtractZoneletsParams._default_params else json_data["extractEdges"]),
                        trace_edges if trace_edges is not None else ( SubtractZoneletsParams._default_params["trace_edges"] if "trace_edges" in SubtractZoneletsParams._default_params else json_data["traceEdges"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            retain_cutter: bool = None,
            extract_edges: bool = None,
            trace_edges: bool = None):
        """Set the default values of SubtractZoneletsParams.

        Parameters
        ----------
        retain_cutter: bool, optional
            Retain the zonelets used for removal.
        extract_edges: bool, optional
            Extract edges of intersection during subtract.
        trace_edges: bool, optional
            Trace edges of intersection on target. Only works if extractEdges is true.
        """
        args = locals()
        [SubtractZoneletsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SubtractZoneletsParams.

        Examples
        --------
        >>> SubtractZoneletsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SubtractZoneletsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["retainCutter"] = self._retain_cutter
        json_data["extractEdges"] = self._extract_edges
        json_data["traceEdges"] = self._trace_edges
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "retain_cutter :  %s\nextract_edges :  %s\ntrace_edges :  %s" % (self._retain_cutter, self._extract_edges, self._trace_edges)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def retain_cutter(self) -> bool:
        """Retain the zonelets used for removal.
        """
        return self._retain_cutter

    @retain_cutter.setter
    def retain_cutter(self, value: bool):
        self._retain_cutter = value

    @property
    def extract_edges(self) -> bool:
        """Extract edges of intersection during subtract.
        """
        return self._extract_edges

    @extract_edges.setter
    def extract_edges(self, value: bool):
        self._extract_edges = value

    @property
    def trace_edges(self) -> bool:
        """Trace edges of intersection on target. Only works if extractEdges is true.
        """
        return self._trace_edges

    @trace_edges.setter
    def trace_edges(self, value: bool):
        self._trace_edges = value

class SubtractZoneletsResults(CoreObject):
    """Results structure associated with subtracting zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            processing_time: float,
            error_code: ErrorCode):
        self._processing_time = processing_time
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            processing_time: float = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SubtractZoneletsResults.

        Parameters
        ----------
        model: Model
            Model to create a SubtractZoneletsResults object with default parameters.
        processing_time: float, optional
            Processing time for subtract operation.
        error_code: ErrorCode, optional
            Error Code associated with subtract operation.
        json_data: dict, optional
            JSON dictionary to create a SubtractZoneletsResults object with provided parameters.

        Examples
        --------
        >>> subtract_zonelets_results = prime.SubtractZoneletsResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["processingTime"],
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [processing_time, error_code])
            if all_field_specified:
                self.__initialize(
                    processing_time,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SubtractZoneletsResults")["SubtractZoneletsResults"]
                    self.__initialize(
                        processing_time if processing_time is not None else ( SubtractZoneletsResults._default_params["processing_time"] if "processing_time" in SubtractZoneletsResults._default_params else json_data["processingTime"]),
                        error_code if error_code is not None else ( SubtractZoneletsResults._default_params["error_code"] if "error_code" in SubtractZoneletsResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            processing_time: float = None,
            error_code: ErrorCode = None):
        """Set the default values of SubtractZoneletsResults.

        Parameters
        ----------
        processing_time: float, optional
            Processing time for subtract operation.
        error_code: ErrorCode, optional
            Error Code associated with subtract operation.
        """
        args = locals()
        [SubtractZoneletsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SubtractZoneletsResults.

        Examples
        --------
        >>> SubtractZoneletsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SubtractZoneletsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["processingTime"] = self._processing_time
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "processing_time :  %s\nerror_code :  %s" % (self._processing_time, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def processing_time(self) -> float:
        """Processing time for subtract operation.
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, value: float):
        self._processing_time = value

    @property
    def error_code(self) -> ErrorCode:
        """Error Code associated with subtract operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
