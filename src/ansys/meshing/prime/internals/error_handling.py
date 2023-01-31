import re
from functools import wraps

from ansys.meshing.prime.autogen.primeconfig import ErrorCode, WarningCode

prime_error_messages = {
    ErrorCode.NOERROR: "Success.",
    ErrorCode.UNKNOWN: "Unknown Error.",
    ErrorCode.SIGSEGV: "Segmentation Violation.",
    ErrorCode.READPMDATFAILED: "Failed to read PMDAT. Kindly check the path or filename specified.",
    ErrorCode.EXPORTFLUENTCASEFAILED: "Failed to export fluent case.",
    ErrorCode.EXPORTFLUENTMESHINGMSHFAILED: "Failed to export fluent meshing mesh file.",
    ErrorCode.VOLUMEZONESNOTFOUNDTOEXPORTFLUENTCASE: "Cell zonelets not found to export fluent case.",
    ErrorCode.MESHNOTFOUNDTOEXPORTFLUENTMESHINGMESH: " Mesh not found to export fluent meshing mesh.",
    ErrorCode.IMPORTFLUENTMESHINGMSHFAILED: "Failed to import fluent meshing mesh file.",
    ErrorCode.IMPORTFLUENTCASEFAILED: "Failed to import fluent case file.",
    ErrorCode.WRITEPMDATFAILED: "Failed to write PMDAT file.",
    ErrorCode.FILENOTFOUND: "Incorrect File Path or Name. Kindly check your file name and path.",
    ErrorCode.SURFERFAILED: "Surface meshing failed.",
    ErrorCode.SURFERAUTOSIZEQUADUNSUPPORTED: "Program controlled surface meshing does not support quadrilateral mesh.",
    ErrorCode.SURFERAUTOSIZEMUSTBEVOLUMETRIC: "Surface meshing supports only volumetric sizefield.",
    ErrorCode.FACEZONELETSFEATURESNOTUPTODATE: "Association between edge and face zonelets is broken. Extract features by edges.",
    ErrorCode.SURFERLAYEREDQUADFAILED: "Layered quad meshing failed.",
    ErrorCode.SURFERINVALIDINPUT: "Surface meshing invalid input.",
    ErrorCode.SURFERNONMANIFOLDEDGE: "Surface meshing non manifold edge.",
    ErrorCode.LOCALSURFERINVALIDNUMRINGS: "Invalid number of rings input for the local surface mesh operation.",
    ErrorCode.SURFERQUADFAILED: " Quad meshing failed for surface meshing.",
    ErrorCode.SURFERINVALIDCONSTANTSIZE: "Invalid size for constant size surface meshing.",
    ErrorCode.SCAFFOLDERBADINPUTEMPTYTOPO: "Empty Topology provided to scaffolder.",
    ErrorCode.SCAFFOLDERBADINPUTNOFREEFACES: "No free faces found in current topology.",
    ErrorCode.SCAFFOLDERBADINPUTPARAMS: "Invalid scaffolder parameters setup.",
    ErrorCode.SCAFFOLDERINVALIDABSOLUTEDISTOL: "Absolute distance tolerance must be a positive double and smaller than constant mesh size.",
    ErrorCode.SCAFFOLDERINVALIDCONSTANTMESHSIZE: "Constant mesh must be a positive double.",
    ErrorCode.OUTOFMEMORY: "Out of memory.",
    ErrorCode.INTERRUPTED: "Prime operation interrupted.",
    ErrorCode.AUTOMESHFAILED: "Auto-Mesh failed.",
    ErrorCode.INVALIDPRISMCONTROLS: "Conflict of prism settings on zonelets or invalid prism controls selected.",
    ErrorCode.PERIODICSURFACESNOTSUPPORTEDFORPRISMS: "Periodic surfaces selected for prism generation, not supported.",
    ErrorCode.ALREADYVOLUMEMESHED: "Already volume meshed.",
    ErrorCode.VOLUMESNOTUPTODATE: "Volumes are not up to date. Update volumes and try again.",
    ErrorCode.QUADRATICMESHSUPPORTEDONLYFORTETS: "Quadratic meshing is supported only for tetrahedrons.",
    ErrorCode.NOACTIVESFFOUND: "Active size fields are not available.",
    ErrorCode.AITOVERLAPALONGMULTIFOUND: "Overlapping faces along mulit-connection found.",
    ErrorCode.TRIANGULATIONFAILED: "Planar triangulation failed.",
    ErrorCode.TOPOFACESREMESHFAILED: "Failed to remesh some topofaces.",
    ErrorCode.PARTNOTFOUND: "Part not found.",
    ErrorCode.TOPODATANOTFOUND: "Topodata not found.",
    ErrorCode.SIZEFIELDNOTFOUND: "Size Field not found.",
    ErrorCode.CADGEOMETRYNOTFOUND: "CAD Geometry not found.",
    ErrorCode.VOLUMENOTFOUND: "Volume not found.",
    ErrorCode.ZONENOTFOUND: "Zone not found.",
    ErrorCode.NOTSUPPORTEDFORTOPOLOGYPART: "Not supported for part with topology data.",
    ErrorCode.NOTSUPPORTEDFORHIGHERORDERMESHPART: "Not supported for part with higher order mesh.",
    ErrorCode.SPHEREATINVALIDNORMALNODESFAILED: "Sphere creation at invalid normal nodes failed.",
    ErrorCode.INVALIDPLANEPOINTS: "Invalid plane points. You need to provide 3 points (9 coordinates).",
    ErrorCode.PLANECOLLINEARPOINTS: "Collinear or duplicate points given to define plane.",
    ErrorCode.INVALIDREGISTERID: "Invalid register id provided. Register ids between 1 to 28 are valid.",
    ErrorCode.SURFACEFEATURETYPENOTSUPPORTED: "Surface search for provided feature type is not supported.",
    ErrorCode.DELETEZONELETSCONNECTEDTOCELLS: "Cannot delete face zonelets connected to volume mesh.",
    ErrorCode.DELETEZONELETSFAILED: "Delete zonelets failed.",
    ErrorCode.PROJECTONCADGEOMETRYFAILED: "Projection on CAD geometry failed.",
    ErrorCode.ZONESARENOTOFSAMETYPE: "Zones selected are not of same type.",
    ErrorCode.TOPOEDGESREMESHFAILED: "Failed to remesh topoedges.",
    ErrorCode.DUPLICATENODESFOUND: "Duplicate nodes found.",
    ErrorCode.DUPLICATEFACESFOUND: "Duplicate faces found.",
    ErrorCode.EDGEINTERSECTINGFACEFOUND: "Edge intersects face.",
    ErrorCode.SEPARATIONRESULTSFAILED: "Failed to separate faces. Kindly provide valid inputs.",
    ErrorCode.SIZEFIELDCOMPUTATIONFAILED: "Size Field computation failed.",
    ErrorCode.REFRESHSIZEFIELDSFAILED: "Refresh Size Fields failed.",
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
    ErrorCode.INVALIDGLOBALMINMAX: "Invalid global min, max value.",
    ErrorCode.INVALIDSIZECONTROLINPUTS: "Invalid size control input. Kindly verify sizing parameters of size control.",
    ErrorCode.INVALIDSIZECONTROLSCOPE: "Invalid size control scope. Failed to evaluate scope for the size control.",
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
    ErrorCode.MATERIALPOINTWITHGIVENNAMEDOESNTEXIST: "Material point with given name does not exist.",
    ErrorCode.IGA_INCORRECTCONTROLPOINTSIZEWRTDEGREE: "Control Points size must be greater than degree.",
    ErrorCode.IGA_INCORRECTCONTROLPOINTSIZEWRTINPUT: "Control Points size cannot be greater than input mesh nodes.",
    ErrorCode.IGA_NURBSFITTINGFAILED: "Failed to fit spline.",
    ErrorCode.IGA_NEGATIVEJACOBIAN: "Negative Jacobian found.",
    ErrorCode.IGA_NURBSOPFAILED: "Spline operation failed.",
    ErrorCode.IGA_PERIODICKNOTVECTORCONVERSIONFAILED: "Periodic knot vector conversion failed.",
    ErrorCode.IGA_HREFINEMENTFAILED: "H refinement failed.",
    ErrorCode.IGA_PREFINEMENTFAILED: "P refinement failed.",
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
    ErrorCode.WRAPPERGLOBALSETTINGSNOTSET: "Wrapper global settings are not set.",
    ErrorCode.WRAPPERRESOLVEINTERSECTIONFAILED: "Wrapper resolve intersection step failed.",
    ErrorCode.WRAPPERCONNECTFAILED: "Wrapper connection generic failure.",
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
    ErrorCode.INVALIDWRAPPERCONTROL: "Invalid wrapper control.",
    ErrorCode.WRAPPERCLOSEGAPS_INVALIDGAPSIZE: "Gap size specified for close gaps should be positive double.",
    ErrorCode.WRAPPERCLOSEGAPS_INVALIDSCOPE: "Scope specified for close gaps is invalid.",
    ErrorCode.WRAPPERCLOSEGAPSFAILED: "Wrapper gap closing failed.",
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
    ErrorCode.FILLHOLEFAILED: "Unable to create capping surface.",
    ErrorCode.INVALIDINPUTPART: "Part is invalid.",
    ErrorCode.INVALIDSCOPEENTITYTYPEINPUT: "Invalid input scope entity type.",
    ErrorCode.ENTITIESSHOULDBEADDEDTOZONEUSINGPARTITBELONGS: "Entities should be added to zone using part it belongs.",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORPMDAT: "Provided file extension is not supported. Supported extensions are .pmdat and .pmdat.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTMESHINGMESH: "Provided file extension is not supported. Supported extensions are .msh and .msh.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTCASE: "Provided file extension is not supported. Supported extensions are .cas and .cas.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORKEYWORDFILE: "Provided file extension is not supported. Supported extensions are .k and .key",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORMAPDLCDB: "Provided file extension is not supported. Supported extension is .cdb",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTSIZEFIELD: "Provided file extension is not supported. Supported extensions are .sf and .sf.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORSIZEFIELD: "Provided file extension is not supported. Supported extensions are .psf and .psf.gz",
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
    ErrorCode.PLUGINLOADFAILURE: "Failed to load surface editor plugin.",
    ErrorCode.INPUTNOTCOMPLETE: "Input provided is incomplete.",
    ErrorCode.SURFERCANNOTREMESHPERIODICZONELETS: "Remesh is not supported for periodic face zonelets.",
    ErrorCode.EXTRACTVOLUMESFAILED: "Extract volumes failed.",
    ErrorCode.REFINEATCONTACTSFAILED: "Failed to refine at contacts.",
    ErrorCode.RECOVERPERIODICSURFACESFAILED: "Failed to recover periodic surfaces.",
    ErrorCode.RECOVERPERIODICSURFACESINVALIDSCOPE: "Source face zonelets are empty. Invalid scope input.",
    ErrorCode.CHECKPERIODICPAIRSFAILED: "Failed to recover periodic surfaces. No matching periodic face pair found. Check the inputs.",
    ErrorCode.PERIODICSURFACESEDGESMISMATCH: "Failed to recover periodic surfaces. Edge entities do not match on periodic source and target surfaces.",
    ErrorCode.CREATECAPONFACEZONELETSFAILED: "Failed to create cap on face zonelets.",
    ErrorCode.INTERSECTIONINTARGETVOLUMES: "Found overlapping or intersecting target volumes.",
    ErrorCode.INTERSECTIONINCUTTERVOLUMES: "Found overlapping or intersecting cutter volumes.",
    ErrorCode.SUBTRACTVOLUMEFAILED: "Failed to subtract volumes.",
    ErrorCode.ZONELETSARENOTOFSAMEDIMENSION: "Zonelets are not of same dimension.",
    ErrorCode.MERGEZONELETSFAILED: "Merge zonelets failed.",
    ErrorCode.MERGESMALLZONELETSSUPPORTEDFORFACEZONELETS: "Merge small zonelets option is supported for only face zonelets.",
    ErrorCode.INVALIDINPUTVOLUMES: "Invalid input volumes.",
    ErrorCode.MATCHEDMESHOPTIONINVALID: "Invalid option chosen to connect two different parts.",
    ErrorCode.COLOCATEMATCHEDNODESFAILED: "Colocation of matched nodes failed.",
    ErrorCode.IMPRINTBOUNDARYNODESFAILED: "Imprint of boundary nodes failed.",
    ErrorCode.IMPRINTBOUNDARYEDGESFAILED: "Imprint of boundary edges failed.",
    ErrorCode.SPLITINTERSECTINGBOUNDARYEDGESFAILED: "Splitting of intersecting boundary edges failed.",
    ErrorCode.MATCHINTERIORFAILED: "Matching of interior region of overlap failed.",
    ErrorCode.TOLERANCEVALUEINVALID: "Invalid tolerance value specified.",
    ErrorCode.SOURCEORTARGETNOTSPECIFIED: "No target or source faces specified.",
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
    WarningCode.OVERRIDECURVATURESIZINGPARAMS: "Invalid curvature sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDESOFTSIZINGPARAMS: "Invalid soft sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEHARDSIZINGPARAMS: "Invalid hard sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEPROXIMITYSIZINGPARAMS: "Invalid proximity sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEBOISIZINGPARAMS: "Invalid BOI sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEMESHEDSIZINGPARAMS: "Invalid meshed sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDESURFACESCOPEENTITY: "Invalid surface scope entity, override by face zonelets.",
    WarningCode.OVERRIDEVOLUMESCOPEENTITY: "Invalid volume scope entity, override by volume.",
    WarningCode.MAXOFPRISMCONTROLSMINASPECTRATIO: "Maximum value of min aspect ratio from selected prism controls is considered for all selected prism controls.",
    WarningCode.OVERRIDESUGGESTEDNAME: "Given name not available. Overriding it with unique name.",
    WarningCode.WRAPPER_SIZECONTROLNOTDEFINED: "No size controls provided for wrapper. Global sizes will be used.",
    WarningCode.WRAPPER_SIZECONTROLNOTSUPPORTED: "Size control is not supported in wrapper. Skipping it.",
    WarningCode.WRAPPER_SMALLERCONTACTPREVENTIONSIZE: "Contact prevention size is smaller than base size. Size will be adjusted to base size.",
    WarningCode.WRAPPER_SMALLERSIZEATFEAURES: "Size at features is smaller than base size. Size will be adjusted to base size.",
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
}


class PrimeRuntimeError(Exception):
    '''Runtime error for PyPrimeMesh.'''

    def __init__(self, message, error_code: ErrorCode = None, error_locations=None):
        super().__init__()
        self._message = self.__process_message(message)
        self._error_code = error_code
        self._error_locations = error_locations

    def __str__(self) -> str:
        return self._message

    def __process_message(self, message: str):
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
    '''Runtime warning for PyPrimeMesh.'''

    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self) -> str:
        return self._message

    @property
    def message(self):
        """Warning message to be reported."""
        return self._message


def communicator_error_handler(
    _func=None,
    *,
    expected_token='Results',
    server_error_token='ServerError',
    info_token='info_msg',
    warning_token='warning_msg',
    error_token='err_msg',
):
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
    def decorator_error_code(func):
        @wraps(func)
        def wrapper_error_code(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except RuntimeError as err:
                import logging

                logging.exception(err)
                raise
            if result is not None:
                if isinstance(result, dict):
                    error_code = result.get('errorCode', None)
                    error_location_arr = result.get('errorLocations', None)
                    error_locations = (
                        [
                            error_location_arr[i : i + 3]
                            for i in range(0, len(error_location_arr), 3)
                        ]
                        if error_location_arr is not None
                        else []
                    )
                    if error_code is not None:
                        if error_code > 0:
                            error_location_msg = (
                                f'\nError Locations: {error_locations}'
                                if len(error_locations) > 0
                                else f''
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
                                prime_warning_messages.get(
                                    WarningCode(w), f'Unrecogonized warning {w}'
                                ),
                                PrimeRuntimeWarning,
                                stacklevel=4,
                            )
                            for w in prime_warnings
                        ]

            return result

        return wrapper_error_code

    if _func is None:
        return decorator_error_code
    else:
        return decorator_error_code(_func)


def apply_if(decorator, condition):
    def decorator_apply_if(func):
        if not condition:
            return func
        return decorator(func)

    return decorator_apply_if
