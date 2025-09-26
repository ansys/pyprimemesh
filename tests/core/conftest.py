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

"""Fixtures for the core modules."""
import pytest

import ansys.meshing.prime as prime


@pytest.fixture(scope="module")
def initialized_model_elbow(get_remote_client, get_examples):
    """Gets the elbow example and initializes the model and its mesher. Returns the initialized
    model and mesher."""
    # load example from fixture
    elbow_lucid = get_examples["elbow_lucid"]

    # initialize model from fixture
    model = get_remote_client.model
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=elbow_lucid)
    return model, mesher


@pytest.fixture(scope="module")
def initialized_model_toycar(get_remote_client, get_examples):
    """Gets the toy car example and initializes the model and its mesher. Returns the initialized
    model and mesher."""
    # load example from fixture
    toy_car = get_examples["toy_car"]

    # initialize model from fixture
    model = get_remote_client.model
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=toy_car)
    return model, mesher
