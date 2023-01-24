.. _ref_index_wrapper:


****************
Surface Wrapping
****************


PyPrimeMesh provides operations to extract a closed watertight surface used to create a volume mesh from geometry where the inputs: 

 - are not connected with overlaps 
 - have holes, leaks or gaps. 
 - have small features that need to be ignored or stepped over 
 
The :class:`Wrapper <ansys.meshing.prime.Wrapper>` allows you to extract flow regions from large assemblies, form closed clean volumes from medical imaging and many more.

The procedure to perform surface wrapping on a model are as follows:

1. Import geometry.

.. code:: python

   model = prime_client.model
   input_file = r"D:/PyPrimeMesh/cylinder_with_flange.pmdat"
   file_io = prime.FileIO(model)
   file_io.read_pmdat(input_file, prime.FileReadParams(model=model))

2. Define global sizing parameters and size controls with curvature refinement. Sizes will be used for Wrapper Octree construction.

.. code:: python

   model.set_global_sizing_params(prime.GlobalSizingParams(model=model, min=0.2, max=3., growth_rate=1.2))

   size_control = model.control_data.create_size_control(sizing_type=prime.SizingType.CURVATURE)
   size_control.set_curvature_sizing_params(prime.CurvatureSizingParams(model=model, min=0.2, max=1., normal_angle=18.0))
   size_control.set_suggested_name("global")
   size_control.set_scope(prime.ScopeDefinition(model=model, part_expression="*"))

3.	Define the material points. Material points are used to define fluid regions or seal regions depending on the status live/dead.
A 3D coordinate describes the position of the material point.

.. code:: python

   model.material_point_data.create_material_point(
      suggested_name="Mpt",
      coords=[20.0, -76.0, -6.0],
      params=prime.CreateMaterialPointParams(
         model=model,
         type=prime.MaterialPointType.LIVE
      )
   )

4.	Create the wrapper control. Scope refers to which entities should be wrapped.

.. code:: python

   wrapper_control = model.control_data.create_wrapper_control()
   wrapper_control.set_suggested_name("cyl_flange_control")
   wrapper_control.set_suggested_wrapper_part_name("Wrap_cyl_flange")
   wrapper_control.set_geometry_scope(prime.ScopeDefinition(model=model, part_expression="flange,pipe", entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS))
   wrapper_control.set_live_material_points(["Mpt"])

5.	Extract features with angle and face zonelets boundary for feature capture.

.. code:: python

   features = prime.FeatureExtraction(model)
   feature_scope = prime.ScopeDefinition(model=model, part_expression="*")
   face_zonelets_prime_array = model.control_data.get_part_zonelets(scope=feature_scope)
   for item in face_zonelets_prime_array:
      features.extract_features_on_face_zonelets(
         part_id=item.part_id,
         face_zonelets=item.face_zonelets,
         params=prime.ExtractFeatureParams(
            model=model,
            feature_angle=40.0,
            label_name="extracted_features",
            replace=True
         )
      )

6.	Define the scope and refinement controls for feature recovery.

.. code:: python

   feature_params = prime.FeatureRecoveryParams(
      model=model,
      scope=prime.ScopeDefinition(
         model=model,
         part_expression="*",
         label_expression="extracted_features"
      )
   )
   wrapper_control.set_feature_recoveries([feature_params])

7.	Wrap the model.

.. code:: python

   wrapper = prime.Wrapper(model=model)
   wrap_params = prime.WrapParams(model, size_control_ids=[size_control.id])
   res=wrapper.wrap(wrapper_control_id=wrapper_control.id, params=wrap_params)
   wrapper_part = model.get_part(res.id)

8.	Apply diagnostics to compute free edges, multi edges, self-intersections, duplicate faces after wrap. (visit :ref:`ref_index_mesh_diagnostics` section for more information)

9. Remesh the model. (visit :ref:`ref_index_surfer` section for more information)

.. Note::
   You can import Fluent Meshing's size field file for remesh. (visit :ref:`ref_index_reading_writing` section for more information)

.. code:: python

   size_control2 = model.control_data.create_size_control(sizing_type=prime.SizingType.HARD)
   size_control2.set_hard_sizing_params(prime.HardSizingParams(model=model, min=0.8))
   size_control2.set_suggested_name("sz2")
   size_control2.set_scope(prime.ScopeDefinition(model=model, part_expression="*", entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS))

   SF1 = prime.SizeField(model)
   SF1.compute_volumetric([size_control2.id], prime.VolumetricSizeFieldComputeParams(model=model, enable_multi_threading=False))

   fz1 = wrapper_part.get_face_zonelets()
   ez1 = wrapper_part.get_edge_zonelets_of_label_name_pattern(
      label_name_pattern="___wrapper_feature_path___",
      name_pattern_params=prime.NamePatternParams(model=model)
   )
   rem1 = prime.Surfer(model)
   surfer_params = rem1.initialize_surfer_params_for_wrapper()
   surfer_params.size_field_type = prime.SizeFieldType.VOLUMETRIC

   rem1.remesh_face_zonelets(wrapper_part.id, face_zonelets=fz1, edge_zonelets=ez1, params = surfer_params)

10. Improve surface quality and resolve connectivity issues.

.. code:: python

   wrapper.improve_quality(part_id=wrapper_part.id, params=prime.WrapperImproveQualityParams(model=model, target_skewness=0.9))

