.. title:: PyPrimeMesh

PyPrimeMesh is a Python client library for the Ansys Prime Server. You are looking at the documentation for version |version|.

.. grid:: 1 2 3 3
    :gutter: 1 2 3 3
    :padding: 1 2 3 3

    .. grid-item-card:: Getting started :fa:`person-running`
        :link: getting_started/index
        :link-type: doc

        Learn how to run the Linux Docker container and how to
		launch and connect to the Ansys Prime Server.

    .. grid-item-card:: User guide :fa:`book-open-reader`
        :link: user_guide/index
        :link-type: doc

        Understand key concepts and approaches for creating and
		modifying meshes for use with various solvers.

    .. jinja:: main_toctree

        {% if build_api %}
        .. grid-item-card:: API reference :fa:`book-bookmark`
            :link: api/index
            :link-type: doc

            Understand PyPrimeMesh API endpoints, their capabilities,
            and how to interact with them programmatically.
        {% endif %}

        {% if build_examples %}
        .. grid-item-card:: Examples :fa:`scroll`
            :link: examples
            :link-type: doc

            Explore examples that show how to use PyPrimeMesh to
            perform many different types of operations.
        {% endif %}

    .. grid-item-card:: Contribute :fa:`people-group`
        :link: contributing
        :link-type: doc

        Learn how to contribute to the PyPrimeMesh codebase
        or documentation.


.. jinja:: main_toctree

    .. toctree::
       :hidden:
       :maxdepth: 3

       getting_started/index
       user_guide/index
       api/index
       examples
       contributing


Introduction
------------

PyPrimeMesh is part of the `PyAnsys <https://docs.pyansys.com>`_ effort to facilitate the use of Ansys technologies directly
from Python. PyPrimeMesh consists of various Python modules that help you to acquire geometry and
prepare surface and volume meshes for multiple solvers. Its primary package is ``ansys-meshing-prime``.

PyPrimeMesh enables you to perform these tasks: 

* Generate quad dominant and triangular surface meshes.
* Generate surface meshes with various sizing options like volumetric and constant.
* Generate volume meshes with linear and quadratic elements of various shapes like tetrahedra, polyhedra,
  hexcore, pyramids, and prisms.
* Generate volume meshes with a single process or distributed process.
* Check mesh quality to provide the best solution for the problem and improve predictive
  capabilities.
* Perform mesh diagnostics for free, multi-connected edges, self-intersection, and overlapping faces
  in the model.
* Modularize meshing algorithms, components, and services for easier reuse in other applications.
* Expose microservices and APIs for meshing operations to promote meshing workflow prototyping.
 
PyPrimeMesh integrates the meshing capabilities of Ansys Prime Server directly into client apps.
PyPrimeMesh provides a Python-friendly interface to drive the software that manages the
submission of low-level Prime commands, while exchanging data through high-performance gRPC
interfaces.

PyPrimeMesh enables you to serve the meshing needs of the industry, providing solutions to complex
issues. PyPrimeMesh, along with the general-purpose Python code, effortlessly manages your meshing needs.
PyPrimeMesh is open source. Contributions are welcome.

PyPrimeMesh features
--------------------

PyPrimeMesh consists of many robust APIs. Some APIs do many jobs when called once. Some APIs
do only one job when called. These APIs also enable you to query the model and allow you to
build complex models based on the underlying queries. PyPrimeMesh, which is easy to set up
and execute, has some distinct features: 

* Supports simple and complex models
* Supports CAD import
* Exports meshes in solver format
* Supports parallel processing, like distributed parallel and threaded parallel, and multiple servers
  driven from Python

Quick code
----------

Here is a brief example of how you use PyPrimeMesh:

To launch PyPrimeMesh, you use this code:

.. code-block:: python

   import ansys.meshing.prime as prime

   with prime.launch_prime() as prime_client:
       model = prime_client.model


To read a mesh file, you use this code:

.. code-block:: python

   import ansys.meshing.prime as prime

   with prime.launch_prime() as prime_client:
       model = prime_client.model

       io = prime.FileIO(model)
       res = io.read_pmdat(r"E:\Temp\box.pmdat", prime.FileReadParams(model=model))

Documentation and issues
------------------------

Documentation for the latest stable release of PyPrimeMesh is hosted at `PyPrimeMesh documentation
<https://prime.docs.pyansys.com/version/stable/>`_.

In the upper right corner of the documentation's title bar, there is an option for switching from
viewing the documentation for the latest stable release to viewing the documentation for the
development version or previously released versions.

You can also `view <https://cheatsheets.docs.pyansys.com/pyprimemesh_cheat_sheet.png>`_ or
`download <https://cheatsheets.docs.pyansys.com/pyprimemesh_cheat_sheet.pdf>`_ the
PyPrimeMesh cheat sheet. This one-page reference provides syntax rules and commands
for using PyPrimeMesh. 

On the `PyPrimeMesh Issues <https://github.com/ansys/pyprimemesh/issues>`_ page,
you can create issues to report bugs and request new features. On the `PyPrimeMesh Discussions
<https://github.com/ansys/pyprimemesh/discussions>`_ page or the `Discussions <https://discuss.ansys.com/>`_
page on the Ansys Developer portal, you can post questions, share ideas, and get community feedback. 

To reach the project support team, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.
