# Discord Bridge — Remote Studio Control

EP can drive **loop R&D from Discord** without returning to Cursor. Long-term goal: full SDLC from phone/backyard; **loops are wired first**.

## Flow (loops)

```
Loop pauses (WAITING_ON_EP)
  → Discord webhook posts grill question
  → EP replies in channel
  → Listener captures reply
  → Auto-dispatches: python3 scripts/rgs.py loop continue <run_id>
  → Agent runs autonomously (Cursor CLI)
  → Discord webhook: step complete / waiting again / finished / error
```

## One-time setup

1. Copy `studio/loops/config/config.example.json` → `local.json`
2. Fill webhook URL, bot token, channel ID
3. Discord Developer Portal → Bot → enable **Message Content Intent**
4. Bot needs **View Channel** + **Read Message History** in the studio channel

## Start listener (required while loops run)

```bash
python3 scripts/studio-discord-bridge.py listen
```

Run in tmux, a dedicated Terminal tab, or via launchd (below). **One listener** handles all active runs.

## Replying in Discord

- Plain text is fine when only one run is `WAITING_ON_EP`
- Multiple runs: prefix with `run:2026-06-28-discovery-game-ideas`
- Examples: `A`, `B — Hearth & Haul`, `keep iterating — need more novel ideas`

The loop **resumes automatically** — do not run `/rgs-loop-continue` in Cursor unless debugging.

## Always-on listener (macOS launchd)

Save as `~/Library/LaunchAgents/com.robloxstudio.discord-bridge.plist` (adjust paths):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.robloxstudio.discord-bridge</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/python3</string>
    <string>/Users/tim/Repositories/timothyallyndrake/roblox/scripts/studio-discord-bridge.py</string>
    <string>listen</string>
  </array>
  <key>WorkingDirectory</key>
  <string>/Users/tim/Repositories/timothyallyndrake/roblox</string>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>/tmp/rgs-discord-bridge.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/rgs-discord-bridge.err</string>
</dict>
</plist>
```

Load: `launchctl load ~/Library/LaunchAgents/com.robloxstudio.discord-bridge.plist`

Logs: `/tmp/rgs-discord-bridge.log`

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Reply ignored, empty content | Enable Message Content Intent |
| HTTP 403 on bot API | Bot token invalid or missing User-Agent (fixed in bridge script) |
| Reply recorded but nothing after | Old listener (pre auto-dispatch) or stuck `dispatch_in_flight` — check `/tmp/rgs-discord-dispatch.log` |
| Only 2 Discord messages per reply | Expected today: "resuming…" then "done/waiting". Per-step pings = future enhancement |
| `dispatch_in_flight` stuck | `python3 scripts/rgs.py loop status <run_id>` — clear manually in `state.json` if needed |

## Roadmap (full Discord studio)

| Phase | Capability |
|-------|------------|
| **Now** | Loop grill → auto-continue → notify |
| Next | `/rgs-loop-start` triggers from Discord slash command |
| Next | Phase gate approvals + game slug lock from Discord |
| Later | Playtest feedback, issue triage, deploy pings — full SDLC without Cursor |

See [rgs-commands.md](rgs-commands.md) and [loops/README.md](../../loops/README.md).
