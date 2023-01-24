""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class ScopeEntity(enum.IntEnum):
    """ScopeDefinition uses entity type to scope entities.
    """
    FACEZONELETS = 1
    """Evaluate scope to get the face zonelets."""
    EDGEZONELETS = 2
    """Evaluate scope to get the edge zonelets."""
    FACEANDEDGEZONELETS = 3
    """Evaluate scope to get face and edge zonelets."""
    VOLUME = 6
    """Evaluate scope to get volumes."""

class ScopeEvaluationType(enum.IntEnum):
    """ScopeDefinition uses evaluation type to evaluate the scope.
    """
    LABELS = 3
    """Use labels to evaluate the scope."""
    ZONES = 4
    """Use zones to evaluate the scope."""

class ScopeExpressionType(enum.IntEnum):
    """ScopeExpressionType uses expression type to evaluate the scope.
    """
    NAMEPATTERN = 2
    """Use name pattern expression to evaluate scope."""

class ScopeDefinition(CoreObject):
    """ScopeDefinition to scope entities based on entity and evaluation type.
    """
    _default_params = {}

    def __initialize(
            self,
            entity_type: ScopeEntity,
            evaluation_type: ScopeEvaluationType,
            part_expression: str,
            label_expression: str,
            zone_expression: str):
        self._entity_type = ScopeEntity(entity_type)
        self._evaluation_type = ScopeEvaluationType(evaluation_type)
        self._part_expression = part_expression
        self._label_expression = label_expression
        self._zone_expression = zone_expression

    def __init__(
            self,
            model: CommunicationManager=None,
            entity_type: ScopeEntity = None,
            evaluation_type: ScopeEvaluationType = None,
            part_expression: str = None,
            label_expression: str = None,
            zone_expression: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ScopeDefinition.

        Parameters
        ----------
        model: Model
            Model to create a ScopeDefinition object with default parameters.
        entity_type: ScopeEntity, optional
            Entity type for which scope needs to be evaluated. The default is set to face zonelets.
        evaluation_type: ScopeEvaluationType, optional
            Evaluation type to scope entities. The default is set to labels.
        part_expression: str, optional
            Part expression to scope parts while evaluating scope.
        label_expression: str, optional
            Label expression to scope entities when evaluation type is set to labels.
        zone_expression: str, optional
            Zone expression to scope entities when evaluation type is set to zones.
        json_data: dict, optional
            JSON dictionary to create a ScopeDefinition object with provided parameters.

        Examples
        --------
        >>> scope_definition = prime.ScopeDefinition(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeEntity(json_data["entityType"] if "entityType" in json_data else None),
                ScopeEvaluationType(json_data["evaluationType"] if "evaluationType" in json_data else None),
                json_data["partExpression"] if "partExpression" in json_data else None,
                json_data["labelExpression"] if "labelExpression" in json_data else None,
                json_data["zoneExpression"] if "zoneExpression" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [entity_type, evaluation_type, part_expression, label_expression, zone_expression])
            if all_field_specified:
                self.__initialize(
                    entity_type,
                    evaluation_type,
                    part_expression,
                    label_expression,
                    zone_expression)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ScopeDefinition")
                    json_data = param_json["ScopeDefinition"] if "ScopeDefinition" in param_json else {}
                    self.__initialize(
                        entity_type if entity_type is not None else ( ScopeDefinition._default_params["entity_type"] if "entity_type" in ScopeDefinition._default_params else ScopeEntity(json_data["entityType"] if "entityType" in json_data else None)),
                        evaluation_type if evaluation_type is not None else ( ScopeDefinition._default_params["evaluation_type"] if "evaluation_type" in ScopeDefinition._default_params else ScopeEvaluationType(json_data["evaluationType"] if "evaluationType" in json_data else None)),
                        part_expression if part_expression is not None else ( ScopeDefinition._default_params["part_expression"] if "part_expression" in ScopeDefinition._default_params else (json_data["partExpression"] if "partExpression" in json_data else None)),
                        label_expression if label_expression is not None else ( ScopeDefinition._default_params["label_expression"] if "label_expression" in ScopeDefinition._default_params else (json_data["labelExpression"] if "labelExpression" in json_data else None)),
                        zone_expression if zone_expression is not None else ( ScopeDefinition._default_params["zone_expression"] if "zone_expression" in ScopeDefinition._default_params else (json_data["zoneExpression"] if "zoneExpression" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            entity_type: ScopeEntity = None,
            evaluation_type: ScopeEvaluationType = None,
            part_expression: str = None,
            label_expression: str = None,
            zone_expression: str = None):
        """Set the default values of ScopeDefinition.

        Parameters
        ----------
        entity_type: ScopeEntity, optional
            Entity type for which scope needs to be evaluated. The default is set to face zonelets.
        evaluation_type: ScopeEvaluationType, optional
            Evaluation type to scope entities. The default is set to labels.
        part_expression: str, optional
            Part expression to scope parts while evaluating scope.
        label_expression: str, optional
            Label expression to scope entities when evaluation type is set to labels.
        zone_expression: str, optional
            Zone expression to scope entities when evaluation type is set to zones.
        """
        args = locals()
        [ScopeDefinition._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ScopeDefinition.

        Examples
        --------
        >>> ScopeDefinition.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScopeDefinition._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._entity_type is not None:
            json_data["entityType"] = self._entity_type
        if self._evaluation_type is not None:
            json_data["evaluationType"] = self._evaluation_type
        if self._part_expression is not None:
            json_data["partExpression"] = self._part_expression
        if self._label_expression is not None:
            json_data["labelExpression"] = self._label_expression
        if self._zone_expression is not None:
            json_data["zoneExpression"] = self._zone_expression
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "entity_type :  %s\nevaluation_type :  %s\npart_expression :  %s\nlabel_expression :  %s\nzone_expression :  %s" % (self._entity_type, self._evaluation_type, self._part_expression, self._label_expression, self._zone_expression)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def entity_type(self) -> ScopeEntity:
        """Entity type for which scope needs to be evaluated. The default is set to face zonelets.
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value: ScopeEntity):
        self._entity_type = value

    @property
    def evaluation_type(self) -> ScopeEvaluationType:
        """Evaluation type to scope entities. The default is set to labels.
        """
        return self._evaluation_type

    @evaluation_type.setter
    def evaluation_type(self, value: ScopeEvaluationType):
        self._evaluation_type = value

    @property
    def part_expression(self) -> str:
        """Part expression to scope parts while evaluating scope.
        """
        return self._part_expression

    @part_expression.setter
    def part_expression(self, value: str):
        self._part_expression = value

    @property
    def label_expression(self) -> str:
        """Label expression to scope entities when evaluation type is set to labels.
        """
        return self._label_expression

    @label_expression.setter
    def label_expression(self, value: str):
        self._label_expression = value

    @property
    def zone_expression(self) -> str:
        """Zone expression to scope entities when evaluation type is set to zones.
        """
        return self._zone_expression

    @zone_expression.setter
    def zone_expression(self, value: str):
        self._zone_expression = value

class LeakPreventionParams(CoreObject):
    """LeakPreventionParams defines leakage prevention control parameters for wrapper.
    """
    _default_params = {}

    def __initialize(
            self,
            material_points: List[str],
            scope: ScopeDefinition,
            max_hole_size: float,
            n_expansion_layers: int):
        self._material_points = material_points
        self._scope = scope
        self._max_hole_size = max_hole_size
        self._n_expansion_layers = n_expansion_layers

    def __init__(
            self,
            model: CommunicationManager=None,
            material_points: List[str] = None,
            scope: ScopeDefinition = None,
            max_hole_size: float = None,
            n_expansion_layers: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the LeakPreventionParams.

        Parameters
        ----------
        model: Model
            Model to create a LeakPreventionParams object with default parameters.
        material_points: List[str], optional
            Material points used for leak prevention control.
        scope: ScopeDefinition, optional
            Scope used for leak prevention control.
        max_hole_size: float, optional
            Maximum hole size to prevent leakage into region.
        n_expansion_layers: int, optional
            Number of layers to expand leaking region.
        json_data: dict, optional
            JSON dictionary to create a LeakPreventionParams object with provided parameters.

        Examples
        --------
        >>> leak_prevention_params = prime.LeakPreventionParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["materialPoints"] if "materialPoints" in json_data else None,
                ScopeDefinition(model = model, json_data = json_data["scope"] if "scope" in json_data else None),
                json_data["maxHoleSize"] if "maxHoleSize" in json_data else None,
                json_data["nExpansionLayers"] if "nExpansionLayers" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [material_points, scope, max_hole_size, n_expansion_layers])
            if all_field_specified:
                self.__initialize(
                    material_points,
                    scope,
                    max_hole_size,
                    n_expansion_layers)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "LeakPreventionParams")
                    json_data = param_json["LeakPreventionParams"] if "LeakPreventionParams" in param_json else {}
                    self.__initialize(
                        material_points if material_points is not None else ( LeakPreventionParams._default_params["material_points"] if "material_points" in LeakPreventionParams._default_params else (json_data["materialPoints"] if "materialPoints" in json_data else None)),
                        scope if scope is not None else ( LeakPreventionParams._default_params["scope"] if "scope" in LeakPreventionParams._default_params else ScopeDefinition(model = model, json_data = (json_data["scope"] if "scope" in json_data else None))),
                        max_hole_size if max_hole_size is not None else ( LeakPreventionParams._default_params["max_hole_size"] if "max_hole_size" in LeakPreventionParams._default_params else (json_data["maxHoleSize"] if "maxHoleSize" in json_data else None)),
                        n_expansion_layers if n_expansion_layers is not None else ( LeakPreventionParams._default_params["n_expansion_layers"] if "n_expansion_layers" in LeakPreventionParams._default_params else (json_data["nExpansionLayers"] if "nExpansionLayers" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            material_points: List[str] = None,
            scope: ScopeDefinition = None,
            max_hole_size: float = None,
            n_expansion_layers: int = None):
        """Set the default values of LeakPreventionParams.

        Parameters
        ----------
        material_points: List[str], optional
            Material points used for leak prevention control.
        scope: ScopeDefinition, optional
            Scope used for leak prevention control.
        max_hole_size: float, optional
            Maximum hole size to prevent leakage into region.
        n_expansion_layers: int, optional
            Number of layers to expand leaking region.
        """
        args = locals()
        [LeakPreventionParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of LeakPreventionParams.

        Examples
        --------
        >>> LeakPreventionParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in LeakPreventionParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._material_points is not None:
            json_data["materialPoints"] = self._material_points
        if self._scope is not None:
            json_data["scope"] = self._scope._jsonify()
        if self._max_hole_size is not None:
            json_data["maxHoleSize"] = self._max_hole_size
        if self._n_expansion_layers is not None:
            json_data["nExpansionLayers"] = self._n_expansion_layers
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "material_points :  %s\nscope :  %s\nmax_hole_size :  %s\nn_expansion_layers :  %s" % (self._material_points, '{ ' + str(self._scope) + ' }', self._max_hole_size, self._n_expansion_layers)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def material_points(self) -> List[str]:
        """Material points used for leak prevention control.
        """
        return self._material_points

    @material_points.setter
    def material_points(self, value: List[str]):
        self._material_points = value

    @property
    def scope(self) -> ScopeDefinition:
        """Scope used for leak prevention control.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

    @property
    def max_hole_size(self) -> float:
        """Maximum hole size to prevent leakage into region.
        """
        return self._max_hole_size

    @max_hole_size.setter
    def max_hole_size(self, value: float):
        self._max_hole_size = value

    @property
    def n_expansion_layers(self) -> int:
        """Number of layers to expand leaking region.
        """
        return self._n_expansion_layers

    @n_expansion_layers.setter
    def n_expansion_layers(self, value: int):
        self._n_expansion_layers = value

class SetLeakPreventionsResults(CoreObject):
    """Results associated with set leak preventions.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            ids: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetLeakPreventionsResults.

        Parameters
        ----------
        model: Model
            Model to create a SetLeakPreventionsResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the set leak preventions.
        ids: Iterable[int], optional
            Ids of added leak prevention controls.
        json_data: dict, optional
            JSON dictionary to create a SetLeakPreventionsResults object with provided parameters.

        Examples
        --------
        >>> set_leak_preventions_results = prime.SetLeakPreventionsResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["ids"] if "ids" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, ids])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SetLeakPreventionsResults")
                    json_data = param_json["SetLeakPreventionsResults"] if "SetLeakPreventionsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetLeakPreventionsResults._default_params["error_code"] if "error_code" in SetLeakPreventionsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        ids if ids is not None else ( SetLeakPreventionsResults._default_params["ids"] if "ids" in SetLeakPreventionsResults._default_params else (json_data["ids"] if "ids" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            ids: Iterable[int] = None):
        """Set the default values of SetLeakPreventionsResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the set leak preventions.
        ids: Iterable[int], optional
            Ids of added leak prevention controls.
        """
        args = locals()
        [SetLeakPreventionsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SetLeakPreventionsResults.

        Examples
        --------
        >>> SetLeakPreventionsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetLeakPreventionsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._ids is not None:
            json_data["ids"] = self._ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nids :  %s" % (self._error_code, self._ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the set leak preventions.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def ids(self) -> Iterable[int]:
        """Ids of added leak prevention controls.
        """
        return self._ids

    @ids.setter
    def ids(self, value: Iterable[int]):
        self._ids = value

class ContactPreventionParams(CoreObject):
    """ContactPreventionParams defines contact prevention control parameters for wrapper.
    """
    _default_params = {}

    def __initialize(
            self,
            source_scope: ScopeDefinition,
            target_scope: ScopeDefinition,
            size: float):
        self._source_scope = source_scope
        self._target_scope = target_scope
        self._size = size

    def __init__(
            self,
            model: CommunicationManager=None,
            source_scope: ScopeDefinition = None,
            target_scope: ScopeDefinition = None,
            size: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ContactPreventionParams.

        Parameters
        ----------
        model: Model
            Model to create a ContactPreventionParams object with default parameters.
        source_scope: ScopeDefinition, optional
            Source scope used for contact prevention control.
        target_scope: ScopeDefinition, optional
            Target scope used for contact prevention control.
        size: float, optional
            Minimum gap size (gap/4) to resolve contact between source and target.
        json_data: dict, optional
            JSON dictionary to create a ContactPreventionParams object with provided parameters.

        Examples
        --------
        >>> contact_prevention_params = prime.ContactPreventionParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["sourceScope"] if "sourceScope" in json_data else None),
                ScopeDefinition(model = model, json_data = json_data["targetScope"] if "targetScope" in json_data else None),
                json_data["size"] if "size" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [source_scope, target_scope, size])
            if all_field_specified:
                self.__initialize(
                    source_scope,
                    target_scope,
                    size)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ContactPreventionParams")
                    json_data = param_json["ContactPreventionParams"] if "ContactPreventionParams" in param_json else {}
                    self.__initialize(
                        source_scope if source_scope is not None else ( ContactPreventionParams._default_params["source_scope"] if "source_scope" in ContactPreventionParams._default_params else ScopeDefinition(model = model, json_data = (json_data["sourceScope"] if "sourceScope" in json_data else None))),
                        target_scope if target_scope is not None else ( ContactPreventionParams._default_params["target_scope"] if "target_scope" in ContactPreventionParams._default_params else ScopeDefinition(model = model, json_data = (json_data["targetScope"] if "targetScope" in json_data else None))),
                        size if size is not None else ( ContactPreventionParams._default_params["size"] if "size" in ContactPreventionParams._default_params else (json_data["size"] if "size" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            source_scope: ScopeDefinition = None,
            target_scope: ScopeDefinition = None,
            size: float = None):
        """Set the default values of ContactPreventionParams.

        Parameters
        ----------
        source_scope: ScopeDefinition, optional
            Source scope used for contact prevention control.
        target_scope: ScopeDefinition, optional
            Target scope used for contact prevention control.
        size: float, optional
            Minimum gap size (gap/4) to resolve contact between source and target.
        """
        args = locals()
        [ContactPreventionParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ContactPreventionParams.

        Examples
        --------
        >>> ContactPreventionParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ContactPreventionParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._source_scope is not None:
            json_data["sourceScope"] = self._source_scope._jsonify()
        if self._target_scope is not None:
            json_data["targetScope"] = self._target_scope._jsonify()
        if self._size is not None:
            json_data["size"] = self._size
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "source_scope :  %s\ntarget_scope :  %s\nsize :  %s" % ('{ ' + str(self._source_scope) + ' }', '{ ' + str(self._target_scope) + ' }', self._size)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def source_scope(self) -> ScopeDefinition:
        """Source scope used for contact prevention control.
        """
        return self._source_scope

    @source_scope.setter
    def source_scope(self, value: ScopeDefinition):
        self._source_scope = value

    @property
    def target_scope(self) -> ScopeDefinition:
        """Target scope used for contact prevention control.
        """
        return self._target_scope

    @target_scope.setter
    def target_scope(self, value: ScopeDefinition):
        self._target_scope = value

    @property
    def size(self) -> float:
        """Minimum gap size (gap/4) to resolve contact between source and target.
        """
        return self._size

    @size.setter
    def size(self, value: float):
        self._size = value

class SetContactPreventionsResults(CoreObject):
    """Results associated with set contact preventions.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            ids: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetContactPreventionsResults.

        Parameters
        ----------
        model: Model
            Model to create a SetContactPreventionsResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the set contact preventions.
        ids: Iterable[int], optional
            Ids of added contact prevention controls.
        json_data: dict, optional
            JSON dictionary to create a SetContactPreventionsResults object with provided parameters.

        Examples
        --------
        >>> set_contact_preventions_results = prime.SetContactPreventionsResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["ids"] if "ids" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, ids])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SetContactPreventionsResults")
                    json_data = param_json["SetContactPreventionsResults"] if "SetContactPreventionsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetContactPreventionsResults._default_params["error_code"] if "error_code" in SetContactPreventionsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        ids if ids is not None else ( SetContactPreventionsResults._default_params["ids"] if "ids" in SetContactPreventionsResults._default_params else (json_data["ids"] if "ids" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            ids: Iterable[int] = None):
        """Set the default values of SetContactPreventionsResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the set contact preventions.
        ids: Iterable[int], optional
            Ids of added contact prevention controls.
        """
        args = locals()
        [SetContactPreventionsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SetContactPreventionsResults.

        Examples
        --------
        >>> SetContactPreventionsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetContactPreventionsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._ids is not None:
            json_data["ids"] = self._ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nids :  %s" % (self._error_code, self._ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the set contact preventions.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def ids(self) -> Iterable[int]:
        """Ids of added contact prevention controls.
        """
        return self._ids

    @ids.setter
    def ids(self, value: Iterable[int]):
        self._ids = value

class FeatureRecoveryParams(CoreObject):
    """FeatureRecoveryParams defines feature recovery control parameters for wrapper.
    """
    _default_params = {}

    def __initialize(
            self,
            scope: ScopeDefinition,
            enable_feature_octree_refinement: bool,
            size_at_features: float):
        self._scope = scope
        self._enable_feature_octree_refinement = enable_feature_octree_refinement
        self._size_at_features = size_at_features

    def __init__(
            self,
            model: CommunicationManager=None,
            scope: ScopeDefinition = None,
            enable_feature_octree_refinement: bool = None,
            size_at_features: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FeatureRecoveryParams.

        Parameters
        ----------
        model: Model
            Model to create a FeatureRecoveryParams object with default parameters.
        scope: ScopeDefinition, optional
            Scope used for feature recovery control.
        enable_feature_octree_refinement: bool, optional
            Checks whether to perform octree refinement at feature edges.
        size_at_features: float, optional
            Refinement size at features.
        json_data: dict, optional
            JSON dictionary to create a FeatureRecoveryParams object with provided parameters.

        Examples
        --------
        >>> feature_recovery_params = prime.FeatureRecoveryParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["scope"] if "scope" in json_data else None),
                json_data["enableFeatureOctreeRefinement"] if "enableFeatureOctreeRefinement" in json_data else None,
                json_data["sizeAtFeatures"] if "sizeAtFeatures" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [scope, enable_feature_octree_refinement, size_at_features])
            if all_field_specified:
                self.__initialize(
                    scope,
                    enable_feature_octree_refinement,
                    size_at_features)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "FeatureRecoveryParams")
                    json_data = param_json["FeatureRecoveryParams"] if "FeatureRecoveryParams" in param_json else {}
                    self.__initialize(
                        scope if scope is not None else ( FeatureRecoveryParams._default_params["scope"] if "scope" in FeatureRecoveryParams._default_params else ScopeDefinition(model = model, json_data = (json_data["scope"] if "scope" in json_data else None))),
                        enable_feature_octree_refinement if enable_feature_octree_refinement is not None else ( FeatureRecoveryParams._default_params["enable_feature_octree_refinement"] if "enable_feature_octree_refinement" in FeatureRecoveryParams._default_params else (json_data["enableFeatureOctreeRefinement"] if "enableFeatureOctreeRefinement" in json_data else None)),
                        size_at_features if size_at_features is not None else ( FeatureRecoveryParams._default_params["size_at_features"] if "size_at_features" in FeatureRecoveryParams._default_params else (json_data["sizeAtFeatures"] if "sizeAtFeatures" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            scope: ScopeDefinition = None,
            enable_feature_octree_refinement: bool = None,
            size_at_features: float = None):
        """Set the default values of FeatureRecoveryParams.

        Parameters
        ----------
        scope: ScopeDefinition, optional
            Scope used for feature recovery control.
        enable_feature_octree_refinement: bool, optional
            Checks whether to perform octree refinement at feature edges.
        size_at_features: float, optional
            Refinement size at features.
        """
        args = locals()
        [FeatureRecoveryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FeatureRecoveryParams.

        Examples
        --------
        >>> FeatureRecoveryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FeatureRecoveryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._scope is not None:
            json_data["scope"] = self._scope._jsonify()
        if self._enable_feature_octree_refinement is not None:
            json_data["enableFeatureOctreeRefinement"] = self._enable_feature_octree_refinement
        if self._size_at_features is not None:
            json_data["sizeAtFeatures"] = self._size_at_features
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "scope :  %s\nenable_feature_octree_refinement :  %s\nsize_at_features :  %s" % ('{ ' + str(self._scope) + ' }', self._enable_feature_octree_refinement, self._size_at_features)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def scope(self) -> ScopeDefinition:
        """Scope used for feature recovery control.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

    @property
    def enable_feature_octree_refinement(self) -> bool:
        """Checks whether to perform octree refinement at feature edges.
        """
        return self._enable_feature_octree_refinement

    @enable_feature_octree_refinement.setter
    def enable_feature_octree_refinement(self, value: bool):
        self._enable_feature_octree_refinement = value

    @property
    def size_at_features(self) -> float:
        """Refinement size at features.
        """
        return self._size_at_features

    @size_at_features.setter
    def size_at_features(self, value: float):
        self._size_at_features = value

class SetFeatureRecoveriesResults(CoreObject):
    """Results associated with set feature recoveries.
    """
    _default_params = {}

    def __initialize(
            self,
            ids: Iterable[int],
            error_code: ErrorCode):
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            ids: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetFeatureRecoveriesResults.

        Parameters
        ----------
        model: Model
            Model to create a SetFeatureRecoveriesResults object with default parameters.
        ids: Iterable[int], optional
            Ids of added feature recovery controls.
        error_code: ErrorCode, optional
            Error code associated with the set feature recoveries.
        json_data: dict, optional
            JSON dictionary to create a SetFeatureRecoveriesResults object with provided parameters.

        Examples
        --------
        >>> set_feature_recoveries_results = prime.SetFeatureRecoveriesResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["ids"] if "ids" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [ids, error_code])
            if all_field_specified:
                self.__initialize(
                    ids,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SetFeatureRecoveriesResults")
                    json_data = param_json["SetFeatureRecoveriesResults"] if "SetFeatureRecoveriesResults" in param_json else {}
                    self.__initialize(
                        ids if ids is not None else ( SetFeatureRecoveriesResults._default_params["ids"] if "ids" in SetFeatureRecoveriesResults._default_params else (json_data["ids"] if "ids" in json_data else None)),
                        error_code if error_code is not None else ( SetFeatureRecoveriesResults._default_params["error_code"] if "error_code" in SetFeatureRecoveriesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            ids: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of SetFeatureRecoveriesResults.

        Parameters
        ----------
        ids: Iterable[int], optional
            Ids of added feature recovery controls.
        error_code: ErrorCode, optional
            Error code associated with the set feature recoveries.
        """
        args = locals()
        [SetFeatureRecoveriesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SetFeatureRecoveriesResults.

        Examples
        --------
        >>> SetFeatureRecoveriesResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetFeatureRecoveriesResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._ids is not None:
            json_data["ids"] = self._ids
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "ids :  %s\nerror_code :  %s" % (self._ids, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def ids(self) -> Iterable[int]:
        """Ids of added feature recovery controls.
        """
        return self._ids

    @ids.setter
    def ids(self, value: Iterable[int]):
        self._ids = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the set feature recoveries.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ScopeZoneletParams(CoreObject):
    """Parameters used to get the scoped face or edge zonelets.
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
        """Initializes the ScopeZoneletParams.

        Parameters
        ----------
        model: Model
            Model to create a ScopeZoneletParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ScopeZoneletParams object with provided parameters.

        Examples
        --------
        >>> scope_zonelet_params = prime.ScopeZoneletParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ScopeZoneletParams")
                    json_data = param_json["ScopeZoneletParams"] if "ScopeZoneletParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of ScopeZoneletParams.

        """
        args = locals()
        [ScopeZoneletParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ScopeZoneletParams.

        Examples
        --------
        >>> ScopeZoneletParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScopeZoneletParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SetScopeResults(CoreObject):
    """Results associated with the set scope operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_code: WarningCode):
        self._error_code = ErrorCode(error_code)
        self._warning_code = WarningCode(warning_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_code: WarningCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetScopeResults.

        Parameters
        ----------
        model: Model
            Model to create a SetScopeResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the set scope.
        warning_code: WarningCode, optional
            Warning code associated with the set scope.
        json_data: dict, optional
            JSON dictionary to create a SetScopeResults object with provided parameters.

        Examples
        --------
        >>> set_scope_results = prime.SetScopeResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                WarningCode(json_data["warningCode"] if "warningCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_code])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SetScopeResults")
                    json_data = param_json["SetScopeResults"] if "SetScopeResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetScopeResults._default_params["error_code"] if "error_code" in SetScopeResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_code if warning_code is not None else ( SetScopeResults._default_params["warning_code"] if "warning_code" in SetScopeResults._default_params else WarningCode(json_data["warningCode"] if "warningCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_code: WarningCode = None):
        """Set the default values of SetScopeResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the set scope.
        warning_code: WarningCode, optional
            Warning code associated with the set scope.
        """
        args = locals()
        [SetScopeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SetScopeResults.

        Examples
        --------
        >>> SetScopeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetScopeResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_code is not None:
            json_data["warningCode"] = self._warning_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_code :  %s" % (self._error_code, self._warning_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the set scope.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_code(self) -> WarningCode:
        """Warning code associated with the set scope.
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, value: WarningCode):
        self._warning_code = value
