.. vale off

{{ fullname | escape | underline}}

.. currentmodule:: {{ fullname }}

{% block attributes %}
{% if attributes %}
.. autosummary::
   :toctree:
   :caption: Attributes

{% for item in attributes %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block functions %}
{% if functions %}
.. autosummary::
   :toctree:
   :caption: Functions

{% for item in functions %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block classes %}
{% if classes %}
.. autosummary:: 
   :toctree:
   :caption: Classes

{% for item in classes %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block exceptions %}
{% if exceptions %}
.. autosummary:: 
   :toctree:
   :caption: Classes

{% for item in exceptions %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block modules %}
{% if modules %}
.. autosummary::
   :toctree:
   :recursive:
   :caption: Modules
{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

.. vale on
