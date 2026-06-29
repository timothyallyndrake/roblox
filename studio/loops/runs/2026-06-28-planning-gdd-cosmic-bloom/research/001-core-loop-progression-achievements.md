# Research 001 — Core Loop, Progression & Achievements

**Agent:** Game Designer  
**Date:** 2026-06-28  
**Run:** `2026-06-28-planning-gdd-cosmic-bloom`

## Mandate

Draft GDD sections for **core loop**, **progression**, and **achievements** for Cosmic Bloom. Align with locked vision, ADR-002, and Phase 02 compliance outcomes.

## Sources

| Topic | URL |
|-------|-----|
| GAG Garden Guide (quests, achievements, collection UI) | https://noleep.com/en/garden-guide-explained-in-grow-a-garden-quests-achievements-plants-and-more/ |
| GAG progression path (levels, collection, expansion) | https://deepwiki.com/gameboyso/grow-a-garden-roblox/4.2-progression-path |
| GAG retention / multi-system progression (2026) | https://mygagcalculator.com/how-to-level-up-fast-in-grow-a-garden/ |
| Cozy sim dopamine loop case study | https://www.primalcam.com/post/growagardenrobloxgamesuccesscasestudy |
| Roblox quest design (achievements, season passes) | https://create.roblox.com/docs/production/game-design/introduction-to-quest-design |
| Roblox Missions feature package | https://create.roblox.com/docs/resources/feature-packages/missions |
| Cosmic Bloom pitch | `studio/docs/discovery/pitch-sells-cosmic-bloom.md` |
| Vision | `games/cosmic-bloom/docs/VISION.md` |
| Phase 02 monetization (concept) | `studio/loops/runs/2026-06-28-compliance-feasibility-starlit-conservatory/research/003-monetization-model-recommendation.md` |

## Genre learnings (applied, not copied)

| Pattern | GAG / genre | Cosmic Bloom adaptation |
|---------|-------------|-------------------------|
| Multi-layer progression | Garden Guide XP + Season Pass + pet age | **Keeper Rank** + **Constellation Codex** + **Collector tier** (moths) — three visible tracks, not one opaque level |
| Collection UI | Grayscale locked plants in guide | **Constellation ceiling projector** — locked stars grey; completed constellations animate on dome |
| Daily retention | 3 daily quests → seed packs | **Keeper daily triad** — breed / polish / sell aligned to core verbs |
| Achievement tiers | Common → Prismatic one-time rewards | **Stardust → Cosmic** tiers; rewards = Cosmic Coins + cosmetic projector frames |
| Sell beat | Market stall instant sell | **Star Counter** — tactile polish before sell (EP differentiator) |
| Excluded | Rebirth reset, PvP steal, random paid eggs | **No rebirth at launch**; cozy mastery via codex breadth; breeds earn-only |

## Core loop (30-second beat)

**Primary verb:** BREED & COMPLETE (with polish-and-sell felt every session)

```
Plant seed → starlight nurture → harvest pollen/stardust →
cross-breed in lab → codex piece lights up →
polish rare bloom at Star Counter → NPC buys → reinvest
```

| Beat | Player action | Feedback | Server owns |
|------|---------------|----------|-------------|
| Plant | Select seed, tap plot | Seed sparkle, plot occupied | Inventory −1 seed, plot state |
| Nurture | Hold starlight can in range | Cooldown ring, plant growth stage | Growth timer, cooldown |
| Harvest | Tap mature plant | Pollen burst, +inventory | Roll yield tier |
| Breed | Pick 2 pollen types in lab | Fusion VFX, outcome reveal | Deterministic matrix + earn-only RNG |
| Codex | Auto on first discovery | Ceiling star lights, 1/N counter | Constellation bitmask |
| Polish | Hold at Star Counter sweet spot | Starlight wipe, quality tier | Quality score → price band |
| Sell | Confirm price in band | Coin shower, NPC reaction | Cosmic Coins grant |

**Fail states:** None punitive — plants don't die permanently; worst case is slower growth or lower polish tier. Cozy = no loss of bred progress.

**Session hook:** "One more breed" before logoff — cross-breed timer + codex near-completion (e.g. Little Dipper 6/7) drives Zeigarnik retention per PrimalCam dopamine sequence analysis.

## Progression architecture

### Layer 1 — Starter dome (0–15 min)

- Single glass dome, 4 plots, Nebula Sprout tutorial line
- Unlock: starlight can, Cross-Breed Lab tier 1, first constellation piece
- Gate: **East Dome** expansion after first polished sale (pitch first hour)

### Layer 2 — Dome expansion (15–60 min)

| Unlock | Cost / trigger | Effect |
|--------|----------------|--------|
| East Dome | First Star Counter sale | +4 plots, shared wall for future co-op |
| Cross-Breed Lab T2 | 3 codex pieces | New parent pollen combos |
| Moth Collector #1 | Complete any 3/7 constellation | Passive pollen attraction in dome |
| Nebula Row biome | Keeper quest chain | Outdoor pads, +pollen rate modifier |

### Layer 3 — Mid-game (hours 2–10)

- **3 constellation sets** at launch (7 pieces each = 21 discovery slots)
- **20 breeds** in cross-breed matrix (some constellation-gated)
- Keeper Rank 1–5: quest difficulty + sale price band bonus (+5% per rank, cap +25%)
- Second moth collector at 2 constellation completions

### Layer 4 — Long-term (days+)

- Complete all 3 launch constellations → **Meteor Shower** priority drops
- Rare breed mastery badges (all polish tiers on one breed)
- Biome cosmetic variants (projector skins earn-only)
- Post-v1: additional sky biomes, season pass track (Phase 17)

### Progression currencies & gates

| Resource | Earn | Spend |
|----------|------|-------|
| Cosmic Coins | NPC sales, quests, events, dailies | Seeds, lab tiers, dome expansions, cosmetics |
| Pollen / Stardust | Harvest | Cross-breed inputs |
| Codex progress | First-time breed discoveries | Unlocks collectors, biomes, quest lines |
| Keeper Rank XP | Quests + first-time discoveries | Sale band bonus, quest access |

**No rebirth** at launch — progression is **breadth** (codex) + **quality** (polish tiers) + **space** (domes/biomes).

### Offline progression

- Plants continue growth offline (GAG-proven retention pattern)
- **Pollen cap** accrues on login (generous; monetization pass skips wait not cap — Phase 02 handoff)
- Meteor Shower schedule runs server-side; missed events replay on next login notification

## Achievements

### Design principles

Per [Roblox quest design docs](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design): achievements are **long-horizon pride markers** tied to core loop engagement, not side content.

Implementation: Roblox **BadgeService** for marquee milestones + in-game **Constellation Chronicle** (Missions package pattern) for tiered track.

### Categories

| Category | Examples | Ties to loop |
|----------|----------|--------------|
| **Breeding** | First cross-breed; 10 unique breeds; complete a constellation set | Lab + codex |
| **Star Counter** | First polish; 50 sales; max-tier polish on a rare bloom | Sell beat |
| **Codex** | Light 7 stars in one set; complete 3 constellations | Collection meta |
| **Exploration** | Visit Nebula Row; survive a Meteor Shower | Biome + events |
| **Keeper** | Finish 7 daily triads; reach Keeper Rank 5 | Daily retention |
| **Social** | Co-polish one bloom (2P) | Co-op stretch |

### Tier structure (Constellation Chronicle)

| Tier | Color theme | Example threshold | Reward |
|------|-------------|-------------------|--------|
| Stardust | White | 5 achievements | 100 Cosmic Coins |
| Nebula | Purple | 15 achievements | Projector frame |
| Galaxy | Blue | 30 achievements | Moth cosmetic variant |
| Cosmic | Gold | 50 achievements | Dome glass tint |
| Legendary | Prismatic | All launch achievements | Badge + title "Astronomer Royal" |

**Launch target:** ~40 achievements (achievable in first 2 weeks for engaged players; 100% completion = months).

### Sample launch achievements (v1 vertical slice)

| ID | Name | Trigger | Tier |
|----|------|---------|------|
| A01 | First Sprout | Plant Nebula Sprout | Stardust |
| A02 | Stardust Pollen | First harvest | Stardust |
| A03 | Little Dipper I | Codex 1/7 Little Dipper | Stardust |
| A04 | First Polish | Complete Star Counter minigame once | Stardust |
| A05 | Sold! | First NPC purchase | Stardust |
| A06 | Eastward | Unlock East Dome | Nebula |
| A07 | Moth Friend | Unlock first Moth Collector | Nebula |
| A08 | Seven Stars | Complete one full constellation | Galaxy |
| A09 | Nebula Walker | Enter Nebula Row | Nebula |
| A10 | Shower Watcher | Collect seed during Meteor Shower | Nebula |
| A11 | Master Breeder | Discover 15 breeds | Galaxy |
| A12 | Perfect Polish | Max polish tier on any rare bloom | Galaxy |
| A13 | Keeper's Favor | Reach Keeper Rank 3 | Galaxy |
| A14 | Triad Streak | 7 daily triads in a row | Cosmic |
| A15 | Cosmic Gardener | Complete all 3 launch constellations | Legendary |

Roblox badges map to **Legendary** tier only (15–20 badges max per Roblox limits guidance); in-game Chronicle handles lower tiers.

## Game Designer outcome

**Sections drafted:** core loop ✅, progression ✅, achievements ✅  
**Deferred to later steps:** monetization detail (economy designer), co-op model scope (systems + EP grill), Star Counter/codex system specs (systems designer), UX flows (UX designer)

**Deliverable:** `games/cosmic-bloom/docs/gdd.md` sections 1–4 updated.
