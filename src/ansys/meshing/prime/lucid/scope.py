from typing import Iterable

from ansys.meshing.prime.autogen.controlstructs import (
    ScopeDefinition,
    ScopeEntity,
    ScopeEvaluationType,
)
from ansys.meshing.prime.autogen.partstructs import NamePatternParams
from ansys.meshing.prime.core.model import Model

from .utils import check_name_pattern


class _LucidScope:
    def __init__(
        self,
        part_expression: str,
        entity_expression: str,
        scope_evaluation_type: ScopeEvaluationType,
        scope_entity_type: ScopeEntity,
    ):
        self._part_expression = part_expression
        self._entity_expression = entity_expression
        self._evaluation_type = scope_evaluation_type
        self._entity_type = scope_entity_type

    def __str__(self) -> str:
        return "#".join(
            [
                self._part_expression,
                self._entity_expression,
                str(int(self._evaluation_type)),
                str(int(self._entity_type)),
            ]
        )

    def get_scope_definition(self, model: Model) -> ScopeDefinition:
        """Gets the scope definition of the scope.

        Parameters
        ----------
        model : Model
            PyPrimeMesh model.

        Returns
        -------
        ScopeDefinition
            Returns the scope definition.

        """
        label_exp: str = None
        zone_exp: str = None
        if self._evaluation_type == ScopeEvaluationType.LABELS:
            label_exp = self._entity_expression
        else:
            zone_exp = self._entity_expression

        sd = ScopeDefinition(
            model=model,
            entity_type=self._entity_type,
            evaluation_type=self._evaluation_type,
            part_expression=self._part_expression,
            label_expression=label_exp,
            zone_expression=zone_exp,
        )
        return sd


class SurfaceScope(_LucidScope):
    """SurfaceScope is one of the classes in Lucid API.

    This class is meant for beginners to meshing. This class is used to define
    a scope for operation on surfaces.

    """

    def __init__(
        self,
        part_expression: str = "*",
        entity_expression: str = "*",
        scope_evaluation_type: ScopeEvaluationType = ScopeEvaluationType.LABELS,
    ):
        """Initialize SurfaceScope with the given part expression,
        entity expression and scope evaluation type.

        Parameters
        ----------
        part_expression : str
            Part expression to scope parts while evaluating scope.
        entity_expression : str
            Label or zone expression to scope entities while evaluating scope.
        scope_evaluation_type : prime.ScopeEvaluationType
            Evaluation type to scope entities. The default is set to labels.

        """
        _LucidScope.__init__(
            self,
            part_expression,
            entity_expression,
            scope_evaluation_type,
            ScopeEntity.FACEZONELETS,
        )

    def get_parts(self, model: Model) -> Iterable[int]:
        """Gets the list of part ids in the scope.

        Parameters
        ----------
        model : Model
            PyPrimeMesh model.

        Returns
        -------
        Iterable[int]
            Returns the list of part ids.

        Examples
        --------
            >>> from ansys.meshing.prime import Model, SurfaceScope
            >>> model = client.model
            >>> su = SurfaceScope("*", "*", prime.ScopeEvaluationType.LABELS)
            >>> part_ids = su.get_parts()

        """
        sel_parts: Iterable[int] = []
        for part in model.parts:
            if check_name_pattern(self._part_expression, part.name):
                sel_parts.append(part.id)
        return sel_parts

    def get_face_zonelets(self, model: Model, part_id: int) -> Iterable[int]:
        """Gets the list of face zonelets for the given part in the scope.

        Parameters
        ----------
        model : Model
            PyPrimeMesh model.
        part_id : int
            Id of the part.

        Returns
        -------
        Iterable[int]
            Returns the list of zonelets.

        Examples
        --------
            >>> from ansys.meshing.prime import Model, SurfaceScope
            >>> model = client.model
            >>> su = SurfaceScope("*", "*", prime.ScopeEvaluationType.LABELS)
            >>> face_zonelets = su.get_face_zonelets(model, 2)

        """
        face_zonelets: Iterable[int] = []
        part = model.get_part(part_id)
        if part and check_name_pattern(self._part_expression, part.name):
            if self._evaluation_type == ScopeEvaluationType.LABELS:
                face_zonelets = part.get_face_zonelets_of_label_name_pattern(
                    self._entity_expression, NamePatternParams(model)
                )
            else:
                face_zonelets = part.get_face_zonelets_of_zone_name_pattern(
                    self._entity_expression, NamePatternParams(model)
                )
        return face_zonelets

    def get_topo_faces(self, model: Model, part_id: int) -> Iterable[int]:
        """Gets the list of topofaces for the given part in the scope.

        Parameters
        ----------
        model : Model
            PyPrimeMesh model.
        part_id : int
            Id of the part.

        Returns
        -------
        Iterable[int]
            Returns the list of zonelets.

        Examples
        --------
            >>> from ansys.meshing.prime import Model, SurfaceScope
            >>> model = client.model
            >>> su = SurfaceScope("*", "*", prime.ScopeEvaluationType.LABELS)
            >>> topo_faces = su.get_topo_faces(model, 2)

        """
        topo_faces: Iterable[int] = []
        part = model.get_part(part_id)
        if part and check_name_pattern(self._part_expression, part.name):
            if self._evaluation_type == ScopeEvaluationType.LABELS:
                topo_faces = part.get_topo_faces_of_label_name_pattern(
                    self._entity_expression, NamePatternParams(model)
                )
            else:
                topo_faces = part.get_topo_faces_of_zone_name_pattern(
                    self._entity_expression, NamePatternParams(model)
                )
        return topo_faces


class VolumeScope(_LucidScope):
    """VolumeScope is one of the classes in Lucid API.

    This class is meant for beginners to meshing. This class is used to define
    a scope for operation on volumes.

    """

    def __init__(
        self,
        part_expression: str = "*",
        entity_expression: str = "*",
        scope_evaluation_type: ScopeEvaluationType = ScopeEvaluationType.ZONES,
    ):
        """Initialize VolumeScope with the given part expression, entity expression and scope
        evaluation type.

        Parameters
        ----------
        part_expression : str
            Part expression to scope parts while evaluating scope.
        entity_expression : str
            Label or zone expression to scope entities while evaluating scope.
        scope_evaluation_type : ScopeEvaluationType
            Evaluation type to scope entities. The default is set to zones.

        """
        _LucidScope.__init__(
            self,
            part_expression,
            entity_expression,
            scope_evaluation_type,
            ScopeEntity.VOLUME,
        )
