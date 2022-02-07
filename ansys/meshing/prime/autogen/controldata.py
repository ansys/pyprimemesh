""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class ControlData(CoreObject):
    """ControlData acts as a container for all controls (size controls, prism controls, wrapper controls, etc).

    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize ControlData """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def create_size_control(self, type : SizingType) -> List[Any]:
        """ Creates size control for the given sizing type.


        Parameters
        ----------
        type : SizingType
            Sizing type used to create a size control.

        Returns
        -------
        SizeControl *
            Returns the size control.

        Notes
        -----
        An empty size control is created on calling this API.

        Examples
        --------
        >>> size_control = model.control_data.create_size_control(SizingType.Curvature)

        """
        args = {"type" : type}
        command_name = "PrimeMesh::ControlData/CreateSizeControl"
        self._model._print_logs_before_command("create_size_control", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_size_control")
        return result

    def delete_control(self, id : int):
        """ Deletes the control for the given id.


        Parameters
        ----------
        id : int
            Id of a control.

        Examples
        --------
        >>> model.control_data.delete_control(size_control.id)

        """
        args = {"id" : id}
        command_name = "PrimeMesh::ControlData/DeleteControl"
        self._model._print_logs_before_command("delete_control", args)
        self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_control")

    def get_scope_face_zonelets(self, scope : ScopeDefinition, params : ScopeZoneletParams) -> List[int]:
        """ Gets the face zonelet ids for the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition to evaluate entities.
        params : ScopeZoneletParams
            Parameters to scope zonelets.

        Returns
        -------
        List[int]
            Returns the ids of face zonelets.

        Examples
        --------
        >>> face_zonelets = model.control_data.get_scope_face_zonelets(
        >>>                 prime.ScopeDefinition(model = model,
        >>>                 entity_type = prime.ScopeEntity.FACEZONELETS,
        >>>                 part_expression = "*"),
        >>>                 prime.ScopeZoneletParams(model =model))

        """
        args = {"scope" : scope._jsonify(),
        "params" : params._jsonify()}
        command_name = "PrimeMesh::ControlData/GetScopeFaceZonelets"
        self._model._print_logs_before_command("get_scope_face_zonelets", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope_face_zonelets")
        return result

    def get_scope_parts(self, scope : ScopeDefinition) -> List[int]:
        """ Gets the part ids for the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition to evaluate the part ids.

        Returns
        -------
        List[int]
            Returns the ids of parts.

        Examples
        --------
        >>> part_ids = model.control_data.get_scope_parts(
        >>>                 prime.ScopeDefinition(model = model,
        >>>                 part_expression = "*"),
        >>>                 prime.ScopeZoneletParams(model =model))

        """
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ControlData/GetScopeParts"
        self._model._print_logs_before_command("get_scope_parts", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope_parts")
        return result

    @property
    def id(self):
        """ Get the id of ControlData."""
        return self._id

    @property
    def name(self):
        """ Get the name of ControlData."""
        return self._name

    @name.setter
    def name(self, name):
        """ Set the name of ControlData. """
        self._name = name
