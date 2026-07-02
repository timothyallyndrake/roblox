# Cosmic Bloom — Staff Cross-Review Report

**Date:** 2026-06-29  
**Scope:** Game-specific docs (`games/cosmic-bloom/docs/`), pitch, ADR-002, studio GDD index, CONTEXT locked decisions  
**Trigger:** EP alignment pass before GDD Step 7 sign-off  
**PR under review:** [#6](https://github.com/timothyallyndrake/roblox/pull/6) *(Phase 03 GDD draft)*

> **Resolution status (2026-07-01):** Findings in this report were addressed in the follow-up fix pass and summarized in `2026-07-01-extensive-plan-review.md`. Keep this file as the original staff audit record; use the July 1 report plus the current GDD for resolved defaults.

---

## Executive summary

**Overall verdict:** Phase 03 design quality is **high** and grill decisions (Q51–Q76) are largely faithful in the canonical GDD. The game is **design-approvable** after resolving **four cross-cutting doc conflicts** and a **pitch compliance fix**.

**Not ready for EP Step 7 sign-off until:**

1. Internal GDD contradictions are reconciled (tutorial manifest, delivery tables, Community Feed goal math, Keeper rank table).
2. Pitch removes the real-sky constellation wink (conflicts with Q58 / GDD §1.3).
3. Stale studio artifacts are marked superseded or updated (`build-candidates.md`, compliance checklist, planning research `001`).

**No Roblox policy blockers** were found for Minimal/all ages or Cozy Fair, assuming v1 ships without paid random and without unfiltered text UGC.

---

## Reviewers

| Role | Focus areas |
|------|-------------|
| Game Designer | §1–4, roster, Keeper, tutorial, achievements, vertical slice |
| Systems Designer | §5 economy, pacing, Feed scaling, Stardust |
| Economy / Monetization Designer | §6 Cozy Fair, Robux SKUs, private meadow fairness |
| UX/UI Designer | §2.1, §7–8, accessibility, Feed UI |
| Narrative Designer | §9 tone, copy, family-friendly framing |
| Creative Director / Art Director | Vision coherence, differentiation, moth/firefly motif |
| Lead Roblox Engineer / Technical Director | Implementation feasibility, persistence, hub sync |
| Security Specialist | Server authority, spin sessions, swab validation |
| Compliance Officer | Minimal/all ages, Cozy Fair, questionnaire readiness |
| Moderation / Trust & Safety | Stranger dynamics, visit privacy, social pressure |
| Community Manager | Parent/kid messaging, Feed FOMO, listing copy |
| Producer / QA Lead | Gate readiness, §10 testability, GitHub Issues |
| Technical Writer | Cross-doc consistency, stale artifact hygiene |

---

## Cross-cutting findings (consolidated)

Issues flagged by **multiple reviewers** — fix these first.

### Blockers *(must resolve before EP sign-off)*

| ID | Issue | Where | Reviewers |
|----|-------|-------|-----------|
| **X-01** | **Tutorial Lumina R1 uses Nebula Pod** but authoritative §5.3 Round 1 is **10 × Glow Berry only** — no Nebula Pod line, no tutorial override documented | §2.1 step 5–6 vs §5.3 L1055–1057 | Game Designer, Systems, Producer |
| **X-02** | **Community Feed server goal magnitude contradicts:** §1.7b example **40k + 25k + 15k** (~80k fruit) vs §5.7 formula **max ~14k** at 12 players | §1.7b L476 vs §5.7 L1160–1167 | Systems, Game Designer, Producer |
| **X-03** | **§1.7 delivery round examples ≠ §5.3 authoritative table** — R2: 20/15/5 vs 15/8/—; R3: 30/20/10 vs 20/12/5; §1.7 bonus drops (R3 seed, R4+ streak) absent from §5.3 | §1.7 L435–440 vs §5.3 | Systems, Game Designer |
| **X-04** | **Pitch invites real-sky constellation recognition** as “fun lore” — **banned** in GDD §1.3 / Q58 (no IAU names, no “inspired by Little Dipper”) | `pitch-sells-cosmic-bloom.md` L62–63 | Game Designer, UX, Compliance, Creative, Producer |

### Major *(resolve before Phase 04 / family playtest)*

| ID | Issue | Where | Reviewers |
|----|-------|-------|-----------|
| **X-05** | **Keeper Rank table skips Beat 4** (Rank 4 ← beat 3, Rank 5 ← beat 5) while prose says *“Each beat → +1 Rank”* | §3.1 L834–854 | Game Designer, Producer, QA |
| **X-06** | **Weaver Watch gate** (“server median Solara R10+”) — no formula, private-server rule, or fallback when gate fails | §1.7b L464 | Game Designer, Systems, Engineering, Producer |
| **X-07** | **§8.5 Community Feed UI mock** shows **Glow Berry line under Solara Supper** — should be sunbound fruits only | §8.5 vs §1.7b | UX, Systems, Engineering, Producer |
| **X-08** | **Stale studio docs** still describe Starlit Conservatory, glass domes, Star Counter, moth collectors | `build-candidates.md`, `concept-compliance-checklist.md`, `research/001-*`, planning `brief.md` | Producer, Technical Writer, Compliance |
| **X-09** | **Achievement catalog incomplete** — “40 achievements target” but only ~8 samples; research `001` lists retired triggers (Star Counter A04) | §4, §10, research 001 | Game Designer, Producer, QA |
| **X-10** | **VISION.md omits Stardust** as a currency/resource (GDD treats it as core secondary item) | `VISION.md` vs GDD §1.2, §5 | Technical Writer |
| **X-11** | **Free spin reset inconsistent:** §1.11 “calendar day” vs §5.9 “24h rolling” | §1.11 vs §5.9 | Engineering, Security |
| **X-12** | **Visit-stats board privacy** — full stats visible to strangers; hide toggle **post-MVP only** | §7.2–7.3 | Compliance, Moderation, UX |
| **X-13** | **§10 vertical slice** is scope list, not acceptance matrix — QA cannot derive test plan | §10 | Producer, QA |
| **X-14** | **Non-signature mutations underspecified** — ≥3 per base breed required but only 10 signature stars named | §1.2b, §1.4b | Game Designer, Creative |

### Minor *(track; not gate-blocking alone)*

| ID | Issue | Where |
|----|-------|-------|
| m-01 | **Stardust** achievement tier name collides with **Stardust** harvest item | §4 L966 |
| m-02 | **Moth bath** decor name after moth **collector** cut (Q67) | §1.8 |
| m-03 | **Firefly motes** ambient in §9.2 vs cut firefly collectors — needs one creative line | §9.2, §10 |
| m-04 | Keeper greet: “food” (§2.1) vs “supper” (§9.4) | §2.1, §9.4 |
| m-05 | **Weaver Watch** vs **Glimmer** planet naming disconnect for kids | §1.7b, §9.7 |
| m-06 | Duplicate §8.10 footer (*“v1: English only…”*) | §8.10 |
| m-07 | §6 section numbering (6.0 after 6.2) | §6 |
| m-08 | Pitch omits private meadow price + Feed scaling (parent UX gap) | pitch vs §6.3b |
| m-09 | **“Observatory Glass”** nursery cosmetic name evokes domes | §6.5 |
| m-10 | GDD “Open questions for EP” empty while CONTEXT has open items | GDD footer vs CONTEXT |

---

## Reviewer reports (by role)

### Game Designer

**Summary:** Strong grill-aligned foundation; two internal contradictions block sign-off.

**Strengths:** §1.2b roster shippable; dual grow/deliver gates (Q52); Community Feed Lumina loop; Cosmic Spin snapshot spec; §10 honest about cuts.

**Top concerns:** X-01 tutorial manifest; X-05 Keeper ranks; X-06 Weaver gate; tier B reachability before Solara R10; achievement scope undefined; non-signature mutations pipeline gap.

**Recommendations:** Mark §5.3 + §5.7 as single source of truth; fix pitch Q58 conflict; publish mutation stub table; update CONTEXT D26 to include signature mutations.

---

### Systems Designer + Economy / Monetization Designer

**Summary:** Cozy Fair framing and §5 formulas are strong; manifest/Feed conflicts are implementation blockers.

**Strengths:** Currency role clarity; Outpost payout formula; private-server fairness table (D29); spin architecture; coin pack naming (D28); Stardust as nursery gate.

**Top concerns:** X-02 Feed goal math; X-03 manifest tables; Lumina R10 pacing unproven on paper; solo VIP Feed clear rate; Stardust mid-game surplus; Garden Row I (+2 plots) as multiplicative income vs F2P floor.

**Recommendations:** Reconcile B1/B2 immediately; extend §5.11 with Feed clear rates at 2/4/6/12 players; economy spreadsheet before Phase 06; document Weaver gate algorithm.

---

### UX/UI Designer + Narrative Designer

**Summary:** Cohesive cozy frame and ~8 min tutorial arc; Feed exclusion UX and pitch compliance gaps block lock.

**Strengths:** Tutorial beat sequence; HUD shell; visit-stats board layout; Keeper voice samples; accessibility baseline; private meadow copy consistency.

**Top concerns:** X-04 pitch; X-07 §8.5 mock; themed-feed exclusion copy missing; grow-vs-deliver gate not in tutorial; tutorial hub↔garden travel threatens 8 min target; Constellation Chronicle UI absent from §8.

**Recommendations:** Fix §8.5 mock; add inactive hopper state + rejection copy; unify Keeper greet line; add Settings screen spec; parent block for private meadows in pitch.

---

### Creative Director + Art Director

**Summary:** Pillar-level vision coherent; pitch/GDD constellation conflict and moth motif need one creative ruling.

**Strengths:** “Open meadow under stars” differentiator; Bloomdex literal shapes; breed naming; Cozy Fair policy layer; anti-dome identity locked.

**Top concerns:** X-04 pitch; moth bath + Nebula Moth Lantern vs cut collectors; visual identity under-specified for Phase 04; hushed meadow vs carnival hub tone tension.

**Recommendations:** Fix pitch; add §9 moth/firefly ambient-only note; Phase 04 style guide mandate; Cosmic Spin spectacle caps; rename Moth bath if playtest confuses.

---

### Lead Roblox Engineer + Technical Director + Security Specialist

**Summary:** Security-compatible and buildable; needs implementation addendum before Phase 06.

**Strengths:** Server authority consistent; Cosmic Spin session model; no P2P; offline buffer bounds; private-server audit scope narrow (D29).

**Top concerns:** X-11 spin/swab clock policy; spin session FSM unspecified; hub ephemeral vs weekly spin pool persistence; no MVP persistence schema; §10 scope too broad for first playtest; research 004 stale (Star Counter, moths).

**Recommendations:** GDD appendix “Server validation & remotes”; ADR for spin FSM; unify rolling-24h clocks; persistence tiers table; phased vertical slice (A→E); rewrite security feature matrix for Cosmic Bloom.

---

### Compliance Officer + Moderation + Community Manager

**Summary:** Conditional pass — on-policy for Minimal/Cozy Fair; parental trust gaps remain.

**Strengths:** No paid random; no P2P; pollen swab bounded; read-only visits; VIP as social comfort; Lumina Feed loop anti-exclusion; friction prompt guardrails.

**Top concerns:** X-04 pitch; X-12 visit privacy; Feed ~30 min FOMO; legendary spin server chat spectacle; Trust & Safety spec absent; private meadow Feed threshold advantage needs parent FAQ.

**Recommendations:** Refresh compliance checklist for Cosmic Bloom; §6.7b parent-facing monetization summary; visit privacy minimum for v1; prefer in-game toasts over chat for legendaries; Community Feed empathetic exclusion copy.

---

### Producer + QA Lead + Technical Writer

**Summary:** Steps 1–6 content complete; Step 7 process incomplete; stale docs risk agent drift.

**Strengths:** Canonical GDD + studio index pattern; foundation table v7; retired terms documented in ADR; §5.11 playtest seed.

**Top concerns:** X-08 stale artifacts; X-13 §10 not testable; Step 7 Issues not created; legendary spin pool unnamed; compliance EP row still Pending.

**Recommendations:** EP sign-off meeting; superseded banners on research 001; GitHub Issues from §10; vertical slice acceptance matrix; fix build-candidates row; phase-03-gdd.md doc.

---

## Discrepancy matrix (canonical vs other docs)

| Topic | Canonical (GDD / ADR / CONTEXT) | Conflicting doc | Severity |
|-------|--------------------------------|-----------------|----------|
| Lumina R1 fruit | §5.3: 10 Glow Berry | §2.1 tutorial: Nebula Pod delivery | **Blocker** |
| Feed server goal | §5.7: 4k–14k formula | §1.7b: 40k/25k/15k example | **Blocker** |
| Lumina R2/R3 manifests | §5.3 table | §1.7 narrative examples | **Blocker** |
| Constellation lore | §1.3: fantasy only, no real sky | Pitch L62–63: real-sky wink | **Blocker** |
| Keeper rank progression | Table skips beat 4 | “Each beat +1 Rank” prose | **Major** |
| Feed UI fruits | §1.7b theme manifests | §8.5 Solara mock = Glow Berry | **Major** |
| Game identity | Cosmic Bloom, open meadows | build-candidates: domes, Star Counter | **Major** |
| Pollen collection | Player + swab only (Q67) | research 001: moth collectors | **Major** |
| Currencies | Coins + Stardust + Shards + Spin Tokens | VISION: omits Stardust | **Minor** |
| Achievement A04 | First Delivery (Outpost) | research 001: First Polish (Star Counter) | **Major** (stale) |

**Aligned (no action):** Cosmic Coins naming; Orbital Outpost; Bloomdex 21 stars; planet gates R10/R15; private meadow 100 R$/mo Feed-only scaling (D29); Cosmic Coin Pouch/Satchel/Vault (D28); moth collector cut in GDD.

---

## Open questions for EP (prioritized)

1. **Tutorial R1:** Tutorial-only manifest with Nebula Pod, or change tutorial to Glow Mote-first flow matching §5.3?
2. **Feed goal canonical source:** §5.7 formula wins — confirm and revise §1.7b example?
3. **Keeper Beat 4:** Does meteor beat grant Rank 4, or is rank jump intentionally skipped?
4. **Weaver gate:** Keep server median Solara R10+, or gate on personal twilight ownership only?
5. **Pitch L62–63:** Approve GDD-safe replacement (in-universe shapes only)?
6. **Visit privacy v1:** Ship hide-from-strangers minimum, or defer to post-MVP?
7. **Achievement v1 scope:** 40 Chronicle entries, ~15 badges, or smaller vertical-slice subset?
8. **Moth bath:** Rename now (Pollen Basin) or clarify as decor-only in copy?
9. **Stardust tier name:** Rename achievement tier (e.g. Spark) to disambiguate from item?
10. **Garden Row I pass:** Accept +2 plot income delta, or reduce scope after playtest?

---

## Recommended resolution order

### Before EP Step 7 sign-off

1. Fix **X-01 through X-04** in canonical GDD + pitch (single editing pass).
2. Reconcile **§1.7 examples** → point to §5.3 / §5.7 or sync numbers.
3. Fix **Keeper rank table** (§3.1) and align §5.3 `keeperRank` bonus math.
4. Fix **§8.5** Solara Supper mock.
5. Add **superseded banners** to `research/001-*` and planning `brief.md`.
6. Update **`build-candidates.md`** Cosmic Bloom row.
7. Add **Stardust** to `VISION.md` currencies line.

### Producer Step 7 (same sprint as sign-off)

8. Create **GitHub Issues** from §10 with acceptance criteria.
9. Expand §10 into **vertical slice acceptance matrix** (QA).
10. Populate GDD **Open questions for EP** or close with “see this report.”

### Phase 04 parallel (non-blocking for design sign-off)

11. Creative brief: moth/firefly ambient-only; style guide + palette.
12. Compliance checklist refresh under Cosmic Bloom slug.
13. Implementation addendum: remotes, spin FSM, persistence tiers.
14. Full achievement catalog + 7 legendary spin decor names.
15. Trust & Safety annex (§7.7 or studio compliance doc).

---

## Sign-off readiness checklist

| Criterion | Status |
|-----------|--------|
| Core loop specified | ✅ |
| Progression specified | ⚠️ Keeper rank table conflict |
| Economy specified | ⚠️ Internal table conflicts |
| Monetization Cozy Fair | ✅ |
| Achievements specified | ❌ Catalog incomplete |
| Co-op / social model | ✅ |
| Cross-doc consistency | ❌ Blockers X-01–X-04, X-08 |
| EP approval (Step 7) | ❌ Pending |
| Producer Issues from §10 | ❌ Not created |
| Compliance delta review | ❌ Checklist stale |

**Recommendation:** Schedule EP review using this report as the agenda. **Approve design direction**; **defer Step 7 gate pass** until blockers X-01–X-04 are patched (can land as a follow-up commit on PR #6 or a small fix PR).

---

## Appendix: source documents reviewed

| Document | Path |
|----------|------|
| Canonical GDD | `games/cosmic-bloom/docs/gdd.md` |
| Vision | `games/cosmic-bloom/docs/VISION.md` |
| README | `games/cosmic-bloom/README.md` |
| Kid pitch | `studio/docs/discovery/pitch-sells-cosmic-bloom.md` |
| Grill log | `studio/docs/discovery/grilling-log.md` |
| Studio GDD index | `studio/docs/game-design/gdd.md` |
| CONTEXT | `studio/CONTEXT.md` |
| ADR-002 | `studio/docs/decisions/002-game-direction-cosmic-bloom.md` |
| Compliance checklist | `studio/docs/compliance/concept-compliance-checklist.md` |
| Build candidates | `studio/docs/discovery/build-candidates.md` |
| Planning research 001–006 | `studio/loops/runs/2026-06-28-planning-gdd-cosmic-bloom/research/` |

---

*Generated by multi-agent staff review session, 2026-06-29. Individual agent transcripts available in Cursor session history.*
