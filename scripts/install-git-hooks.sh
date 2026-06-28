#!/usr/bin/env bash
# Install git hooks for the roblox monorepo (optional, run once locally).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOKS_DIR="$ROOT/.githooks"
TARGET="$ROOT/.git/hooks/pre-commit"

if [[ ! -d "$ROOT/.git" ]]; then
	echo "Not a git repository: $ROOT"
	exit 1
fi

mkdir -p "$HOOKS_DIR"

cat >"$HOOKS_DIR/pre-commit" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

mapfile -t place_files < <(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(rbxlx|rbxm)$' || true)

if ((${#place_files[@]} == 0)); then
	exit 0
fi

SCANNER=""
for candidate in "$ROOT/games/"*/scripts/scan-place-security.py; do
	if [[ -f "$candidate" ]]; then
		SCANNER="$candidate"
		break
	fi
done

if [[ -z "$SCANNER" ]]; then
	echo "No scan-place-security.py found under games/*/scripts/ — skipping place scan"
	exit 0
fi

echo "Running place security scan on staged Roblox files..."
if ! python3 "$SCANNER" "${place_files[@]}"; then
	echo ""
	echo "Commit blocked: fix CRITICAL findings before committing place/model files."
	exit 1
fi
EOF

chmod +x "$HOOKS_DIR/pre-commit"
ln -sf "../../.githooks/pre-commit" "$TARGET"
chmod +x "$HOOKS_DIR/pre-commit"

echo "Installed pre-commit hook -> .githooks/pre-commit"
