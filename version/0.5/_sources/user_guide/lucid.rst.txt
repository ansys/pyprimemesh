.. _ref_index_lucid:

*****************************************
Common meshing tasks and the Lucid module
*****************************************

The `lucid <https://prime.docs.pyansys.com/version/stable/api/_autosummary/ansys.meshing.prime.lucid.html>` module defines high-level methods to abstract
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

Remesh surface using the Lucid module
-------------------------------------

This code shows how to remesh the surface using the Lucid module:

.. code-block:: python

    import ansys.meshing.prime as prime

    prime_client = prime.launch_prime()
    model = prime_client.model

    # Instantiate the Lucid module
    mesh_util = prime.lucid.Mesh(model)

    # Import CAD (STL) file
    input_file = r"D:/Examples/simple-bracket-holes.stl"
    mesh_util.read(input_file)

Surface wrapping using the ``lucid.Mesh`` class
-----------------------------------------------

This example shows you surface wrapping using lucid to get the desired surface mesh results:

.. code:: python

   model = prime_client.model
   mesh_util = prime.lucid.Mesh(model)
   input_file = r"D:/PyPrimeMesh/cylinder_with_flange.pmdat"
   mesh_util.read(input_file)

   # Create size control for remeshing
   size_control2 = model.control_data.create_size_control(
       sizing_type=prime.SizingType.HARD
   )
   size_control2.set_hard_sizing_params(prime.HardSizingParams(model=model, min=0.8))
   size_control2.set_scope(prime.ScopeDefinition(model=model))

   # Wrap and remesh the input parts
   mesh_util.wrap(
       min_size=0.2,
       max_size=1.0,
       input_parts="flange,pipe",
       use_existing_features=True,
       recompute_remesh_sizes=True,
       remesh_size_controls=[size_control2],
   )


   # Surface mesh the geometry with curvature sizing
   # Set minimum and maximum sizing to use for curvature refinement
   mesh_util.surface_mesh(min_size=0.27, max_size=5.5)

Prism controls for polyhedral mesh using the Lucid module
---------------------------------------------------------

This example shows how to generate poly prism method using the Lucid module:

.. code-block:: python

    # Volume mesh with polyhedral elements
    # Set prism layers parameter for boundary layer refinement
    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_layers=5,
        prism_surface_expression="* !inlet !outlet",
    )
