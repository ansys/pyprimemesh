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

class PrismControl(CoreObject):
    """PrismControl allows you to generate prisms.

    PrismControl allows you to control generation of prisms. Controls include setting the face scope, volume scope and growth parameters.

    Parameters
    ----------
    model : Model
        Server model to create PrismControl object.
    id : int
        Id of the PrismControl.
    object_id : int
        Object id of the PrismControl.
    name : str
        Name of the PrismControl.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize PrismControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def set_growth_params(self, prism_control_growth_params : PrismControlGrowthParams):
        """ Set growth parameters for prism control.


        Parameters
        ----------
        prism_control_growth_params : PrismControlGrowthParams
            Parameters to set prism control growth.

        Examples
        --------
        >>> results = prism_control.set_growth_params(PrismControlGrowthParams(model=model))

        """
        if not isinstance(prism_control_growth_params, PrismControlGrowthParams):
            raise TypeError("Invalid argument type passed for 'prism_control_growth_params'. Valid argument type is PrismControlGrowthParams.")
        args = {"prism_control_growth_params" : prism_control_growth_params._jsonify()}
        command_name = "PrimeMesh::PrismControl/SetGrowthParams"
        self._model._print_logs_before_command("set_growth_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_growth_params")

    def set_surface_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the surface control scope.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Examples
        --------
        >>> results = prism_control.set_surface_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::PrismControl/SetSurfaceScope"
        self._model._print_logs_before_command("set_surface_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_surface_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def set_volume_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the volume control scope.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Examples
        --------
        >>> results = prism_control.set_volume_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::PrismControl/SetVolumeScope"
        self._model._print_logs_before_command("set_volume_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_volume_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def get_surface_scope(self) -> ScopeDefinition:
        """ Gets the surface control scope.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Examples
        --------
        >>> scope = prism_control.get_surface_scope()

        """
        args = {}
        command_name = "PrimeMesh::PrismControl/GetSurfaceScope"
        self._model._print_logs_before_command("get_surface_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_surface_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_volume_scope(self) -> ScopeDefinition:
        """ Gets the volume control scope.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Examples
        --------
        >>> scope = prism_control.get_volume_scope()

        """
        args = {}
        command_name = "PrimeMesh::PrismControl/GetVolumeScope"
        self._model._print_logs_before_command("get_volume_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_growth_params(self) -> PrismControlGrowthParams:
        """ Gets the prism parameters for prism control.


        Returns
        -------
        PrismControlGrowthParams
            Returns the PrismControlGrowthParams.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> params = prism_ctrl.get_growth_params()

        """
        args = {}
        command_name = "PrimeMesh::PrismControl/GetGrowthParams"
        self._model._print_beta_api_warning("get_growth_params")
        self._model._print_logs_before_command("get_growth_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_growth_params", PrismControlGrowthParams(model = self._model, json_data = result))
        return PrismControlGrowthParams(model = self._model, json_data = result)

    def set_suggested_name(self, name : str) -> SetNameResults:
        """ Sets the unique name for the prism control based on the suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the prism control.

        Returns
        -------
        SetNameResults
            Returns the SetNameResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> prism_control.set_suggested_name("control1")

        """
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"name" : name}
        command_name = "PrimeMesh::PrismControl/SetSuggestedName"
        self._model._print_beta_api_warning("set_suggested_name")
        self._model._print_logs_before_command("set_suggested_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_name", SetNameResults(model = self._model, json_data = result))
        return SetNameResults(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of PrismControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of PrismControl."""
        return self._name
