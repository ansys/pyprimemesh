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

"""Model for cached data."""
import logging

from ansys.meshing import prime


def create_size_control(model: prime.Model, parameters, cached_data) -> int:
    """Create size control."""
    sizing_type = parameters["sizing_type"]
    sizing_params = parameters["sizing_params"]
    control = model.control_data.create_size_control(sizing_type)
    if sizing_type == prime.SizingType.HARD:
        control.set_hard_sizing_params(sizing_params)
    elif sizing_type == prime.SizingType.SOFT:
        control.set_soft_sizing_params(sizing_params)
    elif sizing_type == prime.SizingType.BOI:
        control.set_boi_sizing_params(sizing_params)
    elif sizing_type == prime.SizingType.CURVATURE:
        control.set_curvature_sizing_params(sizing_params)
    elif sizing_type == prime.SizingType.PROXIMITY:
        control.set_proximity_sizing_params(sizing_params)
    control.set_scope(parameters["scope"])
    return control.id


def create_size_field(model: prime.Model, parameters, cached_data) -> int:
    """Create size field."""
    controls = []
    for size_control in parameters["size_controls"]:
        controls.append(cached_data.create_cached_object(size_control))
    # create_size_field
    size_field = prime.SizeField(model)
    periodic_params = prime.SFPeriodicParams(model, angle=0.0)
    params = prime.VolumetricSizeFieldComputeParams(
        model, enable_multi_threading=False, periodic_params=periodic_params
    )
    res = size_field.compute_volumetric(controls, params)
    for size_control in parameters["size_controls"]:
        cached_data.destroy_cached_object(size_control)
    return res.size_field_id


def delete_control(model: prime.Model, control_id: int):
    """Delete control."""
    model.control_data.delete_controls([control_id])


def delete_size_field(model: prime.Model, size_field_id: int):
    """Delete size field."""
    model.delete_volumetric_size_fields([size_field_id])


class CachedObject:
    """CachedObject class."""

    def __init__(self, method, params):
        """Construct cached object."""
        self.method = method
        self.parameters = params
        self.id: int = 0

    def create(self, model, cached_data) -> int:
        """Create size control or size field for cache."""
        if self.method == "numen.controls.create_size_control":
            self.id = create_size_control(model, self.parameters, cached_data)
        elif self.method == "numen.controls.create_size_field":
            self.id = create_size_field(model, self.parameters, cached_data)
        return self.id

    def destroy(self, model):
        """Destroy cached object."""
        if self.id == 0:
            return
        if self.method == "numen.controls.create_size_control":
            delete_control(model, self.id)
            self.id = 0
        elif self.method == "numen.controls.create_size_field":
            delete_size_field(model, self.id)
            self.id = 0


class CachedData:
    """CachedData class."""

    def __init__(self, model: prime.Model, logger: logging.Logger):
        """Construct cached data object."""
        self._model = model
        self._logger = logger
        self._cached_objects: dict[str, CachedObject] = {}

    def push_cached_object(self, name: str, method: str, parameters: any) -> bool:
        """Push cached object."""
        if name in self._cached_objects:
            self._logger.error("Duplicate name \"%s\".", name)
            return False
        else:
            self._cached_objects[name] = CachedObject(method, parameters)

    def create_cached_object(self, name: str) -> int:
        """Create cached object."""
        if name in self._cached_objects:
            return self._cached_objects[name].create(self._model, self)
        else:
            self._logger.error("Name \"%s\" not found.", name)
        return 0

    def destroy_cached_object(self, name: str):
        """Destroy cached object."""
        if name in self._cached_objects:
            self._cached_objects[name].destroy(self._model)
        else:
            self._logger.error("Name \"%s\" not found.", name)

    def pop_cached_object(self, name: str):
        """Pop cached object."""
        if name in self._cached_objects:
            self._cached_objects[name].destroy(self._model)
            del self._cached_objects[name]
        else:
            self._logger.error("Name \"%s\" not found.", name)
