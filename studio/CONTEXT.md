# Studio Context

> **Agents: read this file first every session.**  
> Updated by the Technical Writer after every phase gate. Last updated: 2026-06-28.

## Current State

| Field | Value |
|-------|-------|
| **Active phase** | Phase 03 — Game Design Document |
| **Active game** | **Cosmic Bloom** (`cosmic-bloom`) |
| **Game folder** | [games/cosmic-bloom/](../games/cosmic-bloom/) (docs until Phase 06 bootstrap) |
| **GitHub repo** | [timothyallyndrake/roblox](https://github.com/timothyallyndrake/roblox) ✅ Live |
| **Last gate passed** | Phase 02 — Compliance & Feasibility (2026-06-28) |
| **Active GDD run** | `2026-06-28-planning-gdd-cosmic-bloom` — **Steps 1–6 complete** |
| **GDD status** | Draft complete — **EP sign-off pending** (Step 7) |

## Locked Decisions

| # | Decision | Source |
|---|----------|--------|
| D1–D20 | _(unchanged — see git history)_ | Grilling / EP |
| D21 | **Game #1:** **Cosmic Bloom** — open meadow plant breeding, **Bloomdex**, **Orbital Outpost** delivery, **Community Feed** | ADR-002 *(amended)*, GDD §1 |
| D22 | **Display name:** **Cosmic Bloom**; slug `cosmic-bloom` | EP Q43 2026-06-28 |
| D23 | **Phase 02 approved:** Minimal/all ages, Cozy Fair F2P, no paid random at launch | EP Q43 |
| D24 | **Cosmic Coins** soft currency; **no glass domes**; **no Star Counter** | Foundation grill, GDD |
| D25 | **Co-op v1:** Solo-first; **private VIP meadows** at launch; **no P2P trading**; no shared plots | Q74, GDD §1.9, §5.10 |
| D26 | **Launch roster:** 10 base breeds + 12 cross-breds + signature mutations *(§1.2b)* | Q70 |
| D27 | **Planet gates:** Lumina R10 → Solara; Solara R15 → Glimmer | Q69 |
| D28 | **Robux coin packs:** **Cosmic Coin Pouch / Satchel / Vault** *(99 / 249 / 499 R$)* | EP alignment 2026-06-28, GDD §6.4 |
| D29 | **Private server fairness:** VIP meadows scale **Community Feed server goal only** — grow timers, personal thresholds, payouts, gates, spin odds **unchanged** | EP alignment 2026-06-28, GDD §5.7 |

## Open Questions

- [ ] **EP sign-off** on GDD draft → Phase 04 creative bible
- [ ] Compliance checklist refresh (domes / retired mechanics stale language)
- [ ] Shared-plot co-op — **deferred post-launch** (not v1)
- [ ] EP confirm revised labels/defaults: Glimmer Gathering, Community Table, Seed Stand, Prize Bloom, private Feed server-goal-only scaling, Extra Garden Beds (+2)

## Active Agents (Phase 03)

| Role | Status |
|------|--------|
| Game Designer | GDD §1–4 ✅ |
| Systems Designer | §5 ✅ |
| Economy/Monetization Designer | §6 ✅ |
| UX/UI Designer | §7–§8 ✅ |
| Narrative Designer | §9 ✅ |
| Technical Writer | Step 6 ✅ — CONTEXT + studio GDD index |
| Producer | Step 7 pending — issues + EP sign-off |

## Phase 03 Gate Checklist

- [x] `studio/docs/game-design/gdd.md` — studio index
- [x] `games/cosmic-bloom/docs/gdd.md` — full GDD §1–10
- [x] Core loop, progression, monetization, achievements, co-op model
- [ ] EP sign-off → Phase 04 creative bible

## Pointers

| Doc | Path |
|-----|------|
| **GDD (canonical)** | [games/cosmic-bloom/docs/gdd.md](../games/cosmic-bloom/docs/gdd.md) |
| GDD studio index | [studio/docs/game-design/gdd.md](docs/game-design/gdd.md) |
| Vision | [games/cosmic-bloom/docs/VISION.md](../games/cosmic-bloom/docs/VISION.md) |
| Pitch | [docs/discovery/pitch-sells-cosmic-bloom.md](docs/discovery/pitch-sells-cosmic-bloom.md) |
| Grill log (Q51–Q74) | [docs/discovery/grilling-log.md](docs/discovery/grilling-log.md) |
| ADR-002 | [docs/decisions/002-game-direction-cosmic-bloom.md](docs/decisions/002-game-direction-cosmic-bloom.md) |
| Compliance checklist | [docs/compliance/concept-compliance-checklist.md](docs/compliance/concept-compliance-checklist.md) |
| Planning run state | [loops/runs/2026-06-28-planning-gdd-cosmic-bloom/state.md](loops/runs/2026-06-28-planning-gdd-cosmic-bloom/state.md) |

## Lessons Learned

- **2026-06-28:** Spark mode + EP taste beats batch discovery. Lock name early in Phase 02/03 — Cosmic Bloom over "Grow a Galactic Garden" (shorter, ownable, not GAG clone).
- **2026-06-28:** Foundation grill (Q51–Q74) before economy/UX steps prevents rework — EP decisions on roster, Keeper, tutorial, private servers saved Step 2–5 churn.
- **2026-06-28:** Studio `gdd.md` stays an **index**; game folder holds the canonical long-form GDD.
