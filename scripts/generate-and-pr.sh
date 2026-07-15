#!/usr/bin/env bash
#
# Regenerate the SDK from the latest YNAB API spec, then optionally open a PR.
#
# Wraps scripts/generate.sh. After regenerating it detects the old -> new spec
# version and, if you confirm, ensures you're on a gen-<version> branch and
# hands the commit + PR off to `claude`, which writes a real summary of the
# functional spec changes. Requires the `claude` CLI to be installed.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRIPT_DIR="$REPO_ROOT/scripts"
SPEC="$REPO_ROOT/open_api_spec.yaml"

cd "$REPO_ROOT"

# Extract info.version from an OpenAPI spec on stdin (the 2-space-indented
# `version:` inside the top-level `info:` block, not `openapi:` or nested ones).
spec_version() {
  awk '/^info:/{f=1} f && /^  version:/{print $2; exit}'
}

OLD_VERSION="$(git show HEAD:open_api_spec.yaml 2>/dev/null | spec_version || true)"

# Regenerate: downloads the latest spec and runs openapi-generator.
bash "$SCRIPT_DIR/generate.sh"

NEW_VERSION="$(spec_version < "$SPEC")"

if [[ -z "$(git status --porcelain)" ]]; then
  echo
  echo "No changes after regeneration — spec ${NEW_VERSION:-unknown} is already up to date. Nothing to do."
  exit 0
fi

echo
echo "Regeneration produced changes. Spec version: ${OLD_VERSION:-unknown} -> ${NEW_VERSION:-unknown}"
git status --short
echo

read -r -p "Create a pull request for these changes? [y/N] " reply
case "$reply" in
  [yY] | [yY][eE][sS]) ;;
  *)
    echo "Leaving the regenerated changes uncommitted in the working tree. Done."
    exit 0
    ;;
esac

# Never commit on a protected branch: if we're on one, create a fresh
# gen-<version> branch (the uncommitted regen changes carry over). Otherwise
# stay on the current feature branch.
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
DESIRED="gen-${NEW_VERSION//./-}"
case "$BRANCH" in
  main | master | develop)
    target="$DESIRED"
    if git show-ref --verify --quiet "refs/heads/$target"; then
      n=2
      while git show-ref --verify --quiet "refs/heads/${DESIRED}-${n}"; do n=$((n + 1)); done
      target="${DESIRED}-${n}"
    fi
    echo "On protected branch '$BRANCH'; creating and switching to '$target'."
    git switch -c "$target"
    ;;
  *)
    echo "Committing on current branch: '$BRANCH'."
    ;;
esac

echo
echo "Handing off to Claude to write the commit + PR (this may take a minute)..."
echo

# Scope the spawned Claude to only the tools the commit/PR flow needs so the
# non-interactive run doesn't stall on approval prompts, without granting a
# blanket permission bypass.
ALLOWED_TOOLS="Bash Read Edit Write Grep Glob Skill TodoWrite"

PROMPT="The working tree contains a regeneration of this SDK from the YNAB OpenAPI spec, version ${OLD_VERSION:-unknown} -> ${NEW_VERSION:-unknown} (produced by scripts/generate.sh).

Do the following, and nothing else:
1. Inspect the diff, focusing on open_api_spec.yaml and docs/ for FUNCTIONAL API changes (new or changed fields, endpoints, enums, response codes). Ignore the mechanical per-file header/version churn under ynab/.
2. Commit ALL changes. The subject should note the spec regeneration and version bump (${OLD_VERSION:-unknown} -> ${NEW_VERSION:-unknown}); the body should summarize the functional changes (or state it is a routine refresh if there are none).
3. Push and open a PR against main with a clear title and description. Do NOT request any reviewers.
4. Print the PR URL on the final line.

Do not modify any generated code — only commit and open the PR."

claude -p "$PROMPT" --allowedTools $ALLOWED_TOOLS

echo
echo "Done."
