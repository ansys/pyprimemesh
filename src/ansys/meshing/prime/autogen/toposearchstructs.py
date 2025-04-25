# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INTERSECTINGTOPOFACES = 1
    """Diagnoses intersecting topofaces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SELFINTERSECTINGTOPOFACES = 2
    """Diagnoses topofaces with self intersecting bounding edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    BROKENLOOPTOPOFACES = 3
    """Diagnoses topofaces with open or broken bounding edge loops.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    NOBOUNDARYLOOPTOPOFACES = 4
    """Diagnoses topofaces without bounding edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INVALIDBOUNDARYTOPOFACES = 5
    """Diagnoses topofaces with incorrect bounding edge orientation.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SMALLTOPOEDGES = 6
    """Diagnoses topofaces with small topoedges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INCORRECTBOUNDARYORIENTATIONTOPOFACES = 7
    """Diagnoses topofaces with incorrect boundary orientations.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    INCONSISTENTNORMALORIENTATIONTOPOFACES = 8
    """Diagnoses topofaces with inconsistent normal orientations.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    NUMBEROFFIELDS = 9
    """Diagnoses all topofaces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
