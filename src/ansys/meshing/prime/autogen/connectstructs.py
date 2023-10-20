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

class MergeNodeType(enum.IntEnum):
    """Type of nodes to be merged.
    """
    ALLALL = 0
    """Merge any type of nodes with any type of nodes."""
    FREEFREE = 1
    """Merge only free nodes with free nodes."""

class MatchedMeshOption(enum.IntEnum):
    """Type to specify treatment of matched mesh.
    """
    NONE = 0
    """No action to be taken for matched mesh."""
    TRIMONESIDE = 3
    """Delete matched faces on one side and merge matched nodes at middle locations (works only within a single part)."""
    TRIMTWOSIDES = 4
    """Delete matched faces on both sides and merge matched nodes at middle locations (works only within a single part)."""

class OverlapPairs(CoreObject):
    """Provides ids of a pair of overlapping face zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            zone_id0: int,
            zone_id1: int):
        self._zone_id0 = zone_id0
        self._zone_id1 = zone_id1

    def __init__(
            self,
            model: CommunicationManager=None,
            zone_id0: int = None,
            zone_id1: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the OverlapPairs.

        Parameters
        ----------
        model: Model
            Model to create a OverlapPairs object with default parameters.
        zone_id0: int, optional
            Id of one overlapping face zonelet.
        zone_id1: int, optional
            Id of other overlapping face zonelet.
        json_data: dict, optional
            JSON dictionary to create a OverlapPairs object with provided parameters.

        Examples
        --------
        >>> overlap_pairs = prime.OverlapPairs(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["zoneId0"] if "zoneId0" in json_data else None,
                json_data["zoneId1"] if "zoneId1" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [zone_id0, zone_id1])
            if all_field_specified:
                self.__initialize(
                    zone_id0,
                    zone_id1)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "OverlapPairs")
                    json_data = param_json["OverlapPairs"] if "OverlapPairs" in param_json else {}
                    self.__initialize(
                        zone_id0 if zone_id0 is not None else ( OverlapPairs._default_params["zone_id0"] if "zone_id0" in OverlapPairs._default_params else (json_data["zoneId0"] if "zoneId0" in json_data else None)),
                        zone_id1 if zone_id1 is not None else ( OverlapPairs._default_params["zone_id1"] if "zone_id1" in OverlapPairs._default_params else (json_data["zoneId1"] if "zoneId1" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            zone_id0: int = None,
            zone_id1: int = None):
        """Set the default values of OverlapPairs.

        Parameters
        ----------
        zone_id0: int, optional
            Id of one overlapping face zonelet.
        zone_id1: int, optional
            Id of other overlapping face zonelet.
        """
        args = locals()
        [OverlapPairs._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of OverlapPairs.

        Examples
        --------
        >>> OverlapPairs.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in OverlapPairs._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._zone_id0 is not None:
            json_data["zoneId0"] = self._zone_id0
        if self._zone_id1 is not None:
            json_data["zoneId1"] = self._zone_id1
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "zone_id0 :  %s\nzone_id1 :  %s" % (self._zone_id0, self._zone_id1)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def zone_id0(self) -> int:
        """Id of one overlapping face zonelet.
        """
        return self._zone_id0

    @zone_id0.setter
    def zone_id0(self, value: int):
        self._zone_id0 = value

    @property
    def zone_id1(self) -> int:
        """Id of other overlapping face zonelet.
        """
        return self._zone_id1

    @zone_id1.setter
    def zone_id1(self, value: int):
        self._zone_id1 = value

class OverlapSearchResults(CoreObject):
    """Provides ids of a pair of overlapping face zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            n_pairs: int,
            overlap_pairs: List[OverlapPairs],
            error_code: ErrorCode):
        self._n_pairs = n_pairs
        self._overlap_pairs = overlap_pairs
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_pairs: int = None,
            overlap_pairs: List[OverlapPairs] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the OverlapSearchResults.

        Parameters
        ----------
        model: Model
            Model to create a OverlapSearchResults object with default parameters.
        n_pairs: int, optional
            Number of pairs.
        overlap_pairs: List[OverlapPairs], optional
            Ids corresponding to pairs of overlapping face zonelets.
        error_code: ErrorCode, optional
            Error Code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a OverlapSearchResults object with provided parameters.

        Examples
        --------
        >>> overlap_search_results = prime.OverlapSearchResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nPairs"] if "nPairs" in json_data else None,
                [OverlapPairs(model = model, json_data = data) for data in json_data["overlapPairs"]] if "overlapPairs" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [n_pairs, overlap_pairs, error_code])
            if all_field_specified:
                self.__initialize(
                    n_pairs,
                    overlap_pairs,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "OverlapSearchResults")
                    json_data = param_json["OverlapSearchResults"] if "OverlapSearchResults" in param_json else {}
                    self.__initialize(
                        n_pairs if n_pairs is not None else ( OverlapSearchResults._default_params["n_pairs"] if "n_pairs" in OverlapSearchResults._default_params else (json_data["nPairs"] if "nPairs" in json_data else None)),
                        overlap_pairs if overlap_pairs is not None else ( OverlapSearchResults._default_params["overlap_pairs"] if "overlap_pairs" in OverlapSearchResults._default_params else [OverlapPairs(model = model, json_data = data) for data in (json_data["overlapPairs"] if "overlapPairs" in json_data else None)]),
                        error_code if error_code is not None else ( OverlapSearchResults._default_params["error_code"] if "error_code" in OverlapSearchResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_pairs: int = None,
            overlap_pairs: List[OverlapPairs] = None,
            error_code: ErrorCode = None):
        """Set the default values of OverlapSearchResults.

        Parameters
        ----------
        n_pairs: int, optional
            Number of pairs.
        overlap_pairs: List[OverlapPairs], optional
            Ids corresponding to pairs of overlapping face zonelets.
        error_code: ErrorCode, optional
            Error Code associated with failure of operation.
        """
        args = locals()
        [OverlapSearchResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of OverlapSearchResults.

        Examples
        --------
        >>> OverlapSearchResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in OverlapSearchResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._n_pairs is not None:
            json_data["nPairs"] = self._n_pairs
        if self._overlap_pairs is not None:
            json_data["overlapPairs"] = [data._jsonify() for data in self._overlap_pairs]
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_pairs :  %s\noverlap_pairs :  %s\nerror_code :  %s" % (self._n_pairs, '[' + ''.join('\n' + str(data) for data in self._overlap_pairs) + ']', self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_pairs(self) -> int:
        """Number of pairs.
        """
        return self._n_pairs

    @n_pairs.setter
    def n_pairs(self, value: int):
        self._n_pairs = value

    @property
    def overlap_pairs(self) -> List[OverlapPairs]:
        """Ids corresponding to pairs of overlapping face zonelets.
        """
        return self._overlap_pairs

    @overlap_pairs.setter
    def overlap_pairs(self, value: List[OverlapPairs]):
        self._overlap_pairs = value

    @property
    def error_code(self) -> ErrorCode:
        """Error Code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

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
            remesh: bool,
            collapse_feature_angle: float,
            collapse_target_skewness: float):
        self._tolerance = tolerance
        self._use_absolute_tolerance = use_absolute_tolerance
        self._remesh = remesh
        self._collapse_feature_angle = collapse_feature_angle
        self._collapse_target_skewness = collapse_target_skewness

    def __init__(
            self,
            model: CommunicationManager=None,
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            remesh: bool = None,
            collapse_feature_angle: float = None,
            collapse_target_skewness: float = None,
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
        collapse_feature_angle: float, optional
            Angle to preserve features while performing collapse in improve operation.
        collapse_target_skewness: float, optional
            Perform collapse on faces with skewness above the provided target skewness.
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
                json_data["remesh"] if "remesh" in json_data else None,
                json_data["collapseFeatureAngle"] if "collapseFeatureAngle" in json_data else None,
                json_data["collapseTargetSkewness"] if "collapseTargetSkewness" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [tolerance, use_absolute_tolerance, remesh, collapse_feature_angle, collapse_target_skewness])
            if all_field_specified:
                self.__initialize(
                    tolerance,
                    use_absolute_tolerance,
                    remesh,
                    collapse_feature_angle,
                    collapse_target_skewness)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "IntersectParams")
                    json_data = param_json["IntersectParams"] if "IntersectParams" in param_json else {}
                    self.__initialize(
                        tolerance if tolerance is not None else ( IntersectParams._default_params["tolerance"] if "tolerance" in IntersectParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( IntersectParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in IntersectParams._default_params else (json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None)),
                        remesh if remesh is not None else ( IntersectParams._default_params["remesh"] if "remesh" in IntersectParams._default_params else (json_data["remesh"] if "remesh" in json_data else None)),
                        collapse_feature_angle if collapse_feature_angle is not None else ( IntersectParams._default_params["collapse_feature_angle"] if "collapse_feature_angle" in IntersectParams._default_params else (json_data["collapseFeatureAngle"] if "collapseFeatureAngle" in json_data else None)),
                        collapse_target_skewness if collapse_target_skewness is not None else ( IntersectParams._default_params["collapse_target_skewness"] if "collapse_target_skewness" in IntersectParams._default_params else (json_data["collapseTargetSkewness"] if "collapseTargetSkewness" in json_data else None)))
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
            collapse_feature_angle: float = None,
            collapse_target_skewness: float = None):
        """Set the default values of IntersectParams.

        Parameters
        ----------
        tolerance: float, optional
            Intersection tolerance.
        use_absolute_tolerance: bool, optional
            True if tolerance provided is absolute value.
        remesh: bool, optional
            Local remesh at the intersection.
        collapse_feature_angle: float, optional
            Angle to preserve features while performing collapse in improve operation.
        collapse_target_skewness: float, optional
            Perform collapse on faces with skewness above the provided target skewness.
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
        if self._collapse_feature_angle is not None:
            json_data["collapseFeatureAngle"] = self._collapse_feature_angle
        if self._collapse_target_skewness is not None:
            json_data["collapseTargetSkewness"] = self._collapse_target_skewness
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "tolerance :  %s\nuse_absolute_tolerance :  %s\nremesh :  %s\ncollapse_feature_angle :  %s\ncollapse_target_skewness :  %s" % (self._tolerance, self._use_absolute_tolerance, self._remesh, self._collapse_feature_angle, self._collapse_target_skewness)
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

    @property
    def collapse_feature_angle(self) -> float:
        """Angle to preserve features while performing collapse in improve operation.
        """
        return self._collapse_feature_angle

    @collapse_feature_angle.setter
    def collapse_feature_angle(self, value: float):
        self._collapse_feature_angle = value

    @property
    def collapse_target_skewness(self) -> float:
        """Perform collapse on faces with skewness above the provided target skewness.
        """
        return self._collapse_target_skewness

    @collapse_target_skewness.setter
    def collapse_target_skewness(self, value: float):
        self._collapse_target_skewness = value

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

class MergeBoundaryNodesParams(CoreObject):
    """Parameters used for the merge boundary nodes operation.
    """
    _default_params = {}

    def __initialize(
            self,
            tolerance: float,
            use_absolute_tolerance: bool,
            merge_node_type: MergeNodeType):
        self._tolerance = tolerance
        self._use_absolute_tolerance = use_absolute_tolerance
        self._merge_node_type = MergeNodeType(merge_node_type)

    def __init__(
            self,
            model: CommunicationManager=None,
            tolerance: float = None,
            use_absolute_tolerance: bool = None,
            merge_node_type: MergeNodeType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MergeBoundaryNodesParams.

        Parameters
        ----------
        model: Model
            Model to create a MergeBoundaryNodesParams object with default parameters.
        tolerance: float, optional
        use_absolute_tolerance: bool, optional
        merge_node_type: MergeNodeType, optional
        json_data: dict, optional
            JSON dictionary to create a MergeBoundaryNodesParams object with provided parameters.

        Examples
        --------
        >>> merge_boundary_nodes_params = prime.MergeBoundaryNodesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["tolerance"] if "tolerance" in json_data else None,
                json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None,
                MergeNodeType(json_data["mergeNodeType"] if "mergeNodeType" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [tolerance, use_absolute_tolerance, merge_node_type])
            if all_field_specified:
                self.__initialize(
                    tolerance,
                    use_absolute_tolerance,
                    merge_node_type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MergeBoundaryNodesParams")
                    json_data = param_json["MergeBoundaryNodesParams"] if "MergeBoundaryNodesParams" in param_json else {}
                    self.__initialize(
                        tolerance if tolerance is not None else ( MergeBoundaryNodesParams._default_params["tolerance"] if "tolerance" in MergeBoundaryNodesParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( MergeBoundaryNodesParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in MergeBoundaryNodesParams._default_params else (json_data["useAbsoluteTolerance"] if "useAbsoluteTolerance" in json_data else None)),
                        merge_node_type if merge_node_type is not None else ( MergeBoundaryNodesParams._default_params["merge_node_type"] if "merge_node_type" in MergeBoundaryNodesParams._default_params else MergeNodeType(json_data["mergeNodeType"] if "mergeNodeType" in json_data else None)))
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
            merge_node_type: MergeNodeType = None):
        """Set the default values of MergeBoundaryNodesParams.

        Parameters
        ----------
        tolerance: float, optional
        use_absolute_tolerance: bool, optional
        merge_node_type: MergeNodeType, optional
        """
        args = locals()
        [MergeBoundaryNodesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergeBoundaryNodesParams.

        Examples
        --------
        >>> MergeBoundaryNodesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergeBoundaryNodesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._tolerance is not None:
            json_data["tolerance"] = self._tolerance
        if self._use_absolute_tolerance is not None:
            json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
        if self._merge_node_type is not None:
            json_data["mergeNodeType"] = self._merge_node_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "tolerance :  %s\nuse_absolute_tolerance :  %s\nmerge_node_type :  %s" % (self._tolerance, self._use_absolute_tolerance, self._merge_node_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def tolerance(self) -> float:
        """
        Distance tolerance for merging boundary nodes.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        self._tolerance = value

    @property
    def use_absolute_tolerance(self) -> bool:
        """
        Indicates whether the tolerance provided is an absolute value or not.
        """
        return self._use_absolute_tolerance

    @use_absolute_tolerance.setter
    def use_absolute_tolerance(self, value: bool):
        self._use_absolute_tolerance = value

    @property
    def merge_node_type(self) -> MergeNodeType:
        """
        Type depending on the type of nodes to be merged.
        """
        return self._merge_node_type

    @merge_node_type.setter
    def merge_node_type(self, value: MergeNodeType):
        self._merge_node_type = value

class MergeBoundaryNodesResults(CoreObject):
    """Results associated with the merge nodes operation.
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
        """Initializes the MergeBoundaryNodesResults.

        Parameters
        ----------
        model: Model
            Model to create a MergeBoundaryNodesResults object with default parameters.
        error_code: ErrorCode, optional
            Error Code associated with failure of merge nodes operation.
        json_data: dict, optional
            JSON dictionary to create a MergeBoundaryNodesResults object with provided parameters.

        Examples
        --------
        >>> merge_boundary_nodes_results = prime.MergeBoundaryNodesResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "MergeBoundaryNodesResults")
                    json_data = param_json["MergeBoundaryNodesResults"] if "MergeBoundaryNodesResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( MergeBoundaryNodesResults._default_params["error_code"] if "error_code" in MergeBoundaryNodesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of MergeBoundaryNodesResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error Code associated with failure of merge nodes operation.
        """
        args = locals()
        [MergeBoundaryNodesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MergeBoundaryNodesResults.

        Examples
        --------
        >>> MergeBoundaryNodesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MergeBoundaryNodesResults._default_params.items())
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
        """Error Code associated with failure of merge nodes operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
