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
.. _ref_contact_patch:

========================================================================
Create a contact patch for wrapping between a wheel and ground interface
========================================================================

**Summary**: This example demonstrates how to create a contact patch for use with wrapping
to avoid meshing into a narrow contact region between two objects.

Objective
~~~~~~~~~
This example uses a contact patch for wrapping to avoid the interface of a wheel with the ground
to improve mesh quality when growing prism layers in the region of the contacting faces.

.. image:: ../../../images/contact_patch.png
   :align: center
   :width: 600

The preceding image shows the following:


* Top left: Wheel/ground interface
* Top right: Addition of contact patch
* Lower left: Grouping tolerance at 4 with multiple contact patches
* Lower right: Grouping tolerance at 20 with merged single contact patch



Procedure
~~~~~~~~~
#. Launch an Ansys Prime Server instance and instantiate the meshing utilities
   from the ``lucid`` class.
#. Import the wheel ground geometry.
#. Convert the topo parts to mesh parts so that the contact patch can be created.
#. Create a contact patch between the wheel and the ground.
#. Extract the fluid region using wrapping.
#. Volume mesh with polyhedral and prism cells.
#. Write a CAS file for use in the Fluent solver.
#. Exit the PyPrimeMesh session.


"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules and launch an instance of Ansys Prime Server.
# From the PyPrimeMesh client, get the model.
# Instantiate meshing utilities from the ``lucid`` class.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import PrimePlotter

client = prime.launch_prime()
model = client.model

mesh_util = prime.lucid.Mesh(model)

###############################################################################
# Import CAD geometry
# ~~~~~~~~~~~~~~~~~~~
# Download the wheel ground geometry (FMD) file exported by SpaceClaim.
# Import the CAD geometry. The geometry consists of two topo parts: a wheel and an enclosing box.
# Labels are defined for the ground topo face on the enclosure and for the wheel
# as all the topo faces of the wheel part.

# For Windows OS users, SCDOC or DSCO is also available. For example:
# wheel_ground_file = prime.examples.download_wheel_ground_scdoc()

wheel_ground_file = prime.examples.download_wheel_ground_fmd()

mesh_util.read(wheel_ground_file)


###################
# Visualize results
# =================
# .. code-block:: python
#
#   display = PrimePlotter()
#   display.plot(model, scope=prime.ScopeDefinition(model, label_expression="ground, wheel"))
#   display.show()

print(model)

###############################################################################
# Convert topo parts to mesh parts
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert the faceted geometry of the topology to mesh for all parts as the contact patch
# requires face zonelets from mesh parts as input.

wheel_part = model.get_part_by_name("wheel_body")
enclosure_part = model.get_part_by_name("enclosure")

[part.delete_topo_entities(prime.DeleteTopoEntitiesParams(model)) for part in model.parts]

###############################################################################
# Create a contact patch
# ~~~~~~~~~~~~~~~~~~~~~~
# To create a contact patch, a direction is needed to define the resulting shape of the patch.
# A new part is created containing the patch.
# A prefix can be specified for the label created for the contact patch face zonelets generated.
# The offset distance determines the thickness and extent of the patch.  The source face zonelet is
# offset to intersect the planar target face and the intersection used to define the contact patch.
# Due to the depth of the treads on the wheel, 20.0 is used as the offset to reach the tire surface.
# If multiple contact regions are found, they can be merged by grouping them using the grouping
# tolerance distance.  With a grouping tolerance of 4.0, separate contact regions are created for
# some of the treads of the tire, see the image at the top of the example. To merge these contact
# regions into a single patch, the grouping tolerance distance is increased to 20.0, avoiding small
# gaps between contact regions.

# The face zonelets of the wheel are defined as the source.
# The planar surface must be specified as the target.
# In this instance, the ground provides the planar target.

source = wheel_part.get_face_zonelets()
target = enclosure_part.get_face_zonelets_of_label_name_pattern(
    "ground", prime.NamePatternParams(model)
)

params = prime.CreateContactPatchParams(
    model,
    contact_patch_axis=prime.ContactPatchAxis.Z,
    offset_distance=20.0,
    grouping_tolerance=20.0,
    suggested_label_prefix="patch",
)
result = prime.SurfaceUtilities(model).create_contact_patch(
    source_zonelets=source, target_zonelets=target, params=params
)
print(result.error_code)
print(model)

###################
# Visualize results
# =================
# .. code-block:: python
#
#   display = PrimePlotter()
#   display.plot(
#          model, scope=prime.ScopeDefinition(model, label_expression="ground, patch*, wheel")
#   )
#   display.show()

###############################################################################
# Wrap the fluid region
# ~~~~~~~~~~~~~~~~~~~~~
# The largest internal region in this instance is the fluid region around the wheel.
# Intersection loops are created to capture the features at the corners between the
# patch, ground, and wheel.

model.set_global_sizing_params(prime.GlobalSizingParams(model, min=4.0, max=100.0, growth_rate=1.4))

# Create a size control to limit the size of mesh on the wheel.
size_control = model.control_data.create_size_control(prime.SizingType.SOFT)
size_control.set_soft_sizing_params(prime.SoftSizingParams(model=model, max=8.0))
size_control.set_scope(prime.ScopeDefinition(model=model, label_expression="wheel"))

wrap_part = mesh_util.wrap(
    min_size=4.0,
    max_size=100.0,
    region_extract=prime.WrapRegion.LARGESTINTERNAL,
    create_intersection_loops=True,
    wrap_size_controls=[size_control],
)

#########################
# Open a pyvistaqt window
# =======================
# .. code-block:: python
#
#     display = PrimePlotter()
#     display.plot(
#         model,
#         scope=prime.ScopeDefinition(model, label_expression="ground, patch*, wheel"), update=True
#     )
#     display.show()

print(model)

###############################################################################
# Volume mesh
# ~~~~~~~~~~~
# Apply five layers of prisms to the wheel, patch, and ground. Mesh with polyhedrals.

model.set_global_sizing_params(prime.GlobalSizingParams(model, min=4.0, max=100.0, growth_rate=1.4))
mesh_util.volume_mesh(
    volume_fill_type=prime.VolumeFillType.POLY,
    prism_layers=5.0,
    prism_surface_expression="wheel, patch*, ground",
    prism_volume_expression="*",
    scope=prime.lucid.VolumeScope(part_expression=wrap_part.name),
)

display = PrimePlotter()
display.plot(
    model,
    scope=prime.ScopeDefinition(model, label_expression="!front !side_right !top"),
    update=True,
)
display.show()

mesh_util.create_zones_from_labels()

wrap_part._print_mesh = True
print(wrap_part)

###############################################################################
# Write model
# ~~~~~~~~~~~
# Write a CAS file for use in the Fluent solver.

with tempfile.TemporaryDirectory() as temp_folder:
    wheel_model = os.path.join(temp_folder, "wheel_ground_contact.cas.h5")
    prime.FileIO(model).export_fluent_case(
        wheel_model,
        export_fluent_case_params=prime.ExportFluentCaseParams(model, cff_format=True),
    )
    assert os.path.exists(wheel_model)
    print(f"Fluent case exported at {wheel_model}")

###############################################################################
# Exit the PyPrimeMesh session
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

client.exit()
