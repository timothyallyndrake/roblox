# Cosmic Bloom — Targeted Roblox Market Scan

**Date:** 2026-07-01
**Purpose:** Pre-build hardening scan for plant sims, cozy collection, server events, monetization, thumbnails, and first-session hooks.
**Decision stance:** This does **not** reopen the concept. It clarifies how Cosmic Bloom should position itself before full v1 implementation.

---

## Summary

Roblox plant sims are validated by the success of *Grow a Garden*: passive crop growth, offline progress, visible gardens, mutations, and frequent events clearly work for the current audience. The same market also exposes the traps Cosmic Bloom is intentionally avoiding: paid stealing, paid random, high-pressure scarcity, overpowered Robux shortcuts, and social mechanics that make kids feel robbed or left behind.

Cosmic Bloom's strongest market lane is **cozy cosmic collection with no stealing**:

> Grow magical space plants, fill constellation-shaped Bloomdex maps, feed friendly planets, and join a server potluck without trading, stealing, or paid random.

---

## Market Signals

| Signal | What it means | Cosmic Bloom implication |
|--------|---------------|--------------------------|
| Idle farming is hot | Players understand seed → wait → harvest → upgrade immediately. | Keep the first action obvious: plant Glow Mote and see it grow fast. |
| Offline growth is expected | Players like returning to progress. | Keep offline buffer but cap it to avoid runaway economy. |
| Events drive return visits | Limited-time and server-wide events create spikes. | Community Table and meteors are market-relevant, but copy must avoid pressure. |
| Mutations and rare flexes matter | Players chase variants and show off rare finds. | Bloomdex signatures, Prize Blooms, and display cases are worth keeping. |
| Paid stealing is controversial | It creates anger, parent concern, and toxicity. | Cosmic Bloom should loudly promise: no stealing, no trading scams, no P2P. |
| Paid random / event crates are risky | They can feel exploitative with a young audience. | Keep Cosmic Spin earn-only and disclose odds. |
| Thumbnail testing matters | Roblox recommends multiple thumbnails and authentic gameplay. | Plan 3–5 thumbnail concepts around actual differentiators. |
| First 30–90 seconds matter | Players leave if first action is unclear. | Spawn must show garden, Glow Mote, Keeper prompt, and immediate grow feedback. |

---

## Competitor Pattern Notes

### Grow a Garden

Observed market lessons:

- Starts with familiar crops and fast first progress.
- Uses passive/offline growth to create low-friction return loops.
- Leans heavily on mutations, rare finds, pets, events, and progression flexes.
- Has monetization criticism around paid acceleration, scarcity, and stealing.

Cosmic Bloom response:

- Keep passive growth and mutation chase.
- Differentiate with **planet feeding**, **Bloomdex star maps**, **Stellar Nursery**, **Community Table**, and **no stealing**.
- Avoid making Robux feel required for full progression.

### Grow Flowers / Similar Garden Clones

Observed pattern:

- Many competitors pitch “relax, grow, harvest, play with friends.”
- Visual identity often stops at “plants + cozy + friends.”

Cosmic Bloom response:

- The thumbnail and first minute must show cosmic specificity: Orbital Outpost, glowing plants, constellation UI, meteor sky, and Community Table.
- Do not market only as “another garden.”

---

## First 60 Seconds Requirement

Cosmic Bloom should prove these beats almost immediately:

1. **This is my meadow.** Player sees personal plot and open starry setting.
2. **I know what to do.** Keeper points to Glow Mote seed / plot.
3. **Something happens fast.** Glow Mote visibly grows or sparkles within seconds.
4. **This is not just farming.** The Orbital Outpost / planet-feeding goal is visible early.
5. **The collection hook exists.** Bloomdex star map appears as a near-term reward.
6. **No threat from other players.** Copy and layout signal separate gardens, no stealing.

Metric target for first live instrumentation:

- First action attempted within 30 seconds.
- First reward / growth feedback within 30 seconds.
- First delivery within 5–6 minutes.
- Tutorial completion within 10 minutes.

---

## Thumbnail Concepts To Test

Use Roblox thumbnail personalization later with multiple authentic options. Candidate concepts:

1. **Meadow + Planet Delivery:** kid avatar holding glowing fruit, capsule launching toward Lumina.
2. **Bloomdex Star Map:** bright plant collection lighting up Little Slipper.
3. **Meteor Night:** players running to personal meteor crates under a star shower.
4. **Community Table:** friends dumping different glowing fruits into a cozy shared table.
5. **Stellar Nursery Reveal:** two pollen vials combining into a new cosmic plant.

Avoid:

- Generic carrot/crop thumbnails.
- Casino wheel as the primary image.
- Overcrowded UI screenshots.
- Any imagery implying theft, trading, combat, or urgency panic.

---

## Monetization Positioning

Cosmic Bloom should be explicit:

- Robux saves time or buys cosmetics.
- Robux does **not** buy spins, exclusive breeds, paid random seeds, planet unlocks, Comet Shards, Spin Tokens, or stealing.
- Private Meadow is comfort and family play, not progression power.
- Extra Garden Beds (+2) is the highest-risk v1 SKU because it multiplies several earn faucets. It must pass economy sim + playtest approval before enablement.

---

## Positioning Statement

For kids who like garden games but parents who dislike stealing, trading scams, and random paid pressure, Cosmic Bloom is a cozy cosmic plant-breeding game where every player tends their own meadow, feeds friendly planets, completes star-map collections, and joins server events without losing their stuff.

---

## Actions For The GDD / Build Plan

- Keep **no stealing / no trading / no paid random** prominent in pitch and store copy.
- Make the first minute visually show **cosmic plant + Orbital Outpost + Bloomdex**, not just generic gardening.
- Treat Community Table and meteors as social warmth, not mandatory FOMO.
- Require economy proof for Extra Garden Beds (+2), Spin Tokens, and Private Meadow Feed scaling.
- Prepare 3–5 authentic thumbnail concepts for launch testing.
