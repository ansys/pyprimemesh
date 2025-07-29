.. _ref_index_solver_translation:

******************
Solver translation
******************

Solver translation (also known as FE2Ansys) translates Abaqus INP files to Ansys CDB and K files (MAPDL and LS-DYNA).
The translation ensures that the Abaqus model can be used in Ansys without recreating from scratch.
It helps to save time and effort even though minor manual adjustments may be required.
The manual adjustments like redefining boundary conditions, loads, and material properties,
ensures that the model behaves as expected in Ansys solver deck.

The following example shows the translation of Abaqus INP file to CDB file format:

1.	Import the Abaqus INP file.

    .. code-block:: python

       file_io = prime.FileIO(model=model)
       import_results = file_io.import_abaqus_inp(
           r"E:/test2/Abaqus_Input_multistep.inp",
           prime.ImportAbaqusParams(model),
       )
       print(import_results)
   
    The import_abaqus_inp imports the INP file as mesh, extracts simulation specific information from the INP file and
    stores the information internally as a JSON document. :class:`ImportAbaqusParams <ansys.meshing.prime.ImportAbaqusParams>`
    allows you to set the parameters for importing the model. The example uses default parameters for importing the model.

    **Output**:

    .. figure:: ../images/fe2ansys_abaqus_import.png

2.	Export the CDB file.

    .. code-block:: python

     export_cdb_result = file_io.export_mapdl_cdb(
            r"E:\test3\Abaqus_Input_multistep.cdb",
            prime.ExportMapdlCdbParams(model)
        )
        print(export_cdb_result)

    :class:`ExportMapdlCdbParams <ansys.meshing.prime.ExportMapdlCdbParams>` allows setting parameters to control
    the export of MAPDL CDB files.

    :class:`ExportMapdlCdbResults <ansys.meshing.prime.ExportMapdlCdbResults>` contains the summary
    result of the export process in json format. This writes the CDB file to the specified location.

    .. figure:: ../images/fe2ansys_cdb_export.png
