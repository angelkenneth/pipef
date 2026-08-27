# pipef

[![PyPI](https://img.shields.io/pypi/v/pipef.svg)](https://pypi.org/project/pipef/)
[![Python](https://img.shields.io/pypi/pyversions/pipef.svg)](https://pypi.org/project/pipef/)
[![License](https://img.shields.io/pypi/l/pipef.svg)](LICENSE.md)

Function pipelines for Python — chain callables with `|`, lazily as a reusable function or eagerly through a value

## Install

```bash
pip install pipef
```

```bash
uv add pipef
```

```bash
poetry add pipef
```

```bash
pipenv install pipef
```

## Usage

See more: [USAGE.md](USAGE.md)

```python
from pipef import pipef

fn = pipef | add_2 | mult_3
fn(2)
> 9
```

## Why pipef

Advantages of `pipef` over the libraries surveyed in [COMPARISON.md](COMPARISON.md):

1. One `|` operator covers both a reusable lazy function (`pipef | f | g`) and an eager value pipeline
   (`pipef(x) | f | g`), instead of needing a different library for each shape
2. Zero dependencies
3. Eager mode shares a branched prefix's computation once instead of recomputing it per branch
4. Accepts a multi-arg/kwarg seed (`pipef(1, 2, c=3) | f`), which nothing surveyed does

None of that is a reason to migrate off a library that's already working for you — if `pipetools`,
`toolz`, `sspipe`, or similar already covers your pipeline, keep using it. `pipef` is aimed at new code,
or a project that wants both shapes without importing two libraries to get them

## Development

Prerequisite: [asdf](https://asdf-vm.com/guide/getting-started.html)

`pipef` supports Python 3.8+. `uv run poe test-all` runs the suite (via tox) against every interpreter
listed in `.tool-versions`, skipping the ones you have not installed — so a partial set is fine

```bash
# Run after cloning
asdf plugin add uv && asdf plugin add python && \
asdf install && \
uv sync && \
uv run poe pre-commit-install && \
cp .env.example .env

# Tests on the pinned interpreter
uv run poe test

# Tests on every installed interpreter (3.8+, via tox)
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
