"""
.. _ref_how_to_add_an_example_reference_key:

Adding a New Gallery Example
----------------------------
This example demonstrates how to add new examples as well as being a template that can
be used in their creation.

This block comment should be included at the top of any new example. Each example
should have a reference tag/key in the form:

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

After this preamble is complete, the first code block begins.
"""

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics

# start Ansys Prime Server and get client model
prime_client = prime.launch_prime()
model = prime_client.model

# Your code goes here...
mesh_util = prime.lucid.Mesh(model=model)
example_file = prime.examples.download_elbow_fmd()
mesh_util.read(example_file)
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
# as per the branch naming conventions found here: :ref:`contributing`.
#
# Note that you only need to create the python source example (.py).  The jupyter
# notebook, the example html and the demo script will all be auto-generated via ``sphinx-gallery``.

###############################################################################
# Stopping Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
prime_client.exit()
