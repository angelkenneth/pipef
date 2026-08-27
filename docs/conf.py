"""Sphinx configuration for the pipef docs site — see https://www.sphinx-doc.org/en/master/usage/configuration.html"""

# pylint: disable=invalid-name

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

from pipef import __version__  # noqa: E402  pylint: disable=wrong-import-position

project = "pipef"
copyright = "2026, Angel Kenneth Tolentino"  # pylint: disable=redefined-builtin
author = "Angel Kenneth Tolentino"
release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Generates anchor ids for headings so in-page links like USAGE.md/COMPARISON.md's `#multi-arg-seed` resolve
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_static_path = ["_static"]
# SVG for modern browsers; falls back to the PNG twin below where SVG favicons aren't supported
html_favicon = "_static/favicon.svg"
# Pins a:visited to the theme's link color — Alabaster leaves it unstyled, so browsers default it to purple
html_css_files = ["custom.css"]

# Matches the PyPA-style layout (pip, pipenv, virtualenv): Alabaster theme, right-hand sidebar
html_theme = "alabaster"
html_theme_options = {
    "description": "Function pipelines for Python — chain callables with |",
    "github_user": "angelkenneth",
    "github_repo": "pipef",
    "github_button": True,
    "github_type": "star",
    "github_banner": False,
    "show_powered_by": False,
    "show_related": False,
    "fixed_sidebar": True,
    "extra_nav_links": {
        "Author's site": "https://www.aktolentino.com",
        "Hosted on Netlify": "https://www.netlify.com",
    },
    # Matches aktolentino.com's body background color, replacing Alabaster's default white
    "base_bg": "#F7F8FF",
    # Transparent so the header pattern in custom.css shows through behind the article text
    "body_bg": "transparent",
    # Matches aktolentino.com's body text color, replacing Alabaster's default #3E4349
    "body_text": "rgba(0, 0, 0, .87)",
    # Matches the "baby brown" accent (#C09D7F) from aktolentino.com, darkened for link contrast
    "link": "#B28B6C",
    "link_hover": "#8B6A4D",
    "sidebar_link_underscore": "#C09D7F",
    "anchor_hover_bg": "#F7F3F0",
}
html_sidebars = {
    "**": ["about.html", "navigation.html", "relations.html", "searchbox.html"],
}
