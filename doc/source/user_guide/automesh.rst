.. _ref_index_automesh:


******************
Volumetric Meshing
******************

The :class:`AutoMesh <ansys.meshing.prime.AutoMesh>` class enables you to 
automatically create the volume mesh using different volume meshing algorithms. It generates the volume mesh for all computed 
volumetric regions of the mesh object. For example, mesh objects created from the imported geometry.
:func:`AutoMesh.mesh() <ansys.meshing.prime.AutoMesh.mesh>` allows you to perform volume meshing with given meshing parameters.

--------------------------------------
Meshing with Second Order Tetrahedrons
--------------------------------------

The following example shows how to initialize automesh parameters and generate volume mesh on meshed topofaces:

.. code:: python

   >>> # Volume mesh with 2nd order tetrahedral elements
   >>> automesher_params = prime.AutoMeshParams(
   >>>     model=model,
   >>>     max_size=1.0,
   >>>     volume_fill_type=prime.VolumeFillType.TET,
   >>>     tet=prime.TetParams(model=model, quadratic=True)
   >>> )
   >>> print(automesher_params)

   size_field_type :  SizeFieldType.GEOMETRIC
   max_size :  1.0
   prism_control_ids :  []
   volume_fill_type :  VolumeFillType.TET
   prism :  { no_imprint_zonelets :  [] }
   tet :  { quadratic :  True }
   volume_control_ids :  []

   >>> prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesher_params)

-----------------------------------
Meshing with Polyhedrons and Prisms
-----------------------------------

The following example shows you the procedure to:

* Create prism control and specify boundary layer setting
* Volume mesh with Polyhedral elements
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

.. code:: python

   >>> # Volume mesh with polyhedral elements
   >>> automesher_params = prime.AutoMeshParams(
   >>>     model=model,
   >>>     volume_fill_type=prime.VolumeFillType.POLY,
   >>>     prism_control_ids=[prism_control.id]
   >>> )
   >>> prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesher_params)

.. code:: python

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
