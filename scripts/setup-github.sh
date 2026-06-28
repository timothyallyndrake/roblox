#!/usr/bin/env bash
# Configure GitHub branches, rulesets, and labels for timothyallyndrake/roblox.
# Requires: gh auth login, repo admin access.
set -euo pipefail

REPO="${GITHUB_REPO:-timothyallyndrake/roblox}"
CORE_RULESET_ID=""
PEER_RULESET_ID=""

lookup_ruleset_id() {
	local name="$1"
	gh api "repos/$REPO/rulesets" --jq ".[] | select(.name == \"${name}\") | .id" | head -1
}

apply_core_ruleset() {
	local payload
	payload="$(cat <<'EOF'
{
  "name": "protected-branches-core-gates",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/dev", "refs/heads/prod"],
      "exclude": []
    }
  },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false,
        "allowed_merge_methods": ["merge", "squash"]
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": true,
        "do_not_enforce_on_create": true,
        "required_status_checks": [
          { "context": "Studio Docs Validation" },
          { "context": "Conventional Commit Messages" },
          { "context": "PR Title Conventional" },
          { "context": "Merge Method Acknowledgement" }
        ]
      }
    }
  ]
}
EOF
)"

	CORE_RULESET_ID="$(lookup_ruleset_id "protected-branches-core-gates")"
	if [[ -n "$CORE_RULESET_ID" ]]; then
		echo "Updating ruleset protected-branches-core-gates (id $CORE_RULESET_ID)..."
		gh api "repos/$REPO/rulesets/${CORE_RULESET_ID}" --method PUT --input - <<<"$payload" >/dev/null
	else
		echo "Creating ruleset protected-branches-core-gates..."
		gh api "repos/$REPO/rulesets" --method POST --input - <<<"$payload" >/dev/null
	fi
}

apply_peer_review_ruleset() {
	local enforcement="${1:-disabled}"
	local payload
	payload="$(cat <<EOF
{
  "name": "protected-branches-peer-review",
  "target": "branch",
  "enforcement": "${enforcement}",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/dev", "refs/heads/prod"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": true,
        "allowed_merge_methods": ["merge", "squash"]
      }
    }
  ]
}
EOF
)"

	PEER_RULESET_ID="$(lookup_ruleset_id "protected-branches-peer-review")"
	if [[ -n "$PEER_RULESET_ID" ]]; then
		echo "Updating ruleset protected-branches-peer-review (enforcement=${enforcement})..."
		gh api "repos/$REPO/rulesets/${PEER_RULESET_ID}" --method PUT --input - <<<"$payload" >/dev/null
	else
		echo "Creating ruleset protected-branches-peer-review (enforcement=${enforcement})..."
		gh api "repos/$REPO/rulesets" --method POST --input - <<<"$payload" >/dev/null
	fi
}

create_labels() {
	echo "Creating GitHub labels..."
	for spec in \
		"feat:0E8A16" "fix:D73A4A" "chore:FBCA04" \
		"phase-00:5319E7" "phase-01:5319E7" "phase-02:5319E7" \
		"type:playtest:F9D0C4" "type:playtest-ready:F9D0C4" "type:docs:0075CA" \
		"gate:blocked:B60205" "agent:producer:0E8A16"; do
		name="${spec%%:*}"
		color="${spec##*:}"
		gh label create "$name" --repo "$REPO" --color "$color" --force 2>/dev/null || true
	done
	for i in $(seq -w 3 17); do
		gh label create "phase-$i" --repo "$REPO" --color "5319E7" --force 2>/dev/null || true
	done
}

echo "=== GitHub setup for $REPO ==="

echo "Setting default branch to dev..."
gh api "repos/$REPO" -X PATCH -f default_branch=dev >/dev/null 2>&1 || echo "(repo may not exist yet — create repo first)"

create_labels

case "${1:-}" in
--apply-rulesets)
	apply_core_ruleset
	apply_peer_review_ruleset "disabled"
	echo "Rulesets applied. Core gates: ACTIVE. Peer review: DISABLED."
	;;
--enable-peer-review)
	apply_peer_review_ruleset "active"
	echo "Peer review ENABLED."
	;;
--disable-peer-review)
	apply_peer_review_ruleset "disabled"
	echo "Peer review DISABLED."
	;;
"")
	echo ""
	echo "Optional:"
	echo "  $0 --apply-rulesets"
	echo "  $0 --enable-peer-review"
	echo "  $0 --disable-peer-review"
	;;
*)
	echo "Unknown option: $1"
	exit 1
	;;
esac

echo "Done."
