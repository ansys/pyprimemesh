""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class Part(CoreObject):
    """A collection of zonelets. 

    Parts are a collection of zonelets and information about how the zonelets are connected to each other.
    Zonelets are a group of interconnected entities in a mesh. There are four types of zonelets. They are:
    - FaceZonelet: A group of interconnected faces
    - EdgeZonelet: A group of connected edges
    - CellZonelet: A group of connected cells
    - NodeZonelet: A group of connected nodes
    """ 

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize Part """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()
    
    def get_summary(self, params : PartSummaryParams) -> PartSummaryResults:
        """ Gets the part summary.

        Gets the part summary for the provided parameters

        Parameters
        ----------
        params : PartSummaryParams
            Part summary parameters.

        Returns
        -------
        PartSummaryResults
            Returns the PartSummaryResults structure.

        Examples
        --------
        
        >>> results = part.get_summary(PartSummaryParams(model=model))

        """
        args = {"params" : params.jsonify()}
        command_name = "PrimeMesh::Part/GetSummary"
        self._model._print_logs_before_command("get_summary", args)
        result = self._comm.serve(command_name, self.object_id, args=args)
        self._model._print_logs_after_command("get_summary", PartSummaryResults(model = self._model, json_data = result))
        return PartSummaryResults(model = self._model, json_data = result)
    
    @property
    def id(self):
        """ Get id """
        return self._id
    
    @property
    def object_id(self):
        """ GetObjectId """
        return self._object_id
    @property
    def name(self):
        """ Get name """
        return self._name
    
    @name.setter
    def name(self, name):
        """ Set the name """
        self._name = name
    
