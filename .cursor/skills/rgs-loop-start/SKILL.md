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

```bash
python3 scripts/rgs.py loop continue
```

Dispatches **Cursor `agent` CLI** to execute the loop (not inline in this chat).

If EP provided brief text in the command, pass via `--brief`.

See [agent-providers.md](../../../studio/docs/company/agent-providers.md).
