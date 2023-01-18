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
    FACEZONELETSFEATURESNOTUPTODATE = 10
    """Face zonelets features are not up to date."""
    SURFERAUTOSIZEQUADUNSUPPORTED = 11
    """Auto sizing for quad meshing is not supported."""
    SURFERAUTOSIZEMUSTBEVOLUMETRIC = 12
    """Auto sizing must be of volumetric type."""
    SURFERNONMANIFOLDEDGE = 14
    """Non manifold edge for meshing."""
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
    AUTOMESHFAILED = 100
    """Auto mesh failed."""
    AITOVERLAPALONGMULTIFOUND = 101
    """Topology identification failed because of overlapping faces."""
    TRIANGULATIONFAILED = 102
    """Triangulation failed."""
    DUPLICATENODESFOUND = 103
    """Duplicate nodes found."""
    EDGEINTERSECTINGFACEFOUND = 104
    """Edge intersecting face found."""
    DUPLICATEFACESFOUND = 105
    """Duplicate faces found."""
    TETIMPROVEFAILED = 106
    """Tet improve failed."""
    AUTONODEMOVEFAILED = 107
    """Auto node move failed."""
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
    AUTOMESHINVALIDMAXSIZE = 116
    """Invalid max size for auto volume meshing."""
    AUTOMESHHEXCOREFAILED = 117
    """Hex generation part of volume meshing failed."""
    INVALIDVOLUMECONTROLS = 118
    """Invalid volume controls specified for volume meshing."""
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
    """Quadratic tetrahedal meshing is not supported in parallel mode."""
    QUADRATICTETNOTSUPPORTEDWITHPRISMS = 131
    """Quadratic tetrahedral meshing is not supported with prism."""
    EXTRACTVOLUMESFAILED = 132
    """Extract volumes failed."""
    PERIODICSURFACESNOTSUPPORTEDFORPRISMS = 135
    """Periodic surfaces selected for prism generation are not supported."""
    OUTOFMEMORY = 200
    """Out of memory."""
    INTERRUPTED = 201
    """Method call interrupted."""
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
    """No CAD Geometry found for projections."""
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
    SIZEFIELDCOMPUTATIONFAILED = 400
    """Size field computation failed."""
    INVALIDSIZECONTROLS = 401
    """Invalid size controls."""
    REFRESHSIZEFIELDSFAILED = 402
    """Refreshing size field failed."""
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
    MATCHEDMESHOPTIONINVALID = 850
    """Invalid option chosen to connect two different parts."""
    COLOCATEMATCHEDNODESFAILED = 851
    """Colocation of matched nodes failed."""
    IMPRINTBOUNDARYNODESFAILED = 852
    """Imprint of boundary nodes failed."""
    IMPRINTBOUNDARYEDGESFAILED = 853
    """Imprint of boundary edges failed."""
    SPLITINTERSECTINGBOUNDARYEDGESFAILED = 854
    """Splitting of intersecting boundary edges failed."""
    MATCHINTERIORFAILED = 855
    """Matching of interior region of overlap failed."""
    TOLERANCEVALUEINVALID = 856
    """Invalid tolerance value specified."""
    SOURCEORTARGETNOTSPECIFIED = 857
    """No target or source faces specified."""
    NOTSUPPORTEDFORTOPOLOGYPART = 1200
    """Not supported for part with topology data."""
    NOTSUPPORTEDFORHIGHERORDERMESHPART = 1201
    """Operation does not support higher order elements."""
    NOTSUPPORTEDFORNONTRIFACEZONE = 1202
    """Only triangular face zone is supported."""
    NOTSUPPORTEDFORNONQUADFACEZONE = 1203
    """Operation supports only quads."""
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
    """Invalid input volumes."""
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
    EXTRACTFEATURESBYANGLEFAILED = 1600
    """Feature extraction by angle failed."""
    EXTRACTFEATURESBYEDGESFAILED = 1601
    """Extracting features by angle failed."""
    CREATEEDGEZONELETFAILED = 1602
    """Creating edge zonelet failed."""
    EXTRACTFEATURESBYINTERSECTIONFAILED = 1603
    """Feature extraction by intersection failed."""
    VOLUMEMESH_MIDNODESNOTSUPPORTED = 1800
    """Mid side nodes are not supported."""
    VOLUMEMESHNOTFOUND = 1801
    """Volume mesh not found."""
    SPLITANDCOLLAPSEFACEELEMENTSFAILED = 2101
    """Faield to split and collapse face element(s)."""
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
    FILLHOLEFAILED = 2901
    """Unable to create capping surface."""
    SUBTRACTZONELETSFAILED = 2903
    """Unable to subtract cutters from input zonelets."""
    CREATECAPONFACEZONELETSFAILED = 2906
    """Failed to create cap on face zonelets."""
    UNITEZONELETSFAILED = 2907
    """Failed to union input zonelets."""
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
    TRANSFORMATIONFAILED = 3000
    """Transformation failed."""
    SCALINGFAILED = 3001
    """Scaling failed."""
    ALIGNMENTFAILED = 3002
    """Alignment failed."""
    INVALIDTRANSFORMATIONMATRIX = 3003
    """Invalid transformation matrix."""
    DELETEMESHFACESFAILED = 3200
    """Delete Mesh faces failed"""
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
    WRAPPERGLOBALSETTINGSNOTSET = 3400
    """Global settings for wrapper not set."""
    WRAPPERRESOLVEINTERSECTIONFAILED = 3401
    """Resolving intersections failed for wrapper."""
    WRAPPERCONNECTFAILED = 3402
    """Wrapper connect failed."""
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
    """Provided file extension is not supported. Supported extensions are .cas and .cas.gz."""
    UNSUPPORTEDFILEEXTENSIONFORKEYWORDFILE = 9004
    """Provided file extension is not supported. Supported extensions are .k and .key."""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTSIZEFIELD = 9005
    """Provided file extension is not supported. Supported extensions are .sf and .sf.gz."""
    UNSUPPORTEDFILEEXTENSIONFORSIZEFIELD = 9006
    """Provided file extension is not supported. Supported extensions are .psf and .psf.gz."""
    UNSUPPORTEDFILEEXTENSIONFORMAPDLCDB = 9007
    """Provided file extension is not supported. Supported extension is .cdb."""
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
    OVERRIDESUGGESTEDNAME = 301
    """Override name by suggested name."""
    OVERRIDESURFACESCOPEENTITY = 401
    """Override surface scope entity."""
    OVERRIDEVOLUMESCOPEENTITY = 402
    """Override volume scope entity."""
    MAXOFPRISMCONTROLSMINASPECTRATIO = 403
    """Maximum value of min aspect ratio from selected prism controls is considered for all selected prism controls."""
    SURFERLAYEREDQUADFAILED = 1800
    """Layered quad failed with surfer."""
    SURFERDEGENERATEFACE = 1801
    """Degenerate input."""
    ALIGN_OPERATIONINTERRUPTED = 1900
    """Align operation interrupted."""
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
    DUPLICATEINPUT = 8001
    """Duplicate items in input."""
