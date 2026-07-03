# Cosmic Bloom — Extensive Plan Review Resolution

**Date:** 2026-07-01  
**Scope:** Phase 03 GDD alignment, naming, kid/parent clarity, economy risk, QA readiness, stale docs  
**Canonical source after this pass:** `games/cosmic-bloom/docs/gdd.md`

---

## Executive Summary

Cosmic Bloom remains a strong game direction: open starlit meadows, Bloomdex completion, Stellar Nursery cross-breeding, Orbital Outpost planet deliveries, Community Table co-op, meteors, and earn-only Cosmic Spin all support a cozy Roblox plant-breeding sim without trading, stealing, or paid random.

This pass resolved the major pre-signoff alignment issues found by the staff cross-review. The GDD now has one canonical source for tutorial flow, delivery math, Community Feed scaling, Keeper Rank, private-server fairness, reset policy, and Step 7 acceptance criteria.

**Gate status:** ready for family/EP review, but Phase 03 should still not be marked passed until EP signs the open questions in GDD §10 and Producer creates GitHub Issues from the acceptance matrix.

---

## Resolved Findings

| Finding | Resolution |
|---------|------------|
| Tutorial used Nebula Pod while Lumina R1 required Glow Berry | Tutorial now starts with **Glow Mote → Glow Berry → Lumina R1**; Moon Melon + Nebula Sprout are granted after first delivery. |
| §1.7 delivery examples conflicted with §5.3 | §1.7 now defers numeric details to §5.3 and uses round-band patterns instead of duplicate tables. |
| Community Feed had ~80k example vs §5.7 formula | §1.7b now uses a generated 12-player example from §5.7; §5.7 is canonical. |
| Keeper Rank skipped Beat 4 | Rank table now maps Beat 4 to Rank 5; Beat 5 is capstone without Rank 6. |
| Reset policies differed | Free spin, Daily Trio, and pollen swabs now use rolling 24h per-account timers. |
| Weaver Watch unclear | Renamed to **Glimmer Gathering**; gate/fallback rule added for public, private, and low-pop servers. |
| Private servers could look like easier progression | Private Meadows now scale **only the shared Community Feed server goal**; personal thresholds, growth, payouts, gates, and spin odds stay public-equivalent. |
| Pitch real-sky wink conflicted with Q58 | Pitch now says Cosmic Bloom uses its own invented star shapes, not real-world constellations. |
| Stardust missing from VISION | VISION now lists Stardust as an upgrade item. |
| §10 was not testable | §10 is now a vertical slice acceptance matrix with owners and pass criteria. |
| Visit privacy was post-MVP | Visit board privacy is now v1: Public / Friends only / Private, with Friends only as the family-friendly default. |
| Pollen swabs could feel invasive | Swab copy now says sampling does not take fruit, pollen, or progress from the owner. |
| Accessibility too thin | Added reduced motion, UI scale, star-map list view, reminder frequency, and settings requirements. |
| Stale docs referenced domes / Star Counter / moth collectors | Active docs updated; historical run artifacts bannered as superseded. |

---

## Naming Decisions

### Keep

- **Cosmic Bloom** — short, ownable, clear space + plants identity.
- **Bloomdex** — excellent collection shorthand.
- **Orbital Outpost** — strong planet-delivery hub name.
- **Stellar Nursery** — clear and cozy for cross-breeding.
- **Cosmic Coins**, **Comet Shards**, **Meadow Express**, **Bloom Rush**, **Private Meadow** — clear enough for players and shop UI.
- **Lumina**, **Solara**, **Glimmer** — readable planet progression.

### Renamed / Adopted

| Old | New | Why |
|-----|-----|-----|
| Seed Broker | **Seed Stand** | More kid-friendly, less financial. |
| Specimen | **Prize Bloom** | Warmer trophy language. |
| Weaver Watch | **Glimmer Gathering** | Ties the event to the Glimmer planet and feeding action. |
| Community Hopper | **Community Table** | Warmer potluck fantasy. |
| Daily triad | **Daily Trio** | Clearer kid-facing phrase. |
| Moth bath | **Pollen Basin** | Avoids confusion with cut moth collectors. |
| Nebula Moth Lantern | **Nebula Glow Lantern** | Avoids implying moth mechanics. |
| Corona Sprig / Fruit | **Halo Sprig / Fruit** | Avoids real-world illness association. |
| Gloaming Ivy / Fruit | **Glimmer Ivy / Fruit** | More understandable and aligns with Glimmer. |
| Dreamer's Root | **Dreamroot** | Cleaner UI string. |
| Weaver's Knot | **Weaver Vine** | Simpler plant name. |
| Cosmic Knot | **Skyknot Bloom** | Reduces overuse of “Cosmic.” |
| Garden Row I | **Extra Garden Beds (+2)** | Clear Roblox shop title. |
| Lifeforms Fed | **Planet Friends Fed** | Warmer and clearer for kids/parents. |

---

## Remaining EP Confirmations

These are intentionally left as Step 7 review items in GDD §10:

1. Confirm Private Meadow scaling stays **server-goal only**, not personal tier thresholds.
2. Confirm **Extra Garden Beds (+2)** remains v1 after playtest checks Stardust, mutation, and Feed acceleration.
3. Confirm the renamed player-facing labels: **Glimmer Gathering**, **Community Table**, **Seed Stand**, **Prize Bloom**, **Pollen Basin**, **Halo Sprig**, **Glimmer Ivy**, **Extra Garden Beds (+2)**.
4. Confirm whether v1 ships the full 40-achievement target or a smaller implementation set.
5. Confirm the seven launch Cosmic Spin Legendary item names before Phase 04 art lock.

---

## Producer Issue Plan

Create Step 7 GitHub Issues from GDD §10. Suggested grouping:

| Issue | Acceptance source |
|-------|-------------------|
| Tutorial + first delivery | GDD §10 row: First-session tutorial |
| Core garden / growth / inventory | Starter garden, Plant growth & nurture, Inventory & harvest |
| Stellar Nursery + Bloomdex | Nursery, Launch roster, Bloomdex, Mutations |
| Orbital Outpost + planet gates | Orbital Outpost, Planet unlock chain |
| Community Table + Private Meadow | Community Table / Feed, Private Meadow |
| Meteors + Merchant | Meteor shower + Merchant |
| Cosmic Spin | Cosmic Spin row + Phase 06 addendum |
| Achievements + Legendary catalog | Achievements and Legendary catalog rows |
| Social / safety | Pollen swabs, Visit privacy, Trust & Safety |
| Monetization | Monetization row + GDD §6 |
| Accessibility | Accessibility row |

---

## Files Updated By This Pass

- `games/cosmic-bloom/docs/gdd.md`
- `games/cosmic-bloom/docs/VISION.md`
- `studio/docs/discovery/pitch-sells-cosmic-bloom.md`
- `studio/docs/game-design/gdd.md`
- `studio/CONTEXT.md`
- `studio/docs/discovery/grilling-log.md`
- `studio/docs/decisions/002-game-direction-cosmic-bloom.md`
- `studio/docs/discovery/build-candidates.md`
- `studio/docs/compliance/concept-compliance-checklist.md`
- Historical planning/compliance run files with superseded banners

---

## Reviewer Guidance

For family review, focus on whether the cleaned names and flows are understandable:

- Can a kid explain **Plant → Nurture → Harvest → Deliver → Mix → Bloomdex → Upgrade**?
- Does **Community Table** sound fun or stressful?
- Are **Seed Stand**, **Prize Bloom**, **Glimmer Gathering**, and **Extra Garden Beds (+2)** clear?
- Does Private Meadow sound like comfort, not cheating?
- Does Cosmic Spin feel fair, not like paid gambling?
- Does the pitch avoid pressure words like “hurry,” “starving,” or “limited power”?

For Producer/QA review, use GDD §10 as the checklist and do not rely on old research artifacts unless they are explicitly marked current.
