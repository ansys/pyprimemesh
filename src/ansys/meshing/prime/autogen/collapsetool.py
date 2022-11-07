""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class CollapseTool(CoreObject):
    """Performs various collapse operations. For example, split and collapse on face zonelets.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize CollapseTool """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::CollapseTool/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for CollapseTool. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for CollapseTool. """
        command_name = "PrimeMesh::CollapseTool/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def split_and_collapse_on_zonelets(self, part_id : int, face_zonelets : Iterable[int], register_id : int, split_params : SplitParams, collapse_params : CollapseParams) -> CollapseResults:
        """ Split and collapse elements on face zonelets with the specified register id.


        Parameters
        ----------
        part_id : int
            Id of a part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id used to identify face elements to split and collapse.
        split_params : SplitParams
            Parameters to split longest edge of face elements before collapse.
        collapse_params : CollapseParams
            Parameters to collapse shortest edge of face elements.

        Returns
        -------
        CollapseResults
            Returns the CollapseResults.

        Examples
        --------
        collapse_tool = prime.CollapseTool(model = model)
        results = collapse_tool.split_and_collapse_on_zonelets(part.id,
        part.get_face_zonelets(),
        register_id,
        prime.SplitParams(model=model),
        prime.CollapseParams(model=model))

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "split_params" : split_params._jsonify(),
        "collapse_params" : collapse_params._jsonify()}
        command_name = "PrimeMesh::CollapseTool/SplitAndCollapseOnZonelets"
        self._model._print_logs_before_command("split_and_collapse_on_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("split_and_collapse_on_zonelets", CollapseResults(model = self._model, json_data = result))
        return CollapseResults(model = self._model, json_data = result)
