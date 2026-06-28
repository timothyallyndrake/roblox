---
name: loop-runner
description: Orchestrate studio R&D loops — research, agent steps, stop criteria, Discord notify, grill-me. Use when EP says start loop, run discovery, or continue run.
---

# Loop Runner

## Mandate

Execute studio loops defined in `studio/loops/**/manifest.md`. Maximum autonomy until stop criteria, EP grill, or handoff approval.

## Before you start

1. Read [`studio/CONTEXT.md`](../../../studio/CONTEXT.md)
2. Read [`studio/loops/ENGINE.md`](../../../studio/loops/ENGINE.md)
3. Read the target loop manifest
4. Read `studio/loops/runs/<run-id>/brief.md` if exists

## Starting a new run

**Use RGS — EP never runs mkdir/cp manually:**

```
/rgs-loop-discovery <optional brief in plain English>
```

Agent executes:
```bash
python3 scripts/rgs.py loop start discovery [--brief "..."]
```

Then `/rgs-loop-continue` to execute manifest steps.

See [rgs-commands.md](../../../studio/docs/company/rgs-commands.md).

## Execution protocol

1. **Load** manifest YAML + merge brief overrides → `criteria.json`
2. **Resolve game_slug** from brief, CONTEXT, or manifest default
3. **Run steps** in order; assign agents per manifest
4. **Research steps:** use WebSearch; cite sources in `runs/<id>/research/*.md`
5. **After each step:** append `log.md`; run `./scripts/studio-notify-discord.sh --event step_complete ...`
6. **Grill steps:** ask ONE question with recommendation; Discord `waiting_on_ep`; STOP until EP answers
7. **Evaluate stop criteria** after synthesize iterations
8. **On finish:** Discord `finished`; write `report.md`; update CONTEXT if needed

## Stop criteria types

| type | Meaning |
|------|---------|
| `max_iterations` | Cap research cycles |
| `deliverable_count` | N finalists in output doc |
| `min_score` | Rubric average ≥ threshold |
| `compliance_clear` | No high-risk without mitigation |
| `ep_approval` | Wait for EP explicit approve in state.md |

## Grill-me integration

When step has `Grill: true`:

- Follow `.cursor/skills/grill-me` / grilling skill: **one question**, recommendation included
- Log to `runs/<run-id>/grilling-log.md`
- Do not proceed until EP responds

## Discord notifications

```bash
./scripts/studio-notify-discord.sh \
  --event waiting_on_ep \
  --run-id "$RUN_ID" \
  --loop discovery.game-ideas \
  --message "Creative Director Q1: Which pitch front-runner?"
```

Config: `studio/loops/config/local.json` (copy from `config.example.json`) — gitignored.

## Loop catalog

| Loop ID | Manifest |
|---------|----------|
| `discovery.game-ideas` | `studio/loops/discovery/game-ideas/manifest.md` |
| _(see registry)_ | `studio/loops/registry.md` |

## Handoff

When loop `finished` and EP approves in `state.md`:

1. Set handoff fields in state
2. Notify Discord
3. EP or Runner starts `handoff.next_loop` with same or updated `game_slug`

## GitHub issues

Loops with `github.create_issues: true` — **Producer** creates issues via `gh issue create` with labels including `game:<slug>` and `phase-NN`.

## EP implementation model

Loops produce docs + issues. EP implements in Blender + Studio; pairs with **lead-roblox-engineer** per issue.
