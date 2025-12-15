.. _ref_index_reading_writing:


*************************
Reading and Writing Files
*************************

The :class:`FileIO <ansys.meshing.prime.FileIO>` class is used for all file based data exchanges.


===================
Native PMDAT Format
===================

PMDAT is the native file format for PyPrimeMesh that contains all data associated with the active model.

This includes, geometry, mesh, topology, controls, labels and zones.

The model data can be read from and written to this format using the :func:`FileIO.read_pmdat() <ansys.meshing.prime.FileIO.read_pmdat>` and
:func:`FileIO.write_pmdat() <ansys.meshing.prime.FileIO.write_pmdat>` functions with parameters defined in the
:class:`FileReadParams <ansys.meshing.prime.FileReadParams>` and :class:`FileWriteParams <ansys.meshing.prime.FileWriteParams>` classes respectively.

.. code:: python

    from ansys.meshing import prime

    # Start Ansys Prime Server and get the model
    prime_client = prime.launch_prime()
    model = prime_client.model

    # Download and read an example pmdat file
    mixing_elbow = prime.examples.download_elbow_pmdat()
    params = prime.FileReadParams(model=model)
    prime.FileIO(model).read_pmdat(file_name=mixing_elbow, file_read_params=params)

.. tip::
    Files can be read or imported based on file extension using the :func:`Mesh.read() <ansys.meshing.prime.lucid.Mesh.read>` in Lucid API. The method supports PyPrimeMesh's native format, various CAD formats and solver mesh files. 


=============
Importing CAD
=============

The :func:`FileIO.import_cad() <ansys.meshing.prime.FileIO.import_cad>` function allows you to import CAD files and set parameters for importing files using the :class:`ImportCadParams <ansys.meshing.prime.ImportCadParams>` class.  


CAD Reader Routes
-----------------

You may require to specify the import route for the CAD files using the :class:`CadReaderRoute <ansys.meshing.prime.CadReaderRoute>` class.

.. code:: python

    params = prime.ImportCadParams(model=model, cad_reader_route=prime.CadReaderRoute.SPACECLAIM)
    prime.FileIO(model).import_cad(file_name=mixing_elbow, params=params)

Alternatively, you can use :class:`Mesh <ansys.meshing.prime.lucid.Mesh>` class in Lucid API:

.. code:: python

    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(file_name=mixing_elbow, cad_reader_route=prime.CadReaderRoute.SPACECLAIM)

CAD import routes available in PyPrimeMesh are Program Controlled, Native, SpaceClaim and Workbench.

 * Program Controlled: Automatically choose the best route based on the CAD format. Program Controlled uses Native as available, SCDM for scdoc and Workbench for all the other formats.  

 * Native: Imports selected natively supported formats like FMD ``(*.fmd)``, ACIS ``(*.sat, *.sab)``, Parasolid ``(*.x_t, *.x_b)``, JTOpen ``(*.jt, *.plmxml)``, STL ``(*.stl)``. 

 * SpaceClaim: Uses SCDM to import supported CAD files from the SpaceClaim reader. Only Windows platform support the SpaceClaim file import.  

 * Workbench: Uses Workbench to import supported CAD files from the Workbench reader.

Refer `CAD Support <https://www.ansys.com/it-solutions/platform-support>`_ document to view the CAD supported for Workbench route on different platforms. 

.. note::
    When deploying scripts using SpaceClaim or Workbench CAD readers, ensure that the CAD configuration and in-application defaults 
    are consistent in the deployed environment.

.. note::
    You must install and configure Workbench CAD Readers or Plug-ins (Ansys Geometry Interfaces) while installing Ansys Workbench. 


Appending CAD files
-------------------

The :attr:`ImportCadParams.append <ansys.meshing.prime.ImportCadParams.append>` attribute allows you to append a CAD file to the model. 

.. code:: python

    params = prime.ImportCadParams(model=model, append=True)
    prime.FileIO(model).import_cad(file_name="cad_to_append.scdoc", params=params)

Alternatively, you can use :class:`Mesh <ansys.meshing.prime.lucid.Mesh>` class in Lucid API:

.. code:: python

    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read("cad_to_append.scdoc", append=True)

Parametric CAD
--------------

Parametric CAD update can be used while importing CAD files that have parameters defined which can be accessed by the Workbench CAD readers.  

To get existing CAD parameters while importing:

.. code:: python

    params = prime.ImportCadParams(model=model)
    params.cad_reader_route = prime.CadReaderRoute.WORKBENCH
    result = prime.FileIO(model).import_cad(file_name="parametric_cad.scdoc", params=params)

.. code:: python

    >>> print(result.cad_parameters)

    {'my_param': 1}

To set parameters used for import:

.. code:: python

    params = prime.ImportCadParams(model=model)
    params.cad_reader_route = prime.CadReaderRoute.WORKBENCH
    params.cad_update_parameters = {'my_param': 2}
    result = prime.FileIO(model).import_cad(file_name="parametric_cad.scdoc", params=params)

.. code:: python

    >>> print(result.cad_parameters)

    {'my_param': 2}


Part Management and Creation
----------------------------

PyPrimeMesh has options for part management within the product structure while importing a CAD (Computer Aided Design) model. 
The CAD model is the top in product hierarchy. A CAD model can have one or more CAD assemblies.
The CAD assembly or sub-assembly has different CAD parts.
The CAD part has bodies or other geometric entities. A typical CAD product structure is as follows:

.. figure:: ../images/cad_structure(2).png
    :width: 100pt
    :align: center

    **Example CAD structure from SpaceClaim**

The :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` class decides whether to create a part per:

 * Model

 * Assembly

 * Part

 * Body


Model
^^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`MODEL <ansys.meshing.prime.PartCreationType.MODEL>`, a single part is created that inherits its name from the CAD model name. 
The number of zones within the part is identical to the number of bodies within the CAD model.  As below:

.. figure:: ../images/creation_model(2).png
    :width: 220pt
    :align: center

    **Part creation by Model (from SpaceClaim to PyPrimeMesh part structure)**

Assembly
^^^^^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`ASSEMBLY <ansys.meshing.prime.PartCreationType.ASSEMBLY>`, a part per CAD assembly is created where the part name is inherited from the CAD assembly name.
The number of zones within each part is identical to the number of bodies within the CAD assembly.  As below:

.. figure:: ../images/creation_assembly(2).png
    :width: 200pt
    :align: center

    **Part creation by Assembly (from SpaceClaim to PyPrimeMesh part structure)**

Part
^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`PART <ansys.meshing.prime.PartCreationType.PART>`, a part per CAD part is created that inherits the part name from the CAD part name. 
The number of zones within a part is identical to the number of bodies within the CAD part.  As below:

.. figure:: ../images/creation_part(2).png
    :width: 221pt
    :align: center

    **Part creation by Part (from SpaceClaim to PyPrimeMesh part structure)**

Body
^^^^

When you import a CAD model and specify the :class:`PartCreationType <ansys.meshing.prime.PartCreationType>` attribute as :attr:`BODY <ansys.meshing.prime.PartCreationType.BODY>`, a part per CAD body is created that inherits the part name from the CAD body name. 
The number of parts is identical to the number of bodies.  As below:

.. figure:: ../images/creation_body(2).png
    :width: 200pt
    :align: center

    **Part creation by Body (from SpaceClaim to PyPrimeMesh part structure)**


=========================================
Importing and Exporting Solver Mesh Files
=========================================

.. tip::
    File extensions such as CAS ``(*.cas)``, MSH ``(*.msh, *.msh.gz)``, CDB ``(*.cdb)`` can be imported using the :func:`Mesh.read() <ansys.meshing.prime.lucid.Mesh.read>` and exported using the :func:`Mesh.write() <ansys.meshing.prime.lucid.Mesh.write>` in Lucid API.

Import Solver Mesh Files
------------------------

 - The :func:`FileIO.import_fluent_case() <ansys.meshing.prime.FileIO.import_fluent_case>` function allows you to import Fluent case ``(*.cas)`` file and set parameters for importing files using the :class:`ImportFluentCaseParams <ansys.meshing.prime.ImportFluentCaseParams>` class.

 - The :func:`FileIO.import_fluent_meshing_meshes() <ansys.meshing.prime.FileIO.import_fluent_meshing_meshes>` function allows you to import Fluent meshing's mesh files ``(*.msh, *.msh.gz)`` and set parameters for importing files using the :class:`ImportFluentMeshingMeshParams <ansys.meshing.prime.ImportFluentMeshingMeshParams>` class. You can import multiple files in parallel using multithreading with optional parameter :attr:`enable_multi_threading <ansys.meshing.prime.ImportFluentMeshingMeshParams.enable_multi_threading>`.

 - The :func:`FileIO.import_mapdl_cdb() <ansys.meshing.prime.FileIO.import_mapdl_cdb>` function allows you to import MAPDL ``(*.cdb)`` file and set parameters for importing files using the :class:`ImportMapdlCdbParams <ansys.meshing.prime.ImportMapdlCdbParams>` class. You can import quadratic mesh elements as linear with optional parameter :attr:`drop_mid_nodes <ansys.meshing.prime.ImportMapdlCdbParams.drop_mid_nodes>`.

.. note::
    All import functions have the optional parameter to append imported file to existing model.

Export Solver Mesh Files
------------------------

 - The :func:`FileIO.export_fluent_case() <ansys.meshing.prime.FileIO.export_fluent_case>` function allows you to export Fluent case ``(*.cas)`` file and set parameters for exporting files using the :class:`ExportFluentCaseParams <ansys.meshing.prime.ExportFluentCaseParams>` class.

 - The :func:`FileIO.export_fluent_meshing_meshes() <ansys.meshing.prime.FileIO.export_fluent_meshing_meshes>` function allows you to export Fluent meshing's meshes ``(*.msh)`` file and set parameters for exporting files using the :class:`ExportFluentMeshingMeshParams <ansys.meshing.prime.ExportFluentMeshingMeshParams>` class.

 - The :func:`FileIO.export_mapdl_cdb() <ansys.meshing.prime.FileIO.export_mapdl_cdb>` function allows you to export MAPDL ``(*.cdb)`` file and set parameters for exporting files using the :class:`ExportMapdlCdbParams <ansys.meshing.prime.ExportMapdlCdbParams>` class.

 - The :func:`FileIO.export_boundary_fitted_spline_kfile() <ansys.meshing.prime.FileIO.export_boundary_fitted_spline_kfile>` function allows you to export IGA LS-DYNA keyword ``(*.k)`` file and set parameters for exporting boundary fitted splines using the :class:`ExportBoundaryFittedSplineParams <ansys.meshing.prime.ExportBoundaryFittedSplineParams>` class.


====================================
Reading and Writing Size Field Files
====================================

Native PSF format
-----------------

 - The :func:`FileIO.read_size_field() <ansys.meshing.prime.FileIO.read_size_field>` function allows you to read Ansys Prime Server's size field ``(*.psf, *.psf.gz)`` file and set parameters for reading size field file using the :class:`ReadSizeFieldParams <ansys.meshing.prime.ReadSizeFieldParams>` class.

 - The :func:`FileIO.write_size_field() <ansys.meshing.prime.FileIO.write_size_field>` function allows you to write Ansys Prime Server's size field ``(*.psf)`` file and set parameters for writing size field file using the :class:`WriteSizeFieldParams <ansys.meshing.prime.WriteSizeFieldParams>` class. You can write only active size fields into the file with optional parameter :attr:`write_only_active_size_fields <ansys.meshing.prime.WriteSizeFieldParams.write_only_active_size_fields>`.

Fluent Meshing format
---------------------

The :func:`FileIO.import_fluent_meshing_size_field() <ansys.meshing.prime.FileIO.import_fluent_meshing_size_field>` function allows you to import Fluent Meshing's size field ``(*.sf, *.sf.gz)`` file.
