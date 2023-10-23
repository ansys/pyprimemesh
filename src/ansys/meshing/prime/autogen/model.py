""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

import logging
from ansys.meshing.prime.internals import utils

class Model(CoreObject, CommunicationManager):
    """Model is the nucleus of Prime. Model forms the base and contains all the information about Prime.

    You can access any information in Prime only through Model.
    Model allows you to query TopoData, ControlData, Parts, SizeFields and more.
    """

    def __init__(self, comm, id: int, object_id: int, name: str):
        """ Initialize Model """
        self._comm = comm
        self._logger = logging.getLogger("PyPrimeMesh")
        self._id = id
        self._object_id = object_id
        self._name = name

    def _print_logs_before_command(self, command, args):
        utils.print_logs_before_command(self._logger, command, args)

    def _print_logs_after_command(self, command, args = None):
        utils.print_logs_after_command(self._logger, command, args)

    def _print_beta_api_warning(self, command):
        utils.print_beta_api_warning(self._logger, command)

    def delete_parts(self, part_ids : Iterable[int]) -> DeleteResults:
        """ Delete the parts and its entities.


        Parameters
        ----------
        part_ids : Iterable[int]
            Ids of parts to be deleted.

        Returns
        -------
        DeleteResults
            Return the DeleteResults.


        Examples
        --------
        >>> results = model.delete_parts(part_ids)

        """
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for part_ids, valid argument type is Iterable[int].")
        args = {"part_ids" : part_ids}
        command_name = "PrimeMesh::Model/DeleteParts"
        self._print_logs_before_command("delete_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("delete_parts", DeleteResults(model = self, json_data = result))
        return DeleteResults(model = self, json_data = result)

    def merge_parts(self, part_ids : Iterable[int], params : MergePartsParams) -> MergePartsResults:
        """ Merges given parts into one.


        Parameters
        ----------
        part_ids : Iterable[int]
            Ids of parts to be merged.
        params : MergePartsParams
            Parameters to merge parts.

        Returns
        -------
        MergePartsResults
            Returns the MergePartsResults.


        Examples
        --------
        >>> params = prime.MergePartsParams(model = model)
        >>> results = model.merge_parts(part_ids, params)

        """
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for part_ids, valid argument type is Iterable[int].")
        if not isinstance(params, MergePartsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is MergePartsParams.")
        args = {"part_ids" : part_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Model/MergeParts"
        self._print_logs_before_command("merge_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("merge_parts", MergePartsResults(model = self, json_data = result))
        return MergePartsResults(model = self, json_data = result)

    def set_global_sizing_params(self, params : GlobalSizingParams) -> SetSizingResults:
        """ Sets the global sizing parameters to initialize surfer parameters and various size control parameters.


        Parameters
        ----------
        params : GlobalSizingParams
            Global sizing parameters.

        Examples
        --------
        >>> model = client.model
        >>> model.set_global_sizing_params(
        >>>           prime.GlobalSizingParams(model=model,
        >>>           min = 0.1, max = 1.0, growth_rate = 1.2))

        """
        if not isinstance(params, GlobalSizingParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is GlobalSizingParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Model/SetGlobalSizingParams"
        self._print_logs_before_command("set_global_sizing_params", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_global_sizing_params", SetSizingResults(model = self, json_data = result))
        return SetSizingResults(model = self, json_data = result)

    def get_active_volumetric_size_fields(self) -> Iterable[int]:
        """ Get the active sizefield ids.


        Returns
        -------
        Iterable[int]
            Return the list of active sizefield ids.


        Examples
        --------
        >>> model = client.model
        >>> active_size_field_ids = model.get_active_volumetric_size_fields()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetActiveVolumetricSizeFields"
        self._print_logs_before_command("get_active_volumetric_size_fields", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_active_volumetric_size_fields")
        return result

    def get_volumetric_size_fields(self) -> Iterable[int]:
        """ Get the sizefield ids.


        Returns
        -------
        Iterable[int]
            Return the list of sizefield ids.


        Examples
        --------
        >>> model = client.model
        >>> size_field_ids = model.get_volumetric_size_fields()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetVolumetricSizeFields"
        self._print_logs_before_command("get_volumetric_size_fields", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_volumetric_size_fields")
        return result

    def activate_volumetric_size_fields(self, size_field_ids : Iterable[int]):
        """ Activate the sizefields identified by the given sizefield ids.


        Parameters
        ----------
        size_field_ids : Iterable[int]
            List of sizefield ids.

        Examples
        --------
        >>> model = client.model
        >>> model.activate_volumetric_size_fields(size_field_ids)

        """
        if not isinstance(size_field_ids, Iterable):
            raise TypeError("Invalid argument type passed for size_field_ids, valid argument type is Iterable[int].")
        args = {"size_field_ids" : size_field_ids}
        command_name = "PrimeMesh::Model/ActivateVolumetricSizeFields"
        self._print_logs_before_command("activate_volumetric_size_fields", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("activate_volumetric_size_fields")

    def deactivate_volumetric_size_fields(self, size_field_ids : Iterable[int]):
        """ Deactivate the sizefields identified by the given sizefield ids.


        Parameters
        ----------
        size_field_ids : Iterable[int]
            List of sizefield ids.

        Examples
        --------
        >>> model = client.model
        >>> model.deactivate_volumetric_size_fields(size_field_ids)

        """
        if not isinstance(size_field_ids, Iterable):
            raise TypeError("Invalid argument type passed for size_field_ids, valid argument type is Iterable[int].")
        args = {"size_field_ids" : size_field_ids}
        command_name = "PrimeMesh::Model/DeactivateVolumetricSizeFields"
        self._print_logs_before_command("deactivate_volumetric_size_fields", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("deactivate_volumetric_size_fields")

    def delete_volumetric_size_fields(self, size_field_ids : Iterable[int]):
        """ Delete the sizefields identified by the given sizefield ids.


        Parameters
        ----------
        size_field_ids : Iterable[int]
            List of sizefield ids.

        Examples
        --------
        >>> model = client.model
        >>> model.delete_volumetric_size_fields(size_field_ids)

        """
        if not isinstance(size_field_ids, Iterable):
            raise TypeError("Invalid argument type passed for size_field_ids, valid argument type is Iterable[int].")
        args = {"size_field_ids" : size_field_ids}
        command_name = "PrimeMesh::Model/DeleteVolumetricSizeFields"
        self._print_logs_before_command("delete_volumetric_size_fields", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("delete_volumetric_size_fields")

    def set_num_threads(self, num : int):
        """ Sets the number of threads for multithreaded operation.


        Parameters
        ----------
        num : int
            Number of threads.

        Examples
        --------
        >>> model = client.model
        >>> model.set_num_threads(4)

        """
        if not isinstance(num, int):
            raise TypeError("Invalid argument type passed for num, valid argument type is int.")
        args = {"num" : num}
        command_name = "PrimeMesh::Model/SetNumThreads"
        self._print_logs_before_command("set_num_threads", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_num_threads")

    def get_num_threads(self) -> int:
        """ Get the number of threads enabled for multithreaded operation.


        Returns
        -------
        int
            Returns the number of threads.


        Examples
        --------
        >>> model = client.model
        >>> num_threads = model.get_num_threads()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetNumThreads"
        self._print_logs_before_command("get_num_threads", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_num_threads")
        return result

    def start_distributed_meshing(self):
        """ Enables distributed meshing mode.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> model.start_distributed_meshing()

        """
        args = {}
        command_name = "PrimeMesh::Model/StartDistributedMeshing"
        self._print_logs_before_command("start_distributed_meshing", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("start_distributed_meshing")

    def create_zone(self, suggested_name : str, type : ZoneType) -> CreateZoneResults:
        """ Creates zone for the given zone type.


        Parameters
        ----------
        suggested_name : str
            Suggested name for the zone to be created.
        type : ZoneType
            Type of the zone to be created.

        Returns
        -------
        CreateZoneResults
            Returns the CreateZoneResults.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> results = model.create_zone("wall", prime.ZoneType.FACE)

        """
        if not isinstance(suggested_name, str):
            raise TypeError("Invalid argument type passed for suggested_name, valid argument type is str.")
        if not isinstance(type, ZoneType):
            raise TypeError("Invalid argument type passed for type, valid argument type is ZoneType.")
        args = {"suggested_name" : suggested_name,
        "type" : type}
        command_name = "PrimeMesh::Model/CreateZone"
        self._print_logs_before_command("create_zone", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("create_zone", CreateZoneResults(model = self, json_data = result))
        return CreateZoneResults(model = self, json_data = result)

    def delete_zone(self, zone_id : int) -> DeleteZoneResults:
        """ Deletes zone identified with the given id.


        Parameters
        ----------
        zone_id : int
            Id of the zone to be deleted.

        Returns
        -------
        DeleteZoneResults
            Returns the DeleteZoneResults.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> results = model.delete_zone(1)

        """
        if not isinstance(zone_id, int):
            raise TypeError("Invalid argument type passed for zone_id, valid argument type is int.")
        args = {"zone_id" : zone_id}
        command_name = "PrimeMesh::Model/DeleteZone"
        self._print_logs_before_command("delete_zone", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("delete_zone", DeleteZoneResults(model = self, json_data = result))
        return DeleteZoneResults(model = self, json_data = result)

    def get_zone_by_name(self, zone_name : str) -> int:
        """ Gets the zone by name.


        Parameters
        ----------
        zone_name : str
            Name of the zone.

        Returns
        -------
        int
            Returns id of the zone.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> zone_id = model.get_zone_by_name("inlet")

        """
        if not isinstance(zone_name, str):
            raise TypeError("Invalid argument type passed for zone_name, valid argument type is str.")
        args = {"zone_name" : zone_name}
        command_name = "PrimeMesh::Model/GetZoneByName"
        self._print_logs_before_command("get_zone_by_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_zone_by_name")
        return result

    def get_zone_name(self, id : int) -> str:
        """ Get the name of given zone.


        Parameters
        ----------
        id : int
            Id of zone.

        Returns
        -------
        str
            Return the name. Return empty name if the id is invalid.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> name = model.get_zone_name(id)

        """
        if not isinstance(id, int):
            raise TypeError("Invalid argument type passed for id, valid argument type is int.")
        args = {"id" : id}
        command_name = "PrimeMesh::Model/GetZoneName"
        self._print_logs_before_command("get_zone_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_zone_name")
        return result

    def set_suggested_zone_name(self, id : int, name : str) -> SetNameResults:
        """ Sets the unique name for zone with given id based on the given suggested name.


        Parameters
        ----------
        id : int
            Id of the zone to set suggested name.
        name : str
            Suggested name for the zone.

        Returns
        -------
        SetNameResults
            Returns the SetNameResults. results.assignedName indicates the assigned name to the zone.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> results = model.set_suggested_zone_name(id = 5, name = "zone1")

        """
        if not isinstance(id, int):
            raise TypeError("Invalid argument type passed for id, valid argument type is int.")
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for name, valid argument type is str.")
        args = {"id" : id,
        "name" : name}
        command_name = "PrimeMesh::Model/SetSuggestedZoneName"
        self._print_logs_before_command("set_suggested_zone_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_suggested_zone_name", SetNameResults(model = self, json_data = result))
        return SetNameResults(model = self, json_data = result)

    @property
    def id(self):
        """ Get the id of Model."""
        return self._id

    @property
    def name(self):
        """ Get the name of Model."""
        return self._name
