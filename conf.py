# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Intel® Technology Enabling for OpenShift*'
copyright = '2024, Intel® Corporation'
author = 'Intel® Corporation'

# The short X.Y version
# version = 'devel'
# The full version, including alpha/beta/rc tags
# release = 'GA'


# -------------- Upstream -------------------
from os import getenv

baseBranch = "main"
sphinx_md_useGitHubURL = True
commitSHA = getenv('GITHUB_SHA')
githubBaseURL = 'https://github.com/' + (getenv('GITHUB_REPOSITORY') or 'intel/intel-technology-enabling-for-openshift') + '/'
githubFileURL = githubBaseURL + "blob/"
githubDirURL = githubBaseURL + "tree/"
if commitSHA:
    githubFileURL = githubFileURL + commitSHA + "/"
    githubDirURL = githubDirURL + commitSHA + "/"
else:
    githubFileURL = githubFileURL + baseBranch + "/"
    githubDirURL = githubDirURL + baseBranch + "/"
sphinx_md_githubFileURL = githubFileURL
sphinx_md_githubDirURL = githubDirURL

# Version displayed in the upper left corner of the site
ref = getenv('GITHUB_REF', default="")
print("ref = ", getenv('GITHUB_REF'))
if ref == "refs/heads/main":
    version = "main"
elif ref.startswith("refs/tags/"):
    version = ref[len("refs/tags/"):]
else:
    version = getenv("BUILD_VERSION", default="unknown")

print("version=", version)
release = getenv("BUILD_VERSION", default="unknown")
print("release=", release)



# Versions to show in the version menu

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx_md', ]
# myst_enable_extensions = [
#     "html_admonition",
# ]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_book_theme'
html_theme = 'sphinx_rtd_theme'
# html_logo = '_static/intel-logo.svg'
html_title = "Intel® Technology Enabling for OpenShift*"
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "display_version": True,
}

html_context = {
    'display_github': True,
    'github_host': 'github.com',
    'github_user': 'intel',
    'github_repo': 'intel-technology-enabling-for-openshift',
    'github_version': 'main/',
    'versions_menu': True,
}
# html_css_files = [
#     'custom.css',
# ]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'IntelTechnologyEnablingforOpenShiftdoc'


