.. _ref_index_features:

*********
Features
*********

--------
Connect 
--------
Connect allows you to connect the face zonelets in a part, volume, or model. Connect performs both faceted connections and topology-based connections on a surface. 
  
**Note:** Connect operations like Join, Stitch and Intersect supports only computational mesh (mesh with reasonable size). Faceted mesh is not supported. 

 
Zonelet Connections
--------------------

Zonelet Connections connect the face zonelets using surface meshing. The three major operation for Zonelet Connection are Intersect, Stitch and Join. 

 - **Intersect**: Allows you to intersect the face zonelets of the part along the intersecting faces. 

 - **Stitch**: Allows you to stitch a set of face zonelets to another set of face zonelets along the boundary of zonelets. 

 - **Join**: Allows you to join a set of face zonelets to another set of face zonelets along the overlapping faces. 
 
 
  
Topology Based Connections
---------------------------
 
Topology Based Connections allows you to connect the topofaces, topoedges and so on. 
 
Scaffolding
^^^^^^^^^^^
 
Scaffolding creates conformal meshes on shared topologies to provide a better connection between the topofaces.
Scaffolding allows you to provide connection using faceted geometry and topology, handling the gaps and mismatches in the geometry.

----
IGA
----  
Pyprime provides Isogeometric Analysis (IGA), a finite element technology that uses splines from Computer Aided Design (CAD) to describe the geometry and the solution field. 
IGA enables you to have a better integration of CAD and its analysis.  IGA supports only LS- DYNA. IGA provides more accurate geometry description, higher predictive accuracy. 
The two different methods of IGA are Boundary Fitted Solid Splines and Uniform Trimmed Solid Splines. 

 

Boundary Fitted Solid Splines extracts control points and body fitted solid splines based on the Structured Hexahedral mesh (Structured Hex Mesh Fitting) or 
Triangular Surface Mesh (Genus Zero Fitting), which is provided as an input for IGA solver in LS-DYNA​. The two methods used for extracting control points and body fitted splines are as follows: 

**Structured Hexmesh Fitting​**: Structured Hexmesh Fitting​ extracts control points and body fitted splines based on structured hexahedral mesh​ that is provided as input for the IGA solver in LS-DYNA. 