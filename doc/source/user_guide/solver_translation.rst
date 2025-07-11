.. _ref_index_solver_translation:

*********************
Solver translation
*********************

Solver Translation (commonly known as FE2Ansys) translates Abaqus input deck to Ansys solver decks (MAPDL and LS-DYNA).
The translation ensures that the abaqus model can be used in Ansys without recreating them from scratch.
It helps to save time and efforts even though minor manual adjustments may be required.
The manual adjustments like redefining boundary conditions, loads, and material properties,
ensures that the model behaves as expected in Ansys solver deck.

The following example shows the translation of Abaqus input file to MAPDL file format:

1.	Import the Abaqus file.

    .. code-block:: python

       file_io = prime.FileIO(model=model)
       import_results = file_io.import_abaqus_inp(r"E:/test2/Abaqus_Input_multistep.inp", prime.ImportAbaqusParams(model))
       print(import_results)
   
    The import_abaqus_inp imports the abaqus file as mesh, extracts simulation specific information from the abaqus file and
    stores the information in Prime as a JSON document. :class:`ImportAbaqusParams <ansys.meshing.prime.ImportAbaqusParams>`
    allows you to set the parameters for importing the model. The example uses default parameters for importing the model.

    **Output**:

    .. figure:: ../images/fe2ansys_abaqus_import.png

2.	Export the file in MAPDL format.

    .. code-block:: python

        mapdl_params = prime.ExportMapdlCdbParams(model=model)
        mesh_file_cdb = os.path.join(r"E:\test3\Abaqus_Input_multistep.cdb")
        export_cdb_result = file_io.export_mapdl_cdb(mesh_file_cdb, params=mapdl_params)
        print(export_cdb_result)

    :class:`ExportMapdlCdbParams <ansys.meshing.prime.ExportMapdlCdbParams>` allows setting parameters to control
    the export of MAPDL CDB files.

    :class:`ExportMapdlCdbResults <ansys.meshing.prime.ExportMapdlCdbResults>` contains the summary
    result of the export process in json format. This writes the .cdb file to the specified location.

    .. figure:: ../images/fe2ansys_cdb_export.png
