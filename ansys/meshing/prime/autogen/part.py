""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class Part(CoreObject):
    """Part contains zonelets and topoentities.

    Topoentities and zonelets are characterized by dimension of entities.
    Zonelets are a group of interconnected elements in a mesh. There are three types of zonelets. They are:

    * FaceZonelet: A group of interconnected face elements.
    * EdgeZonelet: A group of interconnected edge elements.
    * CellZonelet: A group of interconnected cell elements.

    Topoentities represent connectivity information.
    Topoentities can be queried from higher order to lower order topoentities and vice versa.
    Topoentities have geometric representation which may be defined by splines or facets.
    The mesh generated on topoentities will be projected on geometry representation.

    * TopoFace: Topoentity representing surfaces.
    * TopoEdge: Topoentity representing curves.
    * TopoVolume: Topoentity representing volumes.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize Part """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def get_face_zonelets(self) -> List[int]:
        """ Gets the face zonelets of a part.


        Returns
        -------
        List[int]
            Returns the ids of face zonelets.


        Examples
        --------
        >>> face_zonelets = part.get_face_zonelets()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetFaceZonelets"
        self._model._print_logs_before_command("get_face_zonelets", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets")
        return result

    def get_cell_zonelets(self) -> List[int]:
        """ Gets the cell zonelet ids in the part.


        Returns
        -------
        List[int]
            Returns the list of cell zonelet ids.


        Examples
        --------
        >>> from ansys.meshing.prime import Part
        >>> cell_zonelet_ids = part.get_cell_zonelets()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetCellZonelets"
        self._model._print_logs_before_command("get_cell_zonelets", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_cell_zonelets")
        return result

    def get_edge_zonelets(self) -> List[int]:
        """ Gets the edge zonelets of a part.


        Returns
        -------
        List[int]
            Returns the ids of edge zonelets.


        Examples
        --------
        >>> edge_zonelets = part.get_edge_zonelets()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetEdgeZonelets"
        self._model._print_logs_before_command("get_edge_zonelets", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zonelets")
        return result

    def get_topo_faces(self) -> List[int]:
        """ Gets the topo faces of a part.


        Returns
        -------
        List[int]
            Returns the ids of topo faces.


        Examples
        --------
        >>> topo_faces = part.get_topo_faces()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetTopoFaces"
        self._model._print_logs_before_command("get_topo_faces", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces")
        return result

    def get_splines(self) -> List[int]:
        """ Gets the list of spline ids.


        Returns
        -------
        List[int]
            Returns the list of spline ids.


        Examples
        --------
        >>> from ansys.meshing.prime import Part
        >>> results = part.get_splines()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetSplines"
        self._model._print_logs_before_command("get_splines", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_splines")
        return result

    def get_summary(self, params : PartSummaryParams) -> PartSummaryResults:
        """ Gets the part summary.

        Provides the part summary for the given parameters..

        Parameters
        ----------
        params : PartSummaryParams
            Part summary parameters.

        Returns
        -------
        PartSummaryResults
            Returns the PartSummaryResults.

        Examples
        --------
        >>> results = part.get_summary(PartSummaryParams(model=model))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/GetSummary"
        self._model._print_logs_before_command("get_summary", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_summary", PartSummaryResults(model = self._model, json_data = result))
        return PartSummaryResults(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of Part."""
        return self._id

    @property
    def name(self):
        """ Get the name of Part."""
        return self._name

    @name.setter
    def name(self, name):
        """ Set the name of Part. """
        self._name = name
