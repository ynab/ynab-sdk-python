# AGENTS.md

See [DEVELOPMENT.md](DEVELOPMENT.md) for setup, generating the client, and publishing.

## Version bumps

A change that alters what consumers install or run must bump the package version in the same PR, so it can be published without a follow-up PR. This includes runtime dependency ranges in `pyproject.toml` or `templates/pyproject.mustache`, generated code under `ynab/`, and other templates.

- Run `python3 scripts/update_version.py patch` (or `minor` / `major`). It updates both `pyproject.toml` and `openapi-generator-config.yaml`; never edit only one.
- Use `patch` for dependency range changes and bug fixes, `minor` for new API surface, `major` for breaking changes.
- `scripts/generate.sh` already bumps the version, so don't bump again after running it.
- Don't bump for changes that don't ship to consumers: dev and test dependencies, lockfile-only updates, CI workflows, docs.
