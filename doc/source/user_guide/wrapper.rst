========
Wrapper
========


PyPrimeMesh provides wrapper control to extract a closed watertight surface used to create a volume mesh from geometry where the inputs: 

 - are not connected with overlaps 
 - have holes, leaks or gaps. 
 - have small features that need to be ignored or stepped over 
 
Wrapper allows you to extract flow regions from large assemblies, form closed clean volumes from medical imaging and many more.

The procedure to perform wrapping on a model are as follows:

1. Import geometry.

.. code:: python

      file_io=prime.FileIO(model)
      res = file_io.import_fluent_meshing_meshes([os.path.join(os.getenv("INPUT_FILES"), "PyPrime", "cylinder_with_flange_fr_prime.msh.gz")], prime.ImportFluentMeshingMeshParams(model = model) )
   
2. Define sizing and controls.

.. code:: python

    model.set_global_sizing_params(prime.GlobalSizingParams(model,  min = 0.2, max = 1., growth_rate = 1.2))
    sfparams = model.get_global_sizing_params()
    
3.	Define curvature control.

.. code:: python

    size_control = model.control_data.create_size_control(sizing_type=prime.SizingType.CURVATURE)
    size_control.set_curvature_sizing_params(prime.CurvatureSizingParams(model = model, min=0.2, max=1., normal_angle=18.0))
    size_control.set_suggested_name("global") 
    size_control.set_scope(prime.ScopeDefinition(model = model, part_expression="*" ))
    
4.	Define the material points.

.. code:: python

   model.material_point_data.create_material_point(suggested_name = "Fluid", coords = [20.0, -76.0, -6.0],  params = prime.CreateMaterialPointParams(model = model, type = prime.MaterialPointType.LIVE))
   
5.	Create the wrapper control.

.. code:: python

   wrapper_control = model.control_data.create_wrapper_control()
   wrapper_control.set_suggested_name("cyl_flange_control")
   wrapper_control.set_suggested_wrapper_part_name("Wrap_cyl_flange")
   wrapper_control.set_geometry_scope(prime.ScopeDefinition(model = model, part_expression = "flange,pipe", entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS))
   wrapper_control.set_live_material_points(["Fluid"])
   
6.	Extract features.

.. code:: python

   features = prime.FeatureExtraction(model)
   feature_scope = prime.ScopeDefinition(model = model, part_expression="*")
   face_zonelets_prime_array = model.control_data.get_part_zonelets(scope= feature_scope)
   for item in face_zonelets_prime_array:
   res = features.extract_features_on_face_zonelets(part_id = item.part_id, face_zonelets=item.face_zonelets, params=prime.ExtractFeatureParams(model= model, feature_angle=40.0, label_name="extractedfeatures", replace=True))

7.	Define the scope for feature recovery.

.. code:: python

   feature_params = prime.FeatureRecoveryParams(model = model, scope = prime.ScopeDefinition(model = model, part_expression="*", label_expression="extractedfeatures" ))
   wrapper_control.set_feature_recoveries([feature_params])

8.	Wrap the model.

.. code:: python

   wrapper = prime.Wrapper(model = model)
   wrap_params = prime.WrapParams(model, size_control_ids=[size_control.id])
   res=wrapper.wrap(wrapper_control_id=wrapper_control.id, params=wrap_params)
   wrapper_part = model.get_part(res.id)
   
9.	Apply diagnostics to compute free edges, multi edges, self-intersections, duplicate faces.

.. code:: python

   diag = prime.SurfaceSearch(model)
   diag_params = prime.SurfaceDiagnosticSummaryParams(model, scope = prime.ScopeDefinition(model=model, part_expression="wrap"), compute_free_edges= True, compute_multi_edges= True, compute_self_intersections=True, compute_duplicate_faces=True)
   diag_res = diag.get_surface_diagnostic_summary(diag_params)

10.	Apply the quality as per your requirement and remesh the model.

