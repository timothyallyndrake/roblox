#!/usr/bin/env bash
# Post a notification to Discord for studio loop events.
# Usage:
#   ./scripts/studio-notify-discord.sh --event finished --run-id 2026-06-28-discovery --loop discovery.game-ideas --message "Summary..."
#   ./scripts/studio-notify-discord.sh --event waiting_on_ep --run-id ... --message "Grill Q1 ready"
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EVENT=""
RUN_ID=""
LOOP_ID=""
GAME_SLUG=""
MESSAGE=""
WEBHOOK=""

usage() {
	cat <<'EOF'
Usage: studio-notify-discord.sh --event EVENT --run-id ID [options]

Events: step_complete | waiting_on_ep | finished | blocked | error

Options:
  --loop LOOP_ID       e.g. discovery.game-ideas
  --game SLUG          e.g. starlit-conservatory (optional)
  --message TEXT       Body text
  --webhook URL        Override webhook (else config/local.json or env)
EOF
}

while [[ $# -gt 0 ]]; do
	case "$1" in
	--event)
		EVENT="$2"
		shift 2
		;;
	--run-id)
		RUN_ID="$2"
		shift 2
		;;
	--loop)
		LOOP_ID="$2"
		shift 2
		;;
	--game)
		GAME_SLUG="$2"
		shift 2
		;;
	--message)
		MESSAGE="$2"
		shift 2
		;;
	--webhook)
		WEBHOOK="$2"
		shift 2
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

if [[ -z "$EVENT" || -z "$RUN_ID" ]]; then
	echo "Error: --event and --run-id required" >&2
	usage >&2
	exit 1
fi

if [[ -z "$WEBHOOK" ]]; then
	WEBHOOK="${STUDIO_DISCORD_WEBHOOK_URL:-}"
fi

CONFIG="$ROOT/studio/loops/config/local.json"
if [[ -z "$WEBHOOK" && -f "$CONFIG" ]]; then
	WEBHOOK="$(python3 -c "import json; print(json.load(open('$CONFIG')).get('discord_webhook_url',''))" 2>/dev/null || true)"
fi

if [[ -z "$WEBHOOK" ]]; then
	echo "Warning: No Discord webhook configured (set STUDIO_DISCORD_WEBHOOK_URL or studio/loops/config/local.json)" >&2
	exit 0
fi

case "$EVENT" in
step_complete) COLOR=3447003; TITLE="Loop Step Complete" ;;
waiting_on_ep) COLOR=16776960; TITLE="⏸ Waiting on EP" ;;
finished) COLOR=3066993; TITLE="✅ Loop Finished" ;;
blocked) COLOR=15158332; TITLE="🚫 Loop Blocked" ;;
error) COLOR=10038562; TITLE="❌ Loop Error" ;;
*) COLOR=9807270; TITLE="Studio Loop Event" ;;
esac

GAME_LINE=""
[[ -n "$GAME_SLUG" ]] && GAME_LINE="**Game:** \`$GAME_SLUG\`\\n"

PAYLOAD="$(python3 <<PYEOF
import json
payload = {
  "embeds": [{
    "title": "$TITLE",
    "color": $COLOR,
    "description": "**Loop:** \`$LOOP_ID\`\\n**Run:** \`$RUN_ID\`\\n${GAME_LINE}\\n$MESSAGE",
    "footer": {"text": "Roblox Virtual Game Studio — Loop Engine"}
  }]
}
print(json.dumps(payload))
PYEOF
)"

curl -sf -X POST "$WEBHOOK" \
	-H "Content-Type: application/json" \
	-d "$PAYLOAD" >/dev/null

echo "Discord notification sent ($EVENT)"
