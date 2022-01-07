from functools import wraps

from ansys.meshing.prime.autogen.primeconfig import ErrorCode, WarningCode

prime_error_messages = {
    ErrorCode.NOERROR : "Success",
    ErrorCode.UNKNOWN : "Unknown Error",
    ErrorCode.SIGSEGV : "Segmentation Violation",
    ErrorCode.SURFERFAILED : "Surfer Failed",
    ErrorCode.SURFERWITHAUTOSIZINGFAILED : "Surfer with auto sizing Failed",
    ErrorCode.SURFERAUTOSIZEQUADUNSUPPORTED : "Program controlled surface meshing does not support quadrilateral mesh.",
    ErrorCode.SURFERAUTOSIZEMUSTBEVOLUMETRIC : "Surface meshing supports only volumetric sizefield",
    ErrorCode.FACEZONELETSFEATURESNOTUPTODATE : "Association between edge and face zonelets is broken. Try extract features by edges to correct.",
    ErrorCode.SURFERLAYEREDQUADFAILED : "Layered quad meshing failed",
    ErrorCode.SURFERINVALIDINPUT : "Surfer invalid input",
    ErrorCode.SURFERNONMANIFOLDEDGE : "Surfer non manifold edge",
    ErrorCode.SURFERQUADFAILED : "Surfer quad meshing failed",
    ErrorCode.SCAFFOLDERBADINPUTEMPTYTOPO : "Empty Topology provided to scaffolder",
    ErrorCode.SCAFFOLDERBADINPUTNOFREEFACES : "No free faces found in current topology",
    ErrorCode.SCAFFOLDERBADINPUTPARAMS : "Wrong scaffolder params setup",
    ErrorCode.OUTOFMEMORY : "Out of memory",
    ErrorCode.INTERRUPTED : "Prime operation interrupted",
    ErrorCode.AUTOMESHFAILED : "Auto-Mesh Failed",
    ErrorCode.INVALIDPRISMCONTROLS : "Conflict of prism settings on zonelets or invlaid prism controls selected.",
    ErrorCode.ALREADYVOLUMEMESHED : "Already volume meshed",
    ErrorCode.VOLUMESNOTUPTODATE : "Volumes are not up to date. Update volumes and try again",
    ErrorCode.QUATRICMESHSUPPORTEDONLYFORTETS : "Volumes are not up to date. Update volumes and try again",
    ErrorCode.NOACTIVESFFOUND : "Active size fields are not available.",
    ErrorCode.AITOVERLAPALONGMULTIFOUND : "Overlapping faces along mulit-connection found",
    ErrorCode.TRIANGULATIONFAILED : "Planar triangulation failed",
    ErrorCode.TOPOFACESREMESHFAILED : "Failed to Remesh some topo faces",
    ErrorCode.PARTNOTFOUND : "Mesh Part not found",
    ErrorCode.TOPODATANOTFOUND : "Topo Data not found",
    ErrorCode.SIZEFIELDNOTFOUND : "Size Field not found",
    ErrorCode.CADGEOMETRYNOTFOUND : "CAD Geometry not found",
    ErrorCode.VOLUMENOTFOUND : "Volume not found",
    ErrorCode.NOTSUPPORTEDFORTOPOLOGYPART : "Not supported for part with topology data",
    ErrorCode.NOTSUPPORTEDFORHIGHERORDERMESHPART : "Not supported for part with higher order mesh",
    ErrorCode.SPHEREATINVALIDNORMALNODESFAILED : "Sphere creation at invalid normal nodes failed.",
    ErrorCode.PROJECTONCADGEOMETRYFAILED : "Projection on CAD Geometry failed.",
    ErrorCode.ZONESARENOTOFSAMETYPE : "Zones selected are not of same type",
    ErrorCode.TOPOEDGESREMESHFAILED : "Failed tp Remesh topo edges",
    ErrorCode.DUPLICATENODESFOUND : "Duplicate nodes found",
    ErrorCode.DUPLICATEFACESFOUND : "Duplicate faces found",
    ErrorCode.EDGEINTERSECTINGFACEFOUND : "Edge intersects face",
    ErrorCode.SEPARATIONRESULTSFAILED : "Failed to separate faces. Kindly provide valid inputs.",
    ErrorCode.SIZEFIELDCOMPUTATIONFAILED : "Size Field computation failed",
    ErrorCode.REFRESHSIZEFIELDSFAILED : "Refresh Size Fields failed",
    ErrorCode.INVALIDSIZECONTROLS : "Invalid size controls selected to compute size field",
    ErrorCode.TETIMPROVEFAILED : "Tet improvement failed",
    ErrorCode.AUTONODEMOVEFAILED : "Tet improvement using auto node movement failed",
    ErrorCode.COMPUTEBODIESFAILED : "Compute bodies failed",
    ErrorCode.READMESHFAILED : "Read Mesh failed",
    ErrorCode.WRITEMESHFAILED : "Write Mesh failed",
    ErrorCode.QUADRATICMESH_WRITEMESHFAILED : "Saving quadratic mesh into .msh format is not supported. Try saving it as .cdb, .m2g or .k File",
    ErrorCode.CADIMPORTFAILED : "CAD Import failed",
    ErrorCode.READSIZEFIELDFAILED : "Read Size Field failed",
    ErrorCode.WRITESIZEFIELDFAILED : "Write Size Field failed",
    ErrorCode.READPMDBFAILED : "Read PMDB failed",
    ErrorCode.READCDBFAILED : "Read CDB failed",
    ErrorCode.WRITECDBFAILED : "Write CDB failed",
    ErrorCode.READKEYWORDFILEFAILED : "Read K file failed",
    ErrorCode.WRITEKEYWORDFILEFAILED : "Write K file failed",
    ErrorCode.INCLUDEKFILENOTFOUND : "Referenced K file not found",
    ErrorCode.READSIZECONTROLFAILED : "Read Size Control failed",
    ErrorCode.WRITESIZECONTROLFAILED : "Write Size Control failed",
    ErrorCode.PATHNOTFOUND : "File path not found",
    ErrorCode.UNDOFAILED : "Undo failed",
    ErrorCode.REDOFAILED : "Redo failed",
    ErrorCode.GETSTATISTICSFAILED : "Get statistics failed",
    ErrorCode.GETELEMENTCOUNTFAILED : "Get element count failed",
    ErrorCode.EXTRACTFEATURESFAILED : "Feature extraction by angle failed",
    ErrorCode.EXTRACTFEATURESBYEDGESFAILED : "Feature extraction by edge tracing failed",
    ErrorCode.CREATEEDGEZONELETFAILED : "Create edge zonelets by node path failed",
    ErrorCode.NOSIDEFRONTFACES : "Empty side and front faces input",
    ErrorCode.NOTALLSIDEFRONTFACES : "Not all side/front faces of volume/part input",
    ErrorCode.NOMESHONSIDEFACES : "No mesh on side topofaces",
    ErrorCode.NOMESHONFRONTFACES : "No mesh on front topofaces",
    ErrorCode.TETINITFAILED : "MidSurf Tet Init failed",
    ErrorCode.TETCUTFAILED : "MidSurf Tet Cutting failed",
    ErrorCode.MIDSURFACEFAILED : "MidSurf extration failed",
    ErrorCode.IMPRINTFAILED : "Midsurf Imprint failed",
    ErrorCode.INVALIDSIDETHICKNESS : "Midsurf invalid side thickness",
    ErrorCode.NOTMIDSURFTOPOFACE : "Not a midsurf topoface",
    ErrorCode.NOTUNIFORMTHICKNESSMIDSURFTOPOFACE : "No uniform thickness associated with topoface",
    ErrorCode.OPENSIDEFACELOOPS : "Detected side topofaces do not form closed loop",
    ErrorCode.SINGLESETFRONTFACES : "Detected only one set of front topofaces",
    ErrorCode.VOLUMEMESH_MIDNODESNOTSUPPORTED : "Improve volume mesh error: meshes with mid nodes are not supported",
    ErrorCode.VOLUMEMESHNOTFOUND : "Volume mesh not found",
    ErrorCode.NOTSUPPORTEDFORNONTRIFACEZONE : "Only triangular faces are supported.",
    ErrorCode.NOTSUPPORTEDFORNONQUADFACEZONE : "Only quadrilateral faces zonelets are supported.",
    ErrorCode.PARTNOTMESHED : "Part has unmeshed topofaces",
    ErrorCode.TRANSFORMATIONFAILED : "Failed to transform",
    ErrorCode.SCALINGFAILED : "Failed to scale",
    ErrorCode.ALIGNMENTFAILED : "Failed to align",
    ErrorCode.DELETEMESHFACESFAILED : "Failed to delete face element(s).",
    ErrorCode.DELETEFRINGESANDOVERLAPSFAILED : "Failed to delete fringes and overlaps.",
    ErrorCode.DELETEMESHFACES_TOPOLOGYNOTSUPPORTED : "Deletion of face element(s) is not supported for mesh with topology.",
    ErrorCode.DELETEMESHFACES_CELLFOUND : "Cannot delete face element(s) connected to volume mesh.",
    ErrorCode.MATERIALPOINTWITHSAMENAMEEXISTS : "Material point with %s name already exist.",
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
    ErrorCode.IGA_UNIFORMTRIMMEDNURBSFAILED : "Failed to create uniform trimmed solid spline."
}

prime_warning_messages = {
    WarningCode.NOWARNING : "Success",
    WarningCode.UNKNOWN : "Unknown Warning",
    WarningCode.SURFER_AUTOSIZING_MULTITHREADINGNOTSUPPORTED : "Warning: Multi threading is skipped for surfer with auto sizing.",
    WarningCode.SURFER_QUADCLEANUP_MULTITHREADINGNOTSUPPORTED : "Warning: Multi threading is skipped for quad cleanup.",
    WarningCode.SURFERLAYEREDQUADFAILED : "Surfer Warning: Layered quad region has triangles",
    WarningCode.SURFERDEGENERATEFACE : "Surfer Warning: Face has degenerate edge mesh",
    WarningCode.ALIGN_OPERATIONINTERRUPTED : "Align warning: Operation is interrupted by the user. Result can be inaccurate.",
    WarningCode.IGA_NOGEOMZONELETFORSPLINEFITTING : "Geometric face zonelet is not available for spline fitting.",
}

'''

'''
class PrimeRuntimeError(RuntimeError):
    def __init__(self, message):
        self._message = message

    def __str__(self) -> str:
        return self._message

    @property
    def message(self):
        return self._message


class PrimeRuntimeWarning(RuntimeWarning):
    def __init__(self, message):
        RuntimeWarning()
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
                    if error_code:
                        if error_code > 0 and error_code in prime_error_messages:
                            raise PrimeRuntimeError(prime_error_messages.get(error_code, f'Unrecogonized error code {error_code}'))

                    prime_warnings = []
                    single_warning = result.get('warningCode', None)
                    if single_warning is not None and single_warning > 0:
                        prime_warnings.append(single_warning)

                    multiple_warnings = result.get('warningCodes', None)
                    if multiple_warnings: # Note that this will filter out empty list as well
                        [ prime_warnings.append(w) for w in multiple_warnings ]

                    if prime_warnings:
                        import warnings
                        [ warnings.warn(prime_warning_messages.get(w, f'Unrecogonized warning {w}'), PrimeRuntimeWarning) for w in prime_warnings ]

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
