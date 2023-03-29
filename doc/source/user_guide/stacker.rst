=======
Stacker
=======
Stacker creates a volume mesh on 2.5 D models, stacking faces or edge zonelets one above the other in layers. 
Stacker stacks each of the input topovolumes individually. A geometry is stackable only when there is a direction called stacking direction,
to which all surfaces are either perpendicular or parallel. 
A 2.5 D or stackable geometry is any closed volume or set of closed volumes that can be obtained by successive extrusion 
of a series of 2D geometries, along the area normal of the 2D geometries. 

Stacker workflow involves the following:

-	create imprints of model edges on the base face 

- meshes the imprinted base face 

- extrudes the base face mesh at the selected origin by stacking the face in layers one over the other along the specified direction to generate a volume mesh.



create_base_face(self, topo_volume_ids : Iterable[int], params : MeshStackerParams) -> MeshStackerResults creates a face at the origin perpendicular 
to the specified direction.
Also, imprints model edges on the face, repairs the edges within the lateral_defeature_tolerance and duplicates the size controls on the base face. 
Stacker then performs surface meshing on the base face. 

stack_base_face(self, base_face_ids : Iterable[int], topo_volume_ids : Iterable[int], params : MeshStackerParams) -> MeshStackerResult creates the volume mesh stacking
the meshed faced one over the other forming layers along the given direction. stacking_defeature_tolerance provides the distance tolerances between the stacker layers.
max_offset_size provides the maximum stack size allowed for stacking. Size_control_ids allow you to provide the size controls for the stacker. 
delete_base  provides you an option to delete the base face after stacking. 
Also, MeshStackerParams has parameters like origin to specify the origin coordinates of the Stacker. direction specifies the direction vector of the stacker.

The below example shows how to perform stacking on a 2.5 D model:

1. Start the PyPrimeMesh client and read the model.

.. code-block:: python

    import ansys.meshing.prime  as prime
    client = prime.launch_prime(timeout=20) 
    model = client.model
    file_io = prime.FileIO(model)
    res = file_io.import_fluent_meshing_meshes([r"E:\Test\thin_disc_cadfacets.msh"], prime.ImportFluentMeshingMeshParams(model = model))
    print (res)
    print (model)
    
2. Get the part by name.   

.. code-block:: python

    part = model.get_part_by_name("thin_disc")
    print (part)
    
3.	Set the global sizing parameters.

.. code-block:: python

  model.set_global_sizing_params(prime.GlobalSizingParams(model=model, min=0.15, max=0.5, growth_rate=1.2))
  deleted = model.delete_volumetric_size_fields(model.get_active_volumetric_size_fields())
  print (deleted)
  
4.	Set the stacker parameters. 

.. code-block:: python

  sweeper = prime.VolumeSweeper(model)
  stacker_params = prime.MeshStackerParams(
        origin = [2.02832, 0.0, -0.122448], direction = [0., 1., 0.], lateral_defeature_tolerance = 0.1, stacking_defeature_tolerance = 0.1,
        max_offset_size = 0.5, delete_base = True, size_control_ids = [])
  print (stacker_params)
  
 
.. note::
  lateral_defeature_tolerance and stacking_defeature_tolerance values should be set to (global min size/4).
 
5.	Create base face for stacker.

.. code-block:: python
   
  createbase_results = sweeper.create_base_face(part.id, part.get_topo_volumes(), stacker_params)
  print (createbase_results)

6.	Compute volumetric size field. 

.. code-block:: python
  
  baseFaces = createbase_results.base_face_ids
  size_control_ids_new = createbase_results.size_control_ids
  SF1 = prime.SizeField(model)
  computed_volume = SF1.compute_volumetric(size_control_ids_new, prime.VolumetricSizeFieldComputeParams(model))
  print (computed_volume)
  
7.	Perform surface meshing on the base face of the model.

.. code-block:: python

  surfer = prime.Surfer(model)
  meshbase_result = surfer.mesh_topo_faces(part.id, baseFaces, params = prime.SurferParams( model = model,size_field_type = prime.SizeFieldType.VOLUMETRIC, generate_quads = True))
  print (meshbase_result)
  
8.	Delete the size controls and existing size fields. 

.. code-block:: python

 if len(size_control_ids_new) > 0 :
        model.control_data.delete_controls(size_control_ids_new)
 SF = model.delete_volumetric_size_fields(model.get_active_volumetric_sizefields())
 print (SF)
 
9. Stack the base face.

.. code-block:: python
 
 stackbase_results = sweeper.stack_base_face(part.id, baseFaces, part.get_topo_volumes(), stacker_params)
  

--------------
Best Practices
--------------

The best practices to be considered while working with stacker are:

-	Stacker uses global max size by default if you are not providing the max size.

------------
Limitations
------------

Stacker has the following limitations:

-	Stacker works only on 2.5D models.

- Stacker allows only conformal meshing.	


    
    
    
