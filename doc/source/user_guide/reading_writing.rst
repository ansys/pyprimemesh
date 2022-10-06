Reading and Writing Files in PyPrime 
-------------------------------------
PyPrime allows you to import and export different files. PyPrime supports the reading and writing of mesh files and size field files. 
PyPrime imports CAD files, Fluent meshing files and Prime database files. 
Also, exports Fluent meshing files with .msh,.CAS, .CDB extensions. You can save and write the files in PyPrime which can be used later. 

--------------
Importing CAD
--------------

PyPrime supports importing CAD files and appending of CAD files in a model.
``FileIO.import_cad(filename,params)`` allows you to import the CAD files in PyPrime and set the options for importing the files.
This function also allows you to append a CAD model with an existing model. 
You may have to specify the import route for the CAD files depending on the imported files. 
CAD import routes available in PyPrime are Program Controlled, Native, SpaceClaim and Workbench. 

 * Program Controlled: Automatically choose the best route based on the CAD format. Program Controlled uses Native as available, SCDM for scdoc and Workbench for all the other formats.  
  
 * Native: Imports selected natively supported formats like ACIS ``(*.sat, *.sab)``, Parasolid ``(*.x_t, *.x_b)``, JTOpen ``(*.jt, *.plmxml)``, STL ``(*.stl)``. 
 
 * SpaceClaim:  Uses SCDM to import supported CAD files from the SpaceClaim reader. Only Windows platform support the SpaceClaim file import.  
 
 * Workbench: Uses Workbench to import supported CAD files from the Workbench reader. 
 