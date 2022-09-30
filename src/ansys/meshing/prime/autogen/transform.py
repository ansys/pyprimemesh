""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class Transform(CoreObject):
    """Provides functionalities to initialize and manage transformation using transformation matrix.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Transform """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Transform/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Transform. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Transform. """
        command_name = "PrimeMesh::Transform/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def transform_zonelets(self, part_id : int, zonelets : Iterable[int], params : TransformParams) -> TransformResults:
        """ Transforms given zonelets using provided transform parameters.


        Parameters
        ----------
        part_id : int
            Part id of zonelets to be transformed.
        zonelets : Iterable[int]
            Ids of zonelets.
        params : TransformParams
            Transform parameters.

        Returns
        -------
        TransformResults
            Returns the transform results.


        Examples
        --------
        >>> transform_params = prime.TransformParams(model = model)
        >>> zonelets = part.get_face_zonelets()
        >>> results = surface_utilities.transform_zonelets(part.id, zonelets, params)

        """
        args = {"part_id" : part_id,
        "zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Transform/TransformZonelets"
        self._model._print_logs_before_command("transform_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("transform_zonelets", TransformResults(model = self._model, json_data = result))
        return TransformResults(model = self._model, json_data = result)
