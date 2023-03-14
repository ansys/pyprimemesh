'''PyPrimeMesh Client library
'''
# isort: skip_file
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.core.fileio import FileIO
from ansys.meshing.prime.core.surfer import Surfer
from ansys.meshing.prime.autogen.surfacesearch import SurfaceSearch
from ansys.meshing.prime.autogen.volumesearch import VolumeSearch
from ansys.meshing.prime.core.wrappercontrol import WrapperControl
from ansys.meshing.prime.core.controldata import ControlData
from ansys.meshing.prime.core.wrapper import Wrapper
from ansys.meshing.prime.core.surfaceutilities import SurfaceUtilities
from ansys.meshing.prime.core.sizecontrol import SizeControl
from ansys.meshing.prime.core.volumecontrol import VolumeControl

from ansys.meshing.prime.autogen.surfaceutilitystructs import *
from ansys.meshing.prime.autogen.wrapperstructs import *
from ansys.meshing.prime.autogen.scaffolder import Scaffolder
from ansys.meshing.prime.autogen.automesh import AutoMesh
from ansys.meshing.prime.autogen.boundaryfittednurbs import BoundaryFittedSpline
from ansys.meshing.prime.autogen.sizefield import SizeField
from ansys.meshing.prime.autogen.meshinfo import MeshInfo
from ansys.meshing.prime.autogen.transform import Transform
from ansys.meshing.prime.autogen.connect import Connect
from ansys.meshing.prime.autogen.deletetool import DeleteTool
from ansys.meshing.prime.autogen.collapsetool import CollapseTool
from ansys.meshing.prime.autogen.volumemeshtool import VolumeMeshTool
from ansys.meshing.prime.autogen.topoutilities import TopoUtilities
from ansys.meshing.prime.autogen.commontypes import *
from ansys.meshing.prime.autogen.commonstructs import *
from ansys.meshing.prime.autogen.modelstructs import *
from ansys.meshing.prime.autogen.fileiostructs import *
from ansys.meshing.prime.autogen.partstructs import *
from ansys.meshing.prime.autogen.surferstructs import *
from ansys.meshing.prime.autogen.scaffolderstructs import *
from ansys.meshing.prime.autogen.automeshstructs import *
from ansys.meshing.prime.autogen.igastructs import *
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
from ansys.meshing.prime.autogen.connectstructs import *
from ansys.meshing.prime.autogen.surfaceutilitystructs import *
from ansys.meshing.prime.autogen.transformstructs import *
from ansys.meshing.prime.autogen.deletetoolstructs import *
from ansys.meshing.prime.autogen.splittoolstructs import *
from ansys.meshing.prime.autogen.collapsetoolstructs import *
from ansys.meshing.prime.autogen.volumecontrolstructs import *
from ansys.meshing.prime.autogen.featureextractionstructs import *
from ansys.meshing.prime.autogen.featureextraction import *
from ansys.meshing.prime.autogen.volumemeshtoolstructs import *
from ansys.meshing.prime.autogen.topoutilitystructs import *

from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError, PrimeRuntimeWarning
from ansys.meshing.prime.internals.client import Client
from ansys.meshing.prime.internals.launcher import *
from ansys.meshing.prime.internals.config import (
    is_optimizing_numpy_arrays,
    enable_optimizing_numpy_arrays,
    disable_optimizing_numpy_arrays,
    numpy_array_optimization_enabled,
    numpy_array_optimization_disabled,
)

import ansys.meshing.prime.examples as examples
import ansys.meshing.prime.lucid as lucid

# Version
# ------------------------------------------------------------------------------

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__.replace(".", "-"))

# ------------------------------------------------------------------------------

__LOCAL_CLIENT = None


def __get_local_client() -> Client:
    global __LOCAL_CLIENT
    if __LOCAL_CLIENT is None:
        __LOCAL_CLIENT = Client(local=True)
    return __LOCAL_CLIENT


def local_model() -> Model:
    '''Get Local model

    NOTE: USE IN DEVELOPMENT ONLY

    This imports the Ansys Prime Server environment into the python process. It will
    error unless proper environment is setup to support Ansys Prime Server.
    '''
    model = __get_local_client().model
    model._sync_up_model()  # For running python recipe directly on server, local model needs to be sync up with grpc model
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
