# Frequently Asked Questions

## General Questions

### What does the name mean?

`pipef` is a double pun — pipe + function, but also pipe + forked, since each `|` in lazy mode forks
a new immutable chain instead of mutating the old one

### What's the difference between lazy and eager mode?

Bare `pipef | f` opens a lazy chain — a reusable function that runs `f` (and anything piped after it)
only once called. `pipef(x) | f`, any direct call including with no arguments, applies `f` right away
against `x` and holds the result. See [Usage Guide](usage.md) for the full walkthrough

## Usage

### Why do I need `result, = pipef(x) | f` instead of just `pipef(x) | f`?

`pipef(x) | f` still returns a `pipef` instance holding the result, not the raw value. Unpacking
(`result, =`) or calling it (`pipef(x) | f | g` then `()`) both read that held value back out —
whichever reads more naturally at the call site

### Does piping mutate the chain I already built?

No. Both `__or__` implementations return a brand-new `pipef` — a lazy chain gets a new `func_list`
tuple, an eager one gets a freshly wrapped result. The original stays callable and unchanged, which
is what makes forking (branching two pipelines off one shared prefix) safe

### Do steps after the first one receive all of the seed's arguments?

No — only the first function in the chain is called with the seed's `*args`/`**kwargs`. Every step
after that receives exactly one positional argument: the previous step's return value. Design
functions after the first to take a single value (a tuple or dict, if you need to carry more than one
through)

### Does pipef work with async functions?

Not on its own. `__call__` invokes each function synchronously and passes its return value straight
to the next step, so piping an `async def` function just hands the next step an unawaited coroutine
instead of its result

### Can I use a `pipef` instance as a dict key or put it in a set?

No — `__hash__` is set to `None` deliberately, since `kwargs` is a mutable `dict` and would make
hashing unsound. Hash the value the pipeline produced instead, once you've read it out

## Where to Go Next

[Troubleshooting](troubleshooting.md) covers the errors these edge cases raise in practice, and how
to fix them
