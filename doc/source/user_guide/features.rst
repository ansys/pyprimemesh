.. _ref_index_features:

*********
Features
*********

========
Connect
========

The :class:`Connect <ansys.meshing.prime.Connect>` class allows you to connect the face zonelets in a part, volume, or model. Connect performs both faceted connections and topology-based connections on a surface. 

.. note::
    Connect operations like Join, Stitch and Intersect supports only computational mesh (mesh with reasonable size). Faceted mesh is not supported. 


Zonelet Connections
--------------------

Zonelet Connections connect the face zonelets using surface meshing. The three major operations for Zonelet Connection are Intersect, Stitch and Join. 

 - :func:`Connect.intersect_face_zonelets() <ansys.meshing.prime.Connect.intersect_face_zonelets>`: Allows you to intersect the face zonelets of the part along the intersecting faces. 

 - :func:`Connect.stitch_face_zonelets() <ansys.meshing.prime.Connect.stitch_face_zonelets>`: Allows you to stitch a set of face zonelets to another set of face zonelets along the boundary of zonelets. 

 - :func:`Connect.join_face_zonelets() <ansys.meshing.prime.Connect.stitch_face_zonelets>`: Allows you to join a set of face zonelets to another set of face zonelets along the overlapping faces. 


Topology Based Connections
---------------------------

Topology Based Connections allows you to connect the topofaces, topoedges and so on.

Scaffolding
^^^^^^^^^^^

Scaffolding creates conformal meshes on shared topologies to provide a better connection between the topofaces.
The :class:`Scaffolder <ansys.meshing.prime.Scaffolder>` class allows you to provide connection using faceted geometry and topology, handling the gaps and mismatches in the geometry.
