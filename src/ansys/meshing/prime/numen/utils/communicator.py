# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

from ansys.meshing import prime


class PrimeObj:
    def __init__(self, model: prime.Model, object_name: str, part_id: int = None):
        self.model = model
        self.object_name = object_name
        args = {"ModelID": model._object_id, "MaxID": -1}
        if part_id is not None:
            args["PartID"] = part_id
        result = model._communicator.serve(model, f"PrimeMesh::{object_name}/Construct", args=args)
        self._object_id = result["ObjectIndex"]

    def call_method(self, command_name: str, args: dict):
        return call_method(
            self.model, f"PrimeMesh::{self.object_name}/{command_name}", self._object_id, args
        )

    def destruct(self):
        self.model._communicator.serve(
            self.model, f"PrimeMesh::{self.object_name}/Destruct", self._object_id, args={}
        )


def call_method(model: prime.Model, command_name: str, object_id: int, args: dict):
    result = model._communicator.serve(model, command_name, object_id, args=args)
    return result


vt_composer_params = {
    "edgeSharpCornerAngleDeg": 25,
    "mergeFaceNormalsAngleDeg": 30,
    "worstAcceptableMergeInternalFaceAngleDeg": 45,
    "thinStripesTol": 0.001,
    "smallestEdgeLength": -1.0,
    "remeshConstantSize": -1.0,
    "mergeOffsetFactor": 0.0,
    "filletMinRadius": 0.0,
    "filletMaxRadius": 10000000000000000000.0,
    "filletRadiusDeviationRatio": 0.40,
    "filletAspectRatio": 4.0,
    "filletSpanningAngleDeg": 180,
    "directionX": 0.0,
    "directionY": 0.0,
    "directionZ": 0.0,
    "verboseDiagnostics": False,
    "deleteAftermerge": True,
    "suppressSharedEdgesWhenMerging": True,
    "mergeEdgeAllowSelfClose": False,
    "useGeodesicPathForSplitting": True,
    "useDefaultLocalRemeshSize": True,
    "splitFaceMethod": 1,
    "projectionMethod": 0,
    "holeFillMethod": 0,
    "repairFreeEdgesMethod": 1,
    "nHoleFillFaceLayers": 1,
    "duplicateNodesDuringEdgeSeparation": False,
    "dupliateFaceNodesDuringEdgeSeparation": False,
    "projectionMorphHigherEntities": False,
    "suppressBoundaryAfterHoleFill": False,
    "collapseSmallHolesDuringPinch": False,
    "deleteMeshAfterMerge": False,
    "fillAnnularHole": False,
    "splitAlongEdge": False,
    "useSizeFieldRemesh": False,
    "limitMergeScopeToInputs": False,
    "refacetTopoEntities": False,
    "allowCurvedTopoFaces": True,
    "aggressiveMerge": False,
    "holeFillSurfaceType": 0,
}
