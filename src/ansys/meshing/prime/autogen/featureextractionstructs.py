""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class ExtractFeatureParams(CoreObject):
    """Parameter to control feature edge extraction.
    """
    _default_params = {}

    def __initialize(
            self,
            replace: bool,
            feature_angle: float,
            separate_features: bool,
            separation_angle: float,
            disconnect_with_faces: bool,
            label_name: str):
        self._replace = replace
        self._feature_angle = feature_angle
        self._separate_features = separate_features
        self._separation_angle = separation_angle
        self._disconnect_with_faces = disconnect_with_faces
        self._label_name = label_name

    def __init__(
            self,
            model: CommunicationManager=None,
            replace: bool = None,
            feature_angle: float = None,
            separate_features: bool = None,
            separation_angle: float = None,
            disconnect_with_faces: bool = None,
            label_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractFeatureParams.

        Parameters
        ----------
        model: Model
            Model to create a ExtractFeatureParams object with default parameters.
        replace: bool, optional
            Option to replace existing edge zonelets with new extracted edge zonelets.
        feature_angle: float, optional
            Angle used to capture face features to be  extracted as edges.
        separate_features: bool, optional
            Option to separate extracted features.
        separation_angle: float, optional
            Angle used to separate extracted features.
        disconnect_with_faces: bool, optional
            Option to disconnect edges from faces. If false, edges remain connected to faces by sharing nodes.
        label_name: str, optional
            Label name to be assigned to extracted features.
        json_data: dict, optional
            JSON dictionary to create a ExtractFeatureParams object with provided parameters.

        Examples
        --------
        >>> extract_feature_params = prime.ExtractFeatureParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["replace"] if "replace" in json_data else None,
                json_data["featureAngle"] if "featureAngle" in json_data else None,
                json_data["separateFeatures"] if "separateFeatures" in json_data else None,
                json_data["separationAngle"] if "separationAngle" in json_data else None,
                json_data["disconnectWithFaces"] if "disconnectWithFaces" in json_data else None,
                json_data["labelName"] if "labelName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [replace, feature_angle, separate_features, separation_angle, disconnect_with_faces, label_name])
            if all_field_specified:
                self.__initialize(
                    replace,
                    feature_angle,
                    separate_features,
                    separation_angle,
                    disconnect_with_faces,
                    label_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractFeatureParams")
                    json_data = param_json["ExtractFeatureParams"] if "ExtractFeatureParams" in param_json else {}
                    self.__initialize(
                        replace if replace is not None else ( ExtractFeatureParams._default_params["replace"] if "replace" in ExtractFeatureParams._default_params else (json_data["replace"] if "replace" in json_data else None)),
                        feature_angle if feature_angle is not None else ( ExtractFeatureParams._default_params["feature_angle"] if "feature_angle" in ExtractFeatureParams._default_params else (json_data["featureAngle"] if "featureAngle" in json_data else None)),
                        separate_features if separate_features is not None else ( ExtractFeatureParams._default_params["separate_features"] if "separate_features" in ExtractFeatureParams._default_params else (json_data["separateFeatures"] if "separateFeatures" in json_data else None)),
                        separation_angle if separation_angle is not None else ( ExtractFeatureParams._default_params["separation_angle"] if "separation_angle" in ExtractFeatureParams._default_params else (json_data["separationAngle"] if "separationAngle" in json_data else None)),
                        disconnect_with_faces if disconnect_with_faces is not None else ( ExtractFeatureParams._default_params["disconnect_with_faces"] if "disconnect_with_faces" in ExtractFeatureParams._default_params else (json_data["disconnectWithFaces"] if "disconnectWithFaces" in json_data else None)),
                        label_name if label_name is not None else ( ExtractFeatureParams._default_params["label_name"] if "label_name" in ExtractFeatureParams._default_params else (json_data["labelName"] if "labelName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            replace: bool = None,
            feature_angle: float = None,
            separate_features: bool = None,
            separation_angle: float = None,
            disconnect_with_faces: bool = None,
            label_name: str = None):
        """Set the default values of ExtractFeatureParams.

        Parameters
        ----------
        replace: bool, optional
            Option to replace existing edge zonelets with new extracted edge zonelets.
        feature_angle: float, optional
            Angle used to capture face features to be  extracted as edges.
        separate_features: bool, optional
            Option to separate extracted features.
        separation_angle: float, optional
            Angle used to separate extracted features.
        disconnect_with_faces: bool, optional
            Option to disconnect edges from faces. If false, edges remain connected to faces by sharing nodes.
        label_name: str, optional
            Label name to be assigned to extracted features.
        """
        args = locals()
        [ExtractFeatureParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractFeatureParams.

        Examples
        --------
        >>> ExtractFeatureParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractFeatureParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._replace is not None:
            json_data["replace"] = self._replace
        if self._feature_angle is not None:
            json_data["featureAngle"] = self._feature_angle
        if self._separate_features is not None:
            json_data["separateFeatures"] = self._separate_features
        if self._separation_angle is not None:
            json_data["separationAngle"] = self._separation_angle
        if self._disconnect_with_faces is not None:
            json_data["disconnectWithFaces"] = self._disconnect_with_faces
        if self._label_name is not None:
            json_data["labelName"] = self._label_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "replace :  %s\nfeature_angle :  %s\nseparate_features :  %s\nseparation_angle :  %s\ndisconnect_with_faces :  %s\nlabel_name :  %s" % (self._replace, self._feature_angle, self._separate_features, self._separation_angle, self._disconnect_with_faces, self._label_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def replace(self) -> bool:
        """Option to replace existing edge zonelets with new extracted edge zonelets.
        """
        return self._replace

    @replace.setter
    def replace(self, value: bool):
        self._replace = value

    @property
    def feature_angle(self) -> float:
        """Angle used to capture face features to be  extracted as edges.
        """
        return self._feature_angle

    @feature_angle.setter
    def feature_angle(self, value: float):
        self._feature_angle = value

    @property
    def separate_features(self) -> bool:
        """Option to separate extracted features.
        """
        return self._separate_features

    @separate_features.setter
    def separate_features(self, value: bool):
        self._separate_features = value

    @property
    def separation_angle(self) -> float:
        """Angle used to separate extracted features.
        """
        return self._separation_angle

    @separation_angle.setter
    def separation_angle(self, value: float):
        self._separation_angle = value

    @property
    def disconnect_with_faces(self) -> bool:
        """Option to disconnect edges from faces. If false, edges remain connected to faces by sharing nodes.
        """
        return self._disconnect_with_faces

    @disconnect_with_faces.setter
    def disconnect_with_faces(self, value: bool):
        self._disconnect_with_faces = value

    @property
    def label_name(self) -> str:
        """Label name to be assigned to extracted features.
        """
        return self._label_name

    @label_name.setter
    def label_name(self, value: str):
        self._label_name = value

class ExtractFeatureResults(CoreObject):
    """Result of edge zonelet extraction by angle.
    """
    _default_params = {}

    def __initialize(
            self,
            processing_time: float,
            error_code: ErrorCode,
            new_edge_zonelets: Iterable[int]):
        self._processing_time = processing_time
        self._error_code = ErrorCode(error_code)
        self._new_edge_zonelets = new_edge_zonelets if isinstance(new_edge_zonelets, np.ndarray) else np.array(new_edge_zonelets, dtype=np.int32) if new_edge_zonelets is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            processing_time: float = None,
            error_code: ErrorCode = None,
            new_edge_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractFeatureResults.

        Parameters
        ----------
        model: Model
            Model to create a ExtractFeatureResults object with default parameters.
        processing_time: float, optional
            Time taken for edge extraction.
        error_code: ErrorCode, optional
            Error code returned by edge extraction function.
        new_edge_zonelets: Iterable[int], optional
            Ids of new edge zonelets extracted.
        json_data: dict, optional
            JSON dictionary to create a ExtractFeatureResults object with provided parameters.

        Examples
        --------
        >>> extract_feature_results = prime.ExtractFeatureResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["processingTime"] if "processingTime" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["newEdgeZonelets"] if "newEdgeZonelets" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [processing_time, error_code, new_edge_zonelets])
            if all_field_specified:
                self.__initialize(
                    processing_time,
                    error_code,
                    new_edge_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractFeatureResults")
                    json_data = param_json["ExtractFeatureResults"] if "ExtractFeatureResults" in param_json else {}
                    self.__initialize(
                        processing_time if processing_time is not None else ( ExtractFeatureResults._default_params["processing_time"] if "processing_time" in ExtractFeatureResults._default_params else (json_data["processingTime"] if "processingTime" in json_data else None)),
                        error_code if error_code is not None else ( ExtractFeatureResults._default_params["error_code"] if "error_code" in ExtractFeatureResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        new_edge_zonelets if new_edge_zonelets is not None else ( ExtractFeatureResults._default_params["new_edge_zonelets"] if "new_edge_zonelets" in ExtractFeatureResults._default_params else (json_data["newEdgeZonelets"] if "newEdgeZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            processing_time: float = None,
            error_code: ErrorCode = None,
            new_edge_zonelets: Iterable[int] = None):
        """Set the default values of ExtractFeatureResults.

        Parameters
        ----------
        processing_time: float, optional
            Time taken for edge extraction.
        error_code: ErrorCode, optional
            Error code returned by edge extraction function.
        new_edge_zonelets: Iterable[int], optional
            Ids of new edge zonelets extracted.
        """
        args = locals()
        [ExtractFeatureResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractFeatureResults.

        Examples
        --------
        >>> ExtractFeatureResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractFeatureResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._processing_time is not None:
            json_data["processingTime"] = self._processing_time
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._new_edge_zonelets is not None:
            json_data["newEdgeZonelets"] = self._new_edge_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "processing_time :  %s\nerror_code :  %s\nnew_edge_zonelets :  %s" % (self._processing_time, self._error_code, self._new_edge_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def processing_time(self) -> float:
        """Time taken for edge extraction.
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, value: float):
        self._processing_time = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code returned by edge extraction function.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def new_edge_zonelets(self) -> Iterable[int]:
        """Ids of new edge zonelets extracted.
        """
        return self._new_edge_zonelets

    @new_edge_zonelets.setter
    def new_edge_zonelets(self, value: Iterable[int]):
        self._new_edge_zonelets = value

class ExtractedFeatureIds(CoreObject):
    """Contains ids of the features extracted.
    """
    _default_params = {}

    def __initialize(
            self,
            part_id: int,
            new_edge_zonelets: Iterable[int]):
        self._part_id = part_id
        self._new_edge_zonelets = new_edge_zonelets if isinstance(new_edge_zonelets, np.ndarray) else np.array(new_edge_zonelets, dtype=np.int32) if new_edge_zonelets is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            part_id: int = None,
            new_edge_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExtractedFeatureIds.

        Parameters
        ----------
        model: Model
            Model to create a ExtractedFeatureIds object with default parameters.
        part_id: int, optional
            Id of the part from which edge zonelets are extracted.
        new_edge_zonelets: Iterable[int], optional
            Ids of new edge zonelets extracted.
        json_data: dict, optional
            JSON dictionary to create a ExtractedFeatureIds object with provided parameters.

        Examples
        --------
        >>> extracted_feature_ids = prime.ExtractedFeatureIds(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["partId"] if "partId" in json_data else None,
                json_data["newEdgeZonelets"] if "newEdgeZonelets" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [part_id, new_edge_zonelets])
            if all_field_specified:
                self.__initialize(
                    part_id,
                    new_edge_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExtractedFeatureIds")
                    json_data = param_json["ExtractedFeatureIds"] if "ExtractedFeatureIds" in param_json else {}
                    self.__initialize(
                        part_id if part_id is not None else ( ExtractedFeatureIds._default_params["part_id"] if "part_id" in ExtractedFeatureIds._default_params else (json_data["partId"] if "partId" in json_data else None)),
                        new_edge_zonelets if new_edge_zonelets is not None else ( ExtractedFeatureIds._default_params["new_edge_zonelets"] if "new_edge_zonelets" in ExtractedFeatureIds._default_params else (json_data["newEdgeZonelets"] if "newEdgeZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            part_id: int = None,
            new_edge_zonelets: Iterable[int] = None):
        """Set the default values of ExtractedFeatureIds.

        Parameters
        ----------
        part_id: int, optional
            Id of the part from which edge zonelets are extracted.
        new_edge_zonelets: Iterable[int], optional
            Ids of new edge zonelets extracted.
        """
        args = locals()
        [ExtractedFeatureIds._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExtractedFeatureIds.

        Examples
        --------
        >>> ExtractedFeatureIds.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExtractedFeatureIds._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._part_id is not None:
            json_data["partId"] = self._part_id
        if self._new_edge_zonelets is not None:
            json_data["newEdgeZonelets"] = self._new_edge_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "part_id :  %s\nnew_edge_zonelets :  %s" % (self._part_id, self._new_edge_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def part_id(self) -> int:
        """Id of the part from which edge zonelets are extracted.
        """
        return self._part_id

    @part_id.setter
    def part_id(self, value: int):
        self._part_id = value

    @property
    def new_edge_zonelets(self) -> Iterable[int]:
        """Ids of new edge zonelets extracted.
        """
        return self._new_edge_zonelets

    @new_edge_zonelets.setter
    def new_edge_zonelets(self, value: Iterable[int]):
        self._new_edge_zonelets = value

class CreateIntersectionEdgeLoopsParams(CoreObject):
    """Parameters used to calculate edge loops created by intersection of two groups of face zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            label_name: str):
        self._label_name = label_name

    def __init__(
            self,
            model: CommunicationManager=None,
            label_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateIntersectionEdgeLoopsParams.

        Parameters
        ----------
        model: Model
            Model to create a CreateIntersectionEdgeLoopsParams object with default parameters.
        label_name: str, optional
            Label name to be assigned to extracted features.
        json_data: dict, optional
            JSON dictionary to create a CreateIntersectionEdgeLoopsParams object with provided parameters.

        Examples
        --------
        >>> create_intersection_edge_loops_params = prime.CreateIntersectionEdgeLoopsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["labelName"] if "labelName" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [label_name])
            if all_field_specified:
                self.__initialize(
                    label_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CreateIntersectionEdgeLoopsParams")
                    json_data = param_json["CreateIntersectionEdgeLoopsParams"] if "CreateIntersectionEdgeLoopsParams" in param_json else {}
                    self.__initialize(
                        label_name if label_name is not None else ( CreateIntersectionEdgeLoopsParams._default_params["label_name"] if "label_name" in CreateIntersectionEdgeLoopsParams._default_params else (json_data["labelName"] if "labelName" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            label_name: str = None):
        """Set the default values of CreateIntersectionEdgeLoopsParams.

        Parameters
        ----------
        label_name: str, optional
            Label name to be assigned to extracted features.
        """
        args = locals()
        [CreateIntersectionEdgeLoopsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateIntersectionEdgeLoopsParams.

        Examples
        --------
        >>> CreateIntersectionEdgeLoopsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateIntersectionEdgeLoopsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._label_name is not None:
            json_data["labelName"] = self._label_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "label_name :  %s" % (self._label_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def label_name(self) -> str:
        """Label name to be assigned to extracted features.
        """
        return self._label_name

    @label_name.setter
    def label_name(self, value: str):
        self._label_name = value

class CreateIntersectionEdgeLoopsResults(CoreObject):
    """Results for the edge loops created by intersection of two groups of face zonelets.
    """
    _default_params = {}

    def __initialize(
            self,
            processing_time: float,
            error_code: ErrorCode,
            extracted_ids: List[ExtractedFeatureIds]):
        self._processing_time = processing_time
        self._error_code = ErrorCode(error_code)
        self._extracted_ids = extracted_ids

    def __init__(
            self,
            model: CommunicationManager=None,
            processing_time: float = None,
            error_code: ErrorCode = None,
            extracted_ids: List[ExtractedFeatureIds] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CreateIntersectionEdgeLoopsResults.

        Parameters
        ----------
        model: Model
            Model to create a CreateIntersectionEdgeLoopsResults object with default parameters.
        processing_time: float, optional
            Time taken to extract edges formed by intersecting faces.
        error_code: ErrorCode, optional
            Error code returned by edge extraction function.
        extracted_ids: List[ExtractedFeatureIds], optional
            List of ExtractedFeatureIds that contains ids of extracted edges.
        json_data: dict, optional
            JSON dictionary to create a CreateIntersectionEdgeLoopsResults object with provided parameters.

        Examples
        --------
        >>> create_intersection_edge_loops_results = prime.CreateIntersectionEdgeLoopsResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["processingTime"] if "processingTime" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [ExtractedFeatureIds(model = model, json_data = data) for data in json_data["extractedIds"]] if "extractedIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [processing_time, error_code, extracted_ids])
            if all_field_specified:
                self.__initialize(
                    processing_time,
                    error_code,
                    extracted_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CreateIntersectionEdgeLoopsResults")
                    json_data = param_json["CreateIntersectionEdgeLoopsResults"] if "CreateIntersectionEdgeLoopsResults" in param_json else {}
                    self.__initialize(
                        processing_time if processing_time is not None else ( CreateIntersectionEdgeLoopsResults._default_params["processing_time"] if "processing_time" in CreateIntersectionEdgeLoopsResults._default_params else (json_data["processingTime"] if "processingTime" in json_data else None)),
                        error_code if error_code is not None else ( CreateIntersectionEdgeLoopsResults._default_params["error_code"] if "error_code" in CreateIntersectionEdgeLoopsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        extracted_ids if extracted_ids is not None else ( CreateIntersectionEdgeLoopsResults._default_params["extracted_ids"] if "extracted_ids" in CreateIntersectionEdgeLoopsResults._default_params else [ExtractedFeatureIds(model = model, json_data = data) for data in (json_data["extractedIds"] if "extractedIds" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            processing_time: float = None,
            error_code: ErrorCode = None,
            extracted_ids: List[ExtractedFeatureIds] = None):
        """Set the default values of CreateIntersectionEdgeLoopsResults.

        Parameters
        ----------
        processing_time: float, optional
            Time taken to extract edges formed by intersecting faces.
        error_code: ErrorCode, optional
            Error code returned by edge extraction function.
        extracted_ids: List[ExtractedFeatureIds], optional
            List of ExtractedFeatureIds that contains ids of extracted edges.
        """
        args = locals()
        [CreateIntersectionEdgeLoopsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CreateIntersectionEdgeLoopsResults.

        Examples
        --------
        >>> CreateIntersectionEdgeLoopsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateIntersectionEdgeLoopsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._processing_time is not None:
            json_data["processingTime"] = self._processing_time
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._extracted_ids is not None:
            json_data["extractedIds"] = [data._jsonify() for data in self._extracted_ids]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "processing_time :  %s\nerror_code :  %s\nextracted_ids :  %s" % (self._processing_time, self._error_code, '[' + ''.join('\n' + str(data) for data in self._extracted_ids) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def processing_time(self) -> float:
        """Time taken to extract edges formed by intersecting faces.
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, value: float):
        self._processing_time = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code returned by edge extraction function.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def extracted_ids(self) -> List[ExtractedFeatureIds]:
        """List of ExtractedFeatureIds that contains ids of extracted edges.
        """
        return self._extracted_ids

    @extracted_ids.setter
    def extracted_ids(self, value: List[ExtractedFeatureIds]):
        self._extracted_ids = value
