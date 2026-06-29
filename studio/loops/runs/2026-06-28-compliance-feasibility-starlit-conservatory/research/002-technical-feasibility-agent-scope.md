# Research 002 — Technical Feasibility: Agent-Only Implementation Scope

**Agent:** Technical Director  
**Date:** 2026-06-28  
**Run:** `2026-06-28-compliance-feasibility-starlit-conservatory`

## Mandate

Assess whether Starlit Conservatory v1 vertical slice is **feasible under D2**: agents write all Luau; EP builds assets/world in Studio (15+ hrs/week). Bootstrap (Rojo/Knit/CI) deferred to **Phase 06** per SDLC.

## Sources

| Topic | URL |
|-------|-----|
| ProfileService (session locking, autosave) | https://madstudioroblox.github.io/ProfileService/ |
| DataStore patterns (BindToClose, concurrency) | https://simplified.media/guides/roblox-data-stores |
| Roblox DataStore tutorial | https://luaguides.dev/tutorials/lua-roblox/roblox-data-stores/ |
| Studio monorepo bootstrap plan | `games/README.md`, `studio/docs/company/sdlc.md` |
| v1 scope | `studio/docs/discovery/pitch-sells-starlit-conservatory.md` |
| EP/agent split | ADR-002, `games/starlit-conservatory/docs/VISION.md` |

## Executive summary

**Verdict: FEASIBLE** for Phase 07 vertical slice with standard Roblox sim patterns (ProfileService + Knit + server authority). **No architectural blockers.** Primary schedule risk is **EP asset throughput** (20 plant meshes, dome kit, VFX), not agent Luau capacity.

Recommend **deferring async wishlist notes** and treating **2P co-op cross-pollination** as stretch for vertical slice (solo path is 100% functional per pitch).

---

## EP vs agent responsibility matrix

| System | Owner | Feasibility notes |
|--------|-------|-------------------|
| Plant/breed/codex logic | **Agents** | Data-driven config (`BreedConfig`, cross-breed matrix). Server rolls outcomes; client displays. Standard sim pattern. |
| Constellation codex progression | **Agents** | Bitmask or set completion against static constellation tables. |
| Star Counter polish minigame | **Agents** | Client input → server validates hold timing → applies polish quality to inventory item. |
| NPC sell loop + price bands | **Agents** | Server-owned economy; suggested price band from config; NPC purchase is server transaction. |
| Offline pollen cap | **Agents** | `lastSeen` timestamp in profile; accrue capped resources on join. |
| Meteor Shower event stub | **Agents** | Scheduled server event + spawn table; no client trust. |
| Moth collector attraction | **Agents** (logic) + **EP** (VFX/mesh) | Server tracks codex triggers; EP provides moth asset + animation. |
| Dome expansion / biome unlocks | **Agents** (gates) + **EP** (geometry) | Unlock flags in profile; EP places Nebula Row zone + visibility through glass. |
| Plant meshes, dome kit, Star Counter props | **EP** | Blender/marketplace → Studio placement. Agents wire `CollectionService` tags / attributes for interaction. |
| Optional 2P co-op adjacent plots | **Agents** (sync) + **EP** (layout) | Feasible via shared dome instance + server-mediated cross-pollination. **Stretch for Phase 07** — solo first. |
| Async wishlist notes on breeds | **Agents** | Requires TextService filtering, rate limits, persistence (DataStore or MessagingService). **Defer post-v1** to reduce Phase 07 scope. |

**Boundary contract:** EP places tagged interactables (`Plot`, `StarCounter`, `BreedLab`, `NPCVisitorSpawn`); agents own all gameplay state and remotes. No Rojo-managed scripts edited in Studio (D2/D4).

---

## Architecture preview (Phase 05/06 target)

```
games/starlit-conservatory/src/
├── server/
│   ├── Services/
│   │   ├── PlayerDataService      # ProfileService load/release
│   │   ├── PlotService            # plant, water, harvest
│   │   ├── BreedService           # cross-breed RNG (earn-only)
│   │   ├── CodexService           # constellation completion
│   │   ├── StarCounterService     # polish + list for sale
│   │   ├── MarketService          # NPC visitors, coin grants
│   │   └── EventService           # Meteor Shower stub
│   └── ...
├── shared/
│   ├── Config/Breeds.luau
│   ├── Config/Constellations.luau
│   └── Types/PlayerProfile.luau
└── client/
    ├── Controllers/
    │   ├── PlotController
    │   ├── StarCounterController  # polish UI only
    │   └── CodexController
    └── ...
```

**Persistence:** ProfileService profile schema holds plots, inventory (seeds/pollen/blooms), codex progress, coins, unlock flags, offline timestamps. Session-locked; autosave + `BindToClose`.

**Authority model:** All inventory mutations, breed outcomes, sales, and unlocks on server. Client sends intents (`HarvestPlot`, `SubmitPolish`, `RequestBreed`); server validates distance, ownership, cooldowns, and item existence.

---

## v1 vertical slice feasibility (Phase 07 scope)

| Deliverable (from pitch) | Feasible? | Notes |
|--------------------------|-----------|-------|
| 1 starter dome + Nebula Row | **Yes** | EP builds zones; agents gate unlock |
| 20 breeds, 3×7 constellation sets | **Yes** | Config tables; combinatorics manageable at this scale |
| 1 moth collector type | **Yes** | Simple trigger + spawn; EP art dependency |
| Star Counter + 5 NPC visitors | **Yes** | NPC pathing can be simple waypoint loop for v1 |
| Meteor Shower event stub | **Yes** | Timer + drop table |
| Offline pollen cap | **Yes** | Standard idle-cap pattern |

**Estimated agent Luau effort (order of magnitude):** 4–6 weeks of agent PRs post-Phase 06 bootstrap, assuming EP world shell exists. Not a blocker for Phase 02 gate — detail refines in Phase 05 architecture doc.

---

## Top 3 failure modes

1. **Data loss / duplication** — Breeding sims are high-stakes for player trust. Mitigation: ProfileService from day one; never trust client for inventory; `pcall` + retries on all DataStore paths; versioned profile schema.

2. **EP asset bottleneck** — Vertical slice needs recognizable cosmic look (glass dome, 20 plants, Star Counter prop) before playtest is meaningful. Mitigation: Phase 04 creative bible locks minimum asset list; placeholder meshes OK for first agent integration, but EP 15 hr/week must prioritize dome + 5 starter plants before Phase 07 gate.

3. **Scope creep on social/async features** — Wishlist notes + async co-op polish add TextService, persistence, and UX surface area disproportionate to core breed loop. Mitigation: ship v1 without async notes; NPC-only sales; co-op in Alpha (Phase 09) unless EP bandwidth allows earlier.

---

## Technical risks (non-blocking)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Cross-breed balance/config drift | Medium | Single source `Breeds.luau`; unit tests on matrix completeness |
| Polish minigame feel vs breeding focus | Low | Cap polish bonus; keep 3-second hold simple |
| Plot save size at scale | Low | 6–12 plots v1; compress plant state to IDs + growth timestamps |
| No game bootstrap yet (Phase 06) | Expected | Feasibility assumes the-laboratory fork; no code needed in Phase 02 |
| Crowded genre performance bar | Medium | Phase 13 perf gate; mobile-friendly part counts in creative bible |

---

## Dependencies before build

| Phase | Dependency |
|-------|------------|
| 03 GDD | Breed count, economy numbers, unlock pacing |
| 04 Creative Bible | Plant/dome art direction, tag naming for interactables |
| 05 Architecture | Full module map, profile schema, remote contracts |
| 06 Bootstrap | Rojo/Knit/wally from the-laboratory; CI green |
| 07 Vertical slice | EP place shell with tagged props + agent services wired |

---

## Technical Director recommendation

**Feasibility sign-off: PASS**

Starlit Conservatory is technically feasible for the RGS agent-only code model. Standard server-authoritative sim architecture applies; no exotic engine features required. **Conditions:**

1. ProfileService + strict server authority from first data commit (Phase 06+).
2. Defer async wishlist notes to post-vertical-slice.
3. Solo path is Phase 07 critical path; 2P co-op is stretch/Alpha.
4. EP asset delivery tracked as parallel critical path — not agent-blocked but gate-blocked for playtest.

Full architecture doc and module map remain **Phase 05** deliverables; this research satisfies Phase 02 feasibility gate input.
