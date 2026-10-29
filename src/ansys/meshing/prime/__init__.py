'''PyPrimeMesh Client library.'''

# isort: skip_file
from ansys.meshing.prime._version import __version__
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.core.fileio import FileIO
from ansys.meshing.prime.autogen.surfacesearch import SurfaceSearch
from ansys.meshing.prime.autogen.volumesearch import VolumeSearch
from ansys.meshing.prime.core.wrappercontrol import WrapperControl
from ansys.meshing.prime.autogen.multizonecontrol import MultiZoneControl
from ansys.meshing.prime.core.controldata import ControlData
from ansys.meshing.prime.core.wrapper import Wrapper
from ansys.meshing.prime.core.surfaceutilities import SurfaceUtilities
from ansys.meshing.prime.core.sizecontrol import SizeControl
from ansys.meshing.prime.core.volumecontrol import VolumeControl

from ansys.meshing.prime.autogen.surfaceutilitystructs import *
from ansys.meshing.prime.autogen.wrapperstructs import *
from ansys.meshing.prime.autogen.scaffolder import Scaffolder
from ansys.meshing.prime.autogen.automesh import AutoMesh
from ansys.meshing.prime.autogen.surfer import Surfer
from ansys.meshing.prime.autogen.volumesweeper import VolumeSweeper
from ansys.meshing.prime.autogen.boundaryfittednurbs import BoundaryFittedSpline
from ansys.meshing.prime.autogen.quadtospline import QuadToSpline
from ansys.meshing.prime.autogen.hextospline import HexToSpline
from ansys.meshing.prime.autogen.trimmedspline import TrimmedSpline
from ansys.meshing.prime.autogen.sizefield import SizeField
from ansys.meshing.prime.autogen.meshinfo import MeshInfo
from ansys.meshing.prime.autogen.transform import Transform
from ansys.meshing.prime.autogen.connect import Connect
from ansys.meshing.prime.autogen.deletetool import DeleteTool
from ansys.meshing.prime.autogen.collapsetool import CollapseTool
from ansys.meshing.prime.autogen.volumemeshtool import VolumeMeshTool
from ansys.meshing.prime.autogen.topoutilities import TopoUtilities
from ansys.meshing.prime.autogen.morpher import Morpher
from ansys.meshing.prime.autogen.vtcomposer import VTComposer
from ansys.meshing.prime.autogen.topodata import TopoData
from ansys.meshing.prime.autogen.commontypes import *
from ansys.meshing.prime.autogen.commonstructs import *
from ansys.meshing.prime.autogen.modelstructs import *
from ansys.meshing.prime.autogen.fileiostructs import *
from ansys.meshing.prime.autogen.partstructs import *
from ansys.meshing.prime.autogen.surferstructs import *
from ansys.meshing.prime.autogen.scaffolderstructs import *
from ansys.meshing.prime.autogen.automeshstructs import *
from ansys.meshing.prime.autogen.igastructs import *
from ansys.meshing.prime.autogen.trimmedsplinestructs import *
from ansys.meshing.prime.autogen.surfacesearchstructs import *
from ansys.meshing.prime.autogen.volumesearchstructs import *
from ansys.meshing.prime.autogen.materialpointmanagerstructs import *
from ansys.meshing.prime.autogen.materialpointmanager import MaterialPointManager
from ansys.meshing.prime.autogen.controlstructs import *
from ansys.meshing.prime.autogen.sizecontrolstructs import *
from ansys.meshing.prime.autogen.sizefieldstructs import *
from ansys.meshing.prime.autogen.meshinfostructs import *
from ansys.meshing.prime.autogen.prismcontrolstructs import *
from ansys.meshing.prime.autogen.prismcontrol import PrismControl
from ansys.meshing.prime.autogen.thinvolumecontrol import ThinVolumeControl
from ansys.meshing.prime.autogen.connectstructs import *
from ansys.meshing.prime.autogen.surfaceutilitystructs import *
from ansys.meshing.prime.autogen.transformstructs import *
from ansys.meshing.prime.autogen.deletetoolstructs import *
from ansys.meshing.prime.autogen.splittoolstructs import *
from ansys.meshing.prime.autogen.collapsetoolstructs import *
from ansys.meshing.prime.autogen.volumecontrolstructs import *
from ansys.meshing.prime.autogen.periodiccontrol import PeriodicControl
from ansys.meshing.prime.autogen.periodiccontrolstructs import *
from ansys.meshing.prime.autogen.featureextractionstructs import *
from ansys.meshing.prime.autogen.featureextraction import *
from ansys.meshing.prime.autogen.thinvolumecontrolstructs import *
from ansys.meshing.prime.autogen.volumemeshtoolstructs import *
from ansys.meshing.prime.autogen.volumesweeperstructs import *
from ansys.meshing.prime.autogen.topodatastructs import *
from ansys.meshing.prime.autogen.topoutilitystructs import *
from ansys.meshing.prime.autogen.morpherstructs import *
from ansys.meshing.prime.autogen.morpherbcsstructs import *
from ansys.meshing.prime.autogen.autoquadmesher import *
from ansys.meshing.prime.autogen.autoquadmesherstructs import *
from ansys.meshing.prime.autogen.toposearchstructs import *
from ansys.meshing.prime.autogen.vtcomposerstructs import *
from ansys.meshing.prime.autogen.shellblcontrolstructs import *
from ansys.meshing.prime.autogen.shellblcontrol import *
from ansys.meshing.prime.autogen.modelquery import *

from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError, PrimeRuntimeWarning
from ansys.meshing.prime.internals.client import Client
from ansys.meshing.prime.internals.launcher import *
from ansys.meshing.prime.internals.config import (
    is_optimizing_numpy_arrays,
    enable_optimizing_numpy_arrays,
    disable_optimizing_numpy_arrays,
    numpy_array_optimization_enabled,
    numpy_array_optimization_disabled,
    enable_log_output,
)

import ansys.meshing.prime.examples as examples
import ansys.meshing.prime.lucid as lucid

import os

if os.getenv('PRIME_ENABLE_STANDBY_IMPORT'):
    # Import all symbols from Python files in the standby folder
    import importlib.util
    import sys
    from pathlib import Path

    __standby_folder = Path(__file__).parent.parent / 'standby'
    __core_folder = Path(__file__).parent / 'core'
    if __standby_folder.exists() and __standby_folder.is_dir():
        __meshing_package = sys.modules.get('ansys.meshing')
        if __meshing_package is not None:
            __meshing_paths = list(__meshing_package.__path__)
            __source_meshing_path = str(__standby_folder.parent)
            if __source_meshing_path not in __meshing_paths:
                __meshing_paths.insert(0, __source_meshing_path)
                __meshing_package.__path__ = __meshing_paths

        # Sort files to prioritize commonstructs.py and commontypes.py
        __py_files = list(__standby_folder.glob('*.py'))
        __priority_files = ['commontypes.py', 'commonstructs.py']
        __py_files.sort(key=lambda f: (
            __priority_files.index(f.name) if f.name in __priority_files else len(__priority_files),
            f.name
        ))
        # Move all *struct.py and *structs.py files to the end
        __struct_files = [f for f in __py_files if f.name.endswith('struct.py') or f.name.endswith('structs.py')]
        __non_struct_files = [f for f in __py_files if not (f.name.endswith('struct.py') or f.name.endswith('structs.py'))]
        __py_files = __non_struct_files + __struct_files
        for __py_file in __py_files:
            if __py_file.name.startswith('_'):
                continue
            
            __module_name = f"ansys.meshing.prime.{__py_file.stem}"
            __spec = importlib.util.spec_from_file_location(__module_name, __py_file)
            if __spec and __spec.loader:
                __module = importlib.util.module_from_spec(__spec)
                __spec.loader.exec_module(__module)
                # Import all public symbols from the module
                for __attr_name in dir(__module):
                    if not __attr_name.startswith('_'):
                        globals()[__attr_name] = getattr(__module, __attr_name)

__LOCAL_CLIENT = None


def __get_local_client() -> Client:
    global __LOCAL_CLIENT
    if __LOCAL_CLIENT is None:
        __LOCAL_CLIENT = Client(local=True)
    return __LOCAL_CLIENT


def local_model() -> Model:
    '''Get local model

    .. note:: USE IN DEVELOPMENT ONLY

    This imports the Ansys Prime Server environment into the Python process. It will
    error unless proper environment is set up to support Ansys Prime Server.

    Returns
    -------
    Model
            The local model
    '''
    model = __get_local_client().model
    model._sync_up_model()  # For running Python recipe directly on server, local model needs to be synced up with gRPC model
    return model


def __filter_internal_symbols(symbol):
    __internals = [
        'annotations',
        'autogen',
        'core',
        'enum',
        'internals',
        'params',
        'utils',
        'Any',
        'List',
        'Dict',
        'CommunicationManager',
        'CoreObject',
    ]
    return not symbol in __internals


__symbols = (s for s in dir() if not s.startswith('_'))
__symbols = filter(__filter_internal_symbols, __symbols)
__all__ = list(__symbols)
# print(__all__)
