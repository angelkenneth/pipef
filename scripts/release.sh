#!/usr/bin/env bash
# Runs the full release in one shot (RELEASING.md > Every Release > Manual, steps 1-6)
# Needs a clean tree on main and a PyPI token in .env or the environment
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

start_time=$(date +%s)

# Guard: a dirty tree would get bundled into the bump commit, and releases only come off main
if [ -n "$(git status --porcelain)" ]; then
  echo "working tree has staged or unstaged changes — commit or stash them before releasing" >&2
  exit 1
fi
if [ "$(git branch --show-current)" != "main" ]; then
  echo "not on main — switch to it before releasing" >&2
  exit 1
fi

# Guard: fail now, not after the version has already been bumped and tagged
if [ -z "${UV_PUBLISH_TOKEN:-}" ] && ! grep -q '^UV_PUBLISH_TOKEN="pypi-' .env 2>/dev/null; then
  echo "no PyPI token — set UV_PUBLISH_TOKEN in .env (see .env.example)" >&2
  exit 1
fi

# Step 1: run the suite across every installed interpreter
uv run poe test-all

# Step 2: bump the version, write CHANGELOG.md, commit, and tag vX.Y.Z
uv run poe bump --yes
version=$(uv version --short)

# Step 3: re-lock so uv.lock's embedded project version doesn't drift out of sync, then commit it
uv lock
git add uv.lock
git commit -m "chore(na-0): synced uv.lock to version $version"

# Step 4: build, twine-check, and upload to PyPI
uv run poe publish

# Step 5: push the commits and the tag
git push --follow-tags

elapsed=$(( $(date +%s) - start_time ))
echo "released v$version in $(printf '%02d:%02d' $((elapsed / 60)) $((elapsed % 60)))"
