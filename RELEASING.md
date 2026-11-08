## Releasing

Public distribution on [PyPI](https://pypi.org/project/pipef/), as a wheel + sdist built by hatchling. Releases
go out from a local machine, not CI

## First-Time Setup

1. Create an API token at [PyPI](https://pypi.org/manage/account/token/) — "Entire account" scope for a first
   upload, then swap it for one scoped to `pipef`
2. Copy `.env.example` to `.env` and set `UV_PUBLISH_TOKEN` to that token:
   ```bash
   cp .env.example .env
   ```
3. Run `uv sync` so Commitizen, tox, and twine are available

## Every Release

### Automatic

Steps 1-6 of [Manual](#manual) below, run in one shot:

```bash
scripts/release.sh
```

It refuses to start on a dirty tree, off `main`, or without a PyPI token, so a bad start never leaves a
half-bumped version behind

### Manual

1. Run the suite across the whole supported range:
   ```bash
   uv run poe test-all
   ```
2. Bump the version from the commit history — Commitizen updates `pyproject.toml` and
   `src/pipef/__init__.py`, writes `CHANGELOG.md`, commits, and tags `vX.Y.Z`:
   ```bash
   uv run poe bump
   ```
   Only `feat`, `fix`, `perf`, and `refactor` commits bump the version, so a docs-only history has nothing to
   release
3. Re-lock so `uv.lock` picks up the new version, then commit it:
   ```bash
   uv lock
   git add uv.lock
   git commit -m "chore(na-0): synced uv.lock to version $(uv version --short)"
   ```
4. Clean `dist/`, build, twine-check, and upload to PyPI:
   ```bash
   uv run poe publish
   ```
5. Push the commits and the tag:
   ```bash
   git push --follow-tags
   ```
6. Check [pypi.org/project/pipef](https://pypi.org/project/pipef/) shows the new version

## When a Release Fails Midway

PyPI never lets you re-upload a version, so don't re-run the bump. If `publish` failed after the bump, fix the
cause and re-run `uv run poe publish`, then push. If the upload succeeded but the push didn't, only push
