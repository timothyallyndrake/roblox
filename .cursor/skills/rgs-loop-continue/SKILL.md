---
name: rgs-loop-continue
description: Continues an active RGS loop run via Cursor agent CLI. Use for /rgs-loop-continue [run_id].
disable-model-invocation: true
---

## Dispatch loop worker (do not execute steps inline unless agent CLI fails)

```bash
python3 scripts/rgs.py loop continue [run_id]
```

This spawns the **Cursor `agent` CLI** with the loop-continue prompt. Session ID is stored in `state.json` for `--resume` on next continue.

## Options

- `--dry-run` — print prompt without dispatching
- `--provider cursor|ollama|openclaw` — override default backend

## If dispatch fails

1. `python3 scripts/rgs.py agent status` — check provider health
2. Fall back: read run state + follow `.cursor/skills/loop-runner/SKILL.md` in this chat session

## After dispatch

- Check `python3 scripts/rgs.py loop status [run_id]`
- If WAITING_ON_EP: `/rgs-grill` or answer in Discord
- Re-run continue when EP has replied

See [agent-providers.md](../../../studio/docs/company/agent-providers.md).
