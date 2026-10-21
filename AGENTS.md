# AGENTS.md

## Security update PRs

A PR that changes a runtime dependency for security reasons (raising a version floor in `pyproject.toml` and `templates/pyproject.mustache`, for example) must also bump the package version, so it can be published without a follow-up PR.

- Run `python3 scripts/update_version.py patch`. It updates both `pyproject.toml` and `openapi-generator-config.yaml`; never edit only one.
- Don't regenerate the client as part of a security update.
- Dev and test dependency updates don't ship to consumers and don't need a bump.
