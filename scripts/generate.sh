#!/usr/bin/env bash

set -x

echo "Downloading latest YNAB API OpenAPI spec...";
wget https://api.ynab.com/papi/open_api_spec.yaml -O ./open_api_spec.yaml

echo "Running openapi-generator generate (sync clients)..."

openapi-generator generate -i ./open_api_spec.yaml -g python -t ./templates -c openapi-generator-config.yaml -o ./

echo "Running openapi-generator generate (async clients + renaming)..."
async_output="$(mktemp -d)"
trap 'rm -rf "$async_output"' EXIT
openapi-generator generate -i ./open_api_spec.yaml -g python -t ./templates -c openapi-generator-config-async.yaml -o "$async_output"
.venv/bin/python scripts/generate_async.py "$async_output"

echo "Success!"
