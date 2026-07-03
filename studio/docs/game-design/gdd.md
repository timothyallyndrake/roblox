# GDD — Game Design Document (Studio Index)

**Status:** Phase 03 — **Draft hardened (Steps 1–6 + pre-build hardening)** · EP sign-off pending (Step 7)
**Last updated:** 2026-07-01
**Active game:** [Cosmic Bloom](../../../games/cosmic-bloom/) (`cosmic-bloom`)

---

## Canonical source of truth

**Full GDD:** [`games/cosmic-bloom/docs/gdd.md`](../../../games/cosmic-bloom/docs/gdd.md)

This studio file is an **index and gate tracker**. Do not duplicate balance tables or UX specs here — edit the game GDD and update this index when sections change.

| Companion doc | Path |
|---------------|------|
| Vision | [`games/cosmic-bloom/docs/VISION.md`](../../../games/cosmic-bloom/docs/VISION.md) |
| Kid pitch | [`docs/discovery/pitch-sells-cosmic-bloom.md`](../discovery/pitch-sells-cosmic-bloom.md) |
| Market scan | [`games/cosmic-bloom/docs/market/2026-07-01-targeted-market-scan.md`](../../../games/cosmic-bloom/docs/market/2026-07-01-targeted-market-scan.md) |
| Economy proof | [`games/cosmic-bloom/docs/economy/economy-v1.md`](../../../games/cosmic-bloom/docs/economy/economy-v1.md) |
| Content catalog | [`games/cosmic-bloom/docs/content/v1-content-catalog.md`](../../../games/cosmic-bloom/docs/content/v1-content-catalog.md) |
| Family audio overview | [`games/cosmic-bloom/docs/reviews/notebooklm-family-overview.md`](../../../games/cosmic-bloom/docs/reviews/notebooklm-family-overview.md) |
| Family test packet | [`games/cosmic-bloom/docs/reviews/2026-07-01-family-read-aloud-test.md`](../../../games/cosmic-bloom/docs/reviews/2026-07-01-family-read-aloud-test.md) |
| Producer Step 7 issue plan | [`games/cosmic-bloom/docs/reviews/2026-07-01-producer-step7-issue-plan.md`](../../../games/cosmic-bloom/docs/reviews/2026-07-01-producer-step7-issue-plan.md) |
| Creative bible | [`games/cosmic-bloom/docs/creative/phase04-creative-bible.md`](../../../games/cosmic-bloom/docs/creative/phase04-creative-bible.md) |
| Engineering addendum | [`games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md`](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md) |
| Foundation grill (Q51–Q74) | [`docs/discovery/grilling-log.md`](../discovery/grilling-log.md) |
| Planning run | [`loops/runs/2026-06-28-planning-gdd-cosmic-bloom/`](../loops/runs/2026-06-28-planning-gdd-cosmic-bloom/) |
| ADR-002 | [`docs/decisions/002-game-direction-cosmic-bloom.md`](../decisions/002-game-direction-cosmic-bloom.md) |
| Technical ADRs | [`docs/decisions/003-cosmic-bloom-persistence-architecture.md`](../decisions/003-cosmic-bloom-persistence-architecture.md) through [`008-cosmic-bloom-event-scheduler-private-meadow.md`](../decisions/008-cosmic-bloom-event-scheduler-private-meadow.md) |

---

## GDD section map

| § | Title | Step | Agent | Status |
|---|-------|------|-------|--------|
| 1 | Overview, systems, Bloomdex, planets, nursery, events | Foundation + 1 | Game Designer / EP grill | ✅ |
| 2 | Core loop + tutorial (§2.1) | 1, Q72 | Game Designer | ✅ |
| 3 | Progression + Keeper (§3.1) | 1, Q71 | Game Designer | ✅ |
| 4 | Achievements | 1 | Game Designer | ✅ |
| 5 | Economy & balance | 2 | Systems Designer | ✅ |
| 6 | Monetization (Cozy Fair) | 3, Q73–Q74 | Economy Designer | ✅ |
| 7 | Social & visit flows | 4 | UX Designer | ✅ |
| 8 | UX flows + accessibility | 4 | UX Designer | ✅ |
| 9 | Narrative & world | 5 | Narrative Designer | ✅ |
| 10 | v1 vertical slice acceptance matrix | Step 7 prep | Producer / QA | ✅ Hardened |

---

## Planning run progress

**Run ID:** `2026-06-28-planning-gdd-cosmic-bloom`

| Step | Agent | Status |
|------|-------|--------|
| 1 | game-designer | ✅ |
| 2 | systems-designer | ✅ |
| 3 | economy-monetization-designer | ✅ |
| 4 | ux-ui-designer | ✅ |
| 5 | narrative-designer | ✅ |
| 6 | technical-writer | ✅ |
| 7 | producer | ⏳ Producer issues + EP sign-off |

**Research artifacts:** `loops/runs/2026-06-28-planning-gdd-cosmic-bloom/research/001`–`005`

---

## Phase 03 stop criteria

| Criterion | Met | Where |
|-----------|-----|-------|
| Core loop | ✅ | Game GDD §2 |
| Progression | ✅ | Game GDD §3 |
| Monetization | ✅ | Game GDD §6 |
| Achievements | ✅ | Game GDD §4 |
| Co-op model | ✅ | Solo-first; private VIP meadows v1; no P2P — §1.9, §5.10 |
| EP approval | ❌ | Step 7 |
| Pre-build hardening | ✅ | Market scan, economy proof, content catalog, family overview/test packet, creative bible, engineering addendum, ADR-003–008 |

---

## Locked design snapshot *(agents: read game GDD for detail)*

| Topic | Decision |
|-------|----------|
| **World** | Open starlit meadows — **no glass domes** |
| **Core verbs** | Breed & complete · Feed the planets |
| **Currency** | Cosmic Coins · Stardust *(upgrade item)* · Comet Shards · Spin Tokens *(earn-only)* |
| **Bloomdex** | 21 star-map slots; 10 bases + 12 crosses + mutations *(§1.2b)* |
| **Planets** | Lumina → Solara *(R10)* → Glimmer *(R15)* |
| **Economy proof** | Lumina R10 target hardened to **~105–180 min engaged solo** |
| **Community Feed** | ~30 min; Lumina / Solara / Glimmer rotation — **MVP** |
| **Cosmic Spin** | Server-shared; legendary snapshot; 7/week pool |
| **Pollen** | Player-only harvest + swab *(3/day)* — **no moth collectors** |
| **Monetization** | Passes + deterministic dev products + cosmetics; **Cosmic Coin Pouch/Satchel/Vault**; **private meadows 100 R$/mo** *(Feed server goal only — §5.7)* |
| **Tutorial** | ~8 min guided; Keeper → Rank 3 |
| **Nurture tools** | Moon Lantern · Sun Scope · Twilight Lantern |

---

## Post–Step 6 housekeeping

| Item | Status |
|------|--------|
| ADR-002 aligned to Phase 03 GDD | ✅ Amended 2026-06-28 |
| CONTEXT.md updated | ✅ |
| Compliance checklist sync | ✅ Cosmic Coins naming · ⏳ domes — Phase 04 gate |
| Full Bloomdex lore blurbs | ✅ Stable names + starter blurbs in content catalog; art-final blurbs Phase 04 |
| Economy spreadsheet | ✅ Lightweight proof + generated CSV; fuller Phase 09 sheet optional |
| Step 7 acceptance matrix | ✅ Hardened in game GDD §10 |

---

## Phase gate

**Next:** Step 7 — Producer issues + **EP sign-off** → Phase 04 art lock and Phase 06 bootstrap.
