# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
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

"""Module containing the ``Part`` class."""
from typing import Any

# isort: split
from ansys.meshing.prime.autogen.part import Part as _Part

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults as SetNameResults
from ansys.meshing.prime.autogen.partstructs import PartSummaryParams


class Part(_Part):
    """Part contains zonelets and topoentities.

    Topoentities and zonelets are characterized by dimension of entities.
    Zonelets are a group of interconnected elements in a mesh. There are three types of zonelets.
    They are:

    * FaceZonelet: A group of interconnected face elements.
    * EdgeZonelet: A group of interconnected edge elements.
    * CellZonelet: A group of interconnected cell elements.

    Topoentities represent connectivity information.
    Topoentities can be queried from higher order to lower order topoentities and vice versa.
    Topoentities have geometric representation which may be defined by splines or facets.
    The mesh generated on topoentities will be projected on geometry representation.

    * TopoFace: Topoentity representing surfaces.
    * TopoEdge: Topoentity representing curves.
    * TopoVolume: Topoentity representing volumes.

    Parameters
    ----------
    model : Model
        Server model to create Part object.
    id : int
        Id of the Part.
    object_id : int
        Object id of the Part.
    name : str
        Name of the Part.
    """

    __doc__ = _Part.__doc__

    def __init__(self, model, id: int, object_id: int, name: str):
        """Initialize Part."""
        self._model = model
        self._print_mesh = False
        self._print_id = False
        _Part.__init__(self, model, id, object_id, name)

    def __call__(self, *args: Any, **kwds: Any) -> str:
        """Get a summary of the part.

        This method provides a callable interface of the part for getting a part summary
        using supported keyword arguments.

        Parameters
        ----------
        print_mesh : bool, optional
            Whether to get the mesh summary along with the part summary. The default is
            ``False``.
        print_id : bool, optional
            Whether to get IDs of TopEntities or zonelets along with the part summary.
            The default is ``False``.

        Returns
        -------
        str
            Summary of the part.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> part = model.get_part_by_name("Part.1")
        >>> print(part(print_mesh=True, print_id=True))
        """
        params = PartSummaryParams(
            model=self._model, print_id=self._print_id, print_mesh=self._print_mesh
        )
        for key, value in kwds.items():
            setattr(params, key, value)
            if key == 'print_mesh':
                params.print_mesh = value
            if key == 'print_id':
                params.print_id = value
        result = _Part.get_summary(self, params)
        return result.message

    def __str__(self) -> str:
        """Print the summary of a part.

        This method uses the ``print_mesh`` and ``print_id`` properties
        to control the summary of a part.

        Returns
        -------
        str
            Summary of the part.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> part = model.get_part_by_name("Part.1")
        >>> print(part)
        """
        params = PartSummaryParams(model=self._model)
        params.print_mesh = self._print_mesh
        params.print_id = self._print_id
        result = _Part.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the part to a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the part.

        Returns
        -------
        SetNameResults
            Newly suggested name for the part.


        Examples
        --------
        >>> part.set_suggested_name("part1")

        """
        result = _Part.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def print_mesh(self) -> bool:
        """Whether the mesh summary is set to print along with the part summary."""
        return self._print_mesh

    @print_mesh.setter
    def print_mesh(self, value: bool):
        """Print the mesh of the part.

        Parameters
        ----------
        value : bool
            Whether to print the mesh.
        """
        self._print_mesh = value

    @property
    def print_id(self) -> bool:
        """Whether IDs of TopoEntities or zonelets are set to print along with the part summary."""
        return self._print_id

    @print_id.setter
    def print_id(self, value: bool):
        self._print_id = value
