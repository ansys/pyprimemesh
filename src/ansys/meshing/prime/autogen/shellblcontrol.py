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

class ShellBLControl(CoreObject):
    """ShellBLControl allows you to generate quad mesh on face zonelets.

    ShellBLControl allows you to control generation of quad mesh on face zonelets. Controls include setting the edge scope, face scope and growth parameters.

    Parameters
    ----------
    model : Model
        Server model to create ShellBLControl object.
    id : int
        Id of the ShellBLControl.
    object_id : int
        Object id of the ShellBLControl.
    name : str
        Name of the ShellBLControl.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize ShellBLControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def get_growth_params(self) -> ShellBLControlGrowthParams:
        """ Gets thin ShellBL parameters for ShellBL control.


        Returns
        -------
        ShellBLControlGrowthParams
            Returns the ShellBLControlGrowthParams.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> params = shellBL_ctrl.get_growth_params()

        """
        args = {}
        command_name = "PrimeMesh::ShellBLControl/GetGrowthParams"
        self._model._print_beta_api_warning("get_growth_params")
        self._model._print_logs_before_command("get_growth_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_growth_params", ShellBLControlGrowthParams(model = self._model, json_data = result))
        return ShellBLControlGrowthParams(model = self._model, json_data = result)

    def set_growth_params(self, params : ShellBLControlGrowthParams):
        """ Sets growth parameters for ShellBL control.


        Parameters
        ----------
        params : ShellBLControlGrowthParams
            Parameters to set ShellBL growth.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = shellbl_control.set_growth_params(ShellBLControlGrowthParams(model=model))

        """
        if not isinstance(params, ShellBLControlGrowthParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ShellBLControlGrowthParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::ShellBLControl/SetGrowthParams"
        self._model._print_beta_api_warning("set_growth_params")
        self._model._print_logs_before_command("set_growth_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_growth_params")

    def set_edge_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the edge scope.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = shellbl_control.set_edge_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::ShellBLControl/SetEdgeScope"
        self._model._print_beta_api_warning("set_edge_scope")
        self._model._print_logs_before_command("set_edge_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_edge_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def set_surface_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the face zonelet scope.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = shellbl_control.set_surface_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::ShellBLControl/SetSurfaceScope"
        self._model._print_beta_api_warning("set_surface_scope")
        self._model._print_logs_before_command("set_surface_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_surface_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def get_edge_scope(self) -> ScopeDefinition:
        """ Gets the edge scope.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> scope = shellbl_control.get_edge_scope()

        """
        args = {}
        command_name = "PrimeMesh::ShellBLControl/GetEdgeScope"
        self._model._print_beta_api_warning("get_edge_scope")
        self._model._print_logs_before_command("get_edge_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_surface_scope(self) -> ScopeDefinition:
        """ Gets the surface scope.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> scope = shellbl_control.get_surface_scope()

        """
        args = {}
        command_name = "PrimeMesh::ShellBLControl/GetSurfaceScope"
        self._model._print_beta_api_warning("get_surface_scope")
        self._model._print_logs_before_command("get_surface_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_surface_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of ShellBLControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of ShellBLControl."""
        return self._name
