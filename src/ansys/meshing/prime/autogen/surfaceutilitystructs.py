""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class SmoothType(enum.IntEnum):
    """Indicates the the type of operation to be performed during the smooth dihedral face nodes operation.
    """
    SMOOTH = 1
    """Performs smoothing during the operation."""
    INFLATE = 2
    """Performs inflation during the operation."""

class FlowDirection(enum.IntEnum):
    """Flow or wake direction for BOI creation.
    """
    X = 1
    """Flow or wake inflation in the X direction for BOI creation."""
    Y = 2
    """Flow or wake inflation in the Y direction for BOI creation."""
    Z = 3
    """Flow or wake inflation in the Z direction for BOI creation."""

class ContactPatchAxis(enum.IntEnum):
    """Flow or wake direction for BOI creation.
    """
    X = 1
    """Flow or wake inflation in the X direction for BOI creation."""
    Y = 2
    """Flow or wake inflation in the Y direction for BOI creation."""
    Z = 3
    """Flow or wake inflation in the Z direction for BOI creation."""

class BOIType(enum.IntEnum):
    """BOI type for BOI creation.
    """
    OFFSETBOX = 1
    """Box BOI type for BOI creation."""
    OFFSETSURFACE = 2
    """Surface BOI type for BOI creation."""

class FixInvalidNormalNodeParams(CoreObject):
    """Parameters to fix invalid average face normal at nodes by creating a nugget.
    """
    _default_params = {}

    def __initialize(
            self,
            nugget_size: float,
            nugget_mesh_size: float,
            label: str):
        self._nugget_size = nugget_size
        self._nugget_mesh_size = nugget_mesh_size
        self._label = label

    def __init__(
            self,
            model: CommunicationManager=None,
            nugget_size: float = None,
            nugget_mesh_size: float = None,
            label: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FixInvalidNormalNodeParams.

        Parameters
        ----------
        model: Model
            Model to create a FixInvalidNormalNodeParams object with default parameters.
        nugget_size: float, optional
            Relative size used to create nugget at invalid normal node. The size is relative to mesh size at the node.
        nugget_mesh_size: float, optional
            Relative size used as max size to mesh nugget created at invalid normal node. The size is relative to mesh size at the node.
        label: str, optional
            Label to set on new face zonelets created.
        json_data: dict, optional
            JSON dictionary to create a FixInvalidNormalNodeParams object with provided parameters.

        Examples
        --------
        >>> fix_invalid_normal_node_params = prime.FixInvalidNormalNodeParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nuggetSize"] if "nuggetSize" in json_data else None,
                json_data["nuggetMeshSize"] if "nuggetMeshSize" in json_data else None,
                json_data["label"] if "label" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [nugget_size, nugget_mesh_size, label])
            if all_field_specified:
                self.__initialize(
                    nugget_size,
                    nugget_mesh_size,
                    label)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "FixInvalidNormalNodeParams")
                    json_data = param_json["FixInvalidNormalNodeParams"] if "FixInvalidNormalNodeParams" in param_json else {}
                    self.__initialize(
                        nugget_size if nugget_size is not None else ( FixInvalidNormalNodeParams._default_params["nugget_size"] if "nugget_size" in FixInvalidNormalNodeParams._default_params else (json_data["nuggetSize"] if "nuggetSize" in json_data else None)),
                        nugget_mesh_size if nugget_mesh_size is not None else ( FixInvalidNormalNodeParams._default_params["nugget_mesh_size"] if "nugget_mesh_size" in FixInvalidNormalNodeParams._default_params else (json_data["nuggetMeshSize"] if "nuggetMeshSize" in json_data else None)),
                        label if label is not None else ( FixInvalidNormalNodeParams._default_params["label"] if "label" in FixInvalidNormalNodeParams._default_params else (json_data["label"] if "label" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            nugget_size: float = None,
            nugget_mesh_size: float = None,
            label: str = None):
        """Set the default values of FixInvalidNormalNodeParams.

        Parameters
        ----------
        nugget_size: float, optional
            Relative size used to create nugget at invalid normal node. The size is relative to mesh size at the node.
        nugget_mesh_size: float, optional
            Relative size used as max size to mesh nugget created at invalid normal node. The size is relative to mesh size at the node.
        label: str, optional
            Label to set on new face zonelets created.
        """
        args = locals()
        [FixInvalidNormalNodeParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FixInvalidNormalNodeParams.

        Examples
        --------
        >>> FixInvalidNormalNodeParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FixInvalidNormalNodeParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._nugget_size is not None:
            json_data["nuggetSize"] = self._nugget_size
        if self._nugget_mesh_size is not None:
            json_data["nuggetMeshSize"] = self._nugget_mesh_size
        if self._label is not None:
            json_data["label"] = self._label
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "nugget_size :  %s\nnugget_mesh_size :  %s\nlabel :  %s" % (self._nugget_size, self._nugget_mesh_size, self._label)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def nugget_size(self) -> float:
        """Relative size used to create nugget at invalid normal node. The size is relative to mesh size at the node.
        """
        return self._nugget_size

    @nugget_size.setter
    def nugget_size(self, value: float):
        self._nugget_size = value

    @property
    def nugget_mesh_size(self) -> float:
        """Relative size used as max size to mesh nugget created at invalid normal node. The size is relative to mesh size at the node.
        """
        return self._nugget_mesh_size

    @nugget_mesh_size.setter
    def nugget_mesh_size(self, value: float):
        self._nugget_mesh_size = value

    @property
    def label(self) -> str:
        """Label to set on new face zonelets created.
        """
        return self._label

    @label.setter
    def label(self, value: str):
        self._label = value

class FixInvalidNormalNodeResults(CoreObject):
    """Results associated with fix invalid average face normal at nodes.
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
        """Initializes the FixInvalidNormalNodeResults.

        Parameters
        ----------
        model: Model
            Model to create a FixInvalidNormalNodeResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a FixInvalidNormalNodeResults object with provided parameters.

        Examples
        --------
        >>> fix_invalid_normal_node_results = prime.FixInvalidNormalNodeResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "FixInvalidNormalNodeResults")
                    json_data = param_json["FixInvalidNormalNodeResults"] if "FixInvalidNormalNodeResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FixInvalidNormalNodeResults._default_params["error_code"] if "error_code" in FixInvalidNormalNodeResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of FixInvalidNormalNodeResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        """
        args = locals()
        [FixInvalidNormalNodeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FixInvalidNormalNodeResults.

        Examples
        --------
        >>> FixInvalidNormalNodeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FixInvalidNormalNodeResults._default_params.items())
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
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

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
            Suggested name to be set on merged part. If the suggested name is empty, the parameter uses the default name.
        json_data: dict, optional
            JSON dictionary to create a FillHolesAtPlaneParams object with provided parameters.

        Examples
        --------
        >>> fill_holes_at_plane_params = prime.FillHolesAtPlaneParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["createZone"] if "createZone" in json_data else None,
                json_data["suggestedZoneName"] if "suggestedZoneName" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "FillHolesAtPlaneParams")
                    json_data = param_json["FillHolesAtPlaneParams"] if "FillHolesAtPlaneParams" in param_json else {}
                    self.__initialize(
                        create_zone if create_zone is not None else ( FillHolesAtPlaneParams._default_params["create_zone"] if "create_zone" in FillHolesAtPlaneParams._default_params else (json_data["createZone"] if "createZone" in json_data else None)),
                        suggested_zone_name if suggested_zone_name is not None else ( FillHolesAtPlaneParams._default_params["suggested_zone_name"] if "suggested_zone_name" in FillHolesAtPlaneParams._default_params else (json_data["suggestedZoneName"] if "suggestedZoneName" in json_data else None)))
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
            Suggested name to be set on merged part. If the suggested name is empty, the parameter uses the default name.
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
        if self._create_zone is not None:
            json_data["createZone"] = self._create_zone
        if self._suggested_zone_name is not None:
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
        """Suggested name to be set on merged part. If the suggested name is empty, the parameter uses the default name.
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
        self._created_face_zonelets = created_face_zonelets if isinstance(created_face_zonelets, np.ndarray) else np.array(created_face_zonelets, dtype=np.int32) if created_face_zonelets is not None else None
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
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None,
                json_data["createdFaceZonelets"] if "createdFaceZonelets" in json_data else None,
                json_data["assignedZoneName"] if "assignedZoneName" in json_data else None,
                json_data["createdZoneId"] if "createdZoneId" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "FillHolesAtPlaneResults")
                    json_data = param_json["FillHolesAtPlaneResults"] if "FillHolesAtPlaneResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FillHolesAtPlaneResults._default_params["error_code"] if "error_code" in FillHolesAtPlaneResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( FillHolesAtPlaneResults._default_params["warning_codes"] if "warning_codes" in FillHolesAtPlaneResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]),
                        created_face_zonelets if created_face_zonelets is not None else ( FillHolesAtPlaneResults._default_params["created_face_zonelets"] if "created_face_zonelets" in FillHolesAtPlaneResults._default_params else (json_data["createdFaceZonelets"] if "createdFaceZonelets" in json_data else None)),
                        assigned_zone_name if assigned_zone_name is not None else ( FillHolesAtPlaneResults._default_params["assigned_zone_name"] if "assigned_zone_name" in FillHolesAtPlaneResults._default_params else (json_data["assignedZoneName"] if "assignedZoneName" in json_data else None)),
                        created_zone_id if created_zone_id is not None else ( FillHolesAtPlaneResults._default_params["created_zone_id"] if "created_zone_id" in FillHolesAtPlaneResults._default_params else (json_data["createdZoneId"] if "createdZoneId" in json_data else None)))
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
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        if self._created_face_zonelets is not None:
            json_data["createdFaceZonelets"] = self._created_face_zonelets
        if self._assigned_zone_name is not None:
            json_data["assignedZoneName"] = self._assigned_zone_name
        if self._created_zone_id is not None:
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
                    param_json = model._communicator.initialize_params(model, "CreateCapParams")
                    json_data = param_json["CreateCapParams"] if "CreateCapParams" in param_json else {}
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
        if len(message) == 0:
            message = 'The object has no parameters to print.'
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
        self._created_face_zonelets = created_face_zonelets if isinstance(created_face_zonelets, np.ndarray) else np.array(created_face_zonelets, dtype=np.int32) if created_face_zonelets is not None else None

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
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["createdFaceZonelets"] if "createdFaceZonelets" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "CreateCapResults")
                    json_data = param_json["CreateCapResults"] if "CreateCapResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CreateCapResults._default_params["error_code"] if "error_code" in CreateCapResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        created_face_zonelets if created_face_zonelets is not None else ( CreateCapResults._default_params["created_face_zonelets"] if "created_face_zonelets" in CreateCapResults._default_params else (json_data["createdFaceZonelets"] if "createdFaceZonelets" in json_data else None)))
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
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._created_face_zonelets is not None:
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
                    param_json = model._communicator.initialize_params(model, "DeleteUnwettedParams")
                    json_data = param_json["DeleteUnwettedParams"] if "DeleteUnwettedParams" in param_json else {}
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
        if len(message) == 0:
            message = 'The object has no parameters to print.'
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
                    param_json = model._communicator.initialize_params(model, "DeleteUnwettedResult")
                    json_data = param_json["DeleteUnwettedResult"] if "DeleteUnwettedResult" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteUnwettedResult._default_params["error_code"] if "error_code" in DeleteUnwettedResult._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
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
                json_data["numberOfThreads"] if "numberOfThreads" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [number_of_threads])
            if all_field_specified:
                self.__initialize(
                    number_of_threads)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ResolveIntersectionsParams")
                    json_data = param_json["ResolveIntersectionsParams"] if "ResolveIntersectionsParams" in param_json else {}
                    self.__initialize(
                        number_of_threads if number_of_threads is not None else ( ResolveIntersectionsParams._default_params["number_of_threads"] if "number_of_threads" in ResolveIntersectionsParams._default_params else (json_data["numberOfThreads"] if "numberOfThreads" in json_data else None)))
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
        if self._number_of_threads is not None:
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
                    param_json = model._communicator.initialize_params(model, "ResolveIntersectionResult")
                    json_data = param_json["ResolveIntersectionResult"] if "ResolveIntersectionResult" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ResolveIntersectionResult._default_params["error_code"] if "error_code" in ResolveIntersectionResult._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
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
                json_data["retainCutter"] if "retainCutter" in json_data else None,
                json_data["extractEdges"] if "extractEdges" in json_data else None,
                json_data["traceEdges"] if "traceEdges" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "SubtractZoneletsParams")
                    json_data = param_json["SubtractZoneletsParams"] if "SubtractZoneletsParams" in param_json else {}
                    self.__initialize(
                        retain_cutter if retain_cutter is not None else ( SubtractZoneletsParams._default_params["retain_cutter"] if "retain_cutter" in SubtractZoneletsParams._default_params else (json_data["retainCutter"] if "retainCutter" in json_data else None)),
                        extract_edges if extract_edges is not None else ( SubtractZoneletsParams._default_params["extract_edges"] if "extract_edges" in SubtractZoneletsParams._default_params else (json_data["extractEdges"] if "extractEdges" in json_data else None)),
                        trace_edges if trace_edges is not None else ( SubtractZoneletsParams._default_params["trace_edges"] if "trace_edges" in SubtractZoneletsParams._default_params else (json_data["traceEdges"] if "traceEdges" in json_data else None)))
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
        if self._retain_cutter is not None:
            json_data["retainCutter"] = self._retain_cutter
        if self._extract_edges is not None:
            json_data["extractEdges"] = self._extract_edges
        if self._trace_edges is not None:
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
                json_data["processingTime"] if "processingTime" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
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
                    param_json = model._communicator.initialize_params(model, "SubtractZoneletsResults")
                    json_data = param_json["SubtractZoneletsResults"] if "SubtractZoneletsResults" in param_json else {}
                    self.__initialize(
                        processing_time if processing_time is not None else ( SubtractZoneletsResults._default_params["processing_time"] if "processing_time" in SubtractZoneletsResults._default_params else (json_data["processingTime"] if "processingTime" in json_data else None)),
                        error_code if error_code is not None else ( SubtractZoneletsResults._default_params["error_code"] if "error_code" in SubtractZoneletsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
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
        if self._processing_time is not None:
            json_data["processingTime"] = self._processing_time
        if self._error_code is not None:
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

class SmoothDihedralFaceNodesParams(CoreObject):
    """Parameters to smooth dihedral face nodes.
    """
    _default_params = {}

    def __initialize(
            self,
            min_dihedral_angle: float,
            tolerance: float,
            type: SmoothType):
        self._min_dihedral_angle = min_dihedral_angle
        self._tolerance = tolerance
        self._type = SmoothType(type)

    def __init__(
            self,
            model: CommunicationManager=None,
            min_dihedral_angle: float = None,
            tolerance: float = None,
            type: SmoothType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SmoothDihedralFaceNodesParams.

        Parameters
        ----------
        model: Model
            Model to create a SmoothDihedralFaceNodesParams object with default parameters.
        min_dihedral_angle: float, optional
            Minimum angle to be used to identify dihedral faces.
        tolerance: float, optional
            Tolerance relative to local mesh size to control smooth movement of nodes.
        type: SmoothType, optional
            Option to inflate neighbor nodes of dihedral face edges or smooth dihedral face edge nodes to improve dihedral angle.
        json_data: dict, optional
            JSON dictionary to create a SmoothDihedralFaceNodesParams object with provided parameters.

        Examples
        --------
        >>> smooth_dihedral_face_nodes_params = prime.SmoothDihedralFaceNodesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["minDihedralAngle"] if "minDihedralAngle" in json_data else None,
                json_data["tolerance"] if "tolerance" in json_data else None,
                SmoothType(json_data["type"] if "type" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [min_dihedral_angle, tolerance, type])
            if all_field_specified:
                self.__initialize(
                    min_dihedral_angle,
                    tolerance,
                    type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SmoothDihedralFaceNodesParams")
                    json_data = param_json["SmoothDihedralFaceNodesParams"] if "SmoothDihedralFaceNodesParams" in param_json else {}
                    self.__initialize(
                        min_dihedral_angle if min_dihedral_angle is not None else ( SmoothDihedralFaceNodesParams._default_params["min_dihedral_angle"] if "min_dihedral_angle" in SmoothDihedralFaceNodesParams._default_params else (json_data["minDihedralAngle"] if "minDihedralAngle" in json_data else None)),
                        tolerance if tolerance is not None else ( SmoothDihedralFaceNodesParams._default_params["tolerance"] if "tolerance" in SmoothDihedralFaceNodesParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)),
                        type if type is not None else ( SmoothDihedralFaceNodesParams._default_params["type"] if "type" in SmoothDihedralFaceNodesParams._default_params else SmoothType(json_data["type"] if "type" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min_dihedral_angle: float = None,
            tolerance: float = None,
            type: SmoothType = None):
        """Set the default values of SmoothDihedralFaceNodesParams.

        Parameters
        ----------
        min_dihedral_angle: float, optional
            Minimum angle to be used to identify dihedral faces.
        tolerance: float, optional
            Tolerance relative to local mesh size to control smooth movement of nodes.
        type: SmoothType, optional
            Option to inflate neighbor nodes of dihedral face edges or smooth dihedral face edge nodes to improve dihedral angle.
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
        if self._min_dihedral_angle is not None:
            json_data["minDihedralAngle"] = self._min_dihedral_angle
        if self._tolerance is not None:
            json_data["tolerance"] = self._tolerance
        if self._type is not None:
            json_data["type"] = self._type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min_dihedral_angle :  %s\ntolerance :  %s\ntype :  %s" % (self._min_dihedral_angle, self._tolerance, self._type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min_dihedral_angle(self) -> float:
        """Minimum angle to be used to identify dihedral faces.
        """
        return self._min_dihedral_angle

    @min_dihedral_angle.setter
    def min_dihedral_angle(self, value: float):
        self._min_dihedral_angle = value

    @property
    def tolerance(self) -> float:
        """Tolerance relative to local mesh size to control smooth movement of nodes.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        self._tolerance = value

    @property
    def type(self) -> SmoothType:
        """Option to inflate neighbor nodes of dihedral face edges or smooth dihedral face edge nodes to improve dihedral angle.
        """
        return self._type

    @type.setter
    def type(self, value: SmoothType):
        self._type = value

class SmoothDihedralFaceNodesResults(CoreObject):
    """Results structure associated with smooth dihedral face nodes.
    """
    _default_params = {}

    def __initialize(
            self,
            n_nodes_smoothed: int,
            error_code: ErrorCode):
        self._n_nodes_smoothed = n_nodes_smoothed
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_nodes_smoothed: int = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SmoothDihedralFaceNodesResults.

        Parameters
        ----------
        model: Model
            Model to create a SmoothDihedralFaceNodesResults object with default parameters.
        n_nodes_smoothed: int, optional
            Number of dihedral face nodes smoothed.
        error_code: ErrorCode, optional
            Error Code associated with creating offset surface.
        json_data: dict, optional
            JSON dictionary to create a SmoothDihedralFaceNodesResults object with provided parameters.

        Examples
        --------
        >>> smooth_dihedral_face_nodes_results = prime.SmoothDihedralFaceNodesResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nNodesSmoothed"] if "nNodesSmoothed" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [n_nodes_smoothed, error_code])
            if all_field_specified:
                self.__initialize(
                    n_nodes_smoothed,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SmoothDihedralFaceNodesResults")
                    json_data = param_json["SmoothDihedralFaceNodesResults"] if "SmoothDihedralFaceNodesResults" in param_json else {}
                    self.__initialize(
                        n_nodes_smoothed if n_nodes_smoothed is not None else ( SmoothDihedralFaceNodesResults._default_params["n_nodes_smoothed"] if "n_nodes_smoothed" in SmoothDihedralFaceNodesResults._default_params else (json_data["nNodesSmoothed"] if "nNodesSmoothed" in json_data else None)),
                        error_code if error_code is not None else ( SmoothDihedralFaceNodesResults._default_params["error_code"] if "error_code" in SmoothDihedralFaceNodesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_nodes_smoothed: int = None,
            error_code: ErrorCode = None):
        """Set the default values of SmoothDihedralFaceNodesResults.

        Parameters
        ----------
        n_nodes_smoothed: int, optional
            Number of dihedral face nodes smoothed.
        error_code: ErrorCode, optional
            Error Code associated with creating offset surface.
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
        if self._n_nodes_smoothed is not None:
            json_data["nNodesSmoothed"] = self._n_nodes_smoothed
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_nodes_smoothed :  %s\nerror_code :  %s" % (self._n_nodes_smoothed, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_nodes_smoothed(self) -> int:
        """Number of dihedral face nodes smoothed.
        """
        return self._n_nodes_smoothed

    @n_nodes_smoothed.setter
    def n_nodes_smoothed(self, value: int):
        self._n_nodes_smoothed = value

    @property
    def error_code(self) -> ErrorCode:
        """Error Code associated with creating offset surface.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

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
                json_data["contactTolerance"] if "contactTolerance" in json_data else None,
                json_data["relativeTolerance"] if "relativeTolerance" in json_data else None,
                json_data["refineMaxSize"] if "refineMaxSize" in json_data else None,
                json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "RefineAtContactsParams")
                    json_data = param_json["RefineAtContactsParams"] if "RefineAtContactsParams" in param_json else {}
                    self.__initialize(
                        contact_tolerance if contact_tolerance is not None else ( RefineAtContactsParams._default_params["contact_tolerance"] if "contact_tolerance" in RefineAtContactsParams._default_params else (json_data["contactTolerance"] if "contactTolerance" in json_data else None)),
                        relative_tolerance if relative_tolerance is not None else ( RefineAtContactsParams._default_params["relative_tolerance"] if "relative_tolerance" in RefineAtContactsParams._default_params else (json_data["relativeTolerance"] if "relativeTolerance" in json_data else None)),
                        refine_max_size if refine_max_size is not None else ( RefineAtContactsParams._default_params["refine_max_size"] if "refine_max_size" in RefineAtContactsParams._default_params else (json_data["refineMaxSize"] if "refineMaxSize" in json_data else None)),
                        project_on_geometry if project_on_geometry is not None else ( RefineAtContactsParams._default_params["project_on_geometry"] if "project_on_geometry" in RefineAtContactsParams._default_params else (json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None)))
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
        if self._contact_tolerance is not None:
            json_data["contactTolerance"] = self._contact_tolerance
        if self._relative_tolerance is not None:
            json_data["relativeTolerance"] = self._relative_tolerance
        if self._refine_max_size is not None:
            json_data["refineMaxSize"] = self._refine_max_size
        if self._project_on_geometry is not None:
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
                json_data["nRefined"] if "nRefined" in json_data else None,
                json_data["sizeFieldId"] if "sizeFieldId" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
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
                    param_json = model._communicator.initialize_params(model, "RefineAtContactsResults")
                    json_data = param_json["RefineAtContactsResults"] if "RefineAtContactsResults" in param_json else {}
                    self.__initialize(
                        n_refined if n_refined is not None else ( RefineAtContactsResults._default_params["n_refined"] if "n_refined" in RefineAtContactsResults._default_params else (json_data["nRefined"] if "nRefined" in json_data else None)),
                        size_field_id if size_field_id is not None else ( RefineAtContactsResults._default_params["size_field_id"] if "size_field_id" in RefineAtContactsResults._default_params else (json_data["sizeFieldId"] if "sizeFieldId" in json_data else None)),
                        error_code if error_code is not None else ( RefineAtContactsResults._default_params["error_code"] if "error_code" in RefineAtContactsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
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
        if self._n_refined is not None:
            json_data["nRefined"] = self._n_refined
        if self._size_field_id is not None:
            json_data["sizeFieldId"] = self._size_field_id
        if self._error_code is not None:
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
                json_data["thickness"] if "thickness" in json_data else None,
                json_data["reverseFaceNormal"] if "reverseFaceNormal" in json_data else None,
                json_data["suggestedPartName"] if "suggestedPartName" in json_data else None,
                json_data["fixIntersections"] if "fixIntersections" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "AddThicknessParams")
                    json_data = param_json["AddThicknessParams"] if "AddThicknessParams" in param_json else {}
                    self.__initialize(
                        thickness if thickness is not None else ( AddThicknessParams._default_params["thickness"] if "thickness" in AddThicknessParams._default_params else (json_data["thickness"] if "thickness" in json_data else None)),
                        reverse_face_normal if reverse_face_normal is not None else ( AddThicknessParams._default_params["reverse_face_normal"] if "reverse_face_normal" in AddThicknessParams._default_params else (json_data["reverseFaceNormal"] if "reverseFaceNormal" in json_data else None)),
                        suggested_part_name if suggested_part_name is not None else ( AddThicknessParams._default_params["suggested_part_name"] if "suggested_part_name" in AddThicknessParams._default_params else (json_data["suggestedPartName"] if "suggestedPartName" in json_data else None)),
                        fix_intersections if fix_intersections is not None else ( AddThicknessParams._default_params["fix_intersections"] if "fix_intersections" in AddThicknessParams._default_params else (json_data["fixIntersections"] if "fixIntersections" in json_data else None)))
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
        if self._thickness is not None:
            json_data["thickness"] = self._thickness
        if self._reverse_face_normal is not None:
            json_data["reverseFaceNormal"] = self._reverse_face_normal
        if self._suggested_part_name is not None:
            json_data["suggestedPartName"] = self._suggested_part_name
        if self._fix_intersections is not None:
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
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["partId"] if "partId" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "AddThicknessResults")
                    json_data = param_json["AddThicknessResults"] if "AddThicknessResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( AddThicknessResults._default_params["error_code"] if "error_code" in AddThicknessResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        part_id if part_id is not None else ( AddThicknessResults._default_params["part_id"] if "part_id" in AddThicknessResults._default_params else (json_data["partId"] if "partId" in json_data else None)))
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
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._part_id is not None:
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

class CreateBOIParams(CoreObject):
    """Parameters used for BOI surface creation in the given axis.
    """
    _default_params = {}

    def __initialize(
            self,
            boi_type: BOIType,
            perform_initial_wrap: bool,
            wrap_size: float,
            flow_dir: FlowDirection,
            side_scale: float,
            wake_scale: float,
            wake_levels: int,
            suggested_part_name: str,
            suggested_label_prefix: str,
            number_of_threads: int):
        self._boi_type = BOIType(boi_type)
        self._perform_initial_wrap = perform_initial_wrap
        self._wrap_size = wrap_size
        self._flow_dir = FlowDirection(flow_dir)
        self._side_scale = side_scale
        self._wake_scale = wake_scale
        self._wake_levels = wake_levels
        self._suggested_part_name = suggested_part_name
        self._suggested_label_prefix = suggested_label_prefix
        self._number_of_threads = number_of_threads

    def __init__(
            self,
            model: CommunicationManager=None,
            boi_type: BOIType = None,
            perform_initial_wrap: bool = None,
            wrap_size: float = None,
            flow_dir: FlowDirection = None,
            side_scale: float = None,
            wake_scale: float = None,
            wake_levels: int = None,
            suggested_part_name: str = None,
            suggested_label_prefix: str = None,
            number_of_threads: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateBOIParams.

        Parameters
        ----------
        model: Model
            Model to create a CreateBOIParams object with default parameters.
        boi_type: BOIType, optional
            Type of BOI offsetting.
        perform_initial_wrap: bool, optional
            Perform an initial wrap to create a BOI if BOI type is OFFSETSURFACE.
        wrap_size: float, optional
            Set wrap size greater than the largest gap size in the input when performing_initial_wrap is true.
        flow_dir: FlowDirection, optional
            Assigns the offset direction of inflation.
        side_scale: float, optional
            BOI side scaling factor.
        wake_scale: float, optional
            BOI flow direction scaling factor.
        wake_levels: int, optional
            BOI levels.
        suggested_part_name: str, optional
            Suggested part name for created BOI surfaces.
        suggested_label_prefix: str, optional
            Suggested label name for created BOI surfaces.
        number_of_threads: int, optional
            Number of threads for multithreading.
        json_data: dict, optional
            JSON dictionary to create a CreateBOIParams object with provided parameters.

        Examples
        --------
        >>> create_boiparams = prime.CreateBOIParams(model = model)
        """
        if json_data:
            self.__initialize(
                BOIType(json_data["boiType"] if "boiType" in json_data else None),
                json_data["performInitialWrap"] if "performInitialWrap" in json_data else None,
                json_data["wrapSize"] if "wrapSize" in json_data else None,
                FlowDirection(json_data["flowDir"] if "flowDir" in json_data else None),
                json_data["sideScale"] if "sideScale" in json_data else None,
                json_data["wakeScale"] if "wakeScale" in json_data else None,
                json_data["wakeLevels"] if "wakeLevels" in json_data else None,
                json_data["suggestedPartName"] if "suggestedPartName" in json_data else None,
                json_data["suggestedLabelPrefix"] if "suggestedLabelPrefix" in json_data else None,
                json_data["numberOfThreads"] if "numberOfThreads" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [boi_type, perform_initial_wrap, wrap_size, flow_dir, side_scale, wake_scale, wake_levels, suggested_part_name, suggested_label_prefix, number_of_threads])
            if all_field_specified:
                self.__initialize(
                    boi_type,
                    perform_initial_wrap,
                    wrap_size,
                    flow_dir,
                    side_scale,
                    wake_scale,
                    wake_levels,
                    suggested_part_name,
                    suggested_label_prefix,
                    number_of_threads)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CreateBOIParams")
                    json_data = param_json["CreateBOIParams"] if "CreateBOIParams" in param_json else {}
                    self.__initialize(
                        boi_type if boi_type is not None else ( CreateBOIParams._default_params["boi_type"] if "boi_type" in CreateBOIParams._default_params else BOIType(json_data["boiType"] if "boiType" in json_data else None)),
                        perform_initial_wrap if perform_initial_wrap is not None else ( CreateBOIParams._default_params["perform_initial_wrap"] if "perform_initial_wrap" in CreateBOIParams._default_params else (json_data["performInitialWrap"] if "performInitialWrap" in json_data else None)),
                        wrap_size if wrap_size is not None else ( CreateBOIParams._default_params["wrap_size"] if "wrap_size" in CreateBOIParams._default_params else (json_data["wrapSize"] if "wrapSize" in json_data else None)),
                        flow_dir if flow_dir is not None else ( CreateBOIParams._default_params["flow_dir"] if "flow_dir" in CreateBOIParams._default_params else FlowDirection(json_data["flowDir"] if "flowDir" in json_data else None)),
                        side_scale if side_scale is not None else ( CreateBOIParams._default_params["side_scale"] if "side_scale" in CreateBOIParams._default_params else (json_data["sideScale"] if "sideScale" in json_data else None)),
                        wake_scale if wake_scale is not None else ( CreateBOIParams._default_params["wake_scale"] if "wake_scale" in CreateBOIParams._default_params else (json_data["wakeScale"] if "wakeScale" in json_data else None)),
                        wake_levels if wake_levels is not None else ( CreateBOIParams._default_params["wake_levels"] if "wake_levels" in CreateBOIParams._default_params else (json_data["wakeLevels"] if "wakeLevels" in json_data else None)),
                        suggested_part_name if suggested_part_name is not None else ( CreateBOIParams._default_params["suggested_part_name"] if "suggested_part_name" in CreateBOIParams._default_params else (json_data["suggestedPartName"] if "suggestedPartName" in json_data else None)),
                        suggested_label_prefix if suggested_label_prefix is not None else ( CreateBOIParams._default_params["suggested_label_prefix"] if "suggested_label_prefix" in CreateBOIParams._default_params else (json_data["suggestedLabelPrefix"] if "suggestedLabelPrefix" in json_data else None)),
                        number_of_threads if number_of_threads is not None else ( CreateBOIParams._default_params["number_of_threads"] if "number_of_threads" in CreateBOIParams._default_params else (json_data["numberOfThreads"] if "numberOfThreads" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            boi_type: BOIType = None,
            perform_initial_wrap: bool = None,
            wrap_size: float = None,
            flow_dir: FlowDirection = None,
            side_scale: float = None,
            wake_scale: float = None,
            wake_levels: int = None,
            suggested_part_name: str = None,
            suggested_label_prefix: str = None,
            number_of_threads: int = None):
        """Set the default values of CreateBOIParams.

        Parameters
        ----------
        boi_type: BOIType, optional
            Type of BOI offsetting.
        perform_initial_wrap: bool, optional
            Perform an initial wrap to create a BOI if BOI type is OFFSETSURFACE.
        wrap_size: float, optional
            Set wrap size greater than the largest gap size in the input when performing_initial_wrap is true.
        flow_dir: FlowDirection, optional
            Assigns the offset direction of inflation.
        side_scale: float, optional
            BOI side scaling factor.
        wake_scale: float, optional
            BOI flow direction scaling factor.
        wake_levels: int, optional
            BOI levels.
        suggested_part_name: str, optional
            Suggested part name for created BOI surfaces.
        suggested_label_prefix: str, optional
            Suggested label name for created BOI surfaces.
        number_of_threads: int, optional
            Number of threads for multithreading.
        """
        args = locals()
        [CreateBOIParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateBOIParams.

        Examples
        --------
        >>> CreateBOIParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateBOIParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._boi_type is not None:
            json_data["boiType"] = self._boi_type
        if self._perform_initial_wrap is not None:
            json_data["performInitialWrap"] = self._perform_initial_wrap
        if self._wrap_size is not None:
            json_data["wrapSize"] = self._wrap_size
        if self._flow_dir is not None:
            json_data["flowDir"] = self._flow_dir
        if self._side_scale is not None:
            json_data["sideScale"] = self._side_scale
        if self._wake_scale is not None:
            json_data["wakeScale"] = self._wake_scale
        if self._wake_levels is not None:
            json_data["wakeLevels"] = self._wake_levels
        if self._suggested_part_name is not None:
            json_data["suggestedPartName"] = self._suggested_part_name
        if self._suggested_label_prefix is not None:
            json_data["suggestedLabelPrefix"] = self._suggested_label_prefix
        if self._number_of_threads is not None:
            json_data["numberOfThreads"] = self._number_of_threads
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "boi_type :  %s\nperform_initial_wrap :  %s\nwrap_size :  %s\nflow_dir :  %s\nside_scale :  %s\nwake_scale :  %s\nwake_levels :  %s\nsuggested_part_name :  %s\nsuggested_label_prefix :  %s\nnumber_of_threads :  %s" % (self._boi_type, self._perform_initial_wrap, self._wrap_size, self._flow_dir, self._side_scale, self._wake_scale, self._wake_levels, self._suggested_part_name, self._suggested_label_prefix, self._number_of_threads)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def boi_type(self) -> BOIType:
        """Type of BOI offsetting.
        """
        return self._boi_type

    @boi_type.setter
    def boi_type(self, value: BOIType):
        self._boi_type = value

    @property
    def perform_initial_wrap(self) -> bool:
        """Perform an initial wrap to create a BOI if BOI type is OFFSETSURFACE.
        """
        return self._perform_initial_wrap

    @perform_initial_wrap.setter
    def perform_initial_wrap(self, value: bool):
        self._perform_initial_wrap = value

    @property
    def wrap_size(self) -> float:
        """Set wrap size greater than the largest gap size in the input when performing_initial_wrap is true.
        """
        return self._wrap_size

    @wrap_size.setter
    def wrap_size(self, value: float):
        self._wrap_size = value

    @property
    def flow_dir(self) -> FlowDirection:
        """Assigns the offset direction of inflation.
        """
        return self._flow_dir

    @flow_dir.setter
    def flow_dir(self, value: FlowDirection):
        self._flow_dir = value

    @property
    def side_scale(self) -> float:
        """BOI side scaling factor.
        """
        return self._side_scale

    @side_scale.setter
    def side_scale(self, value: float):
        self._side_scale = value

    @property
    def wake_scale(self) -> float:
        """BOI flow direction scaling factor.
        """
        return self._wake_scale

    @wake_scale.setter
    def wake_scale(self, value: float):
        self._wake_scale = value

    @property
    def wake_levels(self) -> int:
        """BOI levels.
        """
        return self._wake_levels

    @wake_levels.setter
    def wake_levels(self, value: int):
        self._wake_levels = value

    @property
    def suggested_part_name(self) -> str:
        """Suggested part name for created BOI surfaces.
        """
        return self._suggested_part_name

    @suggested_part_name.setter
    def suggested_part_name(self, value: str):
        self._suggested_part_name = value

    @property
    def suggested_label_prefix(self) -> str:
        """Suggested label name for created BOI surfaces.
        """
        return self._suggested_label_prefix

    @suggested_label_prefix.setter
    def suggested_label_prefix(self, value: str):
        self._suggested_label_prefix = value

    @property
    def number_of_threads(self) -> int:
        """Number of threads for multithreading.
        """
        return self._number_of_threads

    @number_of_threads.setter
    def number_of_threads(self, value: int):
        self._number_of_threads = value

class CreateBOIResults(CoreObject):
    """Result structure associated with BOI creation of zonelets.
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
        """Initializes the CreateBOIResults.

        Parameters
        ----------
        model: Model
            Model to create a CreateBOIResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        part_id: int, optional
            The BOI part id.
        json_data: dict, optional
            JSON dictionary to create a CreateBOIResults object with provided parameters.

        Examples
        --------
        >>> create_boiresults = prime.CreateBOIResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["partId"] if "partId" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "CreateBOIResults")
                    json_data = param_json["CreateBOIResults"] if "CreateBOIResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CreateBOIResults._default_params["error_code"] if "error_code" in CreateBOIResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        part_id if part_id is not None else ( CreateBOIResults._default_params["part_id"] if "part_id" in CreateBOIResults._default_params else (json_data["partId"] if "partId" in json_data else None)))
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
        """Set the default values of CreateBOIResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        part_id: int, optional
            The BOI part id.
        """
        args = locals()
        [CreateBOIResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateBOIResults.

        Examples
        --------
        >>> CreateBOIResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateBOIResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._part_id is not None:
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
        """The BOI part id.
        """
        return self._part_id

    @part_id.setter
    def part_id(self, value: int):
        self._part_id = value

class CreateContactPatchParams(CoreObject):
    """Parameters used for contact patch creation in the given axis.
    """
    _default_params = {}

    def __initialize(
            self,
            contact_patch_axis: ContactPatchAxis,
            offset_distance: float,
            grouping_tolerance: float,
            suggested_part_name: str,
            suggested_label_prefix: str):
        self._contact_patch_axis = ContactPatchAxis(contact_patch_axis)
        self._offset_distance = offset_distance
        self._grouping_tolerance = grouping_tolerance
        self._suggested_part_name = suggested_part_name
        self._suggested_label_prefix = suggested_label_prefix

    def __init__(
            self,
            model: CommunicationManager=None,
            contact_patch_axis: ContactPatchAxis = None,
            offset_distance: float = None,
            grouping_tolerance: float = None,
            suggested_part_name: str = None,
            suggested_label_prefix: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateContactPatchParams.

        Parameters
        ----------
        model: Model
            Model to create a CreateContactPatchParams object with default parameters.
        contact_patch_axis: ContactPatchAxis, optional
            Assigns the contact patch direction.
        offset_distance: float, optional
            Source offset distance value.
        grouping_tolerance: float, optional
            Tolerance distance value to group regions for contact patch creation.
        suggested_part_name: str, optional
            Suggested part name for created contact patch surfaces.
        suggested_label_prefix: str, optional
            Suggested label name for created contact patch surfaces.
        json_data: dict, optional
            JSON dictionary to create a CreateContactPatchParams object with provided parameters.

        Examples
        --------
        >>> create_contact_patch_params = prime.CreateContactPatchParams(model = model)
        """
        if json_data:
            self.__initialize(
                ContactPatchAxis(json_data["contactPatchAxis"] if "contactPatchAxis" in json_data else None),
                json_data["offsetDistance"] if "offsetDistance" in json_data else None,
                json_data["groupingTolerance"] if "groupingTolerance" in json_data else None,
                json_data["suggestedPartName"] if "suggestedPartName" in json_data else None,
                json_data["suggestedLabelPrefix"] if "suggestedLabelPrefix" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [contact_patch_axis, offset_distance, grouping_tolerance, suggested_part_name, suggested_label_prefix])
            if all_field_specified:
                self.__initialize(
                    contact_patch_axis,
                    offset_distance,
                    grouping_tolerance,
                    suggested_part_name,
                    suggested_label_prefix)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CreateContactPatchParams")
                    json_data = param_json["CreateContactPatchParams"] if "CreateContactPatchParams" in param_json else {}
                    self.__initialize(
                        contact_patch_axis if contact_patch_axis is not None else ( CreateContactPatchParams._default_params["contact_patch_axis"] if "contact_patch_axis" in CreateContactPatchParams._default_params else ContactPatchAxis(json_data["contactPatchAxis"] if "contactPatchAxis" in json_data else None)),
                        offset_distance if offset_distance is not None else ( CreateContactPatchParams._default_params["offset_distance"] if "offset_distance" in CreateContactPatchParams._default_params else (json_data["offsetDistance"] if "offsetDistance" in json_data else None)),
                        grouping_tolerance if grouping_tolerance is not None else ( CreateContactPatchParams._default_params["grouping_tolerance"] if "grouping_tolerance" in CreateContactPatchParams._default_params else (json_data["groupingTolerance"] if "groupingTolerance" in json_data else None)),
                        suggested_part_name if suggested_part_name is not None else ( CreateContactPatchParams._default_params["suggested_part_name"] if "suggested_part_name" in CreateContactPatchParams._default_params else (json_data["suggestedPartName"] if "suggestedPartName" in json_data else None)),
                        suggested_label_prefix if suggested_label_prefix is not None else ( CreateContactPatchParams._default_params["suggested_label_prefix"] if "suggested_label_prefix" in CreateContactPatchParams._default_params else (json_data["suggestedLabelPrefix"] if "suggestedLabelPrefix" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            contact_patch_axis: ContactPatchAxis = None,
            offset_distance: float = None,
            grouping_tolerance: float = None,
            suggested_part_name: str = None,
            suggested_label_prefix: str = None):
        """Set the default values of CreateContactPatchParams.

        Parameters
        ----------
        contact_patch_axis: ContactPatchAxis, optional
            Assigns the contact patch direction.
        offset_distance: float, optional
            Source offset distance value.
        grouping_tolerance: float, optional
            Tolerance distance value to group regions for contact patch creation.
        suggested_part_name: str, optional
            Suggested part name for created contact patch surfaces.
        suggested_label_prefix: str, optional
            Suggested label name for created contact patch surfaces.
        """
        args = locals()
        [CreateContactPatchParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateContactPatchParams.

        Examples
        --------
        >>> CreateContactPatchParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateContactPatchParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._contact_patch_axis is not None:
            json_data["contactPatchAxis"] = self._contact_patch_axis
        if self._offset_distance is not None:
            json_data["offsetDistance"] = self._offset_distance
        if self._grouping_tolerance is not None:
            json_data["groupingTolerance"] = self._grouping_tolerance
        if self._suggested_part_name is not None:
            json_data["suggestedPartName"] = self._suggested_part_name
        if self._suggested_label_prefix is not None:
            json_data["suggestedLabelPrefix"] = self._suggested_label_prefix
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "contact_patch_axis :  %s\noffset_distance :  %s\ngrouping_tolerance :  %s\nsuggested_part_name :  %s\nsuggested_label_prefix :  %s" % (self._contact_patch_axis, self._offset_distance, self._grouping_tolerance, self._suggested_part_name, self._suggested_label_prefix)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def contact_patch_axis(self) -> ContactPatchAxis:
        """Assigns the contact patch direction.
        """
        return self._contact_patch_axis

    @contact_patch_axis.setter
    def contact_patch_axis(self, value: ContactPatchAxis):
        self._contact_patch_axis = value

    @property
    def offset_distance(self) -> float:
        """Source offset distance value.
        """
        return self._offset_distance

    @offset_distance.setter
    def offset_distance(self, value: float):
        self._offset_distance = value

    @property
    def grouping_tolerance(self) -> float:
        """Tolerance distance value to group regions for contact patch creation.
        """
        return self._grouping_tolerance

    @grouping_tolerance.setter
    def grouping_tolerance(self, value: float):
        self._grouping_tolerance = value

    @property
    def suggested_part_name(self) -> str:
        """Suggested part name for created contact patch surfaces.
        """
        return self._suggested_part_name

    @suggested_part_name.setter
    def suggested_part_name(self, value: str):
        self._suggested_part_name = value

    @property
    def suggested_label_prefix(self) -> str:
        """Suggested label name for created contact patch surfaces.
        """
        return self._suggested_label_prefix

    @suggested_label_prefix.setter
    def suggested_label_prefix(self, value: str):
        self._suggested_label_prefix = value

class CreateContactPatchResults(CoreObject):
    """Result structure associated with created contact patch zonelets.
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
        """Initializes the CreateContactPatchResults.

        Parameters
        ----------
        model: Model
            Model to create a CreateContactPatchResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the contact patch creation operation.
        part_id: int, optional
            Contact patch part id.
        json_data: dict, optional
            JSON dictionary to create a CreateContactPatchResults object with provided parameters.

        Examples
        --------
        >>> create_contact_patch_results = prime.CreateContactPatchResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["partId"] if "partId" in json_data else None)
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
                    param_json = model._communicator.initialize_params(model, "CreateContactPatchResults")
                    json_data = param_json["CreateContactPatchResults"] if "CreateContactPatchResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CreateContactPatchResults._default_params["error_code"] if "error_code" in CreateContactPatchResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        part_id if part_id is not None else ( CreateContactPatchResults._default_params["part_id"] if "part_id" in CreateContactPatchResults._default_params else (json_data["partId"] if "partId" in json_data else None)))
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
        """Set the default values of CreateContactPatchResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the contact patch creation operation.
        part_id: int, optional
            Contact patch part id.
        """
        args = locals()
        [CreateContactPatchResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateContactPatchResults.

        Examples
        --------
        >>> CreateContactPatchResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateContactPatchResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._part_id is not None:
            json_data["partId"] = self._part_id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\npart_id :  %s" % (self._error_code, self._part_id)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the contact patch creation operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def part_id(self) -> int:
        """Contact patch part id.
        """
        return self._part_id

    @part_id.setter
    def part_id(self, value: int):
        self._part_id = value

class StretchFreeBoundariesParams(CoreObject):
    """Parameters used for stretch free boundaries operation.
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
        """Initializes the StretchFreeBoundariesParams.

        Parameters
        ----------
        model: Model
            Model to create a StretchFreeBoundariesParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a StretchFreeBoundariesParams object with provided parameters.

        Examples
        --------
        >>> stretch_free_boundaries_params = prime.StretchFreeBoundariesParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "StretchFreeBoundariesParams")
                    json_data = param_json["StretchFreeBoundariesParams"] if "StretchFreeBoundariesParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of StretchFreeBoundariesParams.

        """
        args = locals()
        [StretchFreeBoundariesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of StretchFreeBoundariesParams.

        Examples
        --------
        >>> StretchFreeBoundariesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in StretchFreeBoundariesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        if len(message) == 0:
            message = 'The object has no parameters to print.'
        return message

class StretchFreeBoundariesResults(CoreObject):
    """Results associated with stretch free boundaries operation.
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
        """Initializes the StretchFreeBoundariesResults.

        Parameters
        ----------
        model: Model
            Model to create a StretchFreeBoundariesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a StretchFreeBoundariesResults object with provided parameters.

        Examples
        --------
        >>> stretch_free_boundaries_results = prime.StretchFreeBoundariesResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "StretchFreeBoundariesResults")
                    json_data = param_json["StretchFreeBoundariesResults"] if "StretchFreeBoundariesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( StretchFreeBoundariesResults._default_params["error_code"] if "error_code" in StretchFreeBoundariesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of StretchFreeBoundariesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        """
        args = locals()
        [StretchFreeBoundariesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of StretchFreeBoundariesResults.

        Examples
        --------
        >>> StretchFreeBoundariesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in StretchFreeBoundariesResults._default_params.items())
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
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
