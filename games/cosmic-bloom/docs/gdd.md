# Game Design Document — Cosmic Bloom

**Game:** Cosmic Bloom (`cosmic-bloom`)  
**Phase:** 03 — Game Design Document  
**Status:** Draft — GDD Steps 1–6 complete · Step 7 (EP sign-off) pending  
**Last updated:** 2026-06-28

| Doc | Path |
|-----|------|
| Vision | [VISION.md](./VISION.md) |
| Pitch | [studio/docs/discovery/pitch-sells-cosmic-bloom.md](../../../studio/docs/discovery/pitch-sells-cosmic-bloom.md) |
| ADR-002 | [studio/docs/decisions/002-game-direction-cosmic-bloom.md](../../../studio/docs/decisions/002-game-direction-cosmic-bloom.md) |
| Compliance | [studio/docs/compliance/concept-compliance-checklist.md](../../../studio/docs/compliance/concept-compliance-checklist.md) |

## Locked constraints (Phase 02)

- **Rating:** Minimal / all ages
- **Monetization:** Cozy Fair F2P — no paid random at launch
- **Platform:** Roblox; server-authoritative sim
- **Audience:** Solo-first; friends on same server with **separate gardens** (not shared-plot co-op in v1)
- **Economy safety:** **No player-to-player trading or exchange in v1**
- **World:** Open starlit meadows — **no enclosed glass domes**

---

## EP foundation (workshop v7 — 2026-06-28)

| # | Topic | Decision |
|---|-------|----------|
| 1 | Bloomdex UI | Literal **collection shapes** + hoverable stars → unlock criteria (§1.3) |
| 2 | Night sky | **Post-MVP** — completed collections in sky above plot; visitors see (§1.3b) |
| 3 | Spin board | **Server-authoritative, client-triggered**; legendary **snapshot on spin start** (§1.11) |
| 4 | Bloom fruit | **Many distinct types**; **3 fruits/planet**; **multi-line supply orders** (§1.7) |
| 5 | First discoverer | Recognition race when **new breeds** ship (§1.3c) |
| 6 | Currency | **Cosmic Coins** |
| 7 | Collection size | **Variable** star counts per collection |
| 8–9 | Names / lore | **Fantasy-universe constellations** — concept stays; **no real-Earth** IAU names or sky maps |
| 10 | Nursery | **Splice luck** (↑ mutation odds); slots + speed (§1.4) |
| 11 | Mutations | **≥3 per base breed** — **MVP** (§1.4b) |
| 12 | Decor | Meadow decor = **visual + plot buffs** (§1.8) |
| 13 | Group feed | **Community Feed** at Outpost — **MVP required** (§1.7b) |
| 14 | Planet unlock | Milestone on previous planet; switch freely (§1.7c) |
| 15 | Prize Blooms | Display cases **only** — no Outpost duplicate |
| Q68 | Display cases | **3 cases, 1 Prize Bloom each** — unlock per planet milestone (§1.10) |
| Q69 | Planet unlock gates | **Lumina R10 → Solara; Solara R15 → Glimmer; Glimmer R20 → Launch Pad** *(§1.7c)* |
| Q70 | Launch breed roster | **10 bases + 12 crosses + 10 sig. mutations** *(§1.2b)* |
| Q71 | Keeper Rank + dailies | **Light** — Rank 1–5, 5 story beats, daily triad *(§3.1)* |
| Q72 | Tutorial | **Guided ~8 min** *(§2.1)* |
| Q73 | Nurture tools | **Moon / Sun / Twilight** + **Infinite Nurture** pass *(§1.5, §6)* |
| Q74 | Private servers | **v1 launch** — invite-only meadows *(§1.9, §6)* |
| 16 | Cozy Fair | Spin Tokens **earned only** — no pay-to-win spins |
| 18 | Legendary duplicates | **Both get copy** if snapshotted wins overlap (§1.11, Q59) |
| Q67 | Moth collectors | **Cut MVP** — pollen player-initiated only (§1.2, §1.5) |

*v4 table archived in document history.*

---

## 1. Overview

### One-line pitch

Breed cosmic plants under sun and moon in **open meadows**, fill the **Bloomdex**, deliver harvests at the **Orbital Outpost** to **feed distant planets**, upgrade your **garden** and **Stellar Nursery**, and race **night meteor showers** with the whole server.

### Design pillars

1. **Breed & complete** — cross-breeding + codex “grow ’em all”
2. **Do good, get paid** — feeding planets turns work into Cosmic Coins and wholesome stats
3. **Upgrade everything** — garden, soil, nursery, tools, display cases
4. **Shared sky events** — meteor showers + **Community Feed** (server co-op) without PvP
5. **Cozy mastery** — breadth over punishing loss; no steal, no scams, no rebirth reset
6. **Earn everything** — Robux is convenience only (detail in §6)

---

### 1.1 What every player owns vs the hub

| Location | What’s there |
|----------|----------------|
| **Your garden** | Open meadow plots, soil upgrades, **display cases** for Prize Blooms, visit stats board |
| **Your Stellar Nursery** | Cross-breed stations; upgrade **splice slots**, **speed**, **splice luck** |
| **Central meadow hub** | Orbital Outpost, Meteor Merchant, Seed Stand, Cosmic Spin, Leaderboards |

**No personal market stall.** All selling / planet-feeding happens at shared hub booths.

---

### 1.2 Terminology *(working — EP review)*

#### Inputs (things you plant or combine)

| Term | Source | Used for |
|------|--------|----------|
| **Seed** | Seed Stand *(common starters)*, cross-breed, meteors *(occasional)*, Community Feed *(top tier)*, quests | Plant in garden plot |
| **Pollen** | **Player harvest** from own mature plants; **player swab** from others’ mature plants (3/day) | Cross-breed input in nursery |

#### Outputs (things you harvest)

| Term | Source | Used for |
|------|--------|----------|
| **Bloom fruit** | Primary harvest — **one distinct type per plant breed** (Glow Berry, Moon Melon, Sun Peach…) | Orbital Outpost supply orders + Community Feed |
| **Stardust** | Secondary byproduct on some harvests | Cross-breed catalyst, soil / nursery upgrades |
| **Prize Bloom** | Rare cross-breed or mutation trophy | **Display cases only** — not sold or duplicated |
| **Spin Token** | Rare drops & events *(inventory item, not wallet)* | Extra turns on the **server Cosmic Spin board** beyond 1 free/day |

*Each plant yields its **own** bloom fruit type. Planets never share a generic “fruit” bucket.*

#### Pollen rules *(Q67 locked)*

**Pollen is collected by players only** — no moths, NPCs, or passive auto-drip.

| Action | Who | Limit |
|--------|-----|-------|
| **Harvest pollen** | You, from **your** mature plants | Unlimited (normal harvest) |
| **Pollen swab** | You, from **another player’s** mature plant | **3 / 24h**; once per foreign plant per day *(Q62)* |

*Decor/tools may widen swab/harvest **radius** — still requires player interaction.*

#### Breed layers *(Q51 + Q63 — clarify 9 fruits ≠ 9 plants)*

| Layer | Launch scope | Role |
|-------|--------------|------|
| **Planet delivery fruits** | **9 fruit types** (3 per planet) | **Only** these fulfill **supply orders** for Lumina / Solara / Glimmer |
| **Base breeds** | **10** on star maps *(Q70)* | See §1.2b — 9 planet-fruit bases + **Flare Mint** (off-menu bridge) |
| **Cross-bred breeds** | **12** discoverable at launch *(Q63 + Q70)* | Stellar Nursery outputs — tiered A→D cross matrix (§1.2b) |
| **Mutations** | **≥3 per base** in full Bloomdex index | Variants; **~10 signature** mutations occupy star-map slots |

**9 planet fruits ≠ 9 total plants.** The nine are the **Outpost delivery menu** — what hungry planets accept. Cross-breeding, meteors, and events add **many more breeds** whose fruits may feed Community Feed, future planets, or exist purely for pollen / Prize Blooms / breeding chains.

**Example:** You discover **Starlace Vine** (C1 cross) — produces **Starlace Fruit** (not on any v1 planet menu). Use its **pollen** in Tier B splices toward sunbound breeds; fruit counts toward **Solara Supper** Community Feed when that theme is active — but **Lumina supply orders** still only take Glow Berry, Moon Melon, Nebula Pod.

#### Launch breed roster *(Q70 locked — EP approved 2026-06-28)*

##### Base breeds *(10 — all occupy star-map slots)*

| # | Plant | Fruit | Affinity | Collection | Planet delivery |
|---|-------|-------|----------|------------|-----------------|
| 1 | **Glow Mote** | Glow Berry | Moonbound | Little Slipper | Lumina *(tutorial seed)* |
| 2 | **Moon Melon** | Moon Melon | Moonbound | Little Slipper | Lumina |
| 3 | **Nebula Sprout** | Nebula Pod | Moonbound | Little Slipper | Lumina |
| 4 | **Sun Peach** | Sun Peach | Sunbound | Sun Rawr | Solara |
| 5 | **Star Carrot** | Star Carrot | Sunbound | Sun Rawr | Solara |
| 6 | **Blaze Blossom** | Blaze Blossom | Sunbound | Sun Rawr | Solara |
| 7 | **Flare Mint** | Flare Nectar *(off-menu)* | Sunbound | Sun Rawr | Community Feed / pollen bridge only |
| 8 | **Dusk Lace** | Dusk Lace | Twilight | Silver Weaver | Glimmer |
| 9 | **Twilight Pod** | Twilight Pod | Twilight | Silver Weaver | Glimmer |
| 10 | **Eclipse Fern** | Eclipse Fern | Twilight | Silver Weaver | Glimmer |

**Seed Stand (Cosmic Coins):** Glow Mote, Moon Melon, Nebula Sprout. Sunbound and twilight **bases** are **not** sold at the Stand at launch — obtain via cross-breed chain, meteors, or Community Feed.

##### Signature map mutations *(10 + 1 prize star)*

| Collection | Base | Signature mutation *(map star)* |
|------------|------|----------------------------------|
| Little Slipper | Glow Mote | **Shimmer** Glow Berry |
| Little Slipper | Moon Melon | **Giant** Moon Melon |
| Little Slipper | Nebula Sprout | **Void** Nebula Pod |
| Sun Rawr | Sun Peach | **Golden** Sun Peach |
| Sun Rawr | Star Carrot | **Striped** Star Carrot |
| Sun Rawr | Blaze Blossom | **Double** Blaze Blossom |
| Sun Rawr | Flare Mint | **Spicy** Flare Nectar |
| Silver Weaver | Dusk Lace | **Woven** Dusk Lace |
| Silver Weaver | Twilight Pod | **Glowing** Twilight Pod |
| Silver Weaver | Eclipse Fern | **Silver** Eclipse Fern |
| Silver Weaver | *(prize star)* | Complete map → **Weaver's Lantern** decor |

*Full Bloomdex index lists **≥3 mutations per base** at launch; only **signature** mutations above occupy collection map stars.*

##### Cross-breed matrix *(12 primary outcomes)*

*Splice luck may also roll duplicate pollen, off-table mutations, or rare Prize Blooms — primary deterministic outcomes:*

**Tier A — Lumina × Lumina** *(first hour)*

| ID | Pollen A | Pollen B | → Breed | → Fruit |
|----|----------|----------|---------|---------|
| C1 | Glow Mote | Moon Melon | **Starlace Vine** | Starlace Fruit |
| C2 | Glow Mote | Nebula Sprout | **Comet Cap** | Comet Cap Fruit |
| C3 | Moon Melon | Nebula Sprout | **Dreamroot** | Dream Fruit |

**Tier B — Toward Solara** *(grow early / deliver later — Q52)*

| ID | Pollen A | Pollen B | → Breed | → Fruit |
|----|----------|----------|---------|---------|
| C4 | Starlace Vine | Sun Peach | **Sunthread Moss** | Sunthread Fruit |
| C5 | Comet Cap | Star Carrot | **Halo Sprig** | Halo Fruit |
| C6 | Dreamroot | Blaze Blossom | **Dawn Petal** | Dawn Petal Fruit |
| C7 | Flare Mint | Glow Mote | **Heat Shimmer** | Heat Shimmer Fruit |

**Tier C — Toward Glimmer**

| ID | Pollen A | Pollen B | → Breed | → Fruit |
|----|----------|----------|---------|---------|
| C8 | Sunthread Moss | Dusk Lace | **Glimmer Ivy** | Glimmer Fruit |
| C9 | Halo Sprig | Twilight Pod | **Veilcap** | Veilcap Fruit |
| C10 | Dawn Petal | Eclipse Fern | **Nightglint** | Nightglint Fruit |

**Tier D — Deep chain**

| ID | Pollen A | Pollen B | → Breed | → Fruit |
|----|----------|----------|---------|---------|
| C11 | Starlace Vine | Glimmer Ivy | **Weaver Vine** | Weaver Fruit |
| C12 | Heat Shimmer | Nightglint | **Skyknot Bloom** | Skyknot Fruit *(Prize Bloom-leaning)* |

**Forward seed paths:** Tier A from Broker starters. Tier B requires sunbound pollen (cross chain or meteor). **Flare Mint** seeds from **Solara Supper** Community Feed tier 2+ or meteors. Tier C requires twilight bases from C8–C10 chain or meteors.

*Splice luck %, duplicate pollen rates, and meteor drop weights — **§5.5–5.8**.*

#### Seed obtain paths *(Q53 locked)*

| Tier | Sources |
|------|---------|
| **Common starters** | Seed Stand: **Glow Mote, Moon Melon, Nebula Sprout**; tutorial; Keeper quests |
| **Discovery seeds** | **Primary:** Stellar Nursery cross-breed + pollen swabs |
| **Forward seeds / pollen** | **Secondary (earn-only):** meteor crate rare drops; Community Feed top-tier rewards; first discoverer |

**Seed Stand never sells** twilight / cross-bred / planet-tier rare seeds at launch. No Robux seed packs for undiscovered breeds (Cozy Fair).

*Grow gate (Q52): any legitimately obtained seed can be planted anytime; deliver gate stays linear.*

#### Currencies

| Currency | Earn | Spend |
|----------|------|-------|
| **Cosmic Coins** | Outpost deliveries, Community Feed tiers, quests, dailies, spin board (small), achievements | Seeds (Seed Stand), garden expansions, soil, nursery, tools, display cases, **buff decor** |
| **Comet Shards** | Meteor crash crates, Community Feed top tier | Meteor Merchant — event seeds, decor, cosmetics |

**Spin Tokens are not purchasable** with Robux or Cosmic Coins at launch.

#### Collection meta

| Term | Meaning |
|------|---------|
| **Bloomdex** | Pokédex-style log — breeds, mutations, collection maps |
| **Collection** | Themed group with **variable star count** — e.g. *Little Slipper 4/6* |
| **Collection completion** | All stars in a collection lit → unlock reward |
| **Mutation** | Variant of a base breed (≥3 per breed at launch) — separate Bloomdex criteria |

---

### 1.3 Bloomdex (collection / completeness)

Like a **Pokédex**: discover a breed or mutation → entry unlocks with art, affinity, and lore.

#### Naming & iconography *(locked)*

- **Constellations exist** in Cosmic Bloom’s fantasy universe — same concept as Earth, **different star patterns and names** (another part of the galaxy)
- Collection names are **invented** — **Little Slipper**, **Sun Rawr**, **Silver Weaver** — **not** real IAU names (Orion, Leo, Cassiopeia, etc.)
- **Keep in-game terms:** *constellation*, **Constellation Keeper** (tutorial NPC), **Constellation Chronicle** (achievement UI)
- **Ban:** real-world constellation names, “inspired by the Little Dipper” lore text, projecting real sky maps
- **Graphic = literal fantasy shape:** Little Slipper map = **slipper silhouette** with stars; not a copy of Ursa Minor

#### Star map UI *(MVP)*

Each collection opens a **constellation-shaped star map**:

- **Stars** = individual unlock slots (breed discovery, mutation discovery, collection milestone)
- **Hover star** → tooltip: *“Grow a Moon Melon”*, *“Discover Shimmer mutation on Glow Berry”*, etc.
- Lit stars fill in; completing the shape = collection complete

#### Launch collections *(variable sizes — Q51 locked)*

**v1 model:** **21 star-map slots** — not “21 base breeds each with map stars.”

| Collection | Stars | Shape | Slot breakdown |
|------------|-------|-------|----------------|
| **Little Slipper** | **6** | Slipper | Glow Mote, Moon Melon, Nebula Sprout + Shimmer / Giant / Void mutations |
| **Sun Rawr** | **8** | Lion rawr | Sun Peach, Star Carrot, Blaze Blossom, Flare Mint + Golden / Striped / Double / Spicy mutations |
| **Silver Weaver** | **7** | Woven arc | Dusk Lace, Twilight Pod, Eclipse Fern + Woven / Glowing / Silver mutations + **Weaver's Lantern** prize |

**Totals:** ~**10 base breeds** · ~**10 signature mutations** on maps · **1 prize star**

**Full Bloomdex index** (separate from star maps) still tracks **≥3 mutations per base breed** at launch — grow/harvest/splice discovery. Only **signature** mutations occupy collection map stars; other mutations fill index pages and feed splice luck chase without lighting map stars.

More breeds, mutation stars, and collections via live ops.

#### 1.3b Night sky — completed collections *(post-MVP)*

When a collection is **100% complete**, those stars also appear in the **game sky above your garden plot** (visible at night only). Visitors who walk onto your plot can **look up** and see your accomplishments. Bloomdex UI remains source of truth at launch; sky projection is a **visual flex layer** added after MVP.

#### 1.3c First discoverer *(live ops + launch day races)*

When a **new breed or mutation** ships (patch, season, meteor table):

- **First player on the server** to register the discovery gets *(Q57 locked — per-server only)*:
  - **First Bloom** title on the Bloomdex entry (cosmetic frame on that entry)
  - **Spin Tokens** + bonus Cosmic Coins
  - Hub toast: *“@Player was first to discover Dusk Lace on this server!”*
- Each server runs its **own** patch-day race — no global cross-server winner at launch
- Drives pollen swabs, splice luck grinding, and community excitement — **no pay gate**

---

### 1.3d Planets at launch *(scope)*

**3 planets** — each accepts **exactly 3 bloom fruit types** (not interchangeable between planets).

| Planet | Unlock gate | Accepted fruits *(only these)* |
|--------|-------------|--------------------------------|
| **Lumina** | Start | Glow Berry, Moon Melon, Nebula Pod |
| **Solara** | Lumina **Round 10** | Sun Peach, Star Carrot, Blaze Blossom |
| **Glimmer** | Solara **Round 15** | Dusk Lace, Twilight Pod, Eclipse Fern |

- **Switch freely** between **unlocked** planets at Outpost — return to Lumina round 50 anytime
- **Grow vs deliver (Q52):** Players may **obtain, plant, and harvest** any bloom fruit they legitimately unlock (cross-breed, meteor, pollen swab, etc.) **before** that fruit’s planet accepts deliveries. **Outpost delivery** to a planet stays **linearly gated** — no skipping ahead on supply orders.
- Live ops adds planets (~10 year one); each brings new fruit types + Bloomdex entries

---

### 1.4 Stellar Nursery (upgradeable greenhouse)

**Name locked:** **Stellar Nursery** — personal greenhouse for cross-breeding and mutation chasing.

| Upgrade axis | Effect |
|--------------|--------|
| **Splice slots** | More simultaneous cross-breeds (1 → 2 → 3) |
| **Splice speed** | Shorter wait per cross-breed — tier 1 **~3 min** → max upgrade **~1 min** *(Q64)* |
| **Splice luck** | ↑ chance of **rare outcomes** — especially **mutations** and new breed rolls |

**Splice timing *(Q64):** Real-time wait at nursery — **~3 minutes** at tier 1; continues while **offline**. Short reveal animation on complete. Upgrades + passes reduce wait; never instant skip at launch without upgrade.

Cross-breed flow:

1. Collect **Pollen A** + **Pollen B** (your harvest or **swab** from friends’ gardens)
2. Start splice in nursery — **splice luck** rolls on outcome table
3. Outcome: known **seed**, **mutation** variant, duplicate pollen, or rare **Prize Bloom**

First-time breed or mutation → **Bloomdex** star + collection progress.

#### 1.4b Mutations *(MVP required)*

Every **base breed at launch** ships with **≥3 mutations** (visual + minor stat twist — e.g. +yield, +size, alternate fruit tint).

| Mutation source | Example |
|-----------------|--------|
| Grow & harvest RNG | Shimmer Glow Berry |
| Cross-breed with splice luck | Eclipse Moon Melon |
| Event pollen | Comet-touched variant |

- Mutations have **signature slots** on collection maps; **full index** lists ≥3 variants per base breed (§1.3)
- **Why MVP:** mutations multiply collection depth without 3× base breed count; splice luck upgrade has clear purpose
- Post-MVP: more mutations per breed, seasonal mutation events

---

### 1.5 Day / night cycle, plant affinities & nurturing *(Q55)*

**Cycle:** ~12–15 min full loop (6–7 min day, 6–7 min night). Cozy, readable.

**Default rule:** **night = growth**, **day = harvest ripe fruit**.

| Affinity | Grows | Harvest |
|----------|-------|---------|
| **Moonbound** *(default)* | Night | Day |
| **Sunbound** | Day | Night |
| **Twilight** | Both phases (slower each) | Either phase when ripe |
| **Eclipse** *(rare)* | Dusk / dawn windows only | Short harvest window |

#### Nurture model *(Q55 — hybrid)*

| Mode | Behavior |
|------|----------|
| **Passive growth** | Plants **always** advance slowly on planted plots — including **offline**. Wrong phase = slower; neglected soil = slower. AFK-friendly baseline. |
| **Active nurture** | During the **correct phase** for that plant, use the matching tool → **bonus growth burst**; **90s cooldown** per plot *(§1.5 nurture tools)*. Optional but rewarding. Does **not** bypass phase — wrong phase = passive growth only *(slower)*. |
| **Modifiers** | Soil, tools, buff decor, and affinity match affect **both** passive rate and active burst strength. |

*Design intent: something to do between Outpost trips without punishing players who don’t babysit plots.*

#### Nurture tools *(Q73 locked)*

| Tool | Affinity | Active burst when | Notes |
|------|----------|-------------------|-------|
| **Moon Lantern** | Moonbound | **Night** *(grow phase)* | Tutorial tool |
| **Sun Scope** | Sunbound | **Day** *(grow phase)* | Unlock hint: first sunbound seed |
| **Twilight Lantern** | Twilight | **Day or night** | **−20%** burst vs perfect phase match |

**Passive growth** continues in all phases regardless of tools owned.

**Meteor showers:** **night only.**

**Pollen swabs *(Q62)*:** **3 swabs per 24 hours** from **other players’** mature plants — **player-initiated only**.

| Rule | Detail |
|------|--------|
| **Daily budget** | **3 swabs / 24h** — choose wisely which foreign pollen to sample |
| **Per-plant limit** | Each foreign plant **once per day** per player — no repeat camping |
| **Yield** | **1 pollen unit** per swab — nursery input only; no seeds or fruit stolen |
| **Own garden** | Harvest pollen from **your** plants **unlimited** (normal harvest) |

*Social discovery without pollen speedrunning.*

---

### 1.6 Meteor showers (server events)

**Schedule:** ~every **20 minutes** per server, **night phase only**.

**Flow:**

1. **Warning** — 30 s sky alert + tracker: *“Meteor shower inbound”*
2. **Shower** — visible streaks; **1–3 crash sites** in the meadow (scales with population)
3. **Run** — sprint to a crash marker
4. **Claim** — interact → **guaranteed personal loot** (one crate per player per shower)
5. **Cleanup** — crash sites despawn ~2 min after last claim window

**Meteor Merchant:**

- Appears at hub **~5 minutes after** the shower ends
- Stays open **~10 minutes**
- Accepts **Comet Shards** only — event seeds, meadow decor, limited cosmetics; **occasional forward-tier seed/pollen** in weekly rotation (earn-only)
- Rotating weekly stock — reason to show up; **shards not sold for Robux at launch**

---

### 1.7 Feed the planets (core wholesome loop)

**Fantasy:** Your meadow feeds the galaxy. Work becomes care.

#### Planet-specific diets & supply orders

Each planet accepts **only its 3 bloom fruit types** — never substitutes.

**Supply orders** (per round) are **multi-line planet orders**:

| Lumina — Round 2 example |
|--------------------------|
| 20 × Glow Berry |
| 15 × Moon Melon |
| 5 × Nebula Pod |

UI at **Orbital Outpost**: pick planet → see the planet order → load capsule when inventory satisfies all lines.

#### Recurring delivery rounds (never “done”)

| Round band | Order pattern | Reward scale |
|------------|---------------|--------------|
| 1 | Single starter fruit line *(Lumina R1 = 10 × Glow Berry; see §5.3)* | Modest Cosmic Coins + planet friends fed |
| 2–3 | Adds second / third planet fruit lines from the §5.3 table | Higher coins + Stardust via round milestones |
| 4+ | Escalating quantities; later rounds may add **one cross-bred** fruit line *(§5.3)* | Formula-driven payouts + milestone bonuses |

- **Per-player per-planet** round ladders — infinite depth
- Later rounds may require **mutations** or **meteor-only** fruit types

#### 1.7b Community Feed *(MVP — server co-op)*

**The server works together** at the Orbital Outpost on a schedule separate from personal planet orders.

| Field | Value |
|-------|-------|
| **Schedule** | Every **~30 minutes** per server *(offset from 20 min meteors)* *(Q65)* |
| **Duration** | **12-minute** contribution window |
| **Day / night** | Runs **any phase** — social midday activity |
| **Theme rotation** | **3-feed loop** — see below *(Q54 locked)* |

#### Rotating feed themes *(Q54)*

Feeds **rotate focus** — not every feed asks for every planet’s fruit at once.

| Feed theme | Order focus | Who can contribute |
|------------|----------------|-------------------|
| **Lumina Luncheon** | Glow Berry, Moon Melon, Nebula Pod | **Everyone** — always reachable on loop |
| **Solara Supper** | Sun Peach, Star Carrot, Blaze Blossom | Players who **grow** solara-tier fruit *(cross-breed / events)* |
| **Glimmer Gathering** | Dusk Lace, Twilight Pod, Eclipse Fern | Players with twilight seeds; **feed slot gated** until the server is Glimmer-ready *(rule below)* |

**Loop:** Lumina → Solara → Glimmer → **Lumina again** …

- If you **don’t have seeds** for the current theme, the Community Table explains what fruit is needed and when Lumina returns — personal tiers are unavailable for fruit you do not grow
- **No one is permanently excluded:** the schedule **always loops back to Lumina Luncheon**, which every player can join
- Prepared breeders shine on Solara / Glimmer feeds; new players always get another Lumina feed soon

**Glimmer-ready gate:** The Glimmer slot enters rotation only when the server has enough progressed gardeners: at least **50% of active loaded profiles** have reached **Solara R10+**. In private servers or low-population servers with fewer than 4 active players, the VIP owner reaching **Solara R10+** is sufficient. If the gate is not met, the third slot becomes another **Lumina Luncheon** instead of Glimmer Gathering.

**Flow:**

1. **Announcement** — hub + UI: *“Community Feed: Lumina Luncheon — moonfruit for the table!”*
2. **Shared goal** — server-wide progress bar (quantities scale with **active player count**)
3. **Order** — **theme-appropriate fruit lines only** generated from §5.7 (e.g. 12-player public Lumina goal = **7,800 Glow Berry + 3,900 Moon Melon + 1,300 Nebula Pod**)
4. **Contribute** — add eligible bloom fruit to the **Community Table** *(invalid fruit types rejected with friendly copy)*
5. **Personal tiers** — contribution thresholds on **eligible fruit only**:

| Your contribution | Reward tier |
|-------------------|-------------|
| 25+ fruit | Cosmic Coins + small Stardust |
| 100+ fruit | + Comet Shard |
| 500+ fruit | + **Spin Token** + event pollen; **chance at forward seed** *(twilight / undiscovered tier)* |

6. **Server clear bonus** — bar hits 100% before window ends: every contributor gets bonus Spin Token + Comet Shard bundle + 10 min **+10% Outpost coin** buff

**Why MVP:** Server co-op without trading; Lumina loop guarantees **everyone participates sometimes**; advanced feeds reward preparation.

#### 1.7c Planet unlock chain *(Q69 locked)*

| Planet / feature | Unlock |
|------------------|--------|
| **Lumina** | Available from tutorial |
| **Solara** | Reach **Lumina Round 10** |
| **Glimmer** | Reach **Solara Round 15** |
| **Launch Pad** *(post-MVP)* | Reach **Glimmer Round 20** |

Outpost planet picker shows locked worlds + requirement. **No forfeiting old planets** — Lumina round 100 remains playable after Glimmer unlocks.

**Escalating pattern:** +5 rounds on the prior planet per unlock tier — live ops can extend (R25, R30…) for future worlds.

**Two separate gates:**

| Gate | Rule |
|------|------|
| **Grow gate** | Can you **plant / harvest** this fruit? → Unlocked by seeds, cross-breed, events, pollen — **any time you earn it legitimately** |
| **Deliver gate** | Can you **fulfill supply orders** to this planet? → **Linear** — Solara requires Lumina R10; Glimmer requires Solara R15 |

Stockpiling Glimmer fruit before Glimmer unlock is **intended** — rewards prepared breeders.

#### Delivery flow (personal orders)

1. Harvest required **bloom fruit** types at your garden
2. Walk to hub **Orbital Outpost**
3. Fulfill **supply order** planet order → launch capsule
4. Earn **Cosmic Coins** + **planet friends fed**, **supply runs**, **highest round** stats
5. Advance to next round

---

### 1.8 Upgrades & decor buffs

| Category | Examples | Paid with |
|----------|----------|-----------|
| **Garden size** | +plot rows, meadow wings, **offline harvest storage** tiers | Cosmic Coins + Bloomdex gates |
| **Soil** | Moonloam, Sunpeat, Twilight mix | Cosmic Coins + Stardust |
| **Stellar Nursery** | Splice slots, speed, **splice luck** | Cosmic Coins + Stardust |
| **Tools** | Moon Lantern, Sun Scope, Twilight Lantern, pollen basket | Cosmic Coins |
| **Display cases** | Slots, lighting, plaques | Cosmic Coins — **3 case slots max** at launch *(Q68)* |
| **Meadow decor** | Meteor lantern, sunstone path, Pollen Basin, glow fence | Comet Shards or Cosmic Coins |

#### Meadow decor — look good **and** do good

Decor is **not pure cosmetic** — placed items give **small plot buffs** (stack capped to prevent runaway power):

| Decor example | Buff *(radius-limited)* |
|---------------|-------------------------|
| **Meteor lantern** | +5% night grow speed |
| **Sunstone path** | +5% day harvest yield on adjacent plots |
| **Pollen Basin** | +1 stud pollen gather radius |
| **Glow fence** | +3% mutation roll on plants inside border |

**Cap:** Max **3 active buff decor types** per garden — forces meaningful loadout choice.

---

### 1.9 Social model (solo-first, server-together)

**v1 model:** No shared plots, no co-op mechanics required. **Public meadows** *(up to 12)* or **invite-only private meadows** *(VIP servers — Q74)*.

| Feature | Behavior |
|---------|----------|
| **Public server** | Up to **12** gardens; strangers may share the hub — meteors, Community Feed, Cosmic Spin |
| **Private server** | **Invite-only** — friends & family, no random joiners. Same rules; **scaled** Community Feed goals *(§5.7)* — **does not** speed growth, deliveries, or spin |
| **Same server** | Each player tends **own garden + nursery** |
| **Visit base** | Stats board *(privacy controls v1)* + **look up at night** *(post-MVP: completed collections in sky)* |
| **Pollen gather** | **Player swab** — 3/day from others’ gardens; no automated collection |
| **Meteor shower** | Shared event — run together, personal crates, no loot stealing |
| **Trading** | **None in v1** — avoids scams and economy volatility |

*Store copy for private servers: **“Your own cozy meadow — invite who you want.”** Co-op plot sharing still deferred post-launch.*

**Private server fairness *(not a progression skip)*:** VIP meadows change **only** the shared Community Feed server goal pool *(§5.7)*. Plant grow timers, nurture cooldowns, nursery splice speed, Outpost delivery payouts, Bloomdex gates, meteor schedules, Cosmic Spin odds, and personal Feed thresholds are **identical** to public servers. Time-skip convenience remains separate SKUs *(Bloom Rush, Infinite Nurture)* — not bundled with private servers.

---

### 1.10 Display cases (prized grows) *(Q68 locked)*

- **Prize Blooms** and **mutation trophies** go in cases at your garden — **only slot, no selling duplicates**
- **Launch cap:** **3 display cases**, **1 Prize Bloom per case** — no extra slots at MVP
- **Unlock:** one case per **launch planet milestone** — Lumina → case 1, Solara → case 2, Glimmer → case 3
- Persist until swapped; visitors see on base tours

---

### 1.11 Cosmic Spin board *(hub — server-shared)*

One physical **Cosmic Spin board** at the hub — **the whole server shares it**. Spinning is a **public moment**, not a private menu.

**Architecture:** **Client-triggered, server-authoritative.** The client plays animation; the server alone validates, snapshots odds, resolves rolls, and grants items.

#### Spin session flow

```
Client: RequestSpin()
  → Server: validate (daily spin / Spin Token) → open SpinSession
  → Server: snapshot active legendary + odds → replicate hub banner to all clients
Client: play wheel animation (~6–8 s)
  → Server: ResolveSpin(sessionId) → roll using snapshot → grant reward
  → If legendary claimed: rotate board legendary for NEW sessions only
```

| Step | Owner | Detail |
|------|-------|--------|
| **Start** | Client initiates | Player interacts with board — server must approve before animation |
| **Snapshot** | Server | On approved start, server freezes **`legendaryId`**, **odds table**, and **`legendaryGeneration`** into the session |
| **Resolve** | Server | Roll uses **snapshot only** — never retroactive rule changes mid-spin |
| **Reveal** | Client + server | Result replicated; hub sees public tier-appropriate broadcast |

#### Concurrent in-flight spins

Multiple players may have **active SpinSessions** at once (not a single global mutex for the whole animation window).

| Rule | Detail |
|------|--------|
| **Overlap OK** | Player 2 can **start** while Player 1’s wheel is still spinning |
| **Board banner** | Shows active spinners — e.g. **`timmmmmmmmah is spinning`** (list or carousel if several) |
| **Fairness** | Each session resolves independently against **its own snapshot** |

#### Legendary snapshot & rotation *(kid-tested — EP locked)*

The board shows **one Legendary prize** at a time. Rotation timing is the subtle part:

| Event | What happens |
|-------|----------------|
| **Spin START** | Session records current legendary (e.g. *Nebula Glow Lantern*) + odds at that moment |
| **In-flight overlap** | All sessions started **before** the first legendary **claim completes** keep the **same legendary** and **same odds** they started with |
| **Legendary WIN + claim complete** | Winner gets item; server plays server-wide spectacle; board **rotates** to next legendary for **new** spin starts |
| **Late resolves** | Sessions still in-flight from **before** that claim may **still hit that same legendary** — they were snapshotted fairly |
| **After rotation** | New `RequestSpin()` calls bind to the **next** legendary only |

**Example:**

1. Legendary on board: **Nebula Glow Lantern**
2. Player 1 starts spin (snapshot: Lantern, odds X)
3. Player 2 starts spin before P1 finishes (snapshot: Lantern, odds X)
4. Player 1 resolves — **wins Legendary Lantern** → claim completes → board rotates to **Comet Wind Chime**
5. Player 2 resolves — still rolling against **Lantern** at odds X (may also win Lantern)
6. Player 3 starts **after** P1’s claim — snapshot: **Comet Wind Chime** only

**“Removes legendary for everyone”** means: **no new spins** bind to the old legendary after claim completes — **not** that in-flight snapshotted spins are invalidated.

*Multiple winners of the same legendary slot before rotation is intentional — everyone who started under that snapshot had a fair shot. Each receives the **same cosmetic/decor item** (unlimited copies per rotation window; double legendary hit is very rare).*

#### Server sizing *(Q60 locked)*

| Field | Value |
|-------|-------|
| **Max players per server** | **12** — adjust 10–16 after playtest if needed |
| **Garden lots** | **1 lot per player** — meadow plots ring around central hub |
| **Overflow** | Roblox matchmaking → next server instance when full |

*Distinct from **plot slots** inside a garden (starter 4 → expansions).*

#### Personal spin allowance

| Rule | Detail |
|------|--------|
| **Free spin** | **1 per rolling 24h** per player |
| **Extra spins** | Spend **Spin Token** — **1 token = 1 session** |
| **Not purchasable** | **No Robux spins. No Cosmic Coin spins.** |

#### Prize tiers & public reveal

| Tier | Audience experience |
|------|---------------------|
| Tiers 1–4 | Spinner sees result; hub toast for tiers 3–4 |
| **Tier 5 — Legendary** | **Full server spectacle** on claim — *“@timmmmmmmmah won LEGENDARY: Nebula Glow Lantern!”* |

Rewards grant to the **spinner’s inventory** only (server-authoritative).

#### Rotation table *(Q66 locked)*

- **7 unique legendaries** per server in the **weekly rotation pool** — cosmetic decor / skins (duplicate copies OK per Q59)
- One legendary **on the board** at a time; rotates on claim; pool **resets weekly** (Producer can swap items live-ops)
- Non-legendary tiers use fixed odds and do not rotate

#### Spin Token earn sources

Community Feed tier 3, server clear bonus, meteor epic roll, first discoverer, planet milestones, Daily Trio, achievements. Mutated harvests do **not** grant Spin Tokens at v1; they remain Bloomdex / Stardust moments.

#### UX notes

- **Recent wins ticker** — last 5 hub spins
- **Legendary history** strip — last 3 legendary claimants on this server
- Board readable from hub plaza — hang-out spot between events

*Economy intent: social spectacle + snapshot fairness + no pay-to-spin spam.*

---

### 1.12 Hub merchants & leaderboards

#### Merchants — primary purpose each

| Booth | Name | Primary purpose |
|-------|------|-----------------|
| **Planet feed + coins** | **Orbital Outpost** *(locked)* | Personal **supply orders** + **Community Table** |
| **Event shop** | **Meteor Merchant** | Comet Shards |
| **Seed supply** | **Seed Stand** | Common seeds for Cosmic Coins |
| **Cosmic Spin** | **Cosmic Spin board** *(server-shared)* | Client-triggered sessions; legendary snapshot; public reveals |
| **Rankings** | **Leaderboards** | Five uncapped boards (below) |
| *Future* | **Launch Pad** | Interstellar auto-quests — returns planet-specific seeds after timer |

**Retired:** Star Counter, polish-and-price, personal market stalls.

#### Leaderboards — design rules *(EP workshop v4)*

**Problem:** If v1 has only **3 planets**, a “planets fed” board caps at 3 for everyone — useless.

**Rule:** Launch leaderboards use stats that **never cap** — they keep climbing forever as players deliver, breed, and chase rounds.

| Board *(launch)* | Stat | Why it works |
|------------------|------|--------------|
| **Planet Friends Fed** | Lifetime planet friends nourished across all deliveries | Primary wholesome grind; always grows |
| **Supply Runs** | Total capsules sent from Orbital Outpost | Rewards consistency; uncapped |
| **Highest Round** | Best round reached on **any one** planet (e.g. Lumina R52) | Infinite round ladders → no tie ceiling |
| **Biggest Bloom** | Largest single-plant size score recorded | Competitive flex; grows with upgrades/meta |
| **Meteor Crates** | Lifetime crash crates claimed | Event-driven; uncapped |

**Hub UI:** One **Leaderboard sign** — interact to **page between** the five boards above.

**Not launch leaderboards** *(why)*:

| Stat | Issue |
|------|-------|
| Planets fed / unlocked | Caps at 3 (v1) — use **visit stats** (*Planets unlocked: 3/3*) instead |
| Bloomdex % | Soft-caps at 100% until new breeds ship — use **Discoveries** count in achievements / visit board, not eternal rank |
| Collection complete count | Caps at 3 — milestone badges, not grind board |

**Visit-stats board** (at each player’s garden): shows planet friends fed, supply runs, highest round, biggest bloom, Bloomdex **X/21 stars** (map progress) + index discoverable count, planets unlocked, display cases

---

### 1.13 Future — interstellar seed launches

*(Post-v1 or late vertical-slice stretch — EP flagged as exciting)*

- Hub **Launch Pad**: load a seed → auto-quest timer (minutes to hours)
- Returns **planet-specific seeds / pollen** not found on home meadow
- Extends “feed planets” fantasy in reverse — **they send gifts back**
- Pairs with codex completion and meteor rare drops

---

### Target session

| Length | Goal |
|--------|------|
| 30 sec | Check ripe fruit → quick Outpost delivery |
| 5 min | *(see §2.1)* — mid-tutorial: first delivery in progress |
| **~8 min** | **Tutorial complete** — plant, nurture, deliver, C1 splice, Bloomdex star |
| 30 min | First cross-breed chain; upgrade soil or nursery slot |
| 60 min | First **meteor shower** claimed; Meteor Merchant purchase; second Bloomdex collection started |

---

## 2. Core loop

### Loop diagram

```
Plant seed → nurture (sun / moon per affinity) → harvest bloom fruit & pollen →
cross-breed in Stellar Nursery → codex discovery →
deliver at Orbital Outpost (feed planets, earn Cosmic Coins) →
upgrade garden / soil / nursery / tools / display cases →
(repeat) + night meteor shower + Community Feed + pollen swabs + Cosmic Spin
```

**Primary verb:** BREED & COMPLETE  
**Secondary verb:** FEED THE PLANETS (wholesome delivery)

### Micro-loop (every 30 seconds)

| Step | Input | Output | Feel |
|------|-------|--------|------|
| Nurture | Passive tick + optional active burst (correct phase) | Growth progress | Cozy AFK + engaged bonus |
| Harvest | Ripe plant | Bloom fruit, pollen, maybe stardust | Burst VFX, inventory +1 |
| Breed | 2 pollen in nursery | New seed / Prize Bloom | Anticipation → reveal |
| Codex | First-time breed / mutation | Bloomdex star lit + collection progress |
| Deliver | Multi-line planet order | Cosmic Coins + feed stats | Capsule launch VFX |
| Community | Fruit into Community Table | Tier rewards + Spin Tokens | Server bar fills |
| Display | Rare Prize Bloom | Case slot at garden | Show-off permanence |

### Failure / friction model

- Plants do **not** permanently die
- Growth **slows** if wrong phase / neglected soil — recoverable
- No player-vs-player loss; no trading scams

### 2.1 First-session tutorial *(Q72 locked — guided ~8 min)*

**Constellation Keeper** escorts new players through the core loop. Tutorial completes **Keeper story beats 1–2** (→ **Rank 3**) and leaves the player free to explore.

#### Beat sequence

| Step | Action | Keeper / system |
|------|--------|-----------------|
| 1 | Spawn at **starter garden** — night meadow, Stellar Nursery beside **4 plots** | Welcome dialogue; waypoint to hub |
| 2 | Meet Keeper at **Orbital Outpost** — receive **Glow Mote** seed | *“Every star needs supper. Let’s grow something kind.”* |
| 3 | Plant Glow Mote → **passive growth** explained | Growth bar visible |
| 4 | **Active nurture** during moonlight *(moon lantern)* — bonus burst tutorial | Optional but prompted once |
| 5 | Harvest **Glow Berry** + Glow Mote pollen | Harvest VFX; inventory intro |
| 6 | Walk to **Orbital Outpost** — load **Lumina Round 1** capsule *(10 × Glow Berry; §5.3)* | Planet order UI teaser |
| 7 | Launch first delivery → Cosmic Coins + *“12 planet friends fed on Lumina”* | **Story beat 1** turn-in → **Rank 2** |
| 8 | Keeper grants **Moon Melon** + **Nebula Sprout** seeds — plant on plots 2 & 3 | Seed Stand intro *(visit later)* |
| 9 | Harvest **Moon Melon** + **Nebula Pod** pollen when ready *(tutorial growth accel)* | Affinity recap |
| 10 | **Stellar Nursery** — splice **Glow Mote + Moon Melon** → **C1 Starlace Vine** | Splice wait (~3 min) skippable with **tutorial accel** *(one-time)* |
| 11 | **Bloomdex** — **Little Slipper** star lit *(1/6)* | **Story beat 2** turn-in → **Rank 3** |
| 12 | Keeper release — *“The meadow is yours. Feed the stars.”* | Waypoints off; daily triad + beats 3–5 unlocked |

#### Rules

| Rule | Detail |
|------|--------|
| **Duration** | Target **~8 minutes** wall-clock *(tutorial splice accel shaves wait)* |
| **Skip** | **Returning players** *(account flag)* may skip to step 12 — tutorial rewards granted and player starts at **Rank 3** if skip chosen |
| **No monetization** | Zero Robux / pass prompts during tutorial |
| **Failsafe** | **30s idle** → Keeper **waypoint** + soft reminder ping |
| **Deferred** | Community Feed, Cosmic Spin, meteor shower — natural discovery after release *(~30 min / first night)* |

*Keeper voice and exact dialogue lines — **§9**.*

---

## 3. Progression

### Progression layers

| Track | Visible as | Drives |
|-------|------------|--------|
| **Keeper Rank** | Quest giver level *(1–5)* | Story beat access, explicit Outpost Cosmic Coin bonus lookup *(max +25%)* |
| **Bloomdex** | Bloomdex UI + collection completion | Plot rows, nursery tiers, decor |
| **Planet stats** | Personal + visit board | Achievements, titles, future planet unlocks |
| **Upgrades** | Garden, soil, nursery, tools, cases | Power + expression sinks |

### 3.1 Keeper Rank & dailies *(Q71 locked)*

**Model:** **Light** — Constellation Keeper is a **guide**, not a full quest board. Long-term goals stay on **Bloomdex**, **planet rounds**, and **Community Feed**.

#### Keeper Rank (1–5)

| Rank | How to reach | Outpost coin bonus |
|------|--------------|-------------------|
| **1** | Start *(post-spawn)* | — |
| **2** | Story beat 1 complete | +5% |
| **3** | Story beat 2 complete | +10% |
| **4** | Story beat 3 complete | +15% |
| **5** | Story beat 4 complete | +25% |

*Bonus applies to **Orbital Outpost** delivery payouts only — not Community Feed, spin board, or achievements.*

#### One-time story beats *(5 — Constellation Keeper at hub)*

| # | Beat | Requirement | Typical timing |
|---|------|-------------|----------------|
| 1 | **Feed the Stars** | Complete first Orbital Outpost capsule | Tutorial (~5 min) |
| 2 | **Mix the Pollen** | Complete first cross-breed *(C1 Starlace Vine)* | Tutorial (~5 min) |
| 3 | **Nursery Rising** | Upgrade Stellar Nursery to **tier 2** | ~30–60 min |
| 4 | **Catch a Falling Star** | Claim first **meteor crate** | First night shower (~20–40 min) |
| 5 | **Map the Meadow** | Light **6 Bloomdex stars** on any collection maps *(or complete Little Slipper)* | Mid-game capstone |

Beats 1–4: Keeper dialogue → objective pin on HUD → turn-in at hub → **+1 Rank** + small Cosmic Coin bundle. Beat 5 is the Rank 5 capstone: title / plaque reward + larger Cosmic Coin bundle, but **no Rank 6**.

**No endless quest log at launch** — only these five beats + dailies.

#### Daily Trio

Three quests refresh on a **rolling 24h per-account timer** from the player's first daily claim. Use the same reset model for Keeper dailies, free spins, and pollen swabs.

| Slot | Verb | Rank 1 example | Rank 5 example |
|------|------|----------------|----------------|
| **Breed** | Splice | Complete **1** cross-breed | Complete **2** cross-breeds |
| **Deliver** | Outpost | Feed **50** planet friends | Feed **500** planet friends |
| **Discover** | Harvest / Bloomdex | Harvest **2** fruit types | Register **1** new Bloomdex entry |

**Daily Trio bonus** *(all 3 complete):*

| Rank | Bonus |
|------|-------|
| **1–3** | Seed pack *(Glow Mote / Moon Melon / Nebula Sprout mix)* |
| **4–5** | **1 Spin Token** |

*Targets scale linearly between ranks; exact numbers tune in economy pass.*

### Unlock timeline (launch content)

#### 0–15 minutes

- 4 starter plots, Nursery tier 1 (1 splice slot)
- First Bloomdex entry, first planet delivery round

#### 15–60 minutes

| Time | Unlock |
|------|--------|
| ~15 min | **Second plot row** after first collection milestone |
| ~60–90 min | Nursery tier 2; **Solara** unlocks at Lumina **R10**; first **Community Feed** |
| ~45 min | **Nebula Ridge** garden extension — affinity soil slot |
| ~20–40 min | First **meteor shower** (if night) + Meteor Merchant window |

#### Mid-game (hours 2–10)

- **10 base breeds**, **12 cross-breds** (§1.2b) + signature mutations on maps; full index ≥3 mutations/breed
- **3 planets**, 3 fruits each; Community Feed every ~**30** min
- Keeper Rank 1–5
- **Display cases** — up to **3** (1 per planet milestone)

#### Long-term (days+)

- All 3 launch collections complete → meteor drop tier bump
- Achievement tier **Legendary** (Galaxy Gardener)
- Interstellar Launch Pad — unlocks at **Glimmer R20** *(post-MVP build)*

### Resources & gates

| Resource | Earn | Spend |
|----------|------|-------|
| **Cosmic Coins** | Outpost, Community Feed, quests, dailies, spin (small), achievements | Seeds, upgrades, decor |
| **Comet Shards** | Meteors, Community Feed | Meteor Merchant |
| **Spin Tokens** *(item)* | Community Feed, meteors, planet milestones, Daily Trio, first discoverer, achievements | Extra Cosmic Spin pulls |
| **Stardust** *(item)* | Harvest byproduct | Soil, nursery upgrades |
| **Pollen** *(item)* | Player harvest, player swab | Cross-breed |
| **Bloomdex entries** | First discovery per breed | Collection completion rewards |

### Space progression

```
Starter Garden (4 plots) + Nursery tier 1
  → Second row (+4 plots)
    → Nebula Ridge extension
      → [post-v1 meadow biomes]
```

### Offline progression *(Q61 locked)*

- **Passive growth** continues while offline (hybrid nurture model)
- **Per-plot harvest buffer:** each planted plot stores **1–2 ripe harvests** max while away; growth **pauses at cap** until login (no infinite offline pile)
- **Upgradeable offline storage:** garden upgrade track raises buffer per plot (e.g. +1 stored harvest per tier) — Cosmic Coins + Bloomdex gates; optional pass may add +1 globally later
- Missed meteor showers / Community Feeds while offline — next scheduled event on return

### Explicit exclusions (v1)

- **No rebirth reset**
- **No paywalled biomes** — gates are codex / coins
- **No Robux steal / PvP theft**
- **No player-to-player trading or exchange**
- **No glass domes**
- **No Robux / Cosmic Coin spin purchases**
- **No Prize Bloom Outpost selling**

---

## 4. Achievements

### Systems

- **Constellation Chronicle** — tiered in-game achievement UI
- **Roblox Badges** — ~15 Legendary milestones at launch

### Categories

| Category | Focus |
|----------|-------|
| Breeding | Cross-breeds, unique breeds, collection completion |
| Planetary | Planet friends fed, supply runs, highest round, delivery streaks |
| Codex | Bloomdex entries unlocked, full collections |
| Garden | Upgrades, biggest plant, display cases filled |
| Exploration | Meteors claimed, Meteor Merchant purchases |
| Keeper | Daily Trio, rank milestones |
| Social | Pollen swabs, Community Feed tiers, base visits, first discoverer |

### Tier rewards

| Tier | Count toward | Example reward |
|------|--------------|----------------|
| Spark | 5 | 100 Cosmic Coins |
| Nebula | 15 | Display case plaque cosmetic |
| Galaxy | 30 | Nursery exterior cosmetic |
| Cosmic | 50 | Nursery exterior cosmetic |
| Legendary | All launch | Badge + title *Galaxy Gardener* |

### Daily retention — Keeper triad *(see §3.1)*

Three daily quests (Breed / Deliver / Discover); rolling 24h personal reset; Daily Trio bonus = seed pack (R1–3) or Spin Token (R4–5). Full rank scaling in §3.1.

### Launch achievement samples (v1)

| ID | Name | Trigger |
|----|------|---------|
| A01 | First Sprout | Plant Nebula Sprout |
| A04 | First Delivery | Complete one Orbital Outpost capsule |
| A06 | Meadowward | Unlock second plot row |
| A08 | Collection Complete | Complete one full Bloomdex collection map |
| A30 | Neighborly Chef | Hit tier 3 in a Community Feed |
| A15 | Galaxy Gardener | Complete all 3 launch collections |
| A20 | Meteor Runner | Claim first meteor crate |
| A25 | Good Neighbor | Swab pollen from 3 different players’ plants (one day) |

Full list: 40 achievements target for vertical slice scope.

---

## 5. Economy & systems balance *(Step 2 — systems designer, 2026-06-28)*

*Launch breed roster and cross matrix locked in **§1.2b (Q70)**. Numbers here are **v1 targets** — tune in playtest; formulas are authoritative for implementation.*

### 5.1 Design targets

| Target | v1 goal |
|--------|---------|
| **Tutorial → Rank 3** | ~8 min |
| **Lumina R10** (Solara unlock) | ~60–90 min engaged solo |
| **First cross-bred (C1)** | ~15–25 min post-tutorial |
| **First meteor crate** | ~20–40 min *(night)* |
| **Glimmer unlock (Solara R15)** | ~3–6 hr engaged |
| **Daily session** | 20–40 min feels complete *(triad + 2–3 deliveries + 1 splice)* |

**Principles:** generous F2P floor; no hard currency walls on breeds; coins sink into upgrades faster than earn after mid-game; Stardust gates nursery power; Comet Shards gate event flair.

---

### 5.2 Growth & harvest timing

| Affinity | Passive grow *(correct phase)* | Wrong phase multiplier | Ripe → re-grow |
|----------|----------------------------------|------------------------|----------------|
| **Moonbound** | **8 min** | ×0.4 | Instant replant after harvest |
| **Sunbound** | **8 min** | ×0.4 | Instant replant |
| **Twilight** | **12 min** | ×0.6 *(either phase)* | Instant replant |
| **Cross-bred** *(default)* | Inherits parent avg | — | Instant replant |

| Modifier | Effect |
|----------|--------|
| **Active nurture** *(correct phase)* | **−20%** remaining grow time; **90s cooldown** per plot |
| **Moonloam / Sunpeat soil** | **+10% / +10%** grow speed *(matching affinity)* |
| **Buff decor** *(max 3 types)* | +3–5% per piece; caps in §1.8 |
| **Tutorial / one-time accel** | Fixed **60s** first harvest; **instant** first splice reveal |

**Harvest yield (base):** **3–5** bloom fruit + **1** pollen unit per mature plant. **Stardust:** **1** per harvest, **+1** if mutated fruit.

**Offline *(Q61)*:** growth continues; each plot stores **1** ripe harvest at base, **2** with offline-storage upgrade tier 1.

---

### 5.3 Orbital Outpost — delivery economy

#### Payout formula

```
coins = floor(baseCoins(planet, round) × planetMult × (1 + keeperBonusByRank[rank]))
lifeforms = floor(baseLifeforms(planet, round) × planetMult)
```

`keeperBonusByRank` = `{ R1 = 0.00, R2 = 0.05, R3 = 0.10, R4 = 0.15, R5 = 0.25 }`. Rank 5 intentionally jumps to +25% as the capstone reward.

| Planet | `planetMult` | Notes |
|--------|--------------|-------|
| **Lumina** | 1.0 | Tutorial planet |
| **Solara** | 1.35 | Requires cross-bred prep |
| **Glimmer** | 1.7 | Twilight stockpiling |

#### Lumina manifest scaling *(rounds 1–15+)*

| Round | Glow Berry | Moon Melon | Nebula Pod | Base coins | Base lifeforms |
|-------|------------|------------|------------|------------|----------------|
| 1 | 10 | — | — | 150 | 12 |
| 2 | 15 | 8 | — | 280 | 28 |
| 3 | 20 | 12 | 5 | 420 | 45 |
| 5 | 28 | 18 | 10 | 650 | 80 |
| 10 | 45 | 35 | 22 | 1,200 | 200 |
| 15 | 60 | 48 | 30 | 1,800 | 350 |

**Round 16+:** each fruit line += **+3 / +2 / +1** per round respectively; coins += **+85**, lifeforms += **+18**.

#### Solara & Glimmer manifest scaling

Same structure as Lumina with **planet fruit names swapped** and quantities × **1.15 / ×1.3** per round tier respectively.

**Cross-bred fruit lines** may appear from **Round 4+** on any planet *(max 1 line per manifest)* — quantities **50%** of lowest planet-fruit line that round.

#### Bonus drops *(personal delivery)*

| Round milestone | Bonus |
|-----------------|-------|
| Every **5th** round per planet | **+5 Stardust** |
| Every **10th** round | **+1 Spin Token** *(50% chance)* |
| First delivery to **new planet** | **+200 coins** one-time |

---

### 5.4 Cosmic Coin sinks *(launch catalog)*

#### Seed Stand

| Seed | Cost | Unlock |
|------|------|--------|
| **Glow Mote** | 80 | Always |
| **Moon Melon** | 100 | Always |
| **Nebula Sprout** | 120 | Always *(also tutorial grant after first delivery)* |

*No sunbound / twilight seeds at Broker.*

#### Garden & nursery upgrades

| Upgrade | Tier | Cost | Gate |
|---------|------|------|------|
| **Second plot row** (+4 plots) | — | **1,200** coins | **3 Bloomdex stars** |
| **Nebula Ridge** extension | — | **1,800** coins + **40** Stardust | **6 Bloomdex stars** |
| **Offline storage** (+1 buffer/plot) | 1 | **500** coins | Rank 2 |
| **Offline storage** | 2 | **900** coins | Rank 4 |
| **Nursery splice slot** | 2 | **800** coins + **20** Stardust | Rank 3 |
| **Nursery splice slot** | 3 | **2,500** coins + **60** Stardust | **12 Bloomdex stars** |
| **Nursery speed** | 2 | **600** coins + **15** Stardust | Rank 2 |
| **Nursery speed** | 3 | **2,000** coins + **50** Stardust | Rank 4 |
| **Splice luck** | 2 | **700** coins + **25** Stardust | First cross-breed |
| **Splice luck** | 3 | **2,200** coins + **70** Stardust | **8 Bloomdex stars** |
| **Moonloam soil** *(1 plot)* | — | **400** coins | — |
| **Sunpeat soil** *(1 plot)* | — | **400** coins | Solara unlock |
| **Twilight mix soil** | — | **900** coins + **20** Stardust | Glimmer unlock |
| **Display case polish** | — | **300** coins | Per case unlock |

#### Tools *(one-time)*

| Tool | Cost |
|------|------|
| **Moon Lantern** *(active nurture)* | 250 | Tutorial |
| **Sun Scope** | 250 | First sunbound seed or Lumina **R5** |
| **Twilight Lantern** | 350 | First twilight seed or Solara unlock |
| **Pollen basket** *(+swab radius)* | 350 | Rank 3 |

**Mid-game coin pressure:** by Lumina **R8**, cumulative upgrade spend ≈ **8,000–10,000** coins if pursuing nursery T2 + second row — earn rate ≈ **900–1,100/hr** engaged solo *(matches ~90 min to R10)*.

---

### 5.5 Stellar Nursery — splice resolution *(server)*

**Input validation:** server checks pollen types, nursery tier, player ownership; one session per slot.

#### Outcome roll *(pair in §1.2b matrix)*

| Nursery tier | Primary seed *(matrix match)* | Duplicate pollen | Mutation *(any eligible)* | Prize Bloom *(C12 only)* |
|--------------|------------------------------|------------------|---------------------------|------------------------|
| **1** | 70% | 25% | 5% | — |
| **2** | 74% | 20% | 6% | — |
| **3** | 78% | 15% | 6% | 1% |

**Pair NOT in matrix:** **0%** seed; **88 / 10 / 2%** duplicate / mutation / nothing at T1.

**Wait times *(Q64)*:** T1 **180s** → T2 **120s** → T3 **60s** real time; offline continues.

**Mutation sub-roll:** when mutation wins, **60%** harvest mutation *(grow RNG)* / **40%** splice mutation on parent A breed.

---

### 5.6 Mutations & discovery RNG

| Source | Base mutation chance | Notes |
|--------|---------------------|-------|
| **Harvest** *(mature plant)* | **2%** per harvest | Per breed; pity **+1%** per 20 non-mutated harvests *(cap +5%)* |
| **Splice** | See §5.5 | Can discover off-map mutations |
| **Event pollen** *(meteor)* | **8%** on next harvest | Consumes event pollen buff |

**Signature map mutations** use same rolls but are **flagged** when first discovered — lights map star if signature.

---

### 5.7 Community Feed scaling

**Server goal pool:**

```
goalFruit = min(cap, floor + (750 × activePlayers))
```

| Server type | `floor` | `cap` | `activePlayers` | Notes |
|-------------|---------|-------|-----------------|-------|
| **Public** | 4,000 | 14,000 | 1–12 | Standard hub; 12-player target = 13,000 fruit |
| **Private / VIP** *(Q74)* | **2,500** | **8,000** | 1–6 *(owner + invites)* | Lower server goal for 2–4 friends |

Split **60 / 30 / 10** across theme fruit lines *(Lumina example: Glow / Moon / Nebula)*.

**Personal tiers** *(rewards identical; thresholds do **not** scale by server type unless playtest proves small-group private feeds need it):*

| Tier | Personal threshold | Reward |
|------|--------------------|--------|
| 1 | 25+ fruit | **120** coins + **3** Stardust |
| 2 | 100+ | **+1** Comet Shard |
| 3 | 500+ | **+1** Spin Token + **15%** forward seed roll |

*Meteor showers, Cosmic Spin, and planet deliveries work identically — private servers just feel quieter and cozier.*

#### Private server fairness *(Q74 — anti-exploit policy)*

Private meadows are a **social comfort** SKU *(no strangers)*, **not** a hidden difficulty toggle for the whole game.

| System | Public vs private |
|--------|-------------------|
| Plant grow timers | **Same** |
| Nurture tool cooldowns | **Same** *(Infinite Nurture pass is a separate game pass)* |
| Stellar Nursery splice queue / luck | **Same** |
| Orbital Outpost delivery coin payouts | **Same** |
| Bloomdex / planet rank gates | **Same** |
| Meteor shower cadence & crate odds | **Same** |
| Cosmic Spin odds & reward table | **Same** |
| Community Feed **tier rewards** *(coins, shards, tokens)* | **Same** |
| Community Feed **personal thresholds** | **Same** *(v1 default; protects Feed rewards from VIP efficiency)* |
| Community Feed **server goal pool** | **Lower on private** *(2,500 floor / 8,000 cap)* |

**Why this is balanced:** Fruit still grows at the same rate on the same plots. The **server goal** scales down so **2–4 friends** can clear the shared bar without needing 12 strangers; personal reward thresholds stay the same so VIP servers do not become a faster Spin Token / Comet Shard farm. This is **not** equivalent to Bloom Rush or Cosmic Coin packs.

**Implementation:** Server reads `PrivateServerId`; **only** §5.7 formulas branch. No other gameplay multipliers on VIP instances.

**Server clear:** **+1** Spin Token, **+3** Comet Shards, **10 min +10% Outpost coins** for all contributors.

**Cadence *(Q65)*:** ~**30 min**; Lumina theme ~every **90 min** on 3-feed loop.

---

### 5.8 Comet Shards & Meteor Merchant

#### Earn sources

| Source | Shards |
|--------|--------|
| **Meteor crate** *(guaranteed personal)* | **8–18** |
| **Community Feed** tier 2+ | **+1** |
| **Achievement tier** | **5–20** bundles |

#### Meteor crate loot table

| Roll | Weight | Contents |
|------|--------|----------|
| Common | 70% | Shards only |
| Uncommon | 22% | Shards + **80** coins |
| Rare | 6% | Shards + **forward seed** *(Flare Mint, sunbound base, or Tier B cross seed)* |
| Epic | 2% | Shards + **1** Spin Token |

**Forward seed pity:** if **5** consecutive showers without rare+, next crate **guarantees** forward seed.

#### Weekly Meteor Merchant rotation *(3 slots)*

| Slot | Example SKU | Cost |
|------|-------------|------|
| **A — Event seed** | Flare Mint, random sunbound base | **50–70** shards |
| **B — Decor** | Meteor lantern, glow fence | **25–40** shards |
| **C — Forward vial** | Specific **pollen vial** *(one cross-bred tier)* | **55–65** shards |

Rotation resets **Monday 00:00 UTC**; same catalog all servers that week.

---

### 5.9 Spin Token & Cosmic Spin economy

| Source | Rate |
|--------|------|
| **Free daily spin** | 1 / account / rolling 24h |
| **Community Feed** tier 3 | 1 |
| **Meteor epic roll** | 1 |
| **Planet R10 / R15 first time** | 2 / 3 |
| **Keeper Daily Trio** *(R4–5)* | 1 |
| **First discoverer** | 3 |

**Spin payout tiers *(non-legendary)*:** coins **50–400**, Stardust **2–10**, Comet Shard bundle **5%**, duplicate pollen **15%**.

**Legendary pool *(Q66)*:** 7/week; snapshot odds **0.8%** per spin at board start; duplicate copies OK *(Q59)*.

---

### 5.10 Co-op & trade boundaries *(v1 lock)*

| Rule | v1 |
|------|-----|
| **Shared plots** | **No** |
| **P2P trading** | **No** |
| **Co-op harvest** | **No** |
| **Server events** | Meteors, Community Feed, Cosmic Spin — shared space, personal rewards |
| **Private server scaling** | **Community Feed server goal only** *(§5.7)* — all timers, personal thresholds, payouts, and gates identical to public |
| **Social pollen** | **3 swabs/day** — player-initiated |

*Optional 2P co-op deferred post-launch; economy assumes solo earn paths for all breeds (§1.2b forward paths).*

---

### 5.11 Economy tuning checklist *(playtest)*

- [ ] Lumina R10 still ~60–90 min after fruit yield tweaks
- [ ] Tier B cross **C4–C7** reachable before Solara R10 without meteor luck
- [ ] Coin sink vs earn not stalling nursery T2
- [ ] Stardust earn/sink curve still gates nursery T2/T3 after Bloom Rush, Infinite Nurture, and Extra Garden Beds are considered
- [ ] Spin Token weekly faucet does not exceed target after Feed tier 3, server clear, meteors, first discoverer, milestones, and Daily Trio are combined
- [ ] Community Feed clear rate **40–70%** per window at 6+ public actives and **40–70%** at 2–4 private actives
- [ ] Forward seed pity not flooding twilight before Glimmer gate

*Spreadsheet clone: Producer to attach `economy-v1` sheet in Phase 09 if needed.*

---

## 6. Monetization *(Step 3 — economy/monetization designer, 2026-06-28)*

**Model:** Dual currency — **Cosmic Coins** (earn) + **Robux** (convenience + cosmetic shortcut). **No paid random at launch** *(Q56, Phase 02 Cozy Fair)*.

*v1 price points are **targets** — conversion and retention tune in Phase 12 playtest.*

### 6.1 Hard excludes *(all Robux paths)*

Spin Tokens · Cosmic Spin pulls · random seed packs · paid splice luck · Robux Comet Shards · exclusive breeds/biomes · P2P · legendary direct purchase · Robux crop steal

### 6.2 Earn-rate anchor *(from §5)*

| Metric | v1 target |
|--------|-----------|
| **Engaged solo earn** | **~900–1,100 Cosmic Coins / hr** *(Lumina deliveries + 4 plots)* |
| **First major sink** | Second plot row **1,200** ≈ **~70–80 min** organic |
| **Nursery T2** | **800** coins ≈ **~45–55 min** organic |
| **Session length** | **20–40 min** “feels complete” |

**Robux rule:** every paid SKU must map to a **deterministic** earn path or **time saved** — never exclusive power.

### 6.0 Robux catalog *(v1 launch — master list)*

| Item | Price | Type | Purpose |
|------|-------|------|---------|
| **Meadow Express** | 99 R$ | Game pass | Fast-travel between your garden and the hub — saves walk time during deliveries, feeds, and meteors. |
| **Infinite Nurture** | 149 R$ | Game pass | Removes the **90s cooldown** on **Moon Lantern, Sun Scope, and Twilight Lantern** — still requires the **correct grow phase** for each plant. |
| **Extra Garden Beds (+2)** | 249 R$ | Game pass | **+2 permanent plant plots** on your meadow *(stacks with coin-unlocked rows)* — more crops at once. |
| **Bloom Rush 1h** | 49 R$ | Dev product | Advances **one selected crop’s** grow timer by **60 minutes** — deterministic; plots only. |
| **Bloom Rush 4h** | 149 R$ | Dev product | Same, **4 hours** on one crop. |
| **Bloom Rush 8h** | 249 R$ | Dev product | Same, **8 hours** on one crop. |
| **Cosmic Coin Pouch** | 99 R$ | Dev product | **1,000 Cosmic Coins** — shortcut for upgrades/seeds; ~1 hr organic earn. |
| **Cosmic Coin Satchel** | 249 R$ | Dev product | **2,800 Cosmic Coins** — mid-game sinks *(nursery, rows)*. |
| **Cosmic Coin Vault** | 499 R$ | Dev product | **6,500 Cosmic Coins** — large upgrade push; not required for progression. |
| **Meadow Starter Kit** | 199 R$ | Dev product *(once)* | One-time bundle: **600 coins**, **15 Stardust**, **Glow Mote** seed, **Starter Lantern** cosmetic skin — offered first **72h** after tutorial. |
| **Tool skins** | 49–79 R$ | Cosmetic | Visual reskins for nurture tools — **no stats**; earn path via coins. |
| **Nursery exteriors** | 149–199 R$ | Cosmetic | Stellar Nursery façade variants — **no stats**; earn via coins or Comet Shards. |
| **Display plaques** | 29–49 R$ | Cosmetic | Case nameplate styles — earn path via coins. |
| **Keeper hat / avatar flair** | 79 R$ | Cosmetic | Meadow/hub expression — earn via coins. |
| **Hub emotes** | 49 R$ | Cosmetic | Social emotes at Outpost — some earn-only from Community Feed. |
| **Private meadow** | **100 R$** / mo | VIP server | **Invite-only server** — play with friends & family, no strangers. Same game; smaller shared Community Feed goal for small groups *(§5.7)*. |

**Not sold for Robux at launch:** Spin Tokens · Cosmic Spin pulls · seeds *(random)* · splice luck · Comet Shards · breeds · biomes · legendaries · P2P trades.

**Post-launch *(not v1 vertical slice)*:** Deterministic season pass cosmetics.

---

### 6.3 Game passes *(3 at launch — final v1 prices)*

| Pass | Price | Value | Organic equivalent |
|------|-------|-------|------------------|
| **Infinite Nurture** | **149 R$** | Removes **90s active nurture cooldown** on **all three** nurture tools | Wait cooldowns free; still need correct phase |
| **Extra Garden Beds (+2)** | **249 R$** | **+2 permanent plant plots** *(stacks with row upgrades)* | Save **~1,200+** coins toward other sinks; not a substitute for Bloomdex-gated **+4 row** |
| **Meadow Express** | **99 R$** | **Fast-travel** garden ↔ hub *(~2s load, no walk)* | Walk / run everywhere |

**Implementation:** `MarketplaceService:UserOwnsGamePassAsync` on server before applying buffs. **+2 plots** granted once on first join after purchase. Playtest must confirm this pass does not create a runaway advantage in Stardust, mutation rolls, or Community Feed tier access.

**Value framing *(store copy)*:**

- *Infinite Nurture* — “Nurture every plot on your schedule — moon, sun, or twilight.”
- *Extra Garden Beds (+2)* — “Two extra beds from day one — same seeds, same gates.”
- *Meadow Express* — “Hop to the Outpost when the feed bell rings.”

---

### 6.3b Private meadows *(VIP servers — Q74, v1 launch)*

| Field | Value |
|-------|-------|
| **Price** | **100 R$** / month *(Roblox VIP server subscription — tune at launch)* |
| **Purpose** | **Invite-only meadow** for friends & family — **no strangers**. Warm, cozy, parent-friendly. |
| **Game rules** | Identical to public servers — own gardens, same breeds, earn-only spins |
| **Scaled co-op** | Community Feed **lower server goal** *(§5.7)* so 2–4 friends can clear the shared bar |
| **Not included** | **No** faster growth, deliveries, spins, or gates — see §5.7 private-server fairness |
| **Implementation** | Enable **VIP Servers** on experience; server detects `PrivateServerId` for Feed scaling only |
| **UX copy** | *“Your own cozy meadow — invite who you want.”* · *“Same growth and rewards; cozier table goals.”* |

*Not paywalled progression — optional social comfort layer.*

---

### 6.4 Developer products *(deterministic)*

#### Cosmic Coin packs

| SKU | Robux | Coins | ≈ Organic time saved* |
|-----|-------|-------|------------------------|
| **Cosmic Coin Pouch** | **99 R$** | **1,000** | ~1 hr |
| **Cosmic Coin Satchel** | **249 R$** | **2,800** | ~2.5 hr *(~12% bonus)* |
| **Cosmic Coin Vault** | **499 R$** | **6,500** | ~6 hr *(~18% bonus)* |

*At mid-game earn rate; not a progression skip — coins still spent on the same sinks and cannot bypass Stardust, Bloomdex, planet gates, or unlock requirements.*

**Cap:** max **3 Coin pack purchases / 7 days / account** *(anti-whale inflation; tune in live ops)*.

#### Bloom Rush *(single-plant growth advance — not random)*

| SKU | Robux | Effect |
|-----|-------|--------|
| **Bloom Rush 1h** | **49 R$** | Advance **one selected planted crop** by **60 min** grow time |
| **Bloom Rush 4h** | **149 R$** | Advance **one selected crop** by **240 min** |
| **Bloom Rush 8h** | **249 R$** | Advance **one selected crop** by **480 min** |

**Rules:**

- Cannot target **Stellar Nursery splice queue** — plots only
- Cannot bypass **planet unlock**, **Bloomdex gates**, Stardust costs, or nursery queue rules
- Offline buffer rules unchanged *(§5.2)*
- Prompt copy: *“Help this plant along — everything else still grows while you play.”*

#### Starter kit *(one-time, 72h from first join)*

| **Meadow Starter Kit** | **199 R$** |
|------------------------|------------|
| **600** Cosmic Coins | |
| **15** Stardust | |
| **1×** deterministic **Glow Mote** seed *(not random)* | |
| **1×** cosmetic **Starter Lantern** skin *(Moon lantern reskin, zero stats)* | |

*Shown once after tutorial complete; never repeats. Earn path: same items obtainable organically in early play. Copy must say “optional starter shortcut,” never “limited-time power.”*

**Excluded at launch:** random seed packs, gacha, Robux spin wheels, paid cross-breed rolls.

---

### 6.5 Cosmetics *(dual price — Robux shortcut + earn path)*

**Rule:** **Zero gameplay stats** on any cosmetic. Every launch cosmetic has **Cosmic Coins** or **Comet Shards** price.

| Category | Robux | Earn path | Example |
|----------|-------|-----------|---------|
| **Tool skin** | **49–79 R$** | **800–1,200** coins | Moon lantern *Nebula Print* |
| **Nursery exterior** | **149–199 R$** | **3,500** coins or **45** shards | *Observatory Glass* façade |
| **Display plaque** | **29–49 R$** | **400** coins | Silver nameplate |
| **Keeper hat / emote** | **79 R$** | **1,500** coins | *Constellation Cap* |
| **Hub emote** | **49 R$** | **Community Feed tier 3** *(one season)* | *Capsule Cheer* |

**Rotation:** **4–6** new earnables / month live ops; **2** Robux-only **variants** of same mesh *(tint only)* always paired with earnable base.

---

### 6.6 Friction prompts & store UX

**When to offer** *(max 1 prompt / 10 min session)*:

| Trigger | Offer |
|---------|-------|
| Active nurture on **cooldown** *(3rd+ use in 10 min)* | Infinite Nurture |
| **All plots full** + player has seed in hand | Extra Garden Beds (+2) **or** Coin pack |
| Walk **>12s** to hub with ripe fruit notification | Meadow Express |
| Crop **>75%** grown + player opens shop | Bloom Rush 1h |

**Never prompt on:** first session tutorial · Community Feed · Cosmic Spin animation · first meteor shower.

**Store layout:** **Passes** tab → **Bloom Rush** → **Coin packs** → **Cosmetics**. No loot-box iconography.

---

### 6.7 Compliance & fairness checklist

| Requirement | Status |
|-------------|--------|
| No paid random outcomes | ✅ |
| Spin Tokens / legendaries earn-only | ✅ |
| Odds disclosure for **Cosmic Spin** *(earn board)* | Public board shows tier weights; legendary snapshot % on interact |
| Parental / all-ages copy | No “buy power” — “save time” / “look great” |
| Regional pricing | Roblox dynamic pricing on all SKUs |
| Refund policy | Standard Roblox marketplace |

**Cosmic Spin disclosure *(earn-only)*:** hub board UI shows non-legendary tier table + current legendary name & snapshot odds *(e.g. 0.8%)* before spin confirm.

#### 6.7b Parent-facing summary

- **Robux buys convenience or looks:** faster travel, one-plant Bloom Rush, coin shortcuts, cosmetics, and optional invite-only Private Meadow.
- **Robux does not buy random spins, exclusive breeds, Comet Shards, Spin Tokens, planet unlocks, Bloomdex gates, or nursery luck.**
- **Private Meadow** is for comfort and friend/family play: same growth, same payouts, same odds; only the shared Community Feed server goal is smaller for small groups.

---

### 6.8 Live ops monetization *(post-launch)*

| Feature | Model |
|---------|-------|
| **Constellation Season** | Free track + **deterministic** premium cosmetics *(no random)* |
| **Meteor / Feed drops** | Earn-only |

*Expand pass catalog only after Phase 12 retention data (max +1 pass / quarter).*

---

## 7. Social & visit flows *(Step 4 — UX designer, 2026-06-28)*

### 7.1 Design principles

| Principle | Application |
|-----------|-------------|
| **Solo-safe** | No required social interaction to progress |
| **Visit = read-only flex** | Visitors see stats & trophies; cannot edit or steal |
| **One-tap social** | Pollen swab, emote, leaderboard peek — low friction |
| **Cozy not competitive** | Visit board celebrates growth; no “rank shaming” on plots |

---

### 7.2 Visit-stats board *(at each player’s garden)*

**Placement:** Physical **sign post** at plot entrance — interact or auto-glance when entering own garden.

**Layout *(mobile-first, single column)*:**

```
┌─────────────────────────────┐
│  @PlayerName's Meadow       │
│  Keeper Rank ★★★☆☆         │
├─────────────────────────────┤
│  Planet Friends     12,450 │
│  Supply Runs              87 │
│  Highest Round      Lumina R42│
│  Biggest Bloom        14.2m │
├─────────────────────────────┤
│  Bloomdex  8/21 stars · 18 discoveries │
│  Planets   Lumina · Solara · — │
│  Display Cases  2/3 filled   │
└─────────────────────────────┘
```

| Field | Source stat | Visitor sees? |
|-------|-------------|---------------|
| Planet Friends Fed | Cumulative Outpost | ✅ |
| Supply Runs | Capsule count | ✅ |
| Highest Round | Best round any planet | ✅ |
| Biggest Bloom | Max plant height record | ✅ |
| Bloomdex stars | Map progress **X/21** | ✅ |
| Discoveries | Full index count | ✅ |
| Planets unlocked | Names + lock icons | ✅ |
| Display cases | Count + Prize Bloom names | ✅ *(3D case visible nearby)* |
| Keeper Rank | 1–5 stars | ✅ |

**Own garden:** **Edit plaque** *(cosmetic, 400 coins)* · **Privacy** toggle *(v1): Public / Friends only / Private*. Default for under-13-friendly positioning: **Friends only** on public servers, visible to invitees in Private Meadows.

---

### 7.3 Visiting another player’s garden

**Flow:**

1. Walk into another player’s **plot bounds** *(nameplate above gate)*  
2. **Visit-stats board** auto-highlights *(optional toast: “Visiting @friend”)*  
3. Walk plots — see **mature plants**, **decor**, **display cases** *(read-only)*  
4. **Pollen swab** — see §7.4  
5. **Post-MVP:** look up at **night sky collections** above plot  

**No:** harvesting, decor edit, nursery access, inventory peek, or reducing the owner’s resources.

**Empty/offline garden:** board still readable; plants show offline growth state; toast *“Gardener is away — plants still growing.”*

---

### 7.4 Pollen swab interaction

**Trigger:** Proximity to **mature foreign plant** + **Pollen basket** equipped *(or default hand tool after tutorial)*.

```
[Mobile]  Tap plant → radial: [ Swab Pollen (2/3 today) ]
[Desktop] E on plant → same prompt
```

| Feedback | Detail |
|----------|--------|
| **Success** | Sparkle + *“+1 Moon Melon pollen — nothing taken from this garden”* · daily counter updates |
| **Already swabbed this plant** | *“You already sampled this plant today.”* |
| **Daily cap** | *“Come back tomorrow for more swabs (3/day).”* |
| **Owner benefit** | None — no notification spam *(optional subtle “Someone admired your bloom” — off by default v1)* |

**Swab budget HUD:** persistent chip **`Friendly samples: 2/3`** near inventory when basket equipped.

---

### 7.5 Display cases *(visitor view)*

- Case **plaque** shows breed/mutation name + discover date  
- **Inspect** opens read-only Bloomdex card *(art, lore snippet)*  
- Empty case: *“Awaiting a Prize Bloom”*

---

### 7.6 Hub social presence

| Element | Behavior |
|---------|----------|
| **Player nametags** | Above avatar in hub + garden gates |
| **Cosmic Spin banner** | *“@name is spinning…”* *(§1.11)* |
| **Community Table bar** | Shared world UI — see §8.5 |
| **Leaderboard kiosk** | Interact → full-screen board pager *(§1.12)* |
| **Private server badge** | Small **“Invite meadow”** chip in corner for VIP instances |

**Friends:** Roblox native party/follow — no custom friend list v1.

---

### 7.7 Trust & Safety baseline *(v1)*

| Surface | v1 policy |
|---------|-----------|
| **Custom text** | None in v1 beyond Roblox-native display names and system-generated messages |
| **Chat** | Use Roblox platform chat / filtering only; no custom chat surface |
| **Reports / blocks** | Respect Roblox native reporting and blocking; blocked users should not receive custom follow prompts or swab encouragement |
| **Public recognition** | System UI toasts only; keep first-discoverer and Legendary messages short, positive, and non-repeat-spammy |
| **Visit privacy** | Visit board defaults to Friends only on public servers; player can set Public / Friends only / Private |
| **Pollen swabs** | Friendly sample copy must state no fruit, pollen, or progress is removed from the owner |
| **Community Feed pressure** | Always show next eligible Lumina window; avoid guilt copy and “hurry or lose” language |
| **Private Meadow** | Marketed as invite-only comfort, not progression advantage |

---

## 8. UX flows *(Step 4 — UX designer, 2026-06-28)*

### 8.0 Global shell & navigation

#### Persistent HUD *(own garden + hub)*

```
[Top-left]  Day/Night arc · phase icon (☀/☽)
[Top-right] Cosmic Coins · Stardust · Comet Shards (icons + tap to expand)
[Bottom]    Tool belt: Lantern / Scope / Twilight / Basket (context gray-out)
[Bottom-R]  Bloomdex · Inventory · Keeper (dailies) — 3 icon buttons
[Center]    Objective pin when Keeper beat/daily active (waypoint arrow)
```

**Hub ↔ garden:** walk, or **Meadow Express** teleport pad *(pass)* at garden gate.

**Notifications *(non-blocking toasts, max 1 at a time)*:**

- *“Community Feed starting — Lumina Luncheon!”*
- *“Meteor shower in 30s!”*
- *“Crop ready: Moon Melon”*

---

### 8.1 Bloomdex UI

**Open:** HUD **Bloomdex** button or **B** *(desktop)*.

**Two tabs:**

| Tab | Content |
|-----|---------|
| **Collections** | Little Slipper · Sun Rawr · Silver Weaver — **literal shape** star maps |
| **Index** | Alphabetical/all breeds — grayscale locked entries |

#### Collection star map

- **Pan/zoom** silhouette; stars **pulse** if criteria completable now  
- **Hover/tap star** → tooltip: *“Grow a Moon Melon”* / *“Discover Shimmer Glow Berry”*  
- **Lit star** → tap opens **entry card** *(art, affinity, fruit, lore)*  
- **Progress footer:** *Little Slipper 4/6* · reward preview on complete  

#### Index entry card

- Base breed + **mutations sub-list** *(≥3)* — signature mutations badged ★  
- **First discoverer** frame if applicable *(per-server)*  
- **Actions:** *Track* *(pins grow hint to HUD)* · *View in nursery* if pollen owned  

**Mobile:** full-screen modal; **44×44pt** min tap targets on stars.

---

### 8.2 Orbital Outpost — planet delivery UI

**Interact:** **Supply Console** at Outpost.

**Screen 1 — Planet picker**

```
[ Lumina ✓ R12 ]  [ Solara ✓ R5 ]  [ Glimmer 🔒 Solara R15 ]
```

- Locked planets show **requirement** + gray fruit icons  
- Tap planet → **Screen 2**

**Screen 2 — Planet order**

```
Lumina — Round 12
─────────────────────────
  Glow Berry     42 / 45  [████████░]
  Moon Melon     30 / 30  ✓
  Nebula Pod     12 / 15  [██████░░░]
─────────────────────────
[ Load Capsule ]  (disabled until all ✓)
```

- Pulls from **inventory** automatically on Load — no manual drag v1  
- **Insufficient:** red line + *“Need 3 more Nebula Pod — grow or harvest”*  
- **Success:** capsule launch cinematic → coin popup → **Round 13** preview teaser  

**Keeper bonus** shown inline: *“+15% Keeper Rank → +63 coins”*.

---

### 8.3 Stellar Nursery — splice UI

**Interact:** nursery **Splice Bench** *(slot count = tier)*.

**Flow:**

1. **Slot A** — pick pollen from inventory *(filtered list)*  
2. **Slot B** — pick second pollen  
3. **Preview:** *“Possible: Starlace Vine (C1)”* if known pair; else *“Unknown cross — discovery chance!”*  
4. **Start Splice** — **180s** timer *(tier 1)*; offline continues  
5. **Reveal screen:** seed/mutation/duplicate/Prize Bloom + Bloomdex new-entry fanfare if first time

**Queue:** tier 2–3 = parallel slots shown as **side-by-side benches**.

**Tutorial accel:** first splice shows **fast-forward** button once.

---

### 8.4 Inventory & harvest

**Inventory grid:** fruits · pollen vials · seeds · tokens — **tabs** to reduce scroll.

**Harvest:** tap ripe plot → **Hold to harvest** *(0.5s)* or quick-tap if setting enabled in accessibility.

**Quick-deliver shortcut *(post-tutorial)*:** from inventory fruit stack → *“Deliver to Outpost”* sets waypoint *(does not auto-walk)*.

---

### 8.5 Community Feed UI

**World element:** **Community Table** beside Outpost — always visible; **inactive** between windows.

**Active window *(12 min)*:**

```
┌─ Community Feed: Solara Supper ─────────┐
│  SERVER ████████████░░░░  78%          │
│  Sun Peach line (you: 12 / tier1: 25)  │
│  [ Contribute Fruit ▼ ]                 │
│  Your tiers: ✓1  ✓2  ○3               │
└─────────────────────────────────────────┘
```

- **Contribute:** opens inventory filtered to **eligible fruit only**  
- **Reject ineligible:** *“This table needs sunfruit. Lumina Luncheon returns soon.”*
- **Tier pips** update live; **server clear** confetti + toast  

**Inactive / ineligible state:** show next eligible Lumina window and a grow hint, e.g. *“Solara Supper needs sunfruit. Grow tips: unlock Solara seeds, or bring moonfruit when Lumina Luncheon returns in ~32m.”*

**Private server:** same UI and personal thresholds; lower shared server goal *(§5.7)* — show *“Cozy meadow goal”* subtitle.

---

### 8.6 Cosmic Spin board UI

**Interact:** physical wheel at hub plaza.

**Pre-spin panel:**

```
Current Legendary: Nebula Glow Lantern (0.8%)
[ Free daily spin available ]  or  [ Use Spin Token (3) ]
Tier odds ▼ (expand table)
[ SPIN ]
Recent: @a won Rare · @b won Coins ...
```

- **Spin in progress:** wheel anim **6–8s**; board banner adds your name  
- **Result modal:** tier-colored reveal; **Legendary** = full-screen + server chat  
- **Concurrent spins:** queue position not shown — independent sessions  

---

### 8.7 Merchant UIs

| Merchant | UI pattern |
|----------|------------|
| **Seed Stand** | 3-column seed cards · coin price · *“Owned: 2”* · buy ×1/×5 |
| **Meteor Merchant** | Weekly rotation countdown · **shard prices only** · sold-out gray |
| **Upgrade kiosk** *(garden/nursery)* | Tree of upgrades · red = unmet gate · green = affordable |

---

### 8.8 Keeper — story beats & Daily Trio

**Keeper interact** at hub → **two tabs:**

| Tab | Content |
|-----|---------|
| **Story** | 5 beats checklist · turn-in button when complete |
| **Today** | Breed / Deliver / Discover with progress bars · **Daily Trio** chest |

**Daily reset:** rolling 24h per-account timer, shown as *“New Daily Trio in 4h 12m.”*

**Waypoint:** golden trail to objective target *(garden plot, Outpost, nursery)*.

---

### 8.9 Onboarding UX *(implements §2.1)*

- **Forced focus** — dims unrelated HUD until step complete  
- **Skippable** after account flag — single confirm dialog  
- **30s idle** — Keeper whisper + arrow  
- **No store** until Rank 3 / tutorial complete  

---

### 8.10 Accessibility & mobile checklist

| Check | Target |
|-------|--------|
| Min tap target | **44×44 pt** on all primary actions |
| Text size | Body **≥16pt** mobile; planet order numbers **≥20pt** |
| Color-only phase cue | **Icon + text** *(“Night — moon plants growing”)* |
| Red/green colorblind | ✓/✗ icons on planet order lines, not color alone |
| Hold vs tap | **Toggle** for harvest hold in settings |
| Camera | Default **third-person**; pinch zoom plots; reset button |
| Audio cues | Optional chime on harvest ready · feed start · meteor warning |
| Tutorial | Completable **without voiceover** — all steps text + arrows |
| Reduced motion | Toggle to soften spin, meteor, Feed clear, and Bloomdex starburst effects |
| UI scale | 90–125% slider for mobile/tablet comfort |
| Star-map alternative | List view for Bloomdex stars so hover/pan precision is not required |
| Reminder frequency | Setting to reduce Keeper idle pings / objective nudges |

*v1: English only; Roblox locale for numbers/currency.*

---

## 9. Narrative & world *(Step 5 — narrative designer, 2026-06-28)*

### 9.1 Player fantasy

**You are a meadow keeper** on the edge of a quiet galaxy — a neighbor who **grows food for hungry stars**.

| Pillar | Feeling |
|--------|---------|
| **Care** | Your plants matter; deliveries feed real worlds |
| **Wonder** | Night sky, meteors, new breeds feel magical not stressful |
| **Pride** | Bloomdex stars and visit board show gentle mastery |
| **Together** | Hub events are **warm crowds**, not competition |

**One sentence:** *“I tend my little meadow under the stars — and the whole sky eats better because of me.”*

**Not this game:** war, theft, urgency panic, ironic meta humor, Earth astronomy homework.

---

### 9.2 World setting — *The Meadow Ring*

**Where you are:** A **ring of personal garden plots** around a shared **Orbital Outpost** — floating platforms in an endless **starlit meadow**. No domes, no walls. Soft grass, firefly motes, distant nebula paint.

**What’s beyond:** **Three hungry garden-worlds** *(Lumina, Solara, Glimmer)* — each a distant planet of living light that **requests produce** via supply capsules. You never visit them in v1; you **help from home**.

**Time:** Gentle **day/night** cycle — moon plants at night, sun plants by day, twilight plants in between. **Meteors** fall only when the sky is dark.

**Tone keywords:** warm · hushed · hopeful · cozy · kid-safe · sincere

---

### 9.3 Meadow hub layout *(environment story)*

```
                    [ Night sky / meteor streaks ]
    ┌─────────────────────────────────────────────────┐
    │  Garden plots (12 max) ring the hub             │
    │    🌱 🌱 🌱         HUB PLAZA         🌱 🌱 🌱   │
    │         ╭──────────────────────────╮            │
    │         │  Orbital Outpost (center)│            │
    │         │  · Supply console        │            │
    │         │  · Community Table       │            │
    │         │  · Constellation Keeper  │            │
    │         ╰──────────────────────────╯            │
    │   [Cosmic Spin]  [Leaderboards]  [Seed Stand]  │
    │   [Meteor Merchant*]  (*after showers)          │
    │         Stellar Nursery at each player's plot  │
    └─────────────────────────────────────────────────┘
    *Merchant tent spawns ~5 min post-shower
```

| Zone | Story it tells |
|------|----------------|
| **Personal plot** | *Home* — your soil, your cases, your sky |
| **Outpost center** | *Giving* — where harvest becomes help |
| **Spin board plaza** | *Celebration* — whole meadow cheers luck |
| **Community Table** | *Potluck* — everyone brings what they grew |
| **Merchant tent** | *Gift from the sky* — meteors leave surprises |

**Private meadows:** same layout, softer lighting, **“Invite meadow”** banner — *“A little corner of the ring, just for your people.”*

---

### 9.4 Constellation Keeper *(NPC voice)*

**Who:** **Constellation Keeper** — gentle astronomer-gardener in a **star-pattern apron**. Not a quest-giver king; a **neighbor mentor** who remembers every keeper’s first sprout.

**Voice rules:**

| Do | Don’t |
|----|-------|
| Short, warm sentences | Lore dumps |
| Encourage & explain *why* | Sarcasm, pressure |
| “We / the meadow” | “You must grind” |
| Concrete verbs: *grow, feed, mix, share* | IAU star names, Earth sky facts |

**Sample lines *(v1)*:**

| Moment | Line |
|--------|------|
| Tutorial greet | *“Every star needs supper. Let’s grow something kind.”* |
| First harvest | *“Look — your Nebula Pod is ready. The sky can taste that.”* |
| First delivery | *“Twelve little lives on Lumina ate tonight. You did that.”* |
| First splice | *“Two pollens met — and something new whispered yes.”* |
| Release | *“The meadow is yours now. Feed the stars whenever you’re ready.”* |
| Daily Trio | *“Three small kindnesses today — breed, deliver, discover.”* |
| Meteor warning | *“Skies are sparkling — gifts are falling. Gentle run!”* |
| Feed start | *“Community Table’s open. Bring what you’ve grown.”* |

**Story beat turn-ins:** Keeper **claps once**, small star burst — no lengthy cutscenes.

---

### 9.5 Hungry planets *(lore capsules)*

| Planet | Personality | Feed line *(Outpost)* | Unlock whisper |
|--------|-------------|----------------------|----------------|
| **Lumina** | Soft, moonlit world of **glow-dwellers** | *“Lumina’s table is open for moonfruit.”* | *(start)* |
| **Solara** | Bright, **sun-happy** valleys | *“Solara’s orchards are calling for daylight harvest.”* | *“Solara heard about your meadow. They’re ready for sunfruit.”* |
| **Glimmer** | **Twilight** realm between dusk and dream | *“Glimmer’s weavers are setting the table for twilight fruit.”* | *“The weavers of Glimmer are listening. Bring them duskfruit when you can.”* |

**Planet Friends Fed** stat = aggregate of tiny friendly creatures on each planet — never shown starving; always **grateful**.

---

### 9.6 Bloomdex collections *(shape lore)*

| Collection | Shape | Story *(one line)* |
|------------|-------|---------------------|
| **Little Slipper** | Slipper | *Moon gardeners left a **slipper in the sky** — each star a step for night-blooms.* |
| **Sun Rawr** | Lion “rawr” | *A **sleepy sun-lion** yawns across the meadow — brave plants wake him with color.* |
| **Silver Weaver** | Woven arc | *Twilight **weavers** stitch silver threads between day and night; your blooms are their needles.* |

**Prize star — Weaver’s Lantern:** completing Silver Weaver grants a **lantern decor** — *“A weaver’s thank-you for finishing the pattern.”*

**Ban reminder:** never say “Little Dipper,” “Leo,” “Cassiopeia,” or real star maps in player-facing text.

---

### 9.7 Community Feed theme copy

| Theme | Announcement | Table label |
|-------|--------------|--------------|
| **Lumina Luncheon** | *“Lumina Luncheon — moonfruit for everyone!”* | *“Shared table: Lumina”* |
| **Solara Supper** | *“Solara Supper — sunfruit potluck!”* | *“Shared table: Solara”* |
| **Glimmer Gathering** | *“Glimmer Gathering — twilight fruit for the stitchers!”* | *“Shared table: Glimmer”* |

**Server clear:** *“The table is full! The whole meadow ate well tonight.”*

**Private server variant:** *“Your little table is full — cozy work, friends.”*

---

### 9.8 Supporting NPC stubs *(v1 minimal dialogue)*

| NPC | Role | Voice | Sample |
|-----|------|-------|--------|
| **Seed Stand** | Coin seed shop | Cheerful shopkeeper | *“Starter seeds — good roots for kind keepers.”* |
| **Meteor Merchant** | Shard shop | Wandering stargazer | *“Shower gifts! Trade shards, grow something rare.”* |
| **Leaderboard clerk** | Kiosk | Quiet archivist | *“The meadow remembers who fed the most stars.”* |

No voiced lines v1 — **text bubbles** only.

---

### 9.9 Bloomdex entry flavor *(samples — §1.2b)*

| Breed | Lore blurb *(index card)* |
|-------|---------------------------|
| **Glow Mote** | *A shy bush of berry-lanterns. Glows when the moon is kind.* |
| **Nebula Sprout** | *A humble pod, honest star-food. Many keepers grow it after their first Glow Mote.* |
| **Sun Peach** | *Warm as a sunrise hug. Solara’s favorite dessert.* |
| **Flare Mint** | *Too spicy for planet plates — but Community Table cooks love the zing.* |
| **Dusk Lace** | *Petals like lace at the edge of night. Handle with twilight hands.* |
| **Starlace Vine** *(C1)* | *When moonfruit and moonfruit trade pollen, lace grows between them.* |

*Full index: Game Designer + Art Director fill remaining entries in Phase 04 bible.*

---

### 9.10 Event & achievement voice

| System | Copy style |
|--------|------------|
| **Achievements** | Past-tense pride — *“First Delivery,” “Galaxy Gardener”* |
| **First discoverer** | *“@Player was first to meet Starlace Vine on this meadow!”* |
| **Legendary spin** | *“LEGENDARY! @Player caught the Nebula Glow Lantern!”* |
| **Cosmic Spin (small win)** | *“@Player found stardust on the wheel.”* |

---

### 9.11 Narrative exclusions *(v1)*

- No villain faction · no planet in crisis · no timer apocalypse  
- No romance · no player avatar backstory gate  
- No real-world space agency references  
- **Launch Pad** *(post-MVP)* tease only: *“Someday we’ll send seeds *to* the planets, not just fruit.”*

---

## 10. v1 vertical slice acceptance matrix

This matrix is the Producer / QA source for Step 7 GitHub Issues. §1–§9 remain the design source; this section turns scope into testable gates.

| Feature | In v1 slice? | Acceptance criteria | Owner |
|---------|--------------|---------------------|-------|
| First-session tutorial | ✅ | New player completes Glow Mote → Glow Berry → Lumina R1 delivery → C1 splice → Bloomdex star in **≤10 min** with tutorial accel; ends at **Keeper Rank 3**; no Robux prompts | Game Designer / UX / QA |
| Starter garden | ✅ | 4 starter plots; Garden, Stellar Nursery, display-case area, and visit board visible; no shared plots | Lead Engineer / Art |
| Plant growth & nurture | ✅ | Moon / sun / twilight affinities follow §5.2 timing; wrong phase slows but does not kill plants; active nurture respects cooldown / Infinite Nurture rules | Systems / Engineering |
| Inventory & harvest | ✅ | Harvest grants correct bloom fruit, pollen, and Stardust; no generic fruit bucket; server owns grants | Engineering / QA |
| Stellar Nursery tiers 1–2 | ✅ | Tier 1 supports one splice; tier 2 unlock uses §5.4 cost/gate; C1 deterministic tutorial splice works; duplicate/off-table rolls are server-resolved | Systems / Engineering |
| Launch roster | ✅ | 10 base breeds and 12 cross-breds from §1.2b exist in data; renamed entries (**Dreamroot**, **Halo Sprig**, **Glimmer Ivy**, **Weaver Vine**, **Skyknot Bloom**) are reflected in UI | Game Designer / Art |
| Bloomdex star maps | ✅ | 3 collection maps, 21 star slots, tooltips, reward preview, and list-view alternative; full index tracks ≥3 mutations per base but only signature mutations light map stars | UX / Game Designer |
| Mutations | ✅ | At least 3 mutation entries per base in the index; 10 signature mutations flagged for map stars; pity rules in §5.6 testable | Game Designer / Systems |
| Orbital Outpost | ✅ | Planet picker, locked-world requirements, planet order UI, inventory auto-load, capsule launch, round advance, and `keeperBonusByRank` payout formula match §5.3 | Systems / Engineering / QA |
| Planet unlock chain | ✅ | Lumina start; Solara unlocks at Lumina R10; Glimmer unlocks at Solara R15; Launch Pad visible as post-MVP tease only | Game Designer / QA |
| Community Table / Feed | ✅ | ~30 min cadence; Lumina / Solara / Glimmer rotation with Glimmer gate fallback; §5.7 server goals; identical personal thresholds; friendly ineligible copy | Systems / UX / QA |
| Private Meadow | ✅ | Roblox VIP server enabled; invite-only copy present; only Community Feed server goal branches on `PrivateServerId`; growth, payouts, spin odds, gates, and personal thresholds identical | Producer / Engineering / Compliance |
| Meteor shower + Merchant | ✅ | Night shower cadence ~20 min; personal crate claims; 10 min Merchant window; Comet Shard costs and rare pity follow §5.8 | Systems / Engineering |
| Cosmic Spin | ✅ | Server-authoritative RequestSpin / ResolveSpin; rolling 24h free spin; Spin Tokens earn-only; legendary snapshot fairness; duplicate snapshotted winners receive item | Engineering / Security / QA |
| Pollen swabs | ✅ | 3 rolling-24h friendly samples; once per foreign plant per window; no owner resource loss; clear reassurance copy | UX / Engineering / Trust & Safety |
| Visit privacy | ✅ | Visit board supports Public / Friends only / Private; default family posture is Friends only on public servers | UX / Trust & Safety |
| Display cases | ✅ | 3 cases max; one Prize Bloom per case; unlock per planet milestone; read-only inspection for visitors | Game Designer / UX |
| Buff decor | ✅ | 3 active buff-type cap; Pollen Basin, Meteor lantern, Sunstone path, Glow fence examples work without automated collectors | Systems / Art |
| Achievements | ✅ Draft / Step 7 issue | Launch samples in §4 remain valid; Producer issue must either complete the 40-entry target or explicitly reduce v1 achievement scope before implementation | Game Designer / Producer / QA |
| Legendary catalog | ✅ Draft / Step 7 issue | Cosmic Spin supports 7/week rotation; Producer issue must name the 7 launch Legendary decor/skin items before art lock | Game Designer / Art / Economy |
| Monetization | ✅ | No paid random; Extra Garden Beds (+2), Infinite Nurture, Meadow Express, Bloom Rush, coin packs, starter kit, cosmetics follow §6; all server-validated | Economy / Compliance / Engineering |
| Leaderboards | ✅ | Planet Friends Fed, Supply Runs, Highest Round, Biggest Bloom, Meteor Crates; no capped “planets unlocked” board | Producer / Engineering |
| Accessibility | ✅ | Reduced motion, UI scale, harvest tap/hold, audio toggles, camera reset, Bloomdex list view, text+icon phase cues | UX / QA |
| Trust & Safety | ✅ | No P2P trading, no shared plots, no custom text UGC; public recognition uses system UI / filtered system messages only | Compliance / Trust & Safety |
| GitHub Issues | Step 7 | Producer creates one issue per matrix row or grouped milestone, each with acceptance criteria copied from this table | Producer |

### Explicitly out of v1 slice

- Night-sky collection projection above plots
- Launch Pad auto-quests
- P2P trading or shared-plot co-op
- Moth/firefly collectors or automated pollen
- Robux spins, random seed packs, paid splice luck, Robux Comet Shards, exclusive paid breeds/biomes

### Phase 06 implementation addendum outline

Before code bootstrap, create a short engineering addendum covering:

1. Remote contracts and validation checks for plant, harvest, nurture, splice, delivery, Feed, swab, spin, meteor, and marketplace flows.
2. Persistence schema for profile inventory, plots, plant state, Bloomdex, ranks, clocks, purchases, and migration version.
3. Clock policy: rolling 24h for free spin, Daily Trio, and pollen swabs; server timestamps only.
4. Transaction semantics: atomic debits/grants, idempotent `ProcessReceipt`, duplicate resolve protection.
5. Event scheduler: Community Table, meteors, Cosmic Spin board state, and private-server goal config.
6. Telemetry hooks: tutorial funnel, Lumina R10 time, Stardust earn/spend, Spin Token faucet, Feed clear rate, Robux prompt exposure.

---

## Open questions for EP

| # | Question |
|---|----------|
| 1 | Confirm the safer v1 default: **Private Meadow scales only the shared Community Feed server goal**, not personal tier thresholds. |
| 2 | Confirm **Extra Garden Beds (+2)** remains a v1 pass after playtest specifically checks Stardust, mutation, and Feed contribution acceleration. |
| 3 | Confirm renamed player-facing labels: **Glimmer Gathering**, **Community Table**, **Seed Stand**, **Prize Bloom**, **Pollen Basin**, **Halo Sprig**, **Glimmer Ivy**, **Extra Garden Beds (+2)**. |
| 4 | Confirm whether v1 ships the full 40-achievement target or a smaller implementation set with the rest deferred to Phase 09. |
| 5 | Confirm the seven launch Cosmic Spin Legendary item names before Phase 04 art lock. |

---

## Document history

| Date | Author | Change |
|------|--------|--------|
| 2026-06-28 | Game Designer | §1–4 draft |
| 2026-06-28 | EP v1–v5 | Foundation workshops |
| 2026-06-28 | EP v6 | Server-shared Cosmic Spin, public legendary reveal |
| 2026-06-28 | EP grill Q51 | **Option A** — 21 star-map slots; ~10 base breeds; signature mutations on maps; full index ≥3/breed |
| 2026-06-28 | EP grill Q52 | **Grow early, deliver later** — linear Outpost gates only |
| 2026-06-28 | EP grill Q53 | **Cross-breed primary; meteors + Community Feed secondary** for forward seeds |
| 2026-06-28 | EP grill Q54 | **Rotating Community Feed themes**; Lumina loop; Weaver gated |
| 2026-06-28 | EP grill Q55 | **Hybrid nurture** — passive baseline + active phase bonus |
| 2026-06-28 | EP grill Q56 | **Robux: convenience + cosmetics** (Option B); hard spin/random excludes |
| 2026-06-28 | EP grill Q57 | **First discoverer per-server only** |
| 2026-06-28 | EP grill Q58 | **Keep “constellation”** — fantasy universe; ban real-Earth names only |
| 2026-06-28 | EP grill Q59 | **Duplicate legendary copies OK** per snapshot window |
| 2026-06-28 | EP grill Q60 | **12 players** / garden lots per server |
| 2026-06-28 | EP grill Q61 | **Offline per-plot buffer** + upgradeable storage |
| 2026-06-28 | EP grill Q63 | **~12 cross-breds**; 9 fruits = planet delivery menu only |
| 2026-06-28 | EP grill Q62 | **3 pollen swabs / 24h** from others’ gardens |
| 2026-06-28 | EP grill Q64 | **~3 min splice** tier 1; upgrades → ~1 min |
| 2026-06-28 | EP grill Q65 | **Community Feed every ~30 min** |
| 2026-06-28 | EP grill Q66 | **7 legendaries** in weekly Cosmic Spin pool |
| 2026-06-28 | EP grill Q67 | **Cut moth collectors**; pollen player-initiated only |
| 2026-06-28 | EP grill Q68 | **3 display cases**, 1 Prize Bloom each; unlock per planet milestone |
| 2026-06-28 | EP grill Q69 | **R10 → Solara; R15 → Glimmer; R20 → Launch Pad** (post-MVP) |
| 2026-06-28 | EP grill Q70 | **Launch roster locked** — 10 bases, 12 crosses, signature mutations (§1.2b) |
| 2026-06-28 | EP grill Q71 | **Keeper light** — Rank 1–5, 5 story beats, daily triad (§3.1) |
| 2026-06-28 | EP grill Q72 | **Guided ~8 min tutorial** (§2.1) |
| 2026-06-28 | Systems Designer | **Step 2** — §5 economy & balance (growth, delivery, splice, shards) |
| 2026-06-28 | Economy Designer | **Step 3** — §6 monetization SKUs, prompts, compliance |
| 2026-06-28 | EP grill Q73 | **Three nurture tools**; **Infinite Nurture** pass rename |
| 2026-06-28 | EP grill Q74 | **Private servers at v1** — invite-only meadows; scaled Community Feed |
| 2026-06-28 | EP alignment | **Cosmic Coin Pouch / Satchel / Vault** — Robux coin pack SKU names |
| 2026-06-28 | EP alignment | **Private server fairness** — Feed server goal only; no timer, payout, personal-threshold, or gate acceleration |
| 2026-06-28 | UX Designer | **Step 4** — §7 social/visit flows, §8 UX + accessibility |
| 2026-06-28 | Narrative Designer | **Step 5** — §9 world, Keeper voice, planet/collection lore |
| 2026-06-28 | Technical Writer | **Step 6** — studio GDD index, CONTEXT, ADR-002 amend |
