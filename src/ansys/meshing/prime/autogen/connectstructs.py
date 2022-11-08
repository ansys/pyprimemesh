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

class MatchNodesOption(enum.IntEnum):
    """Type to specify treatment of matched nodes. This is for internal use only.
    """
    TRIMONESIDE = 3
    """Delete the matching faces on one side and merge the matching nodes at mid location (works only within a single part). This is for internal use only."""
    TRIMTWOSIDES = 4
    """Delete the matching faces on both sides and merge the matching nodes at mid location (works only within a single part). This is for internal use only."""

class ConnectResults(CoreObject):
    """Results associated with the connection operations.
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
        """Initializes the ConnectResults.

        Parameters
        ----------
        model: Model
            Model to create a ConnectResults object with default parameters.
        error_code: ErrorCode, optional
            Error Code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a ConnectResults object with provided parameters.

        Examples
        --------
        >>> connect_results = prime.ConnectResults(model = model)
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
                    json_data = model._communicator.initialize_params(model, "ConnectResults")["ConnectResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( ConnectResults._default_params["error_code"] if "error_code" in ConnectResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of ConnectResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error Code associated with failure of operation.
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
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
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
                json_data["tolerance"],
                json_data["useAbsoluteTolerance"],
                json_data["remesh"])
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
                    json_data = model._communicator.initialize_params(model, "IntersectParams")["IntersectParams"]
                    self.__initialize(
                        tolerance if tolerance is not None else ( IntersectParams._default_params["tolerance"] if "tolerance" in IntersectParams._default_params else json_data["tolerance"]),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( IntersectParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in IntersectParams._default_params else json_data["useAbsoluteTolerance"]),
                        remesh if remesh is not None else ( IntersectParams._default_params["remesh"] if "remesh" in IntersectParams._default_params else json_data["remesh"]))
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
        json_data["tolerance"] = self._tolerance
        json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
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
                json_data["tolerance"],
                json_data["useAbsoluteTolerance"],
                json_data["remesh"],
                json_data["matchAngle"],
                json_data["overlapZoneName"])
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
                    json_data = model._communicator.initialize_params(model, "JoinParams")["JoinParams"]
                    self.__initialize(
                        tolerance if tolerance is not None else ( JoinParams._default_params["tolerance"] if "tolerance" in JoinParams._default_params else json_data["tolerance"]),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( JoinParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in JoinParams._default_params else json_data["useAbsoluteTolerance"]),
                        remesh if remesh is not None else ( JoinParams._default_params["remesh"] if "remesh" in JoinParams._default_params else json_data["remesh"]),
                        match_angle if match_angle is not None else ( JoinParams._default_params["match_angle"] if "match_angle" in JoinParams._default_params else json_data["matchAngle"]),
                        overlap_zone_name if overlap_zone_name is not None else ( JoinParams._default_params["overlap_zone_name"] if "overlap_zone_name" in JoinParams._default_params else json_data["overlapZoneName"]))
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
        json_data["tolerance"] = self._tolerance
        json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
        json_data["remesh"] = self._remesh
        json_data["matchAngle"] = self._match_angle
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
                json_data["tolerance"],
                json_data["useAbsoluteTolerance"],
                json_data["remesh"],
                json_data["enableMultiThreading"],
                StitchType(json_data["type"]))
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
                    json_data = model._communicator.initialize_params(model, "StitchParams")["StitchParams"]
                    self.__initialize(
                        tolerance if tolerance is not None else ( StitchParams._default_params["tolerance"] if "tolerance" in StitchParams._default_params else json_data["tolerance"]),
                        use_absolute_tolerance if use_absolute_tolerance is not None else ( StitchParams._default_params["use_absolute_tolerance"] if "use_absolute_tolerance" in StitchParams._default_params else json_data["useAbsoluteTolerance"]),
                        remesh if remesh is not None else ( StitchParams._default_params["remesh"] if "remesh" in StitchParams._default_params else json_data["remesh"]),
                        enable_multi_threading if enable_multi_threading is not None else ( StitchParams._default_params["enable_multi_threading"] if "enable_multi_threading" in StitchParams._default_params else json_data["enableMultiThreading"]),
                        type if type is not None else ( StitchParams._default_params["type"] if "type" in StitchParams._default_params else StitchType(json_data["type"])))
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
        json_data["tolerance"] = self._tolerance
        json_data["useAbsoluteTolerance"] = self._use_absolute_tolerance
        json_data["remesh"] = self._remesh
        json_data["enableMultiThreading"] = self._enable_multi_threading
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
    """Parameter to match surface mesh. This is for internal use only.
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
                    json_data = model._communicator.initialize_params(model, "MeshMatchParams")["MeshMatchParams"]
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
