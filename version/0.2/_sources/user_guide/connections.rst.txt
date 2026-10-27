.. _ref_index_connections:

***********
Connections
***********

==================
Zonelet Connection
==================

Connect operations helps you create a watertight, fully connected, surface mesh for successful volume mesh generation. Connect operation conformally connects multiple watertight volumes providing shared zonelets (and therefore connected volume mesh) between them.
The :class:`Connect <ansys.meshing.prime.Connect>` class allows you to connect the face zonelets in a part, volume, or model using various connect algorithms.
The three major operations for Zonelet Connection are Intersect, Stitch and Join. 

 - The :func:`Connect.intersect_face_zonelets() <ansys.meshing.prime.Connect.intersect_face_zonelets>` function allows you to intersect the face zonelets of the part along the intersecting faces. 

 - The :func:`Connect.stitch_face_zonelets() <ansys.meshing.prime.Connect.stitch_face_zonelets>` function allows you to stitch a set of face zonelets to another set of face zonelets along the boundary of zonelets. 

 - The :func:`Connect.join_face_zonelets() <ansys.meshing.prime.Connect.join_face_zonelets>` function allows you to join a set of face zonelets to another set of face zonelets along the overlapping faces. 


.. note::
    Connect operations support only computational mesh ( That is, mesh with reasonable size changes and quality). Faceted geometry (That is, STL-like mesh which can have extreme size changes and many sliver elements) is not supported.

The following example shows you the procedure to:

* Import model and remove geometry topology from each part
* Merge parts and check surface mesh connectivity
* Perform Join or Intersect operation on face zonelets

Import the  model and delete topo-geom entities of part.

.. code:: python

    prime.FileIO(model).read_pmdat("D:/Temp/mesh.pmdat", file_read_params=prime.FileReadParams(model))
    for part in model.parts:
        topofaces = part.get_topo_faces()
        if topofaces:
            params = prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
            part.delete_topo_entities(params)

Merge parts.

.. code:: python

    model.merge_parts(
        part_ids=[part.id for part in model.parts],
        params=prime.MergePartsParams(model)
    )
        
Check surface before connect operation.

.. code:: python
    
    diag = prime.SurfaceSearch(model)
    diag_res = diag.get_surface_diagnostic_summary(
        prime.SurfaceDiagnosticSummaryParams(
            model,
            scope=prime.ScopeDefinition(model=model, part_expression="*"),
            compute_free_edges=True,
            compute_multi_edges=True,
        )
    )

You can check the surface mesh connectivity (refer :ref:`ref_index_mesh_diagnostics` for more information).

.. code:: python

    >>> print(diag_res)

    error_code :  ErrorCode.NOERROR
    n_self_intersections :  342
    n_free_edges :  564
    n_multi_edges :  0
    n_duplicate_faces :  0

Connect face zonelets in the model.

.. note::
    Only triangular faces are supported.

.. code:: python

    join_params=prime.JoinParams(model)
    inter_params=prime.IntersectParams(model)
    join_params.tolerance = 0.1
    part_id = model.parts[0].id
    faces = model.parts[0].get_face_zonelets()

    for face in faces:
        other_faces=[other for other in faces if face != other]
        prime.Connect(model).intersect_face_zonelets(
            part_id=part_id,
            face_zonelet_ids=[face],
            with_face_zonelet_ids=other_faces,
            params=inter_params
        )
        prime.Connect(model).join_face_zonelets(
            part_id=part_id,
            face_zonelet_ids=[face],
            with_face_zonelet_ids=other_faces,
            params=join_params
        )

Check surface after connect operation.

.. code:: python

    diag_res = diag.get_surface_diagnostic_summary(diag_params)

The results of surface mesh connectivity after performing connect operation is printed below:

.. code:: python

    >>> print(diag_res)

    error_code :  ErrorCode.NOERROR
    n_self_intersections :  0
    n_free_edges :  448
    n_multi_edges :  9
    n_duplicate_faces :  0


=========================
Topology Based Connection
=========================

The :class:`Scaffolder <ansys.meshing.prime.Scaffolder>` class allows you to provide connection using faceted geometry and topology. Also, handles the gaps and mismatches in the geometry.
Topology based connection creates shared topoedges between neighbouring topofaces. Hence, you can create connected mesh between topofaces.

.. note::
  Connectivity cannot be shared across multiple parts.

.. code:: python

    # Merge parts
    model.merge_parts(
        part_ids=[part.id for part in model.parts],
        params=prime.MergePartsParams(model)
    )

    # Scaffold topofaces
    params = prime.ScaffolderParams(
        model=model,
        absolute_dist_tol=0.01,
        intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
        constant_mesh_size=0.1
    )

    scaffolder = prime.Scaffolder(model, part.id)
    res = scaffolder.scaffold_topo_faces_and_beams(
        topo_faces=part.get_topo_faces(),
        topo_beams=[],
        params=params
    )

You can check the number of topofaces failed in scaffold operation by printing the results:

.. code:: python

    >>> print(res)

    n_incomplete_topo_faces :  0
    error_code :  ErrorCode.NOERROR
