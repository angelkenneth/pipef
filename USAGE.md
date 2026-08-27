# Usage

Two ways to chain callables with `|`: build a reusable function lazily, or pipe a value through right away

## Function Factory

Bare `pipef`, never called, builds a reusable function out of everything piped into it

```python
from pipef import pipef

fn_1 = pipef | add_2 | mult_3
fn_1(2)
> 42
```

### Forking

Because every step returns a fresh function, piping more off one never touches the original

```python
from pipef import pipef

fn_1 = pipef | add_2 | mult_3
fn_2 = fn_1 | add_2
fn_3 = fn_1 | minus_3
fn_2(2)
> 44
fn_3(2)
> 39
fn_1(2)
> 42
```

## Immediate Invocation

Calling `pipef(...)` pipes those arguments through the chain right away, one step at a time

### With Args

Each `|` applies immediately, and the final result unpacks with `result, =` or a plain call

```python
from pipef import pipef

result, = pipef(2) | add_2 | mult_3
result
> 42
result_fn = pipef(2) | add_2 | mult_3
result, = result_fn
result
> 42
result = result_fn()  # optional behaviour
result
> 42
```

### With Kwargs

The first function in the chain takes keyword arguments too, spread in alongside any positional ones

```python
from pipef import pipef

result, = pipef(1, 2, c=3) | (lambda a, b, c: a + b + c) | add_2
result
> 8
```

### Empty

Even with nothing passed in, piping still works — the first function is just called with no arguments

```python
from pipef import pipef

result, = pipef() | (lambda: 1) | add_2
result
> 3
```

### On Its Own

Left as is, with nothing piped in either, an empty `pipef()` simply holds `None`

```python
from pipef import pipef

pipef()
> None
```

### Forking

Piping further off an already-resolved result forks a new one without changing it

```python
from pipef import pipef

result_fn = pipef(2) | add_2 | mult_3
result_1, = result_fn | add_5
result_1
> 47
result_2, = result_fn | minus_3
result_2
> 39
result_0, = result_fn
result_0
> 42
```
