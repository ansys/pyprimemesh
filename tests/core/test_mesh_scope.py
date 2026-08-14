# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Tests for mesh visualization helpers."""

import ansys.meshing.prime as prime


def test_get_scoped_polydata_does_not_mutate_scope(initialized_model_elbow):
    """Scoped queries must leave the caller's ScopeDefinition unchanged.

    The query walks parts by temporarily narrowing ``part_expression``. Doing
    that on the input object left later plots that reuse the same scope looking
    at only the last part.
    """
    model, _ = initialized_model_elbow
    scope = prime.ScopeDefinition(model, part_expression="*", label_expression="*")
    before = (
        scope.part_expression,
        scope.label_expression,
        scope.zone_expression,
        scope.entity_type,
        scope.evaluation_type,
    )

    first = model.get_scoped_polydata(scope)
    assert before == (
        scope.part_expression,
        scope.label_expression,
        scope.zone_expression,
        scope.entity_type,
        scope.evaluation_type,
    )

    # reusing the same scope must keep returning the same entities
    second = model.get_scoped_polydata(scope)
    assert set(first) == set(second)
    for part_id in first:
        assert {info.id for _, info in first[part_id]["faces"]} == {
            info.id for _, info in second[part_id]["faces"]
        }
