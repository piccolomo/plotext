# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys


# -- Path setup --------------------------------------------------------------
# Make the plotext package importable so autodoc can pick it up.

_here = os.path.dirname(os.path.abspath(__file__))
_git_root = os.path.dirname(os.path.dirname(_here))  # docs/source -> docs -> git/
sys.path.insert(0, _git_root)


# -- Project information -----------------------------------------------------

project = 'plotext'
author = 'Savino Piccolomo'
copyright = '2024, Savino Piccolomo'
release = '6.0.0b0'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.duration',
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx_copybutton',
]

source_suffix = ['.rst', '.md']
templates_path = ['_templates']
exclude_patterns = []

# Document class/module members in the order they appear in the source file,
# rather than alphabetically. Keeps related methods (e.g. hstack/vstack) next
# to each other and follows the deliberate layout of the source.
autodoc_member_order = 'bysource'


# Escape the leading asterisk of "*args" docstring lines so docutils does not
# read it as an emphasis marker; the runtime docstrings stay untouched.
def escape_star_parameters(app, what, name, obj, options, lines):
    for index, line in enumerate(lines):
        if line.startswith('*'):
            lines[index] = '\\' + line


def setup(app):
    app.connect('autodoc-process-docstring', escape_star_parameters)


# The |plotext| substitution renders like the ``plotext`` literal, but links to the home page
rst_prolog = """
.. |plotext| raw:: html

   <a class="reference internal" href="index.html"><code class="docutils literal notranslate"><span class="pre">plotext</span></code></a>
"""


# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
