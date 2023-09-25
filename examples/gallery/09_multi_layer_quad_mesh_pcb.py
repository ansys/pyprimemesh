"""
.. _ref_multi_layer_pcb_mesh:

================================================================
Meshing a generic PCB geometry with multiple number of hexa layers
================================================================

**Summary**: This example showcases the process of generating a mesh for a generic PCB geometry giving the possibbility to set the base mesh size and the number of layers for each solid.

Objective
~~~~~~~~~~

The example demonstrates how to use PyPrimeMesh to discretize a PCB CAD geometry by means of the stacker technology.
This script allows to easily setup the mesh size of the base face (xy plane in this example) and the number of mesh layers along the sweep direction (z axis in this example).
The CAD adges along the z direction have been assigned with a named selection at CAD level in Ansys Discovery/SpaceClaim (as shown in the description image).
These named selections will allow specifying the number of mesh elements to be generated along such edges.
To simplify the process and enhance convenience, multiple meshing utilities provided in the ``lucid`` class are used.

.. image:: ../../../images/multi_layer_quad_mesh_pcb.png
   :align: center
   :width: 800
   :alt: Generic PCB geometry.

Procedure
~~~~~~~~~~
* Import the fundamental libraries that are necessary top run the script
* Launch an Ansys Prime Server instance and instantiate the meshing utilities from the ``lucid`` class.
* Define the main mesh parameters: base size and number of layers along the sweep direction. 
* Import the CAD geometry.
* Define the edge sizing along the sweep direction (based on pre-existing edges named selections).
* Define the parameters for the volume sweeper.
* Setup, generate, and mesh the base face.
* Stack the base face along the sweep direction.
* Setup the zone naming before the mesh output.
* Write a `.cas` file for use in the Fluent solver.
* Exit the PyPrimeMesh session.
"""

###############################################################################
# Import all necessary modules
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Notice that PyVista library must be installed to be able to run the visualization tools included in this script
# Launch an instance of Ansys Prime Server.
# Connect the PyPrimeMesh client and get the model.
# Instantiate meshing utilities from the ``lucid`` class.

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics
import os
import tempfile

###############################################################################
# Launch Prime server and instantiate the lucid class
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Launch an instance of Ansys Prime Server.
# Connect the PyPrimeMesh client and get the model.
# Instantiate meshing utilities from the ``lucid`` class.

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Define CAD file and mesh settings
# ~~~~~~~~~~~~~~~
# Define the number of layers per solid 
# Define the size in mm of the quad-dominant mesh on the base size
# Define the path to the CAD file to be meshed

# Download the example CAD file using prime.examples function. Else, write the 
# path to the desired CAD file on your machine.
# .scdoc/.dsco/.pmdb/ are supported
cad_file=prime.examples.download_multi_layer_quad_mesh_pcb_pmdat()
layers_per_solid = 4 #number of hexa mesh layers in each solid
base_face_size = 0.5 #the surface mesh size in mm on the base face 
# Chose whether to display or not to Display the CAD/mesh at every stage 
display_intermediate_steps=True#Use True/False


###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Import the geometry into Prime server
# Use the WORKBENCH CadReaderRoute to ensure that the shared topology is kept.
# If you are using .scdoc/.dsco/.pmdb

mesh_util.read(file_name=cad_file)
# Use the following command to open .scdoc/.dsco/.pmdb
# mesh_util.read(
#     file_name = cad_file,
#     cad_reader_route = prime.CadReaderRoute.WORKBENCH)

###############################################################################
# Display the imported CAD in a PyVista window
# ~~~~~~~~~~~~~~~
if display_intermediate_steps:
    display = Graphics(model)
    display()

###############################################################################
# Define edge sizing constraints
# ~~~~~~~~~~~~~~~
# Set generic global sizing from 0.002mm and 2mm.
# Extract the the edges length from the named selections such as "edge_1_0.50_mm" (extract 0.5 mm length) or "edge_23_0.27_mm" (extract 0.27mm length).
# Assign, on each edge, a size equal to the edge's length divided by the pre-defined number of layers per solid.

model.set_global_sizing_params(prime.GlobalSizingParams(model,min=0.002,max=2.))
ids=[]
part = model.parts[0]
for label in part.get_labels():
    # Check whether the named selection's name starts with the string "edge"
    if label.startswith('edge'):
        # Extract the edge's length splitting its name at every "_" string 
        # and collect the second-last number
        length = float(label.split("_")[-2])
        soft_size_control = model.control_data.create_size_control(prime.SizingType.SOFT)
        soft_size_params = prime.SoftSizingParams(model = model,
                                                  max = length/layers_per_solid)
        soft_size_control.set_soft_sizing_params(soft_size_params)
        soft_size_scope = prime.ScopeDefinition(model,
                                              part_expression = part.name,
                                              entity_type = prime.ScopeEntity.FACEANDEDGEZONELETS,
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

# Instantiate the volume sweeper
sweeper = prime.VolumeSweeper(model)
# Define the parameters for stacker
stacker_params = prime.MeshStackerParams(
    model = model,
    direction = [0, 0, 1],# define the sweep direction for the mesh
    delete_base = True,# delete the base face in the end of stacker
    lateral_defeature_tolerance = 0.001,
    stacking_defeature_tolerance = 0.001,
    size_control_ids = ids)# list of control ids to be respected by the stacker

###############################################################################
# Setup, generate, and mesh the base face 
# ~~~~~~~~~~~~~~~
# Create a soft sizing control. 
# Assign the previously defined base_face_size to the soft sizing.
# Create the base face. 
# Mesh the base face.
# Display the base face.

# Setup the necessary parameters for the generation of the base face.
soft_size_control=model.control_data.create_size_control(prime.SizingType.SOFT)
soft_size_params = prime.SoftSizingParams(model = model,max=base_face_size)
soft_size_control.set_soft_sizing_params(soft_size_params)
soft_size_scope = prime.ScopeDefinition(model,part_expression=part.name,
                                    entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS)
soft_size_control.set_scope(soft_size_scope)
soft_size_control.set_suggested_name("b_f_size")

# Create the base face appending the the stacker mesh parameters.
createbase_results = sweeper.create_base_face(
    part_id = model.get_part_by_name(part.name).id,
    topo_volume_ids = model.get_part_by_name(part.name).get_topo_volumes(),
    params=stacker_params)
base_faces = createbase_results.base_face_ids
model.get_part_by_name(part.name).add_labels_on_topo_entities(["base_faces"], base_faces)
scope = prime.ScopeDefinition(model=model, label_expression="base_faces")
base_scope = prime.lucid.SurfaceScope(
    entity_expression = "base_faces",
    part_expression = part.name,
    scope_evaluation_type = prime.ScopeEvaluationType.LABELS)

# Generate the surface mesh on the base face.
mesh_util_controls = mesh_util.surface_mesh_with_size_controls(
                                                        size_control_names="b_f_size", 
                                                        scope=base_scope, 
                                                        generate_quads=True)

###############################################################################
# Display the meshed base face in a PyVista window
# ~~~~~~~~~~~~~~~

if display_intermediate_steps:
    display()

###############################################################################
# Stack the base face using the volume sweeper.
# ~~~~~~~~~~~~~~~
# Use volume sweeper to stack the base face along the previously-defined sweep direction.
# Include the previously-defined stacker parameters.
# Display the final volume mesh.

stackbase_results = sweeper.stack_base_face(
    part_id = model.get_part_by_name(part.name).id,
    base_face_ids = base_faces,
    topo_volume_ids = model.get_part_by_name(part.name).get_topo_volumes(),
    params = stacker_params)

###############################################################################
# Display the final PCB mesh in a PyVista window
# ~~~~~~~~~~~~~~~

if display_intermediate_steps:
    display()

###############################################################################
# Setup the zone naming before the mesh output
# ~~~~~~~~~~~~~~~
# Delete the unnecessary topo entities.
# Name the walls of "solid" as "wall_solid" (ex if the solid's name is "A", the walls surrounding the solid will be named "wall_A").
# Convert the labels to mesh zones.
 
part.delete_topo_entities(params = prime.DeleteTopoEntitiesParams(
                                                            model,
                                                            delete_geom_zonelets=True,
                                                            delete_mesh_zonelets=False))
for volume in part.get_volumes():
    volume_zone_name = "wall_"+model.get_zone_name(part.get_volume_zone_of_volume(volume))
    label_zonelets = part.get_face_zonelets_of_volumes([volume])
    part.add_labels_on_zonelets([volume_zone_name], label_zonelets)
mesh_util_create_zones = mesh_util.create_zones_from_labels()

###############################################################################
# Mesh output
# ~~~~~~~~~~~~~~~~
# Create a temporary folder and use it to output the mesh in .cas format.

# with tempfile.TemporaryDirectory() as temp_folder:
#     mesh_file = os.path.join(temp_folder, "multi_layer_quad_mesh_pcb.cas")
#     mesh_util.write(mesh_file)
#     assert os.path.exists(mesh_file)
#     print("\nExported file:\n", mesh_file)

mesh_util.write('D:/prime_test_pcb_mesh.cas')

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
