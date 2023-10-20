""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class ControlPointSelection(enum.IntEnum):
    """Control point selection type.
    """
    MANUAL = 0
    """Manual Spline control point selection."""
    PROGRAMCONTROLLED = 1
    """Program controlled spline control point selection."""

class SplineRefinementType(enum.IntEnum):
    """Type of spline refinement. Currently, supports h-refinement and p-refinement.
    """
    H = 0
    """H refinement of spline."""
    P = 1
    """P refinement of spline."""

class SplineFeatureCaptureType(enum.IntEnum):
    """Options to capture features in spline.
    """
    IGNORE = 0
    """Ignores feature capture in spline."""
    BYANGLE = 1
    """Uses angle for capturing features in spline."""
    BYEDGES = 2
    """Use edges for capturing features in spline."""

class IGAResults(CoreObject):
    """Results of IGA operations.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_code: WarningCode,
            spline_ids: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._warning_code = WarningCode(warning_code)
        self._spline_ids = spline_ids if isinstance(spline_ids, np.ndarray) else np.array(spline_ids, dtype=np.int32) if spline_ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_code: WarningCode = None,
            spline_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the IGAResults.

        Parameters
        ----------
        model: Model
            Model to create a IGAResults object with default parameters.
        error_code: ErrorCode, optional
            Error code if IGA operation is unsuccessful.
        warning_code: WarningCode, optional
            Warning code if IGA operation is partially successful.
        spline_ids: Iterable[int], optional
            Ids of the created spline.
        json_data: dict, optional
            JSON dictionary to create a IGAResults object with provided parameters.

        Examples
        --------
        >>> iga_results = prime.IGAResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                WarningCode(json_data["warningCode"] if "warningCode" in json_data else None),
                json_data["splineIds"] if "splineIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_code, spline_ids])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_code,
                    spline_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "IGAResults")
                    json_data = param_json["IGAResults"] if "IGAResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( IGAResults._default_params["error_code"] if "error_code" in IGAResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_code if warning_code is not None else ( IGAResults._default_params["warning_code"] if "warning_code" in IGAResults._default_params else WarningCode(json_data["warningCode"] if "warningCode" in json_data else None)),
                        spline_ids if spline_ids is not None else ( IGAResults._default_params["spline_ids"] if "spline_ids" in IGAResults._default_params else (json_data["splineIds"] if "splineIds" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_code: WarningCode = None,
            spline_ids: Iterable[int] = None):
        """Set the default values of IGAResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if IGA operation is unsuccessful.
        warning_code: WarningCode, optional
            Warning code if IGA operation is partially successful.
        spline_ids: Iterable[int], optional
            Ids of the created spline.
        """
        args = locals()
        [IGAResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of IGAResults.

        Examples
        --------
        >>> IGAResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in IGAResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_code is not None:
            json_data["warningCode"] = self._warning_code
        if self._spline_ids is not None:
            json_data["splineIds"] = self._spline_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_code :  %s\nspline_ids :  %s" % (self._error_code, self._warning_code, self._spline_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code if IGA operation is unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_code(self) -> WarningCode:
        """Warning code if IGA operation is partially successful.
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, value: WarningCode):
        self._warning_code = value

    @property
    def spline_ids(self) -> Iterable[int]:
        """Ids of the created spline.
        """
        return self._spline_ids

    @spline_ids.setter
    def spline_ids(self, value: Iterable[int]):
        self._spline_ids = value

class IGASpline(CoreObject):
    """Information of the spline.
    """
    _default_params = {}

    def __initialize(
            self,
            id: int):
        self._id = id

    def __init__(
            self,
            model: CommunicationManager=None,
            id: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the IGASpline.

        Parameters
        ----------
        model: Model
            Model to create a IGASpline object with default parameters.
        id: int, optional
            Unique id of the spline.
        json_data: dict, optional
            JSON dictionary to create a IGASpline object with provided parameters.

        Examples
        --------
        >>> iga_spline = prime.IGASpline(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["id"] if "id" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [id])
            if all_field_specified:
                self.__initialize(
                    id)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "IGASpline")
                    json_data = param_json["IGASpline"] if "IGASpline" in param_json else {}
                    self.__initialize(
                        id if id is not None else ( IGASpline._default_params["id"] if "id" in IGASpline._default_params else (json_data["id"] if "id" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            id: int = None):
        """Set the default values of IGASpline.

        Parameters
        ----------
        id: int, optional
            Unique id of the spline.
        """
        args = locals()
        [IGASpline._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of IGASpline.

        Examples
        --------
        >>> IGASpline.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in IGASpline._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._id is not None:
            json_data["id"] = self._id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "id :  %s" % (self._id)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def id(self) -> int:
        """Unique id of the spline.
        """
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

class IGAUnstructuredSplineSurf(CoreObject):
    """Information of unstructured spline surface.
    """
    _default_params = {}

    def __initialize(
            self,
            id: int,
            spline_refinement_level: int,
            control_points: Iterable[float],
            spline_points: Iterable[float],
            bad_spline_points_indices: Iterable[int],
            deviation_array: Iterable[float],
            invalid_jacobian_elements_count: int,
            average_mesh_size: float,
            elements_count: int,
            shell_thickness: float):
        self._id = id
        self._spline_refinement_level = spline_refinement_level
        self._control_points = control_points if isinstance(control_points, np.ndarray) else np.array(control_points, dtype=np.double) if control_points is not None else None
        self._spline_points = spline_points if isinstance(spline_points, np.ndarray) else np.array(spline_points, dtype=np.double) if spline_points is not None else None
        self._bad_spline_points_indices = bad_spline_points_indices if isinstance(bad_spline_points_indices, np.ndarray) else np.array(bad_spline_points_indices, dtype=np.int32) if bad_spline_points_indices is not None else None
        self._deviation_array = deviation_array if isinstance(deviation_array, np.ndarray) else np.array(deviation_array, dtype=np.double) if deviation_array is not None else None
        self._invalid_jacobian_elements_count = invalid_jacobian_elements_count
        self._average_mesh_size = average_mesh_size
        self._elements_count = elements_count
        self._shell_thickness = shell_thickness

    def __init__(
            self,
            model: CommunicationManager=None,
            id: int = None,
            spline_refinement_level: int = None,
            control_points: Iterable[float] = None,
            spline_points: Iterable[float] = None,
            bad_spline_points_indices: Iterable[int] = None,
            deviation_array: Iterable[float] = None,
            invalid_jacobian_elements_count: int = None,
            average_mesh_size: float = None,
            elements_count: int = None,
            shell_thickness: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the IGAUnstructuredSplineSurf.

        Parameters
        ----------
        model: Model
            Model to create a IGAUnstructuredSplineSurf object with default parameters.
        id: int, optional
            Id of the unstructured spline surface.
        spline_refinement_level: int, optional
            Refinement level for rendering of spline points.
        control_points: Iterable[float], optional
            Coordinates of the control points of the spline.
        spline_points: Iterable[float], optional
            Coordinates of the spline points.
        bad_spline_points_indices: Iterable[int], optional
            Node indices in the spline points list which has negative jacobian value.
        deviation_array: Iterable[float], optional
            Deviation value from the spline point to the model geometry.
        invalid_jacobian_elements_count: int, optional
            Count of elements with negative jacobian.
        average_mesh_size: float, optional
            Reference length to compute deviation.
        elements_count: int, optional
            Count of shell elements.
        shell_thickness: float, optional
            Thickness of shell.
        json_data: dict, optional
            JSON dictionary to create a IGAUnstructuredSplineSurf object with provided parameters.

        Examples
        --------
        >>> iga_unstructured_spline_surf = prime.IGAUnstructuredSplineSurf(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["id"] if "id" in json_data else None,
                json_data["splineRefinementLevel"] if "splineRefinementLevel" in json_data else None,
                json_data["controlPoints"] if "controlPoints" in json_data else None,
                json_data["splinePoints"] if "splinePoints" in json_data else None,
                json_data["badSplinePointsIndices"] if "badSplinePointsIndices" in json_data else None,
                json_data["deviationArray"] if "deviationArray" in json_data else None,
                json_data["invalidJacobianElementsCount"] if "invalidJacobianElementsCount" in json_data else None,
                json_data["averageMeshSize"] if "averageMeshSize" in json_data else None,
                json_data["elementsCount"] if "elementsCount" in json_data else None,
                json_data["shellThickness"] if "shellThickness" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [id, spline_refinement_level, control_points, spline_points, bad_spline_points_indices, deviation_array, invalid_jacobian_elements_count, average_mesh_size, elements_count, shell_thickness])
            if all_field_specified:
                self.__initialize(
                    id,
                    spline_refinement_level,
                    control_points,
                    spline_points,
                    bad_spline_points_indices,
                    deviation_array,
                    invalid_jacobian_elements_count,
                    average_mesh_size,
                    elements_count,
                    shell_thickness)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "IGAUnstructuredSplineSurf")
                    json_data = param_json["IGAUnstructuredSplineSurf"] if "IGAUnstructuredSplineSurf" in param_json else {}
                    self.__initialize(
                        id if id is not None else ( IGAUnstructuredSplineSurf._default_params["id"] if "id" in IGAUnstructuredSplineSurf._default_params else (json_data["id"] if "id" in json_data else None)),
                        spline_refinement_level if spline_refinement_level is not None else ( IGAUnstructuredSplineSurf._default_params["spline_refinement_level"] if "spline_refinement_level" in IGAUnstructuredSplineSurf._default_params else (json_data["splineRefinementLevel"] if "splineRefinementLevel" in json_data else None)),
                        control_points if control_points is not None else ( IGAUnstructuredSplineSurf._default_params["control_points"] if "control_points" in IGAUnstructuredSplineSurf._default_params else (json_data["controlPoints"] if "controlPoints" in json_data else None)),
                        spline_points if spline_points is not None else ( IGAUnstructuredSplineSurf._default_params["spline_points"] if "spline_points" in IGAUnstructuredSplineSurf._default_params else (json_data["splinePoints"] if "splinePoints" in json_data else None)),
                        bad_spline_points_indices if bad_spline_points_indices is not None else ( IGAUnstructuredSplineSurf._default_params["bad_spline_points_indices"] if "bad_spline_points_indices" in IGAUnstructuredSplineSurf._default_params else (json_data["badSplinePointsIndices"] if "badSplinePointsIndices" in json_data else None)),
                        deviation_array if deviation_array is not None else ( IGAUnstructuredSplineSurf._default_params["deviation_array"] if "deviation_array" in IGAUnstructuredSplineSurf._default_params else (json_data["deviationArray"] if "deviationArray" in json_data else None)),
                        invalid_jacobian_elements_count if invalid_jacobian_elements_count is not None else ( IGAUnstructuredSplineSurf._default_params["invalid_jacobian_elements_count"] if "invalid_jacobian_elements_count" in IGAUnstructuredSplineSurf._default_params else (json_data["invalidJacobianElementsCount"] if "invalidJacobianElementsCount" in json_data else None)),
                        average_mesh_size if average_mesh_size is not None else ( IGAUnstructuredSplineSurf._default_params["average_mesh_size"] if "average_mesh_size" in IGAUnstructuredSplineSurf._default_params else (json_data["averageMeshSize"] if "averageMeshSize" in json_data else None)),
                        elements_count if elements_count is not None else ( IGAUnstructuredSplineSurf._default_params["elements_count"] if "elements_count" in IGAUnstructuredSplineSurf._default_params else (json_data["elementsCount"] if "elementsCount" in json_data else None)),
                        shell_thickness if shell_thickness is not None else ( IGAUnstructuredSplineSurf._default_params["shell_thickness"] if "shell_thickness" in IGAUnstructuredSplineSurf._default_params else (json_data["shellThickness"] if "shellThickness" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            id: int = None,
            spline_refinement_level: int = None,
            control_points: Iterable[float] = None,
            spline_points: Iterable[float] = None,
            bad_spline_points_indices: Iterable[int] = None,
            deviation_array: Iterable[float] = None,
            invalid_jacobian_elements_count: int = None,
            average_mesh_size: float = None,
            elements_count: int = None,
            shell_thickness: float = None):
        """Set the default values of IGAUnstructuredSplineSurf.

        Parameters
        ----------
        id: int, optional
            Id of the unstructured spline surface.
        spline_refinement_level: int, optional
            Refinement level for rendering of spline points.
        control_points: Iterable[float], optional
            Coordinates of the control points of the spline.
        spline_points: Iterable[float], optional
            Coordinates of the spline points.
        bad_spline_points_indices: Iterable[int], optional
            Node indices in the spline points list which has negative jacobian value.
        deviation_array: Iterable[float], optional
            Deviation value from the spline point to the model geometry.
        invalid_jacobian_elements_count: int, optional
            Count of elements with negative jacobian.
        average_mesh_size: float, optional
            Reference length to compute deviation.
        elements_count: int, optional
            Count of shell elements.
        shell_thickness: float, optional
            Thickness of shell.
        """
        args = locals()
        [IGAUnstructuredSplineSurf._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of IGAUnstructuredSplineSurf.

        Examples
        --------
        >>> IGAUnstructuredSplineSurf.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in IGAUnstructuredSplineSurf._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._id is not None:
            json_data["id"] = self._id
        if self._spline_refinement_level is not None:
            json_data["splineRefinementLevel"] = self._spline_refinement_level
        if self._control_points is not None:
            json_data["controlPoints"] = self._control_points
        if self._spline_points is not None:
            json_data["splinePoints"] = self._spline_points
        if self._bad_spline_points_indices is not None:
            json_data["badSplinePointsIndices"] = self._bad_spline_points_indices
        if self._deviation_array is not None:
            json_data["deviationArray"] = self._deviation_array
        if self._invalid_jacobian_elements_count is not None:
            json_data["invalidJacobianElementsCount"] = self._invalid_jacobian_elements_count
        if self._average_mesh_size is not None:
            json_data["averageMeshSize"] = self._average_mesh_size
        if self._elements_count is not None:
            json_data["elementsCount"] = self._elements_count
        if self._shell_thickness is not None:
            json_data["shellThickness"] = self._shell_thickness
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "id :  %s\nspline_refinement_level :  %s\ncontrol_points :  %s\nspline_points :  %s\nbad_spline_points_indices :  %s\ndeviation_array :  %s\ninvalid_jacobian_elements_count :  %s\naverage_mesh_size :  %s\nelements_count :  %s\nshell_thickness :  %s" % (self._id, self._spline_refinement_level, self._control_points, self._spline_points, self._bad_spline_points_indices, self._deviation_array, self._invalid_jacobian_elements_count, self._average_mesh_size, self._elements_count, self._shell_thickness)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def id(self) -> int:
        """Id of the unstructured spline surface.
        """
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def spline_refinement_level(self) -> int:
        """Refinement level for rendering of spline points.
        """
        return self._spline_refinement_level

    @spline_refinement_level.setter
    def spline_refinement_level(self, value: int):
        self._spline_refinement_level = value

    @property
    def control_points(self) -> Iterable[float]:
        """Coordinates of the control points of the spline.
        """
        return self._control_points

    @control_points.setter
    def control_points(self, value: Iterable[float]):
        self._control_points = value

    @property
    def spline_points(self) -> Iterable[float]:
        """Coordinates of the spline points.
        """
        return self._spline_points

    @spline_points.setter
    def spline_points(self, value: Iterable[float]):
        self._spline_points = value

    @property
    def bad_spline_points_indices(self) -> Iterable[int]:
        """Node indices in the spline points list which has negative jacobian value.
        """
        return self._bad_spline_points_indices

    @bad_spline_points_indices.setter
    def bad_spline_points_indices(self, value: Iterable[int]):
        self._bad_spline_points_indices = value

    @property
    def deviation_array(self) -> Iterable[float]:
        """Deviation value from the spline point to the model geometry.
        """
        return self._deviation_array

    @deviation_array.setter
    def deviation_array(self, value: Iterable[float]):
        self._deviation_array = value

    @property
    def invalid_jacobian_elements_count(self) -> int:
        """Count of elements with negative jacobian.
        """
        return self._invalid_jacobian_elements_count

    @invalid_jacobian_elements_count.setter
    def invalid_jacobian_elements_count(self, value: int):
        self._invalid_jacobian_elements_count = value

    @property
    def average_mesh_size(self) -> float:
        """Reference length to compute deviation.
        """
        return self._average_mesh_size

    @average_mesh_size.setter
    def average_mesh_size(self, value: float):
        self._average_mesh_size = value

    @property
    def elements_count(self) -> int:
        """Count of shell elements.
        """
        return self._elements_count

    @elements_count.setter
    def elements_count(self, value: int):
        self._elements_count = value

    @property
    def shell_thickness(self) -> float:
        """Thickness of shell.
        """
        return self._shell_thickness

    @shell_thickness.setter
    def shell_thickness(self, value: float):
        self._shell_thickness = value

class BoundaryFittedSplineParams(CoreObject):
    """Boundary fitted spline fitting parameters.
    """
    _default_params = {}

    def __initialize(
            self,
            degree_u: int,
            degree_v: int,
            degree_w: int,
            refinement_fraction_u: float,
            refinement_fraction_v: float,
            refinement_fraction_w: float,
            control_points_count_u: int,
            control_points_count_v: int,
            control_points_count_w: int,
            n_refine: int,
            control_point_selection_type: ControlPointSelection):
        self._degree_u = degree_u
        self._degree_v = degree_v
        self._degree_w = degree_w
        self._refinement_fraction_u = refinement_fraction_u
        self._refinement_fraction_v = refinement_fraction_v
        self._refinement_fraction_w = refinement_fraction_w
        self._control_points_count_u = control_points_count_u
        self._control_points_count_v = control_points_count_v
        self._control_points_count_w = control_points_count_w
        self._n_refine = n_refine
        self._control_point_selection_type = ControlPointSelection(control_point_selection_type)

    def __init__(
            self,
            model: CommunicationManager=None,
            degree_u: int = None,
            degree_v: int = None,
            degree_w: int = None,
            refinement_fraction_u: float = None,
            refinement_fraction_v: float = None,
            refinement_fraction_w: float = None,
            control_points_count_u: int = None,
            control_points_count_v: int = None,
            control_points_count_w: int = None,
            n_refine: int = None,
            control_point_selection_type: ControlPointSelection = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the BoundaryFittedSplineParams.

        Parameters
        ----------
        model: Model
            Model to create a BoundaryFittedSplineParams object with default parameters.
        degree_u: int, optional
            Degree of spline in u direction.
        degree_v: int, optional
            Degree of spline in v direction.
        degree_w: int, optional
            Degree of spline in w direction.
        refinement_fraction_u: float, optional
            Fraction of input mesh size that sets the control points size in u direction. This is used in program controlled control points selection mode.
        refinement_fraction_v: float, optional
            Fraction of input mesh size that sets the control points size in v direction. This is used in program controlled control points selection mode.
        refinement_fraction_w: float, optional
            Fraction of input mesh size that sets the control points size in w direction. This is used in program controlled control points selection mode.
        control_points_count_u: int, optional
            Spline control points count in U direction. Used in manual control points selection mode.
        control_points_count_v: int, optional
            Spline control points count in V direction. Used in manual control points selection mode.
        control_points_count_w: int, optional
            Spline control points count in W direction. Used in manual control points selection mode.
        n_refine: int, optional
            Spline refinement level for rendering.
        control_point_selection_type: ControlPointSelection, optional
            Spline control points selection type.
        json_data: dict, optional
            JSON dictionary to create a BoundaryFittedSplineParams object with provided parameters.

        Examples
        --------
        >>> boundary_fitted_spline_params = prime.BoundaryFittedSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["degreeU"] if "degreeU" in json_data else None,
                json_data["degreeV"] if "degreeV" in json_data else None,
                json_data["degreeW"] if "degreeW" in json_data else None,
                json_data["refinementFractionU"] if "refinementFractionU" in json_data else None,
                json_data["refinementFractionV"] if "refinementFractionV" in json_data else None,
                json_data["refinementFractionW"] if "refinementFractionW" in json_data else None,
                json_data["controlPointsCountU"] if "controlPointsCountU" in json_data else None,
                json_data["controlPointsCountV"] if "controlPointsCountV" in json_data else None,
                json_data["controlPointsCountW"] if "controlPointsCountW" in json_data else None,
                json_data["nRefine"] if "nRefine" in json_data else None,
                ControlPointSelection(json_data["controlPointSelectionType"] if "controlPointSelectionType" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [degree_u, degree_v, degree_w, refinement_fraction_u, refinement_fraction_v, refinement_fraction_w, control_points_count_u, control_points_count_v, control_points_count_w, n_refine, control_point_selection_type])
            if all_field_specified:
                self.__initialize(
                    degree_u,
                    degree_v,
                    degree_w,
                    refinement_fraction_u,
                    refinement_fraction_v,
                    refinement_fraction_w,
                    control_points_count_u,
                    control_points_count_v,
                    control_points_count_w,
                    n_refine,
                    control_point_selection_type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "BoundaryFittedSplineParams")
                    json_data = param_json["BoundaryFittedSplineParams"] if "BoundaryFittedSplineParams" in param_json else {}
                    self.__initialize(
                        degree_u if degree_u is not None else ( BoundaryFittedSplineParams._default_params["degree_u"] if "degree_u" in BoundaryFittedSplineParams._default_params else (json_data["degreeU"] if "degreeU" in json_data else None)),
                        degree_v if degree_v is not None else ( BoundaryFittedSplineParams._default_params["degree_v"] if "degree_v" in BoundaryFittedSplineParams._default_params else (json_data["degreeV"] if "degreeV" in json_data else None)),
                        degree_w if degree_w is not None else ( BoundaryFittedSplineParams._default_params["degree_w"] if "degree_w" in BoundaryFittedSplineParams._default_params else (json_data["degreeW"] if "degreeW" in json_data else None)),
                        refinement_fraction_u if refinement_fraction_u is not None else ( BoundaryFittedSplineParams._default_params["refinement_fraction_u"] if "refinement_fraction_u" in BoundaryFittedSplineParams._default_params else (json_data["refinementFractionU"] if "refinementFractionU" in json_data else None)),
                        refinement_fraction_v if refinement_fraction_v is not None else ( BoundaryFittedSplineParams._default_params["refinement_fraction_v"] if "refinement_fraction_v" in BoundaryFittedSplineParams._default_params else (json_data["refinementFractionV"] if "refinementFractionV" in json_data else None)),
                        refinement_fraction_w if refinement_fraction_w is not None else ( BoundaryFittedSplineParams._default_params["refinement_fraction_w"] if "refinement_fraction_w" in BoundaryFittedSplineParams._default_params else (json_data["refinementFractionW"] if "refinementFractionW" in json_data else None)),
                        control_points_count_u if control_points_count_u is not None else ( BoundaryFittedSplineParams._default_params["control_points_count_u"] if "control_points_count_u" in BoundaryFittedSplineParams._default_params else (json_data["controlPointsCountU"] if "controlPointsCountU" in json_data else None)),
                        control_points_count_v if control_points_count_v is not None else ( BoundaryFittedSplineParams._default_params["control_points_count_v"] if "control_points_count_v" in BoundaryFittedSplineParams._default_params else (json_data["controlPointsCountV"] if "controlPointsCountV" in json_data else None)),
                        control_points_count_w if control_points_count_w is not None else ( BoundaryFittedSplineParams._default_params["control_points_count_w"] if "control_points_count_w" in BoundaryFittedSplineParams._default_params else (json_data["controlPointsCountW"] if "controlPointsCountW" in json_data else None)),
                        n_refine if n_refine is not None else ( BoundaryFittedSplineParams._default_params["n_refine"] if "n_refine" in BoundaryFittedSplineParams._default_params else (json_data["nRefine"] if "nRefine" in json_data else None)),
                        control_point_selection_type if control_point_selection_type is not None else ( BoundaryFittedSplineParams._default_params["control_point_selection_type"] if "control_point_selection_type" in BoundaryFittedSplineParams._default_params else ControlPointSelection(json_data["controlPointSelectionType"] if "controlPointSelectionType" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            degree_u: int = None,
            degree_v: int = None,
            degree_w: int = None,
            refinement_fraction_u: float = None,
            refinement_fraction_v: float = None,
            refinement_fraction_w: float = None,
            control_points_count_u: int = None,
            control_points_count_v: int = None,
            control_points_count_w: int = None,
            n_refine: int = None,
            control_point_selection_type: ControlPointSelection = None):
        """Set the default values of BoundaryFittedSplineParams.

        Parameters
        ----------
        degree_u: int, optional
            Degree of spline in u direction.
        degree_v: int, optional
            Degree of spline in v direction.
        degree_w: int, optional
            Degree of spline in w direction.
        refinement_fraction_u: float, optional
            Fraction of input mesh size that sets the control points size in u direction. This is used in program controlled control points selection mode.
        refinement_fraction_v: float, optional
            Fraction of input mesh size that sets the control points size in v direction. This is used in program controlled control points selection mode.
        refinement_fraction_w: float, optional
            Fraction of input mesh size that sets the control points size in w direction. This is used in program controlled control points selection mode.
        control_points_count_u: int, optional
            Spline control points count in U direction. Used in manual control points selection mode.
        control_points_count_v: int, optional
            Spline control points count in V direction. Used in manual control points selection mode.
        control_points_count_w: int, optional
            Spline control points count in W direction. Used in manual control points selection mode.
        n_refine: int, optional
            Spline refinement level for rendering.
        control_point_selection_type: ControlPointSelection, optional
            Spline control points selection type.
        """
        args = locals()
        [BoundaryFittedSplineParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of BoundaryFittedSplineParams.

        Examples
        --------
        >>> BoundaryFittedSplineParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in BoundaryFittedSplineParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._degree_u is not None:
            json_data["degreeU"] = self._degree_u
        if self._degree_v is not None:
            json_data["degreeV"] = self._degree_v
        if self._degree_w is not None:
            json_data["degreeW"] = self._degree_w
        if self._refinement_fraction_u is not None:
            json_data["refinementFractionU"] = self._refinement_fraction_u
        if self._refinement_fraction_v is not None:
            json_data["refinementFractionV"] = self._refinement_fraction_v
        if self._refinement_fraction_w is not None:
            json_data["refinementFractionW"] = self._refinement_fraction_w
        if self._control_points_count_u is not None:
            json_data["controlPointsCountU"] = self._control_points_count_u
        if self._control_points_count_v is not None:
            json_data["controlPointsCountV"] = self._control_points_count_v
        if self._control_points_count_w is not None:
            json_data["controlPointsCountW"] = self._control_points_count_w
        if self._n_refine is not None:
            json_data["nRefine"] = self._n_refine
        if self._control_point_selection_type is not None:
            json_data["controlPointSelectionType"] = self._control_point_selection_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "degree_u :  %s\ndegree_v :  %s\ndegree_w :  %s\nrefinement_fraction_u :  %s\nrefinement_fraction_v :  %s\nrefinement_fraction_w :  %s\ncontrol_points_count_u :  %s\ncontrol_points_count_v :  %s\ncontrol_points_count_w :  %s\nn_refine :  %s\ncontrol_point_selection_type :  %s" % (self._degree_u, self._degree_v, self._degree_w, self._refinement_fraction_u, self._refinement_fraction_v, self._refinement_fraction_w, self._control_points_count_u, self._control_points_count_v, self._control_points_count_w, self._n_refine, self._control_point_selection_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def degree_u(self) -> int:
        """Degree of spline in u direction.
        """
        return self._degree_u

    @degree_u.setter
    def degree_u(self, value: int):
        self._degree_u = value

    @property
    def degree_v(self) -> int:
        """Degree of spline in v direction.
        """
        return self._degree_v

    @degree_v.setter
    def degree_v(self, value: int):
        self._degree_v = value

    @property
    def degree_w(self) -> int:
        """Degree of spline in w direction.
        """
        return self._degree_w

    @degree_w.setter
    def degree_w(self, value: int):
        self._degree_w = value

    @property
    def refinement_fraction_u(self) -> float:
        """Fraction of input mesh size that sets the control points size in u direction. This is used in program controlled control points selection mode.
        """
        return self._refinement_fraction_u

    @refinement_fraction_u.setter
    def refinement_fraction_u(self, value: float):
        self._refinement_fraction_u = value

    @property
    def refinement_fraction_v(self) -> float:
        """Fraction of input mesh size that sets the control points size in v direction. This is used in program controlled control points selection mode.
        """
        return self._refinement_fraction_v

    @refinement_fraction_v.setter
    def refinement_fraction_v(self, value: float):
        self._refinement_fraction_v = value

    @property
    def refinement_fraction_w(self) -> float:
        """Fraction of input mesh size that sets the control points size in w direction. This is used in program controlled control points selection mode.
        """
        return self._refinement_fraction_w

    @refinement_fraction_w.setter
    def refinement_fraction_w(self, value: float):
        self._refinement_fraction_w = value

    @property
    def control_points_count_u(self) -> int:
        """Spline control points count in U direction. Used in manual control points selection mode.
        """
        return self._control_points_count_u

    @control_points_count_u.setter
    def control_points_count_u(self, value: int):
        self._control_points_count_u = value

    @property
    def control_points_count_v(self) -> int:
        """Spline control points count in V direction. Used in manual control points selection mode.
        """
        return self._control_points_count_v

    @control_points_count_v.setter
    def control_points_count_v(self, value: int):
        self._control_points_count_v = value

    @property
    def control_points_count_w(self) -> int:
        """Spline control points count in W direction. Used in manual control points selection mode.
        """
        return self._control_points_count_w

    @control_points_count_w.setter
    def control_points_count_w(self, value: int):
        self._control_points_count_w = value

    @property
    def n_refine(self) -> int:
        """Spline refinement level for rendering.
        """
        return self._n_refine

    @n_refine.setter
    def n_refine(self, value: int):
        self._n_refine = value

    @property
    def control_point_selection_type(self) -> ControlPointSelection:
        """Spline control points selection type.
        """
        return self._control_point_selection_type

    @control_point_selection_type.setter
    def control_point_selection_type(self, value: ControlPointSelection):
        self._control_point_selection_type = value

class QuadToSplineParams(CoreObject):
    """Parameters to control conversion of quadrilateral mesh to spline.
    """
    _default_params = {}

    def __initialize(
            self,
            feature_capture_type: SplineFeatureCaptureType,
            feature_angle: float,
            corner_angle: float,
            shell_thickness: float,
            solid_shell: bool,
            separate_by_zone: bool,
            zone_name_shell_thickness_pairs: Dict[str, Union[str, int, float, bool]],
            project_on_geometry: bool,
            use_projection_scope: bool,
            projection_scope: ScopeDefinition):
        self._feature_capture_type = SplineFeatureCaptureType(feature_capture_type)
        self._feature_angle = feature_angle
        self._corner_angle = corner_angle
        self._shell_thickness = shell_thickness
        self._solid_shell = solid_shell
        self._separate_by_zone = separate_by_zone
        self._zone_name_shell_thickness_pairs = zone_name_shell_thickness_pairs
        self._project_on_geometry = project_on_geometry
        self._use_projection_scope = use_projection_scope
        self._projection_scope = projection_scope

    def __init__(
            self,
            model: CommunicationManager=None,
            feature_capture_type: SplineFeatureCaptureType = None,
            feature_angle: float = None,
            corner_angle: float = None,
            shell_thickness: float = None,
            solid_shell: bool = None,
            separate_by_zone: bool = None,
            zone_name_shell_thickness_pairs: Dict[str, Union[str, int, float, bool]] = None,
            project_on_geometry: bool = None,
            use_projection_scope: bool = None,
            projection_scope: ScopeDefinition = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the QuadToSplineParams.

        Parameters
        ----------
        model: Model
            Model to create a QuadToSplineParams object with default parameters.
        feature_capture_type: SplineFeatureCaptureType, optional
            Feature capture options.
            This parameter is a Beta. Parameter behavior and name may change in future.
        feature_angle: float, optional
            Angle to capture the feature.
            This parameter is a Beta. Parameter behavior and name may change in future.
        corner_angle: float, optional
            Corner angle of the feature.
            This parameter is a Beta. Parameter behavior and name may change in future.
        shell_thickness: float, optional
            Thickness of shell.
            This parameter is a Beta. Parameter behavior and name may change in future.
        solid_shell: bool, optional
            Solid shell option. Set true to generate solid shell spline, and set false to generate surface spline.
            This parameter is a Beta. Parameter behavior and name may change in future.
        separate_by_zone: bool, optional
            Option to separate IGA shell regions by zone. If set to true, it creates LS-Dyna part per zone while exporting IGA .k file and if set to false, it creates a single LS-Dyna part per Prime part, irrespective of the zones.
            This parameter is a Beta. Parameter behavior and name may change in future.
        zone_name_shell_thickness_pairs: Dict[str, Union[str, int, float, bool]], optional
            Zone name and thickness pair list. For example, {"Zone1Name": Zone1Thickness, "Zone2Name": Zone2Thickness, ...}.
        project_on_geometry: bool, optional
            Option to project on geometry.
            This parameter is a Beta. Parameter behavior and name may change in future.
        use_projection_scope: bool, optional
            Option to use projection scope.
            This parameter is a Beta. Parameter behavior and name may change in future.
        projection_scope: ScopeDefinition, optional
            Scope to evaluate entities for projection.
            This parameter is a Beta. Parameter behavior and name may change in future.
        json_data: dict, optional
            JSON dictionary to create a QuadToSplineParams object with provided parameters.

        Examples
        --------
        >>> quad_to_spline_params = prime.QuadToSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                SplineFeatureCaptureType(json_data["featureCaptureType"] if "featureCaptureType" in json_data else None),
                json_data["featureAngle"] if "featureAngle" in json_data else None,
                json_data["cornerAngle"] if "cornerAngle" in json_data else None,
                json_data["shellThickness"] if "shellThickness" in json_data else None,
                json_data["solidShell"] if "solidShell" in json_data else None,
                json_data["separateByZone"] if "separateByZone" in json_data else None,
                json_data["zoneNameShellThicknessPairs"] if "zoneNameShellThicknessPairs" in json_data else None,
                json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None,
                json_data["useProjectionScope"] if "useProjectionScope" in json_data else None,
                ScopeDefinition(model = model, json_data = json_data["projectionScope"] if "projectionScope" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [feature_capture_type, feature_angle, corner_angle, shell_thickness, solid_shell, separate_by_zone, zone_name_shell_thickness_pairs, project_on_geometry, use_projection_scope, projection_scope])
            if all_field_specified:
                self.__initialize(
                    feature_capture_type,
                    feature_angle,
                    corner_angle,
                    shell_thickness,
                    solid_shell,
                    separate_by_zone,
                    zone_name_shell_thickness_pairs,
                    project_on_geometry,
                    use_projection_scope,
                    projection_scope)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "QuadToSplineParams")
                    json_data = param_json["QuadToSplineParams"] if "QuadToSplineParams" in param_json else {}
                    self.__initialize(
                        feature_capture_type if feature_capture_type is not None else ( QuadToSplineParams._default_params["feature_capture_type"] if "feature_capture_type" in QuadToSplineParams._default_params else SplineFeatureCaptureType(json_data["featureCaptureType"] if "featureCaptureType" in json_data else None)),
                        feature_angle if feature_angle is not None else ( QuadToSplineParams._default_params["feature_angle"] if "feature_angle" in QuadToSplineParams._default_params else (json_data["featureAngle"] if "featureAngle" in json_data else None)),
                        corner_angle if corner_angle is not None else ( QuadToSplineParams._default_params["corner_angle"] if "corner_angle" in QuadToSplineParams._default_params else (json_data["cornerAngle"] if "cornerAngle" in json_data else None)),
                        shell_thickness if shell_thickness is not None else ( QuadToSplineParams._default_params["shell_thickness"] if "shell_thickness" in QuadToSplineParams._default_params else (json_data["shellThickness"] if "shellThickness" in json_data else None)),
                        solid_shell if solid_shell is not None else ( QuadToSplineParams._default_params["solid_shell"] if "solid_shell" in QuadToSplineParams._default_params else (json_data["solidShell"] if "solidShell" in json_data else None)),
                        separate_by_zone if separate_by_zone is not None else ( QuadToSplineParams._default_params["separate_by_zone"] if "separate_by_zone" in QuadToSplineParams._default_params else (json_data["separateByZone"] if "separateByZone" in json_data else None)),
                        zone_name_shell_thickness_pairs if zone_name_shell_thickness_pairs is not None else ( QuadToSplineParams._default_params["zone_name_shell_thickness_pairs"] if "zone_name_shell_thickness_pairs" in QuadToSplineParams._default_params else (json_data["zoneNameShellThicknessPairs"] if "zoneNameShellThicknessPairs" in json_data else None)),
                        project_on_geometry if project_on_geometry is not None else ( QuadToSplineParams._default_params["project_on_geometry"] if "project_on_geometry" in QuadToSplineParams._default_params else (json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None)),
                        use_projection_scope if use_projection_scope is not None else ( QuadToSplineParams._default_params["use_projection_scope"] if "use_projection_scope" in QuadToSplineParams._default_params else (json_data["useProjectionScope"] if "useProjectionScope" in json_data else None)),
                        projection_scope if projection_scope is not None else ( QuadToSplineParams._default_params["projection_scope"] if "projection_scope" in QuadToSplineParams._default_params else ScopeDefinition(model = model, json_data = (json_data["projectionScope"] if "projectionScope" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            feature_capture_type: SplineFeatureCaptureType = None,
            feature_angle: float = None,
            corner_angle: float = None,
            shell_thickness: float = None,
            solid_shell: bool = None,
            separate_by_zone: bool = None,
            zone_name_shell_thickness_pairs: Dict[str, Union[str, int, float, bool]] = None,
            project_on_geometry: bool = None,
            use_projection_scope: bool = None,
            projection_scope: ScopeDefinition = None):
        """Set the default values of QuadToSplineParams.

        Parameters
        ----------
        feature_capture_type: SplineFeatureCaptureType, optional
            Feature capture options.
        feature_angle: float, optional
            Angle to capture the feature.
        corner_angle: float, optional
            Corner angle of the feature.
        shell_thickness: float, optional
            Thickness of shell.
        solid_shell: bool, optional
            Solid shell option. Set true to generate solid shell spline, and set false to generate surface spline.
        separate_by_zone: bool, optional
            Option to separate IGA shell regions by zone. If set to true, it creates LS-Dyna part per zone while exporting IGA .k file and if set to false, it creates a single LS-Dyna part per Prime part, irrespective of the zones.
        zone_name_shell_thickness_pairs: Dict[str, Union[str, int, float, bool]], optional
            Zone name and thickness pair list. For example, {"Zone1Name": Zone1Thickness, "Zone2Name": Zone2Thickness, ...}.
        project_on_geometry: bool, optional
            Option to project on geometry.
        use_projection_scope: bool, optional
            Option to use projection scope.
        projection_scope: ScopeDefinition, optional
            Scope to evaluate entities for projection.
        """
        args = locals()
        [QuadToSplineParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of QuadToSplineParams.

        Examples
        --------
        >>> QuadToSplineParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in QuadToSplineParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._feature_capture_type is not None:
            json_data["featureCaptureType"] = self._feature_capture_type
        if self._feature_angle is not None:
            json_data["featureAngle"] = self._feature_angle
        if self._corner_angle is not None:
            json_data["cornerAngle"] = self._corner_angle
        if self._shell_thickness is not None:
            json_data["shellThickness"] = self._shell_thickness
        if self._solid_shell is not None:
            json_data["solidShell"] = self._solid_shell
        if self._separate_by_zone is not None:
            json_data["separateByZone"] = self._separate_by_zone
        if self._zone_name_shell_thickness_pairs is not None:
            json_data["zoneNameShellThicknessPairs"] = self._zone_name_shell_thickness_pairs
        if self._project_on_geometry is not None:
            json_data["projectOnGeometry"] = self._project_on_geometry
        if self._use_projection_scope is not None:
            json_data["useProjectionScope"] = self._use_projection_scope
        if self._projection_scope is not None:
            json_data["projectionScope"] = self._projection_scope._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "feature_capture_type :  %s\nfeature_angle :  %s\ncorner_angle :  %s\nshell_thickness :  %s\nsolid_shell :  %s\nseparate_by_zone :  %s\nzone_name_shell_thickness_pairs :  %s\nproject_on_geometry :  %s\nuse_projection_scope :  %s\nprojection_scope :  %s" % (self._feature_capture_type, self._feature_angle, self._corner_angle, self._shell_thickness, self._solid_shell, self._separate_by_zone, self._zone_name_shell_thickness_pairs, self._project_on_geometry, self._use_projection_scope, '{ ' + str(self._projection_scope) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def feature_capture_type(self) -> SplineFeatureCaptureType:
        """Feature capture options.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._feature_capture_type

    @feature_capture_type.setter
    def feature_capture_type(self, value: SplineFeatureCaptureType):
        self._feature_capture_type = value

    @property
    def feature_angle(self) -> float:
        """Angle to capture the feature.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._feature_angle

    @feature_angle.setter
    def feature_angle(self, value: float):
        self._feature_angle = value

    @property
    def corner_angle(self) -> float:
        """Corner angle of the feature.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._corner_angle

    @corner_angle.setter
    def corner_angle(self, value: float):
        self._corner_angle = value

    @property
    def shell_thickness(self) -> float:
        """Thickness of shell.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._shell_thickness

    @shell_thickness.setter
    def shell_thickness(self, value: float):
        self._shell_thickness = value

    @property
    def solid_shell(self) -> bool:
        """Solid shell option. Set true to generate solid shell spline, and set false to generate surface spline.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._solid_shell

    @solid_shell.setter
    def solid_shell(self, value: bool):
        self._solid_shell = value

    @property
    def separate_by_zone(self) -> bool:
        """Option to separate IGA shell regions by zone. If set to true, it creates LS-Dyna part per zone while exporting IGA .k file and if set to false, it creates a single LS-Dyna part per Prime part, irrespective of the zones.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._separate_by_zone

    @separate_by_zone.setter
    def separate_by_zone(self, value: bool):
        self._separate_by_zone = value

    @property
    def zone_name_shell_thickness_pairs(self) -> Dict[str, Union[str, int, float, bool]]:
        """Zone name and thickness pair list. For example, {"Zone1Name": Zone1Thickness, "Zone2Name": Zone2Thickness, ...}.
        """
        return self._zone_name_shell_thickness_pairs

    @zone_name_shell_thickness_pairs.setter
    def zone_name_shell_thickness_pairs(self, value: Dict[str, Union[str, int, float, bool]]):
        self._zone_name_shell_thickness_pairs = value

    @property
    def project_on_geometry(self) -> bool:
        """Option to project on geometry.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._project_on_geometry

    @project_on_geometry.setter
    def project_on_geometry(self, value: bool):
        self._project_on_geometry = value

    @property
    def use_projection_scope(self) -> bool:
        """Option to use projection scope.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._use_projection_scope

    @use_projection_scope.setter
    def use_projection_scope(self, value: bool):
        self._use_projection_scope = value

    @property
    def projection_scope(self) -> ScopeDefinition:
        """Scope to evaluate entities for projection.
        This parameter is a Beta. Parameter behavior and name may change in future.
        """
        return self._projection_scope

    @projection_scope.setter
    def projection_scope(self, value: ScopeDefinition):
        self._projection_scope = value

class RefineSplineParams(CoreObject):
    """Spline refinement parameters.
    """
    _default_params = {}

    def __initialize(
            self,
            refine_flag_u: bool,
            refine_flag_v: bool,
            refine_flag_w: bool,
            spline_refinement_type: SplineRefinementType):
        self._refine_flag_u = refine_flag_u
        self._refine_flag_v = refine_flag_v
        self._refine_flag_w = refine_flag_w
        self._spline_refinement_type = SplineRefinementType(spline_refinement_type)

    def __init__(
            self,
            model: CommunicationManager=None,
            refine_flag_u: bool = None,
            refine_flag_v: bool = None,
            refine_flag_w: bool = None,
            spline_refinement_type: SplineRefinementType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the RefineSplineParams.

        Parameters
        ----------
        model: Model
            Model to create a RefineSplineParams object with default parameters.
        refine_flag_u: bool, optional
            Indicates whether refinement is applied in u direction.
        refine_flag_v: bool, optional
            Indicates whether refinement is applied in v direction.
        refine_flag_w: bool, optional
            Indicates whether refinement is applied in w direction.
        spline_refinement_type: SplineRefinementType, optional
            Type of spline refinement. Currently, supports h-refinement and p-refinement.
        json_data: dict, optional
            JSON dictionary to create a RefineSplineParams object with provided parameters.

        Examples
        --------
        >>> refine_spline_params = prime.RefineSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["refineFlagU"] if "refineFlagU" in json_data else None,
                json_data["refineFlagV"] if "refineFlagV" in json_data else None,
                json_data["refineFlagW"] if "refineFlagW" in json_data else None,
                SplineRefinementType(json_data["splineRefinementType"] if "splineRefinementType" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [refine_flag_u, refine_flag_v, refine_flag_w, spline_refinement_type])
            if all_field_specified:
                self.__initialize(
                    refine_flag_u,
                    refine_flag_v,
                    refine_flag_w,
                    spline_refinement_type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "RefineSplineParams")
                    json_data = param_json["RefineSplineParams"] if "RefineSplineParams" in param_json else {}
                    self.__initialize(
                        refine_flag_u if refine_flag_u is not None else ( RefineSplineParams._default_params["refine_flag_u"] if "refine_flag_u" in RefineSplineParams._default_params else (json_data["refineFlagU"] if "refineFlagU" in json_data else None)),
                        refine_flag_v if refine_flag_v is not None else ( RefineSplineParams._default_params["refine_flag_v"] if "refine_flag_v" in RefineSplineParams._default_params else (json_data["refineFlagV"] if "refineFlagV" in json_data else None)),
                        refine_flag_w if refine_flag_w is not None else ( RefineSplineParams._default_params["refine_flag_w"] if "refine_flag_w" in RefineSplineParams._default_params else (json_data["refineFlagW"] if "refineFlagW" in json_data else None)),
                        spline_refinement_type if spline_refinement_type is not None else ( RefineSplineParams._default_params["spline_refinement_type"] if "spline_refinement_type" in RefineSplineParams._default_params else SplineRefinementType(json_data["splineRefinementType"] if "splineRefinementType" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            refine_flag_u: bool = None,
            refine_flag_v: bool = None,
            refine_flag_w: bool = None,
            spline_refinement_type: SplineRefinementType = None):
        """Set the default values of RefineSplineParams.

        Parameters
        ----------
        refine_flag_u: bool, optional
            Indicates whether refinement is applied in u direction.
        refine_flag_v: bool, optional
            Indicates whether refinement is applied in v direction.
        refine_flag_w: bool, optional
            Indicates whether refinement is applied in w direction.
        spline_refinement_type: SplineRefinementType, optional
            Type of spline refinement. Currently, supports h-refinement and p-refinement.
        """
        args = locals()
        [RefineSplineParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of RefineSplineParams.

        Examples
        --------
        >>> RefineSplineParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RefineSplineParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._refine_flag_u is not None:
            json_data["refineFlagU"] = self._refine_flag_u
        if self._refine_flag_v is not None:
            json_data["refineFlagV"] = self._refine_flag_v
        if self._refine_flag_w is not None:
            json_data["refineFlagW"] = self._refine_flag_w
        if self._spline_refinement_type is not None:
            json_data["splineRefinementType"] = self._spline_refinement_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "refine_flag_u :  %s\nrefine_flag_v :  %s\nrefine_flag_w :  %s\nspline_refinement_type :  %s" % (self._refine_flag_u, self._refine_flag_v, self._refine_flag_w, self._spline_refinement_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def refine_flag_u(self) -> bool:
        """Indicates whether refinement is applied in u direction.
        """
        return self._refine_flag_u

    @refine_flag_u.setter
    def refine_flag_u(self, value: bool):
        self._refine_flag_u = value

    @property
    def refine_flag_v(self) -> bool:
        """Indicates whether refinement is applied in v direction.
        """
        return self._refine_flag_v

    @refine_flag_v.setter
    def refine_flag_v(self, value: bool):
        self._refine_flag_v = value

    @property
    def refine_flag_w(self) -> bool:
        """Indicates whether refinement is applied in w direction.
        """
        return self._refine_flag_w

    @refine_flag_w.setter
    def refine_flag_w(self, value: bool):
        self._refine_flag_w = value

    @property
    def spline_refinement_type(self) -> SplineRefinementType:
        """Type of spline refinement. Currently, supports h-refinement and p-refinement.
        """
        return self._spline_refinement_type

    @spline_refinement_type.setter
    def spline_refinement_type(self, value: SplineRefinementType):
        self._spline_refinement_type = value
