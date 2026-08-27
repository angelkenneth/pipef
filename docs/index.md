# pipef

Function pipelines for Python — chain callables with `|`, lazily as a reusable function or eagerly through a
value

`pipef` works as a double pun — pipe + function, but also pipe + forked, since each `|` in lazy mode forks
a new immutable chain instead of mutating the old one

## Install

```bash
pip install pipef
```

## Quick example

```python
from pipef import pipef

fn = pipef | add_2 | mult_3
fn(2)
> 12
```

See [Usage](usage.md) for the full lazy/eager walkthrough, or the [API Reference](api.md) for the
generated class docs

## Why pipef

Advantages of `pipef` over the libraries surveyed in [Comparison](comparison.md):

1. One `|` operator covers both a reusable lazy function (`pipef | f | g`) and an eager value pipeline
   (`pipef(x) | f | g`), instead of needing a different library for each shape
2. Zero dependencies
3. Eager mode shares a branched prefix's computation once instead of recomputing it per branch
4. Accepts a multi-arg/kwarg seed (`pipef(1, 2, c=3) | f`), which nothing surveyed does

None of that is a reason to migrate off a library that's already working for you — if `pipetools`,
`toolz`, `sspipe`, or similar already covers your pipeline, keep using it. `pipef` is aimed at new code,
or a project that wants both shapes without importing two libraries to get them

```{toctree}
:maxdepth: 2
:hidden:

usage
comparison
api
```
