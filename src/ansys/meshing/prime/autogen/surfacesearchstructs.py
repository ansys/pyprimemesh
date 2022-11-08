""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class SearchBySpikeParams(CoreObject):
    """Parameters to control spike detection.
    """
    _default_params = {}

    def __initialize(
            self,
            spike_angle: float):
        self._spike_angle = spike_angle

    def __init__(
            self,
            model: CommunicationManager=None,
            spike_angle: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SearchBySpikeParams.

        Parameters
        ----------
        model: Model
            Model to create a SearchBySpikeParams object with default parameters.
        spike_angle: float, optional
            Threshold angle for spike detection.
        json_data: dict, optional
            JSON dictionary to create a SearchBySpikeParams object with provided parameters.

        Examples
        --------
        >>> search_by_spike_params = prime.SearchBySpikeParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["spikeAngle"])
        else:
            all_field_specified = all(arg is not None for arg in [spike_angle])
            if all_field_specified:
                self.__initialize(
                    spike_angle)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SearchBySpikeParams")["SearchBySpikeParams"]
                    self.__initialize(
                        spike_angle if spike_angle is not None else ( SearchBySpikeParams._default_params["spike_angle"] if "spike_angle" in SearchBySpikeParams._default_params else json_data["spikeAngle"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            spike_angle: float = None):
        """Set the default values of SearchBySpikeParams.

        Parameters
        ----------
        spike_angle: float, optional
            Threshold angle for spike detection.
        """
        args = locals()
        [SearchBySpikeParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchBySpikeParams.

        Examples
        --------
        >>> SearchBySpikeParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchBySpikeParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["spikeAngle"] = self._spike_angle
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "spike_angle :  %s" % (self._spike_angle)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def spike_angle(self) -> float:
        """Threshold angle for spike detection.
        """
        return self._spike_angle

    @spike_angle.setter
    def spike_angle(self, value: float):
        self._spike_angle = value

class SearchBySpikeResults(CoreObject):
    """Results structure associated with search spikes operation.
    """
    _default_params = {}

    def __initialize(
            self,
            n_found: int,
            error_code: ErrorCode):
        self._n_found = n_found
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_found: int = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SearchBySpikeResults.

        Parameters
        ----------
        model: Model
            Model to create a SearchBySpikeResults object with default parameters.
        n_found: int, optional
            Number of spikes detected.
        error_code: ErrorCode, optional
            ErrorCode associated with search spikes operation.
        json_data: dict, optional
            JSON dictionary to create a SearchBySpikeResults object with provided parameters.

        Examples
        --------
        >>> search_by_spike_results = prime.SearchBySpikeResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nFound"],
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [n_found, error_code])
            if all_field_specified:
                self.__initialize(
                    n_found,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SearchBySpikeResults")["SearchBySpikeResults"]
                    self.__initialize(
                        n_found if n_found is not None else ( SearchBySpikeResults._default_params["n_found"] if "n_found" in SearchBySpikeResults._default_params else json_data["nFound"]),
                        error_code if error_code is not None else ( SearchBySpikeResults._default_params["error_code"] if "error_code" in SearchBySpikeResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_found: int = None,
            error_code: ErrorCode = None):
        """Set the default values of SearchBySpikeResults.

        Parameters
        ----------
        n_found: int, optional
            Number of spikes detected.
        error_code: ErrorCode, optional
            ErrorCode associated with search spikes operation.
        """
        args = locals()
        [SearchBySpikeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchBySpikeResults.

        Examples
        --------
        >>> SearchBySpikeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchBySpikeResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["nFound"] = self._n_found
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_found :  %s\nerror_code :  %s" % (self._n_found, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_found(self) -> int:
        """Number of spikes detected.
        """
        return self._n_found

    @n_found.setter
    def n_found(self, value: int):
        self._n_found = value

    @property
    def error_code(self) -> ErrorCode:
        """ErrorCode associated with search spikes operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class SearchByFoldsParams(CoreObject):
    """Parameters to control fold detection.
    """
    _default_params = {}

    def __initialize(
            self,
            critical_angle: float):
        self._critical_angle = critical_angle

    def __init__(
            self,
            model: CommunicationManager=None,
            critical_angle: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SearchByFoldsParams.

        Parameters
        ----------
        model: Model
            Model to create a SearchByFoldsParams object with default parameters.
        critical_angle: float, optional
            Threshold angle for fold detection.
        json_data: dict, optional
            JSON dictionary to create a SearchByFoldsParams object with provided parameters.

        Examples
        --------
        >>> search_by_folds_params = prime.SearchByFoldsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["criticalAngle"])
        else:
            all_field_specified = all(arg is not None for arg in [critical_angle])
            if all_field_specified:
                self.__initialize(
                    critical_angle)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SearchByFoldsParams")["SearchByFoldsParams"]
                    self.__initialize(
                        critical_angle if critical_angle is not None else ( SearchByFoldsParams._default_params["critical_angle"] if "critical_angle" in SearchByFoldsParams._default_params else json_data["criticalAngle"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            critical_angle: float = None):
        """Set the default values of SearchByFoldsParams.

        Parameters
        ----------
        critical_angle: float, optional
            Threshold angle for fold detection.
        """
        args = locals()
        [SearchByFoldsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByFoldsParams.

        Examples
        --------
        >>> SearchByFoldsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByFoldsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["criticalAngle"] = self._critical_angle
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "critical_angle :  %s" % (self._critical_angle)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def critical_angle(self) -> float:
        """Threshold angle for fold detection.
        """
        return self._critical_angle

    @critical_angle.setter
    def critical_angle(self, value: float):
        self._critical_angle = value

class SearchByFoldsResults(CoreObject):
    """Results structure associated with search folds operation.
    """
    _default_params = {}

    def __initialize(
            self,
            n_found: int,
            error_code: ErrorCode):
        self._n_found = n_found
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_found: int = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SearchByFoldsResults.

        Parameters
        ----------
        model: Model
            Model to create a SearchByFoldsResults object with default parameters.
        n_found: int, optional
            Number of folds identified.
        error_code: ErrorCode, optional
            ErrorCode associated with search folds operation.
        json_data: dict, optional
            JSON dictionary to create a SearchByFoldsResults object with provided parameters.

        Examples
        --------
        >>> search_by_folds_results = prime.SearchByFoldsResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nFound"],
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [n_found, error_code])
            if all_field_specified:
                self.__initialize(
                    n_found,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SearchByFoldsResults")["SearchByFoldsResults"]
                    self.__initialize(
                        n_found if n_found is not None else ( SearchByFoldsResults._default_params["n_found"] if "n_found" in SearchByFoldsResults._default_params else json_data["nFound"]),
                        error_code if error_code is not None else ( SearchByFoldsResults._default_params["error_code"] if "error_code" in SearchByFoldsResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_found: int = None,
            error_code: ErrorCode = None):
        """Set the default values of SearchByFoldsResults.

        Parameters
        ----------
        n_found: int, optional
            Number of folds identified.
        error_code: ErrorCode, optional
            ErrorCode associated with search folds operation.
        """
        args = locals()
        [SearchByFoldsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByFoldsResults.

        Examples
        --------
        >>> SearchByFoldsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByFoldsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["nFound"] = self._n_found
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_found :  %s\nerror_code :  %s" % (self._n_found, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_found(self) -> int:
        """Number of folds identified.
        """
        return self._n_found

    @n_found.setter
    def n_found(self, value: int):
        self._n_found = value

    @property
    def error_code(self) -> ErrorCode:
        """ErrorCode associated with search folds operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class SearchBySelfIntersectionParams(CoreObject):
    """Parameters to search by face element intersection. This is for internal use only.
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
        """Initializes the SearchBySelfIntersectionParams.

        Parameters
        ----------
        model: Model
            Model to create a SearchBySelfIntersectionParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SearchBySelfIntersectionParams object with provided parameters.

        Examples
        --------
        >>> search_by_self_intersection_params = prime.SearchBySelfIntersectionParams(model = model)
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
                    json_data = model._communicator.initialize_params(model, "SearchBySelfIntersectionParams")["SearchBySelfIntersectionParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SearchBySelfIntersectionParams.

        """
        args = locals()
        [SearchBySelfIntersectionParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchBySelfIntersectionParams.

        Examples
        --------
        >>> SearchBySelfIntersectionParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchBySelfIntersectionParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SearchByIntersectionResults(CoreObject):
    """Results associated with search by face element intersection. This is for internal use only.
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
        """Initializes the SearchByIntersectionResults.

        Parameters
        ----------
        model: Model
            Model to create a SearchByIntersectionResults object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SearchByIntersectionResults object with provided parameters.

        Examples
        --------
        >>> search_by_intersection_results = prime.SearchByIntersectionResults(model = model)
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
                    json_data = model._communicator.initialize_params(model, "SearchByIntersectionResults")["SearchByIntersectionResults"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SearchByIntersectionResults.

        """
        args = locals()
        [SearchByIntersectionResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByIntersectionResults.

        Examples
        --------
        >>> SearchByIntersectionResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByIntersectionResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SearchByQualityParams(CoreObject):
    """Parameters to control search by quality results.
    """
    _default_params = {}

    def __initialize(
            self,
            quality_limit: float,
            face_quality_measure: FaceQualityMeasure):
        self._quality_limit = quality_limit
        self._face_quality_measure = FaceQualityMeasure(face_quality_measure)

    def __init__(
            self,
            model: CommunicationManager=None,
            quality_limit: float = None,
            face_quality_measure: FaceQualityMeasure = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SearchByQualityParams.

        Parameters
        ----------
        model: Model
            Model to create a SearchByQualityParams object with default parameters.
        quality_limit: float, optional
            Quality limit used for search face elements.
        face_quality_measure: FaceQualityMeasure, optional
            Quality measure used for search face elements.
        json_data: dict, optional
            JSON dictionary to create a SearchByQualityParams object with provided parameters.

        Examples
        --------
        >>> search_by_quality_params = prime.SearchByQualityParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["qualityLimit"],
                FaceQualityMeasure(json_data["faceQualityMeasure"]))
        else:
            all_field_specified = all(arg is not None for arg in [quality_limit, face_quality_measure])
            if all_field_specified:
                self.__initialize(
                    quality_limit,
                    face_quality_measure)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SearchByQualityParams")["SearchByQualityParams"]
                    self.__initialize(
                        quality_limit if quality_limit is not None else ( SearchByQualityParams._default_params["quality_limit"] if "quality_limit" in SearchByQualityParams._default_params else json_data["qualityLimit"]),
                        face_quality_measure if face_quality_measure is not None else ( SearchByQualityParams._default_params["face_quality_measure"] if "face_quality_measure" in SearchByQualityParams._default_params else FaceQualityMeasure(json_data["faceQualityMeasure"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            quality_limit: float = None,
            face_quality_measure: FaceQualityMeasure = None):
        """Set the default values of SearchByQualityParams.

        Parameters
        ----------
        quality_limit: float, optional
            Quality limit used for search face elements.
        face_quality_measure: FaceQualityMeasure, optional
            Quality measure used for search face elements.
        """
        args = locals()
        [SearchByQualityParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByQualityParams.

        Examples
        --------
        >>> SearchByQualityParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByQualityParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["qualityLimit"] = self._quality_limit
        json_data["faceQualityMeasure"] = self._face_quality_measure
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "quality_limit :  %s\nface_quality_measure :  %s" % (self._quality_limit, self._face_quality_measure)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def quality_limit(self) -> float:
        """Quality limit used for search face elements.
        """
        return self._quality_limit

    @quality_limit.setter
    def quality_limit(self, value: float):
        self._quality_limit = value

    @property
    def face_quality_measure(self) -> FaceQualityMeasure:
        """Quality measure used for search face elements.
        """
        return self._face_quality_measure

    @face_quality_measure.setter
    def face_quality_measure(self, value: FaceQualityMeasure):
        self._face_quality_measure = value

class SearchByQualityResults(CoreObject):
    """Results of search by quality.
    """
    _default_params = {}

    def __initialize(
            self,
            n_found: int,
            error_code: ErrorCode,
            max_quality: float,
            min_quality: float):
        self._n_found = n_found
        self._error_code = ErrorCode(error_code)
        self._max_quality = max_quality
        self._min_quality = min_quality

    def __init__(
            self,
            model: CommunicationManager=None,
            n_found: int = None,
            error_code: ErrorCode = None,
            max_quality: float = None,
            min_quality: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SearchByQualityResults.

        Parameters
        ----------
        model: Model
            Model to create a SearchByQualityResults object with default parameters.
        n_found: int, optional
            Number of face elements found by search for given quality limit.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        max_quality: float, optional
            Maximum quality found by search.
        min_quality: float, optional
            Minimum quality found by search.
        json_data: dict, optional
            JSON dictionary to create a SearchByQualityResults object with provided parameters.

        Examples
        --------
        >>> search_by_quality_results = prime.SearchByQualityResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nFound"],
                ErrorCode(json_data["errorCode"]),
                json_data["maxQuality"],
                json_data["minQuality"])
        else:
            all_field_specified = all(arg is not None for arg in [n_found, error_code, max_quality, min_quality])
            if all_field_specified:
                self.__initialize(
                    n_found,
                    error_code,
                    max_quality,
                    min_quality)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SearchByQualityResults")["SearchByQualityResults"]
                    self.__initialize(
                        n_found if n_found is not None else ( SearchByQualityResults._default_params["n_found"] if "n_found" in SearchByQualityResults._default_params else json_data["nFound"]),
                        error_code if error_code is not None else ( SearchByQualityResults._default_params["error_code"] if "error_code" in SearchByQualityResults._default_params else ErrorCode(json_data["errorCode"])),
                        max_quality if max_quality is not None else ( SearchByQualityResults._default_params["max_quality"] if "max_quality" in SearchByQualityResults._default_params else json_data["maxQuality"]),
                        min_quality if min_quality is not None else ( SearchByQualityResults._default_params["min_quality"] if "min_quality" in SearchByQualityResults._default_params else json_data["minQuality"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_found: int = None,
            error_code: ErrorCode = None,
            max_quality: float = None,
            min_quality: float = None):
        """Set the default values of SearchByQualityResults.

        Parameters
        ----------
        n_found: int, optional
            Number of face elements found by search for given quality limit.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        max_quality: float, optional
            Maximum quality found by search.
        min_quality: float, optional
            Minimum quality found by search.
        """
        args = locals()
        [SearchByQualityResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByQualityResults.

        Examples
        --------
        >>> SearchByQualityResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByQualityResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["nFound"] = self._n_found
        json_data["errorCode"] = self._error_code
        json_data["maxQuality"] = self._max_quality
        json_data["minQuality"] = self._min_quality
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_found :  %s\nerror_code :  %s\nmax_quality :  %s\nmin_quality :  %s" % (self._n_found, self._error_code, self._max_quality, self._min_quality)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_found(self) -> int:
        """Number of face elements found by search for given quality limit.
        """
        return self._n_found

    @n_found.setter
    def n_found(self, value: int):
        self._n_found = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def max_quality(self) -> float:
        """Maximum quality found by search.
        """
        return self._max_quality

    @max_quality.setter
    def max_quality(self, value: float):
        self._max_quality = value

    @property
    def min_quality(self) -> float:
        """Minimum quality found by search.
        """
        return self._min_quality

    @min_quality.setter
    def min_quality(self, value: float):
        self._min_quality = value

class SearchByThinStripParams(CoreObject):
    """Parameters to search by thin strip of face elements. This is for internal use only.
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
        """Initializes the SearchByThinStripParams.

        Parameters
        ----------
        model: Model
            Model to create a SearchByThinStripParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SearchByThinStripParams object with provided parameters.

        Examples
        --------
        >>> search_by_thin_strip_params = prime.SearchByThinStripParams(model = model)
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
                    json_data = model._communicator.initialize_params(model, "SearchByThinStripParams")["SearchByThinStripParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SearchByThinStripParams.

        """
        args = locals()
        [SearchByThinStripParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByThinStripParams.

        Examples
        --------
        >>> SearchByThinStripParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByThinStripParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SearchByThinStripResults(CoreObject):
    """Results associated with search by thin strip of face elements. This is for internal use only.
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
        """Initializes the SearchByThinStripResults.

        Parameters
        ----------
        model: Model
            Model to create a SearchByThinStripResults object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SearchByThinStripResults object with provided parameters.

        Examples
        --------
        >>> search_by_thin_strip_results = prime.SearchByThinStripResults(model = model)
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
                    json_data = model._communicator.initialize_params(model, "SearchByThinStripResults")["SearchByThinStripResults"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SearchByThinStripResults.

        """
        args = locals()
        [SearchByThinStripResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SearchByThinStripResults.

        Examples
        --------
        >>> SearchByThinStripResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SearchByThinStripResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SurfaceQualityResult(CoreObject):
    """Result of surface quality.
    """
    _default_params = {}

    def __initialize(
            self,
            face_quality_measure: FaceQualityMeasure,
            measure_name: str,
            quality_limit: float,
            n_found: int,
            max_quality: float,
            min_quality: float):
        self._face_quality_measure = FaceQualityMeasure(face_quality_measure)
        self._measure_name = measure_name
        self._quality_limit = quality_limit
        self._n_found = n_found
        self._max_quality = max_quality
        self._min_quality = min_quality

    def __init__(
            self,
            model: CommunicationManager=None,
            face_quality_measure: FaceQualityMeasure = None,
            measure_name: str = None,
            quality_limit: float = None,
            n_found: int = None,
            max_quality: float = None,
            min_quality: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurfaceQualityResult.

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
        max_quality: float, optional
            Maximum value of quality measure.
        min_quality: float, optional
            Minimum value of quality measure.
        json_data: dict, optional
            JSON dictionary to create a SurfaceQualityResult object with provided parameters.

        Examples
        --------
        >>> surface_quality_result = prime.SurfaceQualityResult(model = model)
        """
        if json_data:
            self.__initialize(
                FaceQualityMeasure(json_data["faceQualityMeasure"]),
                json_data["measureName"],
                json_data["qualityLimit"],
                json_data["nFound"],
                json_data["maxQuality"],
                json_data["minQuality"])
        else:
            all_field_specified = all(arg is not None for arg in [face_quality_measure, measure_name, quality_limit, n_found, max_quality, min_quality])
            if all_field_specified:
                self.__initialize(
                    face_quality_measure,
                    measure_name,
                    quality_limit,
                    n_found,
                    max_quality,
                    min_quality)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SurfaceQualityResult")["SurfaceQualityResult"]
                    self.__initialize(
                        face_quality_measure if face_quality_measure is not None else ( SurfaceQualityResult._default_params["face_quality_measure"] if "face_quality_measure" in SurfaceQualityResult._default_params else FaceQualityMeasure(json_data["faceQualityMeasure"])),
                        measure_name if measure_name is not None else ( SurfaceQualityResult._default_params["measure_name"] if "measure_name" in SurfaceQualityResult._default_params else json_data["measureName"]),
                        quality_limit if quality_limit is not None else ( SurfaceQualityResult._default_params["quality_limit"] if "quality_limit" in SurfaceQualityResult._default_params else json_data["qualityLimit"]),
                        n_found if n_found is not None else ( SurfaceQualityResult._default_params["n_found"] if "n_found" in SurfaceQualityResult._default_params else json_data["nFound"]),
                        max_quality if max_quality is not None else ( SurfaceQualityResult._default_params["max_quality"] if "max_quality" in SurfaceQualityResult._default_params else json_data["maxQuality"]),
                        min_quality if min_quality is not None else ( SurfaceQualityResult._default_params["min_quality"] if "min_quality" in SurfaceQualityResult._default_params else json_data["minQuality"]))
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
            max_quality: float = None,
            min_quality: float = None):
        """Set the default values of SurfaceQualityResult.

        Parameters
        ----------
        face_quality_measure: FaceQualityMeasure, optional
            Type of the face quality measure.
        measure_name: str, optional
            Name of the face quality measure.
        quality_limit: float, optional
            Target quality limit used to find failures.
        n_found: int, optional
            Number of failed faces.
        max_quality: float, optional
            Maximum value of quality measure.
        min_quality: float, optional
            Minimum value of quality measure.
        """
        args = locals()
        [SurfaceQualityResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurfaceQualityResult.

        Examples
        --------
        >>> SurfaceQualityResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceQualityResult._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["faceQualityMeasure"] = self._face_quality_measure
        json_data["measureName"] = self._measure_name
        json_data["qualityLimit"] = self._quality_limit
        json_data["nFound"] = self._n_found
        json_data["maxQuality"] = self._max_quality
        json_data["minQuality"] = self._min_quality
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "face_quality_measure :  %s\nmeasure_name :  %s\nquality_limit :  %s\nn_found :  %s\nmax_quality :  %s\nmin_quality :  %s" % (self._face_quality_measure, self._measure_name, self._quality_limit, self._n_found, self._max_quality, self._min_quality)
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

class SurfaceQualitySummaryResults(CoreObject):
    """Results of surface quality summary.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            quality_results: List[SurfaceQualityResult],
            summary: str):
        self._error_code = ErrorCode(error_code)
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
        """Initializes the SurfaceQualitySummaryResults.

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
        >>> surface_quality_summary_results = prime.SurfaceQualitySummaryResults(model = model)
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
                    json_data = model._communicator.initialize_params(model, "SurfaceQualitySummaryResults")["SurfaceQualitySummaryResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( SurfaceQualitySummaryResults._default_params["error_code"] if "error_code" in SurfaceQualitySummaryResults._default_params else ErrorCode(json_data["errorCode"])),
                        quality_results if quality_results is not None else ( SurfaceQualitySummaryResults._default_params["quality_results"] if "quality_results" in SurfaceQualitySummaryResults._default_params else [SurfaceQualityResult(model = model, json_data = data) for data in json_data["qualityResults"]]),
                        summary if summary is not None else ( SurfaceQualitySummaryResults._default_params["summary"] if "summary" in SurfaceQualitySummaryResults._default_params else json_data["summary"]))
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
        """Set the default values of SurfaceQualitySummaryResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the surface quality summary.
        quality_results: List[SurfaceQualityResult], optional
            Contains surface quality result per face quality measure specified in parameters.
        summary: str, optional
            Surface quality summary text.
        """
        args = locals()
        [SurfaceQualitySummaryResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurfaceQualitySummaryResults.

        Examples
        --------
        >>> SurfaceQualitySummaryResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceQualitySummaryResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["qualityResults"] = [data._jsonify() for data in self._quality_results]
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
    _default_params = {}

    def __initialize(
            self,
            face_quality_measures: List[FaceQualityMeasure],
            scope: ScopeDefinition,
            quality_limit: Iterable[float]):
        self._face_quality_measures = face_quality_measures
        self._scope = scope
        self._quality_limit = quality_limit if isinstance(quality_limit, np.ndarray) else np.array(quality_limit, dtype=np.double)

    def __init__(
            self,
            model: CommunicationManager=None,
            face_quality_measures: List[FaceQualityMeasure] = None,
            scope: ScopeDefinition = None,
            quality_limit: Iterable[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurfaceQualitySummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a SurfaceQualitySummaryParams object with default parameters.
        face_quality_measures: List[FaceQualityMeasure], optional
            List of face quality measures for surface quality diagnostics.
        scope: ScopeDefinition, optional
            Scope the face zonelets for surface quality diagnostics.
        quality_limit: Iterable[float], optional
            Quality limit per face quality measure. If the quality limit is not specified, the default quality limit is used.
        json_data: dict, optional
            JSON dictionary to create a SurfaceQualitySummaryParams object with provided parameters.

        Examples
        --------
        >>> surface_quality_summary_params = prime.SurfaceQualitySummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                [FaceQualityMeasure(data) for data in json_data["faceQualityMeasures"]],
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
                    json_data = model._communicator.initialize_params(model, "SurfaceQualitySummaryParams")["SurfaceQualitySummaryParams"]
                    self.__initialize(
                        face_quality_measures if face_quality_measures is not None else ( SurfaceQualitySummaryParams._default_params["face_quality_measures"] if "face_quality_measures" in SurfaceQualitySummaryParams._default_params else [FaceQualityMeasure(data) for data in json_data["faceQualityMeasures"]]),
                        scope if scope is not None else ( SurfaceQualitySummaryParams._default_params["scope"] if "scope" in SurfaceQualitySummaryParams._default_params else ScopeDefinition(model = model, json_data = json_data["scope"])),
                        quality_limit if quality_limit is not None else ( SurfaceQualitySummaryParams._default_params["quality_limit"] if "quality_limit" in SurfaceQualitySummaryParams._default_params else json_data["qualityLimit"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            face_quality_measures: List[FaceQualityMeasure] = None,
            scope: ScopeDefinition = None,
            quality_limit: Iterable[float] = None):
        """Set the default values of SurfaceQualitySummaryParams.

        Parameters
        ----------
        face_quality_measures: List[FaceQualityMeasure], optional
            List of face quality measures for surface quality diagnostics.
        scope: ScopeDefinition, optional
            Scope the face zonelets for surface quality diagnostics.
        quality_limit: Iterable[float], optional
            Quality limit per face quality measure. If the quality limit is not specified, the default quality limit is used.
        """
        args = locals()
        [SurfaceQualitySummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurfaceQualitySummaryParams.

        Examples
        --------
        >>> SurfaceQualitySummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceQualitySummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["faceQualityMeasures"] = [data for data in self._face_quality_measures]
        json_data["scope"] = self._scope._jsonify()
        json_data["qualityLimit"] = self._quality_limit
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "face_quality_measures :  %s\nscope :  %s\nquality_limit :  %s" % ('[' + ''.join('\n' + str(data) for data in self._face_quality_measures) + ']', '{ ' + str(self._scope) + ' }', self._quality_limit)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def face_quality_measures(self) -> List[FaceQualityMeasure]:
        """List of face quality measures for surface quality diagnostics.
        """
        return self._face_quality_measures

    @face_quality_measures.setter
    def face_quality_measures(self, value: List[FaceQualityMeasure]):
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
    def quality_limit(self) -> Iterable[float]:
        """Quality limit per face quality measure. If the quality limit is not specified, the default quality limit is used.
        """
        return self._quality_limit

    @quality_limit.setter
    def quality_limit(self, value: Iterable[float]):
        self._quality_limit = value

class SurfaceDiagnosticSummaryResults(CoreObject):
    """Results of surface diagnostic summary.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            n_self_intersections: int,
            n_free_edges: int,
            n_multi_edges: int,
            n_duplicate_faces: int):
        self._error_code = ErrorCode(error_code)
        self._n_self_intersections = n_self_intersections
        self._n_free_edges = n_free_edges
        self._n_multi_edges = n_multi_edges
        self._n_duplicate_faces = n_duplicate_faces

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            n_self_intersections: int = None,
            n_free_edges: int = None,
            n_multi_edges: int = None,
            n_duplicate_faces: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurfaceDiagnosticSummaryResults.

        Parameters
        ----------
        model: Model
            Model to create a SurfaceDiagnosticSummaryResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the surface diagnostic summary.
        n_self_intersections: int, optional
            Number of self intersecting faces identified.
        n_free_edges: int, optional
            Number of free face edges identified.
        n_multi_edges: int, optional
            Number of multi face edges identified.
        n_duplicate_faces: int, optional
            Number of duplicate faces identified.
        json_data: dict, optional
            JSON dictionary to create a SurfaceDiagnosticSummaryResults object with provided parameters.

        Examples
        --------
        >>> surface_diagnostic_summary_results = prime.SurfaceDiagnosticSummaryResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]),
                json_data["nSelfIntersections"],
                json_data["nFreeEdges"],
                json_data["nMultiEdges"],
                json_data["nDuplicateFaces"])
        else:
            all_field_specified = all(arg is not None for arg in [error_code, n_self_intersections, n_free_edges, n_multi_edges, n_duplicate_faces])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    n_self_intersections,
                    n_free_edges,
                    n_multi_edges,
                    n_duplicate_faces)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SurfaceDiagnosticSummaryResults")["SurfaceDiagnosticSummaryResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( SurfaceDiagnosticSummaryResults._default_params["error_code"] if "error_code" in SurfaceDiagnosticSummaryResults._default_params else ErrorCode(json_data["errorCode"])),
                        n_self_intersections if n_self_intersections is not None else ( SurfaceDiagnosticSummaryResults._default_params["n_self_intersections"] if "n_self_intersections" in SurfaceDiagnosticSummaryResults._default_params else json_data["nSelfIntersections"]),
                        n_free_edges if n_free_edges is not None else ( SurfaceDiagnosticSummaryResults._default_params["n_free_edges"] if "n_free_edges" in SurfaceDiagnosticSummaryResults._default_params else json_data["nFreeEdges"]),
                        n_multi_edges if n_multi_edges is not None else ( SurfaceDiagnosticSummaryResults._default_params["n_multi_edges"] if "n_multi_edges" in SurfaceDiagnosticSummaryResults._default_params else json_data["nMultiEdges"]),
                        n_duplicate_faces if n_duplicate_faces is not None else ( SurfaceDiagnosticSummaryResults._default_params["n_duplicate_faces"] if "n_duplicate_faces" in SurfaceDiagnosticSummaryResults._default_params else json_data["nDuplicateFaces"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            n_self_intersections: int = None,
            n_free_edges: int = None,
            n_multi_edges: int = None,
            n_duplicate_faces: int = None):
        """Set the default values of SurfaceDiagnosticSummaryResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the surface diagnostic summary.
        n_self_intersections: int, optional
            Number of self intersecting faces identified.
        n_free_edges: int, optional
            Number of free face edges identified.
        n_multi_edges: int, optional
            Number of multi face edges identified.
        n_duplicate_faces: int, optional
            Number of duplicate faces identified.
        """
        args = locals()
        [SurfaceDiagnosticSummaryResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurfaceDiagnosticSummaryResults.

        Examples
        --------
        >>> SurfaceDiagnosticSummaryResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceDiagnosticSummaryResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        json_data["nSelfIntersections"] = self._n_self_intersections
        json_data["nFreeEdges"] = self._n_free_edges
        json_data["nMultiEdges"] = self._n_multi_edges
        json_data["nDuplicateFaces"] = self._n_duplicate_faces
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nn_self_intersections :  %s\nn_free_edges :  %s\nn_multi_edges :  %s\nn_duplicate_faces :  %s" % (self._error_code, self._n_self_intersections, self._n_free_edges, self._n_multi_edges, self._n_duplicate_faces)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the surface diagnostic summary.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def n_self_intersections(self) -> int:
        """Number of self intersecting faces identified.
        """
        return self._n_self_intersections

    @n_self_intersections.setter
    def n_self_intersections(self, value: int):
        self._n_self_intersections = value

    @property
    def n_free_edges(self) -> int:
        """Number of free face edges identified.
        """
        return self._n_free_edges

    @n_free_edges.setter
    def n_free_edges(self, value: int):
        self._n_free_edges = value

    @property
    def n_multi_edges(self) -> int:
        """Number of multi face edges identified.
        """
        return self._n_multi_edges

    @n_multi_edges.setter
    def n_multi_edges(self, value: int):
        self._n_multi_edges = value

    @property
    def n_duplicate_faces(self) -> int:
        """Number of duplicate faces identified.
        """
        return self._n_duplicate_faces

    @n_duplicate_faces.setter
    def n_duplicate_faces(self, value: int):
        self._n_duplicate_faces = value

class SurfaceDiagnosticSummaryParams(CoreObject):
    """Parameters to control surface diagnostics summary results.
    """
    _default_params = {}

    def __initialize(
            self,
            scope: ScopeDefinition,
            compute_self_intersections: bool,
            compute_free_edges: bool,
            compute_multi_edges: bool,
            compute_duplicate_faces: bool):
        self._scope = scope
        self._compute_self_intersections = compute_self_intersections
        self._compute_free_edges = compute_free_edges
        self._compute_multi_edges = compute_multi_edges
        self._compute_duplicate_faces = compute_duplicate_faces

    def __init__(
            self,
            model: CommunicationManager=None,
            scope: ScopeDefinition = None,
            compute_self_intersections: bool = None,
            compute_free_edges: bool = None,
            compute_multi_edges: bool = None,
            compute_duplicate_faces: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SurfaceDiagnosticSummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a SurfaceDiagnosticSummaryParams object with default parameters.
        scope: ScopeDefinition, optional
            Scope the face zonelets for surface diagnostics.
        compute_self_intersections: bool, optional
            Control to identify face intersections are present or not.
        compute_free_edges: bool, optional
            Control to identify free face edges are present or not.
        compute_multi_edges: bool, optional
            Control to identify multi face edges are present or not.
        compute_duplicate_faces: bool, optional
            Control to identify duplicate faces are present or not.
        json_data: dict, optional
            JSON dictionary to create a SurfaceDiagnosticSummaryParams object with provided parameters.

        Examples
        --------
        >>> surface_diagnostic_summary_params = prime.SurfaceDiagnosticSummaryParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["scope"]),
                json_data["computeSelfIntersections"],
                json_data["computeFreeEdges"],
                json_data["computeMultiEdges"],
                json_data["computeDuplicateFaces"])
        else:
            all_field_specified = all(arg is not None for arg in [scope, compute_self_intersections, compute_free_edges, compute_multi_edges, compute_duplicate_faces])
            if all_field_specified:
                self.__initialize(
                    scope,
                    compute_self_intersections,
                    compute_free_edges,
                    compute_multi_edges,
                    compute_duplicate_faces)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params(model, "SurfaceDiagnosticSummaryParams")["SurfaceDiagnosticSummaryParams"]
                    self.__initialize(
                        scope if scope is not None else ( SurfaceDiagnosticSummaryParams._default_params["scope"] if "scope" in SurfaceDiagnosticSummaryParams._default_params else ScopeDefinition(model = model, json_data = json_data["scope"])),
                        compute_self_intersections if compute_self_intersections is not None else ( SurfaceDiagnosticSummaryParams._default_params["compute_self_intersections"] if "compute_self_intersections" in SurfaceDiagnosticSummaryParams._default_params else json_data["computeSelfIntersections"]),
                        compute_free_edges if compute_free_edges is not None else ( SurfaceDiagnosticSummaryParams._default_params["compute_free_edges"] if "compute_free_edges" in SurfaceDiagnosticSummaryParams._default_params else json_data["computeFreeEdges"]),
                        compute_multi_edges if compute_multi_edges is not None else ( SurfaceDiagnosticSummaryParams._default_params["compute_multi_edges"] if "compute_multi_edges" in SurfaceDiagnosticSummaryParams._default_params else json_data["computeMultiEdges"]),
                        compute_duplicate_faces if compute_duplicate_faces is not None else ( SurfaceDiagnosticSummaryParams._default_params["compute_duplicate_faces"] if "compute_duplicate_faces" in SurfaceDiagnosticSummaryParams._default_params else json_data["computeDuplicateFaces"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            scope: ScopeDefinition = None,
            compute_self_intersections: bool = None,
            compute_free_edges: bool = None,
            compute_multi_edges: bool = None,
            compute_duplicate_faces: bool = None):
        """Set the default values of SurfaceDiagnosticSummaryParams.

        Parameters
        ----------
        scope: ScopeDefinition, optional
            Scope the face zonelets for surface diagnostics.
        compute_self_intersections: bool, optional
            Control to identify face intersections are present or not.
        compute_free_edges: bool, optional
            Control to identify free face edges are present or not.
        compute_multi_edges: bool, optional
            Control to identify multi face edges are present or not.
        compute_duplicate_faces: bool, optional
            Control to identify duplicate faces are present or not.
        """
        args = locals()
        [SurfaceDiagnosticSummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SurfaceDiagnosticSummaryParams.

        Examples
        --------
        >>> SurfaceDiagnosticSummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceDiagnosticSummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["scope"] = self._scope._jsonify()
        json_data["computeSelfIntersections"] = self._compute_self_intersections
        json_data["computeFreeEdges"] = self._compute_free_edges
        json_data["computeMultiEdges"] = self._compute_multi_edges
        json_data["computeDuplicateFaces"] = self._compute_duplicate_faces
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "scope :  %s\ncompute_self_intersections :  %s\ncompute_free_edges :  %s\ncompute_multi_edges :  %s\ncompute_duplicate_faces :  %s" % ('{ ' + str(self._scope) + ' }', self._compute_self_intersections, self._compute_free_edges, self._compute_multi_edges, self._compute_duplicate_faces)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def scope(self) -> ScopeDefinition:
        """Scope the face zonelets for surface diagnostics.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

    @property
    def compute_self_intersections(self) -> bool:
        """Control to identify face intersections are present or not.
        """
        return self._compute_self_intersections

    @compute_self_intersections.setter
    def compute_self_intersections(self, value: bool):
        self._compute_self_intersections = value

    @property
    def compute_free_edges(self) -> bool:
        """Control to identify free face edges are present or not.
        """
        return self._compute_free_edges

    @compute_free_edges.setter
    def compute_free_edges(self, value: bool):
        self._compute_free_edges = value

    @property
    def compute_multi_edges(self) -> bool:
        """Control to identify multi face edges are present or not.
        """
        return self._compute_multi_edges

    @compute_multi_edges.setter
    def compute_multi_edges(self, value: bool):
        self._compute_multi_edges = value

    @property
    def compute_duplicate_faces(self) -> bool:
        """Control to identify duplicate faces are present or not.
        """
        return self._compute_duplicate_faces

    @compute_duplicate_faces.setter
    def compute_duplicate_faces(self, value: bool):
        self._compute_duplicate_faces = value
