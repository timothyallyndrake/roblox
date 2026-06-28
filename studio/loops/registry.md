# Loop Registry — SDLC Coverage

Every SDLC step from discovery through **roadmap issue creation** has a loop. All loops are **game-aware** (`game_slug` optional until title locked).

| SDLC | Loop ID | Path | Game scoped | Handoff to |
|------|---------|------|-------------|------------|
| 01 | `discovery.game-ideas` | [discovery/game-ideas/](discovery/game-ideas/manifest.md) | No | `compliance.feasibility` |
| 02 | `compliance.feasibility` | compliance/feasibility/ | No → Yes* | `planning.gdd` |
| 03 | `planning.gdd` | planning/gdd/ | Yes | `creative.bible` |
| 04 | `creative.bible` | creative/bible/ | Yes | `technical.architecture` |
| 05 | `technical.architecture` | technical/architecture/ | Yes | `bootstrap.game-repo` |
| 06 | `bootstrap.game-repo` | bootstrap/game-repo/ | Yes | `build.vertical-slice` |
| 07 | `build.vertical-slice` | build/vertical-slice/ | Yes | `playtest.round-1` |
| 08 | `playtest.round-1` | playtest/round-1/ | Yes | `build.alpha` |
| 09 | `build.alpha` | build/alpha/ | Yes | `analytics.instrumentation` |
| 10 | `analytics.instrumentation` | analytics/instrumentation/ | Yes | `build.beta` |
| 11 | `build.beta` | build/beta/ | Yes | `playtest.round-2` |
| 12 | `playtest.round-2` | playtest/round-2/ | Yes | `quality.performance` |
| 13 | `quality.performance` | quality/performance/ | Yes | `marketing.prep` |
| 14 | `marketing.prep` | marketing/prep/ | Yes | `launch.prep` |
| 15 | `launch.prep` | launch/prep/ | Yes | `launch.ship` |
| 16 | `launch.ship` | launch/ship/ | Yes | `liveops.cadence` |
| 17 | `liveops.cadence` | liveops/cadence/ | Yes | — |

\* Phase 02 attaches `game_slug` once working title locked in discovery.

**Status:** `discovery.game-ideas` implemented. Others are manifest stubs — expand as each SDLC phase is reached.

## Loop categories

| Category | Purpose |
|----------|---------|
| `discovery/` | Research + ideation (studio-wide) |
| `compliance/` | Policy, feasibility gates |
| `planning/` | GDD, systems, economy |
| `creative/` | Art/audio/narrative bible |
| `technical/` | Architecture, analytics schema |
| `bootstrap/` | Fork the-laboratory → `games/<slug>/` |
| `build/` | Vertical slice, alpha, beta |
| `playtest/` | Structured EP playtest loops |
| `quality/` | Performance, accessibility |
| `marketing/` | Store page, assets |
| `launch/` | Maturity rating, publish |
| `liveops/` | Events, retention |

## Issue creation (all build+ loops)

Final step of each loop: **Producer** creates GitHub Issues with:

- Labels: `phase-NN`, `game:<slug>`, `agent:*`
- Body: acceptance criteria from loop output
- Project: Roblox Virtual Game Studio board → Backlog

EP implements via **Blender + Studio + agent pairing** per issue.

## Starting a loop chain for a new game

```
discovery.game-ideas (game_slug: null)
  → EP picks title → game_slug locked in CONTEXT.md
  → compliance.feasibility (game_slug: cosmic-garden)
  → ... chain continues ...
  → build.* loops create issues under games/cosmic-garden/
```
