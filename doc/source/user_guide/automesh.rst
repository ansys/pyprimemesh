.. _ref_index_automesh:


******************
Volumetric meshing
******************

The :class:`AutoMesh <ansys.meshing.prime.AutoMesh>` class enables you to
automatically create the volume mesh using different volume meshing algorithms. This class
generates the volume mesh for all computed volumetric regions of the mesh object.
For example, it creates mesh objects from the imported geometry. The
:func:`AutoMesh.mesh() <ansys.meshing.prime.AutoMesh.mesh>` method allows you to perform
volumetric meshing with given meshing parameters.

.. note::
   The starting point for the volumetric meshing procedure is a valid surface mesh.

.. tip::
    Volume mesh can be generated using the :func:`Mesh.volume_mesh() <ansys.meshing.prime.lucid.Mesh.volume_mesh>`
    method in the Lucid API.

=============================
Second-order tetrahedral mesh
=============================

This code shows how to initialize the :class:`AutoMeshParams<ansys.meshing.prime.AutoMeshParams>` class
and generate the volume mesh on meshed TopoFaces:

.. code-block:: python

   automesh_params = prime.AutoMeshParams(
       model=model,
       max_size=1.0,
       volume_fill_type=prime.VolumeFillType.TET,
       tet=prime.TetParams(model=model, quadratic=True),
   )


This code prints the automatic mesh parameters so that you can review them:

.. code-block:: pycon

   >>> print(automesh_params)

   size_field_type :  SizeFieldType.GEOMETRIC
   max_size :  1.0
   prism_control_ids :  []
   volume_fill_type :  VolumeFillType.TET
   prism :  { no_imprint_zonelets :  [] }
   tet :  { quadratic :  True }
   volume_control_ids :  []


This code generates the volume mesh:

.. code-block:: python

   prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_params)


==================================
Prism controls for polyhedral mesh
==================================

The :class:`PrismControl <ansys.meshing.prime.PrismControl>` class helps you to control prism mesh generation
based on the face scope, volume scope and growth rate. You can use one or more prism controls. Each prism control
definition is applied to one or more boundary zones and affects the height distribution and number of layers of
the prism cells in the adjacent boundary layers.  

This example shows how to perform these steps:

* Create the prism control and specify the boundary layer setting.
* Perform volume meshing with polyhedral elements.
* Check volume mesh quality based on cell quality measures. For more information, see :ref:`ref_index_mesh_diagnostics`.

.. code-block:: python

   # Prism control
   prism_control = model.control_data.create_prism_control()
   face_scope = prime.ScopeDefinition(
       model=model,
       entity_type=prime.ScopeEntity.FACEZONELETS,
       label_expression="* !inlet !outlet",
   )
   volume_scope = prime.ScopeDefinition(
       model=model, entity_type=prime.ScopeEntity.VOLUME, label_expression="*"
   )
   prism_control.set_surface_scope(face_scope)
   prism_control.set_volume_scope(volume_scope)
   prism_control.set_growth_params(prime.PrismControlGrowthParams(model=model))

   # Volume mesh with polyhedral elements
   automesh_params = prime.AutoMeshParams(
       model=model,
       volume_fill_type=prime.VolumeFillType.POLY,
       prism_control_ids=[prism_control.id],
   )
   prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_params)

   # Volume search to check volume mesh quality
   search = prime.VolumeSearch(model=model)
   qual_params = prime.VolumeQualitySummaryParams(
       model=model,
       cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
       quality_limit=[0.95],
   )
   qual_summary_res = search.get_volume_quality_summary(params=qual_params)

This code prints the volume quality summary:

.. code-block:: pycon

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

Prism controls for polyhedral mesh using the Lucid module
---------------------------------------------------------

This example shows how to generate the preceding poly prism method using the Lucid module:

.. code-block:: python

    # Volume mesh with polyhedral elements
    # Set prism layers parameter for boundary layer refinement
    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_layers=5,
        prism_surface_expression="* !inlet !outlet",
    )


=============================
Volume-specific mesh controls
=============================

The :class:`VolumeControl <ansys.meshing.prime.VolumeControl>` class helps you to control volume mesh zonelets and elements.
Volume mesh zonelets include fluids, solid, and dead. Elements include tetrahedrons and polyhedrons. This class
allows you to define the scope and generate the various types of volume mesh.

This example shows how to perform these steps:

* Create volume control and set zone-specific parameters.
* Perform volume meshing with tetrahedral elements.

.. code-block:: python

   # Volume control
   volume_control = model.control_data.create_volume_control()
   volume_scope = prime.ScopeDefinition(
       model=model, evaluation_type=prime.ScopeEvaluationType.ZONES, zone_expression="*"
   )
   volume_control.set_scope(volume_scope)
   volume_control.set_params(
       prime.VolumeControlParams(
           model=model, cell_zonelet_type=prime.CellZoneletType.FLUID
       )
   )

   # Volume mesh
   automesh_params = prime.AutoMeshParams(
       model=model,
       size_field_type=prime.SizeFieldType.VOLUMETRIC,
       volume_fill_type=prime.VolumeFillType.TET,
       volume_control_ids=[volume_control.id],
   )
   prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesh_params)


********************
Thin Volume Meshing
********************

Thin Volume Meshing creates prisms from a source face mesh projecting to a target with the specified number of layers. Thin Volume Meshing can be applied only on meshed surfaces.  

Some points to remember while performing Thin Volume Meshing: 

* Thin Volume meshing does not support topology. 

* Source and target face zonelets should not be the same. 

* The number of prism layers to be created between Source and Target must be greater than zero. 

* A Source face zonelet cannot be target later. 

* A source can only belong to two thin volume controls. 

* Always choose the one with most features as the source. 

* Targets cannot be adjacent to regions with cells whereas Source can. 

* Sides of the new thin volume control cannot be adjacent to region with cells. 

* Sides of one thin volume control can only be a Source to another thin volume control. 

The below example shows how to perform thin volume meshing: 

* Get the model. 

.. code-block:: python

   model = client.model 
   file_io = prime.FileIO(model) 
   res = file_io.read_pmdat(r"E:\Test\pipe2_thin_volume_mesh.pmdat", prime.FileReadParams(model = model)) 

* Create a thin volume control and set source and target. 

.. code-block:: python

   auto_mesh_params = prime.AutoMeshParams(model=model) 
   thin_vol_ctrls_ids = [] 
   thin_vol_ctrl = model.control_data.create_thin_volume_control() 
   thin_vol_ctrl.set_source_scope(prime.ScopeDefinition(model,
                                                        label_expression="thin_src")) 
   thin_vol_ctrl.set_target_scope(prime.ScopeDefinition(model,
                                                        label_expression="thin_trg")) 

* Set the thin volume mesh parameters and perform thin volume meshing. 

.. code-block:: python

   thin_vol_ctrl.set_thin_volume_mesh_params(prime.ThinVolumeMeshParams(model = model, 
                                                                        ignore_extra_source=False, 
                                                                        no_side_imprint=False)) 
   thin_vol_ctrls_ids.append(thin_vol_ctrl.id) 
   auto_mesh_params.thin_volume_control_ids = thin_vol_ctrls_ids 
   generate_vol=prime.AutoMesh(model=model) 
   part=model.get_part_by_name("pipe2") 
   result_vol= generate_vol.mesh(part.id, 
                                 auto_mesh_params) 

Layers of thin volume mesh created between the source and target surfaces with side imprints. Here, thin volume meshing imprints layers of quad on the side surface of the model and the rest of the model is  filled with tet or quad mesh.

.. figure:: ../images/Thinvol_imprints.png
  :width: 800pt
  :align: center

.. code-block:: python

   part_summary_res = part.get_summary(prime.PartSummaryParams(model = model, print_id = False, print_mesh = True)) 
   print(part_summary_res)

   Part Name: pipe2 
   Part ID: 2 

    0 Edge Zonelets 
    6 Face Zonelets 
    2 Cell Zonelets 

    0 Edge Zones 
        Edge Zone Name(s) : [] 
    1 Face Zones 
        Face Zone Name(s) : [fluid] 
    2 Volume Zones 
        Volume Zone Name(s) : [fluid.1, thin_trg] 
    3 Label(s) 
        Names: [fluid, thin_src, thin_trg] 
    Bounding box (-20 -9.94712 -9.95118) 
                 (20 9.98601 9.9862) 

    Mesh Summary: 
        2473 Nodes 
        0 Poly Faces 
        50 Quad Faces 
        2582 Tri Faces 
        2632 Faces 
        0 Poly Cells 
        0 Hex Cells 
        1154 Prism Cells
        0 Pyramid Cells 
        8865 Tet Cells 
        10019 Cells 

Layers of thin volume mesh created between the Source and Target without side imprints. Here, thin volume meshing creates specified layer of tetrahedral mesh on the side surface for the specified number of ignore rings.

.. code-block:: python

   thin_vol_ctrl.set_thin_volume_mesh_params(prime.ThinVolumeMeshParams( 
                                                                        model = model,  
                                                                        n_layers = 3,	 
                                                                        no_side_imprint=True, 
                                                                        n_ignore_rings=1, 
                                                                        ignore_extra_source=False)) 
      thin_vol_ctrls_ids.append(thin_vol_ctrl.id) 
      auto_mesh_params.thin_volume_control_ids = thin_vol_ctrls_ids 
      generate_vol=prime.AutoMesh(model=model) 
      part=model.get_part_by_name("pipe2") 
      result_vol= generate_vol.mesh(part.id,auto_mesh_params) 
      part_summary_res = part.get_summary(prime.PartSummaryParams(model = model,  
                                                                  print_id = False,  
                                                                  print_mesh = True)) 
      print(part_summary_res) 

      Part Name: pipe2 
      Part ID: 2 
      0 Edge Zonelets 
      6 Face Zonelets 
      2 Cell Zonelets 
      0 Edge Zones 
        Edge Zone Name(s) : [] 
      1 Face Zones 
        Face Zone Name(s) : [fluid] 
      2 Volume Zones 
        Volume Zone Name(s) : [fluid.1, thin_trg] 
      3 Label(s) 
        Names: [fluid, thin_src, thin_trg]  
    Bounding box (-20 -9.95603 -9.95119) 
                 (20 10 10) 

    Mesh Summary: 

        3714 Nodes 
        0 Poly Faces 
        0 Quad Faces 
        2710 Tri Faces 
        2710 Faces 
        0 Poly Cells 
        0 Hex Cells 
        3162 Prism Cells 
        150 Pyramid Cells 
        9923 Tet Cells 
        13235 Cells 

