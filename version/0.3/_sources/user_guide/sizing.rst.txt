.. _ref_index_sizing:

******
Sizing
******

PyPrimeMesh provides various sizing controls to help you refine your mesh to obtain the desired accuracy while meshing.


--------------
Sizing control
--------------

When you mesh a model, you expect the mesh size to satisfy specific requirements at various locations in the mesh
to provide accurate results. You must use optimal sizes while meshing to achieve maximum simulation accuracy at
minimum computational cost. PyPrimeMesh specifies the sizing requirements using these sizing controls:

* Scope

* Maximum rate of change of size

* Range within which the sizes should be on or within the scope


The :class:`SizingType <ansys.meshing.prime.SizingType>` class offers various sizing control types to define sizing requirements:

 * Curvature

 * Proximity

 * Hard

 * Soft

 * Meshed

 * Body of influence


Curvature sizing
^^^^^^^^^^^^^^^^

On the :class:`SizingType <ansys.meshing.prime.SizingType>` class, selecting the :attr:`CURVATURE <ansys.meshing.prime.SizingType.CURVATURE>`
parameter sizes based on the scope based on the local curvature. The size is small when the local curvature is large and vice versa.
This code shows how to use the :class:`CurvatureSizingParams <ansys.meshing.prime.CurvatureSizingParams>` class to specify
the minimum and maximum size, growth rate, and normal angle:

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.CURVATURE)
    size_control.set_curvature_sizing_params(
        prime.CurvatureSizingParams(model=model, min=0.2, max=2.0, growth_rate=1.2)
    )
    size_control.set_suggested_name("curv_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


Proximity sizing
^^^^^^^^^^^^^^^^

On the :class:`SizingType <ansys.meshing.prime.SizingType>` class, selecting the
:attr:`PROXIMITY <ansys.meshing.prime.SizingType.PROXIMITY>` parameter sizes based on the closeness of
the surfaces or edges specified in the scope. This code shows how to use the
:class:`ProximitySizingParams <ansys.meshing.prime.ProximitySizingParams>` class to specify the
minimum and maximum size, growth rate, and the number of element per gap:

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.PROXIMITY)
    size_control.set_proximity_sizing_params(
        prime.ProximitySizingParams(
            model=model, min=0.1, max=2.0, growth_rate=1.2, elements_per_gap=3.0
        )
    )
    size_control.set_suggested_name("prox_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


Hard sizing
^^^^^^^^^^^

On the :class:`SizingType <ansys.meshing.prime.SizingType>` class, selecting the
:attr:`HARD <ansys.meshing.prime.SizingType.HARD>` parameter sizes on the scope based on a uniform
value while meshing. This code shows how to use the :class:`HardSizingParams <ansys.meshing.prime.HardSizingParams>`
class to specify the minimum size and growth rate.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.HARD)
    size_control.set_hard_sizing_params(
        prime.HardSizingParams(model=model, min=0.2, growth_rate=1.2)
    )
    size_control.set_suggested_name("hard_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


Soft sizing
^^^^^^^^^^^

On the :class:`SizingType <ansys.meshing.prime.SizingType>` class, selecting the
:attr:`SOFT <ansys.meshing.prime.SizingType.SOFT>` parameter sizes on the scope based on a
certain maximum value that should not be exceeded while meshing. This code shows how
to use the :class:`SoftSizingParams <ansys.meshing.prime.SoftSizingParams>` class to specify
the maximum size and growth rate:

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.SOFT)
    size_control.set_soft_sizing_params(
        prime.SoftSizingParams(model=model, max=0.2, growth_rate=1.2)
    )
    size_control.set_suggested_name("soft_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


Meshed sizing
^^^^^^^^^^^^^

On the :class:`SizingType <ansys.meshing.prime.SizingType>` class, selecting the
:attr:`MESHED <ansys.meshing.prime.SizingType.MESHED>` parameter sizes based on existing local sizes.
This example shows how to use The :class:`MeshedSizingParams <ansys.meshing.prime.MeshedSizingParams>`
class to specify the growth rate:

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.MESHED)
    size_control.set_meshed_sizing_params(
        prime.MeshedSizingParams(model=model, growth_rate=1.2)
    )
    size_control.set_suggested_name("meshed_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


Body of influence sizing
^^^^^^^^^^^^^^^^^^^^^^^^

On the :class:`SizingType <ansys.meshing.prime.SizingType>` class, selecting The
:attr:`BOI <ansys.meshing.prime.SizingType.BOI>` parameter sizes inside a closed volume scope
that is not to exceed a certain maximum value. This code shows how to use the
:class:`BoiSizingParams <ansys.meshing.prime.BoiSizingParams>` class to specify the maximum size and growth rate.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.BOI)
    size_control.set_boi_sizing_params(
        prime.BoiSizingParams(model=model, max=20.0, growth_rate=1.2)
    )
    size_control.set_suggested_name("BOI_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


-----------
Size fields
-----------

The :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class helps you to fetch the element size
at a given location. These size field types are available in PyPrimeMesh: 

 * Geometric

 * Volumetric

 * Geodesic

 * Constant

 * Meshedgeodesic


Geometric size field
^^^^^^^^^^^^^^^^^^^^

On the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class, selecting the
:attr:`GEOMETRIC <ansys.meshing.prime.SizeFieldType.GEOMETRIC>` parameter computes the size field
based on existing boundary sizes. Sizes can gradually increase from the minimum size to the
maximum size based on the growth rate.

Volumetric size field
^^^^^^^^^^^^^^^^^^^^^

On the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class, selecting the
:attr:`VOLUMETRIC <ansys.meshing.prime.SizeFieldType.VOLUMETRIC>` parameter computes the size field
based on the size controls specified.

Geodesic size field
^^^^^^^^^^^^^^^^^^^

On the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class, selecting the
:attr:`GEODESIC <ansys.meshing.prime.SizeFieldType.GEODESIC>` parameter computes the size field
on face nodes based on the size controls specified. Sizes are defined along a surface rather than
the volume. Geodesic sizing enables you to confine sizes to surfaces and avoid problems like
dead space refinement.

Constant size field
^^^^^^^^^^^^^^^^^^^

On the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class, selecting the
:attr:`CONSTANT <ansys.meshing.prime.SizeFieldType.CONSTANT>` parameter computes the size field
based on the size controls specified.

Meshedgeodesic size field
^^^^^^^^^^^^^^^^^^^^^^^^^

On the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class, selecting the
:attr:`MESHEDGEODESIC <ansys.meshing.prime.SizeFieldType.MESHEDGEODESIC>` parameter computes
the size field using average mesh edge lengths and is diffused geodesical.
