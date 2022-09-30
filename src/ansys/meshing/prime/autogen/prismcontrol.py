""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class PrismControl(CoreObject):
    """PrismControl allows you to generate prisms.

    PrismControl allows you to control generation of prisms. Controls include setting the face scope, volume scope and growth parameters.
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

    @property
    def id(self):
        """ Get the id of PrismControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of PrismControl."""
        return self._name
