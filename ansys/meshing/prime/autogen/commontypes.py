""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *


class SizeFieldType(enum.IntEnum):
    """The type of sizing field to be used to fetch element size at given location.
    """
    VOLUMETRIC = 1
    """Uses precomputed variable size in volumetric space defined by size field."""
    CONSTANT = 3
    """Uses constant size at all locations of sizing field."""

class SolverType(enum.IntEnum):
    """Type of solver.
    """
    FLUENT = 1
    """Solver type is Fluent. Creates a group of face quality measures mostly used in Fluent."""
    MAPDL = 2
    """Solver type is MAPDL. Creates a group of face quality measures mostly used in MAPDL."""

class FaceQualityMeasure(enum.IntEnum):
    """The type of face quality measures to check face quality metrics.
    """
    SKEWNESS = 0
    """The Skewness metric ranges between 0 and 1. A value of 0 indicates an equilateral cell (best) and a value of 1 indicates a completely degenerate cell (worst)."""
    ASPECTRATIO = 5
    """The Aspect Ratio metric is greater than 1. A value of 1 indicates an equilateral cell (best) and a value of 20(e.g) indicates a stretched cell (worst)."""
    ELEMENTQUALITY = 50
    """The Element Quality metric ranges between 0 and 1. A value of 1 indicates a perfect cube or square(best) while a value of 0 indicates that the element has a zero or negative volume(worst)."""
