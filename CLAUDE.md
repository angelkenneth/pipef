# CLAUDE.md

Blank UV Project: a Python sandbox for ad hoc scripts, logs, and one-off experiments, with the shared tooling
(git hooks, linting, formatting, tests, CQA) already wired up. Each script or experiment lives in its own
`apps/*` package — `apps/sample` is the starting template

## Dependencies

No dependency isolation between apps: every `apps/*` package shares the single root `pyproject.toml`/`uv.lock`
— don't give an individual app its own `uv.lock`

## Code Style

Keep inline docs (comments, docstrings) to a maximum of two lines

All functions and classes in this repo require inline docs (a docstring or a comment directly above them describing what they do)

Don't end the last sentence of a paragraph with a period; sentences earlier in the paragraph still keep theirs

## Testing

Tests live in a `tests/` package beside the code they cover (`apps/<name>/tests/`), named `<module>_test.py`

## Git

Keep commit messages to a single line — no multi-paragraph body

Commit messages follow `<type>(<ticket>): <summary>`, where `<ticket>` is a space-separated Jira key list
or `na-0` when no ticket applies. Prefer `uv run poe commit` over hand-writing the message

Never run `git commit` unless the user explicitly tells you to commit in that turn. Staging, diffing, and preparing changes is fine without asking; committing is not

Always `git add` any file you create or modify as soon as you're done with it, so nothing is left untracked or unstaged — the user stashes changes from PyCharm's IDE, which only picks up staged/tracked files by default
