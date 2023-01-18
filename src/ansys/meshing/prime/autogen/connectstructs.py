""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class JoinSeparateMethod(enum.IntEnum):
    """Join separation method to handle separated overlapped zonelets.
    """
    KEEPNONE = 0
    """Remove both overlapping zonelets after joining."""
    KEEPONE = 1
    """Keep one overlap zonelets after joining."""
    KEEPBOTH = 2
    """Keep both overlapping zonelets after joining."""

class StitchType(enum.IntEnum):
    """Stitch type depending on nature of surface boundary edges to be stitched.
    """
    ALLALL = 0
    """Stitch surfaces at boundary edges."""
    FREEFREE = 1
    """Stitch surfaces at free boundary edges."""

class MatchedMeshOption(enum.IntEnum):
    """Type to specify treatment of matched mesh. This is for internal use only.
    """
    NONE = 0
    """No action to be taken for matched mesh."""
    TRIMONESIDE = 3
    """Delete matched faces on one side and merge matched nodes at middle locations (works only within a single part)."""
    TRIMTWOSIDES = 4
    """Delete matched faces on both sides and merge matched nodes at middle locations (works only within a single part)."""

class ConnectResults(CoreObject):
    """Results associated with the connection operations.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ConnectResults.

        Parameters
        ----------
        model: Model
            Model to create a ConnectResults object with default parameters.
        error_code: ErrorCode, optional
            Error Code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        json_data: dict, optional
            JSON dictionary to create a ConnectResults object with provided parameters.

        Examples
        --------
        >>> connect_results = prime.ConnectResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ConnectResults")
                    json_data = param_json["ConnectResults"] if "ConnectResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ConnectResults._default_params["error_code"] if "error_code" in ConnectResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ConnectResults._default_params["warning_codes"] if "warning_codes" in ConnectResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of ConnectResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error Code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [ConnectResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ConnectResults.

        Examples
        --------
        >>> ConnectResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ConnectResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error Code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class IntersectParams(CoreObject):
    """Parameters used for intersection.
    """
    _default_params = {}

    def __initialize(
            self,
            tolerance: float,
            use_absolute_tolerance: bool,
            remesh: bool):
        self._tolerance = tolerance
        self._use_absolute_tolerance = use_absolute_tolerance
        self._remesh = remesh

    def __init__(
            self,
            model: CommunicationManager=None,
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the IntersectParams.

        Parameters
        ----------
        model: Model
            Model to create a IntersectParams object with default parameters.
        tolerance: float, optional
            Intersection tolerance.
        use_absolute_tolerance: bool, optional
            True if tolerance provided is absolute value.
        remesh: bool, optional
            Local remesh at the intersection.
        json_data: dict, optional
            JSON dictionary to create a IntersectParams object with provided parameters.

        Examples
        --------
        >>> intersect_params = prime.IntersectParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["tolerance"] if "tolerance" in json_data else None,
                json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None,
                json_data["remesh"] if "remesh" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [tolerance, use_absolute_tolerance, remesh])
            if all_field_specified:
                self.__initialize(
                    tolerance,
                    use_absolute_tolerance,
                    remesh)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "IntersectParams")
                    json_data = param_json["IntersectParams"] if "IntersectParams" in param_json else {}
                    self.__initialize(
                        tolerance if tolerance is not None else ( IntersectParams._default_params["tolerance"] if "tolerance" in IntersectParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( IntersectParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in IntersectParams._default_params else (json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None)),
                        remesh if remesh is not None else ( IntersectParams._default_params["remesh"] if "remesh" in IntersectParams._default_params else (json_data["remesh"] if "remesh" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None):
        """Set the default values of IntersectParams.

        Parameters
        ----------
        tolerance: float, optional
            Intersection tolerance.
        use_absolute_tolerance: bool, optional
            True if tolerance provided is absolute value.
        remesh: bool, optional
            Local remesh at the intersection.
        """
        args = locals()
        [IntersectParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of IntersectParams.

        Examples
        --------
        >>> IntersectParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in IntersectParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._tolerance is not None:
            json_data["tolerance"] = self._tolerance
        if self._use_absolute_tolerance is not None:
            json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
        if self._remesh is not None:
            json_data["remesh"] = self._remesh
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "tolerance :  %s\nuse_absolute_tolerance :  %s\nremesh :  %s" % (self._tolerance, self._use_absolute_tolerance, self._remesh)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def tolerance(self) -> float:
        """Intersection tolerance.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        self._tolerance = value

    @property
    def use_absolute_tolerance(self) -> bool:
        """True if tolerance provided is absolute value.
        """
        return self._use_absolute_tolerance

    @use_absolute_tolerance.setter
    def use_absolute_tolerance(self, value: bool):
        self._use_absolute_tolerance = value

    @property
    def remesh(self) -> bool:
        """Local remesh at the intersection.
        """
        return self._remesh

    @remesh.setter
    def remesh(self, value: bool):
        self._remesh = value

class JoinParams(CoreObject):
    """Parameters used for join.
    """
    _default_params = {}

    def __initialize(
            self,
            tolerance: float,
            use_absolute_tolerance: bool,
            remesh: bool,
            match_angle: float,
            overlap_zone_name: str):
        self._tolerance = tolerance
        self._use_absolute_tolerance = use_absolute_tolerance
        self._remesh = remesh
        self._match_angle = match_angle
        self._overlap_zone_name = overlap_zone_name

    def __init__(
            self,
            model: CommunicationManager=None,
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None,
            match_angle: float = None,
            overlap_zone_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the JoinParams.

        Parameters
        ----------
        model: Model
            Model to create a JoinParams object with default parameters.
        tolerance: float, optional
            Overlap tolerance between overlapping zonelets.
        use_absolute_tolerance: bool, optional
            Tolerance provided is absolute value.
        remesh: bool, optional
            Remesh at overlap surface boundary.
        match_angle: float, optional
            Match angle determines face pair inclination for overlap consideration.
        overlap_zone_name: str, optional
            Zone id to be assigned to overlap zonelets belonging to different zones.
        json_data: dict, optional
            JSON dictionary to create a JoinParams object with provided parameters.

        Examples
        --------
        >>> join_params = prime.JoinParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["tolerance"] if "tolerance" in json_data else None,
                json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None,
                json_data["remesh"] if "remesh" in json_data else None,
                json_data["matchAngle"] if "matchAngle" in json_data else None,
                json_data["overlapZoneName"] if "overlapZoneName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [tolerance, use_absolute_tolerance, remesh, match_angle, overlap_zone_name])
            if all_field_specified:
                self.__initialize(
                    tolerance,
                    use_absolute_tolerance,
                    remesh,
                    match_angle,
                    overlap_zone_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "JoinParams")
                    json_data = param_json["JoinParams"] if "JoinParams" in param_json else {}
                    self.__initialize(
                        tolerance if tolerance is not None else ( JoinParams._default_params["tolerance"] if "tolerance" in JoinParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( JoinParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in JoinParams._default_params else (json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None)),
                        remesh if remesh is not None else ( JoinParams._default_params["remesh"] if "remesh" in JoinParams._default_params else (json_data["remesh"] if "remesh" in json_data else None)),
                        match_angle if match_angle is not None else ( JoinParams._default_params["match_angle"] if "match_angle" in JoinParams._default_params else (json_data["matchAngle"] if "matchAngle" in json_data else None)),
                        overlap_zone_name if overlap_zone_name is not None else ( JoinParams._default_params["overlap_zone_name"] if "overlap_zone_name" in JoinParams._default_params else (json_data["overlapZoneName"] if "overlapZoneName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None,
            match_angle: float = None,
            overlap_zone_name: str = None):
        """Set the default values of JoinParams.

        Parameters
        ----------
        tolerance: float, optional
            Overlap tolerance between overlapping zonelets.
        use_absolute_tolerance: bool, optional
            Tolerance provided is absolute value.
        remesh: bool, optional
            Remesh at overlap surface boundary.
        match_angle: float, optional
            Match angle determines face pair inclination for overlap consideration.
        overlap_zone_name: str, optional
            Zone id to be assigned to overlap zonelets belonging to different zones.
        """
        args = locals()
        [JoinParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of JoinParams.

        Examples
        --------
        >>> JoinParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in JoinParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._tolerance is not None:
            json_data["tolerance"] = self._tolerance
        if self._use_absolute_tolerance is not None:
            json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
        if self._remesh is not None:
            json_data["remesh"] = self._remesh
        if self._match_angle is not None:
            json_data["matchAngle"] = self._match_angle
        if self._overlap_zone_name is not None:
            json_data["overlapZoneName"] = self._overlap_zone_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "tolerance :  %s\nuse_absolute_tolerance :  %s\nremesh :  %s\nmatch_angle :  %s\noverlap_zone_name :  %s" % (self._tolerance, self._use_absolute_tolerance, self._remesh, self._match_angle, self._overlap_zone_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def tolerance(self) -> float:
        """Overlap tolerance between overlapping zonelets.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        self._tolerance = value

    @property
    def use_absolute_tolerance(self) -> bool:
        """Tolerance provided is absolute value.
        """
        return self._use_absolute_tolerance

    @use_absolute_tolerance.setter
    def use_absolute_tolerance(self, value: bool):
        self._use_absolute_tolerance = value

    @property
    def remesh(self) -> bool:
        """Remesh at overlap surface boundary.
        """
        return self._remesh

    @remesh.setter
    def remesh(self, value: bool):
        self._remesh = value

    @property
    def match_angle(self) -> float:
        """Match angle determines face pair inclination for overlap consideration.
        """
        return self._match_angle

    @match_angle.setter
    def match_angle(self, value: float):
        self._match_angle = value

    @property
    def overlap_zone_name(self) -> str:
        """Zone id to be assigned to overlap zonelets belonging to different zones.
        """
        return self._overlap_zone_name

    @overlap_zone_name.setter
    def overlap_zone_name(self, value: str):
        self._overlap_zone_name = value

class SubtractVolumesParams(CoreObject):
    """Parameters to control the volume subtract operation.
    """
    _default_params = {}

    def __initialize(
            self,
            ignore_face_zonelets: Iterable[int],
            check_cutters: bool):
        self._ignore_face_zonelets = ignore_face_zonelets if isinstance(ignore_face_zonelets, np.ndarray) else np.array(ignore_face_zonelets, dtype=np.int32) if ignore_face_zonelets is not None else None
        self._check_cutters = check_cutters

    def __init__(
            self,
            model: CommunicationManager=None,
            ignore_face_zonelets: Iterable[int] = None,
            check_cutters: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SubtractVolumesParams.

        Parameters
        ----------
        model: Model
            Model to create a SubtractVolumesParams object with default parameters.
        ignore_face_zonelets: Iterable[int], optional
            Face zonelet ids that subtract volumes should not remove.(For example, periodic or fluid cap zonelets)
        check_cutters: bool, optional
            Option to handle overlapping or intersecting cutter volumes.
        json_data: dict, optional
            JSON dictionary to create a SubtractVolumesParams object with provided parameters.

        Examples
        --------
        >>> subtract_volumes_params = prime.SubtractVolumesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["ignoreFaceZonelets"] if "ignoreFaceZonelets" in json_data else None,
                json_data["checkCutters"] if "checkCutters" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [ignore_face_zonelets, check_cutters])
            if all_field_specified:
                self.__initialize(
                    ignore_face_zonelets,
                    check_cutters)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SubtractVolumesParams")
                    json_data = param_json["SubtractVolumesParams"] if "SubtractVolumesParams" in param_json else {}
                    self.__initialize(
                        ignore_face_zonelets if ignore_face_zonelets is not None else ( SubtractVolumesParams._default_params["ignore_face_zonelets"] if "ignore_face_zonelets" in SubtractVolumesParams._default_params else (json_data["ignoreFaceZonelets"] if "ignoreFaceZonelets" in json_data else None)),
                        check_cutters if check_cutters is not None else ( SubtractVolumesParams._default_params["check_cutters"] if "check_cutters" in SubtractVolumesParams._default_params else (json_data["checkCutters"] if "checkCutters" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            ignore_face_zonelets: Iterable[int] = None,
            check_cutters: bool = None):
        """Set the default values of SubtractVolumesParams.

        Parameters
        ----------
        ignore_face_zonelets: Iterable[int], optional
            Face zonelet ids that subtract volumes should not remove.(For example, periodic or fluid cap zonelets)
        check_cutters: bool, optional
            Option to handle overlapping or intersecting cutter volumes.
        """
        args = locals()
        [SubtractVolumesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SubtractVolumesParams.

        Examples
        --------
        >>> SubtractVolumesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SubtractVolumesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._ignore_face_zonelets is not None:
            json_data["ignoreFaceZonelets"] = self._ignore_face_zonelets
        if self._check_cutters is not None:
            json_data["checkCutters"] = self._check_cutters
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "ignore_face_zonelets :  %s\ncheck_cutters :  %s" % (self._ignore_face_zonelets, self._check_cutters)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def ignore_face_zonelets(self) -> Iterable[int]:
        """Face zonelet ids that subtract volumes should not remove.(For example, periodic or fluid cap zonelets)
        """
        return self._ignore_face_zonelets

    @ignore_face_zonelets.setter
    def ignore_face_zonelets(self, value: Iterable[int]):
        self._ignore_face_zonelets = value

    @property
    def check_cutters(self) -> bool:
        """Option to handle overlapping or intersecting cutter volumes.
        """
        return self._check_cutters

    @check_cutters.setter
    def check_cutters(self, value: bool):
        self._check_cutters = value

class SubtractVolumesResults(CoreObject):
    """Results of the volume subtract operation.
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
        """Initializes the SubtractVolumesResults.

        Parameters
        ----------
        model: Model
            Model to create a SubtractVolumesResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the volume subtract operation.
        json_data: dict, optional
            JSON dictionary to create a SubtractVolumesResults object with provided parameters.

        Examples
        --------
        >>> subtract_volumes_results = prime.SubtractVolumesResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "SubtractVolumesResults")
                    json_data = param_json["SubtractVolumesResults"] if "SubtractVolumesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SubtractVolumesResults._default_params["error_code"] if "error_code" in SubtractVolumesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of SubtractVolumesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the volume subtract operation.
        """
        args = locals()
        [SubtractVolumesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SubtractVolumesResults.

        Examples
        --------
        >>> SubtractVolumesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SubtractVolumesResults._default_params.items())
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
        """Error code associated with the volume subtract operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class StitchParams(CoreObject):
    """Parameters used for stitch operation.
    """
    _default_params = {}

    def __initialize(
            self,
            tolerance: float,
            use_absolute_tolerance: bool,
            remesh: bool,
            enable_multi_threading: bool,
            type: StitchType):
        self._tolerance = tolerance
        self._use_absolute_tolerance = use_absolute_tolerance
        self._remesh = remesh
        self._enable_multi_threading = enable_multi_threading
        self._type = StitchType(type)

    def __init__(
            self,
            model: CommunicationManager=None,
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None,
            enable_multi_threading: bool = None,
            type: StitchType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the StitchParams.

        Parameters
        ----------
        model: Model
            Model to create a StitchParams object with default parameters.
        tolerance: float, optional
            Distance tolerance for stitching boundaries.
        use_absolute_tolerance: bool, optional
            True if tolerance provided is absolute value.
        remesh: bool, optional
            Remesh at stitch connection.
        enable_multi_threading: bool, optional
            Option to run stitch in parallel using multithread.
        type: StitchType, optional
            Stitch type depending on nature of surface boundary edges to be stitched.
        json_data: dict, optional
            JSON dictionary to create a StitchParams object with provided parameters.

        Examples
        --------
        >>> stitch_params = prime.StitchParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["tolerance"] if "tolerance" in json_data else None,
                json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None,
                json_data["remesh"] if "remesh" in json_data else None,
                json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None,
                StitchType(json_data["type"] if "type" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [tolerance, use_absolute_tolerance, remesh, enable_multi_threading, type])
            if all_field_specified:
                self.__initialize(
                    tolerance,
                    use_absolute_tolerance,
                    remesh,
                    enable_multi_threading,
                    type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "StitchParams")
                    json_data = param_json["StitchParams"] if "StitchParams" in param_json else {}
                    self.__initialize(
                        tolerance if tolerance is not None else ( StitchParams._default_params["tolerance"] if "tolerance" in StitchParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( StitchParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in StitchParams._default_params else (json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None)),
                        remesh if remesh is not None else ( StitchParams._default_params["remesh"] if "remesh" in StitchParams._default_params else (json_data["remesh"] if "remesh" in json_data else None)),
                        enable_multi_threading if enable_multi_threading is not None else ( StitchParams._default_params["enable_multi_threading"] if "enable_multi_threading" in StitchParams._default_params else (json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None)),
                        type if type is not None else ( StitchParams._default_params["type"] if "type" in StitchParams._default_params else StitchType(json_data["type"] if "type" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None,
            enable_multi_threading: bool = None,
            type: StitchType = None):
        """Set the default values of StitchParams.

        Parameters
        ----------
        tolerance: float, optional
            Distance tolerance for stitching boundaries.
        use_absolute_tolerance: bool, optional
            True if tolerance provided is absolute value.
        remesh: bool, optional
            Remesh at stitch connection.
        enable_multi_threading: bool, optional
            Option to run stitch in parallel using multithread.
        type: StitchType, optional
            Stitch type depending on nature of surface boundary edges to be stitched.
        """
        args = locals()
        [StitchParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of StitchParams.

        Examples
        --------
        >>> StitchParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in StitchParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._tolerance is not None:
            json_data["tolerance"] = self._tolerance
        if self._use_absolute_tolerance is not None:
            json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
        if self._remesh is not None:
            json_data["remesh"] = self._remesh
        if self._enable_multi_threading is not None:
            json_data["enableMultiThreading"] = self._enable_multi_threading
        if self._type is not None:
            json_data["type"] = self._type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "tolerance :  %s\nuse_absolute_tolerance :  %s\nremesh :  %s\nenable_multi_threading :  %s\ntype :  %s" % (self._tolerance, self._use_absolute_tolerance, self._remesh, self._enable_multi_threading, self._type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def tolerance(self) -> float:
        """Distance tolerance for stitching boundaries.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        self._tolerance = value

    @property
    def use_absolute_tolerance(self) -> bool:
        """True if tolerance provided is absolute value.
        """
        return self._use_absolute_tolerance

    @use_absolute_tolerance.setter
    def use_absolute_tolerance(self, value: bool):
        self._use_absolute_tolerance = value

    @property
    def remesh(self) -> bool:
        """Remesh at stitch connection.
        """
        return self._remesh

    @remesh.setter
    def remesh(self, value: bool):
        self._remesh = value

    @property
    def enable_multi_threading(self) -> bool:
        """Option to run stitch in parallel using multithread.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value

    @property
    def type(self) -> StitchType:
        """Stitch type depending on nature of surface boundary edges to be stitched.
        """
        return self._type

    @type.setter
    def type(self, value: StitchType):
        self._type = value

class MeshMatchParams(CoreObject):
    """Parameters to match surface mesh. This is for internal use only.
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
        """Initializes the MeshMatchParams.

        Parameters
        ----------
        model: Model
            Model to create a MeshMatchParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a MeshMatchParams object with provided parameters.

        Examples
        --------
        >>> mesh_match_params = prime.MeshMatchParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "MeshMatchParams")
                    json_data = param_json["MeshMatchParams"] if "MeshMatchParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of MeshMatchParams.

        """
        args = locals()
        [MeshMatchParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MeshMatchParams.

        Examples
        --------
        >>> MeshMatchParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MeshMatchParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class MeshMatchResults(CoreObject):
    """Results associated with the mesh match operations. This is for internal use only.
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
        """Initializes the MeshMatchResults.

        Parameters
        ----------
        model: Model
            Model to create a MeshMatchResults object with default parameters.
        error_code: ErrorCode, optional
            Error Code associated with failure of mesh match operation.
        json_data: dict, optional
            JSON dictionary to create a MeshMatchResults object with provided parameters.

        Examples
        --------
        >>> mesh_match_results = prime.MeshMatchResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "MeshMatchResults")
                    json_data = param_json["MeshMatchResults"] if "MeshMatchResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( MeshMatchResults._default_params["error_code"] if "error_code" in MeshMatchResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of MeshMatchResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error Code associated with failure of mesh match operation.
        """
        args = locals()
        [MeshMatchResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MeshMatchResults.

        Examples
        --------
        >>> MeshMatchResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MeshMatchResults._default_params.items())
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
        """Error Code associated with failure of mesh match operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
