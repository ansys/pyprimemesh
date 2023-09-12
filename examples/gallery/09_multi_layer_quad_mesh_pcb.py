"""
.. _ref_generic_f1_rw:

================================================================
Meshing a generic PCB geometry with multiple number of layers
================================================================

**Summary**: This example showcases the process of generating a mesh for a generic PCB geometry setting the base size and the number of layers.

Objective
~~~~~~~~~~

The example demonstrates how to connect various parts of a rear wing from||||||||||||||||||||||||||||||||||||||||||||
a generic F1 car and volume mesh the resulting model using a poly-hexcore mesh containing prisms.||||||||||||||||||||||||||||||||||||||||||||
To simplify the process and enhance convenience, multiple meshing utilities provided in the||||||||||||||||||||||||||||||||||||||||||||
"lucid" class are used.||||||||||||||||||||||||||||||||||||||||||||

.. image:: ../../../images/generic_rear_wing.png||||||||||||||||||||||||||||||||||||||||||||
   :align: center
   :width: 800
   :alt: Generic F1 rear wing.

Procedure
~~~~~~~~~~
* Launch an Ansys Prime Server instance and instantiate the meshing utilities from the ``lucid`` class.
* Write a `.cas` file for use in the Fluent solver.
* Exit the PyPrimeMesh session.
"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch an instance of Ansys Prime Server.
# Connect the PyPrimeMesh client and get the model.
# Instantiate meshing utilities from the ``lucid`` class.

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics
import os
import tempfile
import time

prime_client = prime.launch_prime(timeout=60)
start=time.time()

model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Define mesh settings
# ~~~~~~~~~~~~~~~
# Define the number of layers per solid and the size in mm 
# of the quad-dominant mesh on the base size

number_of_layers_per_solid= 5
base_face_size=0.4
cad_file='C:/Users/gpappala/OneDrive - ANSYS, Inc/Documents/WIP/ANSYS/PY_PRIME_GIT_HUB_EXAMPLE/CADs/multi_layer_quad_mesh_pcb.pmdb'

###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the generic sample pcb geometry.
# Use the WORKBENCH CadReaderRoute to ensure that the shared topology is kept.
# Display the imported geometry.

mesh_util.read(
    file_name=cad_file,
    cad_reader_route=prime.CadReaderRoute.WORKBENCH)
display = Graphics(model)
display()

###############################################################################
# Define edge sizing constraints
# ~~~~~~~~~~~~~~~
# Set generic global sizing from 0.002mm and 2mm.
# Extract the the edges length from the named selections such as edge_1_0.50_mm (extract 0.5 mm length) or edge_23_0.27_mm (extract 0.27mm length).
# Assign, on each edge, a size equal to the edge's length divided by the pre-defined number of layers per solid.

model.set_global_sizing_params(prime.GlobalSizingParams(model,min=0.002,max=2.))
ids=[]
part=model.parts[0]
for label in part.get_labels():
    # Check whether the named selection's name starts with the string "edge"
    if label.startswith('edge'):
        # Extract the edge's length splitting its name at every "_" string and collect the second-last number
        length = float(label.split("_")[-2])
        soft_size_control=model.control_data.create_size_control(prime.SizingType.SOFT)
        soft_size_params = prime.SoftSizingParams(model = model,max=length/number_of_layers_per_solid)
        soft_size_control.set_soft_sizing_params(soft_size_params)
        soft_size_scope=prime.ScopeDefinition(model,part_expression=part.name,
                                                entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS,
                                                label_expression=label+"*")
        soft_size_control.set_scope(soft_size_scope)
        soft_size_control.set_suggested_name(label)
        # Append the id of the edge sizing to the edge sizings' ids' list
        ids.append(soft_size_control.id)

###############################################################################
# Define Controls for volume sweeper
# ~~~~~~~~~~~~~~~
# Set the sweep direction vector.
# Setup the geometric tolerances for lateral and stacking defeature.
# Append the ids of the soft local sizings that have been previously-defined on the edges.

sweeper = prime.VolumeSweeper(model)
stacker_params = prime.MeshStackerParams(
    model=model,
    direction=[0, 0, 1],
    delete_base=True,
    lateral_defeature_tolerance=0.001,
    stacking_defeature_tolerance=0.001,
    size_control_ids=ids
    )

###############################################################################
# Define Controls for base face meshing
# ~~~~~~~~~~~~~~~
# Create a soft sizing control. 
# Assign the previously defined base_face_size to the soft sizing.
# Create the base face. 
# Mesh the base face.
# Display the base face.


soft_size_control=model.control_data.create_size_control(prime.SizingType.SOFT)
soft_size_params = prime.SoftSizingParams(model = model,max=base_face_size)
soft_size_control.set_soft_sizing_params(soft_size_params)
soft_size_scope=prime.ScopeDefinition(model,part_expression=part.name,
                                    entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS)
soft_size_control.set_scope(soft_size_scope)
soft_size_control.set_suggested_name("base_face_size")

# Create the base face appending the the stacker mesh parameters.
createbase_results = sweeper.create_base_face(
    part_id=model.get_part_by_name(part.name).id,
    topo_volume_ids=model.get_part_by_name(part.name).get_topo_volumes(),
    params=stacker_params)
base_faces = createbase_results.base_face_ids
model.get_part_by_name(part.name).add_labels_on_topo_entities(["base_faces"], base_faces)
scope = prime.ScopeDefinition(model=model, label_expression="base_faces")
base_scope = prime.lucid.SurfaceScope(
    entity_expression="base_faces",
    part_expression=part.name,
    scope_evaluation_type=prime.ScopeEvaluationType.LABELS,)
# Generate the surface mesh on the base face.
mesh_util_controls = mesh_util.surface_mesh_with_size_controls(size_control_names="base_face_size", 
                                          scope=base_scope, 
                                          generate_quads=True)
display()

###############################################################################
# Stack the base face using the volume sweeper.
# ~~~~~~~~~~~~~~~
# Use volume sweeper to stack the base face along the previously-defined sweep direction.
# Include the previously-defined stacker parameters.
# Display the final volume mesh.

stackbase_results = sweeper.stack_base_face(
    part_id=model.get_part_by_name(part.name).id,
    base_face_ids=base_faces,
    topo_volume_ids=model.get_part_by_name(part.name).get_topo_volumes(),
    params=stacker_params)
display()

###############################################################################
# Setup the zone naming before the mesh output
# ~~~~~~~~~~~~~~~
# Delete the unnecessary topo entities.
# Name the walls of "solid" as "wall_solid" (ex if the solid's name is "A", the walls surrounding the solid will be named "wall_A").
# Convert the labels to mesh zones.
 
part.delete_topo_entities(params=prime.DeleteTopoEntitiesParams(model,
                                                                delete_geom_zonelets=True,
                                                                delete_mesh_zonelets=False))
for volume in part.get_volumes():
    volume_zone_name = "wall_"+model.get_zone_name(part.get_volume_zone_of_volume(volume))
    label_zonelets = part.get_face_zonelets_of_volumes([volume])
    part.add_labels_on_zonelets([volume_zone_name], label_zonelets)
mesh_util_create_zones = mesh_util.create_zones_from_labels()

###############################################################################
# Output the mesh in .cas format
# ~~~~~~~~~~~~~~~~

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "multi_layer_quad_mesh_pcb.cas")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)
#mesh_util.write(cad_file.replace('pmdb','cas'))
###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
