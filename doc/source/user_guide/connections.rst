.. _ref_index_connections:

***********
Connections
***********

===================
Zonelet Connection
===================

The :class:`Connect <ansys.meshing.prime.Connect>` class allows you to connect the face zonelets in a part, volume, or model using various connect algorithms.
The three major operations for Zonelet Connection are Intersect, Stitch and Join. 

 - :func:`Connect.intersect_face_zonelets() <ansys.meshing.prime.Connect.intersect_face_zonelets>`: Allows you to intersect the face zonelets of the part along the intersecting faces. 

 - :func:`Connect.stitch_face_zonelets() <ansys.meshing.prime.Connect.stitch_face_zonelets>`: Allows you to stitch a set of face zonelets to another set of face zonelets along the boundary of zonelets. 

 - :func:`Connect.join_face_zonelets() <ansys.meshing.prime.Connect.stitch_face_zonelets>`: Allows you to join a set of face zonelets to another set of face zonelets along the overlapping faces. 


.. note::
    Connect operations support only computational mesh (mesh with reasonable size). Faceted mesh is not supported. 


==========================
Topology Based Connection
==========================

The :class:`Scaffolder <ansys.meshing.prime.Scaffolder>` class allows you to provide connection using faceted geometry and topology, handling the gaps and mismatches in the geometry.
Topology based connection creates conformal meshes on shared topologies to provide a better connection between the topofaces.

.. note::
    Connectivity cannot be shared across multiple parts. 

.. code:: python

    >>> # Merge parts
    >>> model.merge_parts(
    >>>     part_ids=[part.id for part in model.parts],
    >>>     params=prime.MergePartsParams(model)
    >>> )
    
    >>> # Scaffold topofaces
    >>> params = prime.ScaffolderParams(
    >>>     model=model, 
    >>>     absolute_dist_tol=0.01,
    >>>     intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
    >>>     constant_mesh_size=0.1
    >>> )
    >>> scaffolder = prime.Scaffolder(model, part.id)
    >>> res = scaffolder.scaffold_topo_faces_and_beams(
    >>>     topo_faces=part.get_topo_faces(), 
    >>>     topo_beams=[], 
    >>>     params=params
    >>> )
    >>> print(res)

    n_incomplete_topo_faces :  0
    error_code :  ErrorCode.NOERROR
