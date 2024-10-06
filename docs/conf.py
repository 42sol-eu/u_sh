# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'u-shell'
copyright = '2024, Andreas Felix Häberle'
author = 'Andreas Felix Häberle'
release = '2024.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = [
    "sphinx.ext.autodoc",
    #"sphinx_autodoc_annotation",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_copybutton",
    "hoverxref.extension",
    # "sphinx_gallery", #TODO: how to include this gallery extension?
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme' # 'groundwork' (strange visited link color), 'alabaster'
html_static_path = ['_static']
