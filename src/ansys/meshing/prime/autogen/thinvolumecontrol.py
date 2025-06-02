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

class ThinVolumeControl(CoreObject):
    """ThinVolumeControl allows you to generate prisms in the space between surfaces.

    ThinVolumeControl allows you to control generation of prisms in the thin space between surfaces. Controls include setting the source face scope, target face scope and thin volume mesh parameters.

    Parameters
    ----------
    model : Model
        Server model to create ThinVolumeControl object.
    id : int
        Id of the ThinVolumeControl.
    object_id : int
        Object id of the ThinVolumeControl.
    name : str
        Name of the ThinVolumeControl.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize ThinVolumeControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def set_thin_volume_mesh_params(self, thin_volume_mesh_params : ThinVolumeMeshParams):
        """ Sets thin volume mesh parameters for thin volume control.


        Parameters
        ----------
        thin_volume_mesh_params : ThinVolumeMeshParams
            Parameters to set thin volume control growth.

        Examples
        --------
        >>> results = thin_vol_ctrl.set_thin_volume_mesh_params(ThinVolumeMeshParams(model=model))

        """
        if not isinstance(thin_volume_mesh_params, ThinVolumeMeshParams):
            raise TypeError("Invalid argument type passed for 'thin_volume_mesh_params'. Valid argument type is ThinVolumeMeshParams.")
        args = {"thin_volume_mesh_params" : thin_volume_mesh_params._jsonify()}
        command_name = "PrimeMesh::ThinVolumeControl/SetThinVolumeMeshParams"
        self._model._print_logs_before_command("set_thin_volume_mesh_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_thin_volume_mesh_params")

    def set_source_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the source surface scope of thin volume control.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition source face entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Examples
        --------
        >>> results = thin_vol_ctrl.set_source_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::ThinVolumeControl/SetSourceScope"
        self._model._print_logs_before_command("set_source_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_source_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def set_target_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the target surface scope of thin volume control.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition for target face entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Examples
        --------
        >>> results = thin_vol_ctrl.set_target_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::ThinVolumeControl/SetTargetScope"
        self._model._print_logs_before_command("set_target_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_target_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def set_volume_scope(self, entities : ScopeDefinition) -> SetScopeResults:
        """ Sets the volume scope of thin volume control.


        Parameters
        ----------
        entities : ScopeDefinition
            Scope definition for volume entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = thin_vol_ctrl.set_volume_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'entities'. Valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::ThinVolumeControl/SetVolumeScope"
        self._model._print_beta_api_warning("set_volume_scope")
        self._model._print_logs_before_command("set_volume_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_volume_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def get_source_scope(self) -> ScopeDefinition:
        """ Gets the source of thin volume control scope.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> scope = thin_vol_ctrl.get_source_scope()

        """
        args = {}
        command_name = "PrimeMesh::ThinVolumeControl/GetSourceScope"
        self._model._print_beta_api_warning("get_source_scope")
        self._model._print_logs_before_command("get_source_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_source_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_target_scope(self) -> ScopeDefinition:
        """ Gets the target of thin volume control scope.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> scope = thin_vol_ctrl.get_target_scope()

        """
        args = {}
        command_name = "PrimeMesh::ThinVolumeControl/GetTargetScope"
        self._model._print_beta_api_warning("get_target_scope")
        self._model._print_logs_before_command("get_target_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_target_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_volume_scope(self) -> ScopeDefinition:
        """ Gets the volume scope of thin volume control.


        Returns
        -------
        ScopeDefinition
            Returns the ScopeDefinition.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> scope = thin_vol_ctrl.get_volume_scope()

        """
        args = {}
        command_name = "PrimeMesh::ThinVolumeControl/GetVolumeScope"
        self._model._print_beta_api_warning("get_volume_scope")
        self._model._print_logs_before_command("get_volume_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of ThinVolumeControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of ThinVolumeControl."""
        return self._name
