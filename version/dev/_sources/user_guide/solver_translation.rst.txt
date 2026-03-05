.. _ref_index_solver_translation:

******************
Solver translation
******************

Solver translation (FE2Ansys) translates Abaqus INP files to Ansys CDB and K files (MAPDL and LS-DYNA).
The translation ensures that the Abaqus model can be used in Ansys without recreating from scratch.
It helps to save time and effort even though minor manual adjustments may be required.
The manual adjustments like redefining boundary conditions, loads, and material properties,
ensures that the model behaves as expected in Ansys solver deck.


Abaqus to Ansys MAPDL Conversion
---------------------------------

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
	
	.. code-block:: pycon
	
	   summary_log : {"Counts": {"beam": 1,"connector": 3,"element": 6944,"elsets": 7,"errors": 0,"node": 6523,
	   "nsets": 2, "physical": 1,"shell": 5375,"skipped": 0,"solid": 1564,"translated": 65,"warnings": 0},"Ids":
	   {"beam": {"max": 7928,"min": 7928},"connector": {"max": 10001,"min": 7929},"element": {"max": 100000,"min": 1},
	   "node": {"max": 100002,"min": 13},"physical": {"max": 100000,"min": 100000},"shell": {"max": 5783,"min": 243},
	   "solid": {"max": 7287,"min": 13}},"Keywords": {"Counts": {"total_keywords_found": 96,"total_keywords_processed": 96,
	   "total_keywords_skipped": 0,"total_keywords_unprocessed": 0},"processed_keywords": {"BEAM SECTION": 1,"BOUNDARY": 1,
	   "CLOAD": 1,"COHESIVE SECTION": 1,"CONNECTOR BEHAVIOR": 1,"CONNECTOR ELASTICITY": 6,"CONNECTOR SECTION": 1,
	   "COUPLING": 1,"DENSITY": 3,"DLOAD": 1,"ELASTIC": 3,"ELEMENT": 13,"ELEMENT OUTPUT": 3,"ELSET": 7,"END STEP": 1,
	   "FASTENER": 1,"FASTENER PROPERTY": 1,"HEADING": 1,"KINEMATIC": 1,"KINEMATIC COUPLING": 1,"MASS": 1,"MATERIAL": 3,
	   "MPC": 3,"NODE": 6,"NODE OUTPUT": 1,"NONSTRUCTURAL MASS": 1,"NSET": 2,"ORIENTATION": 2,"OUTPUT": 2,"PLASTIC": 1,
	   "RIGID BODY": 1,"SECTION CONTROLS": 1,"SHELL SECTION": 2,"SOLID SECTION": 2,"SPRING": 1,"STATIC": 1,"STEP": 1,
	   "SURFACE": 12,"TIE": 4},"skipped_keywords": null,"unprocessed_keywords": null}}
	   error_code : ErrorCode.NOERROR
	   warning_codes : []	
    
	
    Here, the import summary provides information on the following:

    - Total number of keywords in the imported file.

    - Total number of processed keywords.

    - Total number of skipped or unprocessed keywords.

    - Number of imported nodes.

    - Number of imported elements(solid, shell, beam and more).

    - Number and type of skipped elements.

    - Ids of imported nodes and elements.

    - Number of errors and warnings that occurred while importing the file.


2.	Export the CDB file.

    .. code-block:: python

       export_cdb_result = file_io.export_mapdl_cdb(
           r"E:\test3\Abaqus_Input_multistep.cdb",
           prime.ExportMapdlCdbParams(model),
       )
       print(export_cdb_result)

    :class:`ExportMapdlCdbParams <ansys.meshing.prime.ExportMapdlCdbParams>` allows setting parameters to control
    the export of MAPDL CDB files.

    :class:`ExportMapdlCdbResults <ansys.meshing.prime.ExportMapdlCdbResults>` contains the summary
    result of the export process in json format. This writes the CDB file to the specified location.

    .. code-block:: pycon
		
	   summary_log : {"Counts": {"errors": 0,"skipped": 1,"translated": 40,"warnings": 0},"Ids": {"beam": 
	   {"max": 7928},"constant": {"max": 44},"csys": {"max": 2},"element": {"max": 100117},"et": {"max": 28},
	   "material": {"max": 114},"node": {"max": 100002},"section": {"max": 114},"shell": {"max": 100088},
	   "solid": {"max": 7287}}}
	   zone_mesh_results : []
	   error_code : ErrorCode.NOERROR
	   warning_codes : []	
	

    CDB Export summary provides information about:

    - Number of error and warnings that occurred while exporting the CDB file.

    - Maximum number of node ids and elements ids that are exported.

    The following table provides a reference for Abaqus input file keywords supported. It serves as a translation
    reference for converting Abaqus INP format to APDL cdb format.

    .. list-table:: **Supported Abaqus Keywords**
       :widths: 30 70
       :header-rows: 1

       * - **Keyword**
         - **Options**
       * - HEADING
         - None
       * - NODE
         - SYSTEM=R
       * - ELEMENT
         - TYPE=B31, C3D10, C3D4, C3D6, C3D6H, C3D8, C3D8H, C3D8R, C3D8RH, COH3D6, COH3D8, CONN3D2, DCOUP3D, M3D3, M3D4, MASS, R3D3, R3D4, ROTARYI, S3, S3R, S4, S4R, SPRINGA, STRI65
       * - KINEMATIC COUPLING
         - None
       * - MPC
         - None
       * - ORIENTATION
         - DEFINITION=COORDINATES, NODES; SYSTEM=RECTANGULAR
       * - SOLID SECTION
         - None
       * - SHELL SECTION
         - DENSITY=0; NODAL THICKNESS; OFFSET
       * - COHESIVE SECTION
         - RESPONSE=CONTINUUM, TRACTION SEPARATION; THICKNESS=SPECIFIED
       * - BEAM SECTION
         - SECTION=CIRC, PIPE
       * - CONNECTOR SECTION
         - [CARTESIAN–CARDAN], [AXIAL], [CARTESIAN–ROTATION], [WELD], [CARTESIAN–EULER], [JOIN–REVOLUTE], [SLOT–ALIGN]
       * - NSET
         - None
       * - ELSET
         - GENERATE
       * - SURFACE
         - TYPE=ELEMENT, NODE
       * - MATERIAL
         - None
       * - DENSITY
         - None
       * - DAMPING
         - STRUCTURAL=0
       * - ELASTIC
         - TYPE=ISOTROPIC, TRACTION
       * - CONNECTOR BEHAVIOR
         - None
       * - CONNECTOR ELASTICITY
         - NONLINEAR, RIGID
       * - CONNECTOR DAMPING
         - NONLINEAR; TYPE=VISCOUS
       * - SPRING
         - None
       * - MASS
         - None
       * - ROTARY INERTIA
         - None
       * - SECTION CONTROLS
         - ELEMENT DELETION=YES; HOURGLASS=ENHANCED
       * - FASTENER PROPERTY
         - None
       * - NONSTRUCTURAL MASS
         - DISTRIBUTION=MASS PROPORTIONAL; UNITS=TOTAL MASS
       * - TIE
         - ADJUST=NO, YES
       * - FASTENER
         - ADJUST ORIENTATION=NO
       * - AMPLITUDE
         - DEFINITION=EQUALLY SPACED, PERIODIC, TABULAR, periodic; FIXED INTERVAL=0,3; SMOOTH=0; TIME=STEP TIME, step time
       * - RIGID BODY
         - None
       * - STEP
         - NLGEOM=NO, YES; PERTURBATION; UNSYMM=YES
       * - STATIC
         - STABILIZE=0
       * - BOUNDARY
         - BASE NAME=LOAD_FR, LOAD_RR; OP=NEW; TYPE=DISPLACEMENT
       * - CLOAD
         - FOLLOWER; LOADCASE=1; OP=NEW; REAL
       * - DLOAD
         - OP=NEW
       * - OUTPUT
         - FIELD, HISTORY, TIME INTERVAL=0
       * - NODE OUTPUT
         - None
       * - END STEP
         - None
       * - DYNAMIC
         - APPLICATION=MODERATE DISSIPATION, QUASI
       * - ELEMENT OUTPUT
         - POSITION=CENTROIDAL
       * - SYSTEM
         - None
       * - TRANSFORM
         - TYPE=R
       * - PLASTIC
         - None
       * - HYPERELASTIC
         - MODULI=LONG TERM; N=3; NEO HOOKE; REDUCED POLYNOMIAL; YEOH
       * - SURFACE INTERACTION
         - None
       * - FRICTION
         - SLIP TOLERANCE=0
       * - CONTACT PAIR
         - ADJUST=0; SMALL SLIDING; SMOOTH=0; TYPE=NODE TO SURFACE, SURFACE TO SURFACE
       * - MONITOR
         - DOF=1,2,3; NODE=FR_DR_JIG_PT, FR_DR_RH_JIG_PT, JIG_OS_CENTER, RR_DR_JIG_PT, RR_DR_RH_JIG_PT, node
       * - NODE PRINT
         - None
       * - MEMBRANE SECTION
         - None
       * - TIME POINT
         - None
       * - CONTACT
         - None
       * - CONTACT INCLUSIONS
         - ALL EXTERIOR
       * - CONTACT EXCLUSIONS
         - None
       * - CONTACT PROPERTY ASSIGNMENT
         - None
       * - DAMAGE INITIATION
         - CRITERION=DUCTILE
       * - DAMAGE EVOLUTION
         - TYPE=DISPLACEMENT
       * - FREQUENCY
         - DAMPING PROJECTION=ON; EIGENSOLVER=AMS; NORMALIZATION=MASS; RESIDUAL MODES; SIMULATION=STEADY STATE

Abaqus to LS-DYNA Conversion 
-----------------------------

Abaqus to LS-DYNA conversion helps you migrate models between solvers for different types of analysis. 
It avoids rebuilding the model from scratch and saves time and effort.

The following example shows the translation of Abaqus INP file to K file format: 

1. Import the Abaqus INP file. 

    .. code-block:: python
    
        fileio = prime.FileIO(model=model)
        import_results = fileio.import_abaqus_inp(
            r"E:\test3\spot_weld_test.inp",
            prime.ImportAbaqusParams(model),
        )

    The import_abaqus_inp imports the INP file as mesh, extracts simulation specific information from the INP file 
    and stores the information internally as a JSON document. 
    :class:`ImportAbaqusParams <ansys.meshing.prime.ImportAbaqusParams>` allows you to set the parameters for importing the model. 
    The example uses default parameters for importing the model.  

    **Output**

    .. code-block:: pycon

        summary_log : {"Counts": {"connector": 4,"element": 1420,"elsets": 5,"errors": 0,"node": 1708,"nsets": 19,
        "shell": 1416,"skipped": 0,"translated": 47,"warnings": 0},"Ids": {"connector": {"max": 900004,"min": 900001},
        "element": {"max": 900004,"min": 19},"node": {"max": 300424,"min": 47},"shell": {"max": 14186,"min": 19}},
        "Keywords": {"Counts": {"total_keywords_found": 65,"total_keywords_processed": 65,"total_keywords_skipped": 0,
        "total_keywords_unprocessed": 0},"processed_keywords": {"AMPLITUDE": 1,"BOUNDARY": 2,"CONNECTOR BEHAVIOR": 1,
        "CONNECTOR ELASTICITY": 6,"CONNECTOR SECTION": 1,"DENSITY": 2,"DYNAMIC": 1,"ELASTIC": 2,"ELEMENT": 3,
        "ELEMENT OUTPUT": 1,"ELSET": 5,"END STEP": 1,"ENERGY OUTPUT": 1,"FASTENER": 1,"FASTENER PROPERTY": 1,
        "FIXED MASS SCALING": 1,"HEADING": 1,"MATERIAL": 2,"NODE": 1,"NODE OUTPUT": 1,"NSET": 19,"ORIENTATION": 1,
        "OUTPUT": 2,"PLASTIC": 2,"SHELL SECTION": 2,"STEP": 1,"SURFACE": 2,"VARIABLE MASS SCALING": 1},
        "skipped_keywords": null,"unprocessed_keywords": null}} 
        formatted_summary_log : None 
        error_code : 0 
        warning_codes : []  

    Here, the import summary provides information on the following: 

    - Total number of keywords in the imported file. 

    - Total number of processed keywords. 

    - Total number of skipped or unprocessed keywords. 

    - Number of imported nodes. 

    - Number of imported elements (solid, shell, beam and more). 

    - Number and type of skipped elements. 

    - Ids of imported nodes and elements. 

    - Number of errors and warnings that occurred while importing the file. 

2. Export the K file.

    .. code-block:: python

        main_k_file = os.path.join(file_name.split(".")[0] + ".k")
        k_params = prime.ExportLSDynaKeywordFileParams(model=model)
        export_K_result = prime.FileIO(model).export_lsdyna_keyword_file(main_k_file, k_params)
        print(export_K_result)


   
   :func:`FileIO.export_lsdyna_keyword_file <ansys.meshing.prime.FileIO.export_lsdyna_keyword_file>` allows you 
   to write out an LS-DYNA Keyword `(*.k)` file that contains the mesh definition and other necessary information 
   to carry out the analysis run using the LS-DYNA solver.  
    
   :func:`ExportLSDynaKeywordFileParams<ansys.meshing.prime.FileIO.export_lsdyna_keyword_file>` allows you to 
   specify the application type (SEATBELT, DOORSLAM), indicate whether to compute the spot weld thickness, 
   append the material cards in the K file, provide the database cards to append in the K file, and specify
   the LS-DYNA data field format.
   You should specify the material properties card and the database keywords card in LS-DYNA format. 
    
   **Output**

    .. code-block:: pycon

        summary_log : {"Counts": {"errors": 0,"skipped": 0,"translated": 16,"warnings": 0},
        "Ids": {"beam": {"max": 0},"csys": {"max": 1},"element": {"max": 900004},"friction": {"max": 0},
        "hour_glass": {"max": 6},"joint": {"max": 0},"load_curve": {"max": 4},"material": {"max": 67},
        "node": {"max": 300425},"part": {"max": 68},"section": {"max": 67},"set": {"max": 17},
        "shell": {"max": 14186},"solid": {"max": 0}},"Settings": {"analysis_type": "LSDynaAnalysisType_Doorslam",
        "compute_spotweld_thickness": "true","output_format": "LSDynaFormat_i10"}}
        zone_mesh_results : []
        error_code : 0
        warning_codes : [] 

    
  Export summary provides information about: 

    - Number of error and warnings that occurred while exporting the K file. 

    - Maximum number of node ids and elements ids that are exported.