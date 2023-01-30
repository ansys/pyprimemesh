""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class ControlData(CoreObject):
    """ControlData has all controls like size controls, prism controls, wrapper controls and more.

    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize ControlData """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def create_wrapper_control(self) -> List[Any]:
        """ Creates wrapper control with defaults.


        Returns
        -------
        WrapperControl
            Returns the wrapper control.

        Notes
        -----
        A wrapper control with defaults is created on calling this API.

        Examples
        --------
        >>> wrapper_control = model.control_data.create_wrapper_control()

        """
        args = {}
        command_name = "PrimeMesh::ControlData/CreateWrapperControl"
        self._model._print_logs_before_command("create_wrapper_control", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_wrapper_control")
        return result

    def create_size_control(self, type : SizingType) -> List[Any]:
        """ Creates size control for the given sizing type.


        Parameters
        ----------
        type : SizingType
            Sizing type used to create a size control.

        Returns
        -------
        SizeControl
            Returns the size control.

        Notes
        -----
        An empty size control is created on calling this API.

        Examples
        --------
        >>> size_control = model.control_data.create_size_control(SizingType.CURVATURE)

        """
        args = {"type" : type}
        command_name = "PrimeMesh::ControlData/CreateSizeControl"
        self._model._print_logs_before_command("create_size_control", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_size_control")
        return result

    def create_prism_control(self) -> List[Any]:
        """ Creates the PrismControl.


        Returns
        -------
        PrismControl
            Returns the PrismControl.


        Examples
        --------
        >>> prism_control = model.control_data.create_prism_control()

        """
        args = {}
        command_name = "PrimeMesh::ControlData/CreatePrismControl"
        self._model._print_logs_before_command("create_prism_control", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_prism_control")
        return result

    def create_volume_control(self) -> List[Any]:
        """ Creates the volume control.


        Returns
        -------
        VolumeControl
            Returns the volume control.

        Examples
        --------
        >>> volume_control = model.control_data.create_volume_control()

        """
        args = {}
        command_name = "PrimeMesh::ControlData/CreateVolumeControl"
        self._model._print_logs_before_command("create_volume_control", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_volume_control")
        return result

    def create_periodic_control(self) -> List[Any]:
        """ Creates the periodic control.


        Returns
        -------
        PeriodicControl
            Returns the periodic control.

        Examples
        --------
        >>> periodic_control = model.control_data.create_periodic_control()

        """
        args = {}
        command_name = "PrimeMesh::ControlData/CreatePeriodicControl"
        self._model._print_logs_before_command("create_periodic_control", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_periodic_control")
        return result

    def delete_controls(self, control_ids : Iterable[int]) -> DeleteResults:
        """ Delete the controls of the given ids.


        Parameters
        ----------
        control_ids : Iterable[int]
            Ids of controls to be deleted.

        Returns
        -------
        DeleteResults
            Returns the DeleteResults.

        Examples
        --------
        >>> results = model.control_data.delete_controls([size_control.id, volume_control.id])

        """
        args = {"control_ids" : control_ids}
        command_name = "PrimeMesh::ControlData/DeleteControls"
        self._model._print_logs_before_command("delete_controls", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_controls", DeleteResults(model = self._model, json_data = result))
        return DeleteResults(model = self._model, json_data = result)

    def get_scope_face_zonelets(self, scope : ScopeDefinition, params : ScopeZoneletParams) -> Iterable[int]:
        """ Get the face zonelet ids for the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition to evaluate entities.
        params : ScopeZoneletParams
            Parameters to scope zonelets.

        Returns
        -------
        Iterable[int]
            Return the ids of face zonelets.

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
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope_face_zonelets")
        return result

    def get_scope_parts(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Get the part ids for the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition to evaluate the part ids.

        Returns
        -------
        Iterable[int]
            Return the ids of parts.

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
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope_parts")
        return result

    def get_part_zonelets(self, scope : ScopeDefinition) -> List[PartZonelets]:
        """ Creates an array of part zonelet structure using the input ScopeDefinition.


        Parameters
        ----------
        scope : ScopeDefinition
            Input ScopeDefinition.

        Returns
        -------
        List[PartZonelets]
            Returns a list of PartZonelets.


        Examples
        --------
        >>> results = control_data.get_part_zonelets(scope)

        """
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ControlData/GetPartZonelets"
        self._model._print_logs_before_command("get_part_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_zonelets", [PartZonelets(model = self._model, json_data = data) for data in result])
        return [PartZonelets(model = self._model, json_data = data) for data in result]

    @property
    def id(self):
        """ Get the id of ControlData."""
        return self._id

    @property
    def name(self):
        """ Get the name of ControlData."""
        return self._name
