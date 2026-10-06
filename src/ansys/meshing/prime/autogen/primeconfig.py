# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
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

""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np


class ErrorCode(enum.IntEnum):
    """Error codes associated with the failure of PyPrimeMesh operation.
    """
    NOERROR = 0
    """No error."""
    UNKNOWN = 1
    """Unknown error."""
    SIGSEGV = 2
    """Segmentation violation."""
    SURFERFAILED = 3
    """Surface meshing failed."""
    TOPOFACESREMESHFAILED = 4
    """Failed to remesh topofaces."""
    TOPOEDGESREMESHFAILED = 5
    """Failed to remesh topoedges."""
    SURFERLAYEREDQUADFAILED = 6
    """Failed to layer quad meshing."""
    SURFERINVALIDINPUT = 7
    """Invalid input for surface meshing."""
    SURFERQUADFAILED = 8
    """Quad surface meshing failed."""
    SURFERWITHAUTOSIZINGFAILED = 9
    """Surface meshing with auto sizing failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FACEZONELETSFEATURESNOTUPTODATE = 10
    """Face zonelets features are not up to date."""
    SURFERAUTOSIZEQUADUNSUPPORTED = 11
    """Auto sizing for quad meshing is not supported."""
    SURFERAUTOSIZEMUSTBEVOLUMETRIC = 12
    """Auto sizing must be of volumetric type."""
    SURFERDEGENERATEFACE = 13
    """Face is degenerated for surface meshing.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SURFERNONMANIFOLDEDGE = 14
    """Non manifold edge for meshing."""
    MAPMESHINGFAILED = 15
    """Surfer map meshing operation failed."""
    SURFEROPENINITIALFRONTLOOP = 16
    """Open initial front loop for meshing."""
    FREEZEMESHERROR = 30
    """The mesh is frozen and cannot be remeshed."""
    REMESHFACEZONELETSNOTSUPPORTEDFORTOPOLOGYPART = 31
    """Remesh face zonelets is not supported for topology part."""
    REMESHFACEZONELETSLOCALLYNOTSUPPORTEDFORTOPOLOGYPART = 32
    """Remesh face zonelets locally is not supported for topology part."""
    SURFERINVALIDCONSTANTSIZE = 40
    """Invalid size for constant size surface meshing."""
    SURFERINVALIDMINORMAXSIZES = 41
    """Invalid min or max size for surface meshing."""
    SURFERINVALIDANGLES = 42
    """Invalid Corner angle or min angle more than max angle specified for surface meshing."""
    SMOOTHSIZETRANSITIONNOTSUPPORTEDFORTOPO = 43
    """Smooth size transition option is not supported for topology surface meshing yet."""
    LOCALSURFERINVALIDNUMRINGS = 44
    """Invalid number of rings input for the local surface mesh operation."""
    SURFERCANNOTREMESHPERIODICZONELETS = 45
    """Cannot remesh periodic face zonelets."""
    SUBTRACTVOLUMEFAILED = 47
    """Failed to subtract volumes."""
    INTERSECTIONINTARGETVOLUMES = 48
    """Found overlapping or intersecting target volumes."""
    INTERSECTIONINCUTTERVOLUMES = 49
    """Found overlapping or intersecting cutter volumes."""
    SCAFFOLDERBADINPUTEMPTYTOPO = 50
    """Incorrect input. No topo faces or edges in input."""
    SCAFFOLDERBADINPUTNOFREEFACES = 51
    """Incorrect input. No free faces in input."""
    SCAFFOLDERBADINPUTPARAMS = 52
    """Incorrect input parameters."""
    SCAFFOLDERINVALIDABSOLUTEDISTOL = 53
    """Invalid absolute distance tolerance for scaffold operation."""
    SCAFFOLDERINVALIDCONSTANTMESHSIZE = 54
    """Invalid constant mesh size input for scaffold operation."""
    SHELLBLFAILED = 60
    """ShellBL creation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SHELLBLQUADS = 61
    """ShellBL produced quadrilateral elements that require refinement.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SHELLBLNOMESH = 62
    """ShellBL is not supported for unmeshed topofaces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SHELLBLFEWLAYERS = 63
    """Only few ShellBL layers are created.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SHELLBLWRONGTOPO = 64
    """Found topofaces with invalid topology.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    OGRIDREFINEFAILED = 65
    """Post refinement of ShellBl quads failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SPLITTOTRIFAILED = 66
    """ShellBL quads split to triangles failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INVALIDSHELLBLCONTROLS = 67
    """Invalid ShellBL controls.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INVALIDSHELLBLCONTROLS_INCORRECTSCOPEENTITY = 68
    """Invalid scope entity.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    PERIODICEDGESNOTSUPPORTEDFORSHELLBL = 69
    """Periodic surfaces selected for ShellBL generation are not supported.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    AUTOMESHFAILED = 100
    """Auto meshing failed."""
    AITOVERLAPALONGMULTIFOUND = 101
    """Topology identification failed because of overlapping faces."""
    TRIANGULATIONFAILED = 102
    """Triangulation failed."""
    DUPLICATENODESFOUND = 103
    """Duplicate nodes were found in the input mesh."""
    EDGEINTERSECTINGFACEFOUND = 104
    """Edge intersecting face found."""
    DUPLICATEFACESFOUND = 105
    """Duplicate faces were found in the input mesh."""
    TETIMPROVEFAILED = 106
    """Tet improve failed."""
    AUTONODEMOVEFAILED = 107
    """Auto node move failed."""
    AUTOMESHCELLASSOCIATIONFAILED = 108
    """Auto mesh cell zonelet association failed."""
    ALREADYVOLUMEMESHED = 110
    """Volume is already meshed."""
    INVALIDPRISMCONTROLS = 111
    """Invalid prism controls."""
    VOLUMESNOTUPTODATE = 112
    """Volumes are not updated."""
    QUADRATICMESHSUPPORTEDONLYFORTETS = 113
    """Quadratic elements can only be generated for tetrahedral elements."""
    NOACTIVESFFOUND = 114
    """No active size fields found."""
    AUTOMESHSIZEFIELDTYPENOTSUPPORTED = 115
    """Specified size field type is not supported for the specified volume fill type."""
    AUTOMESHINVALIDMAXSIZE = 116
    """Invalid max size for auto volume meshing."""
    AUTOMESHHEXCOREFAILED = 117
    """Hex generation part of volume meshing failed."""
    INVALIDVOLUMECONTROLS = 118
    """Invalid volume controls specified for volume meshing."""
    SOURCEFACINGCELLZONELETS = 119
    """Source face zonelets facing existing volume mesh."""
    TARGETWITHCELLZONELETS = 120
    """Target face zonelets with volume mesh on both side."""
    SIDEZONELETSNOTFIT = 121
    """Side face zonelets are not sweepable for thin volume mesh."""
    SOURCETARGETZONELETSNOTFIT = 122
    """Source and target zonelets do not fit to thin volume mesh."""
    INVALIDPRISMCONTROLS_INCORRECTSCOPEENTITY = 123
    """Invalid scope entity."""
    INVALIDFIRSTASPECTRATIO = 124
    """Invalid first aspect ratio."""
    INVALIDLASTASPECTRATIO = 125
    """Invalid last aspect ratio."""
    INVALIDFIRSTHEIGHT = 126
    """Invalid first height."""
    INVALIDLAYERS = 127
    """Invalid number of layers."""
    INVALIDGROWTHRATE = 128
    """Invalid growth rate."""
    COMPUTEVOLUMESFAILED = 129
    """Compute volumes failed."""
    QUADRATICTETNOTSUPPORTEDINPARALLEL = 130
    """Quadratic tetrahedral meshing is not supported in parallel mode."""
    QUADRATICTETNOTSUPPORTEDWITHPRISMS = 131
    """Quadratic tetrahedral meshing is not supported with prism."""
    EXTRACTVOLUMESFAILED = 132
    """Extract volumes failed."""
    MERGEVOLUMESFAILED = 133
    """Merge volumes failed."""
    DELETEVOLUMESFAILED = 134
    """Delete volumes failed."""
    PERIODICSURFACESNOTSUPPORTEDFORPRISMS = 135
    """Periodic surfaces selected for prism generation are not supported."""
    INVALIDNEIGHBORVOLUMES = 136
    """Invalid neighbor volumes selected to merge volumes."""
    THINVOLUMEMESHFAILED = 137
    """Thin volume meshing failed."""
    PRISMMESHFAILED = 138
    """Prism meshing failed."""
    AUTOMESHINITFAILED = 139
    """Auto mesh initialization failed."""
    POLYMESHFAILED = 140
    """Poly meshing failed."""
    PYRAMIDMESHFAILED = 141
    """Pyramid meshing failed."""
    DELETEMESHFAILED = 142
    """Deleting mesh failed."""
    INCREMENTALVOLUMEMESHINGNOTSUPPORTED = 143
    """Incremental volume meshing is not supported."""
    TOPOFACESPLITNOTSUPPORTED = 144
    """ComputeTopoVolumes and ExtractTopoVolumes do not support topoface split."""
    TOPOLOGYCLEANUPFAILED = 146
    """Topology cleanup operation failed."""
    SUPPRESSINTERIORTOPOEDGESFAILED = 147
    """Suppress interior topology edges operation failed."""
    SUPPRESSTOPONODESFAILED = 148
    """Suppress topology nodes operation failed."""
    REPAIRTOPOEDGESOFTOPOFACESFAILED = 149
    """Repair topology edges of faces operation failed."""
    INVALIDCONSTANTMESHSIZE = 150
    """Invalid constant mesh size parameter."""
    INVALIDABSOLUTEDISTTOLERANCE = 151
    """Invalid absolute distance tolerance parameter."""
    EXTRACTEXTERNALFLOWVOLUMEFAILED = 152
    """Extract external flow volume failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    EXTERNALFLOWINTERSECTIONFAILED = 153
    """External flow part connection with main part failed. Check overlapping surfaces between the parts.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    EXTRACTMRFVOLUMEFAILED = 154
    """Extract MRF volume failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MRFINTERSECTIONFAILED = 155
    """MRF part connection with main part failed. Check overlapping surfaces between the parts.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SUPPRESSNONFEATURETOPOEDGESFAILED = 156
    """Suppress non-feature topology edges operation failed."""
    SURFACEMESHCHECKFAILED = 157
    """Surface mesh check operation failed."""
    OUTOFMEMORY = 200
    """Out of memory."""
    INTERRUPTED = 201
    """Method call interrupted."""
    COREOBJECTSNOTSYNCEDBETWEENNODES = 202
    """Core objects are not synchronized between parallel nodes."""
    GETSTATISTICSFAILED = 250
    """Failed to get mesh statistics."""
    GETELEMENTCOUNTFAILED = 251
    """Failed to get element count."""
    PARTNOTFOUND = 300
    """Given part not found."""
    TOPODATANOTFOUND = 301
    """TopoData not found."""
    SIZEFIELDNOTFOUND = 302
    """Size field not found."""
    ZONESARENOTOFSAMETYPE = 303
    """Zones are not of same type."""
    PARTNOTMESHED = 304
    """Part is not meshed."""
    INVALIDINPUTPART = 305
    """Invalid input part."""
    CADGEOMETRYNOTFOUND = 306
    """No CAD geometry was found for the requested projections."""
    VOLUMENOTFOUND = 307
    """Volumes not found."""
    ZONENOTFOUND = 308
    """Given zone not found."""
    ENTITIESSHOULDBEADDEDTOZONEUSINGPARTITBELONGS = 309
    """Entities should be added to zone using part it belongs."""
    PARTDOESNOTHAVETOPOLOGY = 310
    """Part does not have topology."""
    ZONESARENOTSUPPORTEDFORCELLZONELETS = 311
    """Zones are not supported for cell zonelets."""
    SPHEREATINVALIDNORMALNODESFAILED = 350
    """Sphere creation at invalid normals failed."""
    PROJECTONCADGEOMETRYFAILED = 351
    """Projection on CAD Geometry failed."""
    SEPARATIONRESULTSFAILED = 360
    """Separation failed."""
    ZONELETSARENOTOFSAMEDIMENSION = 374
    """Zonelets are not of same dimension."""
    ADDTHICKNESSRESULTSFAILED = 380
    """Adding thickness failed."""
    BOIRESULTSFAILED = 381
    """BOI creation failed."""
    CREATEBOI_INVALIDSCALE = 382
    """BOI creation failed. Scale factors should not be less than one."""
    CREATEBOI_INVALIDFLOWDIRECTION = 383
    """BOI creation failed. Invalid flow or wake direction."""
    CREATEBOI_INVALIDWRAPMESHSIZE = 384
    """BOI creation failed because wrapping requires a valid mesh size."""
    CREATEBOI_INVALIDWAKELEVELS = 385
    """BOI creation failed. Invalid wake levels input."""
    CREATEBOI_INVALIDTYPEFORWRAP = 386
    """BOI creation failed. Wrapping is invalid for this BOI type."""
    CREATEBOI_INVALIDSCOPE = 387
    """BOI creation failed. Invalid face zonelets as input."""
    CREATECONTACTPATCH_INVALIDOFFSETDISTANCE = 388
    """Contact patch creation process failed. Scale factors should not be less than zero."""
    CREATECONTACTPATCH_INVALIDTOLERANCEVALUE = 389
    """Contact patch creation process failed. Tolerance value should not be less than zero."""
    CREATECONTACTPATCH_INVALIDCONTACTPATCHAXIS = 390
    """Contact patch creation process failed. Invalid contact patch creation axis."""
    CONTACTPATCHRESULTSFAILED = 391
    """Contact patch creation process failed. Check the inputs."""
    COMPUTEINTERNALREGIONPOINTSFAILED = 392
    """Computation of cap based internal region points failed."""
    INTERSECTINGCAPSNOTFOUND = 393
    """Intersecting caps not found."""
    SIZEFIELDCOMPUTATIONFAILED = 400
    """Size field computation failed."""
    INVALIDSIZECONTROLS = 401
    """Invalid size controls."""
    REFRESHSIZEFIELDSFAILED = 402
    """Refreshing size field failed."""
    FAILEDTOCREATESIZECONTROL = 403
    """Failed to create size control."""
    FAILEDTOCREATEPRISMCONTROL = 404
    """Failed to create prism control."""
    DELETEVOLUMETRICSIZEFIELDSFAILED = 405
    """Deleting volumetric size fields failed."""
    SIZINGCONTROL_VOLUMEENTITYNOTSUPPORTED = 406
    """Provided sizing control type does not support volume entity."""
    READMESHFAILED = 500
    """Reading mesh file failed."""
    WRITEMESHFAILED = 501
    """Writing mesh file failed."""
    CADIMPORTFAILED = 502
    """CAD import failed."""
    READSIZEFIELDFAILED = 503
    """Reading size field file failed."""
    READCDBFAILED = 505
    """Reading CDB file failed."""
    WRITECDBFAILED = 506
    """Writing CDB file failed."""
    PATHNOTFOUND = 511
    """Invalid path."""
    READKEYWORDFILEFAILED = 517
    """Reading LS-Dyna Keyword file failed."""
    WRITEKEYWORDFILEFAILED = 518
    """Writing LS-Dyna Keyword file failed."""
    QUADRATICMESH_WRITEMESHFAILED = 519
    """Writing failed with quadratic mesh."""
    INCLUDEKFILENOTFOUND = 520
    """Include keyword file not found."""
    READSIZECONTROLFAILED = 522
    """Reading size control file failed."""
    WRITESIZECONTROLFAILED = 523
    """Writing size control file failed."""
    FILENOTFOUND = 524
    """File path or name not found."""
    READPMDATFAILED = 525
    """PMDAT file read failed."""
    EXPORTFLUENTCASEFAILED = 526
    """Export fluent case failed."""
    VOLUMEZONESNOTFOUNDTOEXPORTFLUENTCASE = 527
    """Volume zones are not found to export fluent case."""
    IMPORTFLUENTMESHINGMSHFAILED = 528
    """Failed to import fluent meshing mesh file."""
    IMPORTFLUENTCASEFAILED = 529
    """Failed to import fluent case file."""
    WRITEPMDATFAILED = 530
    """Failed to write PMDAT file."""
    EXPORTFLUENTMESHINGMSHFAILED = 531
    """Export fluent meshing mesh failed."""
    WRITESIZEFIELDFAILED = 532
    """Writing size field failed."""
    MESHNOTFOUNDTOEXPORTFLUENTMESHINGMESH = 533
    """Mesh not found to export fluent meshing mesh."""
    EXPORTSTLFAILED = 549
    """Export STL failed."""
    EXPORTSTLFAILEDWITHTOPOLOGY = 553
    """Export STL not supported for part with topology data."""
    EXPORTSTLFAILEDWITHQUADFACES = 554
    """Export STL not supported for mesh with quad faces."""
    EXPORTSTLFAILEDWITHPOLYFACES = 555
    """Export STL not supported for mesh with poly faces."""
    EXPORTSTLFAILEDWITHHIGHERORDERMESH = 556
    """Export STL not supported for higher order mesh."""
    EXPORTSTLFAILEDWITHEMPTYPARTIDLIST = 557
    """Export STL failed. List of part ids is empty."""
    EXPORTSTLFAILEDWITHINCORRECTPARTID = 558
    """Export STL failed. Part id is incorrect."""
    SHELLBLCONTROLFAILED = 566
    """Write ShellBL control failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    READSHELLBLCONTROLFAILED = 567
    """Read thin ShellBL control failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FUSEOPTIONINVALID = 850
    """Invalid option chosen to connect two different parts."""
    COLOCATEFUSEDNODESFAILED = 851
    """Colocation of fused nodes failed."""
    IMPRINTBOUNDARYNODESFAILED = 852
    """Imprint of boundary nodes failed."""
    IMPRINTBOUNDARYEDGESFAILED = 853
    """Imprint of boundary edges failed."""
    SPLITINTERSECTINGBOUNDARYEDGESFAILED = 854
    """Splitting of intersecting boundary edges failed."""
    FUSEINTERIORFAILED = 855
    """Fusing interior region of overlap failed."""
    TOLERANCEVALUEINVALID = 856
    """Invalid tolerance value specified."""
    SOURCEORTARGETNOTSPECIFIED = 857
    """No target or source faces specified."""
    STITCHWITHPRESERVEDENTITIESFAILED = 858
    """Stitch with preserved entities failed."""
    STITCHENTITIESFAILED = 859
    """Stitch entities failed."""
    EXTRACTFLOWVOLUMECAPFAILURE = 860
    """Flow volume extraction failed due to cap connection failure."""
    NOTSUPPORTEDFORTOPOLOGYPART = 1200
    """Not supported for part with topology data."""
    NOTSUPPORTEDFORHIGHERORDERMESHPART = 1201
    """Operation does not support higher order elements."""
    NOTSUPPORTEDFORNONTRIFACEZONE = 1202
    """Only triangular face zone is supported."""
    NOTSUPPORTEDFORNONQUADFACEZONE = 1203
    """Operation supports only quads."""
    ADDINGPROVIDEDENTITIESNOTSUPPORTEDFORTOPOLOGYPART = 1205
    """Adding provided entities is not supported for part with topology data."""
    MERGEZONELETSNOTSUPPORTEDFORTOPOLOGYPART = 1206
    """Merge zonelets is not supported for part with topology data."""
    MERGEVOLUMESNOTSUPPORTEDFORTOPOLOGYPART = 1207
    """Merge volumes is not supported for part with topology data."""
    NOTSUPPORTEDFORPOLYMESHPART = 1208
    """Operation does not support poly elements."""
    NOPARTSFOUNDWITHEXPRESSION = 1214
    """No parts found matching the specified expression."""
    MERGEPARTSFAILED = 1301
    """Merge parts failed."""
    MERGEPARTSWANDWOTOPO = 1302
    """Merge parts with topology and parts without topology are not supported."""
    SETNAMEFAILED = 1303
    """Set name failed."""
    CONTROLNOTFOUND = 1304
    """Control not found."""
    NOINPUT = 1305
    """No input provided."""
    DELETEPARTSFAILED = 1306
    """Delete parts failed."""
    DELETECONTROLSFAILED = 1307
    """Delete controls failed."""
    INPUTNOTCOMPLETE = 1308
    """Input provided is incomplete."""
    INVALIDINPUTZONELETS = 1309
    """Invalid input zonelets."""
    MERGEZONELETSFAILED = 1310
    """Merge zonelets failed."""
    MERGESMALLZONELETSSUPPORTEDFORFACEZONELETS = 1311
    """Merge small zonelets option is supported for only face zonelets."""
    INVALIDINPUTVOLUMES = 1312
    """List of volume ids provided is empty or incorrect."""
    MORPHER_COMPUTEBCS = 1410
    """Failed to compute boundary conditions."""
    MATCHMORPH_INVALIDSOURCEINPUT = 1450
    """Invalid source input for match morphing."""
    MATCHMORPH_BCPAIRINPUTTYPEMISMATCH = 1451
    """Entity type does not match with input for defined boundary condition pair."""
    INVALIDGLOBALMINMAX = 1500
    """Invalid global min and max value."""
    INVALIDSIZECONTROLINPUTS = 1501
    """Invalid size control input."""
    INVALIDSIZECONTROLSCOPE = 1502
    """Invalid size control scope."""
    INVALIDCURVATURESIZINGINPUT = 1503
    """Invalid curvature sizing input."""
    INVALIDPROXIMITYSIZINGINPUT = 1504
    """Invalid proximity sizing input."""
    INVALIDSCOPEENTITYTYPEINPUT = 1505
    """Invalid input scope entity type."""
    SETGLOBALSIZINGPARAMSFAILED = 1509
    """Setting global sizing parameters failed."""
    NOSIZECONTROLSMATCHINGEXPRESSION = 1510
    """No size controls matched the given size control expression."""
    EXTRACTFEATURESBYANGLEFAILED = 1600
    """Feature extraction by angle failed."""
    EXTRACTFEATURESBYEDGESFAILED = 1601
    """Extracting features by edges failed."""
    CREATEEDGEZONELETFAILED = 1602
    """Creating edge zonelet failed."""
    EXTRACTFEATURESBYINTERSECTIONFAILED = 1603
    """Feature extraction by intersection failed."""
    VOLUMEMESH_MIDNODESNOTSUPPORTED = 1800
    """Mid side nodes are not supported."""
    VOLUMEMESHNOTFOUND = 1801
    """Volume mesh not found."""
    PREPAREFORVOLUMEMESHINGFAILED = 2000
    """Prepare for volume meshing failed."""
    NOTSUPPORTEDFORDISTRIBUTEMESHING = 2001
    """Method not supported for distributed meshing."""
    SPLITANDCOLLAPSEFACEELEMENTSFAILED = 2101
    """Failed to split and collapse face element(s)."""
    IMPROVESURFACEMESHQUALITYFAILED = 2102
    """Improve surface mesh quality failed."""
    REMOVECUSPSFAILED = 2103
    """Cusp removal failed."""
    NOTSUPPORTEDFORREMOVECUSPS = 2104
    """Parts with multiple volumes do not support Cusp removal."""
    IGA_NURBSOPFAILED = 2400
    """Spline operation failed."""
    IGA_INCORRECTCONTROLPOINTSIZEWRTDEGREE = 2401
    """Incorrect control point size with respect to degree."""
    IGA_INCORRECTCONTROLPOINTSIZEWRTINPUT = 2402
    """Incorrect control point size with respect to mesh size."""
    IGA_NURBSFITTINGFAILED = 2403
    """Spline fitting failed."""
    IGA_NEGATIVEJACOBIAN = 2404
    """Spline has negative jacobian."""
    IGA_PERIODICKNOTVECTORCONVERSIONFAILED = 2405
    """Periodic knot conversion of spline failed."""
    IGA_HREFINEMENTFAILED = 2406
    """H-refinement of spline failed."""
    IGA_PREFINEMENTFAILED = 2407
    """P-refinement of spline failed."""
    IGA_NURBSSMOOTHFAILED = 2408
    """Smoothing of spline failed."""
    IGA_NODEINDEXINGFAILED = 2409
    """Hex mesh is unstructured."""
    IGA_NOCELLZONELETS = 2410
    """No cell zonelets found."""
    IGA_INVALIDINPUTFILEFORSTRUCTUREDHEXMESHFITTING = 2411
    """Invalid model for structured hex-mesh spline fitting."""
    IGA_INVALIDINPUTFILEFORGENUSZEROFITTING = 2412
    """Invalid model for genus-zero spline fitting."""
    IGA_NOFACEZONELETS = 2413
    """No face zonelets found."""
    IGA_EDGEPATHCOMPUTATIONFAILED = 2414
    """Edge path computation failed."""
    IGA_INCORRECTDEGREE = 2415
    """Incorrect degree."""
    IGA_QUADRATICMESHINPUT = 2416
    """Quadratic mesh is not supported for solid spline creation."""
    IGA_UNIFORMTRIMMEDNURBSFAILED = 2417
    """Uniform trimmed spline creation failed."""
    IGA_QUADTOSPLINEBASISFAILED = 2421
    """Quad to spline operation failed."""
    MULTIZONEMESHER_INVALIDPRISMPARAMETERS = 2599
    """The prism parameters for MultiZone are invalid."""
    MULTIZONEMESHER_GEOMETRYTRANSFERFAILED = 2600
    """Geometry import of prime topology failed."""
    MULTIZONEMESHER_BLOCKINGFAILED = 2601
    """Creating MultiZone blocking failed."""
    MULTIZONEMESHER_PRISMMESHINGFAILED = 2602
    """Creating MultiZone boundary layers failed."""
    MULTIZONEMESHER_MESHINGFAILED = 2603
    """Generating MultiZone mesh failed."""
    MULTIZONEMESHER_MESHTRANSFERFAILED = 2604
    """MultiZone mesh transfer failed."""
    MULTIZONEMESHER_USERINPUTTOPOLOGYMISSING = 2610
    """Input does not have topology for MultiZone mesh."""
    MULTIZONEMESHER_MULTIPLECONTROLSNOTSUPPORTED = 2611
    """MultiZone mesh does not support multiple controls."""
    MULTIZONEMESHER_NOVOLUMESFORGEOMETRYTRANSFER = 2612
    """No volumes for geometry import."""
    MULTIZONEMESHER_NOVOLUMESSCOPEDINCURRENTPART = 2613
    """No volumes for geometry import in the current part."""
    PARTHASTOPOLOGY = 2800
    """Part has a topology."""
    SURFACESEARCHFAILED = 2802
    """Surface search failed."""
    SURFACESEARCHPARTWITHMESHNOTFOUND = 2803
    """Part with mesh not found for surface quality check."""
    INVALIDPLANEPOINTS = 2804
    """Invalid plane points, cannot define a plane."""
    PLANECOLLINEARPOINTS = 2805
    """Collinear or duplicate points given to define plane."""
    INVALIDREGISTERID = 2806
    """Invalid register id provided. Register ids between 1 to 28 are valid."""
    SURFACEFEATURETYPENOTSUPPORTED = 2807
    """Surface search for provided feature type is not supported."""
    VOLUMESEARCHPARTWITHMESHNOTFOUND = 2850
    """Part with mesh not found for volume quality check."""
    VOLUMESEARCHFAILED = 2851
    """Volume search failed."""
    INVALIDCELLQUALITYLIMIT = 2852
    """Invalid cell quality limit."""
    MESHCHECKFAILED = 2853
    """Mesh check failed."""
    FILLHOLEFAILED = 2901
    """Unable to create capping surface."""
    SUBTRACTZONELETSFAILED = 2903
    """Unable to subtract cutters from input zonelets."""
    CREATECAPONFACEZONELETSFAILED = 2906
    """Failed to create cap on face zonelets."""
    UNITEZONELETSFAILED = 2907
    """Failed to unite input zonelets."""
    REFINEATCONTACTSFAILED = 2908
    """Failed to refine at contacts."""
    RECOVERPERIODICSURFACESFAILED = 2909
    """Unable to recover periodic surfaces."""
    RECOVERPERIODICSURFACESINVALIDSCOPE = 2910
    """Invalid scope input for periodic surface recovery."""
    CHECKPERIODICPAIRSFAILED = 2911
    """Could not find a matching periodic face pair."""
    PERIODICSURFACESEDGESMISMATCH = 2912
    """Edge entities do not match on periodic source and target surfaces."""
    PERIODICRECOVERYFORALREADYVOLUMEMESHEDPART = 2913
    """Periodic recovery unsupported for already volume meshed part."""
    TRANSFORMATIONFAILED = 3000
    """Transformation failed."""
    SCALINGFAILED = 3001
    """Scaling failed."""
    ALIGNMENTFAILED = 3002
    """Alignment failed."""
    INVALIDTRANSFORMATIONMATRIX = 3003
    """Invalid transformation matrix."""
    DELETEMESHFACESFAILED = 3200
    """Delete Mesh faces failed."""
    DELETEMESHFACES_TOPOLOGYNOTSUPPORTED = 3201
    """Topoentities do not support deleting faces."""
    DELETEMESHFACES_CELLFOUND = 3202
    """Deleting faces failed as they have cell neighbors."""
    DELETEFRINGESANDOVERLAPSFAILED = 3203
    """Deleting fringes and overlaps failed."""
    DELETEZONELETSCONNECTEDTOCELLS = 3204
    """Cannot delete zonelets connected to volume mesh."""
    DELETEZONELETSFAILED = 3205
    """Delete zonelets failed."""
    MATERIALPOINTWITHSAMENAMEEXISTS = 3300
    """Material point with the same name already exists."""
    MATERIALPOINTWITHGIVENNAMEDOESNTEXIST = 3301
    """Material point with the given name does not exist."""
    MATERIALPOINTWITHGIVENIDDOESNTEXIST = 3302
    """Material point with the given ID already exists."""
    CREATEMATERIALPOINTFAILED = 3304
    """Creating material point failed."""
    INVALIDMATERIALPOINT = 3305
    """Invalid material point provided. Provide the location [x, y, z]."""
    OCTREELIMITREACHED = 3350
    """Limit reached for the number of octants supported.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    WRAPPERGLOBALSETTINGSNOTSET = 3400
    """Global settings for wrapper not set."""
    WRAPPERRESOLVEINTERSECTIONFAILED = 3401
    """Resolving intersections failed for wrapper."""
    WRAPPERCONNECTFAILED = 3402
    """Wrapper connect failed."""
    WRAPPERFATALERROR = 3403
    """Wrapper fatal error."""
    WRAPPERCOULDNOTEXTRACTINTERFACE = 3405
    """Failed to extract wrapper interface."""
    WRAPPERLEAKPREVENTIONFAILED = 3406
    """Wrapper leak prevention failed."""
    WRAPPERUNSUPPORTEDWRAPREGION = 3407
    """Wrap region option provided does not support wrap operation."""
    WRAPPERCONTROL_NOLIVEMATERIALPOINTSPROVIDED = 3408
    """Live material points list provided for wrapper control is empty."""
    WRAPPERSURFACEHASHOLES = 3410
    """Wrapper surface has holes."""
    WRAPPEROCTREEREGIONINGFAILED = 3411
    """Octree regioning failed."""
    WRAPPERPROJECTIONFAILED = 3412
    """Projection failed for wrapper."""
    WRAPPERCONTROL_MATERIALPOINTWITHGIVENNAMEDOESNTEXIST = 3413
    """Live material point added to wrapper control doesn't exist."""
    WRAPPERCONTROL_LIVEMATERIALPOINTDOESNTEXIST = 3414
    """Live material point does not exist for wrapper."""
    WRAPPERSIZINGMETHODNOTSUPPORTED = 3415
    """Sizing method is not supported for wrapper."""
    WRAPPERIMPROVEFAILED = 3416
    """Wrapper improve quality failed."""
    WRAPPERSIZEFIELDSNOTDEFINED = 3419
    """No size field ids provided for wrapping."""
    WRAPPERCONTROL_INVALIDGEOMETRYSCOPE = 3420
    """Geometry scope specified under wrapper control is invalid."""
    WRAPPERCONTROL_INVALIDCONTACTPREVENTIONCONTROLID = 3421
    """Contact prevention specified under wrapper control doesn't exist."""
    WRAPPERCONTROL_INVALIDCONTACTPREVENTIONCONTROLINPUTS = 3422
    """Contact prevention control specified under wrapper is invalid."""
    WRAPPERCONTROL_INVALIDLEAKPREVENTIONID = 3423
    """Leak prevention specified under wrapper control doesn't exist."""
    WRAPPERCONTROL_INVALIDLEAKPREVENTIONCONTROLINPUTS = 3424
    """Leak prevention control specified under wrapper is invalid."""
    WRAPPERCONTROL_INVALIDFEATURERECOVERYCONTROLID = 3425
    """Feature recovery control specified under wrapper control doesn't exist."""
    WRAPPERCONTROL_LEAKPREVENTIONMPTCANNOTBELIVE = 3426
    """Dead material point cannot be same as live."""
    INVALIDWRAPPERCONTROL = 3427
    """Invalid wrapper control."""
    WRAPPERCLOSEGAPS_INVALIDGAPSIZE = 3440
    """Gap size specified for patching should be positive double."""
    WRAPPERCLOSEGAPS_INVALIDSCOPE = 3441
    """Scope specified for close gaps is invalid."""
    WRAPPERCLOSEGAPSFAILED = 3442
    """Wrapper gap closing failed."""
    WRAPPERCLOSEGAPS_INVALIDRESOLUTIONFACTOR = 3443
    """Resolution Factor should be greater than 0 but less than or equal to 1."""
    WRAPPERLEAKINGFLUIDREGIONS = 3444
    """Two or more fluid regions leaking into each other.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    WRAPPERPATCHFLOWREGIONS_INVALIDHOLESIZE = 3445
    """Hole size specified for dead region should be positive double.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    WRAPPERPATCHFLOWREGIONS_FAILED = 3446
    """Unable to create patch surfaces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    WRAPPERPATCHFLOWREGIONS_TOOSMALLHOLESIZE = 3447
    """Too small hole size provided for dead region.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    WRAPPERPATCHFLOWREGIONS_INVALIDBASESIZE = 3448
    """Base size specified for patching should be positive double.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    WRAPPERPATCHFLOWREGIONS_EMPTYORINVALIDINPUT = 3449
    """Empty or invalid input face zonelet ids.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_INVALIDINPUT = 3600
    """Invalid input provided for VT operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_MERGEFACESFAILED = 3601
    """Merge faces operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_MERGETHINSTRIPESFAILED = 3602
    """Merge thin stripes operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_MERGETHINEXTFAILED = 3603
    """Merge thin extensions operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_REPAIRSHARPCORNERANGLESFAILED = 3604
    """Repair sharp corner angles operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_PINCHFACESFAILED = 3605
    """Pinch faces operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_FILLHOLEFAILED = 3606
    """Fill hole operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_FILLANNULARHOLEFAILED = 3607
    """Fill annular hole operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_COLLAPSESHORTEDGESFAILED = 3608
    """Collapse short edges operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SEPARATEFACESFAILED = 3609
    """Separate faces operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_CREATELEADINGEDGEFAILED = 3610
    """Create leading edge operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_CREATEMIDEDGEFAILED = 3611
    """Create mid edge operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_OPERATIONFAILED = 3612
    """VT operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_PROTECTEDENTITIESFOUND = 3614
    """The input for VT operation has protected entities.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_INTERIOREDGETRACINGFAILED = 3615
    """Failed to trace interior edge during VT operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_REMESHFACEFAILED = 3616
    """Failed to remesh face during VT operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_MERGEEDGESFAILED = 3617
    """Failed to merge edges through common nodes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VTMERGEVOLUMESNOSHAREDFACESFOUND = 3618
    """Failed to find input topovolumes with shared faces for merging.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_MERGEVOLUMESFAILED = 3619
    """Merge topovolumes operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    JSONKEYNOTFOUND = 3801
    """JSON key not found."""
    NUMENMETHODNOTFOUND = 3901
    """Could not find numen method."""
    NUMEN_AUTOCOMPUTEDEADMPTS_EMPTYEXTERNALCAPSCOPE = 3902
    """External cap part expression resolved to an empty scope during automatic dead material point computation."""
    NUMEN_AUTOCOMPUTEDEADMPTS_NOEXTERNALCAPTOPOFACES = 3903
    """No external cap topofaces were found for automatic dead material point computation."""
    NUMEN_AUTOCOMPUTEDEADMPTS_SOLIDEXTERNALCAPPARTS = 3904
    """External cap part expression includes parts with solid bodies during automatic dead material point computation."""
    NUMEN_AUTOCOMPUTEDEADMPTS_SOLIDINTERNALCAPPARTS = 3905
    """Internal cap part expression includes parts with solid bodies during automatic dead material point computation."""
    NUMEN_AUTOCOMPUTEDEADMPTS_COMPUTEINTERNALREGIONPOINTSFAILED = 3906
    """Failed to compute internal region points during automatic dead material point computation."""
    NUMEN_INITDEFAULTSIZE_NOTOPOPARTS = 3907
    """No topology parts were found matching the part expression during default size initialization."""
    NUMEN_INITDEFAULTSIZE_NOEDGES = 3908
    """No topology edges were found for analysis during default size initialization."""
    NUMEN_INITDEFAULTSIZE_INVALIDBOUNDINGBOX = 3909
    """Model bounding box is degenerated (zero or negative extent) during default size initialization."""
    NUMEN_INITDEFAULTSIZE_INVALIDMINEDGELENGTH = 3910
    """Global minimum edge length could not be determined (all edges filtered out) during default size initialization."""
    NUMEN_INITDEFAULTSIZE_INVALIDCOMPUTEDRANGE = 3911
    """Invalid min or max sizes computed (zero, non-finite, or min >= max) during default size initialization."""
    NUMEN_INITDEFAULTSIZE_SETGLOBALSIZINGFAILED = 3912
    """SetGlobalSizingParams rejected the computed values during default size initialization."""
    NUMEN_AUTOASSIGNPARTSTOWRAPPEDSOLIDMESHFAILED = 3913
    """Auto assign parts to wrapped solid mesh operation failed."""
    NUMEN_EXTRACTFLOWVOLUMEFAILED = 3914
    """Extract flow volume operation failed."""
    NUMEN_EXTRACTFLOWVOLUMEPARTSNOTFOUND = 3936
    """Extract flow volume parts not found."""
    NUMEN_CAPFACEEXPRESSIONEMPTY = 3945
    """Cap face expression is empty for user-defined capping during flow volume extraction."""
    NUMEN_MRFPARTSMORETHANONE = 3946
    """Multiple MRF parts found during flow volume extraction; only one MRF part is allowed."""
    NUMEN_PARTSSAMEASMRFPARTS = 3947
    """Flow volume parts are the same as MRF parts during flow volume extraction."""
    NUMEN_EXTERNALFLOWPARTNOTFOUND = 3948
    """External flow part not found during flow volume extraction."""
    NUMEN_EXTERNALFLOWPARTSSAMEASMRFPARTS = 3949
    """External flow parts are the same as MRF parts during flow volume extraction."""
    NUMEN_EXTERNALFLOWPARTSMORETHANONE = 3950
    """Multiple external flow parts found during flow volume extraction; only one external flow part is allowed."""
    NUMEN_PARTSNOTFOUNDAFTERFILTERING = 3951
    """Flow volume parts are empty after filtering out MRF and external flow parts."""
    NUMEN_VALIDCAPFACESNOTFOUND = 3952
    """No valid cap faces were found for the specified cap face expression during flow volume extraction."""
    NUMEN_CAPPARTSMESHINGFAILED = 3953
    """Meshing of cap parts using volumetric size fields failed during flow volume extraction."""
    NUMEN_NOAUTOFLUIDZONENAME = 3954
    """Flow volume zone name must be defined for the selected capping type."""
    NUMEN_NOCAPFACESFOUND = 3955
    """No cap faces found for the specified cap face expression."""
    NUMEN_MULTIPLESOLIDCAPPARTS = 3956
    """Multiple solid parts found from the cap face expression during flow volume extraction."""
    NUMEN_NOFLOWVOLUMEPARTSFORCAPCREATION = 3957
    """No flow volume parts found for cap creation."""
    NUMEN_CAPEDGEEXPRESSIONNOTDEFINED = 3958
    """Parameter cap_edge_expression must be defined for capping_type 'create'."""
    NUMEN_CAPCREATIONPARTNOTFOUND = 3959
    """Part could not be resolved for cap creation."""
    NUMEN_CAPCREATIONPARTHASNOTOPOLOGY = 3960
    """Part does not have topology required for cap creation."""
    NUMEN_NOCAPEDGESFOUND = 3961
    """No cap edges found for the specified edge expression."""
    NUMEN_CAPCREATIONBYEDGEFAILED = 3962
    """Cap creation using the specified edge expression failed."""
    NUMEN_FLOWVOLUMEPARTSNOTFOUND = 3963
    """No flow volume parts available for flow volume extraction."""
    NUMEN_SPLITVOLUMESFAILED = 3915
    """Split volumes operation failed."""
    NUMEN_CONNECTINTERFACEFAILED = 3915
    """Connect interface operation failed."""
    NUMEN_VOLUMEMESHINGFAILED = 3916
    """Volume meshing operation failed."""
    NUMEN_SETLABELSONFEATUREEDGESFAILED = 3917
    """Set labels on feature edges operation failed."""
    NUMEN_DETECTTHINVOLUMESFAILED = 3918
    """Detect thin volumes operation failed."""
    NUMEN_INITIALIZEDEFAULTSIZEFAILED = 3919
    """Initialize default size operation failed."""
    NUMEN_CREATEFACEZONESFORFACELABELSFAILED = 3920
    """Create face zones for face labels operation failed."""
    NUMEN_POSTMESHCLEANUPFAILED = 3921
    """Post mesh cleanup operation failed."""
    NUMEN_SETTINGSFAILED = 3922
    """Settings operation failed."""
    NUMEN_TOPOLOGYSUMMARYFAILED = 3923
    """Topology summary operation failed."""
    NUMEN_SURFACEMESHSUMMARYFAILED = 3924
    """Surface mesh summary operation failed."""
    NUMEN_SURFACEMESHQUALITYFAILED = 3925
    """Surface mesh quality operation failed."""
    NUMEN_VOLUMEMESHCHECKFAILED = 3926
    """Volume mesh check operation failed."""
    NUMEN_VOLUMEMESHSUMMARYFAILED = 3927
    """Volume mesh summary operation failed."""
    NUMEN_VOLUMEMESHQUALITYFAILED = 3928
    """Volume mesh quality operation failed."""
    NUMEN_FUSEFAILED = 3929
    """Fuse operation failed."""
    NUMEN_FILEREADFAILED = 3930
    """File read operation failed."""
    NUMEN_FILEWRITEFAILED = 3931
    """File write operation failed."""
    NUMEN_PRECHECKMODELFAILED = 3932
    """PrecheckModel operation failed."""
    NUMEN_ZONESCOUNTVALIDATIONFAILED = 3933
    """Zones count validation operation failed."""
    CELLSEPARATIONFAILED = 6000
    """Cell separation failed."""
    NOCELLSSEPARATED = 6001
    """No cells separated based on given input."""
    SIZEFIELDTYPENOTSUPPORTED = 8001
    """Provided Size Field Type is not supported by this operation."""
    UNSUPPORTEDFILEEXTENSIONFORPMDAT = 9001
    """Provided file extension is not supported. Supported extensions are .pmdat and .pmdat.gz."""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTMESHINGMESH = 9002
    """Provided file extension is not supported. Supported extensions are .msh and .msh.gz."""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTCASE = 9003
    """Provided file extension is not supported. Supported extensions are .cas, .cas.gz and .cas.h5."""
    UNSUPPORTEDFILEEXTENSIONFORKEYWORDFILE = 9004
    """Provided file extension is not supported. Supported extensions are .k and .key."""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTSIZEFIELD = 9005
    """Provided file extension is not supported. Supported extensions are .sf and .sf.gz."""
    UNSUPPORTEDFILEEXTENSIONFORSIZEFIELD = 9006
    """Provided file extension is not supported. Supported extensions are .psf and .psf.gz."""
    UNSUPPORTEDFILEEXTENSIONFORMAPDLCDB = 9007
    """Provided file extension is not supported. Supported extension is .cdb."""
    INVALIDFILEEXTENSIONFORFLUENTCASEEXPORT = 9009
    """Provided file extension is invalid. If cff_format is set to False, then supported extensions are .cas and .cas.gz. If cff_format is set to True, then supported extension is .cas.h5 ."""
    INVALIDFILEEXTENSIONFORPRIMEPROJECT = 9010
    """Provided file extension is not supported. Supported extension is .prproject.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CREATEPROJECTFILEFOLDERFAILED = 9011
    """Unable to create folder to store prime project files.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CREATEPROJECTFILEFAILED = 9012
    """Unable to create prime project file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CREATESTRIDEFILEFAILED = 9013
    """Unable to create stride file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ERRORREADINGSTRIDEDATA = 9014
    """Unable to read stride data.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STRIDECONVERTFAILED = 9015
    """Unable to convert to stride file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INVALIDCHECKPOINTNAME = 9016
    """Invalid checkpoint name provided. Checkpoint name should not start or end with space character and should not contain special characters.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ERRORREADINGCHECKPOINTHISTORY = 9017
    """Unable to read checkpoint history.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CHECKPOINTNOTFOUND = 9018
    """Checkpoint not found.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CHECKPOINTALREADYEXISTS = 9019
    """Checkpoint already exists.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    PLUGINLOADFAILURE = 10001
    """Failed to load Surface Editor plugin."""
    TARGETZONELETS_SELFINTERSECTING = 10002
    """Target zonelets form a self intersecting volume."""
    TARGETZONELETS_NOTWATERTIGHT = 10003
    """Target zonelets do not form a watertight volume."""
    TOOLZONELETS_SELFINTERSECTING = 10004
    """Tool zonelets form a self intersecting volume."""
    TOOLZONELETS_NOTWATERTIGHT = 10005
    """Tool zonelets do not form a watertight volume."""
    COULDNOTLOADHAMMERSTEINPLUGIN = 10006
    """Failed to load Hammerstein GPU Plugin.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    PRECOMPUTEDVOLUMESEXIST = 10007
    """Pre-computed volumes exist.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    GPUOUTOFMEMORY = 10008
    """GPU out of memory.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    GPUFATALERROR = 10009
    """Fatal error in GPU Meshing.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CPUOUTOFMEMORY = 10010
    """CPU out of memory.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    NOSIZINGINPUT = 10011
    """No sizing input provided.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_INVALIDINPUTVOLUMES = 10101
    """Invalid input volumes provided to stacker."""
    STACKER_INVALIDPARAMS = 10102
    """Invalid parameters provided to stacker."""
    STACKER_FACESEPARATIONFAILED = 10103
    """Stacker failed to separate base face."""
    STACKER_FAILED = 10104
    """Stacker failed to mesh the model."""
    STACKER_NOFACEFOUNDINVOLUMES = 10105
    """No faces are found in the specified volumes."""
    STACKER_MESHEDFACESFOUND = 10106
    """Some faces in the input model have existing mesh."""
    STACKER_INVALIDBASEFACEINPUT = 10107
    """Base face list input is invalid."""
    STACKER_NONSTACKABLEVOLUMESFOUND = 10109
    """Some volumes are not aligned in the stacking direction."""
    STACKER_INCORRECTBODYDEFINITION = 10110
    """Some bodies are intersecting or incorrectly defined."""
    STACKER_BASEFACEUNMESHED = 10111
    """Base face list input has unmeshed topofaces."""
    STACKER_MESHTRANSFERTOBASEFAILED = 10112
    """Mesh transfer from model to base face failed. Single seed face cannot project onto multiple faces on the base.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_NONIDENTICALMESHEDFACESFOUND = 10114
    """Mesh transfer from model to base face failed because of non-identical mesh on horizontally overlapping faces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_MESHTOTOPOASSOCIATIONFAILED = 10115
    """Stacker failed to associate mesh to model.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_VOLUMEMESHINGFAILED = 10118
    """Stacker failed to mesh some input bodies. Check for overlapping or duplicate bodies, and ensure that the mesh size and tolerance are adequate to resolve geometric features.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_CONFLICTINGSIZES = 10119
    """Stacker failed because of conflict in seed face stack layers. Check Seed Face Scope for mismatch in layers or conflicts with lateral faces of the model.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MERGENODES_MULTIPARTINPUTNOTSUPPORTED = 10121
    """Source or target face inputs span multiple parts. Cross-part merge is not supported.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MERGENODES_INPUTNOTCOMPLETE = 10122
    """Source or target face expression resolved to no meshed face zonelets.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MERGENODES_FAILED = 10123
    """Merge nodes operation failed.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_SEEDFACEMESHINVALID = 10124
    """Stacker failed. Seed faces for stacking should either have edge mesh or fully quad face mesh. Deviation of nodes on face mesh at each layer should be within the stacking tolerance.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_PARTIALEDGEMESHONBASE = 10125
    """Stacker failed because edge mesh from Seed Faces could not be transferred due to conflicting mesh from other faces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_NONIDENTICALEDGEMESHONBASE = 10126
    """Stacker failed because edge mesh from Seed Faces are conflicting with each other. Mesh from seed edges projecting to the same set of base edges should have identical mesh.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_EDGEMESHBASEMAPNOTFOUND = 10127
    """Stacker failed because some mesh edges could not be assigned to any edge on the base. Base edges may have shifted due to tolerance or the edge may have collapsed. Check lateral defeature tolerance.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_FACEMESHMISMATCHONBASE = 10128
    """Mesh transfer to base face failed. Mesh from seed faces projecting to the same set of base faces should have identical mesh.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_BASEFACEPARTITIONFAILED = 10129
    """Mesh transfer to base face failed during association of the projected seed face mesh on the base face.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_SEEDFACEBOUNDARYMERGEFAILED = 10130
    """Mesh transfer to base face failed because edge mesh from laterally adjacent seed faces were conflicting. Edge mesh from seed faces projecting to the same set of base edges should have identical mesh.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FACEZONELETSHAVECELLSCONNECTED = 10205
    """Face zonelets have cells connected."""
    INVALIDTHINVOLUMECONTROLS = 12101
    """Invalid input provided for thin volume control."""
    THINVOLUMECONTROLINVALIDSOURCESCOPE = 12102
    """Invalid source scope provided for thin volume control."""
    THINVOLUMECONTROLINVALIDTARGETSCOPE = 12103
    """Invalid target scope provided for thin volume control."""
    THINVOLUMECONTROLINVALIDSCOPE = 12104
    """Same source and target scope provided for thin volume control."""
    THINVOLUMECONTROLINVALIDSOURCESCOPEENTITY = 12105
    """Invalid source scope entity provided for thin volume control."""
    THINVOLUMECONTROLINVALIDTARGETSCOPEENTITY = 12106
    """Invalid target scope entity provided for thin volume control."""
    THINVOLUMECONTROLINVALIDNUMBEROFLAYER = 12107
    """Invalid number of layers provided for thin volume control."""
    THINVOLUMECONTROLTOPOLOGYNOTSUPPORTED = 12108
    """Thin volume mesh controls not supported for part with topology data."""
    THINVOLUMECONTROLINVALIDVOLUMESCOPE = 12109
    """Invalid volume scope provided for thin volume control."""
    THINVOLUMECONTROLINVALIDCONTROL = 12110
    """Same face scope is set as target for multiple thin volume controls."""
    THINVOLUMECONTROLSAMESOURCEFORMORETHANTWOCONTROL = 12111
    """Same face scope is set as source for more than two thin volume controls."""
    THINVOLUMEMESHNOTSUPPORTEDWITHFACEBASEDDATABASE = 12112
    """Thin volume mesh is not supported with face based database."""
    INVALIDCONTROLPARAMS = 12201
    """Invalid control parameters."""
    MICROSTRUCTUREINVALIDELEMENTTYPE = 13000
    """Invalid input provided. Invalid Element Type."""
    MICROSTRUCTUREINVALIDSHAPETYPE = 13001
    """Invalid input provided. Invalid Shape."""
    MICROSTRUCTUREWRONGAPICALLSEQUENCE = 13002
    """Wrong API call sequence."""
    MICROSTRUCTUREBADSHAPEPROPERTIES = 13003
    """Bad shape properties."""
    MICROSTRUCTURESMOOTHNOTSUPPORTED = 13004
    """Smoothing operation is not supported."""
    MICROSTRUCTUREREMESHNOTSUPPORTED = 13005
    """Surface remesh operation is not supported."""
    MICROSTRUCTUREQUADRATICHEXREQUIREDQUADRATICVOXELGRID = 13006
    """Volume mesh generation for hexahedra requires generation of a quadratic voxel grid."""
    AUTOQUADMESHER_NEGATIVEINPUTPARAMETER = 15000
    """Autoquadmesher error codes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    AUTOQUADMESHER_INVALIDMINMAXSIZES = 15001
    """Difference in maximum value and minimum value is negative.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INVALIDINPUTPOINT = 16000
    """Invalid input point.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    IMPORTABAQUSFAILEDWITHUNKNOWNERROR = 16200
    """Import Abaqus failed. Failed with unknown error.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    IMPORTABAQUSFAILEDWITHPARSINGFAILURE = 16201
    """Import Abaqus failed. Failed to parse file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    IMPORTABAQUSFAILEDDURINGMESHCREATION = 16202
    """Import Abaqus failed. Failed to create mesh entities.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ZEROELEMENTSREADFROMCDBFILE = 16500
    """No elements read from CDB file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ZERONODESREADFROMCDBFILE = 16501
    """No nodes read from CDB file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INVALIDCMBLOCKFORMAT = 16502
    """CMBLOCK command format error in CDB file.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ZEROELEMENTSFORCDBEXPORT = 16600
    """No elements found for cdb export.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    TOPODECOMPOSITION_INVALIDPARAMS = 16700
    """Invalid input parameter(s) provided for topology decomposition.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    TOPODECOMPOSITION_EMPTYINPUT = 16701
    """Empty input provided for topology decomposition.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    TOPODECOMPOSITION_UNMESHEDTOPOFACES = 16702
    """Input contains unmeshed topoface(s).

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    TOPODECOMPOSITION_ORIENTTOPOVOLUMESFAILED = 16703
    """Failed to orient input topovolume(s) during topology decomposition.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    TOPODECOMPOSITION_INVALIDINPUTFACEZONELETS = 16704
    """Input face zonelet(s) are invalid for topology decomposition.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    TOPODECOMPOSITION_TOPOLOGYUPDATEFAILED = 16705
    """Topology update failed during topology decomposition.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MESHDECOUPLEDFAILED = 16900
    """Invalid load balancing or failed in volume meshing for one or more parts.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDINPUTLOOPEDGES = 17101
    """Input edges do not form well-defined closed loops.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_NOINPUTTOPOVOLUMES = 17102
    """No topovolumes scoped in input for splitting.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDPLANEDEFINITIONS = 17103
    """Invalid input plane definitions.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDSOURCETARGETDATA = 17104
    """Invalid input source or target data for blend.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_SPLITFACESGENERATIONFAILED = 17105
    """Failed to generate any interfaces to split volumes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_PREVIEWFACESGENERATIONFAILED = 17106
    """Failed to generate any interfaces for preview.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDCONTROLID = 17107
    """Invalid input control id.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_SPLITTOPOVOLUMESFAILED = 17108
    """Failed to split topovolumes after generating the interfaces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_NOINPUTCONTROLIDS = 17109
    """No control ids provided as input.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_NOINPUTEDGES = 17110
    """No input edges provided.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDSOURCEEDGES = 17111
    """Source edges do not form a valid closed loop for blend.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDTARGETEDGES = 17112
    """Target edges do not form a valid closed loop for blend.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_MULTIPLESOURCELOOPS = 17113
    """Multiple source loops found; blend requires a single loop.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_MULTIPLETARGETLOOPS = 17114
    """Multiple target loops found; blend requires a single loop.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMETRICSCAFFOLDER_INVALIDINPUT = 17201
    """Invalid input provided for the volumetric scaffolder operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CADIMPORTXMLFILEGENERATIONFAILED = 17301
    """CAD Import XML File Generation failed."""
    CADIMPORTFMTRANSMOGRIFIEREXENOTFOUND = 17302
    """FMTransmogrifier_XC executable not found."""

class WarningCode(enum.IntEnum):
    """Warning codes associated with the PyPrimeMesh operation.
    """
    NOWARNING = 0
    """No warnings."""
    UNKNOWN = 1
    """Unknown warning."""
    SURFER_QUADCLEANUP_MULTITHREADINGNOTSUPPORTED = 102
    """Multithreading is not supported for quad cleanup operation."""
    OVERRIDECURVATURESIZINGPARAMS = 201
    """Overriding curvature sizing parameters."""
    OVERRIDESOFTSIZINGPARAMS = 202
    """Overriding soft sizing parameters."""
    OVERRIDEHARDSIZINGPARAMS = 203
    """Overriding hard sizing parameters."""
    OVERRIDEPROXIMITYSIZINGPARAMS = 204
    """Overriding proximity sizing parameters."""
    OVERRIDEBOISIZINGPARAMS = 205
    """Overriding BOI sizing parameters."""
    OVERRIDEMESHEDSIZINGPARAMS = 206
    """Overriding meshed sizing parameters."""
    OVERRIDESOISIZINGPARAMS = 207
    """Overriding SOI sizing parameters."""
    INVALIDSIZECONTROLSCOPE = 208
    """Invalid size control type provided."""
    OVERRIDEGROWTHRATEPARAM = 209
    """Overriding growth rate parameter."""
    PRESCRIBEDSIZEBELOWMINREPRESENTABLESINGLEPRECISION = 210
    """Prescribed sizes are below the minimum representable size for the domain in single precision and will not be respected."""
    PRESCRIBEDSIZEBELOWMINREPRESENTABLEDOUBLEPRECISION = 211
    """Prescribed sizes are below the minimum representable size for the domain in double precision and will not be respected."""
    OVERRIDESUGGESTEDNAME = 301
    """Override name by suggested name."""
    OVERRIDESURFACESCOPEENTITY = 401
    """Override surface scope entity."""
    OVERRIDEVOLUMESCOPEENTITY = 402
    """Override volume scope entity."""
    MAXOFPRISMCONTROLSMINASPECTRATIO = 403
    """Maximum value of min aspect ratio from selected prism controls is considered for all selected prism controls."""
    OVERRIDEEDGESCOPEENTITY = 404
    """Override edge scope entity.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SHELLBLGAPFACTORMINLIMIT = 405
    """Adjusted ShellBL gap factor to 0.001. As 0.001 is minimum value supported.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    PARTNOTINPARTSCOPE = 601
    """Selected part is not in the part scope of the periodic control."""
    NUMERICPARTNAMERENAMETOALPHANUMERIC = 701
    """Numeric part name renamed to alphanumeric name."""
    SURFERLAYEREDQUADFAILED = 1800
    """Layered quad failed with surfer."""
    SURFERDEGENERATEFACE = 1801
    """Degenerate input."""
    ALIGN_OPERATIONINTERRUPTED = 1900
    """Align operation interrupted."""
    FUSEOVERLAPREMOVALINCOMPLETE = 4500
    """Self intersections found. Use Fuse operation to remove it."""
    REMOVEOVERLAPWITHINTERSECT = 4501
    """Self intersections found. Use Intersect operation to remove it."""
    IGA_NOGEOMZONELETFORSPLINEFITTING = 5001
    """Invalid input for IGA."""
    NOHOLESFOUNDONPLANE = 5501
    """Provides warning when no closed holes are found in the given face zonelets at given plane."""
    NOVOLUMESCOMPUTED = 5600
    """There are no volumes found."""
    EXTERNALOPENFACEZONELETSFOUND = 5601
    """External open face zonelets found when computing volumes."""
    NOVOLUMESENCLOSINGMATERIALPOINT = 5602
    """No computed volumes enclosing material point."""
    EXTERNALOPENTOPOFACESFOUND = 5603
    """External open topofaces found when computing topovolumes."""
    FACEZONELETSWITHOUTVOLUMES = 5604
    """Face zonelets have no volume associated to them."""
    JOINEDZONELETSFROMMULTIPLEVOLUMES = 5605
    """Joined zonelets from more than two volumes. The volumes are not auto updated on the zonelets."""
    FAILEDTOUPDATEVOLUMES = 5606
    """Volumes are not updated after performing the operation. Compute the volumes again."""
    WRAPPER_SIZECONTROLNOTDEFINED = 6001
    """No size controls provided for wrapper."""
    WRAPPER_SIZECONTROLNOTSUPPORTED = 6002
    """Size control is not supported in wrapper."""
    WRAPPER_SMALLERSIZEATFEAURES = 6003
    """Size at features is smaller than base size."""
    WRAPPER_SMALLERCONTACTPREVENTIONSIZE = 6004
    """Contact prevention size is smaller than base size."""
    MATERIALPOINTWITHSAMENAMEEXISTS = 6005
    """Material point with the same name exists. Overriding with unique name."""
    WRAPPER_PATCHFLOWREGIONS_NOHOLESFOUND = 6006
    """No holes detected to patch.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ENTITIESNOTBELONGTOANYZONE = 6201
    """Entities do not belong to any zone."""
    INVALIDENTITIESNOTADDEDTOZONE = 6202
    """Entities with invalid id or type not added to zone."""
    LOCALSURFERNOFACEREGISTERED = 7001
    """No face registered with the given register id."""
    MESHHASNONPOSITIVEVOLUMES = 7104
    """Mesh has non positive volumes."""
    MESHHASNONPOSITIVEAREAS = 7105
    """Mesh has non positive areas."""
    MESHHASINVALIDSHAPE = 7106
    """Mesh has invalid shape."""
    MESHHASLEFTHANDEDNESSFACES = 7107
    """Mesh has invalid shape."""
    MESHHASINVALIDPARTITIONSTATE = 7108
    """Mesh has invalid parallel neighborhood."""
    NOCADGEOMETRYFOUND = 7500
    """CAD geometry not found for some or all topo entities. Skipped projection for those topo entities."""
    NOCADGEOMETRYPROJECTONFACETS = 7501
    """CAD geometry not found for some or all topo entities. Projected on facets for those topo entities."""
    DUPLICATEINPUT = 8001
    """Duplicate items in input."""
    STACKER_MESHTOTOPOASSOCIATIONFAILED = 9001
    """Stacker failed to associate mesh to model.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_SIZESLARGERTHANMAXOFFSETFOUND = 9002
    """Size controls with sizes larger than maximum offset size found.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_SIZESSMALLERTHANTOLERANCEFOUND = 9003
    """Size controls with sizes smaller than tolerance found.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_UNMESHEDFACES = 9005
    """Stacker failed to mesh some faces. Check for overlapping faces, reduce tolerance value or both.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_SIZINGSIGNOREDINFAVOROFSEEDFACESCOPE = 9006
    """Stacker does not respect some sizings due to conflict with mesh from Seed Face Scope.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_CONFORMALMESHINGFAILED = 9007
    """Volume meshing is completed and has non-conformal mesh due to intersections among the input volumes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_NUMBEROFDIVISIONSSPLITATGEOMETRY = 9008
    """Number of divisions specified for some edges could not be respected due to geometry constraints.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_NUMBEROFDIVISIONSNOTRESPECTED = 9009
    """Number of divisions specified for some edges could not be respected due to conflicting controls. The smaller sizing among the controls was applied.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_NOSTACKABLEBODIESDETECTED = 9010
    """No stackable bodies were detected among the input volumes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    STACKER_HORIZONTALEDGESUSEDFORSMALLESTSTACKINGEDGES = 9011
    """Horizontal edges are used for indicating the span of smallest stacking edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    UNPROCESSEDKEYWORDSINABAQUSFILE = 11001
    """Unprocessed Abaqus keywords have been found."""
    EXPORTMAPDLANALYSISSETTINGSFAILED = 11101
    """Export MAPDL analysis settings failed."""
    WRITINGCONTACTPAIRSSKIPPED = 11102
    """Writing of contact pairs skipped."""
    WRITINGTIESSKIPPED = 11103
    """Writing of ties skipped."""
    WRITINGZONELETOFLABELTOELEMENTCOMPONENTSKIPPED = 11104
    """Export of label as element component skipped."""
    IMPORTOFNODALCOMPONENTASLABELSKIPPED = 11201
    """Import of nodal component as label skipped."""
    CONNECT_NODESINTARGETZONELETSNOTMERGED = 11201
    """Some or all nodes in target zonelets could not be merged with nodes in the source zonelets.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CONNECT_ONETOONEMAPPINGNOTFOUND = 13202
    """One-to-one mapping between source and target zonelets not found. Check connectivity information or provide smaller tolerance value.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDPROTECTEDENTITIES = 100001
    """Input contains protected entities which have been skipped.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDFEATUREENTITIES = 100002
    """Input contains feature entities which have been skipped.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDFREEEDGES = 100003
    """Input contains free edges which have been skipped.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDNONMANIFOLDEDGES = 100004
    """Input contains non-manifold edges which have been skipped.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDENTITIESINDIFFERENTZONES = 100005
    """Input contains entities in different zones which have been skipped.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_CANNOTMERGENODES = 100006
    """Cannot merge nodes during VT operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_REMESHFACEFAILED = 100007
    """Failed to remesh face(s) during VT operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_FACESEPARATIONFAILED = 100008
    """Interior edge created but face separation failed during VT operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDFACESWITHNOPLANEINTERSECTION = 100009
    """Skipped one or more faces as the faces do not intersect with the input plane.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_SKIPPEDCUSPTOPOEDGES = 100010
    """Input contains cusp topoedges which have been skipped.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_VOLUMENOTMERGEDNOSHAREDFACE = 100012
    """One or more input volumes were skipped during merge as they have no shared face with any other input volume.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_VOLUMEMESHDELETED = 100013
    """Deleted volume mesh on one or more adjacent volumes to allow face splitting.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_VOLUMENOTMERGEDPROTECTEDSHAREDFACE = 100014
    """One or more input volumes were skipped during merge as their shared face is protected.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_VOLUMENOTMERGEDSHAREDFACEDIFFERENTPARTS = 100015
    """One or more input volumes were skipped during merge as their shared face spans different parts.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VT_VOLUMENOTMERGEDSHAREDFACEDIFFERENTZONES = 100016
    """One or more input volumes were skipped during merge as their shared face spans different zones.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    MULTIZONEMESHER_SURFACESCOPEVOLUMESCOPEINCONSISTENCY = 110001
    """MultiZone warning codes."""
    MULTIZONEMESHER_DEFEATUREDTOPOEDGES = 110002
    """TopoEdges that got defeatured in the MultiZone mesh."""
    MULTIZONEMESHER_DEFEATUREDTOPOFACES = 110003
    """TopoFaces that got defeatured in the MultiZone mesh."""
    MULTIZONEMESHER_DEFEATUREDPROTECTEDTOPOLOGY = 110004
    """Protected toponodes or topoedges that got defeatured in the MultiZone mesh."""
    VOLUMETRICSCAFFOLDER_SPLITBYINTERIOREDGESFAILURE = 120001
    """Failed to split using interior edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMETRICSCAFFOLDER_UNRESOLVEDOVERLAPS = 120002
    """Unresolved overlaps left after resolve surface overlaps operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMETRICSCAFFOLDER_FREEFACES = 120003
    """Free faces left after resolve surface overlaps operation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    REMOVECUSP_PARTWITHMULTIPLEVOLUMES = 130001
    """Parts with multiple volumes do not support Cusp removal."""
    VOLUMESLICER_SPLITFACEGENERATIONFAILED = 140001
    """Failed to generate split faces for one or more controls.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_PREVIEWFACEGENERATIONFAILED = 140002
    """Failed to generate preview faces for one or more controls.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_PLANENOINTERSECTION = 140003
    """Plane does not intersect target volume.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_PLANENOCLOSEDBOUNDARY = 140004
    """Plane intersects the target volume but does not form a valid split region.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_UNIQUETOPOVOLUMENOTFOUND = 140005
    """Failed to find a unique volume to split for the given control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_SOURCETARGETPROJECTIONFAILED = 140006
    """Failed to project source edges on target faces for the blend control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_SPLITFACEOVERLAPSTOPOLOGY = 140007
    """Failed to generate split faces for the control. The split region overlaps with the existing topology and cannot divide the volumes into valid regions.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_SPLITFACEOUTSIDEVOLUMEBOUNDARY = 140008
    """Failed to generate split faces for the given control. The split region lies outside of the target volumes and cannot divide the volumes into valid regions.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_LOOPSPLITFACEGENERATIONFAILED = 140009
    """Failed to generate split faces for the loop control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_PLANARSPLITFACEGENERATIONFAILED = 140010
    """Failed to generate split faces for the plane control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_LOOPPREVIEWFACEGENERATIONFAILED = 140011
    """Failed to generate preview faces for the loop control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_PLANARPREVIEWFACEGENERATIONFAILED = 140012
    """Failed to generate preview faces for the plane control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_BLENDSPLITFACEGENERATIONFAILED = 140013
    """Failed to generate split faces for the blend control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_BLENDPREVIEWFACEGENERATIONFAILED = 140014
    """Failed to generate preview faces for the blend control.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_UNCLOSEDSEGMENTSIGNORED = 140015
    """Input contains unclosed edge segments. These segments are ignored during processing.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICER_INVALIDPLANEDEFINITIONSIGNORED = 140016
    """Input contains invalid plane definitions. These definitions are ignored during processing.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_SPLITFACEINTERSECTSTOPOLOGY = 140017
    """Failed to generate split faces for the control. The split region intersects with the existing topology.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    VOLUMESLICERCONTROL_VOLUMEMESHDELETED = 140018
    """Deleted volume mesh on one or more volumes to allow volume splitting.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    NUMEN_SURFACEMESHELEMENTCOUNTVALIDATIONFAILED = 150001
    """Numen surface mesh element count validation failed."""
    NUMEN_SELFINTERSECTIONSVALIDATIONFAILED = 150002
    """Numen self intersections count validation failed."""
    NUMEN_FREEEDGESVALIDATIONFAILED = 150003
    """Numen free edges count validation failed."""
    NUMEN_MULTIEDGESVALIDATIONFAILED = 150004
    """Numen multi edges count validation failed."""
    NUMEN_QUADELEMENTCOUNTVALIDATIONFAILED = 150005
    """Numen quad element count validation failed."""
    NUMEN_POLYELEMENTCOUNTVALIDATIONFAILED = 150006
    """Numen poly element count validation failed."""
    NUMEN_INVALIDNORMALSCOUNTVALIDATIONFAILED = 150007
    """Numen invalid normals count validation failed."""
    NUMEN_FACESABOVECRITERIAVALIDATIONFAILED = 150008
    """Numen faces above quality criterion validation failed."""
    NUMEN_DIHEDRALANGLEVALIDATIONFAILED = 150009
    """Numen dihedral angle validation failed."""
    NUMEN_VOLUMEMESHCHECKVALIDATIONFAILED = 150010
    """Numen volume mesh check validation failed."""
    NUMEN_TOTALFACECOUNTVALIDATIONFAILED = 150011
    """Numen total face element count validation failed."""
    NUMEN_TOTALCELLCOUNTVALIDATIONFAILED = 150012
    """Numen total cell element count validation failed."""
    NUMEN_FLUIDSPRISMCELLCOUNTVALIDATIONFAILED = 150013
    """Numen fluids prism cell count validation failed."""
    NUMEN_SOLIDSPRISMCELLCOUNTVALIDATIONFAILED = 150014
    """Numen solids prism cell count validation failed."""
    NUMEN_HEXCELLCOUNTVALIDATIONFAILED = 150015
    """Numen hex cell count validation failed."""
    NUMEN_POLYCELLCOUNTVALIDATIONFAILED = 150016
    """Numen poly cell count validation failed."""
    NUMEN_PYRAMIDCELLCOUNTVALIDATIONFAILED = 150017
    """Numen pyramid cell count validation failed."""
    NUMEN_TETCELLCOUNTVALIDATIONFAILED = 150018
    """Numen tet cell count validation failed."""
    NUMEN_CELLSABOVECRITERIAVALIDATIONFAILED = 150019
    """Numen cells above quality criterion validation failed."""
    NUMEN_SELFINTERSECTIONSFOUND = 150020
    """Self intersecting face elements found during surface diagnostics."""
    NUMEN_FREEEDGESFOUND = 150021
    """Free edge elements found during surface diagnostics."""
    NUMEN_AUTOCOMPUTEDEADMPTS_EMPTYINTERNALCAPSCOPE = 150022
    """Internal cap part expression resolved to an empty scope during automatic dead material point computation."""
    NUMEN_AUTOCOMPUTEDEADMPTS_NOINTERNALCAPTOPOFACES = 150023
    """No internal cap topofaces were found for automatic dead material point computation."""
    NUMEN_NOCAPFOUNDWARNING = 150024
    """No caps found during model precheck analysis."""
    NUMEN_BAFFLEDETECTED = 150025
    """Baffle(s) detected during model precheck analysis."""
    NUMEN_FACEZONECOUNTVALIDATIONFAILED = 150029
    """Unique face zone count validation failed for a zone name expression."""
    NUMEN_VOLUMEZONECOUNTVALIDATIONFAILED = 150030
    """Unique volume zone count validation failed for a zone name expression."""
    NUMEN_FACEZONEENTITYCOUNTVALIDATIONFAILED = 150031
    """Face entity count validation failed for a zone name expression."""
    NUMEN_VOLUMEZONEENTITYCOUNTVALIDATIONFAILED = 150032
    """Volume entity count validation failed for a zone name expression."""
    NUMEN_MRFPARTNOTFOUND = 150033
    """MRF part not found during flow volume extraction; MRF extraction will be skipped."""
