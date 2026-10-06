# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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
from ansys.meshing.prime.autogen.coreobject import *
from ansys.meshing import prime
from typing import Dict, Any, Union, List, Iterable

import logging
from ansys.meshing.prime.internals import utils

class Model(CoreObject, CommunicationManager):
    """Model is the nucleus of Prime. Model forms the base and contains all the information about Prime.

    You can access any information in Prime only through Model.
    Model allows you to query TopoData, ControlData, Parts, SizeFields and more.


    Parameters
    ----------
    comm : Communicator
        Communicator to connect with the Ansys Prime server.
    id : int
        Id of the Model.
    object_id : int
        Object id of the Model.
    name : str
        Name of the Model.
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

    def create_part(self, suggested_name : str) -> List[Any]:
        """ Creates a part with the given name.


        Parameters
        ----------
        suggested_name : str
            Name of the part.

        Returns
        -------
        Part
            Returns a part with the given name.


        Examples
        --------
        >>> new_part = model.create_part('part_name')

        """
        if not isinstance(suggested_name, str):
            raise TypeError("Invalid argument type passed for 'suggested_name'. Valid argument type is str.")
        args = {"suggested_name" : suggested_name}
        command_name = "PrimeMesh::Model/CreatePart"
        self._print_logs_before_command("create_part", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("create_part")
        return result

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
            raise TypeError("Invalid argument type passed for 'part_ids'. Valid argument type is Iterable[int].")
        args = {"part_ids" : part_ids}
        command_name = "PrimeMesh::Model/DeleteParts"
        self._print_logs_before_command("delete_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("delete_parts", prime.DeleteResults(model = self, json_data = result))
        return prime.DeleteResults(model = self, json_data = result)

    def get_part(self, id : int) -> List[Any]:
        """ Gets the part by id.


        Parameters
        ----------
        id : int
            Id of the part to be accessed.

        Returns
        -------
        Part
            Returns the part with the given id.


        Examples
        --------
        >>> part = model.get_part(part_id)

        """
        if not isinstance(id, int):
            raise TypeError("Invalid argument type passed for 'id'. Valid argument type is int.")
        args = {"id" : id}
        command_name = "PrimeMesh::Model/GetPart"
        self._print_logs_before_command("get_part", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_part")
        return result

    def get_part_by_name(self, name : str) -> List[Any]:
        """ Gets the part by name.


        Parameters
        ----------
        name : str
            Name of the part to be accessed.

        Returns
        -------
        Part
            Returns the part with the given name.


        Examples
        --------
        >>> part = model.get_part_by_name("part_name")

        """
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"name" : name}
        command_name = "PrimeMesh::Model/GetPartByName"
        self._print_logs_before_command("get_part_by_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_part_by_name")
        return result

    def merge_parts(self, part_ids : Iterable[int], params : MergePartsParams) -> MergePartsResults:
        """ Merge given parts into one.


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
*

        Examples
        --------
        >>> params = prime.MergePartsParams(model = model)
        >>> results = model.merge_parts(part_ids, params)

        """
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'part_ids'. Valid argument type is Iterable[int].")
        if type(params).__name__ != 'MergePartsParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MergePartsParams.")
        args = {"part_ids" : part_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Model/MergeParts"
        self._print_logs_before_command("merge_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("merge_parts", prime.MergePartsResults(model = self, json_data = result))
        return prime.MergePartsResults(model = self, json_data = result)

    def get_global_sizing_params(self) -> GlobalSizingParams:
        """ Gets the global size field parameters.


        Returns
        -------
        GlobalSizingParams
            Returns the global size field parameters.


        Examples
        --------
        >>> params = model.get_global_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetGlobalSizingParams"
        self._print_logs_before_command("get_global_sizing_params", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_global_sizing_params", prime.GlobalSizingParams(model = self, json_data = result))
        return prime.GlobalSizingParams(model = self, json_data = result)

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
        if type(params).__name__ != 'GlobalSizingParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is GlobalSizingParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Model/SetGlobalSizingParams"
        self._print_logs_before_command("set_global_sizing_params", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_global_sizing_params", prime.SetSizingResults(model = self, json_data = result))
        return prime.SetSizingResults(model = self, json_data = result)

    def set_verbosity_level(self, verbosity : int):
        """ Sets the verbosity level used for model logging.


        Parameters
        ----------
        verbosity : int
            Level to increase or decrease logging verbosity.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> model.set_verbosity_level(1)

        """
        if not isinstance(verbosity, int):
            raise TypeError("Invalid argument type passed for 'verbosity'. Valid argument type is int.")
        args = {"verbosity" : verbosity}
        command_name = "PrimeMesh::Model/SetVerbosityLevel"
        self._print_beta_api_warning("set_verbosity_level")
        self._print_logs_before_command("set_verbosity_level", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_verbosity_level")

    def set_log_file(self, file_name : str) -> bool:
        """ Sets the log file used for model logging.


        Parameters
        ----------
        file_name : str
            Path to the log file. Passing an empty string stops file logging.

        Returns
        -------
        bool
            Returns true when the requested logging state is applied successfully.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> model.set_log_file("C:/logs/prime_server.log")

        """
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        args = {"file_name" : file_name}
        command_name = "PrimeMesh::Model/SetLogFile"
        self._print_beta_api_warning("set_log_file")
        self._print_logs_before_command("set_log_file", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_log_file")
        return result

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
            raise TypeError("Invalid argument type passed for 'size_field_ids'. Valid argument type is Iterable[int].")
        args = {"size_field_ids" : size_field_ids}
        command_name = "PrimeMesh::Model/ActivateVolumetricSizeFields"
        self._print_logs_before_command("activate_volumetric_size_fields", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("activate_volumetric_size_fields")

    def deactivate_volumetric_size_fields(self, size_field_ids : Iterable[int]):
        """ Deactivate the size fields with the given size field ids.


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
            raise TypeError("Invalid argument type passed for 'size_field_ids'. Valid argument type is Iterable[int].")
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
            raise TypeError("Invalid argument type passed for 'size_field_ids'. Valid argument type is Iterable[int].")
        args = {"size_field_ids" : size_field_ids}
        command_name = "PrimeMesh::Model/DeleteVolumetricSizeFields"
        self._print_logs_before_command("delete_volumetric_size_fields", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("delete_volumetric_size_fields")

    def set_suggested_size_field_name(self, size_field_id : int, name : str) -> SetNameResults:
        """ Sets the suggested name of size field with the given id.


        Parameters
        ----------
        size_field_id : int
            Size field id.
        name : str
            Name of the size field.

        Returns
        -------
        SetNameResults
            Returns the SetNameResults structure having the suggested name of size field.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> model = client.model
        >>> model.set_suggested_size_field_name(size_field_id, name)

        """
        if not isinstance(size_field_id, int):
            raise TypeError("Invalid argument type passed for 'size_field_id'. Valid argument type is int.")
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"size_field_id" : size_field_id,
        "name" : name}
        command_name = "PrimeMesh::Model/SetSuggestedSizeFieldName"
        self._print_beta_api_warning("set_suggested_size_field_name")
        self._print_logs_before_command("set_suggested_size_field_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_suggested_size_field_name", prime.SetNameResults(model = self, json_data = result))
        return prime.SetNameResults(model = self, json_data = result)

    def get_size_field_name(self, size_field_id : int) -> str:
        """ Gets the name of size field with the given id.


        Parameters
        ----------
        size_field_id : int
            Size field id.

        Returns
        -------
        str
            Returns the name of the size field.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> model = client.model
        >>> model.get_size_field_name(size_field_id)

        """
        if not isinstance(size_field_id, int):
            raise TypeError("Invalid argument type passed for 'size_field_id'. Valid argument type is int.")
        args = {"size_field_id" : size_field_id}
        command_name = "PrimeMesh::Model/GetSizeFieldName"
        self._print_beta_api_warning("get_size_field_name")
        self._print_logs_before_command("get_size_field_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_size_field_name")
        return result

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
            raise TypeError("Invalid argument type passed for 'num'. Valid argument type is int.")
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

    def get_num_compute_nodes(self) -> int:
        """ Get the number of compute nodes.


        Returns
        -------
        int
            Returns the number of compute nodes.


        Examples
        --------
        >>> model = client.model
        >>> num_compute_nodes = model.get_num_compute_nodes()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetNumComputeNodes"
        self._print_logs_before_command("get_num_compute_nodes", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_num_compute_nodes")
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

    def create_zone(self, suggested_name : str, zone_type : ZoneType) -> CreateZoneResults:
        """ Creates zone for the given zone type.


        Parameters
        ----------
        suggested_name : str
            Suggested name for the zone to be created.
        zone_type : ZoneType
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
            raise TypeError("Invalid argument type passed for 'suggested_name'. Valid argument type is str.")
        if type(zone_type).__name__ != 'ZoneType':
            raise TypeError("Invalid argument type passed for 'zone_type'. Valid argument type is ZoneType.")
        args = {"suggested_name" : suggested_name,
        "zone_type" : zone_type}
        command_name = "PrimeMesh::Model/CreateZone"
        self._print_logs_before_command("create_zone", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("create_zone", prime.CreateZoneResults(model = self, json_data = result))
        return prime.CreateZoneResults(model = self, json_data = result)

    def delete_zone(self, zone_id : int) -> DeleteZoneResults:
        """ Deletes zone with the given id.


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
            raise TypeError("Invalid argument type passed for 'zone_id'. Valid argument type is int.")
        args = {"zone_id" : zone_id}
        command_name = "PrimeMesh::Model/DeleteZone"
        self._print_logs_before_command("delete_zone", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("delete_zone", prime.DeleteZoneResults(model = self, json_data = result))
        return prime.DeleteZoneResults(model = self, json_data = result)

    def get_zone_by_name(self, zone_name : str) -> int:
        """ Gets the zone with the provided name.


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
            raise TypeError("Invalid argument type passed for 'zone_name'. Valid argument type is str.")
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
            Return the zone name. Return empty name if the id is invalid.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> name = model.get_zone_name(id)

        """
        if not isinstance(id, int):
            raise TypeError("Invalid argument type passed for 'id'. Valid argument type is int.")
        args = {"id" : id}
        command_name = "PrimeMesh::Model/GetZoneName"
        self._print_logs_before_command("get_zone_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_zone_name")
        return result

    def get_edge_zone_names_of_parts(self, part_ids : Iterable[int]) -> List[str]:
        """ Gets the names of all edge zone names across the given parts.


        Parameters
        ----------
        part_ids : Iterable[int]
            List of part ids to query edge zone names from.

        Returns
        -------
        List[str]
            Returns a list of unique edge zone names from the specified parts.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> zone_names = model.get_edge_zone_names_of_parts(part_ids)

        """
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'part_ids'. Valid argument type is Iterable[int].")
        args = {"part_ids" : part_ids}
        command_name = "PrimeMesh::Model/GetEdgeZoneNamesOfParts"
        self._print_beta_api_warning("get_edge_zone_names_of_parts")
        self._print_logs_before_command("get_edge_zone_names_of_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_edge_zone_names_of_parts")
        return result

    def get_volume_zone_names_of_parts(self, part_ids : Iterable[int]) -> List[str]:
        """ Gets the names of all volume zones across the given parts.


        Parameters
        ----------
        part_ids : Iterable[int]
            List of part ids to query volume zone names from.

        Returns
        -------
        List[str]
            Returns a list of unique volume zone names from the specified parts.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> zone_names = model.get_volume_zone_names_of_parts(part_ids)

        """
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'part_ids'. Valid argument type is Iterable[int].")
        args = {"part_ids" : part_ids}
        command_name = "PrimeMesh::Model/GetVolumeZoneNamesOfParts"
        self._print_beta_api_warning("get_volume_zone_names_of_parts")
        self._print_logs_before_command("get_volume_zone_names_of_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_volume_zone_names_of_parts")
        return result

    def get_face_zone_names_of_parts(self, part_ids : Iterable[int]) -> List[str]:
        """ Gets the names of all face zones across the given parts.


        Parameters
        ----------
        part_ids : Iterable[int]
            List of part ids to query face zone names from.

        Returns
        -------
        List[str]
            Returns a list of unique face zone names from the specified parts.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> zone_names = model.get_face_zone_names_of_parts(part_ids)

        """
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'part_ids'. Valid argument type is Iterable[int].")
        args = {"part_ids" : part_ids}
        command_name = "PrimeMesh::Model/GetFaceZoneNamesOfParts"
        self._print_beta_api_warning("get_face_zone_names_of_parts")
        self._print_logs_before_command("get_face_zone_names_of_parts", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_face_zone_names_of_parts")
        return result

    def set_suggested_zone_name(self, id : int, name : str) -> SetNameResults:
        """ Sets the unique name for zone with given id based on the suggested name.


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
            raise TypeError("Invalid argument type passed for 'id'. Valid argument type is int.")
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"id" : id,
        "name" : name}
        command_name = "PrimeMesh::Model/SetSuggestedZoneName"
        self._print_logs_before_command("set_suggested_zone_name", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_suggested_zone_name", prime.SetNameResults(model = self, json_data = result))
        return prime.SetNameResults(model = self, json_data = result)

    def set_working_directory(self, path : str):
        """ Set working directory to be considered for file i/o when file paths are relative.


        Parameters
        ----------
        path : str
            Path to the directory.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> zones = model.set_working_directory("C:/input_files")

        """
        if not isinstance(path, str):
            raise TypeError("Invalid argument type passed for 'path'. Valid argument type is str.")
        args = {"path" : path}
        command_name = "PrimeMesh::Model/SetWorkingDirectory"
        self._print_beta_api_warning("set_working_directory")
        self._print_logs_before_command("set_working_directory", args)
        self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("set_working_directory")

    def get_parts_with_topology(self) -> Iterable[int]:
        """ Gets the list of parts ids that contain topology.


        Returns
        -------
        Iterable[int]
            Returns the ids of parts with topology.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> result = model.get_parts_with_topology()

        """
        args = {}
        command_name = "PrimeMesh::Model/GetPartsWithTopology"
        self._print_beta_api_warning("get_parts_with_topology")
        self._print_logs_before_command("get_parts_with_topology", args)
        result = self._comm.serve(self, command_name, self._object_id, args=args)
        self._print_logs_after_command("get_parts_with_topology")
        return result

    @property
    def id(self):
        """ Get the id of Model."""
        return self._id

    @property
    def name(self):
        """ Get the name of Model."""
        return self._name
