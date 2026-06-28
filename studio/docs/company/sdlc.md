# SDLC — 18 Phases

Each phase has a plan in [`docs/phases/`](../phases/), GitHub Issues, doc deliverables, and a gate requiring EP sign-off.

| Phase | Name | Gate to Proceed |
|-------|------|-----------------|
| **00** | Studio Framework | `timothyallyndrake/roblox` live, studio/ skeleton, Projects configured |
| 01 | Discovery & Vision | Game pitch + working title locked in CONTEXT.md |
| 02 | Compliance & Feasibility | Compliance checklist signed for chosen concept |
| 03 | Game Design Document | GDD v1 approved; monetization strategy recommended |
| 04 | Creative Bible | Visual/audio/animation tone locked |
| 05 | Technical Architecture | Architecture doc + module map + analytics event schema |
| 06 | Game Bootstrap | `games/<game-name>/` from the-laboratory fork, CI green |
| 07 | Vertical Slice | One complete core loop playable in Studio |
| 08 | Playtesting Round 1 | Structured playtest complete; critical bugs fixed |
| 09 | Alpha | Core systems feature-complete |
| 10 | Analytics Instrumentation | Event tracking coded + verified |
| 11 | Beta | Content, monetization, polish |
| 12 | Playtesting Round 2 | Broader playtest; retention loop validated |
| 13 | Performance + Accessibility | Mobile performance + accessibility basics pass |
| 14 | Marketing Prep | Icon, thumbnail, description, social clips ready |
| 15 | Launch Prep | Maturity questionnaire complete; PROD publish |
| 16 | Launch | Public experience live with rating |
| 17 | Live Ops | Update cadence running; first post-launch event shipped |

## Phase protocol

1. **Producer** opens phase plan → creates GitHub Issues with acceptance criteria
2. All agents read `studio/CONTEXT.md` before acting
3. Agents produce deliverables (docs in discovery; PRs in build phases)
4. **Compliance Officer** reviews player-facing concepts before EP approval
5. **Technical Writer** updates CONTEXT.md with locked decisions
6. **EP** accepts, rejects, or requests revision at the gate
7. **Producer** records ADR, closes gate issues, opens next phase issues
8. Phase retrospective → Lessons Learned appended to CONTEXT.md

## Branches

| Branch | Purpose |
|--------|---------|
| `dev` (default) | Integration |
| `prod` | Releases |

Per-game release tags: `<game-name>-v<semver>` via release-please.

See [git-workflow.md](git-workflow.md) for PR and merge policy.
