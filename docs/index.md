# pipef: Function Pipelines for Python

## What is pipef?

`pipef` is a small, dependency-free library that chains callables with `|` instead of nesting
them. One `|` operator covers two shapes: a reusable lazy function built once and called later, and
an eager pipeline that pipes a value through immediately

`pipef` works as a double pun — pipe + function, but also pipe + forked, since each `|` in lazy mode
forks a new immutable chain instead of mutating the old one

Linux, macOS, and Windows are all first-class citizens, and so is every Python from 3.8 up

## Why Use pipef

See [Comparison](comparison.md) for the full survey against `pipetools`, `toolz`, `sspipe`, and
others — in short:

- **One operator, two shapes**: the same `|` builds a reusable lazy function (`pipef | f | g`) or
  pipes a value eagerly (`pipef(x) | f | g`), instead of needing a different library for each
- **Zero dependencies**: nothing else installs alongside it
- **Shared computation in eager mode**: branching off an already-resolved eager chain reuses that
  prefix's result instead of recomputing it per branch
- **Multi-arg/kwarg seed**: `pipef(1, 2, c=3) | f` seeds a chain with more than one value up front,
  which nothing surveyed in the comparison does

None of this is a reason to migrate off a library that's already working for you — `pipef` is aimed
at new code, or a project that wants both shapes without importing two libraries to get them

## Key Features

- **Lazy function factory**: `pipef | f | g` builds a reusable, forkable function
- **Eager value pipeline**: `pipef(x) | f | g` applies each step immediately and hands back a result
- **Immutable forking**: piping further off any chain, lazy or eager, always returns a fresh `pipef`
  and leaves the original callable and unchanged
- **Typed and dependency-free**: ships `py.typed`, works on Python 3.8 through 3.14, and pulls in
  nothing else

## Quick Start

### Installation

```bash
pip install pipef
```

See [Installing pipef](installing.md) for `uv`, Poetry, and Pipenv equivalents

### Basic Usage

```python
from pipef import pipef

fn = pipef | add_2 | mult_3
fn(2)
> 12
```

See [Quick Start Guide](quickstart.md) for a slightly longer walkthrough, [Advanced Usage](usage.md)
for the full lazy/eager reference, or [API Reference](api.md) for the generated class docs

```{toctree}
:maxdepth: 2
:hidden:

installing
quickstart
usage
comparison
faq
troubleshooting
api
```
