"""Sphinx documentation configuration file."""
import os
from datetime import datetime

import ansys.tools.visualization_interface as viz_interface
import pyvista
from ansys_sphinx_theme import ansys_favicon, get_version_match, pyansys_logo_black
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from sphinx_gallery.sorting import FileNameSortKey

from ansys.meshing.prime import __version__

viz_interface.DOCUMENTATION_BUILD = True

# Project information
project = 'ansys-meshing-prime'
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", default="nocname.com")

# HTML options
html_short_title = html_title = "PyPrimeMesh"
html_logo = pyansys_logo_black
html_theme = 'ansys_sphinx_theme'

html_favicon = ansys_favicon

# specify the location of your github repo
html_context = {
    "github_user": "ansys",
    "github_repo": "pyprimemesh",
    "github_version": "main",
    "doc_path": "doc/source",
}

# specify the location of your github repo
html_theme_options = {
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "check_switcher": False,
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "navigation_with_keys": False,
    "github_url": "https://github.com/ansys/pyprimemesh",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "collapse_navigation": True,
    "use_edit_page_button": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "icon_links": [
        {
            "name": "Support",
            "url": "https://github.com/ansys/pyprimemesh/discussions",
            "icon": "fa fa-comment fa-fw",
        },
    ],
    "ansys_sphinx_theme_autoapi": {
        "project": project,
        "keep_files": True,
        "add_toctree_entry": True,
        "package_depth": 5,
    },
    "cheatsheet": {
        "file": "cheatsheet/cheat_sheet.qmd",
        "title": "PyPrimeMesh cheat sheet",
        "version": __version__,
    },
}

# Sphinx extensions
extensions = [
    'sphinx.ext.autosummary',
    "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
    "jupyter_sphinx",
    "notfound.extension",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinxemoji.sphinxemoji",
    "sphinx_design",
    "pyvista.ext.viewer_directive",
    "ansys_sphinx_theme.extension.autoapi",
]
nbsphinx_execute = "always"

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.11", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True
numpydoc_use_plots = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    # "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}


# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

autosummary_generate = True
autosummary_imported_members = True
autosummary_ignore_module_all = False


# exclude_patterns = [
#    "examples/gallery_examples/example_template.rst" "examples/gallery_examples/mixing_elbow.rst"
# ]

# Enable screenshots for gallery for pyvista
pyvista.BUILDING_GALLERY = True

# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True

# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath("./images/"), "auto-generated/")
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

# Sphinx Gallery Options
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    # "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["../../examples"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples/gallery_examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # ignore mixing elbow and example template
    "ignore_pattern": "examples/other_examples",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "ansys-meshing-prime",
    "image_scrapers": (DynamicScraper(), "matplotlib"),
    "ignore_pattern": "flycheck*",
    "thumbnail_size": (350, 350),
}

supress_warnings = ["docutils"]


exclude_patterns = [
    "examples/**/*.ipynb",
    "examples/**/*.py",
    "examples/**/*.md5",
    "api/ansys/visualizer/index.rst",
]


BUILD_API = True
if not BUILD_API:
    exclude_patterns.append("autoapi")

BUILD_EXAMPLES = True
if not BUILD_EXAMPLES:
    exclude_patterns.append("examples/**")
    exclude_patterns.append("examples.rst")

jinja_contexts = {
    "main_toctree": {
        "build_api": BUILD_API,
        "build_examples": BUILD_EXAMPLES,
    }
}


def prepare_jinja_env(jinja_env) -> None:
    """Customize the jinja env.

    Notes
    -----
    See https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.Environment

    """
    jinja_env.globals["project_name"] = project


autoapi_prepare_jinja_env = prepare_jinja_env
