from functools import wraps

from ansys.meshing.prime.autogen.primeconfig import ErrorCode, WarningCode
import re

prime_error_messages = {
    ErrorCode.NOERROR : "Success.",
    ErrorCode.UNKNOWN : "Unknown Error.",
    ErrorCode.SIGSEGV : "Segmentation Violation.",
    ErrorCode.READPMDATFAILED : "Failed to read PMDAT. Kindly check the path or filename specified.",
    ErrorCode.EXPORTFLUENTCASEFAILED : "Failed to export fluent case.",
    ErrorCode.EXPORTFLUENTMESHINGMSHFAILED: "Failed to export fluent meshing mesh file.",
    ErrorCode.VOLUMEZONESNOTFOUNDTOEXPORTFLUENTCASE : "Cell zonelets not found to export fluent case.",
    ErrorCode.IMPORTFLUENTMESHINGMSHFAILED : "Failed to import fluent meshing mesh file.",
    ErrorCode.IMPORTFLUENTCASEFAILED : "Failed to import fluent case file.",
    ErrorCode.WRITEPMDATFAILED : "Failed to write PMDAT file.",
    ErrorCode.FILENOTFOUND : "Incorrect File Path or Name. Kindly check your file name and path.",
    ErrorCode.SURFERFAILED : "Surfer Failed.",
    ErrorCode.SURFERAUTOSIZEQUADUNSUPPORTED : "Program controlled surface meshing does not support quadrilateral mesh.",
    ErrorCode.SURFERAUTOSIZEMUSTBEVOLUMETRIC : "Surface meshing supports only volumetric sizefield.",
    ErrorCode.FACEZONELETSFEATURESNOTUPTODATE : "Association between edge and face zonelets is broken. Try extract features by edges to correct.",
    ErrorCode.SURFERLAYEREDQUADFAILED : "Layered quad meshing failed.",
    ErrorCode.SURFERINVALIDINPUT : "Surfer invalid input.",
    ErrorCode.SURFERNONMANIFOLDEDGE : "Surfer non manifold edge.",
    ErrorCode.LOCALSURFERINVALIDNUMRINGS : "Invalid number of rings input for the local surface mesh operation.",
    ErrorCode.SURFERQUADFAILED : "Surfer quad meshing failed.",
    ErrorCode.SURFERINVALIDCONSTANTSIZE : "Invalid size for constant size surface meshing.",
    ErrorCode.SCAFFOLDERBADINPUTEMPTYTOPO : "Empty Topology provided to scaffolder.",
    ErrorCode.SCAFFOLDERBADINPUTNOFREEFACES : "No free faces found in current topology.",
    ErrorCode.SCAFFOLDERBADINPUTPARAMS : "Wrong scaffolder params setup.",
    ErrorCode.OUTOFMEMORY : "Out of memory.",
    ErrorCode.INTERRUPTED : "Prime operation interrupted.",
    ErrorCode.AUTOMESHFAILED : "Auto-Mesh Failed.",
    ErrorCode.INVALIDPRISMCONTROLS : "Conflict of prism settings on zonelets or invalid prism controls selected.",
    ErrorCode.ALREADYVOLUMEMESHED : "Already volume meshed.",
    ErrorCode.VOLUMESNOTUPTODATE : "Volumes are not up to date. Update volumes and try again.",
    ErrorCode.QUATRICMESHSUPPORTEDONLYFORTETS : "Volumes are not up to date. Update volumes and try again.",
    ErrorCode.NOACTIVESFFOUND : "Active size fields are not available.",
    ErrorCode.AITOVERLAPALONGMULTIFOUND : "Overlapping faces along mulit-connection found.",
    ErrorCode.TRIANGULATIONFAILED : "Planar triangulation failed.",
    ErrorCode.TOPOFACESREMESHFAILED : "Failed to Remesh some topofaces.",
    ErrorCode.PARTNOTFOUND : "Part not found.",
    ErrorCode.TOPODATANOTFOUND : "Topo Data not found.",
    ErrorCode.SIZEFIELDNOTFOUND : "Size Field not found.",
    ErrorCode.CADGEOMETRYNOTFOUND : "CAD Geometry not found.",
    ErrorCode.VOLUMENOTFOUND : "Volume not found.",
    ErrorCode.ZONENOTFOUND : "Zone not found.",
    ErrorCode.NOTSUPPORTEDFORTOPOLOGYPART : "Not supported for part with topology data.",
    ErrorCode.NOTSUPPORTEDFORHIGHERORDERMESHPART : "Not supported for part with higher order mesh.",
    ErrorCode.SPHEREATINVALIDNORMALNODESFAILED : "Sphere creation at invalid normal nodes failed.",
    ErrorCode.INVALIDPLANEPOINTS : "Invalid plane points. You need to provide 3 points (9 coordinates).",
    ErrorCode.PLANECOLLINEARPOINTS : "Collinear or duplicate points given to define plane.",
    ErrorCode.INVALIDREGISTERID : "Invalid register id provided. Register ids between 1 to 28 are valid.",
    ErrorCode.DELETEZONELETSCONNECTEDTOCELLS : "Cannot delete face zonelets connected to volume mesh.",
    ErrorCode.DELETEZONELETSFAILED : "Delete zonelets failed.",
    ErrorCode.PROJECTONCADGEOMETRYFAILED : "Projection on CAD Geometry failed.",
    ErrorCode.ZONESARENOTOFSAMETYPE : "Zones selected are not of same type.",
    ErrorCode.TOPOEDGESREMESHFAILED : "Failed tp Remesh topoedges.",
    ErrorCode.DUPLICATENODESFOUND : "Duplicate nodes found.",
    ErrorCode.DUPLICATEFACESFOUND : "Duplicate faces found.",
    ErrorCode.EDGEINTERSECTINGFACEFOUND : "Edge intersects face.",
    ErrorCode.SEPARATIONRESULTSFAILED : "Failed to separate faces. Kindly provide valid inputs.",
    ErrorCode.SIZEFIELDCOMPUTATIONFAILED : "Size Field computation failed.",
    ErrorCode.REFRESHSIZEFIELDSFAILED : "Refresh Size Fields failed.",
    ErrorCode.SIZEFIELDTYPENOTSUPPORTED : "Provided Size Field Type is not supported by this operation.",
    ErrorCode.INVALIDSIZECONTROLS : "Invalid size controls selected to compute size field.",
    ErrorCode.TETIMPROVEFAILED : "Tet improvement failed.",
    ErrorCode.AUTONODEMOVEFAILED : "Tet improvement using auto node movement failed.",
    ErrorCode.COMPUTEVOLUMESFAILED : "Compute volumes failed.",
    ErrorCode.READMESHFAILED : "Read Mesh failed.",
    ErrorCode.WRITEMESHFAILED : "Write Mesh failed.",
    ErrorCode.QUADRATICMESH_WRITEMESHFAILED : "Saving quadratic mesh into .msh format is not supported. Try saving it as .cdb, .m2g or .k File.",
    ErrorCode.CADIMPORTFAILED : "CAD Import failed.",
    ErrorCode.READSIZEFIELDFAILED : "Read Size Field failed.",
    ErrorCode.WRITESIZEFIELDFAILED : "Write Size Field failed.",
    ErrorCode.READPMDBFAILED : "Read PMDB failed.",
    ErrorCode.READCDBFAILED : "Read CDB failed.",
    ErrorCode.WRITECDBFAILED : "Write CDB failed.",
    ErrorCode.READKEYWORDFILEFAILED : "Read K file failed.",
    ErrorCode.WRITEKEYWORDFILEFAILED : "Write K file failed.",
    ErrorCode.INCLUDEKFILENOTFOUND : "Referenced K file not found.",
    ErrorCode.READSIZECONTROLFAILED : "Read Size Control failed.",
    ErrorCode.WRITESIZECONTROLFAILED : "Write Size Control failed.",
    ErrorCode.PATHNOTFOUND : "File path not found.",
    ErrorCode.UNDOFAILED : "Undo failed.",
    ErrorCode.REDOFAILED : "Redo failed.",
    ErrorCode.GETSTATISTICSFAILED : "Get statistics failed.",
    ErrorCode.GETELEMENTCOUNTFAILED : "Get element count failed.",
    ErrorCode.EXTRACTFEATURESBYANGLEFAILED : "Feature extraction by angle failed.",
    ErrorCode.EXTRACTFEATURESBYINTERSECTIONFAILED : "Feature extraction by intersection failed.",
    ErrorCode.EXTRACTFEATURESBYEDGESFAILED : "Feature extraction by edge tracing failed.",
    ErrorCode.CREATEEDGEZONELETFAILED : "Create edge zonelets by node path failed.",
    ErrorCode.NOSIDEFRONTFACES : "Empty side and front faces input.",
    ErrorCode.NOTALLSIDEFRONTFACES : "Not all side/front faces of volume/part input.",
    ErrorCode.NOMESHONSIDEFACES : "No mesh on side topofaces.",
    ErrorCode.NOMESHONFRONTFACES : "No mesh on front topofaces.",
    ErrorCode.TETINITFAILED : "Tetrahedra Initialization failed.",
    ErrorCode.TETCUTFAILED : "MidSurf Tet Cutting failed.",
    ErrorCode.MIDSURFACEFAILED : "MidSurf extration failed.",
    ErrorCode.IMPRINTFAILED : "Midsurf Imprint failed.",
    ErrorCode.INVALIDSIDETHICKNESS : "Midsurf invalid side thickness.",
    ErrorCode.NOTMIDSURFTOPOFACE : "Not a midsurf topoface.",
    ErrorCode.NOTUNIFORMTHICKNESSMIDSURFTOPOFACE : "No uniform thickness associated with topoface.",
    ErrorCode.OPENSIDEFACELOOPS : "Detected side topofaces do not form closed loop.",
    ErrorCode.SINGLESETFRONTFACES : "Detected only one set of front topofaces.",
    ErrorCode.VOLUMEMESH_MIDNODESNOTSUPPORTED : "Improve volume mesh error: meshes with mid nodes are not supported.",
    ErrorCode.VOLUMEMESHNOTFOUND : "Volume mesh not found.",
    ErrorCode.NOTSUPPORTEDFORNONTRIFACEZONE : "Only triangular faces are supported.",
    ErrorCode.NOTSUPPORTEDFORNONQUADFACEZONE : "Only quadrilateral faces zonelets are supported.",
    ErrorCode.PARTNOTMESHED : "Part has unmeshed topofaces.",
    ErrorCode.INVALIDGLOBALMINMAX : "Invalid global min, max value.",
    ErrorCode.INVALIDSIZECONTROLINPUTS : "Invalid size control input. Please verify sizing parameters of size control.",
    ErrorCode.INVALIDSIZECONTROLSCOPE : "Invalid size control scope. Failed to evaluate scope for the size control.",
    ErrorCode.INVALIDPROXIMITYSIZINGINPUT : "Invalid proximity sizing input. Elements per gap should be a positive value.",
    ErrorCode.INVALIDCURVATURESIZINGINPUT : "Invalid curvature sizing input. Normal angle should be a positive value.",
    ErrorCode.TRANSFORMATIONFAILED : "Failed to transform.",
    ErrorCode.SCALINGFAILED : "Failed to scale.",
    ErrorCode.ALIGNMENTFAILED : "Failed to align.",
    ErrorCode.INVALIDTRANSFORMATIONMATRIX : "Invalid transformation matrix. You need to provide 16(4x4) elements.",
    ErrorCode.DELETEMESHFACESFAILED : "Failed to delete face element(s).",
    ErrorCode.DELETEFRINGESANDOVERLAPSFAILED : "Failed to delete fringes and overlaps.",
    ErrorCode.DELETEMESHFACES_TOPOLOGYNOTSUPPORTED : "Deletion of face element(s) is not supported for mesh with topology.",
    ErrorCode.DELETEMESHFACES_CELLFOUND : "Cannot delete face element(s) connected to volume mesh.",
    ErrorCode.MATERIALPOINTWITHSAMENAMEEXISTS : "Material point with given name already exist.",
    ErrorCode.MATERIALPOINTWITHGIVENIDDOESNTEXIST : "Material point with given id does not exist.",
    ErrorCode.MATERIALPOINTWITHGIVENNAMEDOESNTEXIST : "Material point with given name does not exist.",
    ErrorCode.IGA_INCORRECTCONTROLPOINTSIZEWRTDEGREE : "Control Points size must be greater than degree.",
    ErrorCode.IGA_INCORRECTCONTROLPOINTSIZEWRTINPUT : "Control Points size cannot be greater than input mesh nodes.",
    ErrorCode.IGA_NURBSFITTINGFAILED : "Failed to fit spline.",
    ErrorCode.IGA_NEGATIVEJACOBIAN : "Negative Jacobian found.",
    ErrorCode.IGA_NURBSOPFAILED : "Spline operation failed.",
    ErrorCode.IGA_PERIODICKNOTVECTORCONVERSIONFAILED : "Periodic knot vector conversion failed.",
    ErrorCode.IGA_HREFINEMENTFAILED : "H refinement failed.",
    ErrorCode.IGA_PREFINEMENTFAILED : "P refinement failed.",
    ErrorCode.IGA_NURBSSMOOTHFAILED : "Spline smoothing failed.",
    ErrorCode.IGA_NODEINDEXINGFAILED : "Hex-mesh is not structured.",
    ErrorCode.IGA_NOCELLZONELETS : "No cell zonelets found.",
    ErrorCode.IGA_INVALIDINPUTFILEFORSTRUCTUREDHEXMESHFITTING : "Wrong Input mesh. Only structured hex-mesh is allowed.",
    ErrorCode.IGA_INVALIDINPUTFILEFORGENUSZEROFITTING : "Wrong Input file. Only tetrahedral mesh is allowed.",
    ErrorCode.IGA_NOFACEZONELETS : "No face zonelets found.",
    ErrorCode.IGA_EDGEPATHCOMPUTATIONFAILED : "Edge path computation failed.",
    ErrorCode.IGA_INCORRECTDEGREE : "Degree 0 not allowed.",
    ErrorCode.IGA_QUADRATICMESHINPUT : "Quadratic mesh is not supported for solid spline creation.",
    ErrorCode.IGA_UNIFORMTRIMMEDNURBSFAILED : "Failed to create uniform trimmed solid spline.",
    ErrorCode.PREPAREFORSOLVERFAILED : "Preparation for solver failed.",
    ErrorCode.MERGEPARTSFAILED : "Merge parts failed.",
    ErrorCode.MERGEPARTSWANDWOTOPO : "Merge parts with topology and parts without topology are not supported.",
    ErrorCode.SETNAMEFAILED : "Set name failed.",
    ErrorCode.CONTROLNOTFOUND : "Control not found.",
    ErrorCode.NOINPUT : "No input provided.",
    ErrorCode.DELETEPARTSFAILED : "Delete parts failed.",
    ErrorCode.DELETECONTROLSFAILED : "Delete controls failed.",
    ErrorCode.WRAPPERGLOBALSETTINGSNOTSET : "Wrapper global settings are not set.",
    ErrorCode.WRAPPERRESOLVEINTERSECTIONFAILED : "Wrapper resolve intersection step failed.",
    ErrorCode.WRAPPERCONNECTFAILED : "Wrapper connection generic failure.",
    ErrorCode.WRAPPERCOULDNOTEXTRACTINTERFACE : "Failed to extract wrapper interface.",
    ErrorCode.WRAPPERLEAKPREVENTIONFAILED : "Wrapper leak prevention generic failure. Dead region is leaking to live.",
    ErrorCode.WRAPPERUNSUPPORTEDWRAPREGION : "Wrap region option provided does not support wrap operation.",
    ErrorCode.WRAPPERCONTROL_NOLIVEMATERIALPOINTSPROVIDED : "Live material points list provided for wrapper control is empty.",
    ErrorCode.WRAPPERSURFACEHASHOLES : "Wrapper surface with holes provided.",
    ErrorCode.WRAPPEROCTREEREGIONINGFAILED : "Wrapper octree regioning generic failure.",
    ErrorCode.WRAPPERPROJECTIONFAILED : "Wrapper projection generic failure.",
    ErrorCode.WRAPPERCONTROL_MATERIALPOINTWITHGIVENNAMEDOESNTEXIST : "Wrapper material point with the given name does not exist.",
    ErrorCode.WRAPPERCONTROL_LIVEMATERIALPOINTDOESNTEXIST : "Wrapper Live material point does not exist.",
    ErrorCode.WRAPPERSIZINGMETHODNOTSUPPORTED : "Sizing method is not supported for wrapper.",
    ErrorCode.WRAPPERSIZEFIELDSNOTDEFINED : "No size field ids provided for wrapping.",
    ErrorCode.WRAPPERIMPROVEFAILED : "Wrapper improve quality failed.",
    ErrorCode.WRAPPERCONTROL_INVALIDCONTACTPREVENTIONCONTROLID : "Contact prevention specified under wrapper control doesn't exist.",
    ErrorCode.WRAPPERCONTROL_INVALIDCONTACTPREVENTIONCONTROLINPUTS : "Contact prevention control specified under wrapper is invalid.",
    ErrorCode.WRAPPERCONTROL_INVALIDGEOMETRYSCOPE : "Geometry scope specified under wrapper control is invalid.",
    ErrorCode.WRAPPERCONTROL_INVALIDLEAKPREVENTIONID : "Leak prevention specified under wrapper control doesn't exist.",
    ErrorCode.WRAPPERCONTROL_INVALIDLEAKPREVENTIONCONTROLINPUTS : "Leak prevention control specified under wrapper is invalid.",
    ErrorCode.WRAPPERCONTROL_INVALIDFEATURERECOVERYCONTROLID : "Feature recovery control specified under wrapper control doesn't exist.",
    ErrorCode.WRAPPERCONTROL_LEAKPREVENTIONMPTCANNOTBELIVE : "Dead material point cannot be same as live.",
    ErrorCode.INVALIDWRAPPERCONTROL : "Invalid wrapper control.",
    ErrorCode.AUTOMESHINVALIDMAXSIZE : "AutoMeshParams has invalid max size specified.",
    ErrorCode.INVALIDPRISMCONTROLS_INCORRECTSCOPEENTITY : "Incorrect scope entity.",
    ErrorCode.INVALIDFIRSTASPECTRATIO : "Incorrect first aspect ratio.",
    ErrorCode.INVALIDLASTASPECTRATIO : "Incorrect last aspect ratio.",
    ErrorCode.INVALIDFIRSTHEIGHT : "Invalid first height.",
    ErrorCode.INVALIDLAYERS : "Invalid number of layers.",
    ErrorCode.INVALIDGROWTHRATE : "Invalid growth rate.",
    ErrorCode.AUTOMESHHEXCOREFAILED : "Failed to create hexcore mesh.",
    ErrorCode.INVALIDVOLUMECONTROLS : "Conflict of volume controls on volumes or invalid volume controls selected.",
    ErrorCode.SURFERINVALIDMINORMAXSIZES : "Invalid min, max size or growth rate provided for surface meshing.",
    ErrorCode.SURFERINVALIDANGLES : "Invalid corner angle or min more than max angle provided for surface meshing.",
    ErrorCode.SMOOTHSIZETRANSITIONNOTSUPPORTEDFORTOPO : "Smooth size transition option is not supported for Topology surface meshing.",
    ErrorCode.SURFACESEARCHFAILED : "Surface search failed.",
    ErrorCode.INVALIDINPUTZONELETS : "Invalid input zonelets for surface search.",
    ErrorCode.SURFACESEARCHPARTWITHMESHNOTFOUND : "Part with mesh not found for surface quality check.",
    ErrorCode.VOLUMESEARCHPARTWITHMESHNOTFOUND : "Part with mesh not found for volume quality check.",
    ErrorCode.VOLUMESEARCHFAILED : "Volume search failed.",
    ErrorCode.INVALIDCELLQUALITYLIMIT : "Invalid cell quality limit.",
    ErrorCode.INVALIDINPUTPART : "Part is invalid.",
    ErrorCode.INVALIDSCOPEENTITYTYPEINPUT : "Invalid input scope entity type.",
    ErrorCode.ENTITIESSHOULDBEADDEDTOZONEUSINGPARTITBELONGS : "Entities should be added to zone using part it belongs.",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORPMDAT : "Provided file extension is not supported. Supported extensions are .pmdat and .pmdat.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTMESHINGMESH : "Provided file extension is not supported. Supported extensions are .msh and .msh.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTCASE : "Provided file extension is not supported. Supported extensions are .cas and .cas.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORKEYWORDFILE : "Provided file extension is not supported. Supported extensions are .k and .key",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORMAPDLCDB : "Provided file extension is not supported. Supported extension is .cdb",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORFLUENTSIZEFIELD : "Provided file extension is not supported. Supported extensions are .sf and .sf.gz",
    ErrorCode.UNSUPPORTEDFILEEXTENSIONFORSIZEFIELD : "Provided file extension is not supported. Supported extensions are .psf and .psf.gz",
    ErrorCode.SUBTRACTZONELETSFAILED : "Failed to subtract cutters from input face zonelets.",
    ErrorCode.QUADRATICTETNOTSUPPORTEDINPARALLEL : "Quadratic tetrahedral meshing is not supported in parallel mode.",
    ErrorCode.QUADRATICTETNOTSUPPORTEDWITHPRISMS : "Quadratic tetrahedral meshing is not supported with prisms.",
    ErrorCode.PARTHASTOPOLOGY : "Part has a topology.",
    ErrorCode.PARTDOESNOTHAVETOPOLOGY : "Part does not have a topology.",
    ErrorCode.ZONESARENOTSUPPORTEDFORCELLZONELETS : "Zones are not supported for cell zonelets."
}

prime_warning_messages = {
    WarningCode.NOWARNING : "Success.",
    WarningCode.UNKNOWN : "Unknown Warning.",
    WarningCode.SURFER_QUADCLEANUP_MULTITHREADINGNOTSUPPORTED : "Warning: Multi threading is skipped for quad cleanup.",
    WarningCode.SURFERLAYEREDQUADFAILED : "Surfer Warning: Layered quad region has triangles.",
    WarningCode.SURFERDEGENERATEFACE : "Surfer Warning: Face has degenerate edge mesh",
    WarningCode.ALIGN_OPERATIONINTERRUPTED : "Align warning: Operation is interrupted by the user. Result can be inaccurate.",
    WarningCode.NOHOLESFOUNDONPLANE : "No closed hole found in given face zonelets at given plane.",
    WarningCode.IGA_NOGEOMZONELETFORSPLINEFITTING : "Geometric face zonelet is not available for spline fitting.",
    WarningCode.NOVOLUMESCOMPUTED : "There are no volumes computed.",
    WarningCode.NOVOLUMESENCLOSINGMATERIALPOINT : "There are no computed volumes enclosing the given material point.",
    WarningCode.EXTERNALOPENFACEZONELETSFOUND : "External open face zonelets found.",
    WarningCode.EXTERNALOPENTOPOFACESFOUND : "External open topofaces found.",
    WarningCode.OVERRIDECURVATURESIZINGPARAMS : "Invalid curvature sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDESOFTSIZINGPARAMS : "Invalid soft sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEHARDSIZINGPARAMS : "Invalid hard sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEPROXIMITYSIZINGPARAMS : "Invalid proximity sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEBOISIZINGPARAMS : "Invalid boi sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDEMESHEDSIZINGPARAMS : "Invalid meshed sizing parameters override by global sizing parameters.",
    WarningCode.OVERRIDESURFACESCOPEENTITY : "Invalid surface scope entity, override by facezonelets.",
    WarningCode.OVERRIDEVOLUMESCOPEENTITY : "Invalid volume scope entity, override by volume.",
    WarningCode.OVERRIDESUGGESTEDNAME : "Given name not available. Overriding it with unique name.",
    WarningCode.WRAPPER_SIZECONTROLNOTDEFINED : "No size controls provided for wrapper. Global sizes will be used.",
    WarningCode.WRAPPER_SIZECONTROLNOTSUPPORTED : "Size control is not supported in wrapper. Skipping it.",
    WarningCode.WRAPPER_SMALLERCONTACTPREVENTIONSIZE : "Contact prevention size is smaller than base size. Size will be adjusted to base size.",
    WarningCode.WRAPPER_SMALLERSIZEATFEAURES : "Size at features is smaller than base size. Size will be adjusted to base size.",
    WarningCode.MATERIALPOINTWITHSAMENAMEEXISTS : "Material point with same name exists. Overriding with unique name.",
    WarningCode.LOCALSURFERNOFACEREGISTERED: "No face registered with the given register id.",
    WarningCode.ENTITIESNOTBELONGTOANYZONE: "Entities not belong to any zone.",
    WarningCode.INVALIDENTITIESNOTADDEDTOZONE: "Entities with invalid id or invalid type are not added to the zone.",
    WarningCode.DUPLICATEINPUT: "Duplicate items in input.",
    WarningCode.MESHHASNONPOSITIVEVOLUMES: "Mesh has non positive volumes.",
    WarningCode.MESHHASNONPOSITIVEAREAS: "Mesh has non positive areas.",
    WarningCode.MESHHASINVALIDSHAPE: "Mesh has invalid shape.",
    WarningCode.MESHHASLEFTHANDEDNESSFACES: "Mesh has left handed faces."

}

class PrimeRuntimeError(Exception):
    '''Runtime error for PyPRIME.'''
    def __init__(self, message, error_code : ErrorCode = None):
        super().__init__()
        self._message = self.__process_message(message)
        self._error_code = error_code

    def __str__(self) -> str:
        return self._message

    def __process_message(self, message : str):
        output_message = message
        if "Invalid Parameter Type: " in message:
            param_names = message[len("Invalid Parameter Type: "):].split(".")
            output_message = "Invalid Parameter Type: " + param_names[0]
            if (len(param_names) > 1):
                for name in param_names[1:]:
                    output_message += "." + re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
        return output_message

    @property
    def message(self):
        return self._message

    @property
    def error_code(self) -> ErrorCode:
        return self._error_code


class PrimeRuntimeWarning(UserWarning):
    '''Runtime warning for PyPRIME.'''
    def __init__(self, message):
        super().__init__()
        self._message = message

    def __str__(self) -> str:
        return self._message

    @property
    def message(self):
        return self._message

def communicator_error_handler(_func=None, *,
                               expected_token='Results',
                               server_error_token='ServerError',
                               info_token = 'info_msg',
                               warning_token='warning_msg',
                               error_token='err_msg'):
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
                    if error_code is not None:
                        if error_code > 0:
                            raise PrimeRuntimeError(prime_error_messages.get(ErrorCode(error_code), f'Unrecogonized error code {error_code}'), ErrorCode(error_code))

                    prime_warnings = []
                    single_warning = result.get('warningCode', None)
                    if single_warning is not None and single_warning > 0:
                        prime_warnings.append(single_warning)

                    multiple_warnings = result.get('warningCodes', None)
                    if multiple_warnings: # Note that this will filter out empty list as well
                        [ prime_warnings.append(w) for w in multiple_warnings ]

                    if prime_warnings:
                        import warnings
                        [ warnings.warn(prime_warning_messages.get(WarningCode(w), f'Unrecogonized warning {w}'), PrimeRuntimeWarning) for w in prime_warnings ]

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
