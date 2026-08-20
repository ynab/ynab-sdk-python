# Development

## Setup

- Install Poetry: `pipx install poetry`
- Install dependencies: `poetry install`
- Install [OpenAPI Generator](https://openapi-generator.tech/) (on macOS: `brew install openapi-generator`)
- Run tests: `poetry run pytest`

## Generating

1. Run `scripts/generate.sh`.  This will bump the package version and generate the API client from the latest OpenAPI spec.  The bump defaults to `minor`; pass `major` or `patch` to change it (`scripts/generate.sh patch`), or `none` to regenerate without bumping.  Once generated, you should open a PR and merge the changes.

## Publishing

The version that gets published is whatever `pyproject.toml` on the `main` branch says, so publishing is two steps.

1. Merge a PR that sets the new version.  `scripts/generate.sh` does this for you.  For a release that does not involve re-generating the client, run `python3 scripts/update_version.py minor` (or `major` / `patch`), which updates `pyproject.toml` and `openapi-generator-config.yaml` without creating a commit or tag.
2. Run the "Publish" GitHub Actions workflow.  This builds, tests, and publishes that version to PyPI, then tags the commit and creates a GitHub release.

The workflow never changes the version itself.  If the version in `pyproject.toml` has already been released, the workflow fails before publishing anything.