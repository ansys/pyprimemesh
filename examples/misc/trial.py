import os
import tempfile
import numpy as np
import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics.plotter import PrimePlotter
import pyvista as pv

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

mesh_util.read(file_name=prime.examples.download_block_model_fmd())

print(model)

mesh_util.surface_mesh(min_size=8.0)

part = model.parts[0]

mesh_util.volume_mesh(quadratic=True, volume_fill_type=prime.VolumeFillType.TET)

prime.SurfaceUtilities(model).project_topo_faces_on_geometry(
    part.get_topo_faces(),
    prime.ProjectOnGeometryParams(
        model, project_on_facets_if_cadnot_found=True, project_only_mid_nodes=False
    ),
)

model_pd = model.as_polydata()

for part_id, part_polydata in model_pd.items():
    if "faces" in part_polydata.keys():
        for face_mesh_part, face_mesh_info in part_polydata["faces"]:
            zone_name = face_mesh_info.zone_name
            print(face_mesh_part.mesh)

display = PrimePlotter()
display.plot(model, update=True)
display.show()

prime_client.exit()