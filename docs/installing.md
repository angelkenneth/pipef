# Installing pipef

## Prerequisites

`pipef` supports Python 3.8 and up, on Linux, macOS, and Windows, with no runtime dependencies of
its own

## Installation Methods

Pick whichever matches the tool your project already uses

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

## Verifying Installation

```bash
python -c "from pipef import __version__; print(__version__)"
```

That prints the installed version, mirroring `release` in [`docs/conf.py`](conf.py), which reads it
straight from the package rather than duplicating it

## Upgrading pipef

```bash
pip install --upgrade pipef
```

Substitute `uv add --upgrade`, `poetry update pipef`, or `pipenv update pipef` for the other
installers above. See [Changelog](https://github.com/angelkenneth/pipef/blob/main/CHANGELOG.md) for
what changed between versions

## Next Steps

Continue to [Quick Start](quickstart.md) for a first pipeline, or [Usage Guide](usage.md) for the
full lazy/eager reference
