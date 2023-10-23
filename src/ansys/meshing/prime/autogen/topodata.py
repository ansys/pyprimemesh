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

    def get_geom_zonelets_of_topo_edges(self, topo_edges : Iterable[int]) -> Iterable[int]:
        """ Get the geometry edge zonelets for the provided topoedge ids.


        Parameters
        ----------
        topo_edges : Iterable[int]
            Ids of the topoedges.

        Returns
        -------
        Iterable[int]
            Return the geometry edge zonelet ids.


        Examples
        --------
        >>> geom_edge_zonelets = topo_data.get_geom_zonelets_of_topo_edges(topo_edges)

        """
        if not isinstance(topo_edges, Iterable):
            raise TypeError("Invalid argument type passed for topo_edges, valid argument type is Iterable[int].")
        args = {"topo_edges" : topo_edges}
        command_name = "PrimeMesh::TopoData/GetGeomZoneletsOfTopoEdges"
        self._model._print_logs_before_command("get_geom_zonelets_of_topo_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_geom_zonelets_of_topo_edges")
        return result

    def get_geom_zonelets_of_topo_faces(self, topo_faces : Iterable[int]) -> Iterable[int]:
        """ Get the geometry face zonelets for the provided topoface ids.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of the topofaces.

        Returns
        -------
        Iterable[int]
            Return the geometry face zonelet ids.


        Examples
        --------
        >>> geom_face_zonelets = topo_data.get_geom_zonelets_of_topo_faces(topo_faces)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
        args = {"topo_faces" : topo_faces}
        command_name = "PrimeMesh::TopoData/GetGeomZoneletsOfTopoFaces"
        self._model._print_logs_before_command("get_geom_zonelets_of_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_geom_zonelets_of_topo_faces")
        return result

    def get_mesh_zonelets_of_topo_edges(self, topo_edges : Iterable[int]) -> Iterable[int]:
        """ Get the mesh edge zonelets for the provided topoedge ids.


        Parameters
        ----------
        topo_edges : Iterable[int]
            Ids of the topoedges.

        Returns
        -------
        Iterable[int]
            Return the mesh edge zonelet ids.


        Examples
        --------
        >>> mesh_edge_zonelets = topo_data.get_mesh_zonelets_of_topo_edges(topo_edges)

        """
        if not isinstance(topo_edges, Iterable):
            raise TypeError("Invalid argument type passed for topo_edges, valid argument type is Iterable[int].")
        args = {"topo_edges" : topo_edges}
        command_name = "PrimeMesh::TopoData/GetMeshZoneletsOfTopoEdges"
        self._model._print_logs_before_command("get_mesh_zonelets_of_topo_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_mesh_zonelets_of_topo_edges")
        return result

    def get_mesh_zonelets_of_topo_faces(self, topo_faces : Iterable[int]) -> Iterable[int]:
        """ Get the mesh face zonelets for the provided topoface ids.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of the topofaces.

        Returns
        -------
        Iterable[int]
            Return the mesh face zonelet ids.


        Examples
        --------
        >>> mesh_face_zonelets = topo_data.get_mesh_zonelets_of_topo_faces(topo_faces)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
        args = {"topo_faces" : topo_faces}
        command_name = "PrimeMesh::TopoData/GetMeshZoneletsOfTopoFaces"
        self._model._print_logs_before_command("get_mesh_zonelets_of_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_mesh_zonelets_of_topo_faces")
        return result

    def get_topo_edges_of_topo_faces(self, topo_faces : Iterable[int]) -> Iterable[int]:
        """ Get the topoedges of the provided topoface ids.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of the topoface.

        Returns
        -------
        Iterable[int]
            Returns the list of topoedge ids.


        Examples
        --------
        >>> topo_edges_of_topo_faces = topo_data.get_topo_edges_of_topo_faces(topo_faces)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
        args = {"topo_faces" : topo_faces}
        command_name = "PrimeMesh::TopoData/GetTopoEdgesOfTopoFaces"
        self._model._print_logs_before_command("get_topo_edges_of_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_edges_of_topo_faces")
        return result

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
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
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
        if not isinstance(topo_edges, Iterable):
            raise TypeError("Invalid argument type passed for topo_edges, valid argument type is Iterable[int].")
        args = {"topo_edges" : topo_edges}
        command_name = "PrimeMesh::TopoData/GetAdjacentTopoEdgesOfTopoEdges"
        self._model._print_logs_before_command("get_adjacent_topo_edges_of_topo_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_adjacent_topo_edges_of_topo_edges")
        return result

    def delete_mesh_on_topo_faces(self, topo_faces : Iterable[int], params : DeleteMeshParams) -> DeleteMeshResults:
        """ Delete mesh on the provided topofaces.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topofaces.
        params : DeleteMeshParams
            Parameters to delete mesh on topofaces.

        Returns
        -------
        DeleteMeshResults
            Returns the DeleteMeshResults.


        Notes
        -----
        This API is a Beta. API Behavior and implementation may change in future.

        Examples
        --------
        >>> params = prime.DeleteMeshParams(model = model)
        >>> result = topo_data.delete_mesh_on_topo_faces(top_faces, params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
        if not isinstance(params, DeleteMeshParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is DeleteMeshParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::TopoData/DeleteMeshOnTopoFaces"
        self._model._print_beta_api_warning("delete_mesh_on_topo_faces")
        self._model._print_logs_before_command("delete_mesh_on_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_mesh_on_topo_faces", DeleteMeshResults(model = self._model, json_data = result))
        return DeleteMeshResults(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of TopoData."""
        return self._id

    @property
    def name(self):
        """ Get the name of TopoData."""
        return self._name
