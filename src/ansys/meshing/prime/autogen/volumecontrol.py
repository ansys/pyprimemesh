""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class VolumeControl(CoreObject):
    """Volume controls provide volume specific settings on volumes specified by scope and settings specified by parameters.

    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize VolumeControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def set_params(self, volume_control_params : VolumeControlParams):
        """ Sets the volume control parameters.


        Parameters
        ----------
        volume_control_params : VolumeControlParams
            Parameters to control volume.

        Examples
        --------
        >>> volume_control.set_params(
        >>>                  prime.VolumeControlParams(model=model,
        >>>                  cell_zonelet_type = prime.CellZoneletType.FLUID))

        """
        args = {"volume_control_params" : volume_control_params._jsonify()}
        command_name = "PrimeMesh::VolumeControl/SetParams"
        self._model._print_logs_before_command("set_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_params")

    def set_scope(self, scope : ScopeDefinition) -> SetScopeResults:
        """ Sets the scope for volume control to evaluate.

        Volume control uses scope to evaluate entities for which volume mesh needs to be generated.

        Parameters
        ----------
        scope : ScopeDefinition
            ScopeDefinition to scope entities for volume mesh generation.

        Returns
        -------
        SetScopeResults
            Returns a SetScopeResults.


        Examples
        --------
        >>> volume_control.set_scope(prime.ScopeDefinition(model=model,
        >>>                        entity_type = ScopeEntity.VOLUMES,
        >>>                        evaluation_type = ScopeEvaluationType.ZONES,
        >>>                        zone_expression = "vol_in"))

        """
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::VolumeControl/SetScope"
        self._model._print_logs_before_command("set_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def set_suggested_name(self, name : str) -> SetNameResults:
        """ Sets the unique name for the volume control based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the volume control.

        Returns
        -------
        SetNameResults
            Returns a name of the volume control.


        Examples
        --------
        >>> volume_control.set_suggested_name("control1")

        """
        args = {"name" : name}
        command_name = "PrimeMesh::VolumeControl/SetSuggestedName"
        self._model._print_logs_before_command("set_suggested_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_name", SetNameResults(model = self._model, json_data = result))
        return SetNameResults(model = self._model, json_data = result)

    def get_scope(self) -> ScopeDefinition:
        """ Gets the scope for the volume control.


        Returns
        -------
        ScopeDefinition
            Returns scope of the volume control.


        Examples
        --------
        >>> scope_definition = volume_control.get_scope()

        """
        args = {}
        command_name = "PrimeMesh::VolumeControl/GetScope"
        self._model._print_logs_before_command("get_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_params(self) -> VolumeControlParams:
        """ Get the parameters of the volume control.


        Returns
        -------
        VolumeControlParams
            Return parameters of the volume control.


        Examples
        --------
        >>> params = volume_control.get_params()

        """
        args = {}
        command_name = "PrimeMesh::VolumeControl/GetParams"
        self._model._print_logs_before_command("get_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_params", VolumeControlParams(model = self._model, json_data = result))
        return VolumeControlParams(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of VolumeControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of VolumeControl."""
        return self._name
