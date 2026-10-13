.. _ref_index_mesh_diagnostics:

****************
Mesh Diagnostics
****************

===========================
Mesh Statistics and Quality
===========================

You can use a set of quality metrics to measure the mesh quality. The :class:`SurfaceSearch <ansys.meshing.prime.SurfaceSearch>` and :class:`VolumeSearch <ansys.meshing.prime.VolumeSearch>` classes
allow you to check surface and volume mesh quality, respectively.

------------------
Connectivity Check
------------------

Surface diagnostics are important prior to generating a volume mesh. You can inquire surface diagnostic summary by using :func:`SurfaceSearch.get_surface_diagnostic_summary() <ansys.meshing.prime.SurfaceSearch.get_surface_diagnostic_summary>`.
The :class:`SurfaceDiagnosticSummaryParams <ansys.meshing.prime.SurfaceDiagnosticSummaryParams>` class provides the capability to diagnose surface connectivity for the given scope and controls.

* Duplicate Faces

* Free Face Edges

* Multi Faces Edges

* Self Intersections

.. code:: python

    # Check wrap surface is closed
    scope = prime.ScopeDefinition(model=model, part_expression="wrap")
    diag = prime.SurfaceSearch(model)

    diag_params = prime.SurfaceDiagnosticSummaryParams(
        model,
        scope=scope,
        compute_duplicate_faces=True,
        compute_free_edges=True,
        compute_multi_edges=True,
        compute_self_intersections=True,
    )

    diag_res = diag.get_surface_diagnostic_summary(diag_params)

The results of surface diagnostic summary can be printed as below:

.. code:: python

    >>> print('Number of duplicate faces : ', diag_res.n_duplicate_faces)
    >>> print('Number of free edges : ', diag_res.n_free_edges)
    >>> print('Number of multi edges : ', diag_res.n_multi_edges)
    >>> print('Number of self intersections : ', diag_res.n_self_intersections)

    Number of duplicate faces :  0
    Number of free edges :  0
    Number of multi edges :  0
    Number of self intersections :  0


------------
Face Metrics
------------

The :class:`FaceQualityMeasure <ansys.meshing.prime.FaceQualityMeasure>` class offers various type of face quality measures to check face quality metrics.

 * The :attr:`SKEWNESS <ansys.meshing.prime.FaceQualityMeasure.SKEWNESS>` metric ranges between 0(ideal) and 1(worst).

 * The :attr:`ASPECTRATIO <ansys.meshing.prime.FaceQualityMeasure.ASPECTRATIO>` metric is greater than 1. The smaller the Aspect Ratio, the higher the quality of an element.

 * The :attr:`ELEMENTQUALITY <ansys.meshing.prime.FaceQualityMeasure.ELEMENTQUALITY>` metric ranges between 0(worst) and 1(ideal).

.. code:: python

    face_quality_measures = prime.FaceQualityMeasure.SKEWNESS
    quality = prime.SurfaceSearch(model)
    quality_params = prime.SurfaceQualitySummaryParams(
        model=model,
        scope=prime.ScopeDefinition(model=model, part_expression="wrap"),
        face_quality_measures=[face_quality_measures],
        quality_limit=[0.9]
    )
    qual_summary_res = quality.get_surface_quality_summary(quality_params)

.. code:: python

    >>> print("Maximum surface skewness : ", qual_summary_res.quality_results[0].max_quality)
    >>> print("Number of faces above limit : ", qual_summary_res.quality_results[0].n_found)

    Maximum surface skewness :  0.862375
    Number of faces above limit :  0


------------
Cell Metrics
------------

The :class:`CellQualityMeasure <ansys.meshing.prime.CellQualityMeasure>` class offers various type of cell quality measures to check cell quality metrics.

 * The :attr:`SKEWNESS <ansys.meshing.prime.CellQualityMeasure.SKEWNESS>` metric ranges between 0(ideal) and 1(worst).

 * The :attr:`ASPECTRATIO <ansys.meshing.prime.CellQualityMeasure.ASPECTRATIO>` metric is greater than 1. The smaller the Aspect Ratio, the higher the quality of an element.

 * The :attr:`FLUENTASPECTRATIO <ansys.meshing.prime.CellQualityMeasure.FLUENTASPECTRATIO>` metric is greater than 1. The smaller the Fluent Aspect Ratio, the higher the quality of an element.

 * The :attr:`ELEMENTQUALITY <ansys.meshing.prime.CellQualityMeasure.ELEMENTQUALITY>` metric ranges between 0(worst) and 1(ideal).

.. code:: python

    cell_quality_measures = prime.CellQualityMeasure.SKEWNESS
    quality = prime.VolumeSearch(model)
    quality_params = prime.VolumeQualitySummaryParams(
        model=model,
        scope=prime.ScopeDefinition(model=model, part_expression="wrap"),
        cell_quality_measures=[cell_quality_measures],
        quality_limit=[0.95]
    )
    qual_summary_res = quality.get_volume_quality_summary(quality_params)

.. code:: python

    >>> print("Maximum skewness : ", qual_summary_res.quality_results_part[0].max_quality)
    >>> print("Number of cells above limit : ", qual_summary_res.quality_results_part[0].n_found)

    Maximum skewness :  0.948388
    Number of cells above limit :  0


-----------
Mesh Counts
-----------

The :func:`Part.get_summary() <ansys.meshing.prime.Part.get_summary>` provides the number of nodes, faces or cells after meshing
with given parameters.

.. code:: python

    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model, print_id=False, print_mesh=True))

.. code:: python

    >>> print("Number of tri faces : ", part_summary_res.n_tri_faces)
    >>> print("Number of tet cells : ", part_summary_res.n_tet_cells)
    >>> print("Number of poly cells : ", part_summary_res.n_poly_cells)
    >>> print("Total number of cells : ", part_summary_res.n_cells)

    Number of tri faces :  49430
    Number of tet cells :  254669
    Number of poly cells :  82760
    Total number of cells :  337429


================
Mesh Improvement
================

When the metrics show that the mesh quality is low, the :class:`VolumeMeshTool <ansys.meshing.prime.VolumeMeshTool>` class provides various volume mesh improvement algorithms for you to improve the mesh.

--------------
Auto Node Move
--------------

You can improve volume mesh by auto node move using :func:`VolumeMeshTool.improve_by_auto_node_move() <ansys.meshing.prime.VolumeMeshTool.improve_by_auto_node_move>` 
with given parameters. In addition, you can validate the mesh using :func:`VolumeMeshTool.check_mesh() <ansys.meshing.prime.VolumeMeshTool.check_mesh>`.

.. code:: python

    # Auto Node Move
    perform_anm = prime.VolumeMeshTool(model=model)
    anm_params = prime.AutoNodeMoveParams(
        model=model,
        quality_measure=prime.CellQualityMeasure.SKEWNESS,
        target_quality=0.95,
        dihedral_angle=90,
        n_iterations_per_node=50,
        restrict_boundary_nodes_along_surface=True,
        n_attempts=10,
    )

    perform_anm.improve_by_auto_node_move(
        part_id=part.id,
        cell_zonelets=part.get_cell_zonelets(),
        boundary_zonelets=part.get_face_zonelets(),
        params=anm_params,
    )

    # mesh check
    vtool = prime.VolumeMeshTool(model=model)
    res = vtool.check_mesh(part_id=part.id, params=prime.CheckMeshParams(model=model))

An example of the results of check mesh operation is shown below:

.. code:: python

    >>> print("Non positive volumes:", result.has_non_positive_volumes)
    >>> print("Non positive areas:", result.has_non_positive_areas)
    >>> print("Invalid shape:", result.has_invalid_shape)
    >>> print("Left handed faces:", result.has_left_handed_faces)

    Non positive volumes :  False
    Non positive areas :  False
    Invalid shape :  False
    Left handed faces :  False
