---
name: rgs-loop-start
description: Starts an RGS R&D loop run (auto-creates run folder, brief, state). Use for /rgs-loop-start <type> [brief text].
disable-model-invocation: true
---

## Start a loop (never manual mkdir/cp)

```bash
python3 scripts/rgs.py loop start <type> [--game SLUG] [--brief "plain english goals"]
```

**Types (aliases):** discovery, compliance, gdd, vertical-slice, alpha, beta, launch, liveops, ...

## Then immediately

1. Read manifest from `studio/loops/`
2. Follow `.cursor/skills/loop-runner/SKILL.md` execution protocol
3. Use WebSearch on research steps
4. Discord notify: `python3 scripts/studio-discord-bridge.py notify ...`
5. On grill: `/rgs-grill` one question → Discord `waiting_on_ep`

If EP provided brief text in the command, pass via `--brief`.

