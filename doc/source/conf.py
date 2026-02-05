"""Sphinx documentation configuration file."""

import glob
import os
import subprocess
import sys
from datetime import datetime

# Set PRIME_MODE if not already set (to avoid warnings during doc build)
if "PRIME_MODE" not in os.environ:
    os.environ["PRIME_MODE"] = "GRPC_INSECURE"

os.environ["SPHINX_GALLERY_CONF_FORCE_FRESH"] = "0"

import ansys.tools.visualization_interface as viz_interface
import pyvista
from joblib import Parallel, delayed
from pyvista.plotting.utilities.sphinx_gallery import DynamicScraper
from sphinx_gallery.sorting import FileNameSortKey

from ansys.meshing.prime import __version__
from ansys_sphinx_theme import ansys_favicon, get_version_match, pyansys_logo_black

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
    "pyansys_tags": ["CAD", "Meshing"],
}

# specify the location of your github repo
html_theme_options = {
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
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
}

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
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
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinxemoji.sphinxemoji",
    "sphinx_design",
    # "pyvista.ext.viewer_directive",
    "sphinx_jinja",
]
nbsphinx_execute = "always"

# Sphinx-jinja contexts
jinja_contexts = {
    "main_toctree": {},
}

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


# Enable screenshots for gallery for pyvista
pyvista.BUILDING_GALLERY = True

# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True

# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath("./images/"), "auto-generated/")
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

# Sphinx Gallery Options
# Determine if running in CI/CD (Github Actions) or locally with containers
# CI/CD can handle parallel execution better, local container may have resource conflicts
is_ci_build = (
    os.getenv("PYPRIMEMESH_SPHINX_BUILD", "0") == "1" and os.getenv("CI", "false") == "true"
)
is_local_container_build = os.getenv("PYPRIMEMESH_LAUNCH_CONTAINER", "0") == "1" and not is_ci_build
gallery_parallel = 20 if is_ci_build else 1

# Print build configuration for debugging
print(f"Documentation build configuration:")
print(f"  CI/CD Build: {is_ci_build}")
print(f"  Local Container Build: {is_local_container_build}")
print(f"  Sphinx-Gallery Parallel Jobs: {gallery_parallel}")
print(f"  PYPRIMEMESH_SPHINX_BUILD: {os.getenv('PYPRIMEMESH_SPHINX_BUILD', 'not set')}")
print(f"  CI: {os.getenv('CI', 'not set')}")
print(f"  PYPRIMEMESH_LAUNCH_CONTAINER: {os.getenv('PYPRIMEMESH_LAUNCH_CONTAINER', 'not set')}")
print("")

sphinx_gallery_conf = {
    # convert rst to md for ipynb
    # "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["../../examples"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples/gallery_examples"],
    # Pattern to search for example files
    "filename_pattern": r"^(?!examples/other/).*\.py$",
    # ignore mixing elbow and example template
    "ignore_pattern": r"examples/other/|flycheck*",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": "api/_gallery_backreferences",
    # Modules for which function level galleries are created.  In
    "doc_module": ("ansys.meshing.prime"),
    "exclude_implicit_doc": {"ansys\\.meshing\\.prime\\._.*"},  # ignore private submodules
    "image_scrapers": (DynamicScraper(), "matplotlib"),
    "thumbnail_size": (350, 350),
    "parallel": gallery_parallel,
    "run_stale_examples": False,
    # Code to execute before each example in parallel subprocesses
    # This ensures PyVista knows it's building gallery documentation
    "first_notebook_cell": (
        "import os\n"
        "os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'\n"
        "os.environ['PYVISTA_OFF_SCREEN'] = 'true'"
    ),
}


def run_example(script_path):
    """Run a Python script and return its exit code.

    Parameters
    ----------
    script_path : str
        The path to the Python script to execute.

    Returns
    -------
    int
        The exit code of the script execution. 0 indicates success.
    """
    print(f"Running {script_path} ...")
    result = subprocess.run([sys.executable, script_path], capture_output=True)
    if result.returncode != 0:
        print(f"Error in {script_path}:\n{result.stderr.decode()}")
    return result.returncode


def run_all_examples_in_parallel():
    """Find and run all example Python scripts in parallel, excluding certain patterns.

    This function searches for all `.py` files under the `../../examples` directory,
    excluding any scripts in 'examples/other' and any files containing 'flycheck' in their name.
    All found scripts are executed in parallel using all available CPU cores.
    """
    example_scripts = glob.glob(
        os.path.join(
            os.path.dirname(__file__),
            "../../examples/**/*.py",
        ),
        recursive=True,
    )
    # Exclude any scripts in 'examples/other'
    example_scripts = [f for f in example_scripts if "examples/other" not in f.replace("\\", "/")]
    # Exclude flycheck files if needed
    example_scripts = [f for f in example_scripts if "flycheck" not in f]
    Parallel(n_jobs=-1)(delayed(run_example)(script) for script in example_scripts)


def setup(app):
    """Sphinx setup function to run all example scripts in parallel before building the docs.

    Parameters
    ----------
    app : sphinx.application.Sphinx
        The Sphinx application object.
    """
    # Commented out: Let sphinx-gallery handle example execution instead
    # This manual execution runs in subprocesses that don't inherit pyvista.BUILDING_GALLERY
    # app.connect("builder-inited", lambda app: run_all_examples_in_parallel())
    pass


# Suppress warnings
suppress_warnings = [
    "docutils",
    "ref.ref",  # Suppress undefined reference warnings
    "ref.class",  # Suppress missing class reference warnings
    "ref.obj",  # Suppress missing object reference warnings
    "ref.func",  # Suppress missing function reference warnings
    "ref.meth",  # Suppress missing method reference warnings
    "config.cache",  # Suppress unpickleable configuration warnings
    "autodoc",  # Suppress autodoc warnings including forward reference resolution
]
