from ansys.meshing.prime._version import __version__
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.core.fileio import FileIO
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.core.surfacesearch import SurfaceQualitySummary
from ansys.meshing.prime.autogen.fileiostructs import *
from ansys.meshing.prime.autogen.igastructs import *
from ansys.meshing.prime.autogen.boundaryfittednurbs import BoundaryFittedSpline
from ansys.meshing.prime.autogen.commontypes import *
from ansys.meshing.prime.autogen.partstructs import *
from ansys.meshing.prime.autogen.surfacesearchstructs import *
from ansys.meshing.prime.internals.client import Client
from ansys.meshing.prime.internals.launcher import *

__LOCAL_CLIENT = None

def __get_local_client() -> Client:
    global __LOCAL_CLIENT
    if __LOCAL_CLIENT is None:
        __LOCAL_CLIENT = Client(local=True)
    return __LOCAL_CLIENT
        
def local_model() -> Model:
    model = __get_local_client().model
    model._sync_up_model() # For running python recipe directly on server, local model needs to be sync up with grpc model 
    return model

