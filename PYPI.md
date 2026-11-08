# pipef

Function pipelines for Python — chain callables with `|`, lazily as a reusable function or eagerly through a value

`pipef` works as a double pun — pipe + function, but also pipe + forked, since each `|` in
lazy mode forks a new immutable chain instead of mutating the old one

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

A bare `pipef` builds a reusable function out of everything piped into it

```python
from pipef import pipef


def add_2(x):
    return x + 2


def mult_3(x):
    return x * 3


fn = pipef | add_2 | mult_3
fn(2)
# 12
```

Calling `pipef(...)` pipes a value through the chain right away

```python
result, = pipef(2) | add_2 | mult_3
result
# 12
```

## Why pipef

Advantages of `pipef` over the libraries surveyed in the [comparison](https://pipef.aktolentino.com/comparison.html):

1. One `|` operator covers both a reusable lazy function (`pipef | f | g`) and an eager value pipeline
   (`pipef(x) | f | g`), instead of needing a different library for each shape
2. Zero dependencies
3. Eager mode shares a branched prefix's computation once instead of recomputing it per branch
4. Accepts a multi-arg/kwarg seed (`pipef(1, 2, c=3) | f`), which nothing surveyed does

None of that is a reason to migrate off a library that's already working for you — if `pipetools`,
`toolz`, `sspipe`, or similar already covers your pipeline, keep using it. `pipef` is aimed at new code,
or a project that wants both shapes without importing two libraries to get them

## Learn more

- [Documentation](https://pipef.aktolentino.com)
- [Quickstart](https://pipef.aktolentino.com/quickstart.html)
- [Advanced usage](https://pipef.aktolentino.com/usage.html)
- [Comparison with other libraries](https://pipef.aktolentino.com/comparison.html)
- [API reference](https://pipef.aktolentino.com/api.html)
- [Changelog](https://github.com/angelkenneth/pipef/blob/main/CHANGELOG.md)
- [Source code](https://github.com/angelkenneth/pipef)
