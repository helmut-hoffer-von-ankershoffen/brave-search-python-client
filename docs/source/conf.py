# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
import datetime

project = "brave-search-python-client"
author = "Helmut Hoffer von Ankershoffen"
copyright = " (c) 2025-{}, {}".format(datetime.datetime.now().year, author)
version = "0.2.15"
release = version
github_username = "helmut-hoffer-von-ankershoffen"
github_repository = "brave-search-python-client"

language = "en"

ogp_site_name = "Brave Search Python Client"
ogp_use_first_image = True  # https://github.com/readthedocs/blog/pull/118
# ogp_image = "https://docs.readthedocs.io/en/latest/_static/img/logo-opengraph.png"
# Inspired by https://github.com/executablebooks/MyST-Parser/pull/404/
# ogp_custom_meta_tags = [
#    '<meta name="twitter:card" content="summary_large_image" />',
# ]
ogp_enable_meta_description = True
ogp_description_length = 300


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_toolbox.collapse",  # https://sphinx-toolbox.readthedocs.io/
    "sphinx_toolbox.sidebar_links",
    #    "sphinx_toolbox.more_autodoc",
    #    "sphinx_toolbox.more_autosummary",
    "sphinx_toolbox.github",
    #    "sphinx_toolbox.source",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "enum_tools.autoenum",  # https://github.com/domdfcoding/enum_tools/tree/master
    "sphinx.ext.napoleon",  # https://sphinxcontrib-napoleon.readthedocs.io/en/latest/
    "sphinx-pydantic",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx.ext.coverage",
    "sphinx_copybutton",
    "sphinx.ext.extlinks",  # https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
    "sphinx.ext.imgconverter",
    "sphinx_inline_tabs",
    "sphinx_mdinclude",
    "sphinxemoji.sphinxemoji",  # https://sphinxemojicodes.readthedocs.io/en/stable/
    "sphinxext.opengraph",
]

#   Docker <https://hub.docker.com/r/helmuthva/brave-search-python-client/tags>
#   SonarQube <https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client>
#   Codecov <https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client>
#   ghcr.io <https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/pkgs/container/brave-search-python-client>
#   License <https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/LICENSE>


templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_logo = "../../brave.png"
html_theme_options = {
    "announcement": (
        '<a target="_blank" href="https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client">GitHub</a> - '
        '<a target="_blank" href="https://pypi.org/project/brave-search-python-client/">PyPI</a> - '
        '<a target="_blank" href="https://hub.docker.com/r/helmuthva/brave-search-python-client/tags">Docker</a> - '
        '<a target="_blank" href="https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client">SonarQube</a> - '
        '<a target="_blank" href="https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client">Codecov</a>'
    )
}

latex_engine = "lualatex"  # https://github.com/readthedocs/readthedocs.org/issues/8382

# See https://egitlab.gfdl.noaa.gov/NOAA-GFDL/MDTF-diagnostics/-/blob/hotfix/doc/conf.py
# latex_additional_files = ["latex/latexmkrc"]

# If true, show page references after internal links.
# latex_show_pagerefs = True

# If true, show URL addresses after external links.
# latex_show_urls = "footnote"

# If false, no module index is generated.
# latex_domain_indices = True

# See https://www.sphinx-doc.org/en/master/latex.html
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",
}

latex_documents = [
    (
        "index",
        "{}.tex".format(project),
        r"{} Documentation".format(project),
        author,
        "manual",
    ),
]

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

linkcheck_retries = 2
linkcheck_timeout = 1
linkcheck_workers = 10
linkcheck_ignore = [
    r"http://127\.0\.0\.1",
    r"http://localhost",
]

# https://github.com/sphinx-toolbox/sphinx-toolbox/blob/master/doc-source/conf.py#L22
# latex_elements["preamble"] = r"\usepackage{multicol}"
# nitpicky = True
# needspace_amount = r"4\baselineskip"
# autodoc_type_aliases = {"ForwardRef": "ForwardRef"}


# https://github.com/SAR-ARD/s1ard/blob/main/docs/source/conf.py
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))
