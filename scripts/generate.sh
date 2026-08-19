#!/usr/bin/env bash
#
# Regenerate the API client from the latest YNAB OpenAPI spec and bump the
# package version.
#
# Usage: scripts/generate.sh [major|minor|patch|none]   (defaults to minor)
#
# The generator embeds the version in pyproject.toml and the client itself, so
# the bump has to happen before generating.  Pass "none" to regenerate without
# bumping.

set -euo pipefail

VERSION_TYPE="${1:-minor}"
case "$VERSION_TYPE" in
  major | minor | patch | none) ;;
  *)
    echo "Invalid version type: $VERSION_TYPE (expected major, minor, patch, or none)" >&2
    exit 1
    ;;
esac

if [[ "$VERSION_TYPE" != "none" ]]; then
  echo "Bumping package version ($VERSION_TYPE)..."
  NEW_VERSION="$(python3 scripts/update_version.py "$VERSION_TYPE")"
  echo "New package version: $NEW_VERSION"
fi

echo "Downloading latest YNAB API OpenAPI spec..."
wget https://api.ynab.com/papi/open_api_spec.yaml -O ./open_api_spec.yaml

echo "Running openapi-generator generate..."
openapi-generator generate -i ./open_api_spec.yaml -g python -t ./templates -c openapi-generator-config.yaml -o ./

echo "Success!"
