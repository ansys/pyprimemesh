.. _ref_index_lucid:

*****************************************
Common meshing tasks and the Lucid module
*****************************************

The :mod:`lucid <ansys.meshing.prime.lucid>` module defines high-level methods to abstract
and simplify common meshing tasks. Methods contained in this module are intended to demonstrate
how the low-level APIs can be combined to execute meshing workflows flexibly and with minimal
need for understanding PyPrimeMesh-specific concepts. The methods use global automatic defaults
where possible to reduce effort in creating general purpose operations.

Many common meshing tasks and workflows can be tackled easily using the functions provided.  

Here is an example of meshing the mixing elbow case for a fluid flow analysis:

.. code-block:: python

    from ansys.meshing import prime

    # Start and connect to an Ansys Prime Server instance
    prime_client = prime.launch_prime()
    model = prime_client.model

    # Instantiate the lucid class
    mesh_util = prime.lucid.Mesh(model=model)

    # Read the geometry
    mesh_util.read("mixing_elbow.scdoc")

    # Mesh the geometry with a poly prism mesh
    mesh_util.surface_mesh(min_size=5, max_size=20)

    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_surface_expression="* !inlet !outlet",
        prism_layers=3,
    )

    # Prepare and write the model for the Fluent solver
    mesh_util.create_zones_from_labels()
    mesh_util.write("mixing_elbow.cas")

