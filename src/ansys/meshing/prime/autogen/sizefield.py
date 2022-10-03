""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class SizeField(CoreObject):
    """The size field is computed based on the size control defined.

    You can remesh surfaces and edges based on the size field.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize SizeField """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::SizeField/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for SizeField. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for SizeField. """
        command_name = "PrimeMesh::SizeField/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def compute_volumetric(self, size_control_ids : Iterable[int], volumetric_sizefield_params : VolumetricSizeFieldComputeParams) -> VolumetricSizeFieldComputeResults:
        """ Computes the volumetric size field using given size control ids.


        Parameters
        ----------
        size_control_ids : Iterable[int]
            Ids of size controls.

        Examples
        --------
        >>> size_field.compute_volumetric(
        >>>           [size_control.id for size_control in model.control_data.size_controls], volumetric_sizefield_params))

        """
        args = {"size_control_ids" : size_control_ids,
        "volumetric_sizefield_params" : volumetric_sizefield_params._jsonify()}
        command_name = "PrimeMesh::SizeField/ComputeVolumetric"
        self._model._print_logs_before_command("compute_volumetric", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("compute_volumetric", VolumetricSizeFieldComputeResults(model = self._model, json_data = result))
        return VolumetricSizeFieldComputeResults(model = self._model, json_data = result)
