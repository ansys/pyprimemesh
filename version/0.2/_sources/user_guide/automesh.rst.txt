.. _ref_index_automesh:


******************
Volumetric Meshing
******************

The :class:`AutoMesh <ansys.meshing.prime.AutoMesh>` class enables you to
automatically create the volume mesh using different volume meshing algorithms. It generates the volume mesh for all computed 
volumetric regions of the mesh object. For example, mesh objects created from the imported geometry.
:func:`AutoMesh.mesh() <ansys.meshing.prime.AutoMesh.mesh>` allows you to perform volumetric meshing with given meshing parameters.

.. note::
   The starting point for this volumetric meshing procedure is a valid surface mesh.

.. tip::
    Volume mesh can be generated using :func:`Mesh.volume_mesh() <ansys.meshing.prime.lucid.Mesh.volume_mesh>` in Lucid API.

=============================
Second Order Tetrahedral Mesh
=============================

The following example shows how to initialize :class:`AutoMeshParams<ansys.meshing.prime.AutoMeshParams>` and generate volume mesh on meshed topofaces:

.. code:: python

   automesh_params = prime.AutoMeshParams(
       model=model,
       max_size=1.0,
       volume_fill_type=prime.VolumeFillType.TET,
       tet=prime.TetParams(model=model, quadratic=True)
   )

You can review the parameters for volume meshing:

.. code:: python

   >>> print(automesh_params)

   size_field_type :  SizeFieldType.GEOMETRIC
   max_size :  1.0
   prism_control_ids :  []
   volume_fill_type :  VolumeFillType.TET
   prism :  { no_imprint_zonelets :  [] }
   tet :  { quadratic :  True }
   volume_control_ids :  []

.. code:: python

   prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_params)


==================================
Prism Controls for Polyhedral Mesh
==================================

:class:`PrismControl <ansys.meshing.prime.PrismControl>` class helps you to control the prism mesh generation based on the face scope, volume scope and growth rate.
You can use one or more prism controls. Each prism control definition is applied to one or more boundary zones, and then affects the height distribution and number of layers of the prism cells in the adjacent boundary layers.  

The following example shows you the procedure to:

* Create prism control and specify boundary layer setting
* Volume mesh with polyhedral elements
* Check volume mesh quality based on cell quality measures (visit :ref:`ref_index_mesh_diagnostics` section for more information.)

.. code:: python

   # Prism control
   prism_control = model.control_data.create_prism_control()
   face_scope = prime.ScopeDefinition(
       model=model,
       entity_type = prime.ScopeEntity.FACEZONELETS,
       label_expression="* !inlet !outlet"
   )
   volume_scope = prime.ScopeDefinition(
       model=model,
       entity_type = prime.ScopeEntity.VOLUME,
       label_expression="*"
   )
   prism_control.set_surface_scope(face_scope)
   prism_control.set_volume_scope(volume_scope)
   prism_control.set_growth_params(prime.PrismControlGrowthParams(model=model))

   # Volume mesh with polyhedral elements
   automesh_params = prime.AutoMeshParams(
       model=model,
       volume_fill_type=prime.VolumeFillType.POLY,
       prism_control_ids=[prism_control.id]
   )
   prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_params)

   # Volume search to check volume mesh quality
   search = prime.VolumeSearch(model=model)
   qual_params = prime.VolumeQualitySummaryParams(
       model=model,
       cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
       quality_limit=[0.95]
   )
   qual_summary_res = search.get_volume_quality_summary(params=qual_params)

You can print the result of volume quality summary:

.. code:: python

    >>> print(qual_summary_res)

    error_code :  ErrorCode.NOERROR
    quality_results_part :  [
    cell_quality_measure :  CellQualityMeasure.SKEWNESS
    measure_name :  Skewness
    part_id :  2
    quality_limit :  0.95
    n_found :  0
    max_quality :  0.795889
    min_quality :  0.00163176]
    message :  Skewness
        Part ID: flow_volume
        Quality Limit: 0.95
            Number of failures: 0
            Max Skew: 0.795889
            Min Skew: 0.00163176
    Summary Results:
        Number of failures: 0
        Max Skew: 0.795889
        Min Skew: 0.00163176

Prism Controls for Polyhedral Mesh using Lucid class
----------------------------------------------------

The following example shows you the method required to generate a poly prism mesh as shown above:

.. code:: python

    # Volume mesh with polyhedral elements
    # Set prism layers parameter for boundary layer refinement
    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_layers=5,
        prism_surface_expression="* !inlet !outlet"
    )


=============================
Volume Specific Mesh Controls
=============================

:class:`VolumeControl <ansys.meshing.prime.VolumeControl>` class helps you to control volume mesh zonelet (fluids, solid, dead) and elements (tetrahedrons, polyhedrons and so on).
It allows you to define the scope and generate the various types of volume mesh.

The following example shows you the procedure to:

* Create volume control and set zone-specific parameters
* Volume mesh with tetrahedral elements

.. code:: python

   # Volume control
   volume_control = model.control_data.create_volume_control()
   volume_scope = prime.ScopeDefinition(
       model=model,
       evaluation_type=prime.ScopeEvaluationType.ZONES,
       zone_expression="*"
   )
   volume_control.set_scope(volume_scope)
   volume_control.set_params(
       prime.VolumeControlParams(
           model=model,
           cell_zonelet_type=prime.CellZoneletType.FLUID
       )
   )

   # Volume mesh
   automesh_params = prime.AutoMeshParams(
       model=model,
       size_field_type=prime.SizeFieldType.VOLUMETRIC,
       volume_fill_type=prime.VolumeFillType.TET,
       volume_control_ids=[volume_control.id]
   )
   prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_params)
