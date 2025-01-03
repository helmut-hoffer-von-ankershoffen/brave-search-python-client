# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "brave-search-python-client"
copyright = "2025, Helmut Hoffer von Ankershoffen"
author = "Helmut Hoffer von Ankershoffen"
release = "0.2.14"
github_username = "helmut-hoffer-von-ankershoffen"
github_repository = "brave-search-python-client"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx-pydantic",
    "sphinxcontrib.autodoc_pydantic",
    "enum_tools.autoenum",
    "sphinx_copybutton",
    "sphinx.ext.coverage",
    "sphinx_mdinclude",
    "sphinxext.opengraph",
    "sphinx_inline_tabs",
    "sphinx_toolbox",
]

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
latex_additional_files = ["latex/latexmkrc"]

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = "footnote"

# If false, no module index is generated.
latex_domain_indices = True

# See https://www.sphinx-doc.org/en/master/latex.html
latex_elements = {
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "11pt",
    # fonts
    "fontpkg": r"""
        \RequirePackage{fontspec}
        % RTD uses a texlive installation on linux; apparently xelatex can only
        % find fonts by filename in this situation.
        \setmainfont{texgyretermes-regular.otf}
        \setsansfont{Heuristica-Bold.otf}
    """,
    "geometry": r"\usepackage[xetex,letterpaper]{geometry}",
    # chapter style
    "fncychap": r"\usepackage[Bjarne]{fncychap}",
    # Latex figure (float) alignment
    "figure_align": "H",
    # Additional stuff for the LaTeX preamble.
    "preamble": r"""
        \RequirePackage{unicode-math}
        \makeatletter
        \fancypagestyle{normal}{
            \fancyhf{}
            \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
            % \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
            % \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
            \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}
            \renewcommand{\headrulewidth}{0.4pt}
            \renewcommand{\footrulewidth}{0pt}
        }
        \fancypagestyle{plain}{
            % used for first page of a chapter only
            \fancyhf{}
            \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
            \renewcommand{\footrulewidth}{0pt}
        }
        \setlength{\headheight}{13.61pt} % otherwise get errors from fancyhdr
        \makeatother
    """,
    "extraclassoptions": "openany",
}
