""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class TopoSearchField(enum.IntEnum):
    """Toposearch diagnostic field.
    """
    OVERLAPPINGTOPOFACES = 0
    """Diagnoses overlapping or partially overlapping topofaces.
    This is a beta parameter. The behavior and name may change in the future."""
    INTERSECTINGTOPOFACES = 1
    """Diagnoses intersecting topofaces.
    This is a beta parameter. The behavior and name may change in the future."""
    SELFINTERSECTINGTOPOFACES = 2
    """Diagnoses topofaces with self intersecting bounding edges.
    This is a beta parameter. The behavior and name may change in the future."""
    BROKENLOOPTOPOFACES = 3
    """Diagnoses topofaces with open or broken bounding edge loops.
    This is a beta parameter. The behavior and name may change in the future."""
    NOBOUNDARYLOOPTOPOFACES = 4
    """Diagnoses topofaces without bounding edges.
    This is a beta parameter. The behavior and name may change in the future."""
    INVALIDBOUNDARYTOPOFACES = 5
    """Diagnoses topofaces with incorrect bounding edge orientation.
    This is a beta parameter. The behavior and name may change in the future."""
    SMALLTOPOEDGES = 6
    """Diagnoses topofaces with small topoedges.
    This is a beta parameter. The behavior and name may change in the future."""
    NUMBEROFFIELDS = 7
    """Diagnoses all topofaces.
    This is a beta parameter. The behavior and name may change in the future."""
