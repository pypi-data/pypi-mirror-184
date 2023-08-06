# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import heatgraphy as hg

# -- Project information -----------------------------------------------------

project = 'heatgraphy'
copyright = '2022, Mr-Milk'
author = 'Mr-Milk'

# The full version, including alpha/beta/rc tags
release = hg.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'numpydoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    'sphinx_copybutton',
]
autoclass_content = "class"
autodoc_docstring_signature = True
autodoc_default_options = {'members': None, 'undoc-members': None}
autodoc_typehints = 'none'
# setting autosummary
autosummary_generate = True
numpydoc_show_class_members = False

# setting plot direction
plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = [('png', 180)]
plot_pre_code = "import numpy as np; import pandas as pd;" \
                "from matplotlib import pyplot as plt;" \
                "import matplotlib as mpl; np.random.seed(0);"\
                "mpl.rcParams['savefig.bbox'] = 'tight';"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_logo = "../../img/logo.png"

intersphinx_mapping = {
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'seaborn': ('https://seaborn.pydata.org/', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'legendkit': ('https://legendkit.readthedocs.io/en/stable', None),
}

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5," \
                         r"8}: "
copybutton_prompt_is_regexp = True


def autodoc_skip_member(app, what, name, obj, skip, options):
    methods = ['get_legends', 'get_canvas_size',
               'render_ax', 'render_axes',
               'get_render_data']
    attrs = ['render_main', 'canvas_size_unknown', 'no_split',
             'data', 'deform', 'deform_func']

    if hasattr(obj, "__qualname__"):
        cls = obj.__qualname__.split(".")[0]
        if cls != "RenderPlan":
            if name in methods:
                return True
    if what == "attribute":
        if name in attrs:
            return True
    return


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
