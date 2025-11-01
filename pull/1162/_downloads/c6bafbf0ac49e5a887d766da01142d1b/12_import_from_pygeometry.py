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
#. Launch the Geometry service and create a simple geometry.
#. Launch Ansys Prime Server.
#. Create a CAD geometry with PyGeometry.
#. Import the geometry into PyPrimeMesh.
#. Mesh and display the imported geometry.
#. Exit the PyPrimeMesh and PyGeometry sessions.



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

   modeler = launch_modeler(hidden=True)

   sketch = Sketch()
   (
       sketch.segment(Point2D([-4, 5], unit=UNITS.mm), Point2D([4, 5], unit=UNITS.mm))
       .segment_to_point(Point2D([4, -5], unit=UNITS.mm))
       .segment_to_point(Point2D([-4, -5], unit=UNITS.mm))
       .segment_to_point(Point2D([-4, 5], unit=UNITS.mm))
       .box(Point2D([0, 0], unit=UNITS.mm), Quantity(3, UNITS.mm), Quantity(3, UNITS.mm))
   )
   design = modeler.create_design("ExtrudedPlateNoHoles")
   body = design.extrude_sketch(f"PlateLayer", sketch, Quantity(2, UNITS.mm))
   sketch_hole = Sketch()
   sketch_hole.circle(Point2D([0, 0], unit=UNITS.mm), Quantity(0.5, UNITS.mm))

   hole_centers = [
       Plane(Point3D([3, 4, 0], unit=UNITS.mm)),
       Plane(Point3D([-3, 4, 0], unit=UNITS.mm)),
       Plane(Point3D([-3, -4, 0], unit=UNITS.mm)),
       Plane(Point3D([3, -4, 0], unit=UNITS.mm)),
   ]
   for center in hole_centers:
       sketch_hole.plane = center
       design.extrude_sketch(
           name=f"H_{center.origin.x}_{center.origin.y}",
           sketch=sketch_hole,
           distance=Quantity(2, UNITS.mm),
           cut=True,
       )


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

   model.set_global_sizing_params(
       prime.GlobalSizingParams(model, min=0.2, max=10.0, growth_rate=1.2)
   )
   mesh_util.surface_mesh(min_size=0.2)
   mesh_util.volume_mesh()

   # Print the results
   model.parts[0].print_mesh = True
   print(model)
   display = PrimePlotter()
   display.plot(model)
   display.show()
   modeler.close()
   prime_client.exit()
"""
