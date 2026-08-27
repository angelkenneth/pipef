# Troubleshooting

## `TypeError: a lazy pipef chain can't be unpacked — call it with a value instead`

Raised by `__iter__` when you try `result, = fn` on a lazy chain (built off the bare `pipef` class,
never called). A lazy chain has no held value to unpack — call it with a seed first, either directly
(`fn(x)`) or by starting an eager chain instead (`pipef(x) | f`)

## `TypeError: an eager pipef takes no arguments — start a new pipef(value) instead`

Raised by `__call__` when you call an already-eager `pipef` with arguments, e.g. `result_fn(5)` where
`result_fn` already holds a resolved value from `pipef(x) | f`. Calling an eager `pipef` with no
arguments is fine (it just returns the held value); to run a new value through the same functions,
start a fresh chain instead: `pipef(5) | f`

## `TypeError: unhashable type: 'pipef'`

Raised whenever something hashes a `pipef` instance — putting one in a `set`, using it as a `dict`
key, or calling `hash()` on it directly. This is intentional (see [FAQ](faq.md)); hash the value the
pipeline produced instead of the `pipef` wrapping it

## A step after the first raises a `TypeError` about missing or unexpected arguments

Only the first function in a chain receives the seed's `*args`/`**kwargs` — every step after that is
called with exactly one positional argument, the previous step's return value. If a later function's
signature expects more than one argument, wrap it (a `lambda result: later_fn(*result)` for a tuple
result, for example) rather than piping it in directly

## Docs build fails with `-W`

`uv run poe docs` treats Sphinx warnings as errors. A broken cross-reference (a `.md` link to a page
outside the toctree, an autodoc target that no longer exists) is the usual cause — the warning text
Sphinx prints names the offending file and line
