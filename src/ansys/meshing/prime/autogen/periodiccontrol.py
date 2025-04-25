# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class PeriodicControl(CoreObject):
    """Periodic controls provide settings for the recovery of periodic surfaces.

    A periodic control is specified by the scope (source surfaces) and the transformation parameters: the center, axis and angle.

    Parameters
    ----------
    model : Model
        Server model to create PeriodicControl object.
    id : int
        Id of the PeriodicControl.
    object_id : int
        Object id of the PeriodicControl.
    name : str
        Name of the PeriodicControl.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize PeriodicControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def get_params(self) -> PeriodicControlParams:
        """ Get the parameters of the periodic control.


        Returns
        -------
        PeriodicControlParams
            Return parameters of the periodic control.


        Examples
        --------
        >>> params = periodic_control.get_params()

        """
        args = {}
        command_name = "PrimeMesh::PeriodicControl/GetParams"
        self._model._print_logs_before_command("get_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_params", PeriodicControlParams(model = self._model, json_data = result))
        return PeriodicControlParams(model = self._model, json_data = result)

    def set_params(self, periodic_control_params : PeriodicControlParams) -> SetParamsResults:
        """ Set the periodic control parameters.


        Parameters
        ----------
        periodic_control_params : PeriodicControlParams
            Parameters to control periodic surface recovery.

        Examples
        --------
        >>> periodic_control.set_params(
        >>>                  PeriodicControlParams(model=model,
        >>>                     center=[0,0,0], axis=[0,1,0], angle=180))

        """
        if not isinstance(periodic_control_params, PeriodicControlParams):
            raise TypeError("Invalid argument type passed for 'periodic_control_params'. Valid argument type is PeriodicControlParams.")
        args = {"periodic_control_params" : periodic_control_params._jsonify()}
        command_name = "PrimeMesh::PeriodicControl/SetParams"
        self._model._print_logs_before_command("set_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_params", SetParamsResults(model = self._model, json_data = result))
        return SetParamsResults(model = self._model, json_data = result)

    def set_suggested_name(self, name : str) -> SetNameResults:
        """ Sets the unique name for the periodic control based on the suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the periodic control.

        Returns
        -------
        SetNameResults
            Returns the name of the periodic control.


        Examples
        --------
        >>> periodic_control.set_suggested_name("control1")

        """
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"name" : name}
        command_name = "PrimeMesh::PeriodicControl/SetSuggestedName"
        self._model._print_logs_before_command("set_suggested_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_name", SetNameResults(model = self._model, json_data = result))
        return SetNameResults(model = self._model, json_data = result)

    def get_scope(self) -> ScopeDefinition:
        """ Gets the scope for the periodic control.


        Returns
        -------
        ScopeDefinition
            Returns the scope of the periodic control.


        Examples
        --------
        >>> scope_definition = periodic_control.get_scope()

        """
        args = {}
        command_name = "PrimeMesh::PeriodicControl/GetScope"
        self._model._print_logs_before_command("get_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def set_scope(self, scope : ScopeDefinition) -> SetScopeResults:
        """ Sets the scope for periodic control to evaluate.

        Periodic Control uses scope to evaluate entities for which periodic surface recovery must be carried out.

        Parameters
        ----------
        scope : ScopeDefinition
            ScopeDefinition to scope entities for periodic surface recovery.

        Returns
        -------
        SetScopeResults
            Returns the SetScopeResults.


        Examples
        --------
        >>> surface_scope = prime.ScopeDefinition(model=model,
        >>>                     entity_type=prime.ScopeEntity.FACEZONELETS,
        >>>                     evaluation_type=prime.ScopeEvaluationType.LABELS,
        >>>                     label_expression="periodic-1")
        >>> periodic_control.set_scope(surface_scope)

        """
        if not isinstance(scope, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::PeriodicControl/SetScope"
        self._model._print_logs_before_command("set_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def get_summary(self, params : PeriodicControlSummaryParams) -> PeriodicControlSummaryResult:
        """ Get the periodic control summary along with the evaluated scope for the provided parameters.


        Parameters
        ----------
        params : PeriodicControlSummaryParams
            Periodic control summary parameters.

        Returns
        -------
        PeriodicControlSummaryResult
            Return the PeriodicControlSummaryResult.

        Examples
        --------
        >>> results = periodic_control.get_summary(prime.PeriodicControlSummaryParams(model=model))

        """
        if not isinstance(params, PeriodicControlSummaryParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is PeriodicControlSummaryParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::PeriodicControl/GetSummary"
        self._model._print_logs_before_command("get_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_summary", PeriodicControlSummaryResult(model = self._model, json_data = result))
        return PeriodicControlSummaryResult(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of PeriodicControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of PeriodicControl."""
        return self._name
