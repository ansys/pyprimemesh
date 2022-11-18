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

------------------------------
Second Order Tetrahedral Mesh
------------------------------

The following example shows how to initialize :class:`AutoMeshParams<ansys.meshing.prime.AutoMeshParams>` and generate volume mesh on meshed topofaces:

.. code:: python

   >>> # Volume mesh with 2nd order tetrahedral elements
   >>> automesh_param = prime.AutoMeshParams(
   >>>     model=model,
   >>>     max_size=1.0,
   >>>     volume_fill_type=prime.VolumeFillType.TET,
   >>>     tet=prime.TetParams(model=model, quadratic=True)
   >>> )
   >>> print(automesh_param)

   size_field_type :  SizeFieldType.GEOMETRIC
   max_size :  1.0
   prism_control_ids :  []
   volume_fill_type :  VolumeFillType.TET
   prism :  { no_imprint_zonelets :  [] }
   tet :  { quadratic :  True }
   volume_control_ids :  []

   >>> prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_param)


----------------------------------
Prism Controls for Polyhedral Mesh
----------------------------------

:class:`PrismControl <ansys.meshing.prime.PrismControl>` class helps you to control the prism mesh generation based on the face scope, volume scope and growth rate.
Prism cells creates either quadrilateral or triangular boundary faces, or both. They can resolve a boundary layer region of a tetrahedral mesh.

The following example shows you the procedure to:

* Create prism control and specify boundary layer setting
* Volume mesh with polyhedral elements
* Check volume mesh quality based on cell quality measures

.. code:: python

   >>> # Prism control
   >>> prism_control = model.control_data.create_prism_control()
   >>> face_scope = prime.ScopeDefinition(
   >>>     model=model,
   >>>     entity_type = prime.ScopeEntity.FACEZONELETS,
   >>>     label_expression="* !inlet !outlet"
   >>> )
   >>> volume_scope = prime.ScopeDefinition(
   >>>     model=model,
   >>>     entity_type = prime.ScopeEntity.VOLUME,
   >>>     label_expression="*"
   >>> )
   >>> prism_control.set_surface_scope(face_scope)
   >>> prism_control.set_volume_scope(volume_scope)
   >>> prism_control.set_growth_params(prime.PrismControlGrowthParams(model=model))
   >>>
   >>> # Volume mesh with polyhedral elements
   >>> automesh_param = prime.AutoMeshParams(
   >>>     model=model,
   >>>     volume_fill_type=prime.VolumeFillType.POLY,
   >>>     prism_control_ids=[prism_control.id]
   >>> )
   >>> prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_param)
   >>>
   >>> # Volume search to check volume mesh quality
   >>> search = prime.VolumeSearch(model=model)
   >>> qual_params = prime.VolumeQualitySummaryParams(
   >>>     model=model,
   >>>     cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
   >>>     quality_limit=[0.95]
   >>> )
   >>> qual_summary_res = search.get_volume_quality_summary(params=qual_params)
   >>> print('Max. skewness : ', qual_summary_res.quality_results_part[0].max_quality)
   >>> print('Number of cells violating target skewness : ', qual_summary_res.quality_results_part[0].n_found)
   >>>
   >>> # Get part summary
   >>> part_summary_res = part.get_summary(prime.PartSummaryParams(model=model, print_id=False, print_mesh=True))
   >>> print('Number of cells : ', part_summary_res.n_cells)

   Max. skewness :  0.795889
   Number of cells violating target skewness :  0
   Number of cells :  10630


------------------------------
Volume Specific Mesh Controls
------------------------------

:class:`VolumeControl <ansys.meshing.prime.VolumeControl>` class helps you to control volume mesh zonelet (fluids, solid, dead) and elements (tetrahedrons, polyhedrons and so on).
It allows you to define the scope and generate the various types of volume mesh.

The following example shows you the procedure to:

* Create volume control and set zone-specific parameters
* Volume mesh with tetrahedral elements

.. code:: python

   >>> # Volume control
   >>> volume_control = model.control_data.create_volume_control()
   >>> volume_scope = prime.ScopeDefinition(
   >>>     model=model,
   >>>     evaluation_type=prime.ScopeEvaluationType.ZONES,
   >>>     zone_expression="*"
   >>> )
   >>> volume_control.set_scope(volume_scope)
   >>> volume_control.set_params(
   >>>     prime.VolumeControlParams(
   >>>         model=model,
   >>>         cell_zonelet_type=prime.CellZoneletType.FLUID
   >>>     )
   >>> )
   >>>
   >>> # Volume mesh
   >>> automesh_param = prime.AutoMeshParams(
   >>>     model=model,
   >>>     size_field_type=prime.SizeFieldType.VOLUMETRIC,
   >>>     volume_fill_type=prime.VolumeFillType.TET,
   >>>     volume_control_ids=[volume_control.id]
   >>> )
   >>> prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_param)
