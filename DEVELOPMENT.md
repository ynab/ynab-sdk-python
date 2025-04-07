# Development

## Setup

- Install Poetry: `pip install poetry`
- Install dependencies: `poetry install`
- Install [OpenAPI Generator](https://openapi-generator.tech/) (on macOS: `brew install openapi-generator`)
- Run tests: `poetry run pytest`

## Generating

1. Change `packageVersion` in `openapi-generator-config.yaml`
1. Run `scripts/generate.sh`.

## Publishing

Run the "Publish" GitHub Actions workflow.