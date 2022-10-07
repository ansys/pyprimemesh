*******************
Meshing in PyPrime
*******************

PyPrime uses Prime meshing engine that empowers the meshing needs of your application. 
Prime supports single process, multi-threaded and distributed parallel modes. You can choose any mode based on your requirements. 
PyPrime allows you to generate a tetrahedral, hexcore, or hybrid volume mesh from an existing boundary mesh. 
Also, generates tetrahedral, hexcore, or hybrid volume mesh based on meshing objects from a faceted geometry. 

---------------
Surface Meshing 
---------------

PyPrime enables you to perform surface meshing using different surface meshing algorithms on topofaces or face zonelets.
``ansys.meshing.prime.Surfer(model, part_id)`` provides information on APIs used for surface meshing. 
Surface meshing considers many parameters like size field type, min size, max size, growth rate, transition type while meshing face zonelets or topofaces. 