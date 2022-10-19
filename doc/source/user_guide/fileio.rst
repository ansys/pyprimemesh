.. _ref_index_reading_writing:


*************************************
Reading and Writing Files in PyPrime 
*************************************

The :class:`FileIO <ansys.meshing.prime.FileIO>` class is used for all file based data exchanges.

====================
Native PMDAT Format
====================

PMDAT is the native file format for Prime that contains all data associated with the active model.

This includes, geometry, mesh, topology, controls, labels and zones.

The model data can be read from and written to this format using :func:`FileIO.read_pmdat() <ansys.meshing.prime.FileIO.read_pmdat>` and
:func:`FileIO.write_pmdat() <ansys.meshing.prime.FileIO.write_pmdat>` with parameters defined in the
:class:`FileReadParams <ansys.meshing.prime.FileReadParams>` and :class:`FileWriteParams <ansys.meshing.prime.FileWriteParams>` classes respectively.

.. code:: python
    
    >>> from ansys.meshing import prime
    
    Start prime and get the model
    
    >>> prime_client = prime.launch_prime()
    >>> model = prime_client.model
    
    Download and read an example pmdat file
    
    >>> mixing_elbow = prime.examples.download_elbow_pmdat()
    >>> params = prime.FileReadParams(model=model)
    >>> prime.FileIO(model).read_pmdat(file_name=mixing_elbow, file_read_params=params)

==============
Importing CAD
==============

PyPrime supports importing CAD files and appending of CAD files in a model.
``FileIO.import_cad(filename,params)`` allows you to import the CAD files in PyPrime and set the options for importing the files.
This function also allows you to append a CAD model with an existing model. 
You may have to specify the import route for the CAD files depending on the imported files. 
CAD import routes available in PyPrime are Program Controlled, Native, SpaceClaim and Workbench. 

 * Program Controlled: Automatically choose the best route based on the CAD format. Program Controlled uses Native as available, SCDM for scdoc and Workbench for all the other formats.  
  
 * Native: Imports selected natively supported formats like FMD ``(*.fmd)``,ACIS ``(*.sat, *.sab)``, Parasolid ``(*.x_t, *.x_b)``, JTOpen ``(*.jt, *.plmxml)``, STL ``(*.stl)``. 
 
 * SpaceClaim:  Uses SCDM to import supported CAD files from the SpaceClaim reader. Only Windows platform support the SpaceClaim file import.  
 
 * Workbench: Uses Workbench to import supported CAD files from the Workbench reader. 
 
 
When deploying scripts using SpaceClaim or Workbench CAD readers, ensure that the CAD configuration and in application defaults are consistent
in the deployed environment. 

Refer `CAD Support <https://www.ansys.com/it-solutions/platform-support>`_ document to view the CAD supported for Workbench route on different platforms. 


**Note**: You must install and configure Workbench CAD Readers/Plug-ins (Ansys Geometry Interfaces) while installing Ansys Workbench. 
 

Part Management and Creation
----------------------------

PyPrime has options for part management within the product structure while importing a CAD (Computer Aided Design) model. 
The CAD model is the top in product hierarchy. A CAD model can have one or more CAD assemblies. 
The CAD assembly or sub-assembly has different CAD parts.
The CAD part has bodies or other geometric entities. A typical CAD product structure is as follows: 

.. figure:: ../images/cad_structure.png
    :width: 100pt
    :align: center

    **Example CAD structure**

The :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` class decides whether to create a part per:

 * Model

 * Assembly

 * Part 

 * Body


Model
^^^^^ 

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`MODEL <ansys.meshing.prime.PartCreationType.MODEL>`, a single part is created that inherits its name from the CAD model name. 
The number of zones within the part is identical to the number of bodies within the CAD model.  As below:

.. figure:: ../images/creation_model.png
    :width: 200pt
    :align: center

    **Part creation by Model (from SpaceClaim CAD structure to Prime part structure)**

Assembly 
^^^^^^^^^^^^^^^^^^^^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`ASSEMBLY <ansys.meshing.prime.PartCreationType.ASSEMBLY>`, a part per CAD assembly is created where the part name is inherited from the CAD assembly name.
The number of zones within each part is identical to the number of bodies within the CAD assembly.  As below:

.. figure:: ../images/creation_assembly.png
    :width: 200pt
    :align: center

    **Part creation by Assembly (from SpaceClaim CAD structure to Prime part structure)**

Part 
^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`PART <ansys.meshing.prime.PartCreationType.PART>`, a part per CAD part is created that inherits the part name from the CAD part name. 
The number of zones within a part is identical to the number of bodies within the CAD part.  As below:

.. figure:: ../images/creation_part.png
    :width: 200pt
    :align: center

    **Part creation by Part (from SpaceClaim CAD structure to Prime part structure)**

Body
^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`BODY <ansys.meshing.prime.PartCreationType.BODY>`, a part per CAD body is created that inherits the part name from the CAD body name. 
The number of parts is identical to the number of bodies.  As below:

.. figure:: ../images/creation_body.png
    :width: 200pt
    :align: center

    **Part creation by Body (from SpaceClaim CAD structure to Prime part structure)**

==========================================
Importing and Exporting Solver Mesh Files
==========================================

To be added.

=====================================
Reading and Writing Size Field Files
=====================================

To be added.
