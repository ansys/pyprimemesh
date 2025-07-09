.. vale off

{% set excluded_attrs = ['real', 'imag', 'numerator', 'denominator'] %}

{% set excluded_methods = ['__init__', 'bit_length', 'conjugate', 'from_bytes', 'to_bytes', 'bit_count', 'as_integer_ratio', 'is_integer'] %}

{% set filtered_methods = methods | reject('in', excluded_methods) | list %}

{{ name | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   
   {% block methods %}
   {% if filtered_methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
      :toctree:

   {% for item in filtered_methods %}
      {% if item != '__init__' %}{{ name }}.{{ item }}{% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Attributes') }}

   .. autosummary::
      :toctree:
   {% for item in attributes %}
      {% if item not in excluded_attrs %}
      {{ name }}.{{ item }}
      {% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}

.. minigallery::
    :add-heading: Examples using {{ objname }}

    {{ fullname }}

.. vale on
