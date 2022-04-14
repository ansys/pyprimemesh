import subprocess
import os
import sys
import logging
import json
# import psutil

def start_server(prime_installdir: str=None, ip: str="localhost", port: int=50052):
    proc = None
    try:
        if "PRIME_INSTALLDIR" not in os.environ.keys() and prime_installdir is None:
            raise RuntimeError(
                "Specify where your Prime install is present")
        if prime_installdir is None:
            prime_installdir = os.environ["PRIME_INSTALLDIR"]
        if (sys.platform == "linux") :
            run_script = os.path.join(prime_installdir, 'runPrimeApp.sh')
        else :
            run_script = os.path.join(prime_installdir, 'RunPrime.bat')
        server_path = os.path.join(prime_installdir, 'scripts', 'PrimeGRPC.py')
        proc = subprocess.Popen([run_script, server_path, f"--ip={ip}", f"--port={port}"])
    except Exception as err:
        proc.terminate()
        print(str(err))

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

def terminate_process(process):
    import sys
    import signal
    if sys.platform.startswith('win32'):
        # process.send_signal(signal.CTRL_C_EVENT)
        process.send_signal(signal.CTRL_BREAK_EVENT)
    if process.stdin is not None:
        process.stdin.close()
    if process.stdout is not None:
        process.stdout.close()
    if process.stderr is not None:
        process.stderr.close()
    process.terminate()
    process.wait()

def print_logs_before_command(logger : logging.Logger, command : str, args):
    logger.info("Executing " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Command: " + command)
        logger.debug("Args:")
        for key in args:
            logger.debug("    " + key + ":")
            val = args[key]
            printable_str = ""
            if (hasattr(val, '__str__')):
                printable_str = val.__str__()
            elif (type(val) == 'str'):
                printable_str = val
            else:
                printable_str = str(val)
            for line in printable_str.splitlines():
                logger.debug("        " + line)
        logger.debug("")

def print_logs_after_command(logger : logging.Logger, command : str, ret):
    logger.info("Finished " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Return: ")
        printable_str = ""
        if (hasattr(ret, '__str__')):
            printable_str = ret.__str__()
        elif (type(ret) == 'str'):
            printable_str = ret
        else:
            printable_str = str(ret)
        for line in printable_str.splitlines():
            logger.debug("        " + line)
        logger.debug("")

def get_cad_import_commands(params : str) -> str:
    cad_import_params = json.loads(params)
    print_logs = False
    commands = """
import os
import glob
from ansys.FM import FM
from ansys.FM import InitializeForPyPrime
from ansys.FM.Restore import Restore
from ansys.FM.CADReaders import CADReaders
from ansys.FM.Refacet import Refacet
from ansys.FM.ConvertToPrimeMesh import ConvertToPrimeMesh
from ansys.meshing.prime import ErrorCode

return_value = {"errorCode" : ErrorCode.NOERROR }
cad_import_success = False
    """
    commands += "\ncad_file_name = r\"%s\"" % (cad_import_params['filename'])
    params = cad_import_params['params']
    if (params['cadReaderRoute'] == 0): #CadReaderRoute.PROGRAMCONTROLLED
        cad_reader_route = ""
    elif (params['cadReaderRoute'] == 1): #CadReaderRoute.NATIVE
        cad_reader_route = "FM"
    elif (params['cadReaderRoute'] == 2): #CadReaderRoute.WORKBENCH
        cad_reader_route = "WorkBench"
    elif (params['cadReaderRoute'] == 3): #CadReaderRoute.SPACECLAIM
        cad_reader_route = "SpaceClaim"
    commands += "\ncad_reader_route = \"%s\"" % (cad_reader_route)

    if (params['partCreationType'] == 0): #PartCreationType.MODEL
        part_creation_type = "Model"
    elif (params['partCreationType'] == 1): #PartCreationType.ASSEMBLY
        part_creation_type = "Assembly"
    elif (params['partCreationType'] == 2): #PartCreationType.PART
        part_creation_type = "Part"
    elif (params['partCreationType'] == 3): #PartCreationType.BODY
        part_creation_type = "Body"
    elif (params['partCreationType'] == 4): #PartCreationType.GROUP
        part_creation_type = "Group"
    commands += "\npart_creation_type = \"%s\"" % (part_creation_type)

    commands += "\ngeometry_transfer = %s"\
        % ("True" if params['geometryTransfer'] else "False")
    commands += "\nstitch_tolerance = %f" % (params['stitchTolerance'])

    if params['lengthUnit'] == 0: #LengthUnit.M:
        cad_length_unit = "m"
        conversion_factor = 0.001
    elif params['lengthUnit'] == 1: #LengthUnit.CM:
        cad_length_unit = "cm"
        conversion_factor = 0.1
    elif params['lengthUnit'] == 2: #LengthUnit.MM:
        cad_length_unit = "mm"
        conversion_factor = 1.0
    elif params['lengthUnit'] == 3: #LengthUnit.UM:
        cad_length_unit = "um"
        conversion_factor = 1000
    elif params['lengthUnit'] == 4: #LengthUnit.NM:
        cad_length_unit = "nm"
        conversion_factor = 1000000.0
    elif params['lengthUnit'] == 5: #LengthUnit.FT:
        cad_length_unit = "ft"
        conversion_factor = 0.0033
    elif params['lengthUnit'] == 6: #LengthUnit.IN:
        cad_length_unit = "in"
        conversion_factor = 0.039
    else:
        cad_length_unit = "mm"
        conversion_factor = 1.0
    commands += "\ncad_length_unit = \"%s\"" % (cad_length_unit)

    commands += "\nrefacet = %s" % ("True" if params['refacet'] else "False")
    if params['refacet']:
        refaceting_params = params['cadRefacetingParams']
        if (refaceting_params['cadFaceter'] == 0): #CadFaceter.ACIS:
            commands += "\ncad_faceter = FM.ModelKernel.Types.FT_ACIS"
        elif (refaceting_params['cadFaceter'] == 1): #CadFaceter.PARASOLID:
            commands += "\ncad_faceter = FM.ModelKernel.Types.FT_Parasolid"

        if refaceting_params['facetingResolution'] == 0: #CadRefacetingResolution.COARSE:
            surface_tolerance = 2.0 * conversion_factor
            normal_tolerance = 16.0
        elif refaceting_params['facetingResolution'] == 1: #CadRefacetingResolution.MEDIUM:
            surface_tolerance = 0.75 * conversion_factor
            normal_tolerance = 8.0
        elif refaceting_params['facetingResolution'] == 2: #CadRefacetingResolution.FINE:
            surface_tolerance = 0.5 * conversion_factor
            normal_tolerance = 4.0
        elif refaceting_params['facetingResolution'] == 3: #CadRefacetingResolution.CUSTOM:
            surface_tolerance = refaceting_params['customSurfaceDeviationTolerance']\
                * conversion_factor
            normal_tolerance = refaceting_params['customNormalAngleTolerance']

        commands += "\nsurface_tolerance = (%f,'%s')" % (surface_tolerance, cad_length_unit)
        commands += "\nnormal_tolerance = (%f,'deg')" % (normal_tolerance)
        if refaceting_params['maxEdgeSizeLimit'] == 0:
            #CadRefacetingMaxEdgeSizeLimit.NONE
            commands += "\nmax_edge_length = None"
            commands += "\nmax_edge_length_factor = None"
        elif refaceting_params['maxEdgeSizeLimit'] == 1:
            #CadRefacetingMaxEdgeSizeLimit.ABSOLUTE
            commands += "\nmax_edge_length = (%f, '%s')" \
                    % (refaceting_params['maxEdgeSize'] * conversion_factor, cad_length_unit)
            commands += "\nmax_edge_length_factor = None"
        elif refaceting_params['maxEdgeSizeLimit'] == 2:
            #CadRefacetingMaxEdgeSizeLimit.RELATIVE
            commands += "\nmax_edge_length = None"
            commands += "\nmax_edge_length_factor = %f"  % (refaceting_params['maxEdgeSize'])
        else:
            commands += "\nmax_edge_length = None"
            commands += "\nmax_edge_length_factor = None"

    commands += "\nlogging_enabled = %s" % ("True" if print_logs else "False")
    commands += """
try:
    FM.Model.Get().Clear()
    try:
        op = None
        extension = os.path.splitext(cad_file_name)[1].lower()
        if extension in (".fmd", ".fmdb"):
            op = Restore()
        else:
            op = CADReaders()
            op.ConfigureRoute(route=cad_reader_route)
            op.ConfigureNamedSelectionFiltering(skipNamedSelectionRegEx="^(Color|Layer|Material).*")
            op.ConfigureWorkbenchPreference('PartDimension', 'Solid|Sheet|Wire')
            op.ConfigureWorkbenchPreference('SecondaryImportPref', 'Solid_Sheet_Wire')
            op.ConfigureWorkbenchPreference("NamedSelectionProcessing", True)
            op.ConfigureWorkbenchPreference("NamedSelectionPrefixes", "")
            #Stitch tolerances for WB routes
            if cad_reader_route.lower() in ("wb", "workbench"):
                op.ConfigureWorkbenchPreference("Stitch", "UserTolerance")
                op.ConfigureWorkbenchPreference("StitchTolerance", stitch_tolerance)

        if op is not None:
            scope = op(cad_file_name)
            if logging_enabled:
                print(str(FM.Model.Get()))
    except Exception as msg:
        if logging_enabled:
            print('Import to FM Failed!!!' + str(msg))
        return_value = {"errorCode" : ErrorCode.CADIMPORTFAILED }
    else:
        try:
            #length unit conversion factor
            unitsConverter = FM.Core.UnitsConverter()
            unitsConverter.Initialize()
            modelLengthUnit = FM.Model.Get().GetLengthUnit()
            conversionData = unitsConverter.GetConversionData(modelLengthUnit, cad_length_unit)\
                    if len(modelLengthUnit) else (1.0, 0.0)
    """
    if params['refacet']:
        commands += """
            #refacet
            if refacet and extension not in (".stl", ".tgf", ".cgr"):
                try:
                    op = Refacet()
                    op.ConfigureFaceter(cad_faceter)
                    op.ConfigureFacetOptions(surfaceTolerance=surface_tolerance,\
                        normalTolerance=normal_tolerance, maxEdgeLength=max_edge_length,\
                        maxEdgeLengthFactor=max_edge_length_factor, useMultithreadedFaceter=True,\
                        mergeDuplicateNodes=True, nodeMergeTolerance=0.0)
                    op()
                except Exception as msg:
                    if logging_enabled:
                        print('Error while Refaceting!!!' + str(msg))
                    return_value = {"errorCode" : ErrorCode.CADIMPORTFAILED }
        """
    commands += """
            #convert FM model to PrimeMesh parts
            op = ConvertToPrimeMesh()
            op.ConfigureObjectCreation(objectGranularity=part_creation_type)
            op.ConfigureRegionCreation(separateRegionsPerBody=True)
            op.ConfigureZoneCreation(faceZoneSeparationFlags=FM.ModelKernel.Types.ZST_ByEntity,
                edgeZoneSeparationFlags=FM.ModelKernel.Types.ZST_ByEntity)
            op.ConfigureNaming(deriveNamesFromAttributes=False)
            op.ConfigureScaling(scaleFactor=conversionData[0])
            if extension not in (".stl", ".tgf", ".cgr"):
                op.ConfigureTopologyCreation(createTopology=True)
                op.ConfigureGeometryCreation(createGeometry=geometry_transfer)
            part_ids = op()
            if logging_enabled:
                print('created part(s) with id(s) ' + str(part_ids))
            cad_import_success = isinstance(part_ids, tuple) and len(part_ids) > 0
        except Exception as msg:
            if logging_enabled:
                print('Convertion of FM Model To PrimeMesh Failed!!!' + str(msg))
            return_value = {"errorCode" : ErrorCode.CADIMPORTFAILED }
        else:
            FM.Model.Get().Clear()
except Exception as msg:
    if logging_enabled:
        print('CAD Import Unsuccessful!!!' + str(msg))
    return_value = {"errorCode" : ErrorCode.CADIMPORTFAILED }
else:
    if not cad_import_success:
        if logging_enabled:
            print("CAD Import Failed!")
        return_value = {"errorCode" : ErrorCode.CADIMPORTFAILED }
    """
    return commands
