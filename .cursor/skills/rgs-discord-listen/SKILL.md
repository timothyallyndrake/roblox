---
name: rgs-discord-listen
description: Start Discord listener for EP replies; auto-dispatches loop continue. Use for /rgs-discord-listen.
disable-model-invocation: true
---

Run in background:
```bash
python3 scripts/studio-discord-bridge.py listen
```

When EP replies in Discord while a run is `WAITING_ON_EP`, the listener **automatically** runs `python3 scripts/rgs.py loop continue <run_id>` — no Cursor action needed.

Tell EP:
- Reply in Discord channel when loops ask a question
- Leave listener running (tmux or launchd) for backyard/phone-only workflow
- See `studio/docs/company/discord-bridge.md` for always-on setup
