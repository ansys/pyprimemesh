.. _ref_index_connections:

***********
Connections
***********

==================
Zonelet connection
==================

Connect operations help you to create a watertight, fully connected surface mesh for successful volume mesh generation.
Connect operations conformally connect multiple watertight volumes providing shared zonelets (and therefore connected
volume mesh) between them. The :class:`Connect <ansys.meshing.prime.Connect>` class allows you to connect the face zonelets
in a part, volume, or model using various connect algorithms.

There are three major operations for zonelet connections: 

 - The :func:`Connect.intersect_face_zonelets() <ansys.meshing.prime.Connect.intersect_face_zonelets>` method allows you
   to intersect the face zonelets of the part along the intersecting faces. 

 - The :func:`Connect.stitch_face_zonelets() <ansys.meshing.prime.Connect.stitch_face_zonelets>` method allows you to
   stitch a set of face zonelets to another set of face zonelets along the boundary of zonelets. 

 - The :func:`Connect.join_face_zonelets() <ansys.meshing.prime.Connect.join_face_zonelets>` method allows you to join
   a set of face zonelets to another set of face zonelets along the overlapping faces. 


.. note::
    Connect operations support only computational mesh, which is mesh with reasonable size changes and quality.
    Faceted geometry, which is STL-like mesh that can have extreme size changes and many sliver elements, is not supported.


The following example shows how to perform these steps:

* Import model and remove geometry topology from each part.
* Merge parts and check surface mesh connectivity.
* Perform the join or intersect operation on face zonelets.

Import the model and delete topo-geometric entities from each part:

.. code:: python

    prime.FileIO(model).read_pmdat(
        "D:/Temp/mesh.pmdat", file_read_params=prime.FileReadParams(model)
    )
    for part in model.parts:
        topofaces = part.get_topo_faces()
        if topofaces:
            params = prime.DeleteTopoEntitiesParams(
                model, delete_geom_zonelets=True, delete_mesh_zonelets=False
            )
            part.delete_topo_entities(params)


Merge the parts.

.. code:: python

    model.merge_parts(
        part_ids=[part.id for part in model.parts], params=prime.MergePartsParams(model)
    )

Check the surface before performing the connect operation.

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


For more information on checking the surface mesh connectivity, see :ref:`ref_index_mesh_diagnostics`.

Print the results of the surface mesh connectivity before performing the connect operation:

.. code:: pycon

    >>> print(diag_res)

    error_code :  ErrorCode.NOERROR
    n_self_intersections :  342
    n_free_edges :  564
    n_multi_edges :  0
    n_duplicate_faces :  0


Connect face zonelets in the model:

.. note::
    Only triangular faces are supported.

.. code:: python

    join_params = prime.JoinParams(model)
    inter_params = prime.IntersectParams(model)
    join_params.tolerance = 0.1
    part_id = model.parts[0].id
    faces = model.parts[0].get_face_zonelets()

    for face in faces:
        other_faces = [other for other in faces if face != other]
        prime.Connect(model).intersect_face_zonelets(
            part_id=part_id,
            face_zonelet_ids=[face],
            with_face_zonelet_ids=other_faces,
            params=inter_params,
        )
        prime.Connect(model).join_face_zonelets(
            part_id=part_id,
            face_zonelet_ids=[face],
            with_face_zonelet_ids=other_faces,
            params=join_params,
        )


Check the surface after performing the connect operation:

.. code:: python

    diag_res = diag.get_surface_diagnostic_summary(diag_params)


Print the results of the surface mesh connectivity after performing the connect operation:

.. code:: pycon

    >>> print(diag_res)

    error_code :  ErrorCode.NOERROR
    n_self_intersections :  0
    n_free_edges :  448
    n_multi_edges :  9
    n_duplicate_faces :  0


=========================
Topology-based connection
=========================

The :class:`Scaffolder <ansys.meshing.prime.Scaffolder>` class allows you to provide connection
using faceted geometry and topology. This class also handles the gaps and mismatches in the geometry.

Topology-based connection creates shared topoedges between neighbouring topofaces. Hence, you can
create connected mesh between topofaces.

.. note::
  Connectivity cannot be shared across multiple parts.

This code merges parts and scaffold topofaces:

.. code:: python

    # Merge parts
    model.merge_parts(
        part_ids=[part.id for part in model.parts], params=prime.MergePartsParams(model)
    )

    # Scaffold topofaces
    params = prime.ScaffolderParams(
        model=model,
        absolute_dist_tol=0.01,
        intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
        constant_mesh_size=0.1,
    )

    scaffolder = prime.Scaffolder(model, part.id)
    res = scaffolder.scaffold_topo_faces_and_beams(
        topo_faces=part.get_topo_faces(), topo_beams=[], params=params
    )

This code prints the results so that you can check the number of topofaces that failed
in the scaffold operation:

.. code:: pycon

    >>> print(res)

    n_incomplete_topo_faces :  0
    error_code :  ErrorCode.NOERROR

