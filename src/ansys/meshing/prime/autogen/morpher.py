""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class Morpher(CoreObject):
    """Morpher contain functionalities to change the geometry, adapting the mesh accordingly without a recomputation.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Morpher """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Morpher/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Morpher. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Morpher. """
        command_name = "PrimeMesh::Morpher/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def match_morph(self, part_id : int, match_pairs : List[MatchPair], match_morph_params : MatchMorphParams, bc_params : MorphBCParams, solve_params : MorphSolveParams) -> MatchMorphResults:
        """ Match source and target zonelets defined by match pairs with prescribed boundary conditions for each pair. Also, solves boundary condition parameters to define uniform surface and volume regions in source neighborhood.


        Parameters
        ----------
        part_id : int
            Id of source part.
        match_pairs : MatchPairArray
            Array of match pairs of sources and targets.
        match_morph_params : MatchMorphParams
            Match morph parameters.
        bc_params : MorphBCParams
            Morph boundary condition parameters.
        solve_params : MorphSolveParams
            Morpher solve parameters.

        Returns
        -------
        MatchMorphResults
            Returns the MatchMorphResults.


        Examples
        --------
        >>> result = morph.match_morph([match_pair1, match_pair2], match_morph_params, bc_params, solve_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(match_pairs, List):
            raise TypeError("Invalid argument type passed for match_pairs, valid argument type is List[MatchPair].")
        if not isinstance(match_morph_params, MatchMorphParams):
            raise TypeError("Invalid argument type passed for match_morph_params, valid argument type is MatchMorphParams.")
        if not isinstance(bc_params, MorphBCParams):
            raise TypeError("Invalid argument type passed for bc_params, valid argument type is MorphBCParams.")
        if not isinstance(solve_params, MorphSolveParams):
            raise TypeError("Invalid argument type passed for solve_params, valid argument type is MorphSolveParams.")
        args = {"part_id" : part_id,
        "match_pairs" : [p._jsonify() for p in match_pairs],
        "match_morph_params" : match_morph_params._jsonify(),
        "bc_params" : bc_params._jsonify(),
        "solve_params" : solve_params._jsonify()}
        command_name = "PrimeMesh::Morpher/MatchMorph"
        self._model._print_logs_before_command("match_morph", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("match_morph", MatchMorphResults(model = self._model, json_data = result))
        return MatchMorphResults(model = self._model, json_data = result)
