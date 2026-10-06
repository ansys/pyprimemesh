# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module for error handling in PyPrimeMesh."""
import re
from functools import wraps

from ansys.meshing.prime.autogen.primeconfig import ErrorCode, WarningCode

prime_error_messages = {
    ErrorCode.NOERROR: "Success.",
    ErrorCode.UNKNOWN: "Unknown Error.",
    ErrorCode.SIGSEGV: "Segmentation Violation.",
    ErrorCode.READPMDATFAILED: "Failed to read PMDAT. Check the path or filename specified.",
    ErrorCode.EXPORTFLUENTCASEFAILED: "Failed to export fluent case.",
    ErrorCode.EXPORTFLUENTMESHINGMSHFAILED: "Failed to export fluent meshing mesh file.",
    ErrorCode.VOLUMEZONESNOTFOUNDTOEXPORTFLUENTCASE: "Cell zonelets not found to export fluent case.",
    ErrorCode.MESHNOTFOUNDTOEXPORTFLUENTMESHINGMESH: " Mesh not found to export fluent meshing mesh.",
    ErrorCode.IMPORTFLUENTMESHINGMSHFAILED: "Failed to import fluent meshing mesh file.",
    ErrorCode.IMPORTFLUENTCASEFAILED: "Failed to import fluent case file.",
    ErrorCode.WRITEPMDATFAILED: "Failed to write PMDAT file.",
    ErrorCode.FILENOTFOUND: "Incorrect File Path or Name. Check your file name and path.",
    ErrorCode.SURFERFAILED: "Surface meshing failed.",
    ErrorCode.SURFERAUTOSIZEQUADUNSUPPORTED: "Program controlled surface meshing does not support quadrilateral mesh.",
    ErrorCode.SURFERAUTOSIZEMUSTBEVOLUMETRIC: "Surface meshing supports only volumetric sizefield.",
    ErrorCode.SURFERDEGENERATEFACE: "Face is degenerated for surface meshing.",
    ErrorCode.MAPMESHINGFAILED: "Surfer map meshing operation failed.",
    ErrorCode.FACEZONELETSFEATURESNOTUPTODATE: "Association between edge and face zonelets is broken. Extract features by edges.",
    ErrorCode.SURFERLAYEREDQUADFAILED: "Layered quad meshing failed.",
    ErrorCode.SURFERINVALIDINPUT: "Surface meshing invalid input.",
    ErrorCode.SURFERNONMANIFOLDEDGE: "Surface meshing non manifold edge.",
    ErrorCode.SURFEROPENINITIALFRONTLOOP: "Surface meshing open initial front loop.",
    ErrorCode.LOCALSURFERINVALIDNUMRINGS: "Invalid number of rings input for the local surface mesh operation.",
    ErrorCode.SURFERQUADFAILED: " Quad meshing failed for surface meshing.",
    ErrorCode.SURFERWITHAUTOSIZINGFAILED: "Surface meshing with auto sizing failed.",
    ErrorCode.FREEZEMESHERROR: "Remeshing a frozen mesh failed.",
    ErrorCode.REMESHFACEZONELETSNOTSUPPORTEDFORTOPOLOGYPART: "Remesh face zonelets is not supported for part with topology data. Try mesh_topo_faces in surfer.",
    ErrorCode.REMESHFACEZONELETSLOCALLYNOTSUPPORTEDFORTOPOLOGYPART: "Remesh face zonelets locally is not supported for part with topology data. Try a topology based operation.",
    ErrorCode.SURFERINVALIDCONSTANTSIZE: "Invalid size for constant size surface meshing.",
    ErrorCode.SCAFFOLDERBADINPUTEMPTYTOPO: "Empty Topology provided to scaffolder.",
    ErrorCode.SCAFFOLDERBADINPUTNOFREEFACES: "No free faces found in current topology.",
    ErrorCode.SCAFFOLDERBADINPUTPARAMS: "Invalid scaffolder parameters setup.",
    ErrorCode.SCAFFOLDERINVALIDABSOLUTEDISTOL: "Absolute distance tolerance must be a positive double and smaller than constant mesh size.",
    ErrorCode.SCAFFOLDERINVALIDCONSTANTMESHSIZE: "Constant mesh must be a positive double.",
    ErrorCode.VT_COLLAPSESHORTEDGESFAILED: "Collapse short edges operation failed.",
    ErrorCode.VT_CREATELEADINGEDGEFAILED: "Create leading edge operation failed.",
    ErrorCode.VT_CREATEMIDEDGEFAILED: "Create mid edge operation failed.",
    ErrorCode.VT_FILLANNULARHOLEFAILED: "Fill annular hole operation failed.",
    ErrorCode.VT_FILLHOLEFAILED: "Fill hole operation failed.",
    ErrorCode.VT_INVALIDINPUT: "Invalid input provided for VT operation.",
    ErrorCode.VT_MERGEFACESFAILED: "Merge faces operation failed.",
    ErrorCode.VT_MERGETHINEXTFAILED: "Merge thin extensions operation failed.",
    ErrorCode.VT_MERGETHINSTRIPESFAILED: "Merge thin stripes operation failed.",
    ErrorCode.VT_OPERATIONFAILED: "VT operation failed.",
    ErrorCode.VT_PINCHFACESFAILED: "Pinch faces operation failed.",
    ErrorCode.VT_REPAIRSHARPCORNERANGLESFAILED: "Repair sharp corner angles operation failed.",
    ErrorCode.VT_SEPARATEFACESFAILED: "Separate faces operation failed.",
    ErrorCode.VT_PROTECTEDENTITIESFOUND: "Protected entities found in input during topology modification operation.",
    ErrorCode.VT_INTERIOREDGETRACINGFAILED: "Failed to trace interior edge during topology modification operation.",
    ErrorCode.VT_REMESHFACEFAILED: "Failed to remesh face during topology modification operation.",
    ErrorCode.VT_MERGEEDGESFAILED: "Failed to merge edges through common nodes.",
    ErrorCode.VTMERGEVOLUMESNOSHAREDFACESFOUND: "Failed to find input topovolumes with shared faces for merging.",
    ErrorCode.VT_MERGEVOLUMESFAILED: "Merge topovolumes failed.",
    ErrorCode.VOLUMETRICSCAFFOLDER_INVALIDINPUT: "Invalid input provided for the volumetric scaffolder operation.",
    ErrorCode.TOPODECOMPOSITION_INVALIDPARAMS: "Invalid input parameter(s) provided for topology decomposition.",
    ErrorCode.TOPODECOMPOSITION_EMPTYINPUT: "Empty input provided for topology decomposition.",
    ErrorCode.TOPODECOMPOSITION_UNMESHEDTOPOFACES: "Input for topology decomposition contains unmeshed topoface(s).",
    ErrorCode.TOPODECOMPOSITION_ORIENTTOPOVOLUMESFAILED: "Failed to orient input topovolume(s) during topology decomposition.",
    ErrorCode.TOPODECOMPOSITION_INVALIDINPUTFACEZONELETS: "Input face zonelet(s) are invalid for topology decomposition. Please check for free or degenerate faces in the input.",
    ErrorCode.TOPODECOMPOSITION_TOPOLOGYUPDATEFAILED: "Topology update failed during topology decomposition.",
    ErrorCode.MICROSTRUCTUREBADSHAPEPROPERTIES: "Bad shape properties.",
    ErrorCode.MICROSTRUCTUREINVALIDELEMENTTYPE: "Invalid input provided. Invalid Element Type.",
    ErrorCode.MICROSTRUCTUREINVALIDSHAPETYPE: "Invalid input provided. Invalid Shape.",
    ErrorCode.MICROSTRUCTUREQUADRATICHEXREQUIREDQUADRATICVOXELGRID: "Volume mesh generation for hexahedra requires generation of a quadratic voxel grid.",
    ErrorCode.MICROSTRUCTUREREMESHNOTSUPPORTED: "Surface remesh operation is not supported.",
    ErrorCode.MICROSTRUCTURESMOOTHNOTSUPPORTED: "Smoothing operation is not supported.",
    ErrorCode.MICROSTRUCTUREWRONGAPICALLSEQUENCE: "Wrong API call sequence.",
    ErrorCode.JSONKEYNOTFOUND: "Json key not found.",
    ErrorCode.NUMENMETHODNOTFOUND: "Could not find numen method.",
    ErrorCode.NUMEN_AUTOCOMPUTEDEADMPTS_EMPTYEXTERNALCAPSCOPE: "External cap part expression resolved to an empty scope during automatic dead material point computation. Provide a valid part expression that resolves to external cap surface (sheet) parts.",
    ErrorCode.NUMEN_AUTOCOMPUTEDEADMPTS_NOEXTERNALCAPTOPOFACES: "No external cap topofaces were found for automatic dead material point computation. Ensure external cap parts exist and match the given expression.",
    ErrorCode.NUMEN_AUTOCOMPUTEDEADMPTS_SOLIDEXTERNALCAPPARTS: "External cap part expression includes parts with solid bodies during automatic dead material point computation. Provide only surface (sheet) parts representing external cap surfaces.",
    ErrorCode.NUMEN_AUTOCOMPUTEDEADMPTS_SOLIDINTERNALCAPPARTS: "Internal cap part expression includes parts with solid bodies during automatic dead material point computation. Provide only surface (sheet) parts representing internal cap surfaces.",
    ErrorCode.NUMEN_AUTOCOMPUTEDEADMPTS_COMPUTEINTERNALREGIONPOINTSFAILED: "Failed to compute internal region points during automatic dead material point computation.",
    ErrorCode.NUMEN_INITDEFAULTSIZE_NOTOPOPARTS: "No topology parts were found matching the part expression during default size initialization. Provide a part expression that resolves to parts with topology.",
    ErrorCode.NUMEN_INITDEFAULTSIZE_NOEDGES: "No topology edges were found for analysis during default size initialization. Ensure the specified parts contain topology edges.",
    ErrorCode.NUMEN_INITDEFAULTSIZE_INVALIDBOUNDINGBOX: "Model bounding box is degenerated (zero or negative extent) during default size initialization. Ensure the specified parts have valid geometry with face zonelets.",
    ErrorCode.NUMEN_INITDEFAULTSIZE_INVALIDMINEDGELENGTH: "Global minimum edge length could not be determined during default size initialization. All edges may have been filtered out by the garbage-edge sweep; consider relaxing minGlobalEdgeRatio.",
    ErrorCode.NUMEN_INITDEFAULTSIZE_INVALIDCOMPUTEDRANGE: "Computed min or max sizes are invalid (zero, non-finite, or min >= max) during default size initialization. Review geometry quality and input parameters.",
    ErrorCode.NUMEN_INITDEFAULTSIZE_SETGLOBALSIZINGFAILED: "SetGlobalSizingParams rejected the computed values during default size initialization.",
    ErrorCode.NUMEN_AUTOASSIGNPARTSTOWRAPPEDSOLIDMESHFAILED: "Auto assign parts to wrapped solid mesh operation failed.",
    ErrorCode.NUMEN_EXTRACTFLOWVOLUMEFAILED: "Extract flow volume operation failed.",
    ErrorCode.NUMEN_EXTRACTFLOWVOLUMEPARTSNOTFOUND: "Flow volume parts not found. Ensure the part expression matches at least one part.",
    ErrorCode.NUMEN_CAPFACEEXPRESSIONEMPTY: "Cap face expression is empty for user-defined capping. Ensure the cap face expression is specified.",
    ErrorCode.NUMEN_MRFPARTSMORETHANONE: "Multiple MRF parts found. Only one MRF part is allowed.",
    ErrorCode.NUMEN_PARTSSAMEASMRFPARTS: "Flow volume parts are the same as MRF parts. Specify different parts for flow volume and MRF.",
    ErrorCode.NUMEN_EXTERNALFLOWPARTNOTFOUND: "External flow part not found. Ensure the external flow part expression matches at least one part in the model.",
    ErrorCode.NUMEN_EXTERNALFLOWPARTSSAMEASMRFPARTS: "External flow part and MRF parts are the same. Specify different parts for external flow and MRF.",
    ErrorCode.NUMEN_EXTERNALFLOWPARTSMORETHANONE: "Multiple external flow parts found. Only one external flow part is allowed.",
    ErrorCode.NUMEN_PARTSNOTFOUNDAFTERFILTERING: "Flow volume parts are empty after filtering out MRF and external flow parts. Ensure the flow volume parts do not include MRF and external flow parts.",
    ErrorCode.NUMEN_VALIDCAPFACESNOTFOUND: "No valid cap faces were found for the specified cap face expression. Ensure the cap face expression matches at least one cap face.",
    ErrorCode.NUMEN_CAPPARTSMESHINGFAILED: "Meshing of cap parts using volumetric size fields failed.",
    ErrorCode.NUMEN_NOAUTOFLUIDZONENAME: "Flow volume zone name must be defined for this capping type.",
    ErrorCode.NUMEN_NOCAPFACESFOUND: "No cap faces found for the specified cap face expression.",
    ErrorCode.NUMEN_MULTIPLESOLIDCAPPARTS: "Multiple solid parts found from the cap face expression. Only one solid part is allowed.",
    ErrorCode.NUMEN_NOFLOWVOLUMEPARTSFORCAPCREATION: "No flow volume parts found for cap creation.",
    ErrorCode.NUMEN_CAPEDGEEXPRESSIONNOTDEFINED: "Parameter cap_edge_expression must be defined for capping_type 'create'.",
    ErrorCode.NUMEN_CAPCREATIONPARTNOTFOUND: "Failed to resolve part for cap creation.",
    ErrorCode.NUMEN_CAPCREATIONPARTHASNOTOPOLOGY: "Part does not have topology. Cap creation requires topology parts.",
    ErrorCode.NUMEN_NOCAPEDGESFOUND: "No cap edges found for the specified edge expression.",
    ErrorCode.NUMEN_CAPCREATIONBYEDGEFAILED: "Cap creation using the specified edge expression failed.",
    ErrorCode.NUMEN_FLOWVOLUMEPARTSNOTFOUND: "No flow volume parts available for flow volume extraction.",
    ErrorCode.NUMEN_CONNECTINTERFACEFAILED: "Connect interface operation failed.",
    ErrorCode.NUMEN_VOLUMEMESHINGFAILED: "Volume meshing operation failed.",
    ErrorCode.NUMEN_SETLABELSONFEATUREEDGESFAILED: "Set labels on feature edges operation failed.",
    ErrorCode.NUMEN_DETECTTHINVOLUMESFAILED: "Detect thin volumes operation failed.",
    ErrorCode.NUMEN_INITIALIZEDEFAULTSIZEFAILED: "Initialize default size operation failed.",
    ErrorCode.NUMEN_CREATEFACEZONESFORFACELABELSFAILED: "Create face zones for face labels operation failed.",
    ErrorCode.NUMEN_POSTMESHCLEANUPFAILED: "Post mesh cleanup operation failed.",
    ErrorCode.NUMEN_SETTINGSFAILED: "Settings operation failed.",
    ErrorCode.NUMEN_TOPOLOGYSUMMARYFAILED: "Topology summary operation failed.",
    ErrorCode.NUMEN_SURFACEMESHSUMMARYFAILED: "Surface mesh summary operation failed.",
    ErrorCode.NUMEN_SURFACEMESHQUALITYFAILED: "Surface mesh quality operation failed.",
    ErrorCode.NUMEN_VOLUMEMESHCHECKFAILED: "Volume mesh check operation failed.",
    ErrorCode.NUMEN_VOLUMEMESHSUMMARYFAILED: "Volume mesh summary operation failed.",
    ErrorCode.NUMEN_VOLUMEMESHQUALITYFAILED: "Volume mesh quality operation failed.",
    ErrorCode.NUMEN_FUSEFAILED: "Fuse operation failed.",
    ErrorCode.NUMEN_FILEREADFAILED: "File read operation failed.",
    ErrorCode.NUMEN_FILEWRITEFAILED: "File write operation failed.",
    ErrorCode.NUMEN_PRECHECKMODELFAILED: "Precheck model operation failed.",
    ErrorCode.NUMEN_ZONESCOUNTVALIDATIONFAILED: "Zones count validation operation failed.",
    ErrorCode.PREPAREFORVOLUMEMESHINGFAILED: "Prepare for volume meshing failed.",
    ErrorCode.NOTSUPPORTEDFORDISTRIBUTEMESHING: "Method not supported for distributed meshing.",
    ErrorCode.SPLITANDCOLLAPSEFACEELEMENTSFAILED: "Failed to split and collapse face element(s).",
    ErrorCode.STITCHENTITIESFAILED: "Stitch entities failed.",
    ErrorCode.STITCHWITHPRESERVEDENTITIESFAILED: "Stitch with preserved entities failed.",
    ErrorCode.CELLSEPARATIONFAILED: "Cell separation failed.",
    ErrorCode.NOCELLSSEPARATED: "No cells separated based on given input.",
    ErrorCode.INVALIDCONTROLPARAMS: "Invalid control parameters.",
    ErrorCode.OUTOFMEMORY: "Out of memory.",
    ErrorCode.INTERRUPTED: "Prime operation interrupted.",
    ErrorCode.COREOBJECTSNOTSYNCEDBETWEENNODES: "Core objects are not synchronized between parallel nodes.",
    ErrorCode.AUTOMESHFAILED: "Auto meshing failed.",
    ErrorCode.MESHDECOUPLEDFAILED: "Mesh decoupled parallel failed.",
    ErrorCode.THINVOLUMEMESHFAILED: "Thin volume meshing failed.",
    ErrorCode.PRISMMESHFAILED: "Prism meshing failed.",
    ErrorCode.AUTOMESHINITFAILED: "Auto mesh initialization failed.",
    ErrorCode.AUTOMESHCELLASSOCIATIONFAILED: "Associating auto mesh cells with zonelets failed.",
    ErrorCode.AUTOMESHSIZEFIELDTYPENOTSUPPORTED: "The specified size field type is not supported for the specified volume fill type.",
    ErrorCode.POLYMESHFAILED: "Poly meshing failed.",
    ErrorCode.PYRAMIDMESHFAILED: "Pyramid meshing failed.",
    ErrorCode.DELETEMESHFAILED: "Deleting mesh failed.",
    ErrorCode.INVALIDPRISMCONTROLS: "Conflict of prism settings on zonelets or invalid prism controls selected.",
    ErrorCode.PERIODICSURFACESNOTSUPPORTEDFORPRISMS: "Periodic surfaces selected for prism generation, not supported.",
    ErrorCode.ALREADYVOLUMEMESHED: "Already volume meshed.",
    ErrorCode.INCREMENTALVOLUMEMESHINGNOTSUPPORTED: "Incremental volume meshing is not supported.",
    ErrorCode.TOPOLOGYCLEANUPFAILED: "Topology cleanup operation failed.",
    ErrorCode.SUPPRESSINTERIORTOPOEDGESFAILED: "Suppress interior topology edges operation failed.",
    ErrorCode.SUPPRESSNONFEATURETOPOEDGESFAILED: "Suppress non-feature topology edges operation failed.",
    ErrorCode.SUPPRESSTOPONODESFAILED: "Suppress topology nodes operation failed.",
    ErrorCode.REPAIRTOPOEDGESOFTOPOFACESFAILED: "Repair topology edges of faces operation failed.",
    ErrorCode.INVALIDCONSTANTMESHSIZE: "Invalid constant mesh size parameter.",
    ErrorCode.INVALIDABSOLUTEDISTTOLERANCE: "Invalid absolute distance tolerance parameter.",
    ErrorCode.VOLUMESNOTUPTODATE: "Volumes are not up to date. Compute topovolumes for topology part or compute closed volumes for non topology parts and try again.",
    ErrorCode.QUADRATICMESHSUPPORTEDONLYFORTETS: "Quadratic meshing is supported only for tetrahedrons.",
    ErrorCode.NOACTIVESFFOUND: "Active size fields are not available.",
    ErrorCode.SURFACEMESHCHECKFAILED: "Surface mesh check operation failed.",
    ErrorCode.AITOVERLAPALONGMULTIFOUND: "Overlapping faces along multi-connection found.",
    ErrorCode.TRIANGULATIONFAILED: "Planar triangulation failed.",
    ErrorCode.TOPOFACESREMESHFAILED: "Failed to remesh some topofaces.",
    ErrorCode.PARTNOTFOUND: "Part not found.",
    ErrorCode.TOPODATANOTFOUND: "Topodata not found.",
    ErrorCode.SIZEFIELDNOTFOUND: "Size Field not found.",
    ErrorCode.CADGEOMETRYNOTFOUND: "No CAD geometry was found for the requested projections.",
    ErrorCode.VOLUMENOTFOUND: "Volume not found.",
    ErrorCode.ZONENOTFOUND: "Zone not found.",
    ErrorCode.NOTSUPPORTEDFORTOPOLOGYPART: "Operation is not supported for part with topology data. Try a topology-based operation.",
    ErrorCode.ADDINGPROVIDEDENTITIESNOTSUPPORTEDFORTOPOLOGYPART: "Operation is not supported for part with topology data. Try add_topo_entities_to_zone in part.",
    ErrorCode.MERGEZONELETSNOTSUPPORTEDFORTOPOLOGYPART: "Operation is not supported for part with topology data. Try a topology-based operation.",
    ErrorCode.MERGEVOLUMESNOTSUPPORTEDFORTOPOLOGYPART: "Operation is not supported for part with topology data. Try a topology-based operation.",
    ErrorCode.NOTSUPPORTEDFORHIGHERORDERMESHPART: "Not supported for part with higher order mesh.",
    ErrorCode.NOTSUPPORTEDFORPOLYMESHPART: "Not supported for part with poly mesh.",
    ErrorCode.SPHEREATINVALIDNORMALNODESFAILED: "Sphere creation at invalid normal nodes failed.",
    ErrorCode.INVALIDPLANEPOINTS: "Invalid plane points. You must provide 3 points (9 coordinates).",
    ErrorCode.PLANECOLLINEARPOINTS: "Collinear or duplicate points given to define plane.",
    ErrorCode.INVALIDREGISTERID: "Invalid register id provided. Register ids between 1 to 28 are valid.",
    ErrorCode.SURFACEFEATURETYPENOTSUPPORTED: "Surface search for provided feature type is not supported.",
    ErrorCode.DELETEZONELETSCONNECTEDTOCELLS: "Cannot delete face zonelets connected to volume mesh.",
    ErrorCode.DELETEZONELETSFAILED: "Delete zonelets failed.",
    ErrorCode.PROJECTONCADGEOMETRYFAILED: "Projection on CAD geometry failed.",
    ErrorCode.ZONESARENOTOFSAMETYPE: "Zones selected are not of same type.",
    ErrorCode.TOPOEDGESREMESHFAILED: "Failed to remesh topoedges.",
    ErrorCode.DUPLICATENODESFOUND: "Duplicate nodes were found in the input mesh.",
    ErrorCode.DUPLICATEFACESFOUND: "Duplicate faces were found in the input mesh.",
    ErrorCode.EDGEINTERSECTINGFACEFOUND: "Edge intersects face.",
    ErrorCode.SEPARATIONRESULTSFAILED: "Failed to separate faces. Provide valid inputs.",
    ErrorCode.SIZEFIELDCOMPUTATIONFAILED: "Size Field computation failed.",
    ErrorCode.DELETEVOLUMETRICSIZEFIELDSFAILED: "Deleting volumetric size fields failed.",
    ErrorCode.REFRESHSIZEFIELDSFAILED: "Refresh Size Fields failed.",
    ErrorCode.FAILEDTOCREATESIZECONTROL: "Failed to create size control.",
    ErrorCode.FAILEDTOCREATEPRISMCONTROL: "Failed to create prism control.",
    ErrorCode.SIZINGCONTROL_VOLUMEENTITYNOTSUPPORTED: "Provided sizing control type does not support volume entity.",
    ErrorCode.SIZEFIELDTYPENOTSUPPORTED: "Provided Size Field Type is not supported by this operation.",
    ErrorCode.INVALIDSIZECONTROLS: "Invalid size controls selected to compute size field.",
    ErrorCode.TETIMPROVEFAILED: "Tet improvement failed.",
    ErrorCode.AUTONODEMOVEFAILED: "Tet improvement using auto node movement failed.",
    ErrorCode.COMPUTEVOLUMESFAILED: "Compute volumes failed.",
    ErrorCode.READMESHFAILED: "Reading mesh failed.",
    ErrorCode.WRITEMESHFAILED: "Writing mesh failed.",
    ErrorCode.QUADRATICMESH_WRITEMESHFAILED: "Saving quadratic mesh into .msh format is not supported. Try saving it as .cdb, .m2g or .k File.",
    ErrorCode.CADIMPORTFAILED: "CAD import failed.",
    ErrorCode.READSIZEFIELDFAILED: "Reading size field failed.",
    ErrorCode.WRITESIZEFIELDFAILED: "Writing size field failed.",
    ErrorCode.READCDBFAILED: "Reading CDB failed.",
    ErrorCode.WRITECDBFAILED: "Writing CDB failed.",
    ErrorCode.READKEYWORDFILEFAILED: "Reading K file failed.",
    ErrorCode.WRITEKEYWORDFILEFAILED: "Writing K file failed.",
    ErrorCode.INCLUDEKFILENOTFOUND: "Referenced K file not found.",
    ErrorCode.READSIZECONTROLFAILED: "Reading size control failed.",
    ErrorCode.WRITESIZECONTROLFAILED: "Writing size control failed.",
    ErrorCode.PATHNOTFOUND: "File path not found.",
    ErrorCode.GETSTATISTICSFAILED: "Get statistics failed.",
    ErrorCode.GETELEMENTCOUNTFAILED: "Get element count failed.",
    ErrorCode.EXTRACTFEATURESBYANGLEFAILED: "Feature extraction by angle failed.",
    ErrorCode.EXTRACTFEATURESBYINTERSECTIONFAILED: "Feature extraction by intersection failed.",
    ErrorCode.EXTRACTFEATURESBYEDGESFAILED: "Feature extraction by edge tracing failed.",
    ErrorCode.CREATEEDGEZONELETFAILED: "Create edge zonelets by node path failed.",
    ErrorCode.VOLUMEMESH_MIDNODESNOTSUPPORTED: "Improve volume mesh error: meshes with mid nodes are not supported.",
    ErrorCode.VOLUMEMESHNOTFOUND: "Volume mesh not found.",
    ErrorCode.NOTSUPPORTEDFORNONTRIFACEZONE: "Only triangular faces are supported.",
    ErrorCode.NOTSUPPORTEDFORNONQUADFACEZONE: "Only quadrilateral faces zonelets are supported.",
    ErrorCode.PARTNOTMESHED: "Part has unmeshed topofaces.",
    ErrorCode.MORPHER_COMPUTEBCS: "Failed to compute boundary conditions.",
    ErrorCode.MATCHMORPH_INVALIDSOURCEINPUT: "Invalid source input for match morphing.",
    ErrorCode.MATCHMORPH_BCPAIRINPUTTYPEMISMATCH: "Entity type does not match with input for defined boundary condition pair.",
    ErrorCode.INVALIDGLOBALMINMAX: "Invalid global min, max value.",
    ErrorCode.SETGLOBALSIZINGPARAMSFAILED: "Setting global sizing parameters failed.",
    ErrorCode.INVALIDSIZECONTROLINPUTS: "Invalid size control input. Verify sizing parameters of size control.",
    ErrorCode.INVALIDSIZECONTROLSCOPE: "Invalid size control scope. Failed to evaluate scope for the size control.",
    ErrorCode.NOSIZECONTROLSMATCHINGEXPRESSION: "No size controls found matching the given expression.",
    ErrorCode.INVALIDPROXIMITYSIZINGINPUT: "Invalid proximity sizing input. Elements per gap should be a positive value.",
    ErrorCode.INVALIDCURVATURESIZINGINPUT: "Invalid curvature sizing input. Normal angle should be a positive value.",
    ErrorCode.TRANSFORMATIONFAILED: "Failed to transform.",
    ErrorCode.SCALINGFAILED: "Failed to scale.",
    ErrorCode.ALIGNMENTFAILED: "Failed to align.",
    ErrorCode.INVALIDTRANSFORMATIONMATRIX: "Invalid transformation matrix. You need to provide 16(4x4) elements.",
    ErrorCode.DELETEMESHFACESFAILED: "Failed to delete face element(s).",
    ErrorCode.DELETEFRINGESANDOVERLAPSFAILED: "Failed to delete fringes and overlaps.",
    ErrorCode.DELETEMESHFACES_TOPOLOGYNOTSUPPORTED: "Deletion of face element(s) is not supported for mesh with topology.",
    ErrorCode.DELETEMESHFACES_CELLFOUND: "Cannot delete face element(s) connected to volume mesh.",
    ErrorCode.MATERIALPOINTWITHSAMENAMEEXISTS: "Material point with given name already exist.",
    ErrorCode.MATERIALPOINTWITHGIVENIDDOESNTEXIST: "Material point with given id does not exist.",
    ErrorCode.MATERIALPOINTWITHGIVENNAMEDOESNTEXIST: "Material point with the given name does not exist.",
    ErrorCode.CREATEMATERIALPOINTFAILED: "Creating material point failed.",
    ErrorCode.INVALIDMATERIALPOINT: "Invalid material point provided. Provide the location [x, y, z].",
    ErrorCode.IMPROVESURFACEMESHQUALITYFAILED: "Improve surface mesh quality failed.",
    ErrorCode.REMOVECUSPSFAILED: "Cusp removal failed.",
    ErrorCode.NOTSUPPORTEDFORREMOVECUSPS: "Parts with multiple volumes do not support Cusp removal.",
    ErrorCode.COMPUTEINTERNALREGIONPOINTSFAILED: "Failed to compute internal region points using cap faces.",
    ErrorCode.INTERSECTINGCAPSNOTFOUND: "No intersecting caps found with source geometry for internal region point computation.",
    ErrorCode.IGA_INCORRECTCONTROLPOINTSIZEWRTDEGREE: "Control Points size must be greater than degree.",
    ErrorCode.IGA_INCORRECTCONTROLPOINTSIZEWRTINPUT: "Control Points size cannot be greater than input mesh nodes.",
    ErrorCode.IGA_NURBSFITTINGFAILED: "Failed to fit spline.",
    ErrorCode.IGA_NEGATIVEJACOBIAN: "Negative Jacobian found.",
    ErrorCode.IGA_NURBSOPFAILED: "Spline operation failed.",
    ErrorCode.IGA_PERIODICKNOTVECTORCONVERSIONFAILED: "Periodic knot vector conversion failed.",
    ErrorCode.IGA_HREFINEMENTFAILED: "H refinement failed.",
    ErrorCode.IGA_PREFINEMENTFAILED: "P refinement failed.",
    ErrorCode.IGA_QUADTOSPLINEBASISFAILED: "Quad to spline operation failed.",
    ErrorCode.MULTIZONEMESHER_BLOCKINGFAILED: "MultiZone blocking failed.",
    ErrorCode.MULTIZONEMESHER_MESHINGFAILED: "MultiZone meshing failed.",
    ErrorCode.MULTIZONEMESHER_MESHTRANSFERFAILED: "Mesh transfer from ICEM to Prime failed.",
    ErrorCode.MULTIZONEMESHER_USERINPUTTOPOLOGYMISSING: "Topology not found. Create topology, mesh it and try again.",
    ErrorCode.MULTIZONEMESHER_MULTIPLECONTROLSNOTSUPPORTED: "MultiZone does not support more than one control.",
    ErrorCode.MULTIZONEMESHER_NOVOLUMESFORGEOMETRYTRANSFER: "Incorrect volume scope provided.",
    ErrorCode.MULTIZONEMESHER_NOVOLUMESSCOPEDINCURRENTPART: "No volumes scoped for MultiZone meshing in the current part.",
    ErrorCode.MULTIZONEMESHER_GEOMETRYTRANSFERFAILED: "The transfer of the geometry for MultiZone meshing failed.",
    ErrorCode.MULTIZONEMESHER_INVALIDPRISMPARAMETERS: "The prism parameters for MultiZone are invalid.",
    ErrorCode.MULTIZONEMESHER_PRISMMESHINGFAILED: "The creation of prism layers in the MultiZone mesh failed.",
    ErrorCode.BOIRESULTSFAILED: "BOI creation failed.",
    ErrorCode.CREATEBOI_INVALIDSCALE: "BOI creation failed. Scale factors should not be less than one.",
    ErrorCode.CREATEBOI_INVALIDFLOWDIRECTION: "BOI creation failed. Invalid flow or wake direction.",
    ErrorCode.CREATEBOI_INVALIDWRAPMESHSIZE: "BOI creation failed because wrapping requires a valid mesh size.",
    ErrorCode.CREATEBOI_INVALIDWAKELEVELS: "BOI creation failed. Invalid wake levels input.",
    ErrorCode.CREATEBOI_INVALIDTYPEFORWRAP: "BOI creation failed. Wrapping is invalid for this BOI type.",
    ErrorCode.CREATEBOI_INVALIDSCOPE: "BOI creation failed. Invalid face zonelets as input.",
    ErrorCode.CREATECONTACTPATCH_INVALIDOFFSETDISTANCE: "Contact patch creation process failed. Scale factors should not be less than zero.",
    ErrorCode.CREATECONTACTPATCH_INVALIDCONTACTPATCHAXIS: "Contact patch creation process failed. Invalid Contact patch creation axis.",
    ErrorCode.CONTACTPATCHRESULTSFAILED: "Contact patch creation process failed. Check the inputs.",
    ErrorCode.CREATECONTACTPATCH_INVALIDTOLERANCEVALUE: "Contact patch creation process failed. Tolerance value should not be less than zero.",
    ErrorCode.ADDTHICKNESSRESULTSFAILED: "Adding thickness failed. ",
    ErrorCode.IGA_NURBSSMOOTHFAILED: "Spline smoothing failed.",
    ErrorCode.IGA_NODEINDEXINGFAILED: "Hex-mesh is not structured.",
    ErrorCode.IGA_NOCELLZONELETS: "No cell zonelets found.",
    ErrorCode.IGA_INVALIDINPUTFILEFORSTRUCTUREDHEXMESHFITTING: "Wrong Input mesh. Only structured hex-mesh is allowed.",
    ErrorCode.IGA_INVALIDINPUTFILEFORGENUSZEROFITTING: "Wrong Input file. Only tetrahedral mesh is allowed.",
    ErrorCode.IGA_NOFACEZONELETS: "No face zonelets found.",
    ErrorCode.IGA_EDGEPATHCOMPUTATIONFAILED: "Edge path computation failed.",
    ErrorCode.IGA_INCORRECTDEGREE: "Degree 0 not allowed.",
    ErrorCode.IGA_QUADRATICMESHINPUT: "Quadratic mesh is not supported for solid spline creation.",
    ErrorCode.IGA_UNIFORMTRIMMEDNURBSFAILED: "Failed to create uniform trimmed solid spline.",
    ErrorCode.MERGEPARTSFAILED: "Merge parts failed.",
    ErrorCode.MERGEPARTSWANDWOTOPO: "Merge parts with topology and parts without topology are not supported.",
    ErrorCode.SETNAMEFAILED: "Set name failed.",
    ErrorCode.CONTROLNOTFOUND: "Control not found.",
    ErrorCode.NOINPUT: "No input provided.",
    ErrorCode.DELETEPARTSFAILED: "Delete parts failed.",
    ErrorCode.DELETECONTROLSFAILED: "Delete controls failed.",
    ErrorCode.OCTREELIMITREACHED: "Limit reached for the number of octants supported. Use a coarser sizing and try again.",
    ErrorCode.WRAPPERGLOBALSETTINGSNOTSET: "Wrapper global settings are not set.",
    ErrorCode.WRAPPERRESOLVEINTERSECTIONFAILED: "Wrapper resolve intersection step failed.",
    ErrorCode.WRAPPERCONNECTFAILED: "Wrapper connection generic failure.",
    ErrorCode.WRAPPERFATALERROR: "Wrapper fatal error.",
    ErrorCode.WRAPPERCOULDNOTEXTRACTINTERFACE: "Failed to extract wrapper interface.",
    ErrorCode.WRAPPERLEAKPREVENTIONFAILED: "Wrapper leak prevention generic failure. Dead region is leaking to live.",
    ErrorCode.WRAPPERUNSUPPORTEDWRAPREGION: "Wrap region option provided does not support wrap operation.",
    ErrorCode.WRAPPERCONTROL_NOLIVEMATERIALPOINTSPROVIDED: "Live material points list provided for wrapper control is empty.",
    ErrorCode.WRAPPERSURFACEHASHOLES: "Wrapper surface with holes provided.",
    ErrorCode.WRAPPEROCTREEREGIONINGFAILED: "Wrapper octree regioning generic failure.",
    ErrorCode.WRAPPERPROJECTIONFAILED: "Wrapper projection generic failure.",
    ErrorCode.WRAPPERCONTROL_MATERIALPOINTWITHGIVENNAMEDOESNTEXIST: "Wrapper material point with the given name does not exist.",
    ErrorCode.WRAPPERCONTROL_LIVEMATERIALPOINTDOESNTEXIST: "Wrapper Live material point does not exist.",
    ErrorCode.WRAPPERSIZINGMETHODNOTSUPPORTED: "Sizing method is not supported for wrapper.",
    ErrorCode.WRAPPERSIZEFIELDSNOTDEFINED: "No size field ids provided for wrapping.",
    ErrorCode.WRAPPERIMPROVEFAILED: "Wrapper improve quality failed.",
    ErrorCode.WRAPPERCONTROL_INVALIDCONTACTPREVENTIONCONTROLID: "Contact prevention specified under wrapper control does not exist.",
    ErrorCode.WRAPPERCONTROL_INVALIDCONTACTPREVENTIONCONTROLINPUTS: "Contact prevention control specified under wrapper is invalid.",
    ErrorCode.WRAPPERCONTROL_INVALIDGEOMETRYSCOPE: "Geometry scope specified under wrapper control is invalid.",
    ErrorCode.WRAPPERCONTROL_INVALIDLEAKPREVENTIONID: "Leak prevention specified under wrapper control does not exist.",
    ErrorCode.WRAPPERCONTROL_INVALIDLEAKPREVENTIONCONTROLINPUTS: "Leak prevention control specified under wrapper is invalid.",
    ErrorCode.WRAPPERCONTROL_INVALIDFEATURERECOVERYCONTROLID: "Feature recovery control specified under wrapper control does not exist.",
    ErrorCode.WRAPPERCONTROL_LEAKPREVENTIONMPTCANNOTBELIVE: "Dead material point cannot be same as live.",
    ErrorCode.WRAPPERPATCHFLOWREGIONS_INVALIDHOLESIZE: "Hole size specified for dead region should be positive double.",
    ErrorCode.WRAPPERPATCHFLOWREGIONS_FAILED: "Failed to create patching surfaces.",
    ErrorCode.WRAPPERPATCHFLOWREGIONS_TOOSMALLHOLESIZE: "Too small hole size provided for dead region.",
    ErrorCode.WRAPPERPATCHFLOWREGIONS_INVALIDBASESIZE: "Base size specified for patching should be positive double.",
    ErrorCode.WRAPPERPATCHFLOWREGIONS_EMPTYORINVALIDINPUT: "Provided face zonelet ids for dead region are empty or invalid.",
    ErrorCode.INVALIDWRAPPERCONTROL: "Invalid wrapper control.",
    ErrorCode.WRAPPERCLOSEGAPS_INVALIDGAPSIZE: "Gap size specified for close gaps should be positive double.",
    ErrorCode.WRAPPERCLOSEGAPS_INVALIDSCOPE: "Scope specified for close gaps is invalid.",
    ErrorCode.WRAPPERCLOSEGAPSFAILED: "Wrapper gap closing failed.",
    ErrorCode.WRAPPERCLOSEGAPS_INVALIDRESOLUTIONFACTOR: "Resolution Factor should be greater than 0 but less than or equal to 1.",
    ErrorCode.WRAPPERLEAKINGFLUIDREGIONS: "Two or more fluid regions leaking into each other.",
    ErrorCode.AUTOMESHINVALIDMAXSIZE: "AutoMeshParams has invalid max size specified.",
    ErrorCode.INVALIDPRISMCONTROLS_INCORRECTSCOPEENTITY: "Invalid scope entity.",
    ErrorCode.INVALIDFIRSTASPECTRATIO: "Invalid first aspect ratio.",
    ErrorCode.INVALIDLASTASPECTRATIO: "Invalid last aspect ratio.",
    ErrorCode.INVALIDFIRSTHEIGHT: "Invalid first height.",
    ErrorCode.INVALIDLAYERS: "Invalid number of layers.",
    ErrorCode.INVALIDGROWTHRATE: "Invalid growth rate.",
    ErrorCode.AUTOMESHHEXCOREFAILED: "Failed to create hexcore mesh.",
    ErrorCode.INVALIDVOLUMECONTROLS: "Conflict of volume controls on volumes or invalid volume controls selected.",
    ErrorCode.SURFERINVALIDMINORMAXSIZES: "Invalid min, max size or growth rate provided for surface meshing.",
    ErrorCode.SURFERINVALIDANGLES: "Invalid corner angle or min more than max angle provided for surface meshing.",
    ErrorCode.SMOOTHSIZETRANSITIONNOTSUPPORTEDFORTOPO: "Smooth size transition option is not supported for topology surface meshing.",
    ErrorCode.SURFACESEARCHFAILED: "Surface search failed.",
    ErrorCode.INVALIDINPUTZONELETS: "Invalid input zonelets for surface search.",
    ErrorCode.SURFACESEARCHPARTWITHMESHNOTFOUND: "Part with mesh not found for surface quality check.",
    ErrorCode.VOLUMESEARCHPARTWITHMESHNOTFOUND: "Part with mesh not found for volume quality check.",
    ErrorCode.VOLUMESEARCHFAILED: "Volume search failed.",
    ErrorCode.INVALIDCELLQUALITYLIMIT: "Invalid cell quality limit.",
    ErrorCode.MESHCHECKFAILED: "Mesh check failed.",
    ErrorCode.FILLHOLEFAILED: "Unable to create capping surface.",
    ErrorCode.UNITEZONELETSFAILED: "Failed to unite input zonelets.",
    ErrorCode.INVALIDINPUTPART: "Part is invalid.",
    ErrorCode.INVALIDSCOPEENTITYTYPEINPUT: "Invalid input scope entity type.",
    ErrorCode.ENTITIESSHOULDBEADDEDTOZONEUSINGPARTITBELONGS: "Entities should be added to zone using part it belongs.",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORPMDAT: "Provided file extension is not supported. Supported extensions are .pmdat and .pmdat.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTMESHINGMESH: "Provided file extension is not supported. If cff_format is set to False, then supported extensions are .msh and .msh.gz. If cff_format is set to True, then supported extension is .msh.h5",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTCASE: "Provided file extension is not supported. Supported extensions are .cas and .cas.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORKEYWORDFILE: "Provided file extension is not supported. Supported extensions are .k and .key",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORMAPDLCDB: "Provided file extension is not supported. Supported extension is .cdb",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTSIZEFIELD: "Provided file extension is not supported. Supported extensions are .sf and .sf.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORSIZEFIELD: "Provided file extension is not supported. Supported extensions are .psf and .psf.gz",
    ErrorCode.INVALIDFILEEXTENSIONFORFLUENTCASEEXPORT: "Provided file extension is invalid. If cff_format is set to False, then supported extensions are .cas and .cas.gz. If cff_format is set to True, then supported extension is .cas.h5 .",
    ErrorCode.SUBTRACTZONELETSFAILED: "Failed to subtract cutters from input face zonelets.",
    ErrorCode.QUADRATICTETNOTSUPPORTEDINPARALLEL: "Quadratic tetrahedral meshing is not supported in parallel mode.",
    ErrorCode.QUADRATICTETNOTSUPPORTEDWITHPRISMS: "Quadratic tetrahedral meshing is not supported with prisms.",
    ErrorCode.PARTHASTOPOLOGY: "Part has a topology.",
    ErrorCode.PARTDOESNOTHAVETOPOLOGY: "Part does not have a topology.",
    ErrorCode.ZONESARENOTSUPPORTEDFORCELLZONELETS: "Zones are not supported for cell zonelets.",
    ErrorCode.TARGETZONELETS_NOTWATERTIGHT: "Zonelets of target do not form a watertight volume.",
    ErrorCode.TARGETZONELETS_SELFINTERSECTING: "Zonelets of target form a self intersecting volume.",
    ErrorCode.TOOLZONELETS_NOTWATERTIGHT: "Zonelets of tool do not form a watertight volume.",
    ErrorCode.TOOLZONELETS_SELFINTERSECTING: "Zonelets of tool form a self intersecting volume.",
    ErrorCode.STACKER_INVALIDINPUTVOLUMES: "Invalid input volumes provided to stacker.",
    ErrorCode.STACKER_INVALIDPARAMS: "Invalid parameters provided to stacker.",
    ErrorCode.STACKER_FACESEPARATIONFAILED: "Stacker failed to separate base face.",
    ErrorCode.STACKER_FAILED: "Stacker failed to mesh the model.",
    ErrorCode.STACKER_NOFACEFOUNDINVOLUMES: "No face found in specified volumes.",
    ErrorCode.STACKER_MESHEDFACESFOUND: "Some faces have existing mesh.",
    ErrorCode.STACKER_INVALIDBASEFACEINPUT: "Base face list input has invalid ids.",
    ErrorCode.STACKER_NONSTACKABLEVOLUMESFOUND: "Some volumes are not aligned in the stacking direction.",
    ErrorCode.STACKER_INCORRECTBODYDEFINITION: "Some bodies are intersecting or incorrectly defined.",
    ErrorCode.STACKER_BASEFACEUNMESHED: "Base face list input has unmeshed topofaces.",
    ErrorCode.PLUGINLOADFAILURE: "Failed to load surface editor plugin.",
    ErrorCode.INPUTNOTCOMPLETE: "Input provided is incomplete.",
    ErrorCode.SURFERCANNOTREMESHPERIODICZONELETS: "Remesh is not supported for periodic face zonelets.",
    ErrorCode.EXTRACTVOLUMESFAILED: "Extract volumes failed.",
    ErrorCode.EXTRACTEXTERNALFLOWVOLUMEFAILED: "Extract external flow volume failed.",
    ErrorCode.EXTERNALFLOWINTERSECTIONFAILED: "External flow part connection with main part failed. Check overlapping surfaces between the parts.",
    ErrorCode.EXTRACTMRFVOLUMEFAILED: "Extract MRF volume failed.",
    ErrorCode.MRFINTERSECTIONFAILED: "MRF part connection with main part failed. Check overlapping surfaces between the parts.",
    ErrorCode.REFINEATCONTACTSFAILED: "Failed to refine at contacts.",
    ErrorCode.RECOVERPERIODICSURFACESFAILED: "Failed to recover periodic surfaces.",
    ErrorCode.RECOVERPERIODICSURFACESINVALIDSCOPE: "Source face zonelets are empty. Invalid scope input.",
    ErrorCode.CHECKPERIODICPAIRSFAILED: "Failed to recover periodic surfaces. No matching periodic face pair found. Check the inputs.",
    ErrorCode.PERIODICSURFACESEDGESMISMATCH: "Failed to recover periodic surfaces. Edge entities do not match on periodic source and target surfaces.",
    ErrorCode.PERIODICRECOVERYFORALREADYVOLUMEMESHEDPART: "Already volume meshed. Periodic recovery unsupported.",
    ErrorCode.CREATECAPONFACEZONELETSFAILED: "Failed to create cap on face zonelets.",
    ErrorCode.INTERSECTIONINTARGETVOLUMES: "Found overlapping or intersecting target volumes.",
    ErrorCode.INTERSECTIONINCUTTERVOLUMES: "Found overlapping or intersecting cutter volumes.",
    ErrorCode.SUBTRACTVOLUMEFAILED: "Failed to subtract volumes.",
    ErrorCode.ZONELETSARENOTOFSAMEDIMENSION: "Zonelets are not of same dimension.",
    ErrorCode.MERGEZONELETSFAILED: "Merge zonelets failed.",
    ErrorCode.MERGESMALLZONELETSSUPPORTEDFORFACEZONELETS: "Merge small zonelets option is supported for only face zonelets.",
    ErrorCode.MERGEVOLUMESFAILED: "Merge volumes failed.",
    ErrorCode.DELETEVOLUMESFAILED: "Delete volumes failed.",
    ErrorCode.INVALIDNEIGHBORVOLUMES: "Invalid neighbor volumes selected to merge volumes.",
    ErrorCode.INVALIDINPUTVOLUMES: "Invalid input volumes.",
    ErrorCode.FUSEOPTIONINVALID: "Invalid option chosen to connect two different parts.",
    ErrorCode.COLOCATEFUSEDNODESFAILED: "Colocation of fused nodes failed.",
    ErrorCode.IMPRINTBOUNDARYNODESFAILED: "Imprint of boundary nodes failed.",
    ErrorCode.IMPRINTBOUNDARYEDGESFAILED: "Imprint of boundary edges failed.",
    ErrorCode.SPLITINTERSECTINGBOUNDARYEDGESFAILED: "Splitting of intersecting boundary edges failed.",
    ErrorCode.FUSEINTERIORFAILED: "Fusing interior region of overlap failed.",
    ErrorCode.TOLERANCEVALUEINVALID: "Invalid tolerance value specified.",
    ErrorCode.INVALIDTHINVOLUMECONTROLS: "Invalid thin volume control.",
    ErrorCode.SOURCEORTARGETNOTSPECIFIED: "No target or source faces specified.",
    ErrorCode.THINVOLUMECONTROLINVALIDSOURCESCOPE: "Source scope not found.",
    ErrorCode.THINVOLUMECONTROLINVALIDTARGETSCOPE: "Target scope not found.",
    ErrorCode.THINVOLUMECONTROLINVALIDVOLUMESCOPE: "Volume scope not found.",
    ErrorCode.THINVOLUMECONTROLINVALIDSCOPE: "Source scope and target scope cannot be same.",
    ErrorCode.THINVOLUMECONTROLINVALIDSOURCESCOPEENTITY: "Invalid source scope entity.",
    ErrorCode.THINVOLUMECONTROLINVALIDTARGETSCOPEENTITY: "Invalid target scope entity.",
    ErrorCode.THINVOLUMECONTROLINVALIDNUMBEROFLAYER: "Number of layer in thin volume mesh should be greater than 0.",
    ErrorCode.THINVOLUMECONTROLTOPOLOGYNOTSUPPORTED: "Thin volume mesh controls not supported for part with topology data.",
    ErrorCode.THINVOLUMECONTROLINVALIDCONTROL: "Same face scope is set as target for multiple thin volume controls.",
    ErrorCode.THINVOLUMECONTROLSAMESOURCEFORMORETHANTWOCONTROL: "Same face scope is set as source for more than two thin volume controls.",
    ErrorCode.THINVOLUMEMESHNOTSUPPORTEDWITHFACEBASEDDATABASE: "Thin volume mesh is not supported with face based database.",
    ErrorCode.EXPORTSTLFAILED: "Export STL failed.",
    ErrorCode.EXPORTSTLFAILEDWITHTOPOLOGY: "Export STL not supported for part with topology data.",
    ErrorCode.EXPORTSTLFAILEDWITHQUADFACES: "Export STL not supported for mesh with quad faces.",
    ErrorCode.EXPORTSTLFAILEDWITHPOLYFACES: "Export STL not supported for mesh with poly faces.",
    ErrorCode.EXPORTSTLFAILEDWITHHIGHERORDERMESH: "Export STL not supported for higher order mesh.",
    ErrorCode.EXPORTSTLFAILEDWITHEMPTYPARTIDLIST: "Export STL failed. List of part ids is empty.",
    ErrorCode.EXPORTSTLFAILEDWITHINCORRECTPARTID: "Export STL failed. Part id is incorrect.",
    ErrorCode.SOURCEFACINGCELLZONELETS: "Source face zonelets facing existing volume mesh.",
    ErrorCode.TARGETWITHCELLZONELETS: "Target face zonelets with volume mesh on both sides.",
    ErrorCode.SIDEZONELETSNOTFIT: "Side face zonelets are not sweepable for thin volume mesh.",
    ErrorCode.SOURCETARGETZONELETSNOTFIT: "Source and target zonelets do not fit to thin volume mesh.",
    ErrorCode.AUTOQUADMESHER_INVALIDMINMAXSIZES: "Minimum size is more than maximum size.",
    ErrorCode.AUTOQUADMESHER_NEGATIVEINPUTPARAMETER: "Input parameters contain one or more negative values.",
    ErrorCode.FACEZONELETSHAVECELLSCONNECTED: "Face zonelets have cells connected.",
    ErrorCode.IMPORTABAQUSFAILEDWITHUNKNOWNERROR: "Failed to import abaqus file. Unknown error.",
    ErrorCode.IMPORTABAQUSFAILEDWITHPARSINGFAILURE: "Failed to import abaqus file. Failed to parse file.",
    ErrorCode.IMPORTABAQUSFAILEDDURINGMESHCREATION: "Failed to import abaqus file. Mesh creation failed after parsing.",
    ErrorCode.ZEROELEMENTSREADFROMCDBFILE: "No mesh elements found. Check the input CDB file.",
    ErrorCode.ZERONODESREADFROMCDBFILE: "No nodes found. Check the input CDB file.",
    ErrorCode.INVALIDCMBLOCKFORMAT: "CMBLOCK command format error in input CDB file. Check command syntax or data format.",
    ErrorCode.ZEROELEMENTSFORCDBEXPORT: "No mesh elements found for CDB export. Check if the model is meshed, or set write_by_zones in ExportMapdlCdbParams to false if zones are not defined.",
    ErrorCode.SHELLBLFAILED: "ShellBL creation failed.",
    ErrorCode.SHELLBLQUADS: "ShellBL produced quadrilateral elements that require refinement.",
    ErrorCode.SHELLBLNOMESH: "ShellBL is not supported for unmeshed topofaces.",
    ErrorCode.SHELLBLFEWLAYERS: "Only few ShellBL layers are created.",
    ErrorCode.SHELLBLWRONGTOPO: "Found topofaces with invalid topology.",
    ErrorCode.READSHELLBLCONTROLFAILED: "Read thin ShellBL control failed.",
    ErrorCode.SHELLBLCONTROLFAILED: "Write ShellBL control failed.",
    ErrorCode.OGRIDREFINEFAILED: "Post refinement of ShellBl quads failed.",
    ErrorCode.SPLITTOTRIFAILED: "ShellBL quads split to triangles failed.",
    ErrorCode.INVALIDSHELLBLCONTROLS: "Invalid ShellBL controls.",
    ErrorCode.INVALIDSHELLBLCONTROLS_INCORRECTSCOPEENTITY: "Invalid scope entity.",
    ErrorCode.PERIODICEDGESNOTSUPPORTEDFORSHELLBL: "Periodic surfaces selected for ShellBL generation are not supported.",
    ErrorCode.INVALIDINPUTPOINT: "Invalid input point.",
    ErrorCode.TOPOFACESPLITNOTSUPPORTED: "ComputeTopoVolumes and ExtractTopoVolumes do not support topoface split.",
    ErrorCode.COULDNOTLOADHAMMERSTEINPLUGIN: "Failed to load Hammerstein GPU Plugin.",
    ErrorCode.PRECOMPUTEDVOLUMESEXIST: "Pre-computed volumes exist.",
    ErrorCode.GPUOUTOFMEMORY: "GPU out of memory.",
    ErrorCode.GPUFATALERROR: "Fatal error in GPU meshing.",
    ErrorCode.CPUOUTOFMEMORY: "CPU out of memory.",
    ErrorCode.NOSIZINGINPUT: "No sizing input provided.",
    ErrorCode.NOPARTSFOUNDWITHEXPRESSION: "No parts found matching the part expression.",
    ErrorCode.INVALIDFILEEXTENSIONFORPRIMEPROJECT: "Provided file extension is not supported. Supported extension is .prproject.",
    ErrorCode.CREATEPROJECTFILEFOLDERFAILED: "Unable to create folder to store prime project files.",
    ErrorCode.CREATEPROJECTFILEFAILED: "Unable to create prime project file.",
    ErrorCode.CREATESTRIDEFILEFAILED: "Unable to create stride file.",
    ErrorCode.ERRORREADINGSTRIDEDATA: "Unable to read stride data.",
    ErrorCode.STRIDECONVERTFAILED: "Unable to convert to stride file.",
    ErrorCode.INVALIDCHECKPOINTNAME: "Invalid checkpoint name provided. Checkpoint name should not start or end with space character and should not contain special characters.",
    ErrorCode.ERRORREADINGCHECKPOINTHISTORY: "Unable to read checkpoint history.",
    ErrorCode.CHECKPOINTNOTFOUND: "Checkpoint not found.",
    ErrorCode.CHECKPOINTALREADYEXISTS: "Checkpoint already exists.",
    ErrorCode.CADIMPORTXMLFILEGENERATIONFAILED: "CAD Import XML file generation failed.",
    ErrorCode.CADIMPORTFMTRANSMOGRIFIEREXENOTFOUND: "CAD Import FM Transmogrifier executable file not found.",
    ErrorCode.EXTRACTFLOWVOLUMECAPFAILURE: "Flow volume extraction failed due to cap connection failure.",
    ErrorCode.STACKER_MESHTRANSFERTOBASEFAILED: "Mesh transfer from model to base face failed.",
    ErrorCode.STACKER_NONIDENTICALMESHEDFACESFOUND: "Mesh transfer from model to base face failed because of non-identical mesh on horizontally overlapping faces.",
    ErrorCode.STACKER_MESHTOTOPOASSOCIATIONFAILED: "Stacker failed to associate mesh to model.",
    ErrorCode.STACKER_VOLUMEMESHINGFAILED: "Stacker failed to mesh some input bodies. Check for overlapping or duplicate bodies and ensure that the mesh size and tolerance are adequate to resolve geometric features.",
    ErrorCode.STACKER_CONFLICTINGSIZES: "Stacker failed because of conflict in seed face stack layers. Check Seed Face Scope for mismatch in layers or conflicts with lateral faces of the model.",
    ErrorCode.STACKER_SEEDFACEMESHINVALID: "Stacker failed. Seed faces for stacking should either have edge mesh or fully quad face mesh. Deviation of nodes on face mesh at each layer should be within the stacking tolerance.",
    ErrorCode.STACKER_PARTIALEDGEMESHONBASE: "Stacker failed because edge mesh from Seed Faces could not be transferred due to conflicting mesh from other faces.",
    ErrorCode.STACKER_NONIDENTICALEDGEMESHONBASE: "Stacker failed because edge mesh from Seed Faces are conflicting with each other. Mesh from seed edges projecting to the same set of base edges should have identical mesh.",
    ErrorCode.STACKER_EDGEMESHBASEMAPNOTFOUND: "Stacker failed because some mesh edges could not be assigned to any edge on the base. Base edges may have shifted due to tolerance or the edge may have collapsed. Check lateral defeature tolerance.",
    ErrorCode.STACKER_FACEMESHMISMATCHONBASE: "Mesh transfer to base face failed. Mesh from seed faces projecting to the same set of base faces should have identical mesh.",
    ErrorCode.STACKER_BASEFACEPARTITIONFAILED: "Mesh transfer to base face failed during association of the projected seed face mesh on the base face.",
    ErrorCode.STACKER_SEEDFACEBOUNDARYMERGEFAILED: "Mesh transfer to base face failed because edge mesh from laterally adjacent seed faces were conflicting. Edge mesh from seed faces projecting to the same set of base edges should have identical mesh.",
    ErrorCode.MERGENODES_MULTIPARTINPUTNOTSUPPORTED: "Source or target face inputs span multiple parts. Cross-part merge is not supported.",
    ErrorCode.MERGENODES_INPUTNOTCOMPLETE: "Source or target face expression resolved to no meshed face zonelets.",
    ErrorCode.MERGENODES_FAILED: "Merge nodes operation failed.",
    ErrorCode.VOLUMESLICER_INVALIDINPUTLOOPEDGES: "Input edges do not form well-defined closed loops.",
    ErrorCode.VOLUMESLICER_NOINPUTTOPOVOLUMES: "No topovolumes scoped in input for splitting.",
    ErrorCode.VOLUMESLICER_INVALIDPLANEDEFINITIONS: "Invalid input plane definitions.",
    ErrorCode.VOLUMESLICER_INVALIDSOURCETARGETDATA: "Invalid input source or target data for blend.",
    ErrorCode.VOLUMESLICER_SPLITFACESGENERATIONFAILED: "Failed to generate any interfaces to split volumes.",
    ErrorCode.VOLUMESLICER_PREVIEWFACESGENERATIONFAILED: "Failed to generate any interfaces for preview.",
    ErrorCode.VOLUMESLICER_INVALIDCONTROLID: "Invalid input control id.",
    ErrorCode.VOLUMESLICER_SPLITTOPOVOLUMESFAILED: "Failed to split topovolumes after generating the interfaces.",
    ErrorCode.VOLUMESLICER_NOINPUTCONTROLIDS: "No control ids provided as input.",
    ErrorCode.VOLUMESLICER_NOINPUTEDGES: "No input edges provided.",
    ErrorCode.VOLUMESLICER_INVALIDSOURCEEDGES: "Source edges do not form a valid closed loop for blend.",
    ErrorCode.VOLUMESLICER_INVALIDTARGETEDGES: "Target edges do not form a valid closed loop for blend.",
    ErrorCode.VOLUMESLICER_MULTIPLESOURCELOOPS: "Multiple source loops found; blend requires a single loop.",
    ErrorCode.VOLUMESLICER_MULTIPLETARGETLOOPS: "Multiple target loops found; blend requires a single loop.",
}

prime_warning_messages = {
    WarningCode.NOWARNING: "Success.",
    WarningCode.UNKNOWN: "Unknown Warning.",
    WarningCode.SURFER_QUADCLEANUP_MULTITHREADINGNOTSUPPORTED: "Warning: Multithreading is skipped for quad cleanup.",
    WarningCode.SURFERLAYEREDQUADFAILED: "Surface Meshing Warning: Layered quad region has triangles.",
    WarningCode.SURFERDEGENERATEFACE: "Surface Meshing Warning: Face has degenerate edge mesh.",
    WarningCode.ALIGN_OPERATIONINTERRUPTED: "Align Warning: Operation is interrupted by the user. Result can be inaccurate.",
    WarningCode.NOHOLESFOUNDONPLANE: "No closed hole found in given face zonelets at given plane.",
    WarningCode.IGA_NOGEOMZONELETFORSPLINEFITTING: "Geometric face zonelet is not available for spline fitting.",
    WarningCode.NOVOLUMESCOMPUTED: "There are no volumes computed.",
    WarningCode.NOVOLUMESENCLOSINGMATERIALPOINT: "There are no computed volumes enclosing the given material point.",
    WarningCode.EXTERNALOPENFACEZONELETSFOUND: "External open face zonelets found.",
    WarningCode.EXTERNALOPENTOPOFACESFOUND: "External open topofaces found.",
    WarningCode.VT_CANNOTMERGENODES: "Cannot merge nodes during VT operation.",
    WarningCode.VT_REMESHFACEFAILED: "Failed to remesh face(s) during VT operation.",
    WarningCode.VT_SKIPPEDENTITIESINDIFFERENTZONES: "Input contains entities in different zones which have been skipped.",
    WarningCode.VT_SKIPPEDFEATUREENTITIES: "Input contains feature entities which have been skipped.",
    WarningCode.VT_SKIPPEDFREEEDGES: "Input contains free edges which have been skipped.",
    WarningCode.VT_SKIPPEDNONMANIFOLDEDGES: "Input contains non-manifold edges which have been skipped.",
    WarningCode.VT_SKIPPEDPROTECTEDENTITIES: "Input contains protected entities which have been skipped.",
    WarningCode.VT_FACESEPARATIONFAILED: "Created interior edges but failed to separate one or more faces into multiple regions during topology modification operation.",
    WarningCode.VT_SKIPPEDFACESWITHNOPLANEINTERSECTION: "Skipped one or more faces because they do not intersect with the input plane.",
    WarningCode.VT_SKIPPEDCUSPTOPOEDGES: "Input contains cusp topoedges which have been skipped.",
    WarningCode.VT_VOLUMENOTMERGEDNOSHAREDFACE: "One or more input volumes were skipped during merge as they have no shared face with any other input volume.",
    WarningCode.VT_VOLUMEMESHDELETED: "Deleted volume mesh on one or more adjacent volumes to allow face splitting.",
    WarningCode.VT_VOLUMENOTMERGEDPROTECTEDSHAREDFACE: "One or more input volumes were skipped during merge as they have a protected shared face.",
    WarningCode.VT_VOLUMENOTMERGEDSHAREDFACEDIFFERENTPARTS: "One or more input volumes were skipped during merge as their shared face spans different parts.",
    WarningCode.VT_VOLUMENOTMERGEDSHAREDFACEDIFFERENTZONES: "One or more input volumes were skipped during merge as their shared face spans different zones.",
    WarningCode.VOLUMETRICSCAFFOLDER_SPLITBYINTERIOREDGESFAILURE: "Split by interior edges failed at one or more locations.",
    WarningCode.VOLUMETRICSCAFFOLDER_UNRESOLVEDOVERLAPS: "One or more unresolved overlapping faces are present after resolving surface overlaps.",
    WarningCode.VOLUMETRICSCAFFOLDER_FREEFACES: "One or more free faces are present after resolving surface overlaps.",
    WarningCode.OVERRIDECURVATURESIZINGPARAMS: "Invalid curvature sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDESOFTSIZINGPARAMS: "Invalid soft sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEHARDSIZINGPARAMS: "Invalid hard sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEPROXIMITYSIZINGPARAMS: "Invalid proximity sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEBOISIZINGPARAMS: "Invalid BOI sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEMESHEDSIZINGPARAMS: "Invalid meshed sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDESOISIZINGPARAMS: "Invalid SOI sizing parameters override by global sizing parameters.",
    WarningCode.INVALIDSIZECONTROLSCOPE: "Invalid size control type provided.",
    WarningCode.OVERRIDEGROWTHRATEPARAM: "Overriding growth rate parameter.",
    WarningCode.PRESCRIBEDSIZEBELOWMINREPRESENTABLESINGLEPRECISION: "Prescribed sizes are less than minimum representable size with respect to largest dimension of domain for single precision and will not be respected. Use double precision to represent smaller sizes.",
    WarningCode.PRESCRIBEDSIZEBELOWMINREPRESENTABLEDOUBLEPRECISION: "Prescribed sizes are less than minimum representable size with respect to largest dimension of domain and will not be respected.",
    WarningCode.OVERRIDESURFACESCOPEENTITY: "Invalid surface scope entity, override by face zonelets.",
    WarningCode.OVERRIDEVOLUMESCOPEENTITY: "Invalid volume scope entity, override by volume.",
    WarningCode.MAXOFPRISMCONTROLSMINASPECTRATIO: "Maximum value of min aspect ratio from selected prism controls is considered for all selected prism controls.",
    WarningCode.PARTNOTINPARTSCOPE: "The selected part is not in the part scope of the periodic control.",
    WarningCode.NUMERICPARTNAMERENAMETOALPHANUMERIC: "Numeric part name renamed to alphanumeric name.",
    WarningCode.OVERRIDESUGGESTEDNAME: "Given name not available. Overriding it with unique name.",
    WarningCode.WRAPPER_SIZECONTROLNOTDEFINED: "No size controls provided for wrapper. Global sizes will be used.",
    WarningCode.WRAPPER_SIZECONTROLNOTSUPPORTED: "Size control is not supported in wrapper. Skipping it.",
    WarningCode.WRAPPER_SMALLERCONTACTPREVENTIONSIZE: "Contact prevention size is smaller than base size. Size will be adjusted to base size.",
    WarningCode.WRAPPER_SMALLERSIZEATFEAURES: "Size at features is smaller than base size. Size will be adjusted to base size.",
    WarningCode.WRAPPER_PATCHFLOWREGIONS_NOHOLESFOUND: "No holes detected to patch",
    WarningCode.MATERIALPOINTWITHSAMENAMEEXISTS: "Material point with same name exists. Overriding with unique name.",
    WarningCode.LOCALSURFERNOFACEREGISTERED: "No face registered with the given register id.",
    WarningCode.ENTITIESNOTBELONGTOANYZONE: "Entities not belong to any zone.",
    WarningCode.INVALIDENTITIESNOTADDEDTOZONE: "Entities with invalid id or invalid type are not added to the zone.",
    WarningCode.DUPLICATEINPUT: "Duplicate items in input.",
    WarningCode.MESHHASNONPOSITIVEVOLUMES: "Mesh has non positive volumes.",
    WarningCode.MESHHASNONPOSITIVEAREAS: "Mesh has non positive areas.",
    WarningCode.MESHHASINVALIDSHAPE: "Mesh has invalid shape.",
    WarningCode.MESHHASLEFTHANDEDNESSFACES: "Mesh has left handed faces.",
    WarningCode.FACEZONELETSWITHOUTVOLUMES: "Face zonelets have no volume associated to them.",
    WarningCode.JOINEDZONELETSFROMMULTIPLEVOLUMES: "Joined zonelets from more than two volumes. The volumes are not auto updated on the zonelets.",
    WarningCode.FAILEDTOUPDATEVOLUMES: "Volumes are not updated after performing the operation.  Compute the volumes again.",
    WarningCode.UNPROCESSEDKEYWORDSINABAQUSFILE: "Some keywords are not processed. Check the unprocessed keywords in the summary log of the import results.",
    WarningCode.EXPORTMAPDLANALYSISSETTINGSFAILED: "Export of analysis settings to separate file failed.",
    WarningCode.WRITINGCONTACTPAIRSSKIPPED: "Writing of contact pairs skipped due to no surface or surface interaction definition.",
    WarningCode.WRITINGTIESSKIPPED: "Writing of ties skipped due to no surface definition.",
    WarningCode.WRITINGZONELETOFLABELTOELEMENTCOMPONENTSKIPPED: "Skipped the export of label as element component because the labelled topology or zonelets are not a part of any zone. Refer label_export_params to export desired labels as nodal components.",
    WarningCode.IMPORTOFNODALCOMPONENTASLABELSKIPPED: "Skipped the import of nodal component as label because no element fully represents nodal component.",
    WarningCode.MULTIZONEMESHER_SURFACESCOPEVOLUMESCOPEINCONSISTENCY: "Topofaces of the volumes scoped are more than the topofaces of the surface scoped.",
    WarningCode.MULTIZONEMESHER_DEFEATUREDTOPOFACES: "Topofaces that got defeatured in the MultiZone mesh.",
    WarningCode.MULTIZONEMESHER_DEFEATUREDTOPOEDGES: "Topoedges that got defeatured in the MultiZone mesh.",
    WarningCode.MULTIZONEMESHER_DEFEATUREDPROTECTEDTOPOLOGY: "Protected toponodes or topoedges that got defeatured in the MultiZone mesh.",
    WarningCode.NOCADGEOMETRYFOUND: "CAD geometry not found for some or all topoentities. Skipped projection for those topoentities.",
    WarningCode.NOCADGEOMETRYPROJECTONFACETS: "CAD geometry not found for some or all topoentities. Mesh node projected on facets for those topoentities.",
    WarningCode.FUSEOVERLAPREMOVALINCOMPLETE: "Self intersections found. Use Fuse operation to remove it.",
    WarningCode.REMOVEOVERLAPWITHINTERSECT: "Self intersections found. Use Intersect operation to remove it.",
    WarningCode.OVERRIDEEDGESCOPEENTITY: "Override edge scope entity.",
    WarningCode.SHELLBLGAPFACTORMINLIMIT: "Adjusted ShellBL gap factor to 0.001. As 0.001 is minimum value supported.",
    WarningCode.REMOVECUSP_PARTWITHMULTIPLEVOLUMES: "Parts with multiple volume do not support for cusp removal.",
    WarningCode.MESHHASINVALIDPARTITIONSTATE: "Mesh has invalid partition state.",
    WarningCode.STACKER_MESHTOTOPOASSOCIATIONFAILED: "Stacker failed to associate mesh to model.",
    WarningCode.STACKER_SIZESLARGERTHANMAXOFFSETFOUND: "Size controls with sizes larger than maximum offset size found.",
    WarningCode.STACKER_SIZESSMALLERTHANTOLERANCEFOUND: "Size controls with sizes smaller than tolerance found.",
    WarningCode.STACKER_UNMESHEDFACES: "Stacker failed to mesh some faces. Check for overlapping faces, reduce tolerance value or both.",
    WarningCode.STACKER_SIZINGSIGNOREDINFAVOROFSEEDFACESCOPE: "Stacker does not respect some sizings due to conflict with mesh from Seed Face Scope.",
    WarningCode.STACKER_CONFORMALMESHINGFAILED: "Volume meshing is completed and has non-conformal mesh due to intersections among the input volumes.",
    WarningCode.STACKER_NUMBEROFDIVISIONSSPLITATGEOMETRY: "Number of divisions specified for some edges could not be respected due to geometry constraints.",
    WarningCode.STACKER_NUMBEROFDIVISIONSNOTRESPECTED: "Number of divisions specified for some edges could not be respected due to conflicting controls. The smaller sizing among the controls was applied.",
    WarningCode.STACKER_HORIZONTALEDGESUSEDFORSMALLESTSTACKINGEDGES: "Horizontal edges are used for indicating smallest stacking edges",
    WarningCode.STACKER_NOSTACKABLEBODIESDETECTED: "No stackable bodies were detected among the input volumes.",
    WarningCode.CONNECT_ONETOONEMAPPINGNOTFOUND: "One-to-one mapping between source and target zonelets not found. Check connectivity information or provide smaller tolerance value.",
    WarningCode.CONNECT_NODESINTARGETZONELETSNOTMERGED: "Some or all nodes in target zonelets could not be merged with nodes in the source zonelets.",
    WarningCode.VOLUMESLICER_SPLITFACEGENERATIONFAILED: "Failed to generate split faces for one or more controls.",
    WarningCode.VOLUMESLICER_PREVIEWFACEGENERATIONFAILED: "Failed to generate preview faces for one or more controls.",
    WarningCode.VOLUMESLICERCONTROL_PLANENOINTERSECTION: "Plane does not intersect target volume.",
    WarningCode.VOLUMESLICERCONTROL_PLANENOCLOSEDBOUNDARY: "Plane intersects the target volume but does not form a valid split region.",
    WarningCode.VOLUMESLICERCONTROL_UNIQUETOPOVOLUMENOTFOUND: "Failed to find a unique volume to split for the given control.",
    WarningCode.VOLUMESLICERCONTROL_SOURCETARGETPROJECTIONFAILED: "Failed to project source edges on target faces for the blend control.",
    WarningCode.VOLUMESLICERCONTROL_SPLITFACEOVERLAPSTOPOLOGY: "Failed to generate split faces for the control. The input split region overlaps with the existing topology and cannot divide the volumes into valid regions.",
    WarningCode.VOLUMESLICERCONTROL_SPLITFACEOUTSIDEVOLUMEBOUNDARY: "Failed to generate split faces for the given control. The input split region does not divide the volumes into valid regions.",
    WarningCode.VOLUMESLICERCONTROL_LOOPSPLITFACEGENERATIONFAILED: "Failed to generate split faces for the loop control.",
    WarningCode.VOLUMESLICERCONTROL_PLANARSPLITFACEGENERATIONFAILED: "Failed to generate split faces for the plane control.",
    WarningCode.VOLUMESLICERCONTROL_LOOPPREVIEWFACEGENERATIONFAILED: "Failed to generate preview faces for the loop control.",
    WarningCode.VOLUMESLICERCONTROL_PLANARPREVIEWFACEGENERATIONFAILED: "Failed to generate preview faces for the plane control.",
    WarningCode.VOLUMESLICERCONTROL_BLENDSPLITFACEGENERATIONFAILED: "Failed to generate split faces for the blend control.",
    WarningCode.VOLUMESLICERCONTROL_BLENDPREVIEWFACEGENERATIONFAILED: "Failed to generate preview faces for the blend control.",
    WarningCode.VOLUMESLICER_UNCLOSEDSEGMENTSIGNORED: "Input contains unclosed edge segments. Such segments are ignored while processing.",
    WarningCode.VOLUMESLICER_INVALIDPLANEDEFINITIONSIGNORED: "Input contains invalid plane definitions. Such plane definitions are ignored while processing.",
    WarningCode.VOLUMESLICERCONTROL_SPLITFACEINTERSECTSTOPOLOGY: "Failed to generate split faces for the control. The split region intersects with the existing topology.",
    WarningCode.VOLUMESLICERCONTROL_VOLUMEMESHDELETED: "Deleted volume mesh on one or more volumes to allow volume splitting.",
    WarningCode.NUMEN_SURFACEMESHELEMENTCOUNTVALIDATIONFAILED: "Numen surface mesh element count validation failed.",
    WarningCode.NUMEN_SELFINTERSECTIONSVALIDATIONFAILED: "Numen self intersections count validation failed.",
    WarningCode.NUMEN_FREEEDGESVALIDATIONFAILED: "Numen free edges count validation failed.",
    WarningCode.NUMEN_MULTIEDGESVALIDATIONFAILED: "Numen multi edges count validation failed.",
    WarningCode.NUMEN_QUADELEMENTCOUNTVALIDATIONFAILED: "Numen quad element count validation failed.",
    WarningCode.NUMEN_POLYELEMENTCOUNTVALIDATIONFAILED: "Numen poly element count validation failed.",
    WarningCode.NUMEN_INVALIDNORMALSCOUNTVALIDATIONFAILED: "Numen invalid normals count validation failed.",
    WarningCode.NUMEN_FACESABOVECRITERIAVALIDATIONFAILED: "Numen faces above quality criterion validation failed.",
    WarningCode.NUMEN_DIHEDRALANGLEVALIDATIONFAILED: "Numen dihedral angle validation failed.",
    WarningCode.NUMEN_VOLUMEMESHCHECKVALIDATIONFAILED: "Numen volume mesh check validation failed.",
    WarningCode.NUMEN_TOTALFACECOUNTVALIDATIONFAILED: "Numen total face element count validation failed.",
    WarningCode.NUMEN_TOTALCELLCOUNTVALIDATIONFAILED: "Numen total cell element count validation failed.",
    WarningCode.NUMEN_FLUIDSPRISMCELLCOUNTVALIDATIONFAILED: "Numen fluids prism cell count validation failed.",
    WarningCode.NUMEN_SOLIDSPRISMCELLCOUNTVALIDATIONFAILED: "Numen solids prism cell count validation failed.",
    WarningCode.NUMEN_HEXCELLCOUNTVALIDATIONFAILED: "Numen hex cell count validation failed.",
    WarningCode.NUMEN_POLYCELLCOUNTVALIDATIONFAILED: "Numen poly cell count validation failed.",
    WarningCode.NUMEN_PYRAMIDCELLCOUNTVALIDATIONFAILED: "Numen pyramid cell count validation failed.",
    WarningCode.NUMEN_TETCELLCOUNTVALIDATIONFAILED: "Numen tet cell count validation failed.",
    WarningCode.NUMEN_CELLSABOVECRITERIAVALIDATIONFAILED: "Numen cells above quality criterion validation failed.",
    WarningCode.NUMEN_SELFINTERSECTIONSFOUND: "Self intersecting face elements found during surface diagnostics.",
    WarningCode.NUMEN_FREEEDGESFOUND: "Free edge elements found during surface diagnostics.",
    WarningCode.NUMEN_AUTOCOMPUTEDEADMPTS_EMPTYINTERNALCAPSCOPE: "Internal cap part expression resolved to an empty scope during automatic dead material point computation. Provide a valid part expression that resolves to internal cap surface (sheet) parts.",
    WarningCode.NUMEN_AUTOCOMPUTEDEADMPTS_NOINTERNALCAPTOPOFACES: "No internal cap topofaces were found for automatic dead material point computation. Ensure internal cap parts exist and match the given expression.",
    WarningCode.NUMEN_NOCAPFOUNDWARNING: "No caps found during model precheck analysis. This may affect extract_flow_volume operation.",
    WarningCode.NUMEN_BAFFLEDETECTED: "Baffles in this workflow are free-floating surfaces with no direct connection to solid body edges. They are handled exclusively by the WRAP operation which captures them inside the wrapped geometry. Baffles are only compatible with the WRAPPED SOLID workflow. Using baffles with conformal or non-conformal workflows will produce incorrect results. Ensure the wrapped solid workflow is selected.",
    WarningCode.NUMEN_FACEZONECOUNTVALIDATIONFAILED: "Numen face zone count validation failed.",
    WarningCode.NUMEN_VOLUMEZONECOUNTVALIDATIONFAILED: "Numen volume zone count validation failed.",
    WarningCode.NUMEN_FACEZONEENTITYCOUNTVALIDATIONFAILED: "Numen face zone entity count validation failed.",
    WarningCode.NUMEN_VOLUMEZONEENTITYCOUNTVALIDATIONFAILED: "Numen volume zone entity count validation failed.",
    WarningCode.NUMEN_MRFPARTNOTFOUND: "MRF part not found. MRF extraction will be skipped. Ensure the MRF part expression matches at least one part.",
}


class PrimeRuntimeError(Exception):
    """Provides runtime errors for PyPrimeMesh.

    Parameters
    ----------
    message : str
        Error message to show.
    error_code : ErrorCode, optional
        ID of the error. The default is ``None``.
    error_locations : Any, optional
        Location of the error. The default is ``None``.
    """

    def __init__(self, message: str, error_code: ErrorCode = None, error_locations=None):
        """Initialize the error message."""
        super().__init__()
        self._message = self.__process_message(message)
        self._error_code = error_code
        self._error_locations = error_locations

    def __str__(self) -> str:
        """Transform the message to a string."""
        return self._message

    def __repr__(self) -> str:
        """Provide the full string representation of the error."""
        args = [f"message={self._message!r}"]
        # Skip default arguments
        if self._error_code is not None:
            args.append(f"error_code={self._error_code!r}")
        if self._error_locations is not None:
            args.append(f"error_locations={self._error_locations!r}")
        return f"{self.__class__.__name__}({', '.join(args)})"

    def __process_message(self, message: str):
        """Process the message to be digested by the error class.

        Parameters
        ----------
        message : str
            Message to process.

        Returns
        -------
        str
            Processed message.
        """
        output_message = message
        if "Invalid Parameter Type: " in message:
            param_names = message[len("Invalid Parameter Type: ") :].split(".")
            output_message = "Invalid Parameter Type: " + param_names[0]
            if len(param_names) > 1:
                for name in param_names[1:]:
                    output_message += "." + re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        return output_message

    @property
    def message(self):
        """Error message to be reported."""
        return self._message

    @property
    def error_code(self) -> ErrorCode:
        """Error code representing the error."""
        return self._error_code

    @property
    def error_locations(self) -> list:
        """Locations associated with the error."""
        return self._error_locations


class PrimeRuntimeWarning(UserWarning):
    """Provides the runtime warning for PyPrimeMesh.

    Parameters
    ----------
    message : str
        Message to show.
    """

    def __init__(self, message):
        """Initialize the warning message."""
        super().__init__()
        self._message = message

    def __str__(self) -> str:
        """Transform the message to a string."""
        return self._message

    @property
    def message(self):
        """Warning message to be reported."""
        return self._message


def process_and_handle_results(result: dict):
    """Process and handle results."""
    if result is not None:
        if isinstance(result, dict):
            error_code = result.get('errorCode', None)
            error_location_arr = result.get('errorLocations', None)
            error_locations = (
                [error_location_arr[i : i + 3] for i in range(0, len(error_location_arr), 3)]
                if error_location_arr is not None
                else []
            )
            if error_code is not None:
                if error_code > 0:
                    error_location_msg = (
                        f'\nError Locations: {error_locations}' if len(error_locations) > 0 else f''
                    )
                    raise PrimeRuntimeError(
                        prime_error_messages.get(
                            ErrorCode(error_code), f'Unrecogonized error code {error_code}'
                        )
                        + error_location_msg,
                        ErrorCode(error_code),
                        error_locations,
                    )

            prime_warnings = []
            single_warning = result.get('warningCode', None)
            if single_warning is not None and single_warning > 0:
                prime_warnings.append(single_warning)

            multiple_warnings = result.get('warningCodes', None)
            if multiple_warnings:  # Note that this will filter out empty list as well
                [prime_warnings.append(w) for w in multiple_warnings]

            if prime_warnings:
                import warnings

                [
                    warnings.warn(
                        prime_warning_messages.get(WarningCode(w), f'Unrecogonized warning {w}'),
                        PrimeRuntimeWarning,
                        stacklevel=4,
                    )
                    for w in prime_warnings
                ]
    return result


def communicator_error_handler(
    _func=None,
    *,
    expected_token="Results",
    server_error_token="ServerError",
    info_token="info_msg",
    warning_token="warning_msg",
    error_token="err_msg",
):
    """Create a decorator to use in error handling.

    Parameters
    ----------
    _func : Func, optional
        Function to use as decorator. The default is ``None``.
    expected_token : str, optional
        Token to expect in the response result. The default is ""Results"".
    server_error_token : str, optional
        Token from the server error. The default is ``"ServerError"``.
    info_token : str, optional
        Information message. The default is ``"info_msg"``.
    warning_token : str, optional
        Warning message. The default is ``"warning_msg"``.
    error_token : str, optional
        Error message. The default is ``"err_msg"``.
    """

    def decorator_handle_errors(func):
        @wraps(func)
        def wrapper_handle_errors(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if func_result is None:
                return func_result
            server_error = func_result.get(server_error_token, None)
            if server_error:
                raise PrimeRuntimeError(server_error)
            result = func_result.get(expected_token, None)
            if result is not None:
                if isinstance(result, dict):
                    import logging

                    info = result.get(info_token, None)
                    if info:
                        logging.info(info)
                    warning = result.get(warning_token, None)
                    if warning:
                        logging.warning(warning)
                    error = result.get(error_token, None)
                    if error:
                        logging.error(error)
                return result
            else:
                return func_result

        return wrapper_handle_errors

    if _func is None:
        return decorator_handle_errors
    else:
        return decorator_handle_errors(_func)


def error_code_handler(_func=None):
    """Decode errors from the server.

    Parameters
    ----------
    _func : Func, optional
        Decorator to apply to the error code. The default is ``None``.
    """

    def decorator_error_code(func):
        @wraps(func)
        def wrapper_error_code(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except RuntimeError as err:
                import logging

                logging.exception(err)
                raise
            return process_and_handle_results(result=result)

        return wrapper_error_code

    if _func is None:
        return decorator_error_code
    else:
        return decorator_error_code(_func)


def apply_if(decorator, condition):
    """Apply a function based on a condition.

    Parameters
    ----------
    decorator : Func
        Function to apply.
    condition : bool
        Condition to check.
    """

    def decorator_apply_if(func):
        if not condition:
            return func
        return decorator(func)

    return decorator_apply_if
