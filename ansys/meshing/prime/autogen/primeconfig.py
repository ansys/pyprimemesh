""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np


class ErrorCode(enum.IntEnum):
    """Error codes associated with the failure of PRIME operation.
    """
    NOERROR = 0
    UNKNOWN = 1
    SIGSEGV = 2
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
    """Invalid Corner angle or min angle more than max angle specified for surface meshing"""
    SMOOTHSIZETRANSITIONNOTSUPPORTEDFORTOPO = 43
    """Smooth size transition option is not supported for topology surface meshing yet"""
    LOCALSURFERINVALIDNUMRINGS = 44
    """Invalid number of rings input for the local surface mesh operation."""
    SCAFFOLDERBADINPUTEMPTYTOPO = 50
    """Please Document"""
    SCAFFOLDERBADINPUTNOFREEFACES = 51
    """Please Document"""
    SCAFFOLDERBADINPUTPARAMS = 52
    """Please Document"""
    AUTOMESHFAILED = 100
    """Please Document"""
    AITOVERLAPALONGMULTIFOUND = 101
    """Please Document"""
    TRIANGULATIONFAILED = 102
    """Please Document"""
    DUPLICATENODESFOUND = 103
    """Please Document"""
    EDGEINTERSECTINGFACEFOUND = 104
    """Please Document"""
    DUPLICATEFACESFOUND = 105
    """Please Document"""
    TETIMPROVEFAILED = 106
    """Please Document"""
    AUTONODEMOVEFAILED = 107
    """Please Document"""
    ALREADYVOLUMEMESHED = 110
    """Please Document"""
    INVALIDPRISMCONTROLS = 111
    """Invalid prism controls."""
    VOLUMESNOTUPTODATE = 112
    """Please Document"""
    QUATRICMESHSUPPORTEDONLYFORTETS = 113
    """Please Document"""
    NOACTIVESFFOUND = 114
    """Please Document"""
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
    OUTOFMEMORY = 200
    """Please Document"""
    INTERRUPTED = 201
    """Please Document"""
    GETSTATISTICSFAILED = 250
    """Please Document"""
    GETELEMENTCOUNTFAILED = 251
    """Please Document"""
    PARTNOTFOUND = 300
    """Given part not found."""
    TOPODATANOTFOUND = 301
    """Please Document"""
    SIZEFIELDNOTFOUND = 302
    """Please Document"""
    ZONESARENOTOFSAMETYPE = 303
    """Zones are not of same type."""
    PARTNOTMESHED = 304
    """Please Document"""
    INVALIDINPUTPART = 305
    """Invalid input part."""
    CADGEOMETRYNOTFOUND = 306
    """Please Document"""
    VOLUMENOTFOUND = 307
    """Please Document"""
    ZONENOTFOUND = 308
    """Given zone not found."""
    ENTITIESSHOULDBEADDEDTOZONEUSINGPARTITBELONGS = 309
    """Entities should be added to zone using part it belongs."""
    PARTDOESNOTHAVETOPOLOGY = 310
    """Part does not have topology."""
    ZONESARENOTSUPPORTEDFORCELLZONELETS = 311
    """Zones are not supported for cell zonelets."""
    SPHEREATINVALIDNORMALNODESFAILED = 350
    """Please Document"""
    PROJECTONCADGEOMETRYFAILED = 351
    """Please Document"""
    SEPARATIONRESULTSFAILED = 360
    """Please Document"""
    SIZEFIELDCOMPUTATIONFAILED = 400
    """Please Document"""
    INVALIDSIZECONTROLS = 401
    """Please Document"""
    REFRESHSIZEFIELDSFAILED = 402
    """Please Document"""
    READMESHFAILED = 500
    """Please Document"""
    WRITEMESHFAILED = 501
    """Please Document"""
    CADIMPORTFAILED = 502
    """Please Document"""
    READSIZEFIELDFAILED = 503
    """Please Document"""
    READPMDBFAILED = 504
    """Please Document"""
    READCDBFAILED = 505
    """Please Document"""
    WRITECDBFAILED = 506
    """Please Document"""
    PATHNOTFOUND = 511
    """Please Document"""
    READKEYWORDFILEFAILED = 517
    """Please Document"""
    WRITEKEYWORDFILEFAILED = 518
    """Please Document"""
    QUADRATICMESH_WRITEMESHFAILED = 519
    """Please Document"""
    INCLUDEKFILENOTFOUND = 520
    """Please Document"""
    READSIZECONTROLFAILED = 522
    """Please Document"""
    WRITESIZECONTROLFAILED = 523
    """Please Document"""
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
    UNDOFAILED = 570
    """Please Document"""
    REDOFAILED = 571
    """Please Document"""
    NOTSUPPORTEDFORTOPOLOGYPART = 1200
    """Not supported for part with topology data."""
    NOTSUPPORTEDFORHIGHERORDERMESHPART = 1201
    """Please Document"""
    NOTSUPPORTEDFORNONTRIFACEZONE = 1202
    """Only triangular face zone is supported."""
    NOTSUPPORTEDFORNONQUADFACEZONE = 1203
    """Please Document"""
    PREPAREFORSOLVERFAILED = 1300
    """Please Document"""
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
    """Please Document"""
    CREATEEDGEZONELETFAILED = 1602
    """Please Document"""
    EXTRACTFEATURESBYINTERSECTIONFAILED = 1603
    """Feature extraction by intersection failed."""
    NOSIDEFRONTFACES = 1700
    """Please Document"""
    NOTALLSIDEFRONTFACES = 1701
    """Please Document"""
    NOMESHONSIDEFACES = 1702
    """Please Document"""
    NOMESHONFRONTFACES = 1703
    """Please Document"""
    TETINITFAILED = 1704
    """Please Document"""
    TETCUTFAILED = 1705
    """Please Document"""
    MIDSURFACEFAILED = 1706
    """Please Document"""
    IMPRINTFAILED = 1707
    """Please Document"""
    INVALIDSIDETHICKNESS = 1708
    """Please Document"""
    NOTMIDSURFTOPOFACE = 1709
    """Please Document"""
    NOTUNIFORMTHICKNESSMIDSURFTOPOFACE = 1710
    """Please Document"""
    OPENSIDEFACELOOPS = 1711
    """Please Document"""
    SINGLESETFRONTFACES = 1712
    """Please Document"""
    VOLUMEMESH_MIDNODESNOTSUPPORTED = 1800
    """Please Document"""
    VOLUMEMESHNOTFOUND = 1801
    """Please Document"""
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
    """Part has a topology."""
    SURFACESEARCHPARTWITHMESHNOTFOUND = 2803
    """Part with mesh not found for surface quality check."""
    INVALIDPLANEPOINTS = 2804
    """Invalid plane points, cannot define a plane."""
    PLANECOLLINEARPOINTS = 2805
    """Collinear or duplicate points given to define plane."""
    INVALIDREGISTERID = 2806
    """Invalid register id provided. Register ids between 1 to 28 are valid."""
    INVALIDINPUTZONELETS = 2807
    """Invalid input zonelets for surface search."""
    VOLUMESEARCHPARTWITHMESHNOTFOUND = 2850
    """Part with mesh not found for volume quality check."""
    VOLUMESEARCHFAILED = 2851
    """Volume search failed."""
    INVALIDCELLQUALITYLIMIT = 2852
    """Invalid cell quality limit."""
    SUBTRACTZONELETSFAILED = 2903
    """Unable to subtract cutters from input zonelets."""
    TRANSFORMATIONFAILED = 3000
    """Please Document"""
    SCALINGFAILED = 3001
    """Please Document"""
    ALIGNMENTFAILED = 3002
    """Please Document"""
    INVALIDTRANSFORMATIONMATRIX = 3003
    """Invalid transformation matrix."""
    DELETEMESHFACESFAILED = 3200
    """Please Document"""
    DELETEMESHFACES_TOPOLOGYNOTSUPPORTED = 3201
    """Please Document"""
    DELETEMESHFACES_CELLFOUND = 3202
    """Please Document"""
    DELETEFRINGESANDOVERLAPSFAILED = 3203
    """Please Document"""
    DELETEZONELETSCONNECTEDTOCELLS = 3204
    """Cannot delete zonelets connected to volume mesh."""
    DELETEZONELETSFAILED = 3205
    """Delete zonelets failed."""
    MATERIALPOINTWITHSAMENAMEEXISTS = 3300
    """Please Document"""
    MATERIALPOINTWITHGIVENNAMEDOESNTEXIST = 3301
    """Material point with the given name does not exist."""
    MATERIALPOINTWITHGIVENIDDOESNTEXIST = 3302
    """Please Document"""
    WRAPPERGLOBALSETTINGSNOTSET = 3400
    """Please Document"""
    WRAPPERRESOLVEINTERSECTIONFAILED = 3401
    """Please Document"""
    WRAPPERCONNECTFAILED = 3402
    """Please Document"""
    WRAPPERCOULDNOTEXTRACTINTERFACE = 3405
    """Failed to extract wrapper interface."""
    WRAPPERLEAKPREVENTIONFAILED = 3406
    """Wrapper leak prevention failed."""
    WRAPPERUNSUPPORTEDWRAPREGION = 3407
    """Wrap region option provided does not support wrap operation."""
    WRAPPERCONTROL_NOLIVEMATERIALPOINTSPROVIDED = 3408
    """Live material points list provided for wrapper control is empty."""
    WRAPPERSURFACEHASHOLES = 3410
    """Please Document"""
    WRAPPEROCTREEREGIONINGFAILED = 3411
    """Please Document"""
    WRAPPERPROJECTIONFAILED = 3412
    """Please Document"""
    WRAPPERCONTROL_MATERIALPOINTWITHGIVENNAMEDOESNTEXIST = 3413
    """Live material point added to wrapper control doesn't exist."""
    WRAPPERCONTROL_LIVEMATERIALPOINTDOESNTEXIST = 3414
    """Please Document"""
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
    SIZEFIELDTYPENOTSUPPORTED = 8001
    """Provided Size Field Type is not supported by this operation."""
    UNSUPPORTEDFILEEXTENSIONFORPMDAT = 9001
    """Provided file extension is not supported. Supported extensions are .pmdat and .pmdat.gz"""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTMESHINGMESH = 9002
    """Provided file extension is not supported. Supported extensions are .msh and .msh.gz"""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTCASE = 9003
    """Provided file extension is not supported. Supported extensions are .cas and .cas.gz"""
    UNSUPPORTEDFILEEXTENSIONFORKEYWORDFILE = 9004
    """Provided file extension is not supported. Supported extensions are .k and .key"""
    UNSUPPORTEDFILEEXTENSIONFORFLUENTSIZEFIELD = 9005
    """Provided file extension is not supported. Supported extensions are .sf and .sf.gz"""
    UNSUPPORTEDFILEEXTENSIONFORSIZEFIELD = 9006
    """Provided file extension is not supported. Supported extensions are .psf and .psf.gz"""
    UNSUPPORTEDFILEEXTENSIONFORMAPDLCDB = 9007
    """Provided file extension is not supported. Supported extension is .cdb"""

class WarningCode(enum.IntEnum):
    """Warning codes associated with the PRIME operation.
    """
    NOWARNING = 0
    UNKNOWN = 1
    SURFER_QUADCLEANUP_MULTITHREADINGNOTSUPPORTED = 102
    """Please Document."""
    OVERRIDECURVATURESIZINGPARAMS = 201
    """Please Document."""
    OVERRIDESOFTSIZINGPARAMS = 202
    """Please Document."""
    OVERRIDEHARDSIZINGPARAMS = 203
    """Please Document."""
    OVERRIDEPROXIMITYSIZINGPARAMS = 204
    """Please Document."""
    OVERRIDEBOISIZINGPARAMS = 205
    """Please Document."""
    OVERRIDEMESHEDSIZINGPARAMS = 206
    """Please Document."""
    OVERRIDESUGGESTEDNAME = 301
    """Override name by suggested name."""
    OVERRIDESURFACESCOPEENTITY = 401
    """Override surface scope entity."""
    OVERRIDEVOLUMESCOPEENTITY = 402
    """Override volume scope entity."""
    SURFERLAYEREDQUADFAILED = 1800
    """Please Document."""
    SURFERDEGENERATEFACE = 1801
    """Please Document."""
    ALIGN_OPERATIONINTERRUPTED = 1900
    """Please Document."""
    IGA_NOGEOMZONELETFORSPLINEFITTING = 5001
    """Please Document."""
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
