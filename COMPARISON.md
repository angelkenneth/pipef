# Comparison

How `pipef`'s syntax lines up against other function-piping libraries already on PyPI, and where it
actually differs rather than just looking different

All examples below pipe `1` through `add_2` then `mul_3`, expecting `9`

## Reusable composed callable

`pipef`'s lazy mode builds a function once and calls it later

```python
fn = pipef | add_2 | mul_3
fn(1)
```

| Library | Equivalent | Notes |
| --- | --- | --- |
| [`pipetools`](https://pypi.org/project/pipetools/) | `fn = pipe \| add_2 \| mul_3` | near-identical shape; `pipef` is a close relative of this one |
| [`compose-operator`](https://pypi.org/project/compose-operator/) | `fn = composable(add_2) \| mul_3` | preserves introspection and pickling, which `pipef` doesn't try to |
| [`toolz`](https://pypi.org/project/toolz/) | `fn = compose_left(add_2, mul_3)` | no `\|`, args passed to a function instead |
| [`sspipe`](https://pypi.org/project/sspipe/) | `fn = p(add_2) \| p(mul_3)` then `1 \| fn` | every stage needs its own `p()` wrapper |

## Eager value through a chain

`pipef`'s eager mode applies each step immediately and hands back the result

```python
result, = pipef(1) | add_2 | mul_3
```

| Library | Equivalent | Notes |
| --- | --- | --- |
| [`pipetools`](https://pypi.org/project/pipetools/) | none | build the chain, then call it — there's no true eager form |
| [`sspipe`](https://pypi.org/project/sspipe/) | `1 \| p(add_2) \| p(mul_3)` | returns the value directly, no unpack needed |
| [`pipe-operator`](https://pypi.org/project/pipe-operator/) | `start(1) >> pipe(add_2) >> pipe(mul_3) >> end()` | `>>` instead of `\|`, and needs a closing `end()` |
| [`toolz`](https://pypi.org/project/toolz/) | `toolz.pipe(1, add_2, mul_3)` | a function call, not `\|` chaining |
| [`pipe`](https://pypi.org/project/pipe/) (the PyPI package named `pipe`) | n/a | built for lazily filtering/mapping iterables (`where`, `take_while`), not single-value pipelines |

The `result, =` unpack is the price `pipef` pays for one property nothing else surveyed offers: see
[Multi-arg seed](#multi-arg-seed) below

## Multi-arg seed

Piping `pipef(1, 2, c=3)` seeds the chain with positional and keyword arguments up front, before any
function runs

```python
result, = pipef(1, 2, c=3) | add_all | mul_3
```

| Library | Form | Result |
| --- | --- | --- |
| `pipef` | `pipef(1, 2, c=3) \| add_all \| mul_3`, args seeded first | `18` |
| `pipetools` | `(pipe \| add_all \| mul_3)(1, 2, c=3)`, args supplied last | `18`, and no unpack needed |
| `compose-operator` | `(composable(add_all) \| mul_3)(1, 2, c=3)`, args supplied last | `18`, and no unpack needed |
| `sspipe` | `(1, 2) \| p(add_all)` | `TypeError` — a single piped value, not a spread of args |
| `toolz` | `toolz.pipe(1, 2, add_all)` | `TypeError` — `pipe()` takes exactly one seed value |

No library surveyed accepts arguments at the seed the way `pipef` does. `pipetools` and `compose-operator`
reach the same result by moving the arguments to the end of the expression instead, without needing
`result, =` — so this is a difference in where the arguments go, not in what's possible

## Function factory branching

The Function Factory (`pipef`'s lazy mode) forks into new reusable functions without mutating the
original — piping off an already-built chain returns a fresh one, and the base chain stays callable on
its own

```python
base = pipef | f1
branch_a = base | f2
branch_b = base | f3
```

`branch_a`, `branch_b`, and `base` are all independently callable afterward, and `base(x)` still only runs
`f1`

| Library | Model | Base mutated? |
| --- | --- | --- |
| `pipetools` | `Pipe.__or__` returns a new `Pipe` wrapping a `bind()` composite | no — matches `pipef` |
| `compose-operator` | `composable.__or__` returns a new composed callable | no — matches `pipef` |
| `toolz` | `compose_left(...)` returns a new function each call | no — matches `pipef`, though there's no `\|` step to fork mid-chain |

Unlike eager branching below, this isn't a real differentiator. Nothing in a lazy chain runs until the
final call, so forking one is cheap by construction in every library here — there's simply nothing to
re-execute yet. `pipetools` verifies this identically: `__or__` never assigns to `self.func`, it returns a
new `Pipe` wrapping a new composite, leaving the original untouched and still callable. Where `pipef`
actually pulls ahead is in eager mode, where branching forces a real choice between rerunning a shared
prefix or not

## Eager branching shares computation

This is the one difference that's semantic rather than stylistic. Branch two chains off a shared prefix,
and count how many times the shared step actually runs

```python
base = pipef(1) | f1
branch_a = base | f2
branch_b = base | f3
```

| Library | Model | `f1` invocations |
| --- | --- | --- |
| `pipef` | eager, wraps the resolved value | 1 — computed once at `base`, reused by both branches |
| `pipetools` | lazy composition | 2 — the prefix reruns for every branch |
| `sspipe` | eager, raw value | 1 — same sharing, no wrapper needed |
| `compose-operator`, `toolz` | lazy composition | 2 — the prefix reruns for every branch |

If a shared prefix does real work — a query, a file read, an expensive transform — a lazy library repeats
it per branch. `pipef`'s eager mode already holds the materialized result, so branching off it is free

## Advantages, and when to just use what you have

`pipef`'s case in one sentence: one `|` operator, one import, that covers both the reusable-function shape
and the eager-value shape, with the branch sharing and multi-arg seed above thrown in — and no
dependencies to add

That said, none of this is worth a migration on its own. If a project already pipes through `pipetools`,
`toolz`, `sspipe`, or anything else in the tables above and it reads fine, keep using it — the syntax
differences here are mostly a matter of taste, and rewriting working pipelines to save an `import` isn't a
trade worth making. `pipef` is aimed at new code, or at a project that wants both shapes without pulling in
two different libraries to get them
