""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class ScopeEntity(enum.IntEnum):
    """ScopeDefinition uses entity type to scope entities.
    """
    # Evaluate scope to get the face zonelets.
    FACEZONELETS = 1

class ScopeEvaluationType(enum.IntEnum):
    """ScopeDefinition uses evaluation type to evaluate the scope.
    """
    # Use labels to evaluate the scope.
    LABELS = 3
    # Use zones to evaluate the scope.
    ZONES = 4

class ScopeDefinition(CoreObject):
    """ScopeDefinition to scope entities based on entity and evaluation type.
    """
    default_params = {}

    def __initialize(
            self,
            entity_type: ScopeEntity,
            evaluation_type: ScopeEvaluationType,
            part_expression: str,
            label_expression: str,
            zone_expression: str):
        self._entity_type = entity_type
        self._evaluation_type = evaluation_type
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
        """Initializes ScopeDefinition

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
        >>> scope_definition = ScopeDefinition(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeEntity(json_data["entityType"]),
                ScopeEvaluationType(json_data["evaluationType"]),
                json_data["partExpression"],
                json_data["labelExpression"],
                json_data["zoneExpression"])
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
                    json_data = model.communicator.initialize_params("ScopeDefinition")["ScopeDefinition"]
                    self.__initialize(
                        entity_type if entity_type is not None else ( ScopeDefinition.default_params["entity_type"] if "entity_type" in ScopeDefinition.default_params else ScopeEntity(json_data["entityType"])),
                        evaluation_type if evaluation_type is not None else ( ScopeDefinition.default_params["evaluation_type"] if "evaluation_type" in ScopeDefinition.default_params else ScopeEvaluationType(json_data["evaluationType"])),
                        part_expression if part_expression is not None else ( ScopeDefinition.default_params["part_expression"] if "part_expression" in ScopeDefinition.default_params else json_data["partExpression"]),
                        label_expression if label_expression is not None else ( ScopeDefinition.default_params["label_expression"] if "label_expression" in ScopeDefinition.default_params else json_data["labelExpression"]),
                        zone_expression if zone_expression is not None else ( ScopeDefinition.default_params["zone_expression"] if "zone_expression" in ScopeDefinition.default_params else json_data["zoneExpression"]))
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
        args = locals()
        [ScopeDefinition.default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScopeDefinition.default_params.items())
        print(message)

    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["entityType"] = self._entity_type
        json_data["evaluationType"] = self._evaluation_type
        json_data["partExpression"] = self._part_expression
        json_data["labelExpression"] = self._label_expression
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
