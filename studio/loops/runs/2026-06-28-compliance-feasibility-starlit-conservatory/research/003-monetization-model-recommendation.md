# Research 003 — Monetization Model Recommendation

> **Historical note (2026-07-01):** This monetization pass predates the Cosmic Bloom Phase 03 GDD. Use GDD §6 for current SKU names, Cosmic Coin packs, Private Meadow fairness, and no-paid-random constraints.

**Agent:** Economy/Monetization Designer  
**Date:** 2026-06-28  
**Run:** `2026-06-28-compliance-feasibility-starlit-conservatory`

## Mandate

Recommend a monetization model for Phase 02 that aligns with locked vision (**everything earnable; Robux = currency/time-skip only**), genre benchmarks (GAG, Bee Swarm), and Compliance Officer policy screen (no paid random at launch).

## Sources

| Topic | URL |
|-------|-----|
| GAG monetization analysis | https://www.maxpowergaming.co/post/inside-the-monetization-playbook-of-roblox-s-biggest-hit |
| GAG case study (passes, friction) | https://www.primalcam.com/post/growagardenrobloxgamesuccesscasestudy |
| GAG fair microtransaction tone | https://www.spaceport.xyz/blog/how-grow-a-garden-on-roblox-became-a-marketplace |
| Roblox monetization foundations | https://create.roblox.com/docs/en-us/production/game-design/monetization-foundations |
| Game passes vs dev products | https://simplified.media/guides/roblox-monetization |
| Paid random items policy | https://create.roblox.com/docs/production/monetization/paid-random-items |
| Compliance screen (this run) | `research/001-roblox-policy-screen-starlit-conservatory.md` |
| Vision constraints | `games/starlit-conservatory/docs/VISION.md` |

## Recommended model: **Cozy Fair F2P**

**One sentence:** Dual-currency progression where every breed, biome, and dome upgrade has an earn path; Robux buys **deterministic** convenience (time-skip, cooldown removal, travel) and **cosmetics** — never exclusive power or paid random outcomes.

### Why this model

| Input | Implication |
|-------|-------------|
| EP vision: everything earnable | No Robux-only breeds or constellation pieces |
| D9 / Phase 03 GDD | This doc is **Phase 02 recommendation**; numbers refine in GDD |
| GAG success | Friction-aligned passes (watering, slots) convert without loot boxes |
| Starlit differentiation | **No PvP steal monetization** (GAG uses Robux steals — we exclude per pitch) |
| Compliance PASS | **No paid random items at launch** → no odds disclosure stack required |
| Kids/Select audience target | Avoid predatory random purchases; calm shop tone per Spaceport GAG analysis |

---

## Dual currency

| Currency | Source | Spend on |
|----------|--------|----------|
| **Cosmic Coins** (soft) | NPC bloom sales, Keeper quests, events, daily login | Seeds (earnable shop), dome expansions, lab tiers, cosmetic earnables |
| **Robux** | Real-money purchase | Game passes, dev products (deterministic), cosmetic-only UGC-style dome skins |

**Exchange rule:** Robux may grant Cosmic Coins via dev products, but Cosmic Coins never convert to Robux. Robux never directly buys a **random** breed outcome.

---

## Launch monetization stack (Beta / Phase 11 target)

### Game passes (permanent, 3 at launch — expand later)

| Pass | Indicative price | Value | Earnable equivalent? |
|------|------------------|-------|----------------------|
| **Infinite Starlight Can** | 149–199 R$ | Removes starlight watering cooldown | Yes — wait cooldowns free |
| **Dome Expansion I** | 199–249 R$ | +2 plant plots permanently | Yes — coin unlock at higher tier (slower) |
| **Nebula Express** | 99–149 R$ | Fast-travel between unlocked biomes | Yes — walk/float between domes |

**Design rules:**

- Never paywall core loop (plant → breed → codex → sell).
- Prompt passes at **friction moments** (third watering wait, plot full, long walk to Nebula Row) — not on join spam.
- Server validates ownership via `MarketplaceService:UserOwnsGamePassAsync`; cache per session.

### Developer products (repeatable, deterministic)

| Product | Type | Notes |
|---------|------|-------|
| **Cosmic Coin Pack** (S/M/L) | Currency bundle | Price above organic earn rate; never sole path to progression |
| **Bloom Rush** (1h / 4h / 8h) | Time-skip | Advances **one selected plant's** growth timer by fixed duration — not random |
| **Starter Conservatory Kit** | One-time starter pack (24h window) | Fixed bundle: 500 Cosmic Coins + cosmetic can skin + **named** Nebula Sprout seed (not random) |

**Excluded at launch:** random seed packs, gacha eggs, spin wheels, Robux-paid cross-breed rolls.

### Cosmetics (Robux or Cosmic Coins)

- Dome glass tint, constellation projector style, Star Counter mat, watering can skins.
- Prefer **Cosmic Coin earn path** for every cosmetic; Robux is shortcut for impatient collectors.
- No gameplay stats on paid-only cosmetics.

### Live ops (post-launch, Phase 17)

- **Constellation Season** — quest-based earn-only track (Roblox season pass pattern); premium track = **deterministic** bonus cosmetics only, not random loot ([monetization foundations](https://create.roblox.com/docs/en-us/production/game-design/monetization-foundations)).
- **Meteor Shower events** — rare seeds drop free in-world; no Robux wager on drops.

---

## Explicit exclusions (brand + compliance)

| Mechanic | Status | Reason |
|----------|--------|--------|
| Robux crop steal / PvP theft | **Never** | Pitch differentiator; harassment vector |
| Paid random seed packs / eggs | **Not at launch** | Paid random compliance + vision conflict |
| Robux-only breeds | **Never** | Breaks "everything earnable" |
| Loot boxes / spin wheels | **Never** | Random + trust damage in cozy genre |
| Paywalled biomes | **Never** | Biomes unlock via codex/coins; pass = travel convenience only |

---

## Compliance integration

### Paid random items

**Launch stance: NONE.** Cross-breed RNG is earn-only gameplay (Compliance Research 001). Checklist items satisfied without odds UI.

**If ever added post-launch (not recommended):**

- Numerical odds pre-purchase for every outcome summing to 100%
- `PolicyService:GetPolicyInfoForPlayerAsync` → honor `ArePaidRandomItemsRestricted`
- Guaranteed direct-purchase alternative for restricted players
- Retake Maturity & Compliance Questionnaire

### PolicyService implementation (Phase 06+)

| Flag | Launch need |
|------|-------------|
| `ArePaidRandomItemsRestricted` | Wire when/if paid random exists; stub service module now |
| `IsPaidItemTradingAllowed` | Only if player-to-player bloom trading added (not v1); NPC sales unaffected |

### Monetization + maturity questionnaire

- Declare **no unplayable gambling**, **no paid random items** at launch → supports **Minimal / All ages** target.
- No paid item trading descriptor unless peer trading ships.

---

## Genre benchmark comparison

| | Grow a Garden | Starlit (recommended) |
|--|---------------|-------------------------|
| Core friction monetization | Infinite watering, pet slots, multipliers | Infinite starlight can, plot slots, travel |
| Random paid hatch | Premium eggs (random) | **None** — breeds via earn-only lab |
| PvP steal | Robux-enabled | **Excluded** |
| Soft currency | Sheckles | Cosmic Coins |
| Tone | Optional boosts; some community friction on monetization push | Calm, no loot boxes ([Spaceport](https://www.spaceport.xyz/blog/how-grow-a-garden-on-roblox-became-a-marketplace)) |

---

## Revenue expectations (qualitative)

Plant sims monetize on **impatience at bottlenecks**, not paywalls ([Max Power Gaming GAG analysis](https://www.maxpowergaming.co/post/inside-the-monetization-playbook-of-roblox-s-biggest-hit)). Starlit's Star Counter sell beat creates natural coin earn loops; Robux conversion peaks when players want **one more breed before logoff** (Bloom Rush) or **remove watering friction** (Infinite Can).

Conservative launch: 3 passes + 3 dev products + starter pack. Expand after Phase 12 retention data.

---

## Phase 03 GDD handoff

Economy Designer delivers to GDD:

1. Cosmic Coin earn/spend tables (NPC price bands, unlock costs)
2. Exact Robux price points after playtest conversion data
3. Offline pollen cap ↔ monetization interaction (cap is generous; pass skips wait not cap)
4. Server receipt handler spec (`ProcessReceipt` idempotency per [Simplified Media guide](https://simplified.media/guides/roblox-monetization))

---

## Economy/Monetization Designer recommendation

**Monetization model: APPROVED for Phase 02** — **Cozy Fair F2P** with deterministic passes and dev products only; no paid random at launch.

Aligns with vision, compliance PASS, and GAG commercial lane without steal/gacha baggage.
