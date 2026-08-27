# pipef

[![PyPI](https://img.shields.io/pypi/v/pipef.svg)](https://pypi.org/project/pipef/)
[![Python](https://img.shields.io/pypi/pyversions/pipef.svg)](https://pypi.org/project/pipef/)

Function pipelines for Python — chain callables with `|` instead of nesting them

> Early scaffolding: the package installs and imports, but the pipe API has not landed yet

## Install

```bash
pip install pipef
```

## Usage

```python
import pipef

pipef.__version__
```

## Development

Prerequisite: [asdf](https://asdf-vm.com/guide/getting-started.html)

`pipef` supports Python 3.7+. `uv run poe test-all` runs the suite against every interpreter listed in
`.tool-versions`, skipping the ones you have not installed — so a partial set is fine

3.8+ runs under tox; 3.7 runs separately against the built wheel, because tox's interpreter probe itself
needs 3.8+

```bash
# Run after cloning
asdf plugin add uv && asdf plugin add python && \
asdf install && \
uv sync && \
uv run poe pre-commit-install && \
cp .env.example .env

# Tests on the pinned interpreter
uv run poe test

# Tests on every installed interpreter (tox 3.8+, plus the 3.7 floor)
uv run poe test-all

# Run all Code Quality Assurance
uv run poe cqa

# Commit via the Commitizen prompt
uv run poe commit
```

## Release

Published from a local machine — set `UV_PUBLISH_TOKEN` in `.env` first (see `.env.example`)

```bash
# Bump the version from the commit history, write CHANGELOG.md, and tag vX.Y.Z
uv run poe bump

# Build, twine-check, and upload to PyPI
uv run poe publish

git push --follow-tags
```

## References

1. [.gitignore](https://www.toptal.com/developers/gitignore?templates=node,python,intellij+all,macos,visualstudiocode,windows)
2. [Stylising your Python code: An introduction to linting and formatting](https://www.jumpingrivers.com/blog/python-linting-guide/)
3. [Pylint > Pre-commit integration](https://pylint.pycqa.org/en/stable/user_guide/installation/pre-commit-integration.html)
4. [Ultimate pre-commit Configuration for Python](https://www.hrekov.com/blog/pre-commit-configuration-python)
5. [How to Use Poe the Poet as a Task Runner with uv](https://pydevtools.com/handbook/how-to/how-to-use-poe-the-poet-as-a-task-runner-with-uv/)
6. [commitizen > Pre-commit Integration](https://github.com/commitizen-tools/commitizen?tab=readme-ov-file#pre-commit-integration)
7. [Commitizen > Project-Specific Installation](https://commitizen-tools.github.io/commitizen/#project-specific-installation)
8. [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
9. [uv > Building and publishing a package](https://docs.astral.sh/uv/guides/package/)
10. [tox > Configuration](https://tox.wiki/en/stable/config.html)
11. [Commitizen > Bump](https://commitizen-tools.github.io/commitizen/commands/bump/)
