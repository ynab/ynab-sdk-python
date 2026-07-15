#!/usr/bin/env bash
#
# Regenerate the SDK from the latest YNAB API spec, then optionally open a PR.
#
# Wraps scripts/generate.sh. After regenerating it detects the old -> new spec
# version and, if you confirm, ensures you're on a gen-<version> branch, then
# commits, pushes, and opens a PR via git/gh. The `claude` CLI is used only to
# draft the PR description from the spec diff. Requires the `gh` and `claude`
# CLIs to be installed and authenticated.

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
    BRANCH="$target"
    ;;
  *)
    echo "Committing on current branch: '$BRANCH'."
    ;;
esac

# Commit and push the regenerated client.
git add -A
git commit \
  -m "Regenerate SDK from server specification version ${NEW_VERSION}" \
  -m "Regenerated the client from the YNAB API spec ${NEW_VERSION} (previously ${OLD_VERSION:-unknown})."
git push -u origin "$BRANCH"

# Use claude only to draft the PR description from the meaningful diff (the spec
# and docs; the per-file churn under ynab/ is noise). Everything else is gh/git.
echo
echo "Drafting the PR description with Claude..."
DIFF="$(git diff "origin/main...HEAD" -- open_api_spec.yaml docs/; echo; git diff --stat "origin/main...HEAD")"

BODY_FILE="$(mktemp)"
trap 'rm -f "$BODY_FILE"' EXIT

claude -p "Write a GitHub pull request description for a regeneration of the YNAB Python SDK from the YNAB OpenAPI spec (version ${OLD_VERSION:-unknown} -> ${NEW_VERSION}).

Summarize the FUNCTIONAL API changes (new or changed fields, endpoints, enums, response codes) from the diff below, focusing on open_api_spec.yaml and docs/. If there are no functional changes, say it is a routine spec-generation refresh. Ignore the mechanical per-file header/version churn under ynab/.

Output ONLY the PR description as Markdown — no preamble and no surrounding code fence. Do not use any tools.

Diff:
${DIFF}" > "$BODY_FILE"

if [[ ! -s "$BODY_FILE" ]]; then
  echo "Regenerated the client from the YNAB API spec ${NEW_VERSION} (previously ${OLD_VERSION:-unknown})." > "$BODY_FILE"
fi

# Open the PR (no reviewers). gh prints the PR URL.
gh pr create \
  --base main \
  --head "$BRANCH" \
  --title "Regenerate SDK from server specification version ${NEW_VERSION}" \
  --body-file "$BODY_FILE"

echo
echo "Done."
