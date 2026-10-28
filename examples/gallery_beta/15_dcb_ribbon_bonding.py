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

"""
.. _ref_dcb_ribbon_bonding:

================================================================
Mesh ribbon and wire bonds on a direct copper bond module (beta)
================================================================

**Summary**: This example meshes a direct copper bond module twice, once from
shared topology and once from separate bodies. Both runs use the same mesh:
the ribbons are thin-swept hexahedra, the wires are tetrahedra, and the
substrate stack is hexahedra plus the wedges swept from the wire feet. The
two runs differ in how the contacting faces are made conformal.

.. note::
   This example uses beta APIs. The behavior and names may change in the future.
   MultiZone controls are a beta feature. The beta parameters used here are:

   * ``SweepType.THINSWEEP``
   * ``MultiZoneSweepMeshParams.sweep_type``, ``thin_sweep``, and ``n_divisions``
   * ``MultiZoneSizingParams.min_size`` and ``max_size``
   * ``DeleteMeshParams.delete_mesh_on_connected_topo_edges``
   * ``MeshStackerParams.seed_faces``, used only for the separate bodies
   * ``LabelExportParams.label_expression_for_nodal_components``

Objective
~~~~~~~~~~
The module is a 25 mm substrate with copper, ceramic, die-attach, devices,
three ribbon bonds, and four wire bonds. The ribbons are too arched for the
stacker, so multi-zone thin-sweeps them. The wires are filled with tetrahedra
from a 0.25 mm quad surface. That fill triangulates the wire boundary, so the
wire mesh has no pyramids: a tetrahedron meets a triangle directly. The stacker
then sweeps those triangles on the wire feet through the substrate, which is
where the wedges come from. The rest of the stack is 0.8 mm quads, one cell
through each substrate layer, and the ribbons have three cells through their
thickness.

The CAD is prepared in two ways. The mesh recipe above is the same for both.
Only the connectivity changes:

* Shared topology, stored as a PMDAT. The wire feet and the copper are the
  same faces, so the tetrahedra and the swept wedges already share them. No
  node merge is required.
* Separate bodies, stored as an FMD. The flat faces on each wire foot are
  seeded onto the stacker base, the parts are meshed, and boundary nodes
  within 0.01 mm are fused.

The shared-topology PMDAT starts as a Discovery document (``.dsco``) in which
the solids already share faces. Prime reads it with the Workbench CAD reader,
which is the route that keeps shared topology, and writes the session to
PMDAT. One part is created for the whole model, in millimeters, and the shared
faces are validated on the way in. The example then reads that PMDAT.

.. code-block:: python

   params = prime.ImportCadParams(
       model=model,
       cad_reader_route=prime.CadReaderRoute.WORKBENCH,
       part_creation_type=prime.PartCreationType.MODEL,
       length_unit=prime.LengthUnit.MM,
       validate_shared_topology=True,
   )
   prime.FileIO(model).import_cad("dcb_bonding.dsco", params=params)
   prime.FileIO(model).write_pmdat(
       "dcb_bonding_shared_topology.pmdat", prime.FileWriteParams(model)
   )

.. image:: ../../../images/dcb_ribbon_shared_topology.png
   :align: center
   :width: 800
   :alt: Direct copper bond module with shared topology.

.. image:: ../../../images/dcb_ribbon_mesh.png
   :align: center
   :width: 800
   :alt: Mesh of the direct copper bond module.

Procedure
~~~~~~~~~~
#. Launch Ansys Prime Server.
#. Read the shared-topology module and mesh it.
#. Import the same module as separate bodies and mesh it with the foot faces
   seeded onto the stack.
#. Merge boundary nodes on the separate-body mesh.
#. Write each mesh to a MAPDL CDB file.
"""

# sphinx_gallery_tags = ["Structural", "Semiconductor", "Hex", "Tet", "Quad", "MultiZone", "Stacker", "Beta"]
# sphinx_gallery_thumbnail_number = 2

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import the modules used by both preparations.
# The geometry files are downloaded from the PyPrimeMesh example data.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import PrimePlotter

QUAD_SIZE = 0.8
WIRE_SIZE = 0.25


def show_model(model, update=False):
    """Show the module from above so the bonds are visible.

    The board lies in the XZ plane and is only a few millimeters thick, so the
    camera looks down the thickness direction with a small tilt.
    """
    display = PrimePlotter()
    display.plot(model, update=update)
    display.scene.camera_position = [(32.0, 28.0, 34.0), (0.0, 4.0, 0.0), (0.0, 1.0, 0.0)]
    display.show()


def mesh_counts(model, part):
    """Print cell and node counts."""
    summary = part.get_summary(prime.PartSummaryParams(model=model, print_mesh=True))
    print(
        f"\n{summary.n_nodes} nodes, {summary.n_hex_cells} hex, "
        f"{summary.n_prism_cells} prism, {summary.n_pyra_cells} pyramid, "
        f"{summary.n_tet_cells} tet ({summary.n_cells} cells)"
    )
    return summary


def export_mapdl_cdb(model, file_name):
    """Write a MAPDL CDB file and export labels as nodal components.

    ``label_expression_for_nodal_components`` is a beta parameter.
    """
    # Beta: LabelExportParams.label_expression_for_nodal_components.
    # The behavior and name may change in the future.
    params = prime.ExportMapdlCdbParams(model=model)
    params.label_export_params = prime.LabelExportParams(
        model=model,
        label_expression_for_nodal_components="*",
    )
    with tempfile.TemporaryDirectory() as temp_folder:
        mesh_file = os.path.join(temp_folder, file_name)
        prime.FileIO(model=model).export_mapdl_cdb(file_name=mesh_file, params=params)
        assert os.path.exists(mesh_file)
        print("\nExported file:\n", mesh_file)


def _python_ids(values):
    return [int(value) for value in values]


def _label_wire_feet(model):
    """Mark each wire volume, and the flat faces that sit on the copper."""
    utilities = prime.SurfaceUtilities(model)
    for part in list(model.parts):
        labels = list(part.get_labels())
        if not (part.name.startswith("solid") and not any("ribbon" in label for label in labels)):
            continue
        part.add_labels_on_topo_entities(["wire_solid"], _python_ids(part.get_topo_volumes()))
        faces = _python_ids(part.get_topo_faces())
        boxes = []
        for face in faces:
            zonelets = _python_ids(model.topo_data.get_geom_zonelets_of_topo_faces([face]))
            if not zonelets:
                continue
            box = utilities.get_bounding_box_of_zonelets(zonelets)
            boxes.append((face, box.ymin, box.ymax))
        if not boxes:
            continue
        foot = min(ymin for _, ymin, _ in boxes)
        # The sides of the wire make the stacker reject the seed. Keep the flat foot.
        contact = [
            face
            for face, ymin, ymax in boxes
            if ymin <= foot + 0.02 and ymax <= foot + 0.05
        ]
        if contact:
            part.add_labels_on_topo_entities(["wire_contact"], contact)


def mesh_bonded_module(model, part, use_contact_seeds=False):
    """Tet-fill the wires, thin-sweep the ribbons, and stack the substrate.

    Parameters
    ----------
    model : prime.Model
        Active model.
    part : prime.Part
        Part that contains the wires, the ribbons, and the substrate.
    use_contact_seeds : bool, optional
        Imprint the ``wire_contact`` faces onto the stacker base. Separate
        bodies need this. Shared topology already has those faces in common.

    Returns
    -------
    prime.Part
        The meshed part, still carrying topology.
    """
    name_params = prime.NamePatternParams(model)
    ribbons = _python_ids(part.get_topo_volumes_of_label_name_pattern("*ribbon*", name_params))
    wires = _python_ids(part.get_topo_volumes_of_label_name_pattern("wire_solid", name_params))
    if not wires:
        wires = _python_ids(part.get_topo_volumes_of_zone_name_pattern("*wire*", name_params))
        part.add_labels_on_topo_entities(["wire_solid"], wires)
    stack_volumes = [
        volume
        for volume in _python_ids(part.get_topo_volumes())
        if volume not in set(ribbons + wires)
    ]
    part.add_labels_on_topo_entities(["stack_solid"], stack_volumes)
    wire_faces = _python_ids(part.get_topo_faces_of_topo_volumes(wires))
    part.add_labels_on_topo_entities(["wire_faces"], wire_faces)
    print(f"\nRibbons={len(ribbons)} wires={len(wires)}")

    model.set_global_sizing_params(prime.GlobalSizingParams(model=model, min=2.0, max=2.0))
    prime.lucid.Mesh(model).surface_mesh(
        min_size=WIRE_SIZE,
        scope=prime.lucid.SurfaceScope(
            entity_expression="wire_faces",
            part_expression=part.name,
            scope_evaluation_type=prime.ScopeEvaluationType.LABELS,
        ),
        generate_quads=True,
    )

    multi_zone = model.control_data.create_multi_zone_control()
    volume_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.VOLUME,
        evaluation_type=prime.ScopeEvaluationType.LABELS,
        label_expression="*ribbon*",
    )
    surface_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.FACEZONELETS,
        evaluation_type=prime.ScopeEvaluationType.LABELS,
        label_expression="*ribbon*",
    )
    multi_zone.set_volume_scope(volume_scope)
    multi_zone.set_surface_scope(surface_scope)
    # Beta: MultiZoneSizingParams.min_size and max_size.
    # The behavior and names may change in the future.
    multi_zone.set_multi_zone_sizing_params(
        prime.MultiZoneSizingParams(model=model, min_size=QUAD_SIZE, max_size=QUAD_SIZE)
    )
    # Beta: SweepType.THINSWEEP and MultiZoneSweepMeshParams.sweep_type,
    # thin_sweep, and n_divisions.
    # The behavior and names may change in the future.
    multi_zone.set_sweep_mesh_params(
        prime.MultiZoneSweepMeshParams(
            model=model,
            sweep_type=prime.SweepType.THINSWEEP,
            thin_sweep=True,
            n_divisions=3,
        )
    )
    dead = model.control_data.create_volume_control()
    dead.set_params(prime.VolumeControlParams(model, cell_zonelet_type=prime.CellZoneletType.DEAD))
    dead.set_scope(
        prime.ScopeDefinition(
            model,
            evaluation_type=prime.ScopeEvaluationType.LABELS,
            entity_type=prime.ScopeEntity.VOLUME,
            label_expression="stack_solid",
        )
    )
    auto_mesh_params = prime.AutoMeshParams(model, volume_fill_type=prime.VolumeFillType.TET)
    auto_mesh_params.volume_control_ids = [dead.id]
    auto_mesh_params.multi_zone_control_ids = [multi_zone.id]
    prime.AutoMesh(model).mesh(part.id, auto_mesh_params)

    ribbon_faces = set(_python_ids(part.get_topo_faces_of_topo_volumes(ribbons)))
    keep = set(wire_faces) | ribbon_faces
    # Beta: DeleteMeshParams.delete_mesh_on_connected_topo_edges.
    # The behavior and name may change in the future.
    model.topo_data.delete_mesh_on_topo_faces(
        [face for face in _python_ids(part.get_topo_faces()) if face not in keep],
        prime.DeleteMeshParams(model=model, delete_mesh_on_connected_topo_edges=True),
    )

    stacker_params = prime.MeshStackerParams(
        model=model,
        direction=[0, 1, 0],
        max_offset_size=1.0,
        delete_base=True,
        lateral_defeature_tolerance=0.005,
        stacking_defeature_tolerance=0.005,
    )
    if use_contact_seeds:
        # Beta: MeshStackerParams.seed_faces.
        # The behavior and name may change in the future.
        stacker_params.seed_faces = _python_ids(
            part.get_topo_faces_of_label_name_pattern("wire_contact", name_params)
        )
    sweeper = prime.VolumeSweeper(model)
    base_faces = sweeper.create_base_face(
        part_id=part.id, topo_volume_ids=stack_volumes, params=stacker_params
    ).base_face_ids
    unmeshed = [
        face
        for face in _python_ids(base_faces)
        if not _python_ids(model.topo_data.get_mesh_zonelets_of_topo_faces([face]))
    ]
    if unmeshed:
        part.add_labels_on_topo_entities(["base_faces"], unmeshed)
        prime.lucid.Mesh(model).surface_mesh(
            min_size=QUAD_SIZE,
            scope=prime.lucid.SurfaceScope(
                entity_expression="base_faces",
                part_expression=part.name,
                scope_evaluation_type=prime.ScopeEvaluationType.LABELS,
            ),
            generate_quads=True,
        )
    sweeper.stack_base_face(
        part_id=part.id,
        base_face_ids=base_faces,
        topo_volume_ids=stack_volumes,
        params=stacker_params,
    )
    return part


###############################################################################
# Mesh the shared-topology module
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The PMDAT was written from the Discovery document with the Workbench CAD
# reader, as described above, so the shared faces are already in the file.
# Read that file. One part holds every solid, and the wire feet are faces of
# both the wire and the copper. Multi-zone meshes the ribbons, the wires are
# filled with tetrahedra, and the stacker sweeps the foot triangles with the
# substrate. No node merge is required.

shared_topology = prime.examples.download_dcb_bonding_shared_topology_pmdat()

prime_client = prime.launch_prime()
model = prime_client.model
prime.lucid.Mesh(model).read(shared_topology)
print(model)
show_model(model)

part = mesh_bonded_module(model, model.parts[0], use_contact_seeds=False)
show_model(model, update=True)
part.delete_topo_entities(
    prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
)
mesh_counts(model, part)
export_mapdl_cdb(model, "dcb_bonding_shared_topology.cdb")
prime_client.exit()

###############################################################################
# Import the module as separate bodies
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import each body as its own part. Label the wire volumes and the flat faces
# on each wire foot, then merge the parts. The foot faces are seeded onto the
# stacker so the substrate inherits the same triangles the tetrahedra use.
#
# .. image:: ../../../images/dcb_ribbon_separate_parts.png
#    :align: center
#    :width: 800
#    :alt: Direct copper bond module imported as separate bodies.

separate_parts = prime.examples.download_dcb_bonding_separate_parts_fmd()

prime_client = prime.launch_prime()
model = prime_client.model
prime.FileIO(model).import_cad(
    file_name=separate_parts,
    params=prime.ImportCadParams(
        model=model,
        length_unit=prime.LengthUnit.MM,
        part_creation_type=prime.PartCreationType.BODY,
    ),
)
print(model)
show_model(model)
_label_wire_feet(model)
merge_result = model.merge_parts(
    [part.id for part in model.parts],
    prime.MergePartsParams(model),
)
part = model.get_part(merge_result.merged_part_id)
part = mesh_bonded_module(model, part, use_contact_seeds=True)

###############################################################################
# Merge the boundary nodes
# ~~~~~~~~~~~~~~~~~~~~~~~~
# Drop the topology, then fuse boundary nodes within 0.01 mm. The seeded feet
# give the wire and the copper the same triangles, so the fuse welds that
# interface along with the other contacts between the separate bodies.

before = mesh_counts(model, part)
part.delete_topo_entities(
    prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
)
face_zonelets = _python_ids(part.get_face_zonelets())
prime.Connect(model).merge_boundary_nodes(
    part.id,
    face_zonelets,
    face_zonelets,
    prime.MergeBoundaryNodesParams(
        model,
        tolerance=0.01,
        use_absolute_tolerance=True,
        merge_node_type=prime.MergeNodeType.ALLALL,
    ),
)
after = mesh_counts(model, part)
print(f"\nMerged {before.n_nodes - after.n_nodes} nodes")
show_model(model, update=True)
export_mapdl_cdb(model, "dcb_bonding_separate_parts.cdb")
prime_client.exit()
