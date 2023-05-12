"""
.. _ref_how_to_add_an_example_reference_key:

Adding a new example
--------------------
This example demonstrates how to add new examples and serves as a template
that you can use in their creation.

A block comment must be included at the top of any new example. Each example
must have a reference tag in this format:

``.. _ref_my_example:``

The ``.. _ref_`` is necessary. Everything that follows is your reference tag. As
convention, we keep all references all in ``snake_case``.

This section should give a brief overview of what the example is about and/or demonstrates.
The title should be changed to reflect the topic your example covers.

New examples should be added as python scripts to:

``pyprimemesh/examples/gallery``

.. note::
   Avoid creating new folders unless absolutely necessary. If in doubt put the example
   in the folder closest to what it is doing and its precise location can be advised
   on in the pull request. If you *must* create a new folder, make sure to add a
   ``README.txt`` containing a reference, a title and a single sentence description of the folder.
   Otherwise the new folder will be ignored by Sphinx.

Example file names should be in the format:

``example_name.py``

.. note::
    Supporting input files for the example, such as CAD or mesh file assets, must be either original
    content or have appropriate licensing and ownership permissions from their respective owners. If
    the input files are used within the example script provided they must be capable of running in
    the CI pipeline. This means that only files that can be read using the native file formats and
    CAD readers can be used in the scripted examples.

The recommended data formats to be included in the example are:

* .pmdat
* .fmd
* .scdoc or .dsco (supported on Windows OS)

Supporting input files should be added in:

`Github Example Data Repository <https://github.com/pyansys/example-data/tree/master/pyprimemesh>`_

Referencing files as enum and creating download function in:

``pyprimemesh/examples.py``

Also adding download function to:

``pyprimemesh/examples/__init__.py``

After this preamble is the first code block:
"""

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics

# Start Ansys Prime Server instance and get client model
prime_client = prime.launch_prime()
model = prime_client.model

# Your code goes here...
mesh_util = prime.lucid.Mesh(model=model)

# For Windows OS users scdoc is also available:
# mixing_elbow = prime.examples.download_elbow_scdoc()
mixing_elbow = prime.examples.download_elbow_fmd()
mesh_util.read(mixing_elbow)
print(model)

###############################################################################
# Section Title
# ~~~~~~~~~~~~~
# Code blocks can be broken up with text "sections" which are interpreted as
# restructured text.
#
# This will also be translated into a markdown cell in the generated jupyter notebook.
# Sections can contain any information you may have regarding the example
# such as step-by-step comments or notes regarding motivations etc.
#
# As in jupyter notebooks, if code is left unassigned at the end of a code block
# (as with ``model`` in the previous block) the output will be generated and
# printed to the screen according to its ``__repr__``.  Otherwise, you can use
# ``print()`` to output the ``__str__``.

# more code...
mesh_util.surface_mesh(min_size=5, max_size=20)
mesh_util.volume_mesh(
    volume_fill_type=prime.VolumeFillType.POLY,
    prism_surface_expression="* !inlet !outlet",
    prism_layers=3,
)

###############################################################################
# Rendering graphics
# ~~~~~~~~~~~~~~~~~~
# If you display graphics the result will be auto-generated and
# rendered in the page. Like so:
display = Graphics(model)
display()

###############################################################################
# Making a Pull Request
# ~~~~~~~~~~~~~~~~~~~~~
# Once your example is complete and you've verified builds locally, you can make a
# pull request (PR).  Branches containing examples should be prefixed with `doc/`
# as per the branch naming conventions found here: :ref:`ref_index_contributing`.
#
# Note that you only need to create the python source example (.py).  The jupyter
# notebook, the example html and the demo script will all be auto-generated via ``sphinx-gallery``.

###############################################################################
# Stopping Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
prime_client.exit()
