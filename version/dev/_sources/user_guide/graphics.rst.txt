.. _ref_index_graphics:

**********************************
Interactive graphics using PyVista
**********************************
PyPrimeMesh provides support for interactive graphical visualisation using `PyVista <https://docs.pyvista.org/>`_
if this package is installed as a dependency.

This code shows how to display the model using the :class:`Graphics <ansys.meshing.prime.graphics>` class:

.. code-block:: pycon

    >>> from ansys.meshing.prime.graphics import PrimePlotter
    >>> import ansys.meshing.prime as prime
    >>> display = PrimePlotter()
    >>> display.plot(model)
    >>> display.show()


.. figure:: ../images/graphics.png
    :width: 400pt
    :align: center

    **Entire model displayed**

Using the :class:`ScopeDefinition <ansys.meshing.prime.ScopeDefinition>` class allows
you to limit the display to particular regions of the model:

.. code-block:: pycon

    >>> # display the first part only
    >>> display = PrimePlotter()
    >>> display.plot(
    ...     model, scope=prime.ScopeDefinition(model, part_expression=model.parts[0].name)
    ... )
    >>> display.show()


.. figure:: ../images/graphics_part.png
    :width: 400pt
    :align: center

    **Single part displayed**

Selections can be made of displayed objects. If selections in the window are made,
information about them can be printed to the console. Selections can also be hidden.

These graphics buttons are provided to help navigate the model and to
carry out basic verifications:

.. figure:: ../images/graphics_buttons.png
    :width: 300pt
    :align: center

    **Graphics buttons, in the order they appear on screen**

Several of these buttons cycle through more than two states, so hovering over one
shows what it is set to and what the next click does, such as ``Colouring by zone.
Click to colour by zonelet.`` The icon tells you which state you are in and the hover
text tells you where the next click takes you.

Coloring the display
====================
The color button cycles through the ways entities can be colored. The mode can also be
set from a script with ``ColorByType``:

.. code-block:: pycon

    >>> from ansys.meshing.prime.core.mesh import ColorByType
    >>> display = PrimePlotter()
    >>> display.add_model(model)
    >>> display.set_color_by_type(ColorByType.CONNECTIVITY)
    >>> display.show()

``ZONE``, ``ZONELET``, and ``PART`` give each zone, entity, or part its own color from a
palette, which tells entities apart but carries no meaning beyond that.

``CONNECTIVITY`` instead colors entities by how they connect to the rest of their part,
which is the quickest way to spot leaks, missing interfaces, and unintended sheet bodies
before meshing. Faces are colored by the number of volumes they bound:

.. list-table::
    :header-rows: 1
    :widths: 20 80

    * - Class
      - Meaning
    * - ``SURFACE``
      - Bounds no volume, such as a sheet body.
    * - ``BODY``
      - Bounds exactly one volume, so it is the outer skin of a solid body.
    * - ``SHARED``
      - Bounds two or more volumes, so it is an interface inside the part.

Edges keep the connectivity colors they are always drawn with, so free, double, and
multiply connected edges stay distinguishable in every mode, including while a face is
selected. The exact colors are given by ``FACE_CONNECTIVITY_COLORS`` and
``TOPO_EDGE_TYPE_COLORS`` in ``ansys.meshing.prime.core.mesh``.

Face connectivity is read from the volumes of each part, so it works for topology parts
and for mesh parts alike, and for topology parts that have since been meshed. It is
resolved the first time you select the connectivity mode rather than at display time,
which keeps the cost off models that never use it.

Showing the mesh
================
The show mesh button toggles the interior edges of the displayed faces. What those edges
are depends on whether a face carries a mesh:

- A meshed face shows its element edges, drawn in the theme edge color. These are shown
  by default.
- An unmeshed face shows the facets that approximate its CAD surface, drawn faintly so
  that tessellation is not mistaken for a real mesh. These are hidden by default.

The two follow opposite sides of the same button, because facets stand in for a mesh
that is not there. A CAD model therefore arrives with clean surfaces and reveals its
tessellation only when you ask for it, while a meshed model shows its elements straight
away. In a partly meshed model the button swaps between the two, which shows at a glance
which faces have been meshed.

The hover text follows what is on display, so it never offers something that is not
there. Where nothing is left unmeshed, whether it is topology or mesh, there is no
faceting to fall back on and the button reads as showing or hiding the mesh edges. Where
nothing is meshed, there are no mesh edges either, so it reads as showing the topology
or its CAD faceting. Where both are present, it swaps one for the other.

Choosing what a click selects
=============================
Faces and edges are both selectable, but an edge is thin and usually sits on the surface
of the face behind it, so a click near a shared boundary tends to reach whichever the
renderer happens to hit first. The selection button cycles the selection target so that
you can say what you are aiming at. The target can also be set from a script:

.. code-block:: pycon

    >>> from ansys.meshing.prime.core.mesh import SelectionTarget
    >>> display.set_selection_target(SelectionTarget.EDGES)

``BOTH`` leaves everything selectable, ``FACES`` clicks through edges, and ``EDGES``
clicks through faces. Only the entities in the target take part in hit testing, so a
face can no longer shadow the edge behind it.

Changing the target never clears what is already selected, so faces and edges can be
gathered into one selection by picking the faces you want, switching the target, and
then picking the edges.

Clipping the model
==================
The clip button cuts the model open with a plane you can drag and rotate, which is how
you look inside a closed volume or check a mesh on an internal face. Click it again to
show the whole model. The same is available from a script:

.. code-block:: pycon

    >>> display.set_clipping(True)

Clipping is applied when the model is drawn rather than to the model itself, so the
entities are unchanged: they keep their colors, they stay selectable, and picking a
face that has been cut still selects the whole face. Anything hidden stays hidden,
and turning clipping off restores the view exactly.

Resetting the display
=====================
The reset button returns the display to how the model was first drawn. Selections are
cleared, hidden entities come back, coloring returns to the default, edge display and
the selection target return to their opening state, any clipping plane is removed, and
the camera goes back to the view the model opened with. The same is available from a
script:

.. code-block:: pycon

    >>> display.reset_display()

The geometry itself is kept, so this is a way out of an unreadable display without
adding the model again. To discard the geometry as well, use
:meth:`PrimePlotter.clear() <ansys.meshing.prime.graphics.plotter.PrimePlotter.clear>`,
which empties the scene entirely.
