# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'plotext'
copyright = '2024, Savino Piccolomo'
author = 'Savino Piccolomo'
release = '6.0.0 beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


import sys, os
source = os.path.dirname(os.path.abspath(__file__))
docs = os.path.dirname(source)
git = os.path.dirname(docs)
plotext = os.path.join(git, 'plotext')
sys.path.insert(0, git)


extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx_copybutton'
    ]

source_suffix = ['.rst', '.md']