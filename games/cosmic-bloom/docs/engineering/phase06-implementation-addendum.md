# Cosmic Bloom — Phase 06 Implementation Addendum

**Date:** 2026-07-01
**Purpose:** Technical handoff before Luau/Rojo implementation.
**Source of truth:** GDD §10 for acceptance criteria, plus the ADRs listed below.

---

## Required ADRs

| ADR | Topic |
|-----|-------|
| ADR-003 | Persistence architecture and schema ownership |
| ADR-004 | Cosmic Spin finite-state machine and snapshot fairness |
| ADR-005 | Unified rolling 24h clock policy |
| ADR-006 | Server remotes and validation matrix |
| ADR-007 | Marketplace receipt idempotency and purchase caps |
| ADR-008 | Event scheduler and Private Meadow audit rule |

---

## Server Authority Rules

- Server owns all currency, inventory, cooldowns, timers, ownership, rolls, odds, rewards, and purchases.
- Client may request intent only: plant, nurture, harvest, splice, deliver, contribute, spin, claim, purchase prompt.
- Server validates every request against persisted profile and server config.
- No client-provided reward amount, timer value, seed ID grant, spin result, purchase grant, or Feed contribution tier may be trusted.
- All content IDs should come from server-authored content tables.

---

## Initial Module Boundaries

| Module | Owns |
|--------|------|
| `ProfileService` / persistence wrapper | Player profile load/save, schema migrations, receipt history |
| `GardenService` | Plots, planting, growth, harvest buffers, offline growth |
| `InventoryService` | Seeds, pollen, fruit, Stardust, Comet Shards, Spin Tokens, cosmetics |
| `NurseryService` | Splice sessions, mutation rolls, Prize Bloom rolls |
| `OutpostService` | Personal planet orders, round state, payouts |
| `CommunityTableService` | Server event goals, contribution tiers, rewards |
| `CosmicSpinService` | Daily spin validation, SpinSession FSM, odds snapshots |
| `EventSchedulerService` | Meteors, Community Table, weekly Legendary rotation windows |
| `MarketplaceServiceAdapter` | Game pass checks, dev product receipts, idempotency |
| `TelemetryService` | Tutorial, economy, purchases, event participation |

Names may change during implementation, but ownership boundaries should not blur.

---

## Profile Schema Draft

| Field | Owner | Notes |
|-------|-------|-------|
| `schemaVersion` | Persistence | Migration gate |
| `currencies.cosmicCoins` | Inventory | Earned + dev product grants |
| `currencies.stardust` | Inventory | Harvest + rewards |
| `currencies.cometShards` | Inventory | Meteors + Community Table |
| `items.spinTokens` | Inventory | Earn-only extra spins |
| `inventory.seeds` | Inventory | Server content IDs |
| `inventory.pollen` | Inventory | Breed IDs + counts |
| `inventory.fruit` | Inventory | Fruit IDs + counts |
| `garden.plots` | Garden | Plot IDs, seed IDs, planted time, stored harvests |
| `garden.upgrades` | Garden | Rows, soil, offline storage |
| `nursery.sessions` | Nursery | Active splice jobs and completion times |
| `bloomdex.discoveries` | Bloomdex | Breed/mutation/Prize Bloom flags |
| `planets.rounds` | Outpost | Current round per planet |
| `keeper.rank` | Keeper | Rank 1–5 |
| `daily.lastClaimAt` | Clock | Rolling 24h Daily Trio |
| `spin.lastFreeSpinAt` | Clock/Spin | Rolling 24h free spin |
| `social.swabLog` | Clock/Social | Per target plant / rolling limit |
| `purchases.gamePasses` | Marketplace | Cached ownership for current session |
| `purchases.receipts` | Marketplace | Processed dev product receipt IDs |

---

## Remote Validation Matrix

| Remote intent | Required server validation |
|---------------|----------------------------|
| Plant seed | Player owns seed, plot exists, plot empty, seed is plantable, no invalid client timer |
| Nurture plot | Plot belongs to player, tool unlocked, cooldown/pass valid, correct phase bonus computed server-side |
| Harvest plot | Plot belongs to player, mature by server time, buffer available, rewards computed server-side |
| Start splice | Pollen counts sufficient, pair allowed, nursery slot free, tier valid |
| Claim splice | Session complete by server time, result generated/claimed once |
| Deliver order | Player owns required fruit, planet unlocked, round state current, payout computed server-side |
| Contribute Community Table | Event active, fruit eligible, counts available, tier state server-owned |
| Request spin | Free spin available or Spin Token count > 0, session not already pending, snapshot created server-side |
| Resolve spin | Session exists, belongs to player, not already resolved, roll uses stored snapshot only |
| Claim meteor crate | Event crate assigned to player, unclaimed, loot rolled server-side |
| Swab pollen | Target plant eligible, owner not blocked, per-day and per-plant limits valid, no owner inventory removal |
| Equip cosmetic | Player owns cosmetic, slot/category valid |

---

## Event Scheduler Rules

- Community Table cadence: roughly every 30 minutes on a Lumina / Solara / Glimmer loop.
- Meteor shower cadence: roughly every 20 minutes at night.
- Cosmic Spin Legendary rotation: weekly pool reset; board item rotates on completed Legendary claim for new spins only.
- Scheduler uses server time and deterministic event windows.
- Event windows should survive server restarts by recomputing from canonical time, not by trusting client clocks.
- Private Meadow state may alter only Community Table server-goal constants.

---

## Marketplace Rules

- Game pass ownership is checked on the server before applying pass effects.
- Dev product grants are idempotent by receipt ID.
- Bloom Rush applies only to one selected planted crop and never grants inventory directly.
- Cosmic Coin products grant fixed deterministic amounts.
- Meadow Starter Kit is once per account.
- No receipt path may grant Spin Tokens, random seeds, Comet Shards, exclusive breeds, Cosmic Spin pulls, or Prize Blooms.
- Purchase caps must be enforced server-side where applicable.

---

## Private Meadow Audit Rule

Implementation must support this grep-able invariant:

> The only gameplay formula allowed to branch on VIP/private server state is the Community Table server-goal calculation.

Do not branch on private server state for:

- Growth timers
- Harvest yield
- Stardust
- Outpost payouts
- Personal Community Table thresholds
- Meteor odds
- Cosmic Spin odds
- Nursery speed or luck
- Bloomdex gates

---

## Telemetry Minimums

| Event | Reason |
|-------|--------|
| Tutorial step reached | Find first-session drop-offs |
| First harvest time | Validate first 30–90 seconds |
| First delivery time | Validate tutorial pacing |
| First splice start / claim | Validate Stellar Nursery clarity |
| Lumina R5 / R10 | Validate economy proof |
| Second row purchase | Validate row timing |
| Nursery T2/T3 purchase | Validate Stardust gates |
| Community Table contribution tier | Validate public/private clear rates |
| Spin Token earn/spend | Validate spin faucet |
| Extra Garden Beds owner pacing | Validate pass risk |
| Purchase receipt result | Audit marketplace idempotency |

---

## Phase 06 Entry Checklist

- [ ] ADR-003 through ADR-008 accepted.
- [ ] Content catalog imported into implementation tasks.
- [ ] Economy constants reflect hardening proof.
- [ ] Remote matrix converted into server tests.
- [ ] Marketplace receipt tests created before dev products ship.
- [ ] Private Meadow audit is part of code review checklist.
- [ ] No Luau implementation begins from older superseded research docs.
