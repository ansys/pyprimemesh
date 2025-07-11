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
print(model)
print(import_results)  
