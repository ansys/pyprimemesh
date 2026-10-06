# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class GapSealEvaluationOption(enum.IntEnum):
    """Indicates the scope granularity to apply gap sealing.
    """
    ZONELETS = 0
    """Applies gap sealing on the selected zonelets."""
    BODIES = 1
    """Applies gap sealing on the bodies."""
    PARTS = 2
    """Applies gap sealing on the parts."""

class SweepType(enum.IntEnum):
    """Provides the Sweep Mesh Decomposition type.
    """
    STANDARD = 1
    """Multizone create mapped and swept blocks if possible (should be default).

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    THINSWEEP = 2
    """Creates swept blocks on thin wall geometries.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MEDIALAXIS = 3
    """Creates swept blocks on axisymmetric sweepable geometries.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    PROGRAMCONTROLLED = 4
    """Multizone chooses the best decomposition method based on geometry analysis and decomposition tries.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class MultizonePrismType(enum.IntEnum):
    """Provides the multizone prism type//.name -> multizoneprismtype
    """
    UNIFORM = 2
    """Prescribed first prism layer height.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    LASTASPECTRATIO = 4
    """Prescribed last prism layer's aspect ratio.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FIRSTASPECTRATIO = 5
    """Prescribed first prism layer's aspect ratio.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class LeakPreventionParams(CoreObject):
    """LeakPreventionParams defines leakage prevention control parameters for wrapper.

    Parameters
    ----------
    model : Model
        Model to create a ``LeakPreventionParams`` object with default parameters.
    material_points : List[str], optional
        Material points used for leak prevention control.
    scope : ScopeDefinition, optional
        Scope used for leak prevention control.
    max_hole_size : float, optional
        Maximum hole size to prevent leakage into region.
    n_expansion_layers : int, optional
        Number of layers to expand leaking region.
    json_data : dict, optional
        JSON dictionary to create a ``LeakPreventionParams`` object with provided parameters.

    Examples
    --------
    >>> leak_prevention_params = prime.LeakPreventionParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            material_points : List[str],
            scope : ScopeDefinition,
            max_hole_size : float,
            n_expansion_layers : int):
        self._material_points = material_points
        self._scope = scope
        self._max_hole_size = max_hole_size
        self._n_expansion_layers = n_expansion_layers

    def __init__(
            self,
            model: CommunicationManager=None,
            material_points : List[str] = None,
            scope : ScopeDefinition = None,
            max_hole_size : float = None,
            n_expansion_layers : int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``LeakPreventionParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``LeakPreventionParams`` object with default parameters.
        material_points : List[str], optional
            Material points used for leak prevention control.
        scope : ScopeDefinition, optional
            Scope used for leak prevention control.
        max_hole_size : float, optional
            Maximum hole size to prevent leakage into region.
        n_expansion_layers : int, optional
            Number of layers to expand leaking region.
        json_data : dict, optional
            JSON dictionary to create a ``LeakPreventionParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            material_points : List[str] = None,
            scope : ScopeDefinition = None,
            max_hole_size : float = None,
            n_expansion_layers : int = None):
        """Set the default values of the ``LeakPreventionParams`` object.

        Parameters
        ----------
        material_points : List[str], optional
            Material points used for leak prevention control.
        scope : ScopeDefinition, optional
            Scope used for leak prevention control.
        max_hole_size : float, optional
            Maximum hole size to prevent leakage into region.
        n_expansion_layers : int, optional
            Number of layers to expand leaking region.
        """
        args = locals()
        [LeakPreventionParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``LeakPreventionParams`` object.

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
            json_data["scope"] = self._scope if isinstance(self._scope, dict) else self._scope._jsonify()
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

    Parameters
    ----------
    model : Model
        Model to create a ``SetLeakPreventionsResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with the set leak preventions.
    ids : Iterable[int], optional
        Ids of added leak prevention controls.
    json_data : dict, optional
        JSON dictionary to create a ``SetLeakPreventionsResults`` object with provided parameters.

    Examples
    --------
    >>> set_leak_preventions_results = prime.SetLeakPreventionsResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode,
            ids : Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            ids : Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetLeakPreventionsResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetLeakPreventionsResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with the set leak preventions.
        ids : Iterable[int], optional
            Ids of added leak prevention controls.
        json_data : dict, optional
            JSON dictionary to create a ``SetLeakPreventionsResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetLeakPreventionsResults")
                    json_data = param_json["SetLeakPreventionsResults"] if "SetLeakPreventionsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetLeakPreventionsResults._default_params["error_code"] if "error_code" in SetLeakPreventionsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        ids if ids is not None else ( SetLeakPreventionsResults._default_params["ids"] if "ids" in SetLeakPreventionsResults._default_params else (json_data["ids"] if "ids" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None,
            ids : Iterable[int] = None):
        """Set the default values of the ``SetLeakPreventionsResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with the set leak preventions.
        ids : Iterable[int], optional
            Ids of added leak prevention controls.
        """
        args = locals()
        [SetLeakPreventionsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetLeakPreventionsResults`` object.

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

class GapSealParams(CoreObject):
    """GapSealParams defines gap sealing control parameters for wrapper.

    Parameters
    ----------
    model : Model
        Model to create a ``GapSealParams`` object with default parameters.
    scope : ScopeDefinition, optional
        Scope used for gap sealing control.
    gap_size : float, optional
        Maximum gap size to seal.
    evaluation_option : GapSealEvaluationOption, optional
        Granularity at which gap sealing is applied.
    json_data : dict, optional
        JSON dictionary to create a ``GapSealParams`` object with provided parameters.

    Examples
    --------
    >>> gap_seal_params = prime.GapSealParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            scope : ScopeDefinition,
            gap_size : float,
            evaluation_option : GapSealEvaluationOption):
        self._scope = scope
        self._gap_size = gap_size
        self._evaluation_option = GapSealEvaluationOption(evaluation_option)

    def __init__(
            self,
            model: CommunicationManager=None,
            scope : ScopeDefinition = None,
            gap_size : float = None,
            evaluation_option : GapSealEvaluationOption = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``GapSealParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``GapSealParams`` object with default parameters.
        scope : ScopeDefinition, optional
            Scope used for gap sealing control.
        gap_size : float, optional
            Maximum gap size to seal.
        evaluation_option : GapSealEvaluationOption, optional
            Granularity at which gap sealing is applied.
        json_data : dict, optional
            JSON dictionary to create a ``GapSealParams`` object with provided parameters.

        Examples
        --------
        >>> gap_seal_params = prime.GapSealParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["scope"] if "scope" in json_data else None),
                json_data["gapSize"] if "gapSize" in json_data else None,
                GapSealEvaluationOption(json_data["evaluationOption"] if "evaluationOption" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [scope, gap_size, evaluation_option])
            if all_field_specified:
                self.__initialize(
                    scope,
                    gap_size,
                    evaluation_option)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "GapSealParams")
                    json_data = param_json["GapSealParams"] if "GapSealParams" in param_json else {}
                    self.__initialize(
                        scope if scope is not None else ( GapSealParams._default_params["scope"] if "scope" in GapSealParams._default_params else ScopeDefinition(model = model, json_data = (json_data["scope"] if "scope" in json_data else None))),
                        gap_size if gap_size is not None else ( GapSealParams._default_params["gap_size"] if "gap_size" in GapSealParams._default_params else (json_data["gapSize"] if "gapSize" in json_data else None)),
                        evaluation_option if evaluation_option is not None else ( GapSealParams._default_params["evaluation_option"] if "evaluation_option" in GapSealParams._default_params else GapSealEvaluationOption(json_data["evaluationOption"] if "evaluationOption" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            scope : ScopeDefinition = None,
            gap_size : float = None,
            evaluation_option : GapSealEvaluationOption = None):
        """Set the default values of the ``GapSealParams`` object.

        Parameters
        ----------
        scope : ScopeDefinition, optional
            Scope used for gap sealing control.
        gap_size : float, optional
            Maximum gap size to seal.
        evaluation_option : GapSealEvaluationOption, optional
            Granularity at which gap sealing is applied.
        """
        args = locals()
        [GapSealParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``GapSealParams`` object.

        Examples
        --------
        >>> GapSealParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in GapSealParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._scope is not None:
            json_data["scope"] = self._scope if isinstance(self._scope, dict) else self._scope._jsonify()
        if self._gap_size is not None:
            json_data["gapSize"] = self._gap_size
        if self._evaluation_option is not None:
            json_data["evaluationOption"] = self._evaluation_option
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "scope :  %s\ngap_size :  %s\nevaluation_option :  %s" % ('{ ' + str(self._scope) + ' }', self._gap_size, self._evaluation_option)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def scope(self) -> ScopeDefinition:
        """Scope used for gap sealing control.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

    @property
    def gap_size(self) -> float:
        """Maximum gap size to seal.
        """
        return self._gap_size

    @gap_size.setter
    def gap_size(self, value: float):
        self._gap_size = value

    @property
    def evaluation_option(self) -> GapSealEvaluationOption:
        """Granularity at which gap sealing is applied.
        """
        return self._evaluation_option

    @evaluation_option.setter
    def evaluation_option(self, value: GapSealEvaluationOption):
        self._evaluation_option = value

class SetGapSealsResults(CoreObject):
    """Results associated with set gap seals.

    Parameters
    ----------
    model : Model
        Model to create a ``SetGapSealsResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with the set gap seals.
    ids : Iterable[int], optional
        Ids of added gap seal controls.
    json_data : dict, optional
        JSON dictionary to create a ``SetGapSealsResults`` object with provided parameters.

    Examples
    --------
    >>> set_gap_seals_results = prime.SetGapSealsResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode,
            ids : Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            ids : Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetGapSealsResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetGapSealsResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with the set gap seals.
        ids : Iterable[int], optional
            Ids of added gap seal controls.
        json_data : dict, optional
            JSON dictionary to create a ``SetGapSealsResults`` object with provided parameters.

        Examples
        --------
        >>> set_gap_seals_results = prime.SetGapSealsResults(model = model)
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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetGapSealsResults")
                    json_data = param_json["SetGapSealsResults"] if "SetGapSealsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetGapSealsResults._default_params["error_code"] if "error_code" in SetGapSealsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        ids if ids is not None else ( SetGapSealsResults._default_params["ids"] if "ids" in SetGapSealsResults._default_params else (json_data["ids"] if "ids" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None,
            ids : Iterable[int] = None):
        """Set the default values of the ``SetGapSealsResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with the set gap seals.
        ids : Iterable[int], optional
            Ids of added gap seal controls.
        """
        args = locals()
        [SetGapSealsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetGapSealsResults`` object.

        Examples
        --------
        >>> SetGapSealsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetGapSealsResults._default_params.items())
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
        """Error code associated with the set gap seals.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def ids(self) -> Iterable[int]:
        """Ids of added gap seal controls.
        """
        return self._ids

    @ids.setter
    def ids(self, value: Iterable[int]):
        self._ids = value

class ContactPreventionParams(CoreObject):
    """ContactPreventionParams defines contact prevention control parameters for wrapper.

    Parameters
    ----------
    model : Model
        Model to create a ``ContactPreventionParams`` object with default parameters.
    source_scope : ScopeDefinition, optional
        Source scope used for contact prevention control.
    target_scope : ScopeDefinition, optional
        Target scope used for contact prevention control.
    size : float, optional
        Minimum gap size (gap/4) to resolve contact between source and target.
    json_data : dict, optional
        JSON dictionary to create a ``ContactPreventionParams`` object with provided parameters.

    Examples
    --------
    >>> contact_prevention_params = prime.ContactPreventionParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            source_scope : ScopeDefinition,
            target_scope : ScopeDefinition,
            size : float):
        self._source_scope = source_scope
        self._target_scope = target_scope
        self._size = size

    def __init__(
            self,
            model: CommunicationManager=None,
            source_scope : ScopeDefinition = None,
            target_scope : ScopeDefinition = None,
            size : float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ContactPreventionParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``ContactPreventionParams`` object with default parameters.
        source_scope : ScopeDefinition, optional
            Source scope used for contact prevention control.
        target_scope : ScopeDefinition, optional
            Target scope used for contact prevention control.
        size : float, optional
            Minimum gap size (gap/4) to resolve contact between source and target.
        json_data : dict, optional
            JSON dictionary to create a ``ContactPreventionParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ContactPreventionParams")
                    json_data = param_json["ContactPreventionParams"] if "ContactPreventionParams" in param_json else {}
                    self.__initialize(
                        source_scope if source_scope is not None else ( ContactPreventionParams._default_params["source_scope"] if "source_scope" in ContactPreventionParams._default_params else ScopeDefinition(model = model, json_data = (json_data["sourceScope"] if "sourceScope" in json_data else None))),
                        target_scope if target_scope is not None else ( ContactPreventionParams._default_params["target_scope"] if "target_scope" in ContactPreventionParams._default_params else ScopeDefinition(model = model, json_data = (json_data["targetScope"] if "targetScope" in json_data else None))),
                        size if size is not None else ( ContactPreventionParams._default_params["size"] if "size" in ContactPreventionParams._default_params else (json_data["size"] if "size" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            source_scope : ScopeDefinition = None,
            target_scope : ScopeDefinition = None,
            size : float = None):
        """Set the default values of the ``ContactPreventionParams`` object.

        Parameters
        ----------
        source_scope : ScopeDefinition, optional
            Source scope used for contact prevention control.
        target_scope : ScopeDefinition, optional
            Target scope used for contact prevention control.
        size : float, optional
            Minimum gap size (gap/4) to resolve contact between source and target.
        """
        args = locals()
        [ContactPreventionParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ContactPreventionParams`` object.

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
            json_data["sourceScope"] = self._source_scope if isinstance(self._source_scope, dict) else self._source_scope._jsonify()
        if self._target_scope is not None:
            json_data["targetScope"] = self._target_scope if isinstance(self._target_scope, dict) else self._target_scope._jsonify()
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

    Parameters
    ----------
    model : Model
        Model to create a ``SetContactPreventionsResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with the set contact preventions.
    ids : Iterable[int], optional
        Ids of added contact prevention controls.
    json_data : dict, optional
        JSON dictionary to create a ``SetContactPreventionsResults`` object with provided parameters.

    Examples
    --------
    >>> set_contact_preventions_results = prime.SetContactPreventionsResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode,
            ids : Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            ids : Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetContactPreventionsResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetContactPreventionsResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with the set contact preventions.
        ids : Iterable[int], optional
            Ids of added contact prevention controls.
        json_data : dict, optional
            JSON dictionary to create a ``SetContactPreventionsResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetContactPreventionsResults")
                    json_data = param_json["SetContactPreventionsResults"] if "SetContactPreventionsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetContactPreventionsResults._default_params["error_code"] if "error_code" in SetContactPreventionsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        ids if ids is not None else ( SetContactPreventionsResults._default_params["ids"] if "ids" in SetContactPreventionsResults._default_params else (json_data["ids"] if "ids" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None,
            ids : Iterable[int] = None):
        """Set the default values of the ``SetContactPreventionsResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with the set contact preventions.
        ids : Iterable[int], optional
            Ids of added contact prevention controls.
        """
        args = locals()
        [SetContactPreventionsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetContactPreventionsResults`` object.

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

    Parameters
    ----------
    model : Model
        Model to create a ``FeatureRecoveryParams`` object with default parameters.
    scope : ScopeDefinition, optional
        Scope used for feature recovery control.
    enable_feature_octree_refinement : bool, optional
        Checks whether to perform octree refinement at feature edges.
    size_at_features : float, optional
        Refinement size at features.
    json_data : dict, optional
        JSON dictionary to create a ``FeatureRecoveryParams`` object with provided parameters.

    Examples
    --------
    >>> feature_recovery_params = prime.FeatureRecoveryParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            scope : ScopeDefinition,
            enable_feature_octree_refinement : bool,
            size_at_features : float):
        self._scope = scope
        self._enable_feature_octree_refinement = enable_feature_octree_refinement
        self._size_at_features = size_at_features

    def __init__(
            self,
            model: CommunicationManager=None,
            scope : ScopeDefinition = None,
            enable_feature_octree_refinement : bool = None,
            size_at_features : float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``FeatureRecoveryParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``FeatureRecoveryParams`` object with default parameters.
        scope : ScopeDefinition, optional
            Scope used for feature recovery control.
        enable_feature_octree_refinement : bool, optional
            Checks whether to perform octree refinement at feature edges.
        size_at_features : float, optional
            Refinement size at features.
        json_data : dict, optional
            JSON dictionary to create a ``FeatureRecoveryParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "FeatureRecoveryParams")
                    json_data = param_json["FeatureRecoveryParams"] if "FeatureRecoveryParams" in param_json else {}
                    self.__initialize(
                        scope if scope is not None else ( FeatureRecoveryParams._default_params["scope"] if "scope" in FeatureRecoveryParams._default_params else ScopeDefinition(model = model, json_data = (json_data["scope"] if "scope" in json_data else None))),
                        enable_feature_octree_refinement if enable_feature_octree_refinement is not None else ( FeatureRecoveryParams._default_params["enable_feature_octree_refinement"] if "enable_feature_octree_refinement" in FeatureRecoveryParams._default_params else (json_data["enableFeatureOctreeRefinement"] if "enableFeatureOctreeRefinement" in json_data else None)),
                        size_at_features if size_at_features is not None else ( FeatureRecoveryParams._default_params["size_at_features"] if "size_at_features" in FeatureRecoveryParams._default_params else (json_data["sizeAtFeatures"] if "sizeAtFeatures" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            scope : ScopeDefinition = None,
            enable_feature_octree_refinement : bool = None,
            size_at_features : float = None):
        """Set the default values of the ``FeatureRecoveryParams`` object.

        Parameters
        ----------
        scope : ScopeDefinition, optional
            Scope used for feature recovery control.
        enable_feature_octree_refinement : bool, optional
            Checks whether to perform octree refinement at feature edges.
        size_at_features : float, optional
            Refinement size at features.
        """
        args = locals()
        [FeatureRecoveryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FeatureRecoveryParams`` object.

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
            json_data["scope"] = self._scope if isinstance(self._scope, dict) else self._scope._jsonify()
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

    Parameters
    ----------
    model : Model
        Model to create a ``SetFeatureRecoveriesResults`` object with default parameters.
    ids : Iterable[int], optional
        Ids of added feature recovery controls.
    error_code : ErrorCode, optional
        Error code associated with the set feature recoveries.
    json_data : dict, optional
        JSON dictionary to create a ``SetFeatureRecoveriesResults`` object with provided parameters.

    Examples
    --------
    >>> set_feature_recoveries_results = prime.SetFeatureRecoveriesResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            ids : Iterable[int],
            error_code : ErrorCode):
        self._ids = ids if isinstance(ids, np.ndarray) else np.array(ids, dtype=np.int32) if ids is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            ids : Iterable[int] = None,
            error_code : ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetFeatureRecoveriesResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetFeatureRecoveriesResults`` object with default parameters.
        ids : Iterable[int], optional
            Ids of added feature recovery controls.
        error_code : ErrorCode, optional
            Error code associated with the set feature recoveries.
        json_data : dict, optional
            JSON dictionary to create a ``SetFeatureRecoveriesResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetFeatureRecoveriesResults")
                    json_data = param_json["SetFeatureRecoveriesResults"] if "SetFeatureRecoveriesResults" in param_json else {}
                    self.__initialize(
                        ids if ids is not None else ( SetFeatureRecoveriesResults._default_params["ids"] if "ids" in SetFeatureRecoveriesResults._default_params else (json_data["ids"] if "ids" in json_data else None)),
                        error_code if error_code is not None else ( SetFeatureRecoveriesResults._default_params["error_code"] if "error_code" in SetFeatureRecoveriesResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            ids : Iterable[int] = None,
            error_code : ErrorCode = None):
        """Set the default values of the ``SetFeatureRecoveriesResults`` object.

        Parameters
        ----------
        ids : Iterable[int], optional
            Ids of added feature recovery controls.
        error_code : ErrorCode, optional
            Error code associated with the set feature recoveries.
        """
        args = locals()
        [SetFeatureRecoveriesResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetFeatureRecoveriesResults`` object.

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

    Parameters
    ----------
    model : Model
        Model to create a ``ScopeZoneletParams`` object with default parameters.
    json_data : dict, optional
        JSON dictionary to create a ``ScopeZoneletParams`` object with provided parameters.

    Examples
    --------
    >>> scope_zonelet_params = prime.ScopeZoneletParams(model = model)
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
        """Initialize a ``ScopeZoneletParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``ScopeZoneletParams`` object with default parameters.
        json_data : dict, optional
            JSON dictionary to create a ``ScopeZoneletParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ScopeZoneletParams")
                    json_data = param_json["ScopeZoneletParams"] if "ScopeZoneletParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of the ``ScopeZoneletParams`` object.

        """
        args = locals()
        [ScopeZoneletParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ScopeZoneletParams`` object.

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
        if len(message) == 0:
            message = 'The object has no parameters to print.'
        return message

class SetScopeResults(CoreObject):
    """Results associated with the set scope operation.

    Parameters
    ----------
    model : Model
        Model to create a ``SetScopeResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with the set scope.
    warning_code : WarningCode, optional
        Warning code associated with the set scope.
    json_data : dict, optional
        JSON dictionary to create a ``SetScopeResults`` object with provided parameters.

    Examples
    --------
    >>> set_scope_results = prime.SetScopeResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode,
            warning_code : WarningCode):
        self._error_code = ErrorCode(error_code)
        self._warning_code = WarningCode(warning_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            warning_code : WarningCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetScopeResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetScopeResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with the set scope.
        warning_code : WarningCode, optional
            Warning code associated with the set scope.
        json_data : dict, optional
            JSON dictionary to create a ``SetScopeResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetScopeResults")
                    json_data = param_json["SetScopeResults"] if "SetScopeResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetScopeResults._default_params["error_code"] if "error_code" in SetScopeResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_code if warning_code is not None else ( SetScopeResults._default_params["warning_code"] if "warning_code" in SetScopeResults._default_params else WarningCode(json_data["warningCode"] if "warningCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None,
            warning_code : WarningCode = None):
        """Set the default values of the ``SetScopeResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with the set scope.
        warning_code : WarningCode, optional
            Warning code associated with the set scope.
        """
        args = locals()
        [SetScopeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetScopeResults`` object.

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

class SetParamsResults(CoreObject):
    """Results associated with the set parameters operation.

    Parameters
    ----------
    model : Model
        Model to create a ``SetParamsResults`` object with default parameters.
    error_code : ErrorCode, optional
        Error code associated with the set parameters operation.
    warning_code : WarningCode, optional
        Warning code associated with the set parameters operation.
    json_data : dict, optional
        JSON dictionary to create a ``SetParamsResults`` object with provided parameters.

    Examples
    --------
    >>> set_params_results = prime.SetParamsResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code : ErrorCode,
            warning_code : WarningCode):
        self._error_code = ErrorCode(error_code)
        self._warning_code = WarningCode(warning_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code : ErrorCode = None,
            warning_code : WarningCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SetParamsResults`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``SetParamsResults`` object with default parameters.
        error_code : ErrorCode, optional
            Error code associated with the set parameters operation.
        warning_code : WarningCode, optional
            Warning code associated with the set parameters operation.
        json_data : dict, optional
            JSON dictionary to create a ``SetParamsResults`` object with provided parameters.

        Examples
        --------
        >>> set_params_results = prime.SetParamsResults(model = model)
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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SetParamsResults")
                    json_data = param_json["SetParamsResults"] if "SetParamsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SetParamsResults._default_params["error_code"] if "error_code" in SetParamsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_code if warning_code is not None else ( SetParamsResults._default_params["warning_code"] if "warning_code" in SetParamsResults._default_params else WarningCode(json_data["warningCode"] if "warningCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code : ErrorCode = None,
            warning_code : WarningCode = None):
        """Set the default values of the ``SetParamsResults`` object.

        Parameters
        ----------
        error_code : ErrorCode, optional
            Error code associated with the set parameters operation.
        warning_code : WarningCode, optional
            Warning code associated with the set parameters operation.
        """
        args = locals()
        [SetParamsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SetParamsResults`` object.

        Examples
        --------
        >>> SetParamsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetParamsResults._default_params.items())
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
        """Error code associated with the set parameters operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_code(self) -> WarningCode:
        """Warning code associated with the set parameters operation.
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, value: WarningCode):
        self._warning_code = value

class MultiZoneSweepMeshParams(CoreObject):
    """Defines MultiZone thin sweep mesh control parameters.

    Parameters
    ----------
    model : Model
        Model to create a ``MultiZoneSweepMeshParams`` object with default parameters.
    source_and_target_scope : ScopeDefinition, optional
        Source and target faces used to determine the direction of sweep in MultiZone meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    sweep_mesh_size : float, optional
        Sweep mesh size used to determine the mesh size and number of divisions in the sweep direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    n_divisions : int, optional
        Number of divisions in the sweep direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    thin_sweep : bool, optional
        Thin sweep option set to True will generate sweep mesh in thin volumes by respecting nDivisions.   Thin sweep option set to False will generate sweep mesh whose number of divisions in the direction of sweep is determined by sweepMeshSize.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    sweep_type : SweepType, optional
        Option to specify the sweep mesh decomposition type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data : dict, optional
        JSON dictionary to create a ``MultiZoneSweepMeshParams`` object with provided parameters.

    Examples
    --------
    >>> multi_zone_sweep_mesh_params = prime.MultiZoneSweepMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            source_and_target_scope : ScopeDefinition,
            sweep_mesh_size : float,
            n_divisions : int,
            thin_sweep : bool,
            sweep_type : SweepType):
        self._source_and_target_scope = source_and_target_scope
        self._sweep_mesh_size = sweep_mesh_size
        self._n_divisions = n_divisions
        self._thin_sweep = thin_sweep
        self._sweep_type = SweepType(sweep_type)

    def __init__(
            self,
            model: CommunicationManager=None,
            source_and_target_scope : ScopeDefinition = None,
            sweep_mesh_size : float = None,
            n_divisions : int = None,
            thin_sweep : bool = None,
            sweep_type : SweepType = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``MultiZoneSweepMeshParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``MultiZoneSweepMeshParams`` object with default parameters.
        source_and_target_scope : ScopeDefinition, optional
            Source and target faces used to determine the direction of sweep in MultiZone meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        sweep_mesh_size : float, optional
            Sweep mesh size used to determine the mesh size and number of divisions in the sweep direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        n_divisions : int, optional
            Number of divisions in the sweep direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        thin_sweep : bool, optional
            Thin sweep option set to True will generate sweep mesh in thin volumes by respecting nDivisions.   Thin sweep option set to False will generate sweep mesh whose number of divisions in the direction of sweep is determined by sweepMeshSize.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        sweep_type : SweepType, optional
            Option to specify the sweep mesh decomposition type.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data : dict, optional
            JSON dictionary to create a ``MultiZoneSweepMeshParams`` object with provided parameters.

        Examples
        --------
        >>> multi_zone_sweep_mesh_params = prime.MultiZoneSweepMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["sourceAndTargetScope"] if "sourceAndTargetScope" in json_data else None),
                json_data["sweepMeshSize"] if "sweepMeshSize" in json_data else None,
                json_data["nDivisions"] if "nDivisions" in json_data else None,
                json_data["thinSweep"] if "thinSweep" in json_data else None,
                SweepType(json_data["sweepType"] if "sweepType" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [source_and_target_scope, sweep_mesh_size, n_divisions, thin_sweep, sweep_type])
            if all_field_specified:
                self.__initialize(
                    source_and_target_scope,
                    sweep_mesh_size,
                    n_divisions,
                    thin_sweep,
                    sweep_type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "MultiZoneSweepMeshParams")
                    json_data = param_json["MultiZoneSweepMeshParams"] if "MultiZoneSweepMeshParams" in param_json else {}
                    self.__initialize(
                        source_and_target_scope if source_and_target_scope is not None else ( MultiZoneSweepMeshParams._default_params["source_and_target_scope"] if "source_and_target_scope" in MultiZoneSweepMeshParams._default_params else ScopeDefinition(model = model, json_data = (json_data["sourceAndTargetScope"] if "sourceAndTargetScope" in json_data else None))),
                        sweep_mesh_size if sweep_mesh_size is not None else ( MultiZoneSweepMeshParams._default_params["sweep_mesh_size"] if "sweep_mesh_size" in MultiZoneSweepMeshParams._default_params else (json_data["sweepMeshSize"] if "sweepMeshSize" in json_data else None)),
                        n_divisions if n_divisions is not None else ( MultiZoneSweepMeshParams._default_params["n_divisions"] if "n_divisions" in MultiZoneSweepMeshParams._default_params else (json_data["nDivisions"] if "nDivisions" in json_data else None)),
                        thin_sweep if thin_sweep is not None else ( MultiZoneSweepMeshParams._default_params["thin_sweep"] if "thin_sweep" in MultiZoneSweepMeshParams._default_params else (json_data["thinSweep"] if "thinSweep" in json_data else None)),
                        sweep_type if sweep_type is not None else ( MultiZoneSweepMeshParams._default_params["sweep_type"] if "sweep_type" in MultiZoneSweepMeshParams._default_params else SweepType(json_data["sweepType"] if "sweepType" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            source_and_target_scope : ScopeDefinition = None,
            sweep_mesh_size : float = None,
            n_divisions : int = None,
            thin_sweep : bool = None,
            sweep_type : SweepType = None):
        """Set the default values of the ``MultiZoneSweepMeshParams`` object.

        Parameters
        ----------
        source_and_target_scope : ScopeDefinition, optional
            Source and target faces used to determine the direction of sweep in MultiZone meshing.
        sweep_mesh_size : float, optional
            Sweep mesh size used to determine the mesh size and number of divisions in the sweep direction.
        n_divisions : int, optional
            Number of divisions in the sweep direction.
        thin_sweep : bool, optional
            Thin sweep option set to True will generate sweep mesh in thin volumes by respecting nDivisions.   Thin sweep option set to False will generate sweep mesh whose number of divisions in the direction of sweep is determined by sweepMeshSize.
        sweep_type : SweepType, optional
            Option to specify the sweep mesh decomposition type.
        """
        args = locals()
        [MultiZoneSweepMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``MultiZoneSweepMeshParams`` object.

        Examples
        --------
        >>> MultiZoneSweepMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MultiZoneSweepMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._source_and_target_scope is not None:
            json_data["sourceAndTargetScope"] = self._source_and_target_scope if isinstance(self._source_and_target_scope, dict) else self._source_and_target_scope._jsonify()
        if self._sweep_mesh_size is not None:
            json_data["sweepMeshSize"] = self._sweep_mesh_size
        if self._n_divisions is not None:
            json_data["nDivisions"] = self._n_divisions
        if self._thin_sweep is not None:
            json_data["thinSweep"] = self._thin_sweep
        if self._sweep_type is not None:
            json_data["sweepType"] = self._sweep_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "source_and_target_scope :  %s\nsweep_mesh_size :  %s\nn_divisions :  %s\nthin_sweep :  %s\nsweep_type :  %s" % ('{ ' + str(self._source_and_target_scope) + ' }', self._sweep_mesh_size, self._n_divisions, self._thin_sweep, self._sweep_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def source_and_target_scope(self) -> ScopeDefinition:
        """Source and target faces used to determine the direction of sweep in MultiZone meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._source_and_target_scope

    @source_and_target_scope.setter
    def source_and_target_scope(self, value: ScopeDefinition):
        self._source_and_target_scope = value

    @property
    def sweep_mesh_size(self) -> float:
        """Sweep mesh size used to determine the mesh size and number of divisions in the sweep direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._sweep_mesh_size

    @sweep_mesh_size.setter
    def sweep_mesh_size(self, value: float):
        self._sweep_mesh_size = value

    @property
    def n_divisions(self) -> int:
        """Number of divisions in the sweep direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._n_divisions

    @n_divisions.setter
    def n_divisions(self, value: int):
        self._n_divisions = value

    @property
    def thin_sweep(self) -> bool:
        """Thin sweep option set to True will generate sweep mesh in thin volumes by respecting nDivisions.   Thin sweep option set to False will generate sweep mesh whose number of divisions in the direction of sweep is determined by sweepMeshSize.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._thin_sweep

    @thin_sweep.setter
    def thin_sweep(self, value: bool):
        self._thin_sweep = value

    @property
    def sweep_type(self) -> SweepType:
        """Option to specify the sweep mesh decomposition type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._sweep_type

    @sweep_type.setter
    def sweep_type(self, value: SweepType):
        self._sweep_type = value

class MultiZoneEdgeBiasingParams(CoreObject):
    """Defines MultiZone edge biasing control parameters.

    Parameters
    ----------
    model : Model
        Model to create a ``MultiZoneEdgeBiasingParams`` object with default parameters.
    face_scope : ScopeDefinition, optional
        Reference face zonelets to control mesh clustering orientation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    edge_scope : ScopeDefinition, optional
        Edge zonelets to control the expanse of edge biasing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    bias_factor : float, optional
        Bias factor used for MultiZone edge biasing control.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    n_divisions : int, optional
        Number of divisions on the section where edge biasing is done.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data : dict, optional
        JSON dictionary to create a ``MultiZoneEdgeBiasingParams`` object with provided parameters.

    Examples
    --------
    >>> multi_zone_edge_biasing_params = prime.MultiZoneEdgeBiasingParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            face_scope : ScopeDefinition,
            edge_scope : ScopeDefinition,
            bias_factor : float,
            n_divisions : int):
        self._face_scope = face_scope
        self._edge_scope = edge_scope
        self._bias_factor = bias_factor
        self._n_divisions = n_divisions

    def __init__(
            self,
            model: CommunicationManager=None,
            face_scope : ScopeDefinition = None,
            edge_scope : ScopeDefinition = None,
            bias_factor : float = None,
            n_divisions : int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``MultiZoneEdgeBiasingParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``MultiZoneEdgeBiasingParams`` object with default parameters.
        face_scope : ScopeDefinition, optional
            Reference face zonelets to control mesh clustering orientation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        edge_scope : ScopeDefinition, optional
            Edge zonelets to control the expanse of edge biasing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        bias_factor : float, optional
            Bias factor used for MultiZone edge biasing control.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        n_divisions : int, optional
            Number of divisions on the section where edge biasing is done.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data : dict, optional
            JSON dictionary to create a ``MultiZoneEdgeBiasingParams`` object with provided parameters.

        Examples
        --------
        >>> multi_zone_edge_biasing_params = prime.MultiZoneEdgeBiasingParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["faceScope"] if "faceScope" in json_data else None),
                ScopeDefinition(model = model, json_data = json_data["edgeScope"] if "edgeScope" in json_data else None),
                json_data["biasFactor"] if "biasFactor" in json_data else None,
                json_data["nDivisions"] if "nDivisions" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [face_scope, edge_scope, bias_factor, n_divisions])
            if all_field_specified:
                self.__initialize(
                    face_scope,
                    edge_scope,
                    bias_factor,
                    n_divisions)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "MultiZoneEdgeBiasingParams")
                    json_data = param_json["MultiZoneEdgeBiasingParams"] if "MultiZoneEdgeBiasingParams" in param_json else {}
                    self.__initialize(
                        face_scope if face_scope is not None else ( MultiZoneEdgeBiasingParams._default_params["face_scope"] if "face_scope" in MultiZoneEdgeBiasingParams._default_params else ScopeDefinition(model = model, json_data = (json_data["faceScope"] if "faceScope" in json_data else None))),
                        edge_scope if edge_scope is not None else ( MultiZoneEdgeBiasingParams._default_params["edge_scope"] if "edge_scope" in MultiZoneEdgeBiasingParams._default_params else ScopeDefinition(model = model, json_data = (json_data["edgeScope"] if "edgeScope" in json_data else None))),
                        bias_factor if bias_factor is not None else ( MultiZoneEdgeBiasingParams._default_params["bias_factor"] if "bias_factor" in MultiZoneEdgeBiasingParams._default_params else (json_data["biasFactor"] if "biasFactor" in json_data else None)),
                        n_divisions if n_divisions is not None else ( MultiZoneEdgeBiasingParams._default_params["n_divisions"] if "n_divisions" in MultiZoneEdgeBiasingParams._default_params else (json_data["nDivisions"] if "nDivisions" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            face_scope : ScopeDefinition = None,
            edge_scope : ScopeDefinition = None,
            bias_factor : float = None,
            n_divisions : int = None):
        """Set the default values of the ``MultiZoneEdgeBiasingParams`` object.

        Parameters
        ----------
        face_scope : ScopeDefinition, optional
            Reference face zonelets to control mesh clustering orientation.
        edge_scope : ScopeDefinition, optional
            Edge zonelets to control the expanse of edge biasing.
        bias_factor : float, optional
            Bias factor used for MultiZone edge biasing control.
        n_divisions : int, optional
            Number of divisions on the section where edge biasing is done.
        """
        args = locals()
        [MultiZoneEdgeBiasingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``MultiZoneEdgeBiasingParams`` object.

        Examples
        --------
        >>> MultiZoneEdgeBiasingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MultiZoneEdgeBiasingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._face_scope is not None:
            json_data["faceScope"] = self._face_scope if isinstance(self._face_scope, dict) else self._face_scope._jsonify()
        if self._edge_scope is not None:
            json_data["edgeScope"] = self._edge_scope if isinstance(self._edge_scope, dict) else self._edge_scope._jsonify()
        if self._bias_factor is not None:
            json_data["biasFactor"] = self._bias_factor
        if self._n_divisions is not None:
            json_data["nDivisions"] = self._n_divisions
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "face_scope :  %s\nedge_scope :  %s\nbias_factor :  %s\nn_divisions :  %s" % ('{ ' + str(self._face_scope) + ' }', '{ ' + str(self._edge_scope) + ' }', self._bias_factor, self._n_divisions)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def face_scope(self) -> ScopeDefinition:
        """Reference face zonelets to control mesh clustering orientation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._face_scope

    @face_scope.setter
    def face_scope(self, value: ScopeDefinition):
        self._face_scope = value

    @property
    def edge_scope(self) -> ScopeDefinition:
        """Edge zonelets to control the expanse of edge biasing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_scope

    @edge_scope.setter
    def edge_scope(self, value: ScopeDefinition):
        self._edge_scope = value

    @property
    def bias_factor(self) -> float:
        """Bias factor used for MultiZone edge biasing control.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._bias_factor

    @bias_factor.setter
    def bias_factor(self, value: float):
        self._bias_factor = value

    @property
    def n_divisions(self) -> int:
        """Number of divisions on the section where edge biasing is done.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._n_divisions

    @n_divisions.setter
    def n_divisions(self, value: int):
        self._n_divisions = value

class MultiZoneMapMeshParams(CoreObject):
    """Define controlling parameters for the map mesh using MultiZone.

    Parameters
    ----------
    model : Model
        Model to create a ``MultiZoneMapMeshParams`` object with default parameters.
    scope : ScopeDefinition, optional
        Scope used for MultiZone map mesh control.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data : dict, optional
        JSON dictionary to create a ``MultiZoneMapMeshParams`` object with provided parameters.

    Examples
    --------
    >>> multi_zone_map_mesh_params = prime.MultiZoneMapMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            scope : ScopeDefinition):
        self._scope = scope

    def __init__(
            self,
            model: CommunicationManager=None,
            scope : ScopeDefinition = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``MultiZoneMapMeshParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``MultiZoneMapMeshParams`` object with default parameters.
        scope : ScopeDefinition, optional
            Scope used for MultiZone map mesh control.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data : dict, optional
            JSON dictionary to create a ``MultiZoneMapMeshParams`` object with provided parameters.

        Examples
        --------
        >>> multi_zone_map_mesh_params = prime.MultiZoneMapMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                ScopeDefinition(model = model, json_data = json_data["scope"] if "scope" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [scope])
            if all_field_specified:
                self.__initialize(
                    scope)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "MultiZoneMapMeshParams")
                    json_data = param_json["MultiZoneMapMeshParams"] if "MultiZoneMapMeshParams" in param_json else {}
                    self.__initialize(
                        scope if scope is not None else ( MultiZoneMapMeshParams._default_params["scope"] if "scope" in MultiZoneMapMeshParams._default_params else ScopeDefinition(model = model, json_data = (json_data["scope"] if "scope" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            scope : ScopeDefinition = None):
        """Set the default values of the ``MultiZoneMapMeshParams`` object.

        Parameters
        ----------
        scope : ScopeDefinition, optional
            Scope used for MultiZone map mesh control.
        """
        args = locals()
        [MultiZoneMapMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``MultiZoneMapMeshParams`` object.

        Examples
        --------
        >>> MultiZoneMapMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MultiZoneMapMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._scope is not None:
            json_data["scope"] = self._scope if isinstance(self._scope, dict) else self._scope._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "scope :  %s" % ('{ ' + str(self._scope) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def scope(self) -> ScopeDefinition:
        """Scope used for MultiZone map mesh control.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._scope = value

class MultiZoneSizingParams(CoreObject):
    """Parameters for MultiZone meshing.

    Parameters
    ----------
    model : Model
        Model to create a ``MultiZoneSizingParams`` object with default parameters.
    max_size : float, optional
        Defines global maximum mesh size.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    min_size : float, optional
        Defines global minimum mesh size.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    growth_rate : float, optional
        Defines growth rate.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    use_volumetric_size_field : bool, optional
        Defines whether to use size field for MultiZone meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data : dict, optional
        JSON dictionary to create a ``MultiZoneSizingParams`` object with provided parameters.

    Examples
    --------
    >>> multi_zone_sizing_params = prime.MultiZoneSizingParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            max_size : float,
            min_size : float,
            growth_rate : float,
            use_volumetric_size_field : bool):
        self._max_size = max_size
        self._min_size = min_size
        self._growth_rate = growth_rate
        self._use_volumetric_size_field = use_volumetric_size_field

    def __init__(
            self,
            model: CommunicationManager=None,
            max_size : float = None,
            min_size : float = None,
            growth_rate : float = None,
            use_volumetric_size_field : bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``MultiZoneSizingParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``MultiZoneSizingParams`` object with default parameters.
        max_size : float, optional
            Defines global maximum mesh size.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        min_size : float, optional
            Defines global minimum mesh size.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        growth_rate : float, optional
            Defines growth rate.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        use_volumetric_size_field : bool, optional
            Defines whether to use size field for MultiZone meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data : dict, optional
            JSON dictionary to create a ``MultiZoneSizingParams`` object with provided parameters.

        Examples
        --------
        >>> multi_zone_sizing_params = prime.MultiZoneSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["maxSize"] if "maxSize" in json_data else None,
                json_data["minSize"] if "minSize" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["useVolumetricSizeField"] if "useVolumetricSizeField" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [max_size, min_size, growth_rate, use_volumetric_size_field])
            if all_field_specified:
                self.__initialize(
                    max_size,
                    min_size,
                    growth_rate,
                    use_volumetric_size_field)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "MultiZoneSizingParams")
                    json_data = param_json["MultiZoneSizingParams"] if "MultiZoneSizingParams" in param_json else {}
                    self.__initialize(
                        max_size if max_size is not None else ( MultiZoneSizingParams._default_params["max_size"] if "max_size" in MultiZoneSizingParams._default_params else (json_data["maxSize"] if "maxSize" in json_data else None)),
                        min_size if min_size is not None else ( MultiZoneSizingParams._default_params["min_size"] if "min_size" in MultiZoneSizingParams._default_params else (json_data["minSize"] if "minSize" in json_data else None)),
                        growth_rate if growth_rate is not None else ( MultiZoneSizingParams._default_params["growth_rate"] if "growth_rate" in MultiZoneSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        use_volumetric_size_field if use_volumetric_size_field is not None else ( MultiZoneSizingParams._default_params["use_volumetric_size_field"] if "use_volumetric_size_field" in MultiZoneSizingParams._default_params else (json_data["useVolumetricSizeField"] if "useVolumetricSizeField" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            max_size : float = None,
            min_size : float = None,
            growth_rate : float = None,
            use_volumetric_size_field : bool = None):
        """Set the default values of the ``MultiZoneSizingParams`` object.

        Parameters
        ----------
        max_size : float, optional
            Defines global maximum mesh size.
        min_size : float, optional
            Defines global minimum mesh size.
        growth_rate : float, optional
            Defines growth rate.
        use_volumetric_size_field : bool, optional
            Defines whether to use size field for MultiZone meshing.
        """
        args = locals()
        [MultiZoneSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``MultiZoneSizingParams`` object.

        Examples
        --------
        >>> MultiZoneSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MultiZoneSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._max_size is not None:
            json_data["maxSize"] = self._max_size
        if self._min_size is not None:
            json_data["minSize"] = self._min_size
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._use_volumetric_size_field is not None:
            json_data["useVolumetricSizeField"] = self._use_volumetric_size_field
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "max_size :  %s\nmin_size :  %s\ngrowth_rate :  %s\nuse_volumetric_size_field :  %s" % (self._max_size, self._min_size, self._growth_rate, self._use_volumetric_size_field)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def max_size(self) -> float:
        """Defines global maximum mesh size.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def min_size(self) -> float:
        """Defines global minimum mesh size.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value: float):
        self._min_size = value

    @property
    def growth_rate(self) -> float:
        """Defines growth rate.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def use_volumetric_size_field(self) -> bool:
        """Defines whether to use size field for MultiZone meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._use_volumetric_size_field

    @use_volumetric_size_field.setter
    def use_volumetric_size_field(self, value: bool):
        self._use_volumetric_size_field = value
