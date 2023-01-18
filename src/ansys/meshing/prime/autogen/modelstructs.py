""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class MergePartsParams(CoreObject):
    """Parameters to merge parts.
    """
    _default_params = {}

    def __initialize(
            self,
            merged_part_suggested_name: str):
        self._merged_part_suggested_name = merged_part_suggested_name

    def __init__(
            self,
            model: CommunicationManager=None,
            merged_part_suggested_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergePartsParams.

        Parameters
        ----------
        model: Model
            Model to create a MergePartsParams object with default parameters.
        merged_part_suggested_name: str, optional
            Suggested name to be set on merged part. First in alphabetical order of given part names will be used, when empty name is given.
        json_data: dict, optional
            JSON dictionary to create a MergePartsParams object with provided parameters.

        Examples
        --------
        >>> merge_parts_params = prime.MergePartsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["mergedPartSuggestedName"] if "mergedPartSuggestedName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [merged_part_suggested_name])
            if all_field_specified:
                self.__initialize(
                    merged_part_suggested_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergePartsParams")
                    json_data = param_json["MergePartsParams"] if "MergePartsParams" in param_json else {}
                    self.__initialize(
                        merged_part_suggested_name if merged_part_suggested_name is not None else ( MergePartsParams._default_params["merged_part_suggested_name"] if "merged_part_suggested_name" in MergePartsParams._default_params else (json_data["mergedPartSuggestedName"] if "mergedPartSuggestedName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            merged_part_suggested_name: str = None):
        """Set the default values of MergePartsParams.

        Parameters
        ----------
        merged_part_suggested_name: str, optional
            Suggested name to be set on merged part. First in alphabetical order of given part names will be used, when empty name is given.
        """
        args = locals()
        [MergePartsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergePartsParams.

        Examples
        --------
        >>> MergePartsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergePartsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._merged_part_suggested_name is not None:
            json_data["mergedPartSuggestedName"] = self._merged_part_suggested_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "merged_part_suggested_name :  %s" % (self._merged_part_suggested_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def merged_part_suggested_name(self) -> str:
        """Suggested name to be set on merged part. First in alphabetical order of given part names will be used, when empty name is given.
        """
        return self._merged_part_suggested_name

    @merged_part_suggested_name.setter
    def merged_part_suggested_name(self, value: str):
        self._merged_part_suggested_name = value

class MergePartsResults(CoreObject):
    """Parameters to merge parts.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            merged_part_assigned_name: str,
            merged_part_id: int):
        self._error_code = ErrorCode(error_code)
        self._merged_part_assigned_name = merged_part_assigned_name
        self._merged_part_id = merged_part_id

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            merged_part_assigned_name: str = None,
            merged_part_id: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergePartsResults.

        Parameters
        ----------
        model: Model
            Model to create a MergePartsResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        merged_part_assigned_name: str, optional
            Name assigned to merged part. Suffix is added to suggested name if the name not available.
        merged_part_id: int, optional
            Id assigned to merged part.
        json_data: dict, optional
            JSON dictionary to create a MergePartsResults object with provided parameters.

        Examples
        --------
        >>> merge_parts_results = prime.MergePartsResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["mergedPartAssignedName"] if "mergedPartAssignedName" in json_data else None,
                json_data["mergedPartId"] if "mergedPartId" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, merged_part_assigned_name, merged_part_id])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    merged_part_assigned_name,
                    merged_part_id)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergePartsResults")
                    json_data = param_json["MergePartsResults"] if "MergePartsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( MergePartsResults._default_params["error_code"] if "error_code" in MergePartsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        merged_part_assigned_name if merged_part_assigned_name is not None else ( MergePartsResults._default_params["merged_part_assigned_name"] if "merged_part_assigned_name" in MergePartsResults._default_params else (json_data["mergedPartAssignedName"] if "mergedPartAssignedName" in json_data else None)),
                        merged_part_id if merged_part_id is not None else ( MergePartsResults._default_params["merged_part_id"] if "merged_part_id" in MergePartsResults._default_params else (json_data["mergedPartId"] if "mergedPartId" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            merged_part_assigned_name: str = None,
            merged_part_id: int = None):
        """Set the default values of MergePartsResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        merged_part_assigned_name: str, optional
            Name assigned to merged part. Suffix is added to suggested name if the name not available.
        merged_part_id: int, optional
            Id assigned to merged part.
        """
        args = locals()
        [MergePartsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergePartsResults.

        Examples
        --------
        >>> MergePartsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergePartsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._merged_part_assigned_name is not None:
            json_data["mergedPartAssignedName"] = self._merged_part_assigned_name
        if self._merged_part_id is not None:
            json_data["mergedPartId"] = self._merged_part_id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nmerged_part_assigned_name :  %s\nmerged_part_id :  %s" % (self._error_code, self._merged_part_assigned_name, self._merged_part_id)
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
    def merged_part_assigned_name(self) -> str:
        """Name assigned to merged part. Suffix is added to suggested name if the name not available.
        """
        return self._merged_part_assigned_name

    @merged_part_assigned_name.setter
    def merged_part_assigned_name(self, value: str):
        self._merged_part_assigned_name = value

    @property
    def merged_part_id(self) -> int:
        """Id assigned to merged part.
        """
        return self._merged_part_id

    @merged_part_id.setter
    def merged_part_id(self, value: int):
        self._merged_part_id = value

class GlobalSizingParams(CoreObject):
    """Global sizing parameters.
    """
    _default_params = {}

    def __initialize(
            self,
            min: float,
            max: float,
            growth_rate: float):
        self._min = min
        self._max = max
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            min: float = None,
            max: float = None,
            growth_rate: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the GlobalSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a GlobalSizingParams object with default parameters.
        min: float, optional
            Minimum value of global sizing parameters.
        max: float, optional
            Maximum value of global sizing parameters.
        growth_rate: float, optional
            Growth rate of global sizing parameters.
        json_data: dict, optional
            JSON dictionary to create a GlobalSizingParams object with provided parameters.

        Examples
        --------
        >>> global_sizing_params = prime.GlobalSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["min"] if "min" in json_data else None,
                json_data["max"] if "max" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [min, max, growth_rate])
            if all_field_specified:
                self.__initialize(
                    min,
                    max,
                    growth_rate)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "GlobalSizingParams")
                    json_data = param_json["GlobalSizingParams"] if "GlobalSizingParams" in param_json else {}
                    self.__initialize(
                        min if min is not None else ( GlobalSizingParams._default_params["min"] if "min" in GlobalSizingParams._default_params else (json_data["min"] if "min" in json_data else None)),
                        max if max is not None else ( GlobalSizingParams._default_params["max"] if "max" in GlobalSizingParams._default_params else (json_data["max"] if "max" in json_data else None)),
                        growth_rate if growth_rate is not None else ( GlobalSizingParams._default_params["growth_rate"] if "growth_rate" in GlobalSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min: float = None,
            max: float = None,
            growth_rate: float = None):
        """Set the default values of GlobalSizingParams.

        Parameters
        ----------
        min: float, optional
            Minimum value of global sizing parameters.
        max: float, optional
            Maximum value of global sizing parameters.
        growth_rate: float, optional
            Growth rate of global sizing parameters.
        """
        args = locals()
        [GlobalSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of GlobalSizingParams.

        Examples
        --------
        >>> GlobalSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in GlobalSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._min is not None:
            json_data["min"] = self._min
        if self._max is not None:
            json_data["max"] = self._max
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min :  %s\nmax :  %s\ngrowth_rate :  %s" % (self._min, self._max, self._growth_rate)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min(self) -> float:
        """Minimum value of global sizing parameters.
        """
        return self._min

    @min.setter
    def min(self, value: float):
        self._min = value

    @property
    def max(self) -> float:
        """Maximum value of global sizing parameters.
        """
        return self._max

    @max.setter
    def max(self, value: float):
        self._max = value

    @property
    def growth_rate(self) -> float:
        """Growth rate of global sizing parameters.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

class CreateZoneResults(CoreObject):
    """Results associated with the create zone.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            zone_id: int,
            assigned_name: str):
        self._error_code = ErrorCode(error_code)
        self._zone_id = zone_id
        self._assigned_name = assigned_name

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            zone_id: int = None,
            assigned_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateZoneResults.

        Parameters
        ----------
        model: Model
            Model to create a CreateZoneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the create zone operation.
        zone_id: int, optional
            Id of newly created zone.
        assigned_name: str, optional
            Assigned name of newly created zone.
        json_data: dict, optional
            JSON dictionary to create a CreateZoneResults object with provided parameters.

        Examples
        --------
        >>> create_zone_results = prime.CreateZoneResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["zoneID"] if "zoneID" in json_data else None,
                json_data["assignedName"] if "assignedName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, zone_id, assigned_name])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    zone_id,
                    assigned_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CreateZoneResults")
                    json_data = param_json["CreateZoneResults"] if "CreateZoneResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CreateZoneResults._default_params["error_code"] if "error_code" in CreateZoneResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        zone_id if zone_id is not None else ( CreateZoneResults._default_params["zone_id"] if "zone_id" in CreateZoneResults._default_params else (json_data["zoneID"] if "zoneID" in json_data else None)),
                        assigned_name if assigned_name is not None else ( CreateZoneResults._default_params["assigned_name"] if "assigned_name" in CreateZoneResults._default_params else (json_data["assignedName"] if "assignedName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            zone_id: int = None,
            assigned_name: str = None):
        """Set the default values of CreateZoneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the create zone operation.
        zone_id: int, optional
            Id of newly created zone.
        assigned_name: str, optional
            Assigned name of newly created zone.
        """
        args = locals()
        [CreateZoneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateZoneResults.

        Examples
        --------
        >>> CreateZoneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateZoneResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._zone_id is not None:
            json_data["zoneID"] = self._zone_id
        if self._assigned_name is not None:
            json_data["assignedName"] = self._assigned_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nzone_id :  %s\nassigned_name :  %s" % (self._error_code, self._zone_id, self._assigned_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the create zone operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def zone_id(self) -> int:
        """Id of newly created zone.
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, value: int):
        self._zone_id = value

    @property
    def assigned_name(self) -> str:
        """Assigned name of newly created zone.
        """
        return self._assigned_name

    @assigned_name.setter
    def assigned_name(self, value: str):
        self._assigned_name = value

class DeleteZoneResults(CoreObject):
    """Results associated with the delete zone.
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
        """Initializes the DeleteZoneResults.

        Parameters
        ----------
        model: Model
            Model to create a DeleteZoneResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the delete zone operation.
        json_data: dict, optional
            JSON dictionary to create a DeleteZoneResults object with provided parameters.

        Examples
        --------
        >>> delete_zone_results = prime.DeleteZoneResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "DeleteZoneResults")
                    json_data = param_json["DeleteZoneResults"] if "DeleteZoneResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteZoneResults._default_params["error_code"] if "error_code" in DeleteZoneResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of DeleteZoneResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the delete zone operation.
        """
        args = locals()
        [DeleteZoneResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteZoneResults.

        Examples
        --------
        >>> DeleteZoneResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteZoneResults._default_params.items())
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
        """Error code associated with the delete zone operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
