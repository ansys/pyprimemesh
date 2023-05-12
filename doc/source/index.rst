PyPrimeMesh documentation |version|
===================================

.. toctree::
   :hidden:
   :maxdepth: 3

   getting_started/index
   user_guide/index
   examples/index
   api/index
   contributing/index

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
       _ = io.read_pmdat(r"E:\Temp\box.pmdat", prime.FileReadParams(model=model))
