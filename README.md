## Blank UV Project

Contains ad hoc scriupts, logs, etc.

## Prerequisites

1. [asdf](https://asdf-vm.com/guide/getting-started.html)

## TLDR

```bash
# Run after cloning
asdf install && \
uv sync && \
uv run poe pre-commit-install && \
cp .env.example .env

# Run all Code Quality Assurance
uv run poe cqa
```

## Setup

1. Clone this repo

2. Install the pinned tool versions via asdf:

    ```bash
    asdf plugin add uv
    asdf plugin add python
    asdf install
    ```

3. Sync dependencies

    ```bash
    uv sync
    ```

4. Install Git hooks for CQA, if you plan to contribute code to this project:

    ```bash
    uv run poe pre-commit-install
    ```

5. Done

## Git Commit CLI

See: [Commitizen > Create Commits](https://commitizen-tools.github.io/commitizen/#create-commits)

```bash
uv run poe commit
```

## References

1. [.gitignore](https://www.toptal.com/developers/gitignore?templates=node,python,intellij+all,macos,windows)
2. [Stylising your Python code: An introduction to linting and formatting](https://www.jumpingrivers.com/blog/python-linting-guide/)
3. [Pylint > Pre-commit integration](https://pylint.pycqa.org/en/stable/user_guide/installation/pre-commit-integration.html)
4. [Ultimate pre-commit Configuration for Python](https://www.hrekov.com/blog/pre-commit-configuration-python)
5. [How to Use Poe the Poet as a Task Runner with uv](https://pydevtools.com/handbook/how-to/how-to-use-poe-the-poet-as-a-task-runner-with-uv/)
6. [commitizen > Pre-commit Integration](https://github.com/commitizen-tools/commitizen?tab=readme-ov-file#pre-commit-integration)
7. [Commitizen > Project-Specific Installation](https://commitizen-tools.github.io/commitizen/#project-specific-installation)
