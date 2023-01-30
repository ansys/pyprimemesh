.. _ref_index_graphics:

**********************************
Interactive graphics using PyVista
**********************************
PyPrimeMesh provides support for interactive graphical visualisation using `PyVista <https://docs.pyvista.org/>`_
if this package is installed as a dependency.

This code shows how to display the model using the :class:`Graphics <ansys.meshing.prime.graphics>` class:

.. code:: pycon

    >>> from ansys.meshing.prime.graphics import Graphics
    >>> import ansys.meshing.prime as prime
    >>> display = Graphics(model)
    >>> display()


.. figure:: ../images/graphics.png
    :width: 400pt
    :align: center

    **Entire model displayed**

Using the :class:`ScopeDefinition <ansys.meshing.prime.ScopeDefinition>` class allows
you to limit the display to particular regions of the model:

.. code:: pycon

    >>> # display the first part only
    >>> display(scope=prime.ScopeDefinition(model, part_expression=model.parts[0].name))


.. figure:: ../images/graphics_part.png
    :width: 400pt
    :align: center

    **Single part displayed**

Selections can be made of displayed objects. If selections in the window are made,
information about them can be printed to the console. Selections can also be hidden.

These graphics buttons are provided to help navigate the model and to
carry out basic verifications:

.. figure:: ../images/graphics_buttons(2).png
    :width: 200pt
    :align: center

    **Graphics buttons**
