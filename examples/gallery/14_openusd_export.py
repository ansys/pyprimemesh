# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
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

"""Load an F1 rear wing example mesh and export it as OpenUSD.

This example reuses the generic F1 rear wing STL files used by the
generic rear wing gallery example (download helpers in ``prime.examples``).

Steps
-----
1. Launch Prime.
2. Import F1 rear wing geometry.
3. Create a quick wrapped surface to ensure meshed faces exist.
4. Build USD geometry from the same connectivity source used for PolyData.
5. Export an HTML viewer using a temporary USD file.
"""

import webbrowser
from pathlib import Path

from ansys.meshing.prime.core.mesh_usd_io import export_usd_viewer_html


def _count_entities(usd_geom):
    """Return a compact count of exported entities."""
    n_faces = sum(len(p.get("faces", [])) for p in usd_geom.values())
    n_edges = sum(len(p.get("edges", [])) for p in usd_geom.values())
    n_ctrlpts = sum(len(p.get("ctrlpts", [])) for p in usd_geom.values())
    n_splinesurf = sum(len(p.get("splinesurf", [])) for p in usd_geom.values())
    return n_faces, n_edges, n_ctrlpts, n_splinesurf


def main():
    import ansys.meshing.prime as prime

    """Run F1 rear wing USD export example."""
    prime_client = prime.launch_prime()
    model = prime_client.model

    try:
        # sphinx_gallery_tags = ["Structural", "Shell", "Quad", "Connect"]

        ###############################################################################
        # Launch Ansys Prime Server
        # ~~~~~~~~~~~~~~~~~~~~~~~~~
        # Import all necessary modules.
        # Launch an instance of Ansys Prime Server.
        # Connect the PyPrimeMesh client and get the model.

        from ansys.meshing import prime
        from ansys.meshing.prime.graphics import PrimePlotter

        prime_client = prime.launch_prime()
        model = prime_client.model

        ###############################################################################
        # Import CAD geometry
        # ~~~~~~~~~~~~~~~~~~~
        # Download the bracket geometry (FMD) file exported by SpaceClaim.
        # Import the CAD geometry.
        # Create the part per the CAD model for the topology-based connection.

        # For Windows OS users, scdoc is also available:
        # bracket_file = prime.examples.download_bracket_scdoc()

        bracket_file = prime.examples.download_bracket_fmd()

        file_io = prime.FileIO(model)
        file_io.import_cad(
            file_name=bracket_file,
            params=prime.ImportCadParams(
                model=model,
                length_unit=prime.LengthUnit.MM,
                part_creation_type=prime.PartCreationType.MODEL,
            ),
        )

        ###############################################################################
        # Review the part
        # ~~~~~~~~~~~~~~~
        # Get the part summary.
        # Display the model to show edges by connection.
        # Use keyboard shortcuts to switch between
        # the surface (``s``) and wireframe (``w``) representations.
        # Color code for edge connectivity:
        #
        # - Red: free
        # - Black: double
        # - Purple: triple

        part = model.get_part_by_name('bracket_mid_surface-3')
        part_summary_res = part.get_summary(prime.PartSummaryParams(model, print_mesh=False))
        print(part_summary_res)

        display = PrimePlotter()
        display.add_model(model)
        display.show()

        ###############################################################################
        # Connection
        # ~~~~~~~~~~
        # Initialize the connection tolerance and other parameters. (The connection
        # tolerance is smaller than the target element size.)
        # Scaffold the topofaces, topoedges, or both with connection parameters.

        # Target element size
        element_size = 0.5

        params = prime.ScaffolderParams(
            model,
            absolute_dist_tol=0.1 * element_size,
            intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
            constant_mesh_size=element_size,
        )

        # Get existing topoface or topoedge IDs
        faces = part.get_topo_faces()
        beams = []

        scaffold_res = prime.Scaffolder(model, part.id).scaffold_topo_faces_and_beams(
            topo_faces=faces, topo_beams=beams, params=params
        )
        print(scaffold_res)

        ###############################################################################
        # Surface mesh
        # ~~~~~~~~~~~~
        # Initialize surface meshing parameters.
        # Mesh topofaces with the constant size and generate quad elements.

        surfer_params = prime.SurferParams(
            model=model,
            size_field_type=prime.SizeFieldType.CONSTANT,
            constant_size=element_size,
            generate_quads=True,
        )

        surfer_result = prime.Surfer(model).mesh_topo_faces(
            part.id, topo_faces=faces, params=surfer_params
        )

        # Display the mesh
        pl = PrimePlotter()
        pl.plot(model, update=True)
        pl.show()

        usd_geom = model.as_usd(update=True)
        n_faces, n_edges, n_ctrlpts, n_splinesurf = _count_entities(usd_geom)
        print(
            f"Prepared USD geometry: faces={n_faces}, edges={n_edges}, "
            f"ctrlpts={n_ctrlpts}, splinesurf={n_splinesurf}"
        )

        out_dir = Path.cwd() / "examples" / "gallery" / "_generated"
        out_dir.mkdir(parents=True, exist_ok=True)

        usd_path = out_dir / "f1_rear_wing_mesh.usd"
        html_path = export_usd_viewer_html(
            usd_geom, usd_path, out_dir / "f1_rear_wing_mesh_viewer.html"
        )

        print(f"Viewer page generated at: {html_path}")
        print(f"USD file generated at: {usd_path}")
        print("Controls: left-drag orbit, right-drag pan, mouse wheel zoom.")
        webbrowser.open(html_path.resolve().as_uri())
    finally:
        prime_client.exit()


if __name__ == "__main__":
    main()
