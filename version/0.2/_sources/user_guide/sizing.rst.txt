.. _ref_index_sizing:

******
Sizing
******

PyPrimeMesh provides various sizing controls to help you refine your mesh to obtain the desired accuracy while meshing.


--------------
Sizing Control
--------------

When you mesh a model, you expect the mesh size to satisfy specific requirements at various locations in the mesh to provide accurate results.
You must use optimal sizes while meshing to achieve maximum simulation accuracy at minimum computational cost.
PyPrimeMesh specifies the sizing requirements using sizing controls. The sizing controls in PyPrimeMesh have the following:

* Scope

* Maximum rate of change of size

* Range within which the sizes should be, on or within the scope


The :class:`SizingType <ansys.meshing.prime.SizingType>` class offers various sizing control types to define sizing requirements:

 * Curvature

 * Proximity

 * Hard

 * Soft

 * Meshed

 * Body of Influence


Curvature Sizing
^^^^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`CURVATURE <ansys.meshing.prime.SizingType.CURVATURE>`, sizes on the scope are based on the local curvature, with the size being small when the local curvature is large and vice versa. The :class:`CurvatureSizingParams <ansys.meshing.prime.CurvatureSizingParams>` is used to specify following parameters: min/max size, growth rate and normal angle.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.CURVATURE)
    size_control.set_curvature_sizing_params(
        prime.CurvatureSizingParams(
            model=model,
            min=0.2,
            max=2.0,
            growth_rate=1.2
        )
    )
    size_control.set_suggested_name("curv_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))

Proximity Sizing
^^^^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`PROXIMITY <ansys.meshing.prime.SizingType.PROXIMITY>`, sizes are based on the closeness of surfaces or edges specified in the scope. The :class:`ProximitySizingParams <ansys.meshing.prime.ProximitySizingParams>` is used to specify following parameters: min/max size, growth rate and the number of element per gap.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.PROXIMITY)
    size_control.set_proximity_sizing_params(
        prime.ProximitySizingParams(
            model=model,
            min=0.1,
            max=2.0,
            growth_rate=1.2,
            elements_per_gap=3.0
        )
    )
    size_control.set_suggested_name("prox_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))

Hard Sizing
^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`HARD <ansys.meshing.prime.SizingType.HARD>`, sizes on the scope are based on a uniform value while meshing. The :class:`HardSizingParams <ansys.meshing.prime.HardSizingParams>` is used to specify following parameters: minimum size and growth rate.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.HARD)
    size_control.set_hard_sizing_params(
        prime.HardSizingParams(
            model=model,
            min=0.2,
            growth_rate=1.2
        )
    )
    size_control.set_suggested_name("hard_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))

Soft Sizing
^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`SOFT <ansys.meshing.prime.SizingType.SOFT>`, sizes on the scope are based on a certain maximum value which should not exceed while meshing. The :class:`SoftSizingParams <ansys.meshing.prime.SoftSizingParams>` is used to specify following parameters: maximum size and growth rate.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.SOFT)
    size_control.set_soft_sizing_params(
        prime.SoftSizingParams(
            model=model,
            max=0.2,
            growth_rate=1.2
        )
    )
    size_control.set_suggested_name("soft_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))

Meshed Sizing
^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`MESHED <ansys.meshing.prime.SizingType.MESHED>`, sizes are based on existing local sizes. The :class:`MeshedSizingParams <ansys.meshing.prime.MeshedSizingParams>` class is used to specify growth rate.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.MESHED)
    size_control.set_meshed_sizing_params(
        prime.MeshedSizingParams(
            model=model,
            growth_rate=1.2
        )
    )
    size_control.set_suggested_name("meshed_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))

Body of Influence Sizing
^^^^^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`BOI <ansys.meshing.prime.SizingType.BOI>`, sizes inside a closed volume scope should not cross a certain maximum value. The :class:`BoiSizingParams <ansys.meshing.prime.BoiSizingParams>` is used to specify following parameters: maximum size and growth rate.

.. code:: python

    size_control = model.control_data.create_size_control(prime.SizingType.BOI)
    size_control.set_boi_sizing_params(
        prime.BoiSizingParams(
            model=model,
            max=20.0,
            growth_rate=1.2
        )
    )
    size_control.set_suggested_name("BOI_control")
    size_control.set_scope(prime.ScopeDefinition(model=model))


-----------
Size Fields
-----------

The :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class helps you to fetch the element size at a given location. The size field types available in PyPrimeMesh are: 

 * Geometric

 * Volumetric

 * Geodesic

 * Constant

 * Meshedgeodesic


Geometric size field
^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`GEOMETRIC <ansys.meshing.prime.SizeFieldType.GEOMETRIC>`, size field is computed based on the existing boundary sizes. Sizes can gradually increase from minimum size to maximum size based on the growth rate.

Volumetric size field
^^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`VOLUMETRIC <ansys.meshing.prime.SizeFieldType.VOLUMETRIC>`, size field is computed based on the size controls specified.

Geodesic size field
^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`GEODESIC <ansys.meshing.prime.SizeFieldType.GEODESIC>`, size field is computed on face nodes based on the size controls specified. Sizes are defined along a surface rather than the volume. Geodesic sizing enables you to confine sizes to surfaces and avoid problems like dead space refinement.

Constant size field
^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`CONSTANT <ansys.meshing.prime.SizeFieldType.CONSTANT>`, size field is computed based on the size controls specified.

Meshedgeodesic size field
^^^^^^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`MESHEDGEODESIC <ansys.meshing.prime.SizeFieldType.MESHEDGEODESIC>`, size field is computed using average mesh edge lengths and is diffused geodesical.
