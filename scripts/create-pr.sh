#!/usr/bin/env bash
# Create a GitHub PR with the repo template footer (merge acknowledgement included).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

BASE="dev"
HEAD=""
TITLE=""
BODY_FILE=""
DRAFT=false

usage() {
	cat <<'EOF'
Usage: ./scripts/create-pr.sh --title "feat(scope): description" [options]

Options:
  --base BRANCH     Target branch (default: dev)
  --head BRANCH     Source branch (default: current branch)
  --body-file FILE  Markdown file for Summary + Test plan sections only
  --draft           Open as draft PR
  -h, --help        Show this help
EOF
}

while [[ $# -gt 0 ]]; do
	case "$1" in
	--base)
		BASE="$2"
		shift 2
		;;
	--head)
		HEAD="$2"
		shift 2
		;;
	--title)
		TITLE="$2"
		shift 2
		;;
	--body-file)
		BODY_FILE="$2"
		shift 2
		;;
	--draft)
		DRAFT=true
		shift
		;;
	-h | --help)
		usage
		exit 0
		;;
	*)
		echo "Unknown option: $1" >&2
		usage >&2
		exit 1
		;;
	esac
done

if [[ -z "$TITLE" ]]; then
	echo "Error: --title is required" >&2
	usage >&2
	exit 1
fi

if [[ -z "$HEAD" ]]; then
	HEAD="$(git branch --show-current)"
fi

if [[ "$HEAD" == "$BASE" ]]; then
	echo "Error: head and base are both '$BASE'" >&2
	exit 1
fi

MERGE_METHOD="squash"
if [[ "$HEAD" == release-please--* ]]; then
	MERGE_METHOD="squash"
elif [[ "$BASE" == "prod" && "$HEAD" == "dev" ]]; then
	MERGE_METHOD="merge"
elif [[ "$BASE" == "dev" && "$HEAD" == "prod" ]]; then
	MERGE_METHOD="merge"
elif [[ "$BASE" == "dev" ]]; then
	MERGE_METHOD="squash"
fi

TEMPLATE="$ROOT/.github/pull_request_template.md"
FOOTER="$(awk 'BEGIN{p=0} /^---$/{p=1; print; next} p{print}' "$TEMPLATE")"

SQUASH_BOX="- [ ] I will use Squash and merge"
MERGE_BOX="- [ ] I will use Create a merge commit"
if [[ "$MERGE_METHOD" == "squash" ]]; then
	SQUASH_BOX="- [x] I will use Squash and merge"
else
	MERGE_BOX="- [x] I will use Create a merge commit"
fi

FOOTER="${FOOTER//$'- [ ] I will use Squash and merge'/$SQUASH_BOX}"
FOOTER="${FOOTER//$'- [ ] I will use Create a merge commit'/$MERGE_BOX}"

TMP_BODY="$(mktemp)"
trap 'rm -f "$TMP_BODY" "${TMP_BODY}.full"' EXIT

if [[ -n "$BODY_FILE" ]]; then
	cat "$BODY_FILE" >"$TMP_BODY"
else
	cat >"$TMP_BODY" <<'EOF'
## Summary

- <!-- fill in -->

## Test plan

- [ ] Studio validation / game CI as applicable

## Pre-merge checklist (required)

- [ ] PR title uses Conventional Commit format
- [ ] `studio/CONTEXT.md` updated if needed

## Waivers (if any)

- None

EOF
fi

{
	cat "$TMP_BODY"
	printf '\n%s\n' "$FOOTER"
} >"${TMP_BODY}.full"

ARGS=(pr create --base "$BASE" --head "$HEAD" --title "$TITLE" --body-file "${TMP_BODY}.full")
if [[ "$DRAFT" == true ]]; then
	ARGS+=(--draft)
fi

echo "Creating PR: $HEAD -> $BASE (merge method: $MERGE_METHOD)"
gh "${ARGS[@]}"
