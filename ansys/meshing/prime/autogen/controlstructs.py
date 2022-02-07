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
    FACEZONELETS = 1
    """Evaluate scope to get the face zonelets."""

class ScopeEvaluationType(enum.IntEnum):
    """ScopeDefinition uses evaluation type to evaluate the scope.
    """
    LABELS = 3
    """Use labels to evaluate the scope."""
    ZONES = 4
    """Use zones to evaluate the scope."""

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
                    json_data = model._communicator.initialize_params("ScopeDefinition")["ScopeDefinition"]
                    self.__initialize(
                        entity_type if entity_type is not None else ( ScopeDefinition._default_params["entity_type"] if "entity_type" in ScopeDefinition._default_params else ScopeEntity(json_data["entityType"])),
                        evaluation_type if evaluation_type is not None else ( ScopeDefinition._default_params["evaluation_type"] if "evaluation_type" in ScopeDefinition._default_params else ScopeEvaluationType(json_data["evaluationType"])),
                        part_expression if part_expression is not None else ( ScopeDefinition._default_params["part_expression"] if "part_expression" in ScopeDefinition._default_params else json_data["partExpression"]),
                        label_expression if label_expression is not None else ( ScopeDefinition._default_params["label_expression"] if "label_expression" in ScopeDefinition._default_params else json_data["labelExpression"]),
                        zone_expression if zone_expression is not None else ( ScopeDefinition._default_params["zone_expression"] if "zone_expression" in ScopeDefinition._default_params else json_data["zoneExpression"]))
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
        """Sets the default values of ScopeDefinition.

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
        """Prints the default values of ScopeDefinition.

        Examples
        --------
        >>> ScopeDefinition.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScopeDefinition._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
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
                    json_data = model._communicator.initialize_params("ScopeZoneletParams")["ScopeZoneletParams"]
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Sets the default values of ScopeZoneletParams.

        """
        args = locals()
        [ScopeZoneletParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of ScopeZoneletParams.

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
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetScopeResults.

        Parameters
        ----------
        model: Model
            Model to create a SetScopeResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the set scope.
        json_data: dict, optional
            JSON dictionary to create a SetScopeResults object with provided parameters.

        Examples
        --------
        >>> set_scope_results = prime.SetScopeResults(model = model)
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
                    json_data = model._communicator.initialize_params("SetScopeResults")["SetScopeResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( SetScopeResults._default_params["error_code"] if "error_code" in SetScopeResults._default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Sets the default values of SetScopeResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the set scope.
        """
        args = locals()
        [SetScopeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of SetScopeResults.

        Examples
        --------
        >>> SetScopeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetScopeResults._default_params.items())
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
        """Error code associated with the set scope.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class SetNameResults(CoreObject):
    """Results associated with the set name of control.
    """
    _default_params = {}

    def __initialize(
            self,
            warning_code: WarningCode,
            suggested_name: str):
        self._warning_code = WarningCode(warning_code)
        self._suggested_name = suggested_name

    def __init__(
            self,
            model: CommunicationManager=None,
            warning_code: WarningCode = None,
            suggested_name: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetNameResults.

        Parameters
        ----------
        model: Model
            Model to create a SetNameResults object with default parameters.
        warning_code: WarningCode, optional
            Warning code associated with the set name of control.
        suggested_name: str, optional
            Override name of a control.
        json_data: dict, optional
            JSON dictionary to create a SetNameResults object with provided parameters.

        Examples
        --------
        >>> set_name_results = prime.SetNameResults(model = model)
        """
        if json_data:
            self.__initialize(
                WarningCode(json_data["warningCode"]),
                json_data["suggestedName"])
        else:
            all_field_specified = all(arg is not None for arg in [warning_code, suggested_name])
            if all_field_specified:
                self.__initialize(
                    warning_code,
                    suggested_name)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params("SetNameResults")["SetNameResults"]
                    self.__initialize(
                        warning_code if warning_code is not None else ( SetNameResults._default_params["warning_code"] if "warning_code" in SetNameResults._default_params else WarningCode(json_data["warningCode"])),
                        suggested_name if suggested_name is not None else ( SetNameResults._default_params["suggested_name"] if "suggested_name" in SetNameResults._default_params else json_data["suggestedName"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            warning_code: WarningCode = None,
            suggested_name: str = None):
        """Sets the default values of SetNameResults.

        Parameters
        ----------
        warning_code: WarningCode, optional
            Warning code associated with the set name of control.
        suggested_name: str, optional
            Override name of a control.
        """
        args = locals()
        [SetNameResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of SetNameResults.

        Examples
        --------
        >>> SetNameResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetNameResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["warningCode"] = self._warning_code
        json_data["suggestedName"] = self._suggested_name
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "warning_code :  %s\nsuggested_name :  %s" % (self._warning_code, self._suggested_name)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def warning_code(self) -> WarningCode:
        """Warning code associated with the set name of control.
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, value: WarningCode):
        self._warning_code = value

    @property
    def suggested_name(self) -> str:
        """Override name of a control.
        """
        return self._suggested_name

    @suggested_name.setter
    def suggested_name(self, value: str):
        self._suggested_name = value
