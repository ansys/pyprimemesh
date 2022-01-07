""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class SurfaceQualityResult(CoreObject):
    """Result of surface quality.
    """
    default_params = {}

    def __initialize(
            self,
            face_quality_measure: FaceQualityMeasure,
            measure_name: str,
            quality_limit: float,
            n_found: int,
            max_value: float,
            min_value: float):
        self._face_quality_measure = face_quality_measure
        self._measure_name = measure_name
        self._quality_limit = quality_limit
        self._n_found = n_found
        self._max_value = max_value
        self._min_value = min_value

    def __init__(
            self,
            model: CommunicationManager=None,
            face_quality_measure: FaceQualityMeasure = None,
            measure_name: str = None,
            quality_limit: float = None,
            n_found: int = None,
            max_value: float = None,
            min_value: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes SurfaceQualityResult

        Parameters
        ----------
        model: Model
            Model to create a SurfaceQualityResult object with default parameters.
        face_quality_measure: FaceQualityMeasure, optional
            Type of the face quality measure.
        measure_name: str, optional
            Name of the face quality measure.
        quality_limit: float, optional
            Target quality limit used to find failures.
        n_found: int, optional
            Number of failed faces.
        max_value: float, optional
            Maximum value of quality measure.
        min_value: float, optional
            Minimum value of quality measure.
        json_data: dict, optional
            JSON dictionary to create a SurfaceQualityResult object with provided parameters.

        Examples
        --------
        >>> surface_quality_result = SurfaceQualityResult(model = model)
        """
        if json_data:
            self.__initialize(
                FaceQualityMeasure(json_data["faceQualityMeasure"]),
                json_data["measureName"],
                json_data["qualityLimit"],
                json_data["nFound"],
                json_data["maxValue"],
                json_data["minValue"])
        else:
            all_field_specified = all(arg is not None for arg in [face_quality_measure, measure_name, quality_limit, n_found, max_value, min_value])
            if all_field_specified:
                self.__initialize(
                    face_quality_measure,
                    measure_name,
                    quality_limit,
                    n_found,
                    max_value,
                    min_value)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("SurfaceQualityResult")["SurfaceQualityResult"]
                    self.__initialize(
                        face_quality_measure if face_quality_measure is not None else ( SurfaceQualityResult.default_params["face_quality_measure"] if "face_quality_measure" in SurfaceQualityResult.default_params else FaceQualityMeasure(json_data["faceQualityMeasure"])),
                        measure_name if measure_name is not None else ( SurfaceQualityResult.default_params["measure_name"] if "measure_name" in SurfaceQualityResult.default_params else json_data["measureName"]),
                        quality_limit if quality_limit is not None else ( SurfaceQualityResult.default_params["quality_limit"] if "quality_limit" in SurfaceQualityResult.default_params else json_data["qualityLimit"]),
                        n_found if n_found is not None else ( SurfaceQualityResult.default_params["n_found"] if "n_found" in SurfaceQualityResult.default_params else json_data["nFound"]),
                        max_value if max_value is not None else ( SurfaceQualityResult.default_params["max_value"] if "max_value" in SurfaceQualityResult.default_params else json_data["maxValue"]),
                        min_value if min_value is not None else ( SurfaceQualityResult.default_params["min_value"] if "min_value" in SurfaceQualityResult.default_params else json_data["minValue"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            face_quality_measure: FaceQualityMeasure = None,
            measure_name: str = None,
            quality_limit: float = None,
            n_found: int = None,
            max_value: float = None,
            min_value: float = None):
        args = locals()
        [SurfaceQualityResult.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceQualityResult.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["faceQualityMeasure"] = self._face_quality_measure
        json_data["measureName"] = self._measure_name
        json_data["qualityLimit"] = self._quality_limit
        json_data["nFound"] = self._n_found
        json_data["maxValue"] = self._max_value
        json_data["minValue"] = self._min_value
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "face_quality_measure :  %s\nmeasure_name :  %s\nquality_limit :  %s\nn_found :  %s\nmax_value :  %s\nmin_value :  %s" % (self._face_quality_measure, self._measure_name, self._quality_limit, self._n_found, self._max_value, self._min_value)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def face_quality_measure(self) -> FaceQualityMeasure:
        """Type of the face quality measure.
        """
        return self._face_quality_measure

    @face_quality_measure.setter
    def face_quality_measure(self, value: FaceQualityMeasure):
        self._face_quality_measure = value

    @property
    def measure_name(self) -> str:
        """Name of the face quality measure.
        """
        return self._measure_name

    @measure_name.setter
    def measure_name(self, value: str):
        self._measure_name = value

    @property
    def quality_limit(self) -> float:
        """Target quality limit used to find failures.
        """
        return self._quality_limit

    @quality_limit.setter
    def quality_limit(self, value: float):
        self._quality_limit = value

    @property
    def n_found(self) -> int:
        """Number of failed faces.
        """
        return self._n_found

    @n_found.setter
    def n_found(self, value: int):
        self._n_found = value

    @property
    def max_value(self) -> float:
        """Maximum value of quality measure.
        """
        return self._max_value

    @max_value.setter
    def max_value(self, value: float):
        self._max_value = value

    @property
    def min_value(self) -> float:
        """Minimum value of quality measure.
        """
        return self._min_value

    @min_value.setter
    def min_value(self, value: float):
        self._min_value = value

class SurfaceQualitySummaryResults(CoreObject):
    """Results of surface quality summary.
    """
    default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            quality_results: List[SurfaceQualityResult],
            summary: str):
        self._error_code = error_code
        self._quality_results = quality_results
        self._summary = summary

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            quality_results: List[SurfaceQualityResult] = None,
            summary: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes SurfaceQualitySummaryResults

        Parameters
        ----------
        model: Model
            Model to create a SurfaceQualitySummaryResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the surface quality summary.
        quality_results: List[SurfaceQualityResult], optional
            Contains surface quality result per face quality measure specified in parameters.
        summary: str, optional
            Surface quality summary text.
        json_data: dict, optional
            JSON dictionary to create a SurfaceQualitySummaryResults object with provided parameters.

        Examples
        --------
        >>> surface_quality_summary_results = SurfaceQualitySummaryResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                [SurfaceQualityResult(model = model, json_data = data) for data in json_data["qualityResults"]],
                json_data["summary"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, quality_results, summary])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    quality_results,
                    summary)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("SurfaceQualitySummaryResults")["SurfaceQualitySummaryResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( SurfaceQualitySummaryResults.default_params["error_code"] if "error_code" in SurfaceQualitySummaryResults.default_params else ErrorCode(json_data["errorCode"])),
                        quality_results if quality_results is not None else ( SurfaceQualitySummaryResults.default_params["quality_results"] if "quality_results" in SurfaceQualitySummaryResults.default_params else [SurfaceQualityResult(model = model, json_data = data) for data in json_data["qualityResults"]]),
                        summary if summary is not None else ( SurfaceQualitySummaryResults.default_params["summary"] if "summary" in SurfaceQualitySummaryResults.default_params else json_data["summary"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            quality_results: List[SurfaceQualityResult] = None,
            summary: str = None):
        args = locals()
        [SurfaceQualitySummaryResults.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceQualitySummaryResults.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["qualityResults"] = [data.jsonify() for data in self._quality_results]
        json_data["summary"] = self._summary
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nquality_results :  %s\nsummary :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._quality_results) + ']', self._summary)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the surface quality summary.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def quality_results(self) -> List[SurfaceQualityResult]:
        """Contains surface quality result per face quality measure specified in parameters.
        """
        return self._quality_results

    @quality_results.setter
    def quality_results(self, value: List[SurfaceQualityResult]):
        self._quality_results = value

    @property
    def summary(self) -> str:
        """Surface quality summary text.
        """
        return self._summary

    @summary.setter
    def summary(self, value: str):
        self._summary = value

class SurfaceQualitySummaryParams(CoreObject):
    """Parameters to control surface quality summary results.
    """
    default_params = {}

    def __initialize(
            self,
            face_quality_measures: List[int],
            scope: ScopeDefinition,
            quality_limit: List[float]):
        self._face_quality_measures = face_quality_measures
        self._scope = scope
        self._quality_limit = quality_limit

    def __init__(
            self,
            model: CommunicationManager=None,
            face_quality_measures: List[int] = None,
            scope: ScopeDefinition = None,
            quality_limit: List[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes SurfaceQualitySummaryParams

        Parameters
        ----------
        model: Model
            Model to create a SurfaceQualitySummaryParams object with default parameters.
        face_quality_measures: List[int], optional
            List of face quality measures for surface quality diagnostics.
        scope: ScopeDefinition, optional
            Scope the face zonelets for surface quality diagnostics.
        quality_limit: List[float], optional
            Quality limit per face quality measure, if not specified for particular measure default quality limit is used.
        json_data: dict, optional
            JSON dictionary to create a SurfaceQualitySummaryParams object with provided parameters.

        Examples
        --------
        >>> surface_quality_summary_params = SurfaceQualitySummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["faceQualityMeasures"],
                ScopeDefinition(model = model, json_data = json_data["scope"]),
                json_data["qualityLimit"])
        else:
            all_field_specified = all(arg is not None for arg in [face_quality_measures, scope, quality_limit])
            if all_field_specified:
                self.__initialize(
                    face_quality_measures,
                    scope,
                    quality_limit)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("SurfaceQualitySummaryParams")["SurfaceQualitySummaryParams"]
                    self.__initialize(
                        face_quality_measures if face_quality_measures is not None else ( SurfaceQualitySummaryParams.default_params["face_quality_measures"] if "face_quality_measures" in SurfaceQualitySummaryParams.default_params else json_data["faceQualityMeasures"]),
                        scope if scope is not None else ( SurfaceQualitySummaryParams.default_params["scope"] if "scope" in SurfaceQualitySummaryParams.default_params else ScopeDefinition(model = model, json_data = json_data["scope"])),
                        quality_limit if quality_limit is not None else ( SurfaceQualitySummaryParams.default_params["quality_limit"] if "quality_limit" in SurfaceQualitySummaryParams.default_params else json_data["qualityLimit"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            face_quality_measures: List[int] = None,
            scope: ScopeDefinition = None,
            quality_limit: List[float] = None):
        args = locals()
        [SurfaceQualitySummaryParams.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceQualitySummaryParams.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["faceQualityMeasures"] = self._face_quality_measures
        json_data["scope"] = self._scope.jsonify()
        json_data["qualityLimit"] = self._quality_limit
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "face_quality_measures :  %s\nscope :  %s\nquality_limit :  %s" % (self._face_quality_measures, '{ ' + str(self._scope) + ' }', self._quality_limit)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def face_quality_measures(self) -> List[int]:
        """List of face quality measures for surface quality diagnostics.
        """
        return self._face_quality_measures

    @face_quality_measures.setter
    def face_quality_measures(self, value: List[int]):
        self._face_quality_measures = value

    @property
    def scope(self) -> ScopeDefinition:
        """Scope the face zonelets for surface quality diagnostics.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

    @property
    def quality_limit(self) -> List[float]:
        """Quality limit per face quality measure, if not specified for particular measure default quality limit is used.
        """
        return self._quality_limit

    @quality_limit.setter
    def quality_limit(self, value: List[float]):
        self._quality_limit = value
