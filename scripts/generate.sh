#!/usr/bin/env bash

set -x

echo "Downloading latest YNAB API OpenAPI spec...";
wget https://api.ynab.com/papi/open_api_spec.yaml -O ./open_api_spec.yaml

echo "Running openapi-generator generate..."
openapi-generator generate -i ./open_api_spec.yaml -g python  -t ./templates -c openapi-generator-config.yaml -o ./

echo "Success!"