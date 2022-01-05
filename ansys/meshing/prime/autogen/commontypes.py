""" Auto-generated file. DO NOT MODIFY """
import enum
import logging
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class SolverType(enum.IntEnum):
    """ 
     Type of solver.

    """ 
    FLUENT = 1
    """ Solver type is Fluent. Creates a group of face quality measures mostly used in Fluent.""" 
    MAPDL = 2
    """ Solver type is MAPDL. Creates a group of face quality measures mostly used in MAPDL.""" 
    

class FaceQualityMeasure(enum.IntEnum):
    """ 
    """ 
    SKEWNESS = 0
    """ The Skewness metric ranges between 0 and 1. A value of 0 indicates an equilateral cell (best) and a value of 1 indicates a completely degenerate cell (worst)""" 
    ASPECTRATIO = 5
    """ The Aspect Ratio metric is greater than 1. A value of 1 indicates an equilateral cell (best) and a value of 20(e.g) indicates a stretched cell (worst)""" 
    ELEMENTQUALITY = 50
    """ The Element Quality metric ranges between 0 and 1. A value of 1 indicates a perfect cube or square(best) while a value of 0 indicates that the element has a zero or negative volume(worst)""" 
    



