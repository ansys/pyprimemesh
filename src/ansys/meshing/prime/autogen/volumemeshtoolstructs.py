""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class AutoNodeMoveParams(CoreObject):
    """Parameters used to improve volume mesh by auto node move.
    """
    _default_params = {}

    def __initialize(
            self,
            quality_measure: CellQualityMeasure,
            target_quality: float,
            dihedral_angle: float,
            n_iterations_per_node: int,
            restrict_boundary_nodes_along_surface: bool,
            n_attempts: int):
        self._quality_measure = CellQualityMeasure(quality_measure)
        self._target_quality = target_quality
        self._dihedral_angle = dihedral_angle
        self._n_iterations_per_node = n_iterations_per_node
        self._restrict_boundary_nodes_along_surface = restrict_boundary_nodes_along_surface
        self._n_attempts = n_attempts

    def __init__(
            self,
            model: CommunicationManager=None,
            quality_measure: CellQualityMeasure = None,
            target_quality: float = None,
            dihedral_angle: float = None,
            n_iterations_per_node: int = None,
            restrict_boundary_nodes_along_surface: bool = None,
            n_attempts: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the AutoNodeMoveParams.

        Parameters
        ----------
        model: Model
            Model to create a AutoNodeMoveParams object with default parameters.
        quality_measure: CellQualityMeasure, optional
            Specify cell quality measure to be used for volume mesh improvement. The default value for cell quality measure is skewness.
        target_quality: float, optional
            Specify target quality used for the mesh improvement based on specified quality measure.
        dihedral_angle: float, optional
            Dihedral angle used to mantain features of boundary face zonelets.
        n_iterations_per_node: int, optional
            Number of iterations per node to be moved.
        restrict_boundary_nodes_along_surface: bool, optional
            Option to restrict the movement of the boundary node to the plane containing the boundary faces sharing the boundary node.
        n_attempts: int, optional
            Number of attempts to improve specified quality measure by node movement.
        json_data: dict, optional
            JSON dictionary to create a AutoNodeMoveParams object with provided parameters.

        Examples
        --------
        >>> auto_node_move_params = prime.AutoNodeMoveParams(model = model)
        """
        if json_data:
            self.__initialize(
                CellQualityMeasure(json_data["qualityMeasure"] if "qualityMeasure" in json_data else None),
                json_data["targetQuality"] if "targetQuality" in json_data else None,
                json_data["dihedralAngle"] if "dihedralAngle" in json_data else None,
                json_data["nIterationsPerNode"] if "nIterationsPerNode" in json_data else None,
                json_data["restrictBoundaryNodesAlongSurface"] if "restrictBoundaryNodesAlongSurface" in json_data else None,
                json_data["nAttempts"] if "nAttempts" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [quality_measure, target_quality, dihedral_angle, n_iterations_per_node, restrict_boundary_nodes_along_surface, n_attempts])
            if all_field_specified:
                self.__initialize(
                    quality_measure,
                    target_quality,
                    dihedral_angle,
                    n_iterations_per_node,
                    restrict_boundary_nodes_along_surface,
                    n_attempts)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "AutoNodeMoveParams")
                    json_data = param_json["AutoNodeMoveParams"] if "AutoNodeMoveParams" in param_json else {}
                    self.__initialize(
                        quality_measure if quality_measure is not None else ( AutoNodeMoveParams._default_params["quality_measure"] if "quality_measure" in AutoNodeMoveParams._default_params else CellQualityMeasure(json_data["qualityMeasure"] if "qualityMeasure" in json_data else None)),
                        target_quality if target_quality is not None else ( AutoNodeMoveParams._default_params["target_quality"] if "target_quality" in AutoNodeMoveParams._default_params else (json_data["targetQuality"] if "targetQuality" in json_data else None)),
                        dihedral_angle if dihedral_angle is not None else ( AutoNodeMoveParams._default_params["dihedral_angle"] if "dihedral_angle" in AutoNodeMoveParams._default_params else (json_data["dihedralAngle"] if "dihedralAngle" in json_data else None)),
                        n_iterations_per_node if n_iterations_per_node is not None else ( AutoNodeMoveParams._default_params["n_iterations_per_node"] if "n_iterations_per_node" in AutoNodeMoveParams._default_params else (json_data["nIterationsPerNode"] if "nIterationsPerNode" in json_data else None)),
                        restrict_boundary_nodes_along_surface if restrict_boundary_nodes_along_surface is not None else ( AutoNodeMoveParams._default_params["restrict_boundary_nodes_along_surface"] if "restrict_boundary_nodes_along_surface" in AutoNodeMoveParams._default_params else (json_data["restrictBoundaryNodesAlongSurface"] if "restrictBoundaryNodesAlongSurface" in json_data else None)),
                        n_attempts if n_attempts is not None else ( AutoNodeMoveParams._default_params["n_attempts"] if "n_attempts" in AutoNodeMoveParams._default_params else (json_data["nAttempts"] if "nAttempts" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            quality_measure: CellQualityMeasure = None,
            target_quality: float = None,
            dihedral_angle: float = None,
            n_iterations_per_node: int = None,
            restrict_boundary_nodes_along_surface: bool = None,
            n_attempts: int = None):
        """Set the default values of AutoNodeMoveParams.

        Parameters
        ----------
        quality_measure: CellQualityMeasure, optional
            Specify cell quality measure to be used for volume mesh improvement. The default value for cell quality measure is skewness.
        target_quality: float, optional
            Specify target quality used for the mesh improvement based on specified quality measure.
        dihedral_angle: float, optional
            Dihedral angle used to mantain features of boundary face zonelets.
        n_iterations_per_node: int, optional
            Number of iterations per node to be moved.
        restrict_boundary_nodes_along_surface: bool, optional
            Option to restrict the movement of the boundary node to the plane containing the boundary faces sharing the boundary node.
        n_attempts: int, optional
            Number of attempts to improve specified quality measure by node movement.
        """
        args = locals()
        [AutoNodeMoveParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of AutoNodeMoveParams.

        Examples
        --------
        >>> AutoNodeMoveParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AutoNodeMoveParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._quality_measure is not None:
            json_data["qualityMeasure"] = self._quality_measure
        if self._target_quality is not None:
            json_data["targetQuality"] = self._target_quality
        if self._dihedral_angle is not None:
            json_data["dihedralAngle"] = self._dihedral_angle
        if self._n_iterations_per_node is not None:
            json_data["nIterationsPerNode"] = self._n_iterations_per_node
        if self._restrict_boundary_nodes_along_surface is not None:
            json_data["restrictBoundaryNodesAlongSurface"] = self._restrict_boundary_nodes_along_surface
        if self._n_attempts is not None:
            json_data["nAttempts"] = self._n_attempts
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "quality_measure :  %s\ntarget_quality :  %s\ndihedral_angle :  %s\nn_iterations_per_node :  %s\nrestrict_boundary_nodes_along_surface :  %s\nn_attempts :  %s" % (self._quality_measure, self._target_quality, self._dihedral_angle, self._n_iterations_per_node, self._restrict_boundary_nodes_along_surface, self._n_attempts)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def quality_measure(self) -> CellQualityMeasure:
        """Specify cell quality measure to be used for volume mesh improvement. The default value for cell quality measure is skewness.
        """
        return self._quality_measure

    @quality_measure.setter
    def quality_measure(self, value: CellQualityMeasure):
        self._quality_measure = value

    @property
    def target_quality(self) -> float:
        """Specify target quality used for the mesh improvement based on specified quality measure.
        """
        return self._target_quality

    @target_quality.setter
    def target_quality(self, value: float):
        self._target_quality = value

    @property
    def dihedral_angle(self) -> float:
        """Dihedral angle used to mantain features of boundary face zonelets.
        """
        return self._dihedral_angle

    @dihedral_angle.setter
    def dihedral_angle(self, value: float):
        self._dihedral_angle = value

    @property
    def n_iterations_per_node(self) -> int:
        """Number of iterations per node to be moved.
        """
        return self._n_iterations_per_node

    @n_iterations_per_node.setter
    def n_iterations_per_node(self, value: int):
        self._n_iterations_per_node = value

    @property
    def restrict_boundary_nodes_along_surface(self) -> bool:
        """Option to restrict the movement of the boundary node to the plane containing the boundary faces sharing the boundary node.
        """
        return self._restrict_boundary_nodes_along_surface

    @restrict_boundary_nodes_along_surface.setter
    def restrict_boundary_nodes_along_surface(self, value: bool):
        self._restrict_boundary_nodes_along_surface = value

    @property
    def n_attempts(self) -> int:
        """Number of attempts to improve specified quality measure by node movement.
        """
        return self._n_attempts

    @n_attempts.setter
    def n_attempts(self, value: int):
        self._n_attempts = value

class CheckMeshParams(CoreObject):
    """Parameters used to check mesh.
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
        """Initializes the CheckMeshParams.

        Parameters
        ----------
        model: Model
            Model to create a CheckMeshParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a CheckMeshParams object with provided parameters.

        Examples
        --------
        >>> check_mesh_params = prime.CheckMeshParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "CheckMeshParams")
                    json_data = param_json["CheckMeshParams"] if "CheckMeshParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of CheckMeshParams.

        """
        args = locals()
        [CheckMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CheckMeshParams.

        Examples
        --------
        >>> CheckMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CheckMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class VolumeMeshToolResults(CoreObject):
    """Result associated with the volume mesh tool operation.
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
        """Initializes the VolumeMeshToolResults.

        Parameters
        ----------
        model: Model
            Model to create a VolumeMeshToolResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the volume mesh tool operation.
        json_data: dict, optional
            JSON dictionary to create a VolumeMeshToolResults object with provided parameters.

        Examples
        --------
        >>> volume_mesh_tool_results = prime.VolumeMeshToolResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["error_code"] if "error_code" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumeMeshToolResults")
                    json_data = param_json["VolumeMeshToolResults"] if "VolumeMeshToolResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( VolumeMeshToolResults._default_params["error_code"] if "error_code" in VolumeMeshToolResults._default_params else ErrorCode(json_data["error_code"] if "error_code" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of VolumeMeshToolResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the volume mesh tool operation.
        """
        args = locals()
        [VolumeMeshToolResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumeMeshToolResults.

        Examples
        --------
        >>> VolumeMeshToolResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumeMeshToolResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["error_code"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the volume mesh tool operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class CheckMeshResults(CoreObject):
    """Result associated with the check mesh operation.
    """
    _default_params = {}

    def __initialize(
            self,
            has_non_positive_volumes: bool,
            has_non_positive_areas: bool,
            has_invalid_shape: bool,
            has_left_handed_faces: bool,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._has_non_positive_volumes = has_non_positive_volumes
        self._has_non_positive_areas = has_non_positive_areas
        self._has_invalid_shape = has_invalid_shape
        self._has_left_handed_faces = has_left_handed_faces
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            has_non_positive_volumes: bool = None,
            has_non_positive_areas: bool = None,
            has_invalid_shape: bool = None,
            has_left_handed_faces: bool = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CheckMeshResults.

        Parameters
        ----------
        model: Model
            Model to create a CheckMeshResults object with default parameters.
        has_non_positive_volumes: bool, optional
            Indicates whether mesh has non positive volumes.
        has_non_positive_areas: bool, optional
            Indicates whether mesh has non positive areas.
        has_invalid_shape: bool, optional
            Indicates whether mesh has invalid shape.
        has_left_handed_faces: bool, optional
            Indicates whether mesh has left handed faces.
        error_code: ErrorCode, optional
            Error code associated with the check grid operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the check grid operation.
        json_data: dict, optional
            JSON dictionary to create a CheckMeshResults object with provided parameters.

        Examples
        --------
        >>> check_mesh_results = prime.CheckMeshResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["hasNonPositiveVolumes"] if "hasNonPositiveVolumes" in json_data else None,
                json_data["hasNonPositiveAreas"] if "hasNonPositiveAreas" in json_data else None,
                json_data["hasInvalidShape"] if "hasInvalidShape" in json_data else None,
                json_data["hasLeftHandedFaces"] if "hasLeftHandedFaces" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [has_non_positive_volumes, has_non_positive_areas, has_invalid_shape, has_left_handed_faces, error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    has_non_positive_volumes,
                    has_non_positive_areas,
                    has_invalid_shape,
                    has_left_handed_faces,
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CheckMeshResults")
                    json_data = param_json["CheckMeshResults"] if "CheckMeshResults" in param_json else {}
                    self.__initialize(
                        has_non_positive_volumes if has_non_positive_volumes is not None else ( CheckMeshResults._default_params["has_non_positive_volumes"] if "has_non_positive_volumes" in CheckMeshResults._default_params else (json_data["hasNonPositiveVolumes"] if "hasNonPositiveVolumes" in json_data else None)),
                        has_non_positive_areas if has_non_positive_areas is not None else ( CheckMeshResults._default_params["has_non_positive_areas"] if "has_non_positive_areas" in CheckMeshResults._default_params else (json_data["hasNonPositiveAreas"] if "hasNonPositiveAreas" in json_data else None)),
                        has_invalid_shape if has_invalid_shape is not None else ( CheckMeshResults._default_params["has_invalid_shape"] if "has_invalid_shape" in CheckMeshResults._default_params else (json_data["hasInvalidShape"] if "hasInvalidShape" in json_data else None)),
                        has_left_handed_faces if has_left_handed_faces is not None else ( CheckMeshResults._default_params["has_left_handed_faces"] if "has_left_handed_faces" in CheckMeshResults._default_params else (json_data["hasLeftHandedFaces"] if "hasLeftHandedFaces" in json_data else None)),
                        error_code if error_code is not None else ( CheckMeshResults._default_params["error_code"] if "error_code" in CheckMeshResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( CheckMeshResults._default_params["warning_codes"] if "warning_codes" in CheckMeshResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            has_non_positive_volumes: bool = None,
            has_non_positive_areas: bool = None,
            has_invalid_shape: bool = None,
            has_left_handed_faces: bool = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of CheckMeshResults.

        Parameters
        ----------
        has_non_positive_volumes: bool, optional
            Indicates whether mesh has non positive volumes.
        has_non_positive_areas: bool, optional
            Indicates whether mesh has non positive areas.
        has_invalid_shape: bool, optional
            Indicates whether mesh has invalid shape.
        has_left_handed_faces: bool, optional
            Indicates whether mesh has left handed faces.
        error_code: ErrorCode, optional
            Error code associated with the check grid operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the check grid operation.
        """
        args = locals()
        [CheckMeshResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CheckMeshResults.

        Examples
        --------
        >>> CheckMeshResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CheckMeshResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._has_non_positive_volumes is not None:
            json_data["hasNonPositiveVolumes"] = self._has_non_positive_volumes
        if self._has_non_positive_areas is not None:
            json_data["hasNonPositiveAreas"] = self._has_non_positive_areas
        if self._has_invalid_shape is not None:
            json_data["hasInvalidShape"] = self._has_invalid_shape
        if self._has_left_handed_faces is not None:
            json_data["hasLeftHandedFaces"] = self._has_left_handed_faces
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "has_non_positive_volumes :  %s\nhas_non_positive_areas :  %s\nhas_invalid_shape :  %s\nhas_left_handed_faces :  %s\nerror_code :  %s\nwarning_codes :  %s" % (self._has_non_positive_volumes, self._has_non_positive_areas, self._has_invalid_shape, self._has_left_handed_faces, self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def has_non_positive_volumes(self) -> bool:
        """Indicates whether mesh has non positive volumes.
        """
        return self._has_non_positive_volumes

    @has_non_positive_volumes.setter
    def has_non_positive_volumes(self, value: bool):
        self._has_non_positive_volumes = value

    @property
    def has_non_positive_areas(self) -> bool:
        """Indicates whether mesh has non positive areas.
        """
        return self._has_non_positive_areas

    @has_non_positive_areas.setter
    def has_non_positive_areas(self, value: bool):
        self._has_non_positive_areas = value

    @property
    def has_invalid_shape(self) -> bool:
        """Indicates whether mesh has invalid shape.
        """
        return self._has_invalid_shape

    @has_invalid_shape.setter
    def has_invalid_shape(self, value: bool):
        self._has_invalid_shape = value

    @property
    def has_left_handed_faces(self) -> bool:
        """Indicates whether mesh has left handed faces.
        """
        return self._has_left_handed_faces

    @has_left_handed_faces.setter
    def has_left_handed_faces(self, value: bool):
        self._has_left_handed_faces = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the check grid operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the check grid operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value
