from ansys.meshing.prime.autogen.controlstructs import ScopeDefinition
from ansys.meshing.prime.autogen.volumesearch import VolumeSearch as _VolumeSearch
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.autogen.volumesearchstructs import (
    VolumeQualitySummaryParams,
    VolumeQualitySummaryResults
)
from ansys.meshing.prime.autogen.commontypes import (
    CellQualityMeasure,
    SolverType
)
from typing import List

class VolumeQualitySummary( _VolumeSearch):
    __doc__ = _VolumeSearch.__doc__

    def __init__(self,
                 model: Model,
                 parts: List[Part]=None,
                 scope: ScopeDefinition=None,
                 solver:  SolverType=None,
                 cell_quality_measures: List[CellQualityMeasure]=None,
                 quality_limit: List[float]=None):
        """Initialize VolumeQualitySummary.

        Constructor to initialize VolumeQualitySummary object.
        Uses solver type to define cell quality measures if not defined explicitly.

        Parameters
        ----------
        model : CommunicationManager
            Communication manager to serve JSON API.
        parts : List[Part], optional
            List of parts used to scope cell zonelets to get volume quality summary.
        scope : ScopeDefinition, optional
            Scope definition to scope the cell zonelets to get volume quality summary.
            If specified will take precedence over parts. The default scope is cell
            zonelets of all parts.
        solver : SolverType, optional
            Grouping of cell quality measures based on solver type. The default is MAPDL.
        cell_quality_measures : List[CellQualityMeasure], optional
            List of cell quality measures used to get volume quality summary.
            If specified will ignore a group defined by solver type.
        quality_limit : List[float], optional
            List of quality limit per cell quality measure. Uses default quality limit
            if not specified.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> volume_quality_summary = VolumeQualitySummary(model=model, solver = SolverType.FLUENT)
        """
        self._model = model
        self._params  = VolumeQualitySummaryParams(model=model)
        self._qualityresults : VolumeQualitySummaryResults = None
        self._solver_type: SolverType = SolverType.MAPDL
        self._parts: List[Part] = None
        if (solver != None):
            self._solver_type = solver
            self._params.cell_quality_measures = [CellQualityMeasure.ELEMENTQUALITY]
            if (solver == SolverType.FLUENT):
                self._params.cell_quality_measures = [CellQualityMeasure.SKEWNESS]
        if (parts != None):
            self._parts = parts
            self._params.scope.part_expression = ''.join(part.name + ', ' for part in parts)
        if (cell_quality_measures != None):
            self._params.cell_quality_measures = cell_quality_measures
        if (quality_limit != None):
            self._params.quality_limit = quality_limit
        if (scope != None):
            self._params.scope = scope
        _VolumeSearch.__init__(self, model)

    def __str__(self) -> str:
        """Prints the volume quality summary.

        Uses cell quality measures, parts, scope, solver type and quality limit properties
        to print the volume quality summary.

        Returns
        -------
        str
            Returns the volume quality summary.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> print(model)
        """
        self._qualityresults = _VolumeSearch.get_volume_quality_summary(self, self._params)
        return self._qualityresults.summary

    @property
    def cell_quality_measures(self) -> List[int]:
        """ List of cell quality measures for which to get volume quality summary."""
        return self._params.cell_quality_measures

    @cell_quality_measures.setter
    def cell_quality_measures(self, value: List[int]):
        self._qualityresults = None
        self._params.cell_quality_measures = value

    @property
    def scope(self) -> ScopeDefinition:
        """ Scope definition to scope cell zonelets to get volume quality summary."""
        return self._params.scope

    @scope.setter
    def scope(self, value: ScopeDefinition):
        self._qualityresults = None
        self._params.scope = value

    @property
    def solver_type(self) -> SolverType:
        """ Grouping of cell quality measures based on solver type."""
        return self._solver_type

    @solver_type.setter
    def solver_type(self, value: SolverType):
        self._qualityresults = None
        self._solver_type = value
        self._params.cell_quality_measures = [CellQualityMeasure.ELEMENTQUALITY]
        if (value == SolverType.FLUENT):
            self._params.cell_quality_measures = [CellQualityMeasure.SKEWNESS]

    @property
    def quality_limit(self) -> List[float]:
        """ List of quality limit per cell quality measure."""
        return self._params.quality_limit

    @quality_limit.setter
    def quality_limit(self, value: List[float]):
        self._qualityresults = None
        self._params.quality_limit = value

    @property
    def parts(self) -> List[Part]:
        """ List of parts to scope cell zonelets to get volume quality summary."""
        return self._parts

    @parts.setter
    def parts(self, value: List[Part]):
        self._qualityresults = None
        self._parts = value
        self._params.scope.part_expression = ''.join(part.name + ', ' for part in value)