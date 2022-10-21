.. _ref_index_automesh


******************
Volumetric Meshing 
******************

PyPrime enables you to have fully automated volume meshing. Automeshing enables you to automatically create the volume mesh using 
the different mesh elements available. Auto mesh generates the volume mesh for all computed volumetric regions of the mesh object 
(i.e. meshed topofaces). ``ansys.meshing.prime.AutoMesh`` class provides you with APIs to perform automeshing. 

You can create volume mesh with tetrahedrons from the model:

.. code:: python

    >>>     # Volume mesh with tetrahedral elements
    >>>     automesher_params = prime.AutoMeshParams(model=model, volume_fill_type=prime.VolumeFillType.TET)
    >>>     prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesher_params)
