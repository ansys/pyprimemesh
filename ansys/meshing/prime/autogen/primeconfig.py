""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *


class ErrorCode(enum.IntEnum):
    """Please Document
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
    SURFERWITHAUTOSIZINGFAILED = 9
    """Surface meshing with auto sizing failed."""
    FACEZONELETSFEATURESNOTUPTODATE = 10
    """Face zonelets features are not up to date."""
    SURFERAUTOSIZEQUADUNSUPPORTED = 11
    """Auto sizing for quad meshing is not supported."""
    SURFERAUTOSIZEMUSTBEVOLUMETRIC = 12
    """Auto sizing must be of volumetric type."""
    SURFERDEGENERATEFACE = 13
    """Face is degenerated for surface meshing."""
    SURFERNONMANIFOLDEDGE = 14
    """Non manifold edge for meshing."""
    MAPMESHINGFAILED = 15
    """Please Document"""
    CHECKSLICERINPUTFAILED = 17
    """Please Document"""
    SLICERINPUTFREEMULTIFACES = 18
    """Please Document"""
    SLICERINPUTOVERLAPPINGFACES = 19
    """Please Document"""
    SLICERINPUTINTERSECTINGFACES = 20
    """Please Document"""
    PRESLICERFAILED = 21
    """Please Document"""
    POSTSLICERFAILED = 22
    """Please Document"""
    SLICERPROJECTIONINTERSECTINGFACES = 23
    """Please Document"""
    SLICERFAILED = 24
    """Please Document"""
    IMPROVESLICEDPARTFAILED = 25
    """Please Document"""
    INFLATESLICECELLNODESFAILED = 26
    """Please Document"""
    DELETETRAPPEDSLICESFAILED = 27
    """Please Document"""
    CHECKSLICEDLAYERSFAILED = 28
    """Please Document"""
    SURFERINVALIDCONSTANTSIZE = 40
    """Invalid size for constant size surface meshing."""
    SCAFFOLDERBADINPUTEMPTYTOPO = 50
    """Please Document"""
    SCAFFOLDERBADINPUTNOFREEFACES = 51
    """Please Document"""
    SCAFFOLDERBADINPUTPARAMS = 52
    """Please Document"""
    SHELLBLFAILED = 60
    """Please Document"""
    SHELLBLQUADS = 61
    """Please Document"""
    SHELLBLNOMESH = 62
    """Please Document"""
    SHELLBLFEWLAYERS = 63
    """Please Document"""
    SHELLBLWRONGTOPO = 64
    """Please Document"""
    OGRIDREFINEFAILED = 65
    """Please Document"""
    SPLITTOTRIFAILED = 66
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
    COMPUTEBODIESFAILED = 109
    """Please Document"""
    ALREADYVOLUMEMESHED = 110
    """Please Document"""
    INVALIDPRISMCONTROLS = 111
    """Please Document"""
    VOLUMESNOTUPTODATE = 112
    """Please Document"""
    QUATRICMESHSUPPORTEDONLYFORTETS = 113
    """Please Document"""
    NOACTIVESFFOUND = 114
    """Please Document"""
    AUTOMESHSIZEFILEDTYPENOTSUPPORTED = 115
    """Specified size field type is not supported for specified volume fill type."""
    AUTOMESHINVALIDMAXSIZE = 116
    """Invalid max size for auto volume meshing."""
    AUTOMESHHEXCOREFAILED = 117
    """Hex generation part of volume meshing failed."""
    INVALIDVOLUMECONTROLS = 118
    """Invalid volume controls specified for volume meshing."""
    OUTOFMEMORY = 200
    """Please Document"""
    INTERRUPTED = 201
    """Please Document"""
    GETSTATISTICSFAILED = 250
    """Please Document"""
    GETELEMENTCOUNTFAILED = 251
    """Please Document"""
    PARTNOTFOUND = 300
    """Please Document"""
    TOPODATANOTFOUND = 301
    """Please Document"""
    SIZEFIELDNOTFOUND = 302
    """Please Document"""
    ZONESARENOTOFSAMETYPE = 303
    """Please Document"""
    PARTNOTMESHED = 304
    """Please Document"""
    INVALIDINPUTPART = 305
    """Please Document"""
    CADGEOMETRYNOTFOUND = 306
    """Please Document"""
    VOLUMENOTFOUND = 307
    """Please Document"""
    SPHEREATINVALIDNORMALNODESFAILED = 350
    """Please Document"""
    PROJECTONCADGEOMETRYFAILED = 351
    """Please Document"""
    SEPARATIONRESULTSFAILED = 360
    """Please Document"""
    STRUCTUREDBLOCKSEPARATIONFAILED = 361
    """Please Document"""
    MERGEFACEZONELETSRESULTSFAILED = 371
    """Please Document"""
    COPYFACEZONELETSRESULTSFAILED = 372
    """Please Document"""
    COPYEDGEZONELETSRESULTSFAILED = 373
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
    WRITESIZEFIELDFAILED = 503
    """Please Document"""
    READPMDBFAILED = 504
    """Please Document"""
    READCDBFAILED = 505
    """Please Document"""
    WRITECDBFAILED = 506
    """Please Document"""
    READG2MFAILED = 507
    """Please Document"""
    WRITEM2GFAILED = 508
    """Please Document"""
    READNLAD2DFAILED = 509
    """Please Document"""
    WRITENLAD2DFAILED = 510
    """Please Document"""
    PATHNOTFOUND = 511
    """Please Document"""
    READPROJFAILED = 512
    """Please Document"""
    WRITEPROJFAILED = 513
    """Please Document"""
    READMZPROJECTFAILED = 514
    """Please Document"""
    WRITEMZPROJECTFAILED = 515
    """Please Document"""
    WRITEBLOCKINGFAILED = 516
    """Please Document"""
    READKEYWORDFILEFAILED = 517
    """Please Document"""
    WRITEKEYWORDFILEFAILED = 518
    """Please Document"""
    QUADRATICMESH_WRITEMESHFAILED = 519
    """Please Document"""
    INCLUDEKFILENOTFOUND = 520
    """Please Document"""
    READVTKFAILED = 521
    """Please Document"""
    READSIZECONTROLFAILED = 522
    """Please Document"""
    WRITESIZECONTROLFAILED = 523
    """Please Document"""
    FILENOTFOUND = 524
    """Please Document"""
    READPMDATFAILED = 525
    """Please Document"""
    CREATECHECKPOINTFAILED = 550
    """Please Document"""
    RESTORECHECKPOINTFAILED = 551
    """Please Document"""
    CLEARCHECKPOINTFAILED = 552
    """Please Document"""
    UNDOFAILED = 570
    """Please Document"""
    REDOFAILED = 571
    """Please Document"""
    WELDCONTROLNOTDEFINED = 600
    """Please Document"""
    WELDMESHERBADINPUTPARAMS = 601
    """Please Document"""
    WELDINPUTWELDEDGEEMPTY = 602
    """Please Document"""
    NEARBYENTITYNOTFOUND = 603
    """Please Document"""
    CREATETENTFACESFAILED = 604
    """Please Document"""
    WELDFACESCONNECTEDBADLY = 605
    """Please Document"""
    SPOTWELDLOCATIONSNOTPROVIDED = 606
    """Please Document"""
    SPOTWELDLOCATIONSINFOINCOMPLETE = 607
    """Please Document"""
    SPOTWELDCREATIONFAILED = 608
    """Please Document"""
    SPOTWELDNOFACESFOUNDWITHININPUTRADIUS = 609
    """Please Document"""
    SPOTWELDDESIREDNUMBEROFLAYERSNOTFOUND = 610
    """Please Document"""
    ORTHOGONALSPOTWELDNOTPOSSIBLE = 611
    """Please Document"""
    SPOTWELDSNAPTOEDGETOLNOTPROVIDED = 612
    """Please Document"""
    SPOTWELDLABELSNOTDEFINED = 613
    """Please Document"""
    SPOTWELDSNAPTOEDGEVIOLATESANGLETOL = 614
    """Please Document"""
    WELDLINETOOCLOSETOUPEGDE = 615
    """Please Document"""
    WELDINPUTEDGESDONTBELONGTOUPFACES = 616
    """Please Document"""
    WELDINPUTUPFACEEMPTY = 617
    """Please Document"""
    WELDINPUTDOWNFACEEMPTY = 618
    """Please Document"""
    WELDINPUTEDGELISTHASREPETITION = 619
    """Please Document"""
    WELDINPUTUPFACELISTHASREPETITION = 620
    """Please Document"""
    WELDINPUTDOWNFACELISTHASREPETITION = 621
    """Please Document"""
    WELDINPUTWELDEDGENOTCONTINUOUS = 622
    """Please Document"""
    WELDWRONGLAPWELDANGLEINPUT = 623
    """Please Document"""
    WELDREPLACESUPPRESSFAILURE = 624
    """Please Document"""
    SPOTWELDLOCATIONSOUTSIDEBBOX = 625
    """Please Document"""
    RIGIDWELDNOEXTENSIONFACESEXITS = 626
    """Please Document"""
    SPOTWELDINPUTMESHSIZENOTPROVIDED = 627
    """Please Document"""
    WELDUNABLETOFINDUPFACEEDGE = 628
    """Please Document"""
    WELDINTERSECTIONCONFIGURATIONNOTSUPPORTED = 629
    """Please Document"""
    WELDINTERSECTIONWORKSFOREXTENSIONONLY = 630
    """Please Document"""
    WELDINTERSECTIONGAPFILLINGFAILED = 631
    """Please Document"""
    WELDINTERSECTIONREQUIRESSUCCESSFULWELDCREATION = 632
    """Please Document"""
    WELDINTERSECTIONINVALIDWELDCONTROLID = 633
    """Please Document"""
    WELDINTERSECTIONNEEDSATLEASTTWOWELDS = 634
    """Please Document"""
    OCTFORESTCONSTRUCTIONFAILED = 700
    """Please Document"""
    CONFORMALHEXMESHINGPROJECTIONFAILED = 800
    """Please Document"""
    MECHMESHERFAILED = 900
    """Please Document"""
    INVALIDINPUTMODEL = 901
    """Please Document"""
    HARDNODENOTPRESERVED = 902
    """Please Document"""
    INTERSECTIONFAILED = 903
    """Please Document"""
    INVALIDFRACTUREMESH = 904
    """Please Document"""
    QUALITYIMPROVEMENTFAILED = 905
    """Please Document"""
    LARGESIZEDIFFERENCE = 906
    """Please Document"""
    LARGEPORTIONBADQUALITYELEMENTS = 907
    """Please Document"""
    ADAPTMESHSIZEFAILED = 908
    """Please Document"""
    INVALIDELEMENTS = 909
    """Please Document"""
    BADQUALITYELEMENTS = 910
    """Please Document"""
    QUADRATICEDGEPROJECTIONFAILED = 911
    """Please Document"""
    QUADRATICFACEPROJECTIONFAILED = 912
    """Please Document"""
    NULLPTR = 913
    """Please Document"""
    UNSUPPORTSIZEFIELDTYPE = 914
    """Please Document"""
    SPLITATHARDMIDNODE = 915
    """Please Document"""
    INPUTMESHSIZETOOCOARSE = 916
    """Please Document"""
    INPUTMESHQUALITYTOOBAD = 917
    """Please Document"""
    SMOOTHBADEDGEMIDPNTFAILED = 918
    """Please Document"""
    SIZEADAPTFAILURE = 919
    """Please Document"""
    INVERSEMAPPINGFAILURE = 920
    """Please Document"""
    LOADINGASSOCIATIONFAILED = 921
    """Please Document"""
    LOADINGGEOMETRYFAILED = 922
    """Please Document"""
    SELFMERGEFAILED = 923
    """Please Document"""
    NEWCRACKOUTSIDEOFREGION = 924
    """Please Document"""
    NEWCRACKTOOSHALLOW = 925
    """Please Document"""
    PROPERTYTABLEINVALIDTYPE = 1001
    """Please Document"""
    PACKPARTICLESNOWATERTIGHTREGION = 1100
    """Please Document"""
    NOTSUPPORTEDFORTOPOLOGYPART = 1200
    """Please Document"""
    NOTSUPPORTEDFORHIGHERORDERMESHPART = 1201
    """Please Document"""
    NOTSUPPORTEDFORNONTRIFACEZONE = 1202
    """Please Document"""
    NOTSUPPORTEDFORNONQUADFACEZONE = 1203
    """Please Document"""
    PREPAREFORSOLVERFAILED = 1300
    """Please Document"""
    MORPHFIELD_INVALIDINPUTVECTORSSIZE = 1400
    """Please Document"""
    MORPHFIELD_SOLVEFIELDFAILED = 1401
    """Please Document"""
    MORPHFIELD_EVALUATIONFIELDFAILED = 1402
    """Please Document"""
    MORPHFIELD_INVALIDOPERATIONSORDER = 1404
    """Please Document"""
    MORPHFIELD_CANNOTREADMORPHFIELDFILE = 1405
    """Please Document"""
    MORPHFIELD_CANNOTWRITEMORPHFIELDFILE = 1406
    """Please Document"""
    MORPHFIELD_CANNOTCREATEMORPHFIELD = 1407
    """Please Document"""
    MORPHFIELD_CANNOTAPPLYMORPHFIELDFILE = 1408
    """Please Document"""
    MORPHFIELD_CANNOTGATHERDATA = 1409
    """Please Document"""
    MORPHER_COMPUTEBCS = 1410
    """Please Document"""
    MORPHER_MORPHSOLVE = 1411
    """Please Document"""
    MORPHER_MORPHAPPLYSOLUTION = 1412
    """Please Document"""
    MORPHER_MORPHALONGNORMALSSOLVEANDAPPLY = 1413
    """Please Document"""
    MORPHER_EXTERNALFIELDMORPHSOLVEANDAPPLY = 1414
    """Please Document"""
    MORPHER_BCSINCORRECTINPUTFORSYMMETRY = 1415
    """Please Document"""
    MORPHER_BCSPARTIDNOTPROVIDED = 1416
    """Please Document"""
    MORPHER_MORPHWITHTRANSFORMATIONSOLVEANDAPPLY = 1417
    """Please Document"""
    MORPHFIELD_APPLYFIELDFAILED = 1418
    """Please Document"""
    MORPHFIELD_SERIALIZATIONFAILED = 1419
    """Please Document"""
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
    EXTRACTFEATURESFAILED = 1600
    """Please Document"""
    EXTRACTFEATURESBYEDGESFAILED = 1601
    """Please Document"""
    CREATEEDGEZONELETFAILED = 1602
    """Please Document"""
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
    MESHDISTRIBUTIONFAILED = 1802
    """Please Document"""
    UNOCONTROL_CONTROLNOTSTORED = 1900
    """Please Document"""
    UNOCONTROL_EMPTYCONTROLLIST = 1901
    """Please Document"""
    UNO_CANNOTOPENFILE = 1902
    """Please Document"""
    UNOCONTROL_DUPLICATEDNAMESINFILE = 1903
    """Please Document"""
    UNOCONTROL_NOTVALIDCONTROLINFILE = 1904
    """Please Document"""
    UNOCONTROL_GENERIC = 1905
    """Please Document"""
    UNOOPERATION_NOTVALIDOPERATIONINFILE = 1906
    """Please Document"""
    UNOOPERATION_NOTVALIDWORKFLOWINFILE = 1907
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
    IGA_NONCONFORMALHEXMESH = 2418
    """Structured hex-mesh in non conformal."""
    IGA_EMPTYSPLINEIDLIST = 2419
    """Spline id list is empty."""
    IGA_INVALIDREFINESPLINEPARAM = 2420
    """Invalid refine spline parameters."""
    MZMESHER_GEOMETRYTRANSFERFAILED = 2600
    """Please Document"""
    MZMESHER_BLOCKINGFAILED = 2601
    """Please Document"""
    MZMESHER_PRISMMESHINGFAILED = 2602
    """Please Document"""
    MZMESHER_MESHINGFAILED = 2603
    """Please Document"""
    MZMESHER_MESHTRANSFERFAILED = 2604
    """Please Document"""
    MZMESHER_SETMATCHCONTROLFAILED = 2605
    """Please Document"""
    SWEEPERINVALIDINPUT = 2705
    """Please Document"""
    SWEEPERINVALIDPARAMS = 2706
    """Please Document"""
    SWEEPERINTERSECTINGDIRECTIONS = 2707
    """Please Document"""
    SWEEPERCLOSEDBODYCOMPUTATIONFAILED = 2708
    """Please Document"""
    PARTHASTOPOLOGY = 2800
    """Please Document"""
    SEARCHHOLESONFACEZONELETSFAILED = 2801
    """Please Document"""
    SURFACESEARCHFAILED = 2802
    """Please Document"""
    SURFACESEARCHPARTWITHMESHNOTFOUND = 2803
    """Part with mesh not found for surface quality check."""
    NODESNOTFOUND = 2900
    """Please Document"""
    FILLHOLEFAILED = 2901
    """Please Document"""
    CREATEFACEZONELETSBYEDGEZONELETSFAILED = 2902
    """Please Document"""
    TRANSFORMATIONFAILED = 3000
    """Please Document"""
    SCALINGFAILED = 3001
    """Please Document"""
    ALIGNMENTFAILED = 3002
    """Please Document"""
    DELETEMESHFACESFAILED = 3200
    """Please Document"""
    DELETEMESHFACES_TOPOLOGYNOTSUPPORTED = 3201
    """Please Document"""
    DELETEMESHFACES_CELLFOUND = 3202
    """Please Document"""
    DELETEFRINGESANDOVERLAPSFAILED = 3203
    """Please Document"""
    MATERIALPOINTWITHSAMENAMEEXISTS = 3300
    """Please Document"""
    MATERIALPOINTWITHGIVENNAMEDOESNTEXIST = 3301
    """Please Document"""
    MATERIALPOINTWITHGIVENIDDOESNTEXIST = 3302
    """Please Document"""
    MATERIALPOINTWITHSAMEIDEXISTS = 3303
    """Please Document"""
    WRAPPERGLOBALSETTINGSNOTSET = 3400
    """Please Document"""
    WRAPPERRESOLVEINTERSECTIONFAILED = 3401
    """Please Document"""
    WRAPPERCONNECTFAILED = 3402
    """Please Document"""
    WRAPPERFATALERROR = 3403
    """Please Document"""
    WRAPPERCOULDNOTSETUPFROMXMLFILE = 3404
    """Please Document"""
    WRAPPERCOULDNOTEXTRACTINTERFACE = 3405
    """Please Document"""
    WRAPPERLEAKPREVENTIONFAILED = 3406
    """Please Document"""
    WRAPPERSURFACEHASHOLES = 3410
    """Please Document"""
    WRAPPEROCTREEREGIONINGFAILED = 3411
    """Please Document"""
    WRAPPERPROJECTIONFAILED = 3412
    """Please Document"""
    WRAPPERCONTROL_MATERIALPOINTWITHGIVENNAMEDOESNTEXIST = 3413
    """Please Document"""
    WRAPPERCONTROL_LIVEMATERIALPOINTDOESNTEXIST = 3414
    """Please Document"""
    MESHEDITCANNOTMOVEMULTIPLENODES = 3500
    """Please Document"""
    MESHEDITNODEATEDGEBOUNDARY = 3501
    """Please Document"""
    MESHEDITINVALIDPOSITION = 3502
    """Please Document"""
    MESHEDITNOTSUPPORTEDFORHIGHERORDER = 3503
    """Please Document"""
    MESHEDITNOTINITIALIZED = 3504
    """Please Document"""
    MESHEDITNOTSUPPORTEDFORPARTSWITHVOLUMEMESH = 3505
    """Please Document"""
    MESHEDITSWAPEDGEFAILED = 3506
    """Please Document"""
    MESHEDITSWAPEDGEFAILED_FACESONDIFFERENTZONELET = 3507
    """Please Document"""
    MESHEDITSWAPEDGEFAILED_TGEDGEPRESENT = 3508
    """Please Document"""
    MESHEDITNODEMOVEMENTNOTINITIALIZED = 3509
    """Please Document"""
    MESHEDITPROJECTTOPLANENOTSUPPORTTOPOLOGY = 3510
    """Please Document"""
    MESHEDITMERGETRIFACESFAILED_UNSUPPORTEDFACES = 3511
    """Please Document"""
    MESHEDITMERGENODESFAILED = 3512
    """Please Document"""
    MESHEDITPOLYNOTSUPPORTED = 3513
    """Please Document"""
    VT_BADINPUT = 3600
    """Please Document"""
    VT_MERGEFACESFAILED = 3601
    """Please Document"""
    VT_MERGETHINSTRIPESFAILED = 3602
    """Please Document"""
    VT_MERGETHINEXTFAILED = 3603
    """Please Document"""
    VT_REPAIRSHARPCORNERANGLESFAILED = 3604
    """Please Document"""
    VT_PINCHFACESFAILED = 3605
    """Please Document"""
    VT_FILLHOLEFAILED = 3606
    """Please Document"""
    VT_FILLANNULARHOLEFAILED = 3607
    """Please Document"""
    VT_COLLAPSESHORTEDGESFAILED = 3608
    """Please Document"""
    MORPHFIELDMANAGER_GENERIC = 4000
    """Please Document"""
    MORPHFIELDMANAGER_INCORRECTINPUTBBOXES = 4001
    """Please Document"""
    MORPHFIELDMANAGER_INCORRECTSTOPRECORDING = 4002
    """Please Document"""
    MORPHFIELDMANAGER_FILEERROR = 4003
    """Please Document"""
    MORPHFIELDMANAGER_INCORRECTNAME = 4004
    """Please Document"""
    MORPHFIELDMANAGER_DUPLICATENAME = 4005
    """Please Document"""
    MORPHFIELDPLAYER_GENERIC = 5001
    """Please Document"""
    MORPHFIELDPLAYER_MORPHFIELDNOTINITIALIZED = 5002
    """Please Document"""
    MORPHFIELDPLAYER_MORPHFIELDALREADYINITIALIZED = 5003
    """Please Document"""
    MORPHFIELDPLAYER_SOLVEFAILED = 5004
    """Please Document"""
    MORPHFIELDPLAYER_INCORRECTNAME = 5005
    """Please Document"""
    MORPHFIELDPLAYER_DUPLICATENAME = 5006
    """Please Document"""
    MORPHFIELDPLAYER_ONLYTRANSFORMATIONSUPPORT = 5007
    """Please Document"""
    CREATENODEENTITIESFAILED = 5500
    """Please Document"""
    CREATEEDGEENTITIESFAILED = 5501
    """Please Document"""
    CREATEFACEENTITIESFAILED = 5502
    """Please Document"""
    EXPRESSION_MISSING_OPERATOR = 7100
    """Please Document"""
    EXPRESSION_UNSUPPORTED_OPERATOR = 7101
    """Please Document"""
    EXPRESSION_MISPLACED_OPERATOR = 7102
    """Please Document"""
    EXPRESSION_MISSING_VARIABLE_VALUE = 7103
    """Please Document"""
    EXPRESSION_ARITHMETIC_EXCEPTION = 7104
    """Please Document"""

class WarningCode(enum.IntEnum):
    """Warning codes associated with failure of PRIME operation.
    """
    NOWARNING = 0
    UNKNOWN = 1
    WELD_WIDTHADJUSTFAILED = 5
    WELD_HEIGHTADJUSTFAILED = 6
    WELD_INTERSECTIONFOUND = 7
    SPOTWELD_FACELABELSNOTPROVIDED = 8
    SPOTWELD_NOFACESWITHPROVIDEDLABELSEXITS = 9
    SPOTWELD_RBEONTRIFACE = 10
    WELD_WRONGINPUTTOLERANCE = 11
    WELD_WRONGINPUTANGLE = 12
    WELD_SHARPBENDINWELDCURVE = 13
    SPOTWELD_DEGENERATEDBEAM = 14
    WELD_PARTIALWELDCREATED = 15
    WELD_NOEXTENSIONFACESDUETOCOINCIDENCE = 16
    WELD_INTERSECTIONNEEDSATLEASTTWOWELDS = 17
    WELD_INTERSECTIONGAPFILLINGINCOMPLETE = 18
    WELD_HEIGHTADJUSTMENTNOTSUPPORTEDFORINTERSECTINGWELDS = 19
    WELD_INTERSECTIONNOTSUPPORTEDFORTENTANDEXTENSION = 20
    WELD_INTERSECTIONNOTSUPPORTEDAROUND3DFILLETSURFACE = 21
    WELD_INTERSECTIONNOTSUPPORTEDFORINTERMITTENTSEAMWELDS = 22
    WELD_SHEETTHICKNESSISTOOSMALL = 23
    WELD_SEPARATEWELDFACESCREATED = 24
    SURFER_AUTOSIZING_MULTITHREADINGNOTSUPPORTED = 101
    SURFER_QUADCLEANUP_MULTITHREADINGNOTSUPPORTED = 102
    OVERRIDECURVATURESIZINGPARAMS = 201
    OVERRIDESOFTSIZINGPARAMS = 202
    OVERRIDEHARDSIZINGPARAMS = 203
    OVERRIDEPROXIMITYSIZINGPARAMS = 204
    OVERRIDEBOISIZINGPARAMS = 205
    OVERRIDEMESHEDSIZINGPARAMS = 206
    OVERRIDESUGGESTEDNAME = 301
    MORPHER_BIASINGNOMORPHNODES = 1600
    MORPHER_MOVABLEEDGESUNSUPPORTED = 1601
    MORPHER_ONSELECTIONWHILEMORPHING = 1602
    MORPHFIELD_RECORDINGCANCELLED = 1700
    MORPHFIELD_APPLYCANCELLED = 1701
    UNOCONTROL_EMPTYCONTROLLIST = 1800
    UNOCONTROL_CONTROLNOTSTORED = 1801
    UNOCONTROL_NOCONTROLSINFILE = 1802
    UNOCONTROL_DUPLICATEDNAMES = 1902
    UNOCONTROL_INVALIDCONTROLFILE = 1803
    UNOCONTROL_INVALIDSCOPETYPE = 1804
    UNOCONTROL_INVALIDSCOPEENTITY = 1805
    UNOCONTROL_INVALIDDATA = 1806
    UNOCONTROL_INVALIDSCOPEENTITYSIZE = 1807
    UNOOPERATION_NOOPERATIONSINFILE = 1808
    UNOOPERATION_INVALIDOPERATIONFILE = 1809
    UNOWORKFLOW_NOOPERATIONSINFILE = 1810
    UNOWORKFLOW_INVALIDOPERATIONFILE = 1811
    UNOWORKFLOW_NOWORKFLOWSINFILE = 1812
    UNOWORKFLOW_INVALIDWORKFLOWFILE = 1813
    SURFERLAYEREDQUADFAILED = 1800
    SURFERDEGENERATEFACE = 1801
    ALIGN_OPERATIONINTERRUPTED = 1900
    MORPHFIELDMANAGER_INCORRECTNAME = 4004
    MORPHFIELDMANAGER_DUPLICATENAME = 4005
    IGA_NOGEOMZONELETFORSPLINEFITTING = 5001
