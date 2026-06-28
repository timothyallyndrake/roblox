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

## Discord notifications (bidirectional)

### Outbound (webhook)

Loop steps post embeds via:

```bash
python3 scripts/studio-discord-bridge.py notify \
  --event waiting_on_ep --run-id "$RUN_ID" --loop discovery.game-ideas \
  --message "Creative Director Q1: ..."
```

Or `./scripts/studio-notify-discord.sh` (webhook-only wrapper).

### Inbound (bot — EP replies in channel)

Webhooks are **one-way**. For EP to **answer grill questions in Discord**, run the bridge listener:

```bash
python3 scripts/studio-discord-bridge.py listen
```

When a run is `WAITING_ON_EP`:

1. Bot posts question embed (footer contains `run:<run-id>`)
2. EP replies in channel (include `run:<run-id>` or reply when only one run is waiting)
3. Listener writes answer to `runs/<run-id>/grilling-log.md`, sets status → `RUNNING`
4. Loop Runner resumes on next agent session

### Config (gitignored)

Copy `config.example.json` → `config/local.json`:

```json
{
  "discord_webhook_url": "https://discord.com/api/webhooks/...",
  "discord_bot_token": "BOT_TOKEN",
  "discord_channel_id": "CHANNEL_ID",
  "discord_bot_name": "Convo AI"
}
```

**Never commit `local.json`.** Regenerate bot token if exposed.

### Discord events

| Event | When |
|-------|------|
| `step_complete` | After each loop step |
| `waiting_on_ep` | Grill question posted — **reply in channel** |
| `finished` | Stop criteria met |
| `blocked` | Compliance block |
| `error` | Loop failure |

## Starting the game-ideas discovery loop

**EP command:** `/rgs-loop-discovery <your goals in plain English>`

Agent runs RGS — no manual mkdir/cp. See [rgs-commands.md](../docs/company/rgs-commands.md) and [discovery/game-ideas/manifest.md](discovery/game-ideas/manifest.md).

## Implementation reality (EP + agent pairing)

Loops **produce docs, decisions, and GitHub Issues** — not Luau. EP builds in Blender + Studio; agents implement issue code in paired sessions.
