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

"""
.. _ref_pygeometry_import:

=================================
Import a geometry from PyGeometry
=================================

**Summary**: This example demonstrates how to create a simple geometry using
PyGeometry and import it into PyPrimeMesh.



Procedure
~~~~~~~~~
#. Launch Ansys Prime Server.
#. Create a CAD geometry with PyGeometry.
#. Import the geometry into PyPrimeMesh.
#. Exit the PyPrimeMesh session.



Create the geometry
~~~~~~~~~~~~~~~~~~~
First we create a simple geometry using PyGeometry. The geometry is a plate
with a hole in the center:

.. code-block:: python

   from pint import Quantity

   from ansys.geometry.core import launch_modeler
   from ansys.geometry.core.math import Point2D
   from ansys.geometry.core.misc import UNITS
   from ansys.geometry.core.sketch import Sketch
   from ansys.geometry.core.math import Point2D

   sketch = Sketch()
   (
       sketch.segment(Point2D([-4, 5], unit=UNITS.m), Point2D([4, 5], unit=UNITS.m))
       .segment_to_point(Point2D([4, -5], unit=UNITS.m))
       .segment_to_point(Point2D([-4, -5], unit=UNITS.m))
       .segment_to_point(Point2D([-4, 5], unit=UNITS.m))
       .box(Point2D([0, 0], unit=UNITS.m), Quantity(3, UNITS.m), Quantity(3, UNITS.m))
   )
   modeler = launch_modeler(hidden=True)
   design = modeler.create_design("ExtrudedPlateNoHoles")
   body = design.extrude_sketch(f"PlateLayer", sketch, Quantity(2, UNITS.m))

Import the geometry into PyPrimeMesh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once the geometry is created, we can pass the Design object to PyPrimeMesh to
create a mesh:

.. code-block:: python

   import ansys.meshing.prime as prime
   from ansys.meshing.prime.graphics.plotter import PrimePlotter

   prime_client = prime.launch_prime()
   model = prime_client.model
   mesh_util = prime.lucid.Mesh(model=model)
   mesh_util.from_geometry(design)


Mesh the geometry and display it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
With the geometry imported, we can now mesh it and display the mesh:

.. code-block:: python

   mesh_util.surface_mesh(min_size=0.1, max_size=0.5)
   display = PrimePlotter()
   display.plot(model)
   display.show()
   modeler.close()
"""
