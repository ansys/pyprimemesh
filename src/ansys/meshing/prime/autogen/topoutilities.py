""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class TopoUtilities(CoreObject):
    """Performs various general surface utilities algorithms. For example, copy zonelets, resolve surface intersections.

    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize TopoUtilities  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::TopoUtilities/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for TopoUtilities. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for TopoUtilities. """
        command_name = "PrimeMesh::TopoUtilities/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def fill_hole(self, topo_edges : Iterable[int], params : TopoFillHoleParams) -> TopoFillHoleResult:
        """ Fill holes bounded by given topoedges.


        Parameters
        ----------
        topo_edges : Iterable[int]
            Ids of topoedges to be used to find holes.
        params : TopoFillHoleParams
            Parameters to fill holes.

        Returns
        -------
        TopoFillHoleResult
            Return the TopoFillHoleResult.


        Examples
        --------
        >>> results = topo_utils.fill_hole(topo_edges, params)

        """
        args = {"topo_edges" : topo_edges,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::TopoUtilities/FillHole"
        self._model._print_logs_before_command("fill_hole", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("fill_hole", TopoFillHoleResult(model = self._model, json_data = result))
        return TopoFillHoleResult(model = self._model, json_data = result)
