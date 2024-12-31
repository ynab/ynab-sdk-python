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

1. Generate package: `poetry build`.
1. Run `poetry config pypi-token.pypi YOUR_PYPI_API_TOKEN`
1. Upload package: `poetry publish --build`.