.. vale off

{% set excluded_attrs = ['real', 'imag', 'numerator', 'denominator'] %}

{% set excluded_methods = ['bit_length', 'conjugate', 'from_bytes', 'to_bytes', 'bit_count', 'as_integer_ratio', 'is_integer'] %}

{{ name | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   {% block methods %}
   {% if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
      :toctree:

   {% for item in methods %}
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
      {% if item not in excluded_attrs %}{{ name }}.{{ item }}{% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}

.. minigallery::
    :add-heading: Examples using {{ objname }}

    {{ fullname }}

.. vale on
