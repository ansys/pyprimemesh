.. _ref_index_automesh:


******************
Volumetric Meshing
******************

PyPrime enables you to have fully automated volume meshing. Automeshing enables you to automatically create the volume mesh using 
the different mesh elements available. Auto mesh generates the volume mesh for all computed volumetric regions of the mesh object 
(i.e. meshed topofaces). ``ansys.meshing.prime.AutoMesh`` class provides you with APIs to perform automeshing. 

Following the computation of volumetric size field as well as generating surface mesh, you can create volume mesh with tetrahedrons 
from the model:

.. code:: python

    >>> # Volume mesh with tetrahedral elements
    >>> automesher_params = prime.AutoMeshParams(model=model, volume_fill_type=prime.VolumeFillType.TET)
    >>> automesh_result = prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesher_params)

-----------------------------------
Meshing with Polyhedrons and Prisms
-----------------------------------

The following example shows you the procedure how to:

* Create prism control and specify boundary layer setting
* Volume mesh with Polyhedral elements

.. code:: python

    >>> # Prism control
    >>> prism_control = model.control_data.create_prism_control()
    >>> face_scope = prime.ScopeDefinition(
    >>>    model=model,
    >>>    entity_type = prime.ScopeEntity.FACEZONELETS,
    >>>    label_expression="* !inlet !outlet"
    >>> )
    >>> volume_scope = prime.ScopeDefinition(
    >>>    model=model,
    >>>    entity_type = prime.ScopeEntity.VOLUME,
    >>>    label_expression="*"
    >>> )
    >>> prism_control.set_surface_scope(face_scope)
    >>> prism_control.set_volume_scope(volume_scope)
    >>> prism_control.set_growth_params(prime.PrismControlGrowthParams(model=model))
    >>>
    >>> # Volume mesh with polyhedral elements
    >>> automesher_params = prime.AutoMeshParams(
    >>>    model=model,
    >>>    volume_fill_type=prime.VolumeFillType.POLY,
    >>>    prism_control_ids=[prism_control.id]
    >>> )
    >>> automesh_result = prime.AutoMesh(model).mesh(part_id=part.id, automesh_params=automesher_params)
