""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class ThinVolumeControl(CoreObject):
    """ThinVolumeControl allows you to generate prisms in the space between surfaces.

    ThinVolumeControl allows you to control generation of prisms in the thin space between surfaces. Controls include setting the source face scope, target face scope and thin volume mesh parameters.
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
            raise TypeError("Invalid argument type passed for thin_volume_mesh_params, valid argument type is ThinVolumeMeshParams.")
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
            Scope definition entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Examples
        --------
        >>> results = thin_vol_ctrl.set_source_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for entities, valid argument type is ScopeDefinition.")
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
            Scope definition entities.

        Returns
        -------
        SetScopeResults
            Returns SetScopeResults.


        Examples
        --------
        >>> results = thin_vol_ctrl.set_target_scope(entities)

        """
        if not isinstance(entities, ScopeDefinition):
            raise TypeError("Invalid argument type passed for entities, valid argument type is ScopeDefinition.")
        args = {"entities" : entities._jsonify()}
        command_name = "PrimeMesh::ThinVolumeControl/SetTargetScope"
        self._model._print_logs_before_command("set_target_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_target_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of ThinVolumeControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of ThinVolumeControl."""
        return self._name
