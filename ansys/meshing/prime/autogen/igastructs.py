""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class IGASplineType(enum.IntEnum):
    """    """
    # Boundary fitted solid spline type
    BOUNDARYFITTEDSOLIDSPLINE = 0

class ControlPointSelection(enum.IntEnum):
    """    """
    # Manual Spline control point selection
    MANUAL = 0
    # Program controlled spline control point selection
    PROGRAMCONTROLLED = 1

class SplineRefinementType(enum.IntEnum):
    """    """
    # H refinement of spline
    H = 0
    # P refinement of spline
    P = 1

class IGAResults(CoreObject):
    """    """
    default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_code: WarningCode,
            spline_ids: List[int]):
        self._error_code = error_code
        self._warning_code = warning_code
        self._spline_ids = spline_ids

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_code: WarningCode = None,
            spline_ids: List[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes IGAResults

        Parameters
        ----------
        model: Model
            Model to create a IGAResults object with default parameters.
        error_code: ErrorCode, optional
        warning_code: WarningCode, optional
        spline_ids: List[int], optional
        json_data: dict, optional
            JSON dictionary to create a IGAResults object with provided parameters.

        Examples
        --------
        >>> i_garesults = IGAResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                WarningCode(json_data["warningCode"]),
                json_data["splineIds"])
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
                    json_data = model.communicator.initialize_params("IGAResults")["IGAResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( IGAResults.default_params["error_code"] if "error_code" in IGAResults.default_params else ErrorCode(json_data["errorCode"])),
                        warning_code if warning_code is not None else ( IGAResults.default_params["warning_code"] if "warning_code" in IGAResults.default_params else WarningCode(json_data["warningCode"])),
                        spline_ids if spline_ids is not None else ( IGAResults.default_params["spline_ids"] if "spline_ids" in IGAResults.default_params else json_data["splineIds"]))
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
            spline_ids: List[int] = None):
        args = locals()
        [IGAResults.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in IGAResults.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["warningCode"] = self._warning_code
        json_data["splineIds"] = self._spline_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_code :  %s\nspline_ids :  %s" % (self._error_code, self._warning_code, self._spline_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """
        Error code if IGA operation is unsuccessful
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_code(self) -> WarningCode:
        """
        Warning code if IGA operation is partially successful
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, value: WarningCode):
        self._warning_code = value

    @property
    def spline_ids(self) -> List[int]:
        """
        Ids of the created spline
        """
        return self._spline_ids

    @spline_ids.setter
    def spline_ids(self, value: List[int]):
        self._spline_ids = value

class IGASpline(CoreObject):
    """    """
    default_params = {}

    def __initialize(
            self,
            id: int,
            cell_zonelet_ids: List[int]):
        self._id = id
        self._cell_zonelet_ids = cell_zonelet_ids

    def __init__(
            self,
            model: CommunicationManager=None,
            id: int = None,
            cell_zonelet_ids: List[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes IGASpline

        Parameters
        ----------
        model: Model
            Model to create a IGASpline object with default parameters.
        id: int, optional
        cell_zonelet_ids: List[int], optional
        json_data: dict, optional
            JSON dictionary to create a IGASpline object with provided parameters.

        Examples
        --------
        >>> i_gaspline = IGASpline(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["id"],
                json_data["cellZoneletIds"])
        else:
            all_field_specified = all(arg is not None for arg in [id, cell_zonelet_ids])
            if all_field_specified:
                self.__initialize(
                    id,
                    cell_zonelet_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("IGASpline")["IGASpline"]
                    self.__initialize(
                        id if id is not None else ( IGASpline.default_params["id"] if "id" in IGASpline.default_params else json_data["id"]),
                        cell_zonelet_ids if cell_zonelet_ids is not None else ( IGASpline.default_params["cell_zonelet_ids"] if "cell_zonelet_ids" in IGASpline.default_params else json_data["cellZoneletIds"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            id: int = None,
            cell_zonelet_ids: List[int] = None):
        args = locals()
        [IGASpline.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in IGASpline.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["id"] = self._id
        json_data["cellZoneletIds"] = self._cell_zonelet_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "id :  %s\ncell_zonelet_ids :  %s" % (self._id, self._cell_zonelet_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def id(self) -> int:
        """
        Unique id of the spline
        """
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def cell_zonelet_ids(self) -> List[int]:
        """
        Ids of the cell zonelets from which the structured hexmesh fitted Spline was created
        """
        return self._cell_zonelet_ids

    @cell_zonelet_ids.setter
    def cell_zonelet_ids(self, value: List[int]):
        self._cell_zonelet_ids = value

class BoundaryFittedSplineParams(CoreObject):
    """    """
    default_params = {}

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
        self._control_point_selection_type = control_point_selection_type

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
        """Initializes BoundaryFittedSplineParams

        Parameters
        ----------
        model: Model
            Model to create a BoundaryFittedSplineParams object with default parameters.
        degree_u: int, optional
        degree_v: int, optional
        degree_w: int, optional
        refinement_fraction_u: float, optional
        refinement_fraction_v: float, optional
        refinement_fraction_w: float, optional
        control_points_count_u: int, optional
        control_points_count_v: int, optional
        control_points_count_w: int, optional
        n_refine: int, optional
        control_point_selection_type: ControlPointSelection, optional
        json_data: dict, optional
            JSON dictionary to create a BoundaryFittedSplineParams object with provided parameters.

        Examples
        --------
        >>> boundary_fitted_spline_params = BoundaryFittedSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["degreeU"],
                json_data["degreeV"],
                json_data["degreeW"],
                json_data["refinementFractionU"],
                json_data["refinementFractionV"],
                json_data["refinementFractionW"],
                json_data["controlPointsCountU"],
                json_data["controlPointsCountV"],
                json_data["controlPointsCountW"],
                json_data["nRefine"],
                ControlPointSelection(json_data["controlPointSelectionType"]))
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
                    json_data = model.communicator.initialize_params("BoundaryFittedSplineParams")["BoundaryFittedSplineParams"]
                    self.__initialize(
                        degree_u if degree_u is not None else ( BoundaryFittedSplineParams.default_params["degree_u"] if "degree_u" in BoundaryFittedSplineParams.default_params else json_data["degreeU"]),
                        degree_v if degree_v is not None else ( BoundaryFittedSplineParams.default_params["degree_v"] if "degree_v" in BoundaryFittedSplineParams.default_params else json_data["degreeV"]),
                        degree_w if degree_w is not None else ( BoundaryFittedSplineParams.default_params["degree_w"] if "degree_w" in BoundaryFittedSplineParams.default_params else json_data["degreeW"]),
                        refinement_fraction_u if refinement_fraction_u is not None else ( BoundaryFittedSplineParams.default_params["refinement_fraction_u"] if "refinement_fraction_u" in BoundaryFittedSplineParams.default_params else json_data["refinementFractionU"]),
                        refinement_fraction_v if refinement_fraction_v is not None else ( BoundaryFittedSplineParams.default_params["refinement_fraction_v"] if "refinement_fraction_v" in BoundaryFittedSplineParams.default_params else json_data["refinementFractionV"]),
                        refinement_fraction_w if refinement_fraction_w is not None else ( BoundaryFittedSplineParams.default_params["refinement_fraction_w"] if "refinement_fraction_w" in BoundaryFittedSplineParams.default_params else json_data["refinementFractionW"]),
                        control_points_count_u if control_points_count_u is not None else ( BoundaryFittedSplineParams.default_params["control_points_count_u"] if "control_points_count_u" in BoundaryFittedSplineParams.default_params else json_data["controlPointsCountU"]),
                        control_points_count_v if control_points_count_v is not None else ( BoundaryFittedSplineParams.default_params["control_points_count_v"] if "control_points_count_v" in BoundaryFittedSplineParams.default_params else json_data["controlPointsCountV"]),
                        control_points_count_w if control_points_count_w is not None else ( BoundaryFittedSplineParams.default_params["control_points_count_w"] if "control_points_count_w" in BoundaryFittedSplineParams.default_params else json_data["controlPointsCountW"]),
                        n_refine if n_refine is not None else ( BoundaryFittedSplineParams.default_params["n_refine"] if "n_refine" in BoundaryFittedSplineParams.default_params else json_data["nRefine"]),
                        control_point_selection_type if control_point_selection_type is not None else ( BoundaryFittedSplineParams.default_params["control_point_selection_type"] if "control_point_selection_type" in BoundaryFittedSplineParams.default_params else ControlPointSelection(json_data["controlPointSelectionType"])))
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
        args = locals()
        [BoundaryFittedSplineParams.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in BoundaryFittedSplineParams.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["degreeU"] = self._degree_u
        json_data["degreeV"] = self._degree_v
        json_data["degreeW"] = self._degree_w
        json_data["refinementFractionU"] = self._refinement_fraction_u
        json_data["refinementFractionV"] = self._refinement_fraction_v
        json_data["refinementFractionW"] = self._refinement_fraction_w
        json_data["controlPointsCountU"] = self._control_points_count_u
        json_data["controlPointsCountV"] = self._control_points_count_v
        json_data["controlPointsCountW"] = self._control_points_count_w
        json_data["nRefine"] = self._n_refine
        json_data["controlPointSelectionType"] = self._control_point_selection_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "degree_u :  %s\ndegree_v :  %s\ndegree_w :  %s\nrefinement_fraction_u :  %s\nrefinement_fraction_v :  %s\nrefinement_fraction_w :  %s\ncontrol_points_count_u :  %s\ncontrol_points_count_v :  %s\ncontrol_points_count_w :  %s\nn_refine :  %s\ncontrol_point_selection_type :  %s" % (self._degree_u, self._degree_v, self._degree_w, self._refinement_fraction_u, self._refinement_fraction_v, self._refinement_fraction_w, self._control_points_count_u, self._control_points_count_v, self._control_points_count_w, self._n_refine, self._control_point_selection_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def degree_u(self) -> int:
        """
        Degree of spline in u direction
        """
        return self._degree_u

    @degree_u.setter
    def degree_u(self, value: int):
        self._degree_u = value

    @property
    def degree_v(self) -> int:
        """
        Degree of spline in v direction
        """
        return self._degree_v

    @degree_v.setter
    def degree_v(self, value: int):
        self._degree_v = value

    @property
    def degree_w(self) -> int:
        """
        Degree of spline in w direction
        """
        return self._degree_w

    @degree_w.setter
    def degree_w(self, value: int):
        self._degree_w = value

    @property
    def refinement_fraction_u(self) -> float:
        """
        Refinement fraction of spline control points size with respect to input mesh node size in u direction. Used in program controlled control points selection mode
        """
        return self._refinement_fraction_u

    @refinement_fraction_u.setter
    def refinement_fraction_u(self, value: float):
        self._refinement_fraction_u = value

    @property
    def refinement_fraction_v(self) -> float:
        """
        Refinement fraction of spline control points size with respect to input mesh node size in v direction. Used in program controlled control points selection mode
        """
        return self._refinement_fraction_v

    @refinement_fraction_v.setter
    def refinement_fraction_v(self, value: float):
        self._refinement_fraction_v = value

    @property
    def refinement_fraction_w(self) -> float:
        """
        Refinement fraction of spline control points size with respect to input mesh node size in w direction. Used in program controlled control points selection mode
        """
        return self._refinement_fraction_w

    @refinement_fraction_w.setter
    def refinement_fraction_w(self, value: float):
        self._refinement_fraction_w = value

    @property
    def control_points_count_u(self) -> int:
        """
        Spline control points count in u direction
        """
        return self._control_points_count_u

    @control_points_count_u.setter
    def control_points_count_u(self, value: int):
        self._control_points_count_u = value

    @property
    def control_points_count_v(self) -> int:
        """
        Spline control points count in v direction
        """
        return self._control_points_count_v

    @control_points_count_v.setter
    def control_points_count_v(self, value: int):
        self._control_points_count_v = value

    @property
    def control_points_count_w(self) -> int:
        """
        Spline control points count in w direction
        """
        return self._control_points_count_w

    @control_points_count_w.setter
    def control_points_count_w(self, value: int):
        self._control_points_count_w = value

    @property
    def n_refine(self) -> int:
        """
        Spline refinement level for rendering
        """
        return self._n_refine

    @n_refine.setter
    def n_refine(self, value: int):
        self._n_refine = value

    @property
    def control_point_selection_type(self) -> ControlPointSelection:
        """
        Spline control point size selection type
        """
        return self._control_point_selection_type

    @control_point_selection_type.setter
    def control_point_selection_type(self, value: ControlPointSelection):
        self._control_point_selection_type = value

class RefineSplineParams(CoreObject):
    """    """
    default_params = {}

    def __initialize(
            self,
            refine_flag_u: bool,
            refine_flag_v: bool,
            refine_flag_w: bool,
            spline_refinement_type: SplineRefinementType):
        self._refine_flag_u = refine_flag_u
        self._refine_flag_v = refine_flag_v
        self._refine_flag_w = refine_flag_w
        self._spline_refinement_type = spline_refinement_type

    def __init__(
            self,
            model: CommunicationManager=None,
            refine_flag_u: bool = None,
            refine_flag_v: bool = None,
            refine_flag_w: bool = None,
            spline_refinement_type: SplineRefinementType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes RefineSplineParams

        Parameters
        ----------
        model: Model
            Model to create a RefineSplineParams object with default parameters.
        refine_flag_u: bool, optional
        refine_flag_v: bool, optional
        refine_flag_w: bool, optional
        spline_refinement_type: SplineRefinementType, optional
        json_data: dict, optional
            JSON dictionary to create a RefineSplineParams object with provided parameters.

        Examples
        --------
        >>> refine_spline_params = RefineSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["refineFlagU"],
                json_data["refineFlagV"],
                json_data["refineFlagW"],
                SplineRefinementType(json_data["splineRefinementType"]))
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
                    json_data = model.communicator.initialize_params("RefineSplineParams")["RefineSplineParams"]
                    self.__initialize(
                        refine_flag_u if refine_flag_u is not None else ( RefineSplineParams.default_params["refine_flag_u"] if "refine_flag_u" in RefineSplineParams.default_params else json_data["refineFlagU"]),
                        refine_flag_v if refine_flag_v is not None else ( RefineSplineParams.default_params["refine_flag_v"] if "refine_flag_v" in RefineSplineParams.default_params else json_data["refineFlagV"]),
                        refine_flag_w if refine_flag_w is not None else ( RefineSplineParams.default_params["refine_flag_w"] if "refine_flag_w" in RefineSplineParams.default_params else json_data["refineFlagW"]),
                        spline_refinement_type if spline_refinement_type is not None else ( RefineSplineParams.default_params["spline_refinement_type"] if "spline_refinement_type" in RefineSplineParams.default_params else SplineRefinementType(json_data["splineRefinementType"])))
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
        args = locals()
        [RefineSplineParams.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RefineSplineParams.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["refineFlagU"] = self._refine_flag_u
        json_data["refineFlagV"] = self._refine_flag_v
        json_data["refineFlagW"] = self._refine_flag_w
        json_data["splineRefinementType"] = self._spline_refinement_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "refine_flag_u :  %s\nrefine_flag_v :  %s\nrefine_flag_w :  %s\nspline_refinement_type :  %s" % (self._refine_flag_u, self._refine_flag_v, self._refine_flag_w, self._spline_refinement_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def refine_flag_u(self) -> bool:
        """
        Whether refinement is applied in u direction
        """
        return self._refine_flag_u

    @refine_flag_u.setter
    def refine_flag_u(self, value: bool):
        self._refine_flag_u = value

    @property
    def refine_flag_v(self) -> bool:
        """
        Whether refinement is applied in v direction
        """
        return self._refine_flag_v

    @refine_flag_v.setter
    def refine_flag_v(self, value: bool):
        self._refine_flag_v = value

    @property
    def refine_flag_w(self) -> bool:
        """
        Whether refinement is applied in w direction
        """
        return self._refine_flag_w

    @refine_flag_w.setter
    def refine_flag_w(self, value: bool):
        self._refine_flag_w = value

    @property
    def spline_refinement_type(self) -> SplineRefinementType:
        """
        Spline refinement type h/p
        """
        return self._spline_refinement_type

    @spline_refinement_type.setter
    def spline_refinement_type(self, value: SplineRefinementType):
        self._spline_refinement_type = value
