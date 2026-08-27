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
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Generates anchor ids for headings so in-page links like USAGE.md/COMPARISON.md's `#multi-arg-seed` resolve
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

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
}
html_sidebars = {
    "**": ["about.html", "navigation.html", "relations.html", "searchbox.html"],
}
