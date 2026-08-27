# Quick Start Guide

## Installation

```bash
pip install pipef
```

See [Installing pipef](installing.md) for other package managers

## Your First Lazy Pipeline

Bare `pipef`, never called, builds a reusable function out of everything piped into it

```python
from pipef import pipef

def add_2(x):
    return x + 2

def mult_3(x):
    return x * 3

fn = pipef | add_2 | mult_3
fn(2)
> 12
```

## Your First Eager Pipeline

Calling `pipef(...)` pipes those arguments through the chain right away, one step at a time. The
result unpacks with `result, =`, or a plain call

```python
from pipef import pipef

result, = pipef(2) | add_2 | mult_3
result
> 12
```

## Forking

Every `|` returns a fresh `pipef`, so branching off one chain never changes the original — in either
mode

```python
from pipef import pipef

base = pipef | add_2
branch_a = base | mult_3
branch_b = base | (lambda x: x - 3)
branch_a(2)
> 12
branch_b(2)
> 1
base(2)
> 4
```

## Next Steps

[Advanced Usage](usage.md) covers kwargs seeds, empty seeds, and the edge cases around reading a value
before piping it. [Comparison](comparison.md) lines pipef's syntax up against other piping libraries
