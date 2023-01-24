""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class VolumeQualityResultsPart(CoreObject):
    """Result of volume quality of part.
    """
    _default_params = {}

    def __initialize(
            self,
            cell_quality_measure: CellQualityMeasure,
            measure_name: str,
            part_id: int,
            quality_limit: float,
            n_found: int,
            max_quality: float,
            min_quality: float):
        self._cell_quality_measure = CellQualityMeasure(cell_quality_measure)
        self._measure_name = measure_name
        self._part_id = part_id
        self._quality_limit = quality_limit
        self._n_found = n_found
        self._max_quality = max_quality
        self._min_quality = min_quality

    def __init__(
            self,
            model: CommunicationManager=None,
            cell_quality_measure: CellQualityMeasure = None,
            measure_name: str = None,
            part_id: int = None,
            quality_limit: float = None,
            n_found: int = None,
            max_quality: float = None,
            min_quality: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumeQualityResultsPart.

        Parameters
        ----------
        model: Model
            Model to create a VolumeQualityResultsPart object with default parameters.
        cell_quality_measure: CellQualityMeasure, optional
            Type of the cell quality measure.
        measure_name: str, optional
            Name of the cell quality measure.
        part_id: int, optional
            Id of the part for which quality is computed.
        quality_limit: float, optional
            Target quality limit used to find failures.
        n_found: int, optional
            Number of failed cells.
        max_quality: float, optional
            Maximum value of quality measure.
        min_quality: float, optional
            Minimum value of quality measure.
        json_data: dict, optional
            JSON dictionary to create a VolumeQualityResultsPart object with provided parameters.

        Examples
        --------
        >>> volume_quality_results_part = prime.VolumeQualityResultsPart(model = model)
        """
        if json_data:
            self.__initialize(
                CellQualityMeasure(json_data["cellQualityMeasure"] if "cellQualityMeasure" in json_data else None),
                json_data["measureName"] if "measureName" in json_data else None,
                json_data["partId"] if "partId" in json_data else None,
                json_data["qualityLimit"] if "qualityLimit" in json_data else None,
                json_data["nFound"] if "nFound" in json_data else None,
                json_data["maxQuality"] if "maxQuality" in json_data else None,
                json_data["minQuality"] if "minQuality" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [cell_quality_measure, measure_name, part_id, quality_limit, n_found, max_quality, min_quality])
            if all_field_specified:
                self.__initialize(
                    cell_quality_measure,
                    measure_name,
                    part_id,
                    quality_limit,
                    n_found,
                    max_quality,
                    min_quality)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumeQualityResultsPart")
                    json_data = param_json["VolumeQualityResultsPart"] if "VolumeQualityResultsPart" in param_json else {}
                    self.__initialize(
                        cell_quality_measure if cell_quality_measure is not None else ( VolumeQualityResultsPart._default_params["cell_quality_measure"] if "cell_quality_measure" in VolumeQualityResultsPart._default_params else CellQualityMeasure(json_data["cellQualityMeasure"] if "cellQualityMeasure" in json_data else None)),
                        measure_name if measure_name is not None else ( VolumeQualityResultsPart._default_params["measure_name"] if "measure_name" in VolumeQualityResultsPart._default_params else (json_data["measureName"] if "measureName" in json_data else None)),
                        part_id if part_id is not None else ( VolumeQualityResultsPart._default_params["part_id"] if "part_id" in VolumeQualityResultsPart._default_params else (json_data["partId"] if "partId" in json_data else None)),
                        quality_limit if quality_limit is not None else ( VolumeQualityResultsPart._default_params["quality_limit"] if "quality_limit" in VolumeQualityResultsPart._default_params else (json_data["qualityLimit"] if "qualityLimit" in json_data else None)),
                        n_found if n_found is not None else ( VolumeQualityResultsPart._default_params["n_found"] if "n_found" in VolumeQualityResultsPart._default_params else (json_data["nFound"] if "nFound" in json_data else None)),
                        max_quality if max_quality is not None else ( VolumeQualityResultsPart._default_params["max_quality"] if "max_quality" in VolumeQualityResultsPart._default_params else (json_data["maxQuality"] if "maxQuality" in json_data else None)),
                        min_quality if min_quality is not None else ( VolumeQualityResultsPart._default_params["min_quality"] if "min_quality" in VolumeQualityResultsPart._default_params else (json_data["minQuality"] if "minQuality" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            cell_quality_measure: CellQualityMeasure = None,
            measure_name: str = None,
            part_id: int = None,
            quality_limit: float = None,
            n_found: int = None,
            max_quality: float = None,
            min_quality: float = None):
        """Set the default values of VolumeQualityResultsPart.

        Parameters
        ----------
        cell_quality_measure: CellQualityMeasure, optional
            Type of the cell quality measure.
        measure_name: str, optional
            Name of the cell quality measure.
        part_id: int, optional
            Id of the part for which quality is computed.
        quality_limit: float, optional
            Target quality limit used to find failures.
        n_found: int, optional
            Number of failed cells.
        max_quality: float, optional
            Maximum value of quality measure.
        min_quality: float, optional
            Minimum value of quality measure.
        """
        args = locals()
        [VolumeQualityResultsPart._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumeQualityResultsPart.

        Examples
        --------
        >>> VolumeQualityResultsPart.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumeQualityResultsPart._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._cell_quality_measure is not None:
            json_data["cellQualityMeasure"] = self._cell_quality_measure
        if self._measure_name is not None:
            json_data["measureName"] = self._measure_name
        if self._part_id is not None:
            json_data["partId"] = self._part_id
        if self._quality_limit is not None:
            json_data["qualityLimit"] = self._quality_limit
        if self._n_found is not None:
            json_data["nFound"] = self._n_found
        if self._max_quality is not None:
            json_data["maxQuality"] = self._max_quality
        if self._min_quality is not None:
            json_data["minQuality"] = self._min_quality
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "cell_quality_measure :  %s\nmeasure_name :  %s\npart_id :  %s\nquality_limit :  %s\nn_found :  %s\nmax_quality :  %s\nmin_quality :  %s" % (self._cell_quality_measure, self._measure_name, self._part_id, self._quality_limit, self._n_found, self._max_quality, self._min_quality)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def cell_quality_measure(self) -> CellQualityMeasure:
        """Type of the cell quality measure.
        """
        return self._cell_quality_measure

    @cell_quality_measure.setter
    def cell_quality_measure(self, value: CellQualityMeasure):
        self._cell_quality_measure = value

    @property
    def measure_name(self) -> str:
        """Name of the cell quality measure.
        """
        return self._measure_name

    @measure_name.setter
    def measure_name(self, value: str):
        self._measure_name = value

    @property
    def part_id(self) -> int:
        """Id of the part for which quality is computed.
        """
        return self._part_id

    @part_id.setter
    def part_id(self, value: int):
        self._part_id = value

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
        """Number of failed cells.
        """
        return self._n_found

    @n_found.setter
    def n_found(self, value: int):
        self._n_found = value

    @property
    def max_quality(self) -> float:
        """Maximum value of quality measure.
        """
        return self._max_quality

    @max_quality.setter
    def max_quality(self, value: float):
        self._max_quality = value

    @property
    def min_quality(self) -> float:
        """Minimum value of quality measure.
        """
        return self._min_quality

    @min_quality.setter
    def min_quality(self, value: float):
        self._min_quality = value

class VolumeQualitySummaryResults(CoreObject):
    """Results of volume quality summary.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            quality_results_part: List[VolumeQualityResultsPart],
            message: str):
        self._error_code = ErrorCode(error_code)
        self._quality_results_part = quality_results_part
        self._message = message

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            quality_results_part: List[VolumeQualityResultsPart] = None,
            message: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumeQualitySummaryResults.

        Parameters
        ----------
        model: Model
            Model to create a VolumeQualitySummaryResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the volume quality summary.
        quality_results_part: List[VolumeQualityResultsPart], optional
            Contains volume quality result per cell quality measure by parts specified in parameters.
        message: str, optional
            Volume quality summary text.
        json_data: dict, optional
            JSON dictionary to create a VolumeQualitySummaryResults object with provided parameters.

        Examples
        --------
        >>> volume_quality_summary_results = prime.VolumeQualitySummaryResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [VolumeQualityResultsPart(model = model, json_data = data) for data in json_data["qualityResultsPart"]] if "qualityResultsPart" in json_data else None,
                json_data["message"] if "message" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, quality_results_part, message])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    quality_results_part,
                    message)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumeQualitySummaryResults")
                    json_data = param_json["VolumeQualitySummaryResults"] if "VolumeQualitySummaryResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( VolumeQualitySummaryResults._default_params["error_code"] if "error_code" in VolumeQualitySummaryResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        quality_results_part if quality_results_part is not None else ( VolumeQualitySummaryResults._default_params["quality_results_part"] if "quality_results_part" in VolumeQualitySummaryResults._default_params else [VolumeQualityResultsPart(model = model, json_data = data) for data in (json_data["qualityResultsPart"] if "qualityResultsPart" in json_data else None)]),
                        message if message is not None else ( VolumeQualitySummaryResults._default_params["message"] if "message" in VolumeQualitySummaryResults._default_params else (json_data["message"] if "message" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            quality_results_part: List[VolumeQualityResultsPart] = None,
            message: str = None):
        """Set the default values of VolumeQualitySummaryResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the volume quality summary.
        quality_results_part: List[VolumeQualityResultsPart], optional
            Contains volume quality result per cell quality measure by parts specified in parameters.
        message: str, optional
            Volume quality summary text.
        """
        args = locals()
        [VolumeQualitySummaryResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumeQualitySummaryResults.

        Examples
        --------
        >>> VolumeQualitySummaryResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumeQualitySummaryResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._quality_results_part is not None:
            json_data["qualityResultsPart"] = [data._jsonify() for data in self._quality_results_part]
        if self._message is not None:
            json_data["message"] = self._message
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nquality_results_part :  %s\nmessage :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._quality_results_part) + ']', self._message)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the volume quality summary.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def quality_results_part(self) -> List[VolumeQualityResultsPart]:
        """Contains volume quality result per cell quality measure by parts specified in parameters.
        """
        return self._quality_results_part

    @quality_results_part.setter
    def quality_results_part(self, value: List[VolumeQualityResultsPart]):
        self._quality_results_part = value

    @property
    def message(self) -> str:
        """Volume quality summary text.
        """
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

class VolumeQualitySummaryParams(CoreObject):
    """Parameters to control volume quality summary results.
    """
    _default_params = {}

    def __initialize(
            self,
            cell_quality_measures: List[CellQualityMeasure],
            scope: ScopeDefinition,
            quality_limit: Iterable[float]):
        self._cell_quality_measures = cell_quality_measures
        self._scope = scope
        self._quality_limit = quality_limit if isinstance(quality_limit, np.ndarray) else np.array(quality_limit, dtype=np.double) if quality_limit is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            cell_quality_measures: List[CellQualityMeasure] = None,
            scope: ScopeDefinition = None,
            quality_limit: Iterable[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumeQualitySummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a VolumeQualitySummaryParams object with default parameters.
        cell_quality_measures: List[CellQualityMeasure], optional
            List of cell quality measures for volume quality diagnostics.
        scope: ScopeDefinition, optional
            Scope of the cell zonelets for volume quality diagnostics.
        quality_limit: Iterable[float], optional
            Quality limit per cell quality measure. If the quality limit is not specified, the default quality limit is used.
        json_data: dict, optional
            JSON dictionary to create a VolumeQualitySummaryParams object with provided parameters.

        Examples
        --------
        >>> volume_quality_summary_params = prime.VolumeQualitySummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                [CellQualityMeasure(data) for data in json_data["cellQualityMeasures"]] if "cellQualityMeasures" in json_data else None,
                ScopeDefinition(model = model, json_data = json_data["scope"] if "scope" in json_data else None),
                json_data["qualityLimit"] if "qualityLimit" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [cell_quality_measures, scope, quality_limit])
            if all_field_specified:
                self.__initialize(
                    cell_quality_measures,
                    scope,
                    quality_limit)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumeQualitySummaryParams")
                    json_data = param_json["VolumeQualitySummaryParams"] if "VolumeQualitySummaryParams" in param_json else {}
                    self.__initialize(
                        cell_quality_measures if cell_quality_measures is not None else ( VolumeQualitySummaryParams._default_params["cell_quality_measures"] if "cell_quality_measures" in VolumeQualitySummaryParams._default_params else [CellQualityMeasure(data) for data in (json_data["cellQualityMeasures"] if "cellQualityMeasures" in json_data else None)]),
                        scope if scope is not None else ( VolumeQualitySummaryParams._default_params["scope"] if "scope" in VolumeQualitySummaryParams._default_params else ScopeDefinition(model = model, json_data = (json_data["scope"] if "scope" in json_data else None))),
                        quality_limit if quality_limit is not None else ( VolumeQualitySummaryParams._default_params["quality_limit"] if "quality_limit" in VolumeQualitySummaryParams._default_params else (json_data["qualityLimit"] if "qualityLimit" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            cell_quality_measures: List[CellQualityMeasure] = None,
            scope: ScopeDefinition = None,
            quality_limit: Iterable[float] = None):
        """Set the default values of VolumeQualitySummaryParams.

        Parameters
        ----------
        cell_quality_measures: List[CellQualityMeasure], optional
            List of cell quality measures for volume quality diagnostics.
        scope: ScopeDefinition, optional
            Scope of the cell zonelets for volume quality diagnostics.
        quality_limit: Iterable[float], optional
            Quality limit per cell quality measure. If the quality limit is not specified, the default quality limit is used.
        """
        args = locals()
        [VolumeQualitySummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumeQualitySummaryParams.

        Examples
        --------
        >>> VolumeQualitySummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumeQualitySummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._cell_quality_measures is not None:
            json_data["cellQualityMeasures"] = [data for data in self._cell_quality_measures]
        if self._scope is not None:
            json_data["scope"] = self._scope._jsonify()
        if self._quality_limit is not None:
            json_data["qualityLimit"] = self._quality_limit
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "cell_quality_measures :  %s\nscope :  %s\nquality_limit :  %s" % ('[' + ''.join('\n' + str(data) for data in self._cell_quality_measures) + ']', '{ ' + str(self._scope) + ' }', self._quality_limit)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def cell_quality_measures(self) -> List[CellQualityMeasure]:
        """List of cell quality measures for volume quality diagnostics.
        """
        return self._cell_quality_measures

    @cell_quality_measures.setter
    def cell_quality_measures(self, value: List[CellQualityMeasure]):
        self._cell_quality_measures = value

    @property
    def scope(self) -> ScopeDefinition:
        """Scope of the cell zonelets for volume quality diagnostics.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

    @property
    def quality_limit(self) -> Iterable[float]:
        """Quality limit per cell quality measure. If the quality limit is not specified, the default quality limit is used.
        """
        return self._quality_limit

    @quality_limit.setter
    def quality_limit(self, value: Iterable[float]):
        self._quality_limit = value
