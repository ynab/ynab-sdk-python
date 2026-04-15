# Development

## Setup

- Install Poetry: `pipx install poetry`
- Install dependencies: `poetry install`
- Install [OpenAPI Generator](https://openapi-generator.tech/) (on macOS: `brew install openapi-generator`)
- Run tests: `poetry run pytest`

## Generating

1. Run `scripts/generate.sh`.  This will generate the API client from the latest OpenAPI spec. Once generated, you should open a PR and merge the changes.

## Publishing

Run the "Publish" GitHub Actions workflow.