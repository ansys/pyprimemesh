{% if obj.display %}

{# ----------------- Start macros definition for tab item ------------------#}
{% macro tab_item_from_objects_list(objects_list, title="") -%}

  .. tab-item:: {{ title }}

      .. list-table::
          :header-rows: 0
          :widths: auto

          {% for obj in objects_list %}
          * - :py:attr:`~{{ obj.name }}`
            - {{ obj.summary }}
          {% endfor %}
{%- endmacro %}

{# ------------------------ End macros definition for tab ------------------- #}

{# ----------------- Start macros definition for autosummary -----------------#}

{% macro autosummary_section(title, members) -%}

{{ title }}
{{ "-" * title | length }}

.. autoapisummary::

    {% for member in members %}
    {{ member.id }}
    {% endfor %}

{%- endmacro %}
{# ------------------ End macros definition for autosummary --------------- #}

{# ----------------- Start macros definition for headers -----------------#}

{% macro render_members_section(title, members) -%}

{{ title }}
{{ "-" * title | length }}

    {% for member in members %}
{{ member.render() }}
    {% endfor %}

{%- endmacro %}
{# ------------------ End macros definition for headers --------------- #}


    {% if is_own_page %}
:class:`{{ obj.name }}`
========={{ "=" * obj.name | length }}

    {% endif %}
    {% set visible_children = obj.children|selectattr("display")|list %}
    {% set own_page_children = visible_children|selectattr("type", "in", own_page_types)|list %}
    {% if is_own_page and own_page_children %}
.. toctree::
   :hidden:

        {% for child in own_page_children %}
    {{ child.short_name }}<{{ child.include_path }}>
        {% endfor %}

    {% endif %}

.. py:{{ obj.type }}:: {% if is_own_page %}{{ obj.id }}{% else %}{{ obj.short_name }}{% endif %}{% if obj.args %}({{ obj.args }}){% endif %}

    {% for (args, return_annotation) in obj.overloads %}
      {{ " " * (obj.type | length) }}   {{ obj.short_name }}{% if args %}({{ args }}){% endif %}

    {% endfor %}
    {% if obj.bases %}
      {% if "show-inheritance" in autoapi_options %}

   Bases: {% for base in obj.bases %}{{ base|link_objs }}{% if not loop.last %}, {% endif %}{% endfor %}
      {% endif %}


      {% if "show-inheritance-diagram" in autoapi_options and obj.bases != ["object"] %}
   .. autoapi-inheritance-diagram:: {{ obj.obj["full_name"] }}
      :parts: 1
         {% if "private-members" in autoapi_options %}
      :private-bases:
         {% endif %}

      {% endif %}
    {% endif %}
    {% if obj.docstring %}

   {{ obj.docstring|indent(3) }}
    {% endif %}
    {% set this_page_children = visible_children|rejectattr("type", "in", own_page_types)|list %}
    {% set visible_abstract_methods = [] %}
    {% set visible_constructor_methods = [] %}
    {% set visible_instance_methods = [] %}
    {% set visible_special_methods = [] %}
    {% set visible_static_methods = [] %}
    {% set visible_properties = this_page_children|selectattr("type", "equalto", "property")|list %}
    {% set visible_attributes = this_page_children|selectattr("type", "equalto", "attribute")|list %}
    {% set all_visible_methods = this_page_children|selectattr("type", "equalto", "method")|list %}
    {% if all_visible_methods %}
        {% for element in all_visible_methods %}
        {% if "abstractmethod" in element.properties %}
            {% set _ = visible_abstract_methods.append(element) %}

        {% elif "staticmethod" in element.properties %}
            {% set _ = visible_static_methods.append(element) %}

        {% elif "classmethod" in element.properties or element.name in ["__new__", "__init__"] %}
            {% set _ = visible_constructor_methods.append(element) %}

        {% elif element.name.startswith("__") and element.name.endswith("__") and element.name not in ["__new__", "__init__"] %}
            {% set _ = visible_special_methods.append(element) %}

        {% else %}
            {% set _ = visible_instance_methods.append(element) %}
        {% endif %}
        {% endfor %}
    {% endif %}

    {% if this_page_children %}

.. py:currentmodule:: {{ obj.short_name }}
{# ------------------------- Begin tab-set definition ----------------------- #}

Overview
--------

.. tab-set::

        {% if visible_abstract_methods %}
   {{ tab_item_from_objects_list(visible_abstract_methods, "Abstract methods") }}
        {% endif %}

        {% if visible_constructor_methods %}
   {{ tab_item_from_objects_list(visible_constructor_methods, "Constructors") }}
        {% endif %}

        {% if visible_instance_methods %}
   {{ tab_item_from_objects_list(visible_instance_methods, "Methods") }}
        {% endif %}

        {% if visible_properties %}
   {{ tab_item_from_objects_list(visible_properties, "Properties") }}
        {% endif %}

        {% if visible_attributes %}
   {{ tab_item_from_objects_list(visible_attributes, "Attributes") }}
        {% endif %}

        {% if visible_static_methods %}
   {{ tab_item_from_objects_list(visible_static_methods, "Static methods") }}
        {% endif %}

        {% if visible_special_methods %}
   {{ tab_item_from_objects_list(visible_special_methods, "Special methods") }}
        {% endif %}

    {% endif %}
{# ---------------------- End class tabset -------------------- #}

{# ---------------------- Begin class details -------------------- #}

Import detail
-------------
{% set split_parts = obj.obj["full_name"].split('.') %}
{% set joined_parts = '.'.join(split_parts[:-1]) %}

.. code-block:: python

    from {{ joined_parts }} import {{ obj["short_name"] }}

    {% if visible_properties %}
{{ render_members_section("Property detail", visible_properties) }}
    {% endif %}

    {% if visible_attributes %}
{{ render_members_section("Attribute detail", visible_attributes) }}
    {% endif %}

    {% if all_visible_methods %}
{{ render_members_section("Method detail", all_visible_methods) }}
    {% endif %}

    {% if is_own_page and own_page_children %}
        {% set visible_attributes = own_page_children|selectattr("type", "equalto", "attribute")|list %}

        {% if visible_attributes %}
{{ autosummary_section("Attributes", visible_attributes) }}
        {% endif %}
        {% set visible_exceptions = own_page_children|selectattr("type", "equalto", "exception")|list %}

        {% if visible_exceptions %}
{{ autosummary_section("Exceptions", visible_exceptions) }}
        {% endif %}
        {% set visible_classes = own_page_children|selectattr("type", "equalto", "class")|list %}

        {% if visible_classes %}
{{ autosummary_section("Classes", visible_classes) }}

        {% endif %}
        {% set visible_methods = own_page_children|selectattr("type", "equalto", "method")|list %}

        {% if visible_methods %}
{{ autosummary_section("Methods", visible_methods) }}
        {% endif %}
    {% endif %}

{# ---------------------- End class details -------------------- #}
{% endif %}
