.. _ref_index_controls:

********************
Controls in PyPrime
********************
 
PyPrime provides various controls to help you refine your mesh to obtain the desired accuracy while meshing. 

---------------
Sizing Control
---------------
 
When you mesh a model, you expect the mesh size to satisfy specific requirements at various locations in the mesh to provide accurate results.
You must use optimal sizes while meshing to achieve maximum simulation accuracy at minimum computational cost. 
PyPrime specifies the sizing requirements using sizing controls. The sizing controls in PyPrime  have  the following: 

* Scope 

* Maximum rate of change of size 

* Range within which the sizes should be, on or within the scope. 


PyPrime offers various sizing control types to define sizing requirements. They are: 


 * Soft Sizing: Sizes on the scope are based on a certain maximum value which should not exceed while meshing. 
 
 * Constant Sizing: Sizes on the scope are based on a certain value while meshing. 
 
 * Curvature Sizing: Sizes on the scope are based on the local curvature, with the size being small when the local curvature is large and vice versa. 

 * Proximity Sizing: Sizes are based on the closeness of surfaces or edges specified in the scope. 

 * Body of Influence Sizing: Sizes inside a closed volume scope should not cross a certain maximum value. 
 
 
----------------
Wrapper Control 
----------------

PyPrime provides wrapper control to extract a closed watertight surface used to create a volume mesh from geometry where the inputs: 

*	are not connected with overlaps 

*	have holes, leaks or gaps

*	have small features that need to be ignored or stepped over 

Wrapper is used for extracting flow regions from large assemblies, forming closed clean volumes from medical imaging and many more.


-------------
Prism Control 
-------------

Prism control helps you to control the prism mesh generation based on the face scope, volume scope and growth rate.  
Prism cells creates either quadrilateral or triangular boundary faces, or both. They can resolve a boundary layer region of a tetrahedral mesh.  
 
-----------------
Volume Control
-----------------
 
 Volume control helps you to control volume mesh zonelet (fluids, solid, dead) and elements (tetrahedrons, polyhedrons and so on).
 It allows you to define the scope and generate the various types of volume mesh. 

