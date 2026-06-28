# Studio Loop Engine

A reusable **Research & Development loop system** for the virtual game studio. Start a loop on a concept, let agents research and iterate autonomously, get **Discord notifications** when output is ready or when the loop needs you.

## Concepts

| Term | Meaning |
|------|---------|
| **Loop** | A packaged workflow: agents, steps, research, stop criteria, outputs |
| **Manifest** | Machine-readable loop definition (`manifest.md` + YAML frontmatter) |
| **Run** | One execution of a loop (`studio/loops/runs/<run-id>/`) |
| **Brief** | EP natural-language goals for this run → parsed into structured criteria |
| **Handoff** | Output of loop A becomes input of loop B |
| **Game scope** | `game_slug: null` = studio-wide; `starlit-conservatory` = under `games/<slug>/` |

## How EP uses it

1. Pick a loop from [registry.md](registry.md) (maps 1:1 to SDLC through issue creation)
2. Start a run: copy `templates/run-brief.template.md` → `runs/<run-id>/brief.md` (plain English goals)
3. Invoke **Loop Runner** agent (`.cursor/skills/loop-runner/SKILL.md`) with run id
4. Loop runs autonomously: web research → agent steps → `/grill-me` only when EP input required
5. **Discord** pings you each step + when **waiting on EP** or **finished**
6. Approve handoff → next loop in chain

## Autonomy model

**As autonomous as possible.** EP is not asked at every step.

| Pause reason | Discord event | EP action |
|--------------|---------------|-----------|
| Step completed | `step_complete` | Optional read summary |
| Grill session needed | `waiting_on_ep` | Answer one grilling question |
| Stop criteria met | `finished` | Review deliverables, approve handoff |
| Compliance block | `blocked` | Review flag, override or kill pitch |
| Max iterations hit | `finished` | Review best-effort output |

**Phase gates** (SDLC) = EP sign-off between major loops — not between every agent message.

## Grill-me integration

When a step has `grill: true` in the manifest:

1. Assigned agent asks **one question** (with recommendation)
2. Loop **stops**, Discord `waiting_on_ep`
3. EP answers → logged to `runs/<run-id>/grilling-log.md`
4. Loop resumes

## Game awareness (multi-game monorepo)

```yaml
game_slug: null          # studio-level (e.g. discovery before title locked)
game_slug: cosmic-garden # all outputs under games/cosmic-garden/ + run state
```

Run state always records `game_slug`. Loops after Phase 06 read/write `games/<slug>/docs/` and create issues labeled `game:<slug>`.

## File layout

```
studio/loops/
├── README.md              ← you are here
├── ENGINE.md              ← full spec
├── registry.md            ← all loops ↔ SDLC
├── config/
│   ├── config.example.json
│   └── .gitignore         ← local webhook URL never committed
├── templates/
│   ├── loop.manifest.template.md
│   ├── run-brief.template.md
│   └── run-state.template.md
├── discovery/game-ideas/  ← example loop (Phase 01)
└── runs/<run-id>/         ← per-run artifacts (gitignored except README)
```

## Discord notifications

Set webhook in `studio/loops/config/local.json` (gitignored):

```json
{ "discord_webhook_url": "https://discord.com/api/webhooks/..." }
```

Or env var `STUDIO_DISCORD_WEBHOOK_URL`.

Run: `./scripts/studio-notify-discord.sh --event step_complete --run-id <id> --message "..."`

## Starting the game-ideas discovery loop

See [discovery/game-ideas/manifest.md](discovery/game-ideas/manifest.md).

```bash
RUN_ID="2026-06-28-discovery-game-ideas"
mkdir -p studio/loops/runs/$RUN_ID
cp studio/loops/templates/run-brief.template.md studio/loops/runs/$RUN_ID/brief.md
# Edit brief.md in plain English, then invoke Loop Runner skill
```

## Implementation reality (EP + agent pairing)

Loops **produce docs, decisions, and GitHub Issues** — not Luau. EP builds in Blender + Studio; agents implement issue code in paired sessions.
