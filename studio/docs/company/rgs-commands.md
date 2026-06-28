# RGS Commands — Roblox Game Studio

**RGS** = Roblox Game Studio orchestrator. EP uses **`/rgs-*` skills** in Cursor — never manual loop shell setup.

**Entry point:** `/rgs-orchestrator` or `/rgs-help`

**CLI (agents run this):** `python3 scripts/rgs.py <command>`

---

## Studio overview

| Skill | CLI | Purpose |
|-------|-----|---------|
| `/rgs-orchestrator` | — | Master router — use when unsure |
| `/rgs-help` | `help` | Command catalog |
| `/rgs-status` | `status` | Phase, game, active runs, WAITING_ON_EP |
| `/rgs-context` | `context` | Living studio state |
| `/rgs-phase-status` | `phase status` | SDLC phase index |

---

## Staff (virtual agents)

| Skill | CLI | Purpose |
|-------|-----|---------|
| `/rgs-list-staff` | `staff list` | All 25+ agent roles |
| `/rgs-show-staff` | `staff show <slug>` | One agent's skill file |
| `/rgs-update-staff` | — | Edit agent skill + roster (agent-assisted) |

Staff skills live at `.cursor/skills/<slug>/` (game-designer, producer, …).

---

## Games (monorepo)

| Skill | CLI | Purpose |
|-------|-----|---------|
| `/rgs-list-games` | `games list` | `games/<slug>/` folders + bootstrap status |

Game slug locked in CONTEXT.md after discovery handoff.

---

## Loops (R&D engine)

| Skill | CLI | Purpose |
|-------|-----|---------|
| `/rgs-list-loops` | `loops list` | All SDLC loops (registry) |
| `/rgs-list-runs` | `runs list` | All loop run folders |
| `/rgs-loop-start` | `loop start <type>` | **Create run** (auto brief/state/research/) |
| `/rgs-loop-continue` | `loop continue [run_id]` | **Dispatch Cursor `agent` CLI** — execute next manifest step |
| `/rgs-loop-status` | `loop status [run_id]` | One run or all |

### Loop shortcuts

| Skill | Starts loop |
|-------|-------------|
| `/rgs-loop-discovery` | `discovery.game-ideas` (Phase 01) |
| `/rgs-loop-compliance` | `compliance.feasibility` (Phase 02) |
| `/rgs-loop-gdd` | `planning.gdd` (Phase 03) |
| `/rgs-loop-vertical-slice` | `build.vertical-slice` (Phase 07) |

**Aliases:** `discovery`, `compliance`, `gdd`, `vertical-slice`, `alpha`, `beta`, `launch`, `liveops`, …

### Example — start discovery (EP says this, not shell)

```
/rgs-loop-discovery cozy pastel sim, Bee Swarm reference, 3 finalists score 8+
```

Agent runs:
```bash
python3 scripts/rgs.py loop start discovery --brief "cozy pastel sim, Bee Swarm reference, 3 finalists score 8+"
```
Then `/rgs-loop-continue` dispatches the Cursor `agent` CLI to execute research steps.

---

## Agent providers (pluggable backends)

| Skill | CLI | Purpose |
|-------|-----|---------|
| — | `agent status` | Check Cursor/Ollama/OpenClaw provider health |
| — | `agent providers` | List available backends |

Default: **Cursor `agent` CLI** (headless, `-p --trust`). Swap via `studio/config/agent.local.json`.

See [agent-providers.md](agent-providers.md).

## Discord

| Skill | Purpose |
|-------|---------|
| `/rgs-discord-listen` | Background listener for EP replies |
| `/rgs-discord-notify` | Post step notification |

Config: `studio/loops/config/local.json` (gitignored)

---

## Grilling

| Skill | Purpose |
|-------|---------|
| `/rgs-grill` | One question + recommendation; logs to run grilling-log |

Used inside loops when EP taste input required.

---

## Typical EP session

1. `/rgs-status` — where are we?
2. `/rgs-loop-discovery <your goals in plain English>`
3. `/rgs-discord-listen` (once, background)
4. `/rgs-loop-continue` — agent researches, notifies Discord
5. Answer in Discord or chat when `/rgs-grill` fires
6. `/rgs-loop-status` — check progress
7. When finished → pick game → `/rgs-loop-compliance`

---

## Architecture

```
EP → /rgs-* skills → scripts/rgs.py → studio/loops/ + CONTEXT.md
                    → agent_providers/ → Cursor `agent` CLI (default)
                    → (future: Ollama, OpenClaw)
                    → loop-runner protocol → staff skills → WebSearch
                    → Discord bridge → EP replies
                    → GitHub Issues (Producer, later loops)
```

See [loops/README.md](../loops/README.md) and [loops/ENGINE.md](../loops/ENGINE.md).
