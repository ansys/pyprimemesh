from ansys.meshing.prime.autogen.controlstructs import ScopeDefinition
from ansys.meshing.prime.autogen.surfacesearch import SurfaceSearch as _SurfaceSearch
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.autogen.surfacesearchstructs import (
    SurfaceQualitySummaryParams,
    SurfaceQualitySummaryResults
)
from ansys.meshing.prime.autogen.commontypes import (
    FaceQualityMeasure,
    SolverType
)
from typing import List, Iterable

class SurfaceQualitySummary( _SurfaceSearch):
    __doc__ = _SurfaceSearch.__doc__

    def __init__(self,
                 model: Model,
                 parts: List[Part]=None,
                 scope: ScopeDefinition=None,
                 solver:  SolverType=None,
                 face_quality_measures: List[FaceQualityMeasure]=None,
                 quality_limit: Iterable[float]=None):
        """Initialize SurfaceQualitySummary.

        Constructor to initialize SurfaceQualitySummary object.
        Uses solver type to define face quality measures if not defined explicitly.

        Parameters
        ----------
        model : CommunicationManager
            Communication manager to serve JSON API.
        parts : List[Part], optional
            List of parts used to scope face zonelets to get surface quality summary.
        scope : ScopeDefinition, optional
            Scope definition to scope the face zonelets to get surface quality summary.
            If specified will take precedence over parts. The default scope is face
            zonelets of all parts.
        solver : SolverType, optional
            Grouping of face quality measures based on solver type. The default is MAPDL.
        face_quality_measures : List[FaceQualityMeasure], optional
            List of face quality measures used to get surface quality summary.
            If specified will ignore a group defined by solver type.
        quality_limit : Iterable[float], optional
            Iterable of quality limit per face quality measure. Uses default quality limit
            if not specified.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> quality_summary = SurfaceQualitySummary(model=model, solver = SolverType.FLUENT)
        """
        self._model = model
        self._params  = SurfaceQualitySummaryParams(model=model)
        self._qualityresults : SurfaceQualitySummaryResults = None
        self._solver_type: SolverType = SolverType.MAPDL
        self._parts: List[Part] = None
        if (solver != None):
            self._solver_type = solver
            self._params.face_quality_measures = [FaceQualityMeasure.ELEMENTQUALITY]
            if (solver == SolverType.FLUENT):
                self._params.face_quality_measures = [FaceQualityMeasure.SKEWNESS]
        if (parts != None):
            self._parts = parts
            self._params.scope.part_expression = ''.join(part.name + ', ' for part in parts)
        if (face_quality_measures != None):
            self._params.face_quality_measures = face_quality_measures
        if (quality_limit != None):
            self._params.quality_limit = quality_limit
        if (scope != None):
            self._params.scope = scope
        _SurfaceSearch.__init__(self, model)

    def __str__(self) -> str:
        """Prints the suface quality summary.

        Uses face quality measures, parts, scope, solver type and quality limit properties
        to print the surface quality summary.

        Returns
        -------
        str
            Returns the surface quality summary.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> print(model)
        """
        self._qualityresults = _SurfaceSearch.get_surface_quality_summary(self, self._params)
        return self._qualityresults.summary

    @property
    def face_quality_measures(self) -> List[int]:
        """ List of face quality measures for which to get surface quality summary."""
        return self._params.face_quality_measures

    @face_quality_measures.setter
    def face_quality_measures(self, value: List[int]):
        self._qualityresults = None
        self._params.face_quality_measures = value

    @property
    def scope(self) -> ScopeDefinition:
        """ Scope definition to scope face zonelets to get surface quality summary."""
        return self._params.scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._qualityresults = None
        self._params.scope = value

    @property
    def solver_type(self) -> SolverType:
        """ Grouping of face quality measures based on solver type."""
        return self._solver_type

    @solver_type.setter
    def solver_type(self, value: SolverType):
        self._qualityresults = None
        self._solver_type = value
        self._params.face_quality_measures = [FaceQualityMeasure.ELEMENTQUALITY]
        if (value == SolverType.FLUENT):
            self._params.face_quality_measures = [FaceQualityMeasure.SKEWNESS]

    @property
    def quality_limit(self) -> List[float]:
        """ List of quality limit per face quality measure."""
        return self._params.quality_limit

    @quality_limit.setter
    def quality_limit(self, value: List[float]):
        self._qualityresults = None
        self._params.quality_limit = value

    @property
    def parts(self) -> List[Part]:
        """ List of parts to scope face zonelets to get surface quality summary."""
        return self._parts

    @parts.setter
    def parts(self, value: List[Part]):
        self._qualityresults = None
        self._parts = value
        self._params.scope.part_expression = ''.join(part.name + ', ' for part in value)