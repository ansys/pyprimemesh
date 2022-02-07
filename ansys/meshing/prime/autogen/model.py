""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

import logging
from ansys.meshing.prime.internals import utils

class Model(CoreObject, CommunicationManager):
    """Model is the nucleus of PRIME. Model forms the base and contains all the information about PRIME.

    You can access any information in PRIME only through Model.
    Model allows you to query TopoData, ControlData, Parts, SizeFields and more.
    """

    def __init__(self, comm, id: int, object_id: int, name: str):
        """ Initialize Model """
        self._comm = comm
        self._logger = logging.getLogger("PyPrime")
        self._id = id
        self._object_id = object_id
        self._name = name

    def _print_logs_before_command(self, command, args):
        utils.print_logs_before_command(self._logger, command, args)

    def _print_logs_after_command(self, command, args = None):
        utils.print_logs_after_command(self._logger, command, args)

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
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Model/SetGlobalSizingParams"
        self._print_logs_before_command("set_global_sizing_params", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._print_logs_after_command("set_global_sizing_params", SetSizingResults(model = self, json_data = result))
        return SetSizingResults(model = self, json_data = result)

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
        args = {"num" : num}
        command_name = "PrimeMesh::Model/SetNumThreads"
        self._print_logs_before_command("set_num_threads", args)
        self._comm.serve(command_name, self._object_id, args=args)
        self._print_logs_after_command("set_num_threads")

    @property
    def id(self):
        """ Get the id of Model."""
        return self._id

    @property
    def name(self):
        """ Get the name of Model."""
        return self._name

    @name.setter
    def name(self, name):
        """ Set the name of Model. """
        self._name = name
