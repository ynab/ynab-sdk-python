# Development

## Setup

- Install Poetry: `pipx install poetry`
- Install dependencies: `poetry install`
- Install [OpenAPI Generator](https://openapi-generator.tech/) (on macOS: `brew install openapi-generator`)
- Run tests: `poetry run pytest`

## Generating

1. Run `scripts/generate.sh`.  This will generate the API client from the latest OpenAPI spec. Once generated, you should open a PR and merge the changes.

Alternatively, run `scripts/generate-and-pr.sh` to do the above and automate the PR. It wraps `generate.sh`, detects the old → new spec version, and (after you confirm) ensures you're on a `gen-<version>` branch, then commits, pushes, and opens a PR against `main` via `git`/`gh`, printing the PR URL. The [`claude`](https://docs.claude.com/en/docs/claude-code/overview) CLI is used only to draft the PR description from the spec diff. Requires the `gh` and `claude` CLIs to be installed and authenticated.

## Publishing

Run the "Publish" GitHub Actions workflow.