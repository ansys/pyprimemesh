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
.. _ref_saddle_thin_hex:

===============================================
Mesh a saddle bracket for a structural analysis
===============================================

**Summary**: This example demonstrates how to mesh a thin
solid with hexahedral and prism cells.

Objective
~~~~~~~~~

This example creates a mainly hexahedral mesh on a thin solid volume.

.. image:: ../../../images/saddle_bracket.png
   :align: center
   :width: 400
   :alt: Thin volume hexahedral mesh.

Procedure
~~~~~~~~~
#. Launch Ansys Prime Server.
#. Import the CAD geometry.
#. Quad surface mesh the source face.
#. Surface mesh the remaining unmeshed TopoFaces with tri surface mesh.
#. Delete the topology.
#. Define volume meshing controls to use thin volume meshing.
#. Volume mesh with hexahedral and prism cells.
#. Write a CDB file for use in the APDL solver.
#. Exit the PyPrimeMesh session.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch an instance of Ansys Prime Server.
# Connect the PyPrimeMesh client and get the model.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import PrimePlotter

prime_client = prime.launch_prime()
model = prime_client.model

mesh_util = prime.lucid.Mesh(model)

###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the saddle bracket geometry (FMD) file exported by SpaceClaim.
# Import the geometry and display all.

# For Windows OS users, scdoc is also available:
# saddle_bracket = prime.examples.download_saddle_bracket_scdoc()

saddle_bracket = prime.examples.download_saddle_bracket_fmd()

mesh_util.read(file_name=saddle_bracket)

print(model)

display = PrimePlotter()
display.plot(model)
display.show()

###############################################################################
# Quad mesh source faces
# ~~~~~~~~~~~~~~~~~~~~~~
# Mesh the source faces for the thin volume control with quads.

scope = prime.lucid.SurfaceScope(
    part_expression="*",
    entity_expression="source_thin",
    scope_evaluation_type=prime.ScopeEvaluationType.LABELS,
)

mesh_util.surface_mesh(
    scope=scope,
    min_size=2.0,
    generate_quads=True,
)

display = PrimePlotter()
display.plot(model, update=True)
display.show()

###############################################################################
# Surface mesh unmeshed faces
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Mesh unmeshed faces with tri surface mesh.  Tri surface mesh on the target
# and side faces is used to show more clearly that the result of the thin
# volume control is a hex mesh that is imprinted up to the side faces.
# All quads could be used for the surface mesh to simplify the process.

part = model.parts[0]

all_faces = part.get_topo_faces()
meshed_faces = part.get_topo_faces_of_label_name_pattern(
    label_name_pattern="source_thin",
    name_pattern_params=prime.NamePatternParams(model),
)

unmeshed_faces = [face for face in all_faces if face not in meshed_faces]

part.add_labels_on_topo_entities(
    labels=["unmeshed_faces"],
    topo_entities=unmeshed_faces,
)

scope = prime.lucid.SurfaceScope(
    part_expression="*",
    entity_expression="unmeshed_faces",
    scope_evaluation_type=prime.ScopeEvaluationType.LABELS,
)

mesh_util.surface_mesh(
    scope=scope,
    min_size=2.0,
)

display = PrimePlotter()
display.plot(model, update=True)
display.show()

###############################################################################
# Delete topology
# ~~~~~~~~~~~~~~~
# Delete topology to leave only the surface mesh.  This is necessary for the
# thin volume control to be used.

part.delete_topo_entities(
    prime.DeleteTopoEntitiesParams(
        model=model,
        delete_geom_zonelets=True,
        delete_mesh_zonelets=False,
    )
)

###############################################################################
# Define volume meshing controls
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define volume meshing controls to use thin volume meshing.
# Specify source and target faces for the thin volume using imported labels.
# Set the number of layers of cells through the thickness of the thin solid to be 4.
# To create a fully hexahedral and prism mesh the side faces must be imprinted on
# the side faces. If needed, a buffer region at the sides of the volume can be
# defined where the volume fill type used for the volume mesh parameters is
# used to infill. This is useful on more complex geometries, where it provides
# more robustness of the method. To create a buffer region set ``imprint_sides``
# to ``False`` and specify how many rings of cells to ignore at the sides
# using ``n_ignore_rings``.

auto_mesh_params = prime.AutoMeshParams(model=model)
thin_vol_ctrls_ids = []
thin_vol_ctrl = model.control_data.create_thin_volume_control()

thin_vol_ctrl.set_source_scope(
    prime.ScopeDefinition(
        model=model,
        label_expression="source_thin",
    )
)

thin_vol_ctrl.set_target_scope(
    prime.ScopeDefinition(
        model=model,
        label_expression="target_thin",
    )
)

thin_params = prime.ThinVolumeMeshParams(
    model=model,
    n_layers=4,
    imprint_sides=True,
)

thin_vol_ctrl.set_thin_volume_mesh_params(thin_volume_mesh_params=thin_params)
thin_vol_ctrls_ids.append(thin_vol_ctrl.id)
auto_mesh_params.thin_volume_control_ids = thin_vol_ctrls_ids
auto_mesh_params.volume_fill_type = prime.VolumeFillType.TET

###############################################################################
# Generate volume mesh
# ~~~~~~~~~~~~~~~~~~~~
# Volume mesh to obtain hexahedral and prism mesh.
# Print mesh summary.
# Display volume mesh.

volume_mesh = prime.AutoMesh(model=model)
result_vol = volume_mesh.mesh(part_id=part.id, automesh_params=auto_mesh_params)
print(part.get_summary(prime.PartSummaryParams(model)))

display = PrimePlotter()
display.plot(model, update=True)
display.show()
###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write a CDB file for use in the MAPDL solver.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "saddle_bracket.cdb")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
