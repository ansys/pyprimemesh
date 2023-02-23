""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class TopoData(CoreObject):
    """Topodata has all information about connectivity of nodes, edges, elements and more.

    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize TopoData """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def get_adjacent_topo_faces_of_topo_faces(self, topo_faces : Iterable[int]) -> Iterable[int]:
        """ Get the adjacent topofaces for the provided topoface ids.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of the topoface.

        Returns
        -------
        Iterable[int]
            Returns the list of adjacent topoface ids.


        Examples
        --------
        >>> topo_faces_of_topo_faces = topo_data.get_adjacent_topo_faces_of_topo_faces(topo_faces)

        """
        args = {"topo_faces" : topo_faces}
        command_name = "PrimeMesh::TopoData/GetAdjacentTopoFacesOfTopoFaces"
        self._model._print_logs_before_command("get_adjacent_topo_faces_of_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_adjacent_topo_faces_of_topo_faces")
        return result

    def get_adjacent_topo_edges_of_topo_edges(self, topo_edges : Iterable[int]) -> Iterable[int]:
        """ Get the adjacent topoedges for the provided topoedge ids.


        Parameters
        ----------
        topo_edges : Iterable[int]
            Ids of the topoedge.

        Returns
        -------
        Iterable[int]
            Returns the list of adjacent topoedge ids.


        Examples
        --------
        >>> topo_edges_of_topo_edges = topo_data.get_adjacent_topo_edges_of_topo_edges(topo_edges)

        """
        args = {"topo_edges" : topo_edges}
        command_name = "PrimeMesh::TopoData/GetAdjacentTopoEdgesOfTopoEdges"
        self._model._print_logs_before_command("get_adjacent_topo_edges_of_topo_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_adjacent_topo_edges_of_topo_edges")
        return result

    @property
    def id(self):
        """ Get the id of TopoData."""
        return self._id

    @property
    def name(self):
        """ Get the name of TopoData."""
        return self._name
