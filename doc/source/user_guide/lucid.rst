.. _ref_index_lucid:

****************************************
Common Meshing Tasks and the Lucid class
****************************************

The :class:`Lucid <ansys.meshing.prime.lucid>` class defines high level methods to abstract and simplify common meshing tasks.  
Methods contained here are intended to demonstrate how the low level API’s can be combined to execute meshing workflows flexibly 
and with minimal need for user understanding of Ansys Prime specific concepts.  They use global automatic defaults where possible to 
reduce the user effort in creating general purpose operations. 

Many common meshing tasks and workflows can be tackled easily using the functions provided.  

Below is an example of meshing the mixing elbow case for fluid flow analysis:

.. code:: python
    
    >>> # Start and connect to a Prime server
    
    >>> from ansys.meshing import prime
    >>> prime_client = prime.launch_prime()
    >>> model = prime_client.model
    
    >>> # Instantiate the lucid class
    
    >>> mesh_util = prime.lucid.Mesh(model=model)
    
    >>> # Read the geometry
    
    >>> mesh_util.read("mixing_elbow.scdoc")
    
    >>> # Mesh the geometry with a poly prism mesh
    
    >>> mesh_util.surface_mesh(min_size=5, max_size=20)
    >>> mesh_util.volume_mesh(volume_fill_type=prime.VolumeFillType.POLY,
    >>>     prism_surface_expression="* !inlet !outlet",
    >>>     prism_layers=3,
    >>> )
    
    >>> # Prepare and write the model for the Fluent solver
    
    >>> mesh_util.create_zones_from_labels("inlet,outlet")
    >>> mesh_util.write("mixing_elbow.cas")


