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


class SizeFieldType(enum.IntEnum):
    """The type of sizing field to be used to fetch element size at given location.
    """
    GEOMETRIC = 0
    """Geometric size field."""
    VOLUMETRIC = 1
    """Uses precomputed variable size in volumetric space defined by size field."""
    GEODESIC = 2
    """Uses geodesic size field."""
    CONSTANT = 3
    """Uses constant size at all locations of sizing field."""
    MESHEDGEODESIC = 7
    """Computes size field using existing surface mesh sizes and diffuses geodesically. Then uses the computed size field to remesh surfaces. Notes: The type is applicable when remeshing already meshed surfaces."""

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
    """The Skewness metric ranges between 0 (worst) and 1 (best). A value of 0 indicates an equilateral cell (best) and a value of 1 indicates a completely degenerate cell (worst)."""
    SIZECHANGE = 2
    """Size Change is the maximum ratio of the area of each neighboring face element to the area of face element when the area of the face element is smaller than the neighbor. The minimum value for size change is 1."""
    ASPECTRATIO = 5
    """The Aspect Ratio metric is greater than 1. A value of 1 indicates an equilateral cell (best) and a value of 20(e.g) indicates a stretched cell (worst)."""
    WARP = 7
    """Face quality metric to check warping factor.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ELEMENTQUALITY = 50
    """The Element Quality metric ranges between 0 (worst) and 1 (best). A value of 1 indicates a perfect cube or square (best) while a value of 0 indicates that the element has a zero or negative volume (worst)."""

class CellQualityMeasure(enum.IntEnum):
    """The type of cell quality measures to check cell quality metrics.
    """
    SKEWNESS = 0
    """The Skewness metric ranges between 0 (best) and 1 (worst). A value of 0 indicates an equilateral cell (best) and a value of 1 indicates a completely degenerate cell (worst)."""
    ASPECTRATIO = 5
    """The Aspect Ratio metric is greater than 1. A value of 1 indicates an equilateral cell (best) and a value of 20(e.g) indicates a stretched cell (worst)."""
    FLUENTASPECTRATIO = 13
    """The Fluent aspect Ratio metric is greater than 1. A value of 1 indicates an equilateral cell (best) and a value of 20(e.g) indicates a stretched cell (worst)."""
    INVERSEORTHOGONAL = 14
    """The inverse orthogonal metric ranges between 0 (best) and 1 (worst)."""
    INVERSEORTHOGONAL_V2 = 25
    """The advanced inverse orthogonal metric ranges between 0 (best) and 1 (worst)."""
    ELEMENTQUALITY = 50
    """The Element Quality metric ranges between 0 (worst) and 1 (best). A value of 1 indicates a perfect cube or square (best) while a value of 0 indicates that the element has a zero or negative volume (worst)."""

class SurfaceFeatureType(enum.IntEnum):
    """Type of face edges considered as features.
    """
    NONE = 0
    """None of face edges are considered as feature."""
    ZONEBOUNDARY = 1
    """Face edges at zone boundary are considered as feature."""
    FEATURE = 2
    """Face edges with normal angle more than threshold are considered as feature."""
    FEATUREORZONEBOUNDARY = 3
    """Face edges at zone boundary or with normal angle more than threshold are considered as feature."""
    ZONELETBOUNDARY = 4
    """Face edges at zonelet boundary are considered as feature."""
    FEATUREORZONELETBOUNDARY = 5
    """Face edges at zonelet boundary or with normal angle more than threshold are considered as feature."""

class ShellBLOffsetType(enum.IntEnum):
    """Type of offset method during ShellBL generation.
    """
    ASPECTRATIO = 0
    """Option to set ShellBL offset type as Aspect Ratio.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    LASTRATIO = 1
    """Option to set ShellBL offset type as Last Ratio.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    UNIFORM = 2
    """Option to set ShellBL offset type as Uniform.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CURVATUREBASED = 4
    """Option to set ShellBL offset type as CurvatureBased.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
