# CLAUDE.md

`pipef`: a small Python library published to PyPI that chains callables with `|` instead of nesting them.
The package lives in `src/pipef/`; it is distributed as a wheel + sdist built by hatchling

## Stack Decisions

The "Stack Decisions" section in [README.md](README.md) is the source of truth for this repo's tooling and
the reasoning behind it — read it before proposing a tooling change. Each entry is a deliberate choice,
including reverted or avoided alternatives (the "Non-stack Decision" subsection); don't swap one out
without raising it with the user first

Keep that section current in the same change that alters it — adding, removing, or replacing a dependency
or tool

## Dependencies

The library itself stays dependency-free — runtime dependencies need a deliberate decision, so raise it
before adding one. Tooling belongs in the `dev` dependency group

The library supports Python 3.8+, but the `dev` group resolves against the pinned interpreter only
(`[tool.uv.dependency-groups]`), so dev tooling may use newer syntax than the library can

## Code Style

Keep inline docs (comments, docstrings) to a maximum of two lines

All functions and classes in this repo require inline docs (a docstring or a comment directly above them describing what they do)

Don't end the last sentence of a paragraph with a period; sentences earlier in the paragraph still keep theirs

Shipped code must stay compatible with Python 3.8 — no builtin generics or `X | Y` unions outside
`from __future__ import annotations`

`pylint` enforces this via `py-version`, but it does not catch everything — `uv run poe test-all` does

## Dogfooding

This repo is `pipef`'s own home, so prefer `pipef` over nested calls when writing or editing Python here —
scripts, examples, docs snippets, even tests where it doesn't fight the assertion style — wherever chaining
reads more naturally than nesting

Don't force it where a plain call or comprehension is clearer; this is about modeling idiomatic usage, not
maximizing pipe count

## Testing

Tests live in the top-level `tests/` package, named `<module>_test.py` after the module they cover

`uv run poe test` runs them on the pinned interpreter; `uv run poe test-all` covers the whole support range
via tox

## Versioning and Release

`pyproject.toml` is the single source of truth for the version; Commitizen mirrors it into
`src/pipef/__init__.py` via `version_files` — never hand-edit either

Release from a local machine with `scripts/release.sh`, which runs the steps in [RELEASING.md](RELEASING.md):
`uv run poe bump` (Commitizen) then `uv run poe publish`, which cleans `dist/`, builds, twine-checks, and
uploads with the `UV_PUBLISH_TOKEN` in `.env`. Keep the script and RELEASING.md in step when either changes

## Git

Keep commit messages to a single line — no multi-paragraph body

Commit messages follow `<type>(<ticket>): <summary>`, where `<ticket>` is a space-separated Jira key list
or `na-0` when no ticket applies. Prefer `uv run poe commit` over hand-writing the message

Never run `git commit` unless the user explicitly tells you to commit in that turn. Staging, diffing, and preparing changes is fine without asking; committing is not

Always `git add` any file you create or modify as soon as you're done with it, so nothing is left untracked or unstaged — the user stashes changes from PyCharm's IDE, which only picks up staged/tracked files by default
