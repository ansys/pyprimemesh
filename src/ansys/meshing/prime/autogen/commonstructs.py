# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class ScopeEntity(enum.IntEnum):
    """ScopeDefinition uses entity type to scope entities.
    """
    FACEZONELETS = 1
    """Evaluate scope to get the face zonelets."""
    EDGEZONELETS = 2
    """Evaluate scope to get the edge zonelets."""
    FACEANDEDGEZONELETS = 3
    """Evaluate scope to get face and edge zonelets."""
    VOLUME = 6
    """Evaluate scope to get volumes."""

class ScopeEvaluationType(enum.IntEnum):
    """ScopeDefinition uses evaluation type to evaluate the scope.
    """
    LABELS = 3
    """Use labels to evaluate the scope."""
    ZONES = 4
    """Use zones to evaluate the scope."""

class ScopeExpressionType(enum.IntEnum):
    """ScopeExpressionType uses expression type to evaluate the scope.
    """
    NAMEPATTERN = 2
    """Use name pattern expression to evaluate scope."""

class PartZonelets(CoreObject):
    """A structure containing some or all face zonelet ids available in a part.

    Parameters
    ----------
    model : Model
        Model to create a ``PartZonelets`` object with default parameters.
    part_id : int, optional
        Id of part.
    face_zonelets : Iterable[int], optional
        List of face zonelet ids available in the part.
    json_data : dict, optional
        JSON dictionary to create a ``PartZonelets`` object with provided parameters.

    Examples
    --------
    >>> part_zonelets = prime.PartZonelets(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            part_id : int,
            face_zonelets : Iterable[int]):
        self._part_id = part_id
        self._face_zonelets = face_zonelets if isinstance(face_zonelets, np.ndarray) else np.array(face_zonelets, dtype=np.int32) if face_zonelets is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            part_id : int = None,
            face_zonelets : Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``PartZonelets`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``PartZonelets`` object with default parameters.
        part_id : int, optional
            Id of part.
        face_zonelets : Iterable[int], optional
            List of face zonelet ids available in the part.
        json_data : dict, optional
            JSON dictionary to create a ``PartZonelets`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "PartZonelets")
                    json_data = param_json["PartZonelets"] if "PartZonelets" in param_json else {}
                    self.__initialize(
                        part_id if part_id is not None else ( PartZonelets._default_params["part_id"] if "part_id" in PartZonelets._default_params else (json_data["partID"] if "partID" in json_data else None)),
                        face_zonelets if face_zonelets is not None else ( PartZonelets._default_params["face_zonelets"] if "face_zonelets" in PartZonelets._default_params else (json_data["faceZonelets"] if "faceZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            part_id : int = None,
            face_zonelets : Iterable[int] = None):
        """Set the default values of the ``PartZonelets`` object.

        Parameters
        ----------
        part_id : int, optional
            Id of part.
        face_zonelets : Iterable[int], optional
            List of face zonelet ids available in the part.
        """
        args = locals()
        [PartZonelets._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``PartZonelets`` object.

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

    Parameters
    ----------
    model : Model
        Model to create a ``SetNameResults`` object with default parameters.
    warning_code : WarningCode, optional
        Warning code associated with the set name of given entity.
    assigned_name : str, optional
        Assigned name of given entity.
    error_code : ErrorCode, optional
        Error code associated with the failure of operation.
    json_data : dict, optional
        JSON dictionary to create a ``SetNameResults`` object with provided parameters.

    Examples
    --------
    >>> set_name_results = prime.SetNameResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            warning_code : WarningCode,
            assigned_name : str,
            error_code : ErrorCode):
        self._warning_code = WarningCode(warning_code)
        self._assigned_name = assigned_name
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            warning_code : WarningCode = None,
            assigned_name : str = None,
            error_code : ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetNameResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetNameResults`` object with default parameters.
        warning_code : WarningCode, optional
            Warning code associated with the set name of given entity.
        assigned_name : str, optional
            Assigned name of given entity.
        error_code : ErrorCode, optional
            Error code associated with the failure of operation.
        json_data : dict, optional
            JSON dictionary to create a ``SetNameResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetNameResults")
                    json_data = param_json["SetNameResults"] if "SetNameResults" in param_json else {}
                    self.__initialize(
                        warning_code if warning_code is not None else ( SetNameResults._default_params["warning_code"] if "warning_code" in SetNameResults._default_params else WarningCode(json_data["warningCode"] if "warningCode" in json_data else None)),
                        assigned_name if assigned_name is not None else ( SetNameResults._default_params["assigned_name"] if "assigned_name" in SetNameResults._default_params else (json_data["assignedName"] if "assignedName" in json_data else None)),
                        error_code if error_code is not None else ( SetNameResults._default_params["error_code"] if "error_code" in SetNameResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            warning_code : WarningCode = None,
            assigned_name : str = None,
            error_code : ErrorCode = None):
        """Set the default values of the ``SetNameResults`` object.

        Parameters
        ----------
        warning_code : WarningCode, optional
            Warning code associated with the set name of given entity.
        assigned_name : str, optional
            Assigned name of given entity.
        error_code : ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [SetNameResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetNameResults`` object.

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

    Parameters
    ----------
    model : Model
        Model to create a ``DeleteResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with the failure of operation.
    json_data : dict, optional
        JSON dictionary to create a ``DeleteResults`` object with provided parameters.

    Examples
    --------
    >>> delete_results = prime.DeleteResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DeleteResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``DeleteResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with the failure of operation.
        json_data : dict, optional
            JSON dictionary to create a ``DeleteResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteResults")
                    json_data = param_json["DeleteResults"] if "DeleteResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteResults._default_params["error_code"] if "error_code" in DeleteResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None):
        """Set the default values of the ``DeleteResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [DeleteResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DeleteResults`` object.

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

class CopyZoneletsParams(CoreObject):
    """Parameters to copy zonelets.

    Parameters
    ----------
    model : Model
        Model to create a ``CopyZoneletsParams`` object with default parameters.
    copy_labels : bool, optional
        Option to copy labels of input zonelets to the corresponding copied zonelets.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    copy_zones : bool, optional
        Option to copy zones of input zonelets to corresponding copied zonelets.
    json_data : dict, optional
        JSON dictionary to create a ``CopyZoneletsParams`` object with provided parameters.

    Examples
    --------
    >>> copy_zonelets_params = prime.CopyZoneletsParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            copy_labels : bool,
            copy_zones : bool):
        self._copy_labels = copy_labels
        self._copy_zones = copy_zones

    def __init__(
            self,
            model: CommunicationManager=None,
            copy_labels : bool = None,
            copy_zones : bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``CopyZoneletsParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``CopyZoneletsParams`` object with default parameters.
        copy_labels : bool, optional
            Option to copy labels of input zonelets to the corresponding copied zonelets.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        copy_zones : bool, optional
            Option to copy zones of input zonelets to corresponding copied zonelets.
        json_data : dict, optional
            JSON dictionary to create a ``CopyZoneletsParams`` object with provided parameters.

        Examples
        --------
        >>> copy_zonelets_params = prime.CopyZoneletsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["copyLabels"] if "copyLabels" in json_data else None,
                json_data["copyZones"] if "copyZones" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [copy_labels, copy_zones])
            if all_field_specified:
                self.__initialize(
                    copy_labels,
                    copy_zones)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "CopyZoneletsParams")
                    json_data = param_json["CopyZoneletsParams"] if "CopyZoneletsParams" in param_json else {}
                    self.__initialize(
                        copy_labels if copy_labels is not None else ( CopyZoneletsParams._default_params["copy_labels"] if "copy_labels" in CopyZoneletsParams._default_params else (json_data["copyLabels"] if "copyLabels" in json_data else None)),
                        copy_zones if copy_zones is not None else ( CopyZoneletsParams._default_params["copy_zones"] if "copy_zones" in CopyZoneletsParams._default_params else (json_data["copyZones"] if "copyZones" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            copy_labels : bool = None,
            copy_zones : bool = None):
        """Set the default values of the ``CopyZoneletsParams`` object.

        Parameters
        ----------
        copy_labels : bool, optional
            Option to copy labels of input zonelets to the corresponding copied zonelets.
        copy_zones : bool, optional
            Option to copy zones of input zonelets to corresponding copied zonelets.
        """
        args = locals()
        [CopyZoneletsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``CopyZoneletsParams`` object.

        Examples
        --------
        >>> CopyZoneletsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CopyZoneletsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._copy_labels is not None:
            json_data["copyLabels"] = self._copy_labels
        if self._copy_zones is not None:
            json_data["copyZones"] = self._copy_zones
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "copy_labels :  %s\ncopy_zones :  %s" % (self._copy_labels, self._copy_zones)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def copy_labels(self) -> bool:
        """Option to copy labels of input zonelets to the corresponding copied zonelets.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._copy_labels

    @copy_labels.setter
    def copy_labels(self, value: bool):
        self._copy_labels = value

    @property
    def copy_zones(self) -> bool:
        """Option to copy zones of input zonelets to corresponding copied zonelets.
        """
        return self._copy_zones

    @copy_zones.setter
    def copy_zones(self, value: bool):
        self._copy_zones = value

class CopyZoneletsResults(CoreObject):
    """Result structure associated with copying zonelets.

    Parameters
    ----------
    model : Model
        Model to create a ``CopyZoneletsResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with failure of operation.
    copied_zonelets : Iterable[int], optional
        Ids of the copied zonelets.
    copied_face_zonelets : Iterable[int], optional
        Ids of the copied bounding faces of cell zonelets.
    json_data : dict, optional
        JSON dictionary to create a ``CopyZoneletsResults`` object with provided parameters.

    Examples
    --------
    >>> copy_zonelets_results = prime.CopyZoneletsResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode,
            copied_zonelets : Iterable[int],
            copied_face_zonelets : Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._copied_zonelets = copied_zonelets if isinstance(copied_zonelets, np.ndarray) else np.array(copied_zonelets, dtype=np.int32) if copied_zonelets is not None else None
        self._copied_face_zonelets = copied_face_zonelets if isinstance(copied_face_zonelets, np.ndarray) else np.array(copied_face_zonelets, dtype=np.int32) if copied_face_zonelets is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            copied_zonelets : Iterable[int] = None,
            copied_face_zonelets : Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``CopyZoneletsResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``CopyZoneletsResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with failure of operation.
        copied_zonelets : Iterable[int], optional
            Ids of the copied zonelets.
        copied_face_zonelets : Iterable[int], optional
            Ids of the copied bounding faces of cell zonelets.
        json_data : dict, optional
            JSON dictionary to create a ``CopyZoneletsResults`` object with provided parameters.

        Examples
        --------
        >>> copy_zonelets_results = prime.CopyZoneletsResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["copiedZonelets"] if "copiedZonelets" in json_data else None,
                json_data["copiedFaceZonelets"] if "copiedFaceZonelets" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, copied_zonelets, copied_face_zonelets])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    copied_zonelets,
                    copied_face_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "CopyZoneletsResults")
                    json_data = param_json["CopyZoneletsResults"] if "CopyZoneletsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CopyZoneletsResults._default_params["error_code"] if "error_code" in CopyZoneletsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        copied_zonelets if copied_zonelets is not None else ( CopyZoneletsResults._default_params["copied_zonelets"] if "copied_zonelets" in CopyZoneletsResults._default_params else (json_data["copiedZonelets"] if "copiedZonelets" in json_data else None)),
                        copied_face_zonelets if copied_face_zonelets is not None else ( CopyZoneletsResults._default_params["copied_face_zonelets"] if "copied_face_zonelets" in CopyZoneletsResults._default_params else (json_data["copiedFaceZonelets"] if "copiedFaceZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None,
            copied_zonelets : Iterable[int] = None,
            copied_face_zonelets : Iterable[int] = None):
        """Set the default values of the ``CopyZoneletsResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with failure of operation.
        copied_zonelets : Iterable[int], optional
            Ids of the copied zonelets.
        copied_face_zonelets : Iterable[int], optional
            Ids of the copied bounding faces of cell zonelets.
        """
        args = locals()
        [CopyZoneletsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``CopyZoneletsResults`` object.

        Examples
        --------
        >>> CopyZoneletsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CopyZoneletsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._copied_zonelets is not None:
            json_data["copiedZonelets"] = self._copied_zonelets
        if self._copied_face_zonelets is not None:
            json_data["copiedFaceZonelets"] = self._copied_face_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\ncopied_zonelets :  %s\ncopied_face_zonelets :  %s" % (self._error_code, self._copied_zonelets, self._copied_face_zonelets)
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
        """Ids of the copied zonelets.
        """
        return self._copied_zonelets

    @copied_zonelets.setter
    def copied_zonelets(self, value: Iterable[int]):
        self._copied_zonelets = value

    @property
    def copied_face_zonelets(self) -> Iterable[int]:
        """Ids of the copied bounding faces of cell zonelets.
        """
        return self._copied_face_zonelets

    @copied_face_zonelets.setter
    def copied_face_zonelets(self, value: Iterable[int]):
        self._copied_face_zonelets = value

class ScopeDefinition(CoreObject):
    """ScopeDefinition to scope entities based on entity and evaluation type.

    Parameters
    ----------
    model : Model
        Model to create a ``ScopeDefinition`` object with default parameters.
    entity_type : ScopeEntity, optional
        Entity type for which scope needs to be evaluated. The default is set to face zonelets.
    evaluation_type : ScopeEvaluationType, optional
        Evaluation type to scope entities. The default is set to labels.
    part_expression : str, optional
        Part expression to scope parts while evaluating scope.
    label_expression : str, optional
        Label expression to scope entities when evaluation type is set to labels.
    zone_expression : str, optional
        Zone expression to scope entities when evaluation type is set to zones.
    json_data : dict, optional
        JSON dictionary to create a ``ScopeDefinition`` object with provided parameters.

    Examples
    --------
    >>> scope_definition = prime.ScopeDefinition(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            entity_type : ScopeEntity,
            evaluation_type : ScopeEvaluationType,
            part_expression : str,
            label_expression : str,
            zone_expression : str):
        self._entity_type = ScopeEntity(entity_type)
        self._evaluation_type = ScopeEvaluationType(evaluation_type)
        self._part_expression = part_expression
        self._label_expression = label_expression
        self._zone_expression = zone_expression

    def __init__(
            self,
            model: CommunicationManager=None,
            entity_type : ScopeEntity = None,
            evaluation_type : ScopeEvaluationType = None,
            part_expression : str = None,
            label_expression : str = None,
            zone_expression : str = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ScopeDefinition`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``ScopeDefinition`` object with default parameters.
        entity_type : ScopeEntity, optional
            Entity type for which scope needs to be evaluated. The default is set to face zonelets.
        evaluation_type : ScopeEvaluationType, optional
            Evaluation type to scope entities. The default is set to labels.
        part_expression : str, optional
            Part expression to scope parts while evaluating scope.
        label_expression : str, optional
            Label expression to scope entities when evaluation type is set to labels.
        zone_expression : str, optional
            Zone expression to scope entities when evaluation type is set to zones.
        json_data : dict, optional
            JSON dictionary to create a ``ScopeDefinition`` object with provided parameters.

        Examples
        --------
        >>> scope_definition = prime.ScopeDefinition(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeEntity(json_data["entityType"] if "entityType" in json_data else None),
                ScopeEvaluationType(json_data["evaluationType"] if "evaluationType" in json_data else None),
                json_data["partExpression"] if "partExpression" in json_data else None,
                json_data["labelExpression"] if "labelExpression" in json_data else None,
                json_data["zoneExpression"] if "zoneExpression" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [entity_type, evaluation_type, part_expression, label_expression, zone_expression])
            if all_field_specified:
                self.__initialize(
                    entity_type,
                    evaluation_type,
                    part_expression,
                    label_expression,
                    zone_expression)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ScopeDefinition")
                    json_data = param_json["ScopeDefinition"] if "ScopeDefinition" in param_json else {}
                    self.__initialize(
                        entity_type if entity_type is not None else ( ScopeDefinition._default_params["entity_type"] if "entity_type" in ScopeDefinition._default_params else ScopeEntity(json_data["entityType"] if "entityType" in json_data else None)),
                        evaluation_type if evaluation_type is not None else ( ScopeDefinition._default_params["evaluation_type"] if "evaluation_type" in ScopeDefinition._default_params else ScopeEvaluationType(json_data["evaluationType"] if "evaluationType" in json_data else None)),
                        part_expression if part_expression is not None else ( ScopeDefinition._default_params["part_expression"] if "part_expression" in ScopeDefinition._default_params else (json_data["partExpression"] if "partExpression" in json_data else None)),
                        label_expression if label_expression is not None else ( ScopeDefinition._default_params["label_expression"] if "label_expression" in ScopeDefinition._default_params else (json_data["labelExpression"] if "labelExpression" in json_data else None)),
                        zone_expression if zone_expression is not None else ( ScopeDefinition._default_params["zone_expression"] if "zone_expression" in ScopeDefinition._default_params else (json_data["zoneExpression"] if "zoneExpression" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            entity_type : ScopeEntity = None,
            evaluation_type : ScopeEvaluationType = None,
            part_expression : str = None,
            label_expression : str = None,
            zone_expression : str = None):
        """Set the default values of the ``ScopeDefinition`` object.

        Parameters
        ----------
        entity_type : ScopeEntity, optional
            Entity type for which scope needs to be evaluated. The default is set to face zonelets.
        evaluation_type : ScopeEvaluationType, optional
            Evaluation type to scope entities. The default is set to labels.
        part_expression : str, optional
            Part expression to scope parts while evaluating scope.
        label_expression : str, optional
            Label expression to scope entities when evaluation type is set to labels.
        zone_expression : str, optional
            Zone expression to scope entities when evaluation type is set to zones.
        """
        args = locals()
        [ScopeDefinition._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ScopeDefinition`` object.

        Examples
        --------
        >>> ScopeDefinition.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScopeDefinition._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._entity_type is not None:
            json_data["entityType"] = self._entity_type
        if self._evaluation_type is not None:
            json_data["evaluationType"] = self._evaluation_type
        if self._part_expression is not None:
            json_data["partExpression"] = self._part_expression
        if self._label_expression is not None:
            json_data["labelExpression"] = self._label_expression
        if self._zone_expression is not None:
            json_data["zoneExpression"] = self._zone_expression
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "entity_type :  %s\nevaluation_type :  %s\npart_expression :  %s\nlabel_expression :  %s\nzone_expression :  %s" % (self._entity_type, self._evaluation_type, self._part_expression, self._label_expression, self._zone_expression)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def entity_type(self) -> ScopeEntity:
        """Entity type for which scope needs to be evaluated. The default is set to face zonelets.
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value: ScopeEntity):
        self._entity_type = value

    @property
    def evaluation_type(self) -> ScopeEvaluationType:
        """Evaluation type to scope entities. The default is set to labels.
        """
        return self._evaluation_type

    @evaluation_type.setter
    def evaluation_type(self, value: ScopeEvaluationType):
        self._evaluation_type = value

    @property
    def part_expression(self) -> str:
        """Part expression to scope parts while evaluating scope.
        """
        return self._part_expression

    @part_expression.setter
    def part_expression(self, value: str):
        self._part_expression = value

    @property
    def label_expression(self) -> str:
        """Label expression to scope entities when evaluation type is set to labels.
        """
        return self._label_expression

    @label_expression.setter
    def label_expression(self, value: str):
        self._label_expression = value

    @property
    def zone_expression(self) -> str:
        """Zone expression to scope entities when evaluation type is set to zones.
        """
        return self._zone_expression

    @zone_expression.setter
    def zone_expression(self, value: str):
        self._zone_expression = value

class SetSizingResults(CoreObject):
    """Result associated with the different set sizing parameters.

    Parameters
    ----------
    model : Model
        Model to create a ``SetSizingResults`` object with default parameters.
    warning_codes : List[WarningCode], optional
        Warning codes associated with the set sizing parameters.
    error_code : ErrorCode, optional
        Error code associated with the set sizing parameters.
    json_data : dict, optional
        JSON dictionary to create a ``SetSizingResults`` object with provided parameters.

    Examples
    --------
    >>> set_sizing_results = prime.SetSizingResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            warning_codes : List[WarningCode],
            error_code : ErrorCode):
        self._warning_codes = warning_codes
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            warning_codes : List[WarningCode] = None,
            error_code : ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetSizingResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetSizingResults`` object with default parameters.
        warning_codes : List[WarningCode], optional
            Warning codes associated with the set sizing parameters.
        error_code : ErrorCode, optional
            Error code associated with the set sizing parameters.
        json_data : dict, optional
            JSON dictionary to create a ``SetSizingResults`` object with provided parameters.

        Examples
        --------
        >>> set_sizing_results = prime.SetSizingResults(model = model)
        """
        if json_data:
            self.__initialize(
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [warning_codes, error_code])
            if all_field_specified:
                self.__initialize(
                    warning_codes,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetSizingResults")
                    json_data = param_json["SetSizingResults"] if "SetSizingResults" in param_json else {}
                    self.__initialize(
                        warning_codes if warning_codes is not None else ( SetSizingResults._default_params["warning_codes"] if "warning_codes" in SetSizingResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]),
                        error_code if error_code is not None else ( SetSizingResults._default_params["error_code"] if "error_code" in SetSizingResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            warning_codes : List[WarningCode] = None,
            error_code : ErrorCode = None):
        """Set the default values of the ``SetSizingResults`` object.

        Parameters
        ----------
        warning_codes : List[WarningCode], optional
            Warning codes associated with the set sizing parameters.
        error_code : ErrorCode, optional
            Error code associated with the set sizing parameters.
        """
        args = locals()
        [SetSizingResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetSizingResults`` object.

        Examples
        --------
        >>> SetSizingResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetSizingResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "warning_codes :  %s\nerror_code :  %s" % ('[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the set sizing parameters.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the set sizing parameters.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class GlobalSizingParams(CoreObject):
    """Global sizing parameters.

    Parameters
    ----------
    model : Model
        Model to create a ``GlobalSizingParams`` object with default parameters.
    min : float, optional
        Minimum value of global sizing parameters.
    max : float, optional
        Maximum value of global sizing parameters.
    growth_rate : float, optional
        Growth rate of global sizing parameters.
    json_data : dict, optional
        JSON dictionary to create a ``GlobalSizingParams`` object with provided parameters.

    Examples
    --------
    >>> global_sizing_params = prime.GlobalSizingParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            min : float,
            max : float,
            growth_rate : float):
        self._min = min
        self._max = max
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            min : float = None,
            max : float = None,
            growth_rate : float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``GlobalSizingParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``GlobalSizingParams`` object with default parameters.
        min : float, optional
            Minimum value of global sizing parameters.
        max : float, optional
            Maximum value of global sizing parameters.
        growth_rate : float, optional
            Growth rate of global sizing parameters.
        json_data : dict, optional
            JSON dictionary to create a ``GlobalSizingParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "GlobalSizingParams")
                    json_data = param_json["GlobalSizingParams"] if "GlobalSizingParams" in param_json else {}
                    self.__initialize(
                        min if min is not None else ( GlobalSizingParams._default_params["min"] if "min" in GlobalSizingParams._default_params else (json_data["min"] if "min" in json_data else None)),
                        max if max is not None else ( GlobalSizingParams._default_params["max"] if "max" in GlobalSizingParams._default_params else (json_data["max"] if "max" in json_data else None)),
                        growth_rate if growth_rate is not None else ( GlobalSizingParams._default_params["growth_rate"] if "growth_rate" in GlobalSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min : float = None,
            max : float = None,
            growth_rate : float = None):
        """Set the default values of the ``GlobalSizingParams`` object.

        Parameters
        ----------
        min : float, optional
            Minimum value of global sizing parameters.
        max : float, optional
            Maximum value of global sizing parameters.
        growth_rate : float, optional
            Growth rate of global sizing parameters.
        """
        args = locals()
        [GlobalSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``GlobalSizingParams`` object.

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
