# Grilling Log

Append-only record of all Q&A from grill sessions. Source of truth for EP decisions.

---

## Session 1 — Plan-level grilling (2026-06-27)

| # | Question | Answer |
|---|----------|--------|
| Q1 | Primary motivation | **Hybrid:** learn seriously + aim for real traction |
| Q2 | Who builds / time | **Agents code everything.** EP: assets, Studio, playtest. **15+ hrs/week.** |
| Q3 | Target audience | **TBD** — Market Research + Compliance recommend |
| Q4 | Where does the company live? | **Monorepo:** `studio/` + `games/<name>/` |
| Q5 | Context inheritance | **`studio/CONTEXT.md`** — single living doc |
| Q6 | Monorepo GitHub name | **`timothyallyndrake/roblox`** |
| Q7 | Missing agent roles | **Full expanded roster** (+ Marketing, Analytics, Technical Writer, Security, Moderation, Animator) |
| Q8 | SDLC granularity | **~18 phases (00–17)** |
| Q9 | Monetization | **Research decides in Phase 03** |
| Q10 | Playtest feedback | **Structured templates + GitHub Issues** |
| Q11 | Project board owner | **Producer + GitHub Actions automation** |
| Q12 | Repo go-live timing | **Phase 00 immediately** |
| Q13 | Son involvement | **Not now** — Junior Contributor slot reserved |
| Q14 | Infrastructure preservation | **Everything relevant from the-laboratory**, adapted |
| Q15 | Release-please strategy | **Per-game tags** — each `games/<name>/` own version + CHANGELOG |
| Q16 | Workspace / repo layout | **`roblox/`** at `github.com/timothyallyndrake/roblox` with `studio/` + `games/` |
| Q17 | Phase 01 grilling timing | **Deferred to Phase 01 creative session** |

---

## Session 2 — Phase 01 creative grilling (2026-06-28)

_Creative Director leads. One question at a time._

| # | Question | Answer |
|---|----------|--------|
| Q18 | When you imagine **playing** this game 15 hrs/week, what's the core feeling? | **Unsure yet.** Rough ideas: (1) **hacker simulator** — grind loops TBD; (2) **base build/defend + Angry Birds-style projectile attacks** on other players' bases, players can't leave their base during attacks. Grindy loops unclear on both. Wants process to continue. |
| Q19 | Which rough idea excites you more to **play** for an hour? | **Either/or + open to other ideas.** Kids said base siege sounds cool. Son flagged hacker sim might get Roblox shutdown (valid compliance concern). EP wants a series of creative questions to spark novel ideas — continue grilling one at a time. |
| Q20 | What sounded cool to kids about base siege? | **Unlocking new stuff.** EP still exploring randomly. Wants agents to pitch 2–3 novel ideas. Criteria: novel, fun, cozy, relaxing, addicting/rewarding loops, **solo-playable** (base siege PvP may fail this). |
| Q21 | Which pitch to deep-dive first? (A Starlit / B Fixery / C Sandcastle) | **None yet — keep grilling, pitch more options** |
| Q22 | What Roblox games do you/kids play most? | **Simulators / collectors** |
| Q23 | What frustrates you about simulators today? | **Top 3:** (1) runs out of things to do after unlocking everything, (2) too pay-to-win — wants **everything earnable in-game** (Robux ok for currency/time-skip only), (3) feels lonely solo. Wants fresh twist; **simpler + more elegant = better**. |
| Q24 | Refined pitches D/E/F — pick one? | **Keep grilling.** Starlit Conservatory explicitly stays on the potential options list. |
| Q25 | What does "not lonely" look like? | **Live co-op** — wants to play alongside others in real time |
| Q26 | Solo vs co-op model? | **Solo works fully + co-op optional bonus** |
| Q27 | Visual vibe? | **Cozy pastel** — soft, warm, Ghibli / Animal Crossing energy |
| Q28 | Ready to name front-runner? | **Not yet.** Starlit stays on list. EP pitched **treasure hunt + storefront** idea. Wants **final list of 3** to discuss: Starlit + elaborated treasure shop + one more agent pitch. |
| Q29 | _(pending — EP picks from Final 3)_ | |
| Q30 | Games you've really enjoyed? | **Bee Swarm Simulator, Pet Simulator, Wizard Tycoon, Plane Crazy, Rally Kart** |
| Q31 | Which reference game hook kept you coming back? | **Bee Swarm Simulator** — field grinding, bees, quests, events |
| Q32 | When you say **"simple,"** what do you mean? | **A — One core verb.** Collect → upgrade → collect faster (Bee Swarm DNA). Few systems, deep mastery. |
| Q33 | All 3 finalists score 8+ (Starlit 8.65, Hearth 8.48, Glider 8.45). **Which front-runner?** A) **Starlit Conservatory** B) **Hearth & Haul** C) **Glider's Rest** D) **Not ready — keep iterating.** | **D + redirect (Discord 2026-06-28):** Find 3 all-new pitches — not referenced anywhere in repo, truly novel (never made before on Roblox). |
| Q34 | **Iteration 1 — repo-clean Final 3** (Driftbell 8.73, Snowglobe 8.63, Chime 8.53). Uniqueness-verified via web research. **Which front-runner?** A) **Driftbell Valley** B) **Snowglobe Shelf** C) **Chime Orchard** D) **Keep iterating** | **Redirect (Discord 2026-06-28):** Need full sell pitches — game loop, etc. Delivered in `runs/.../pitch-sells.md`. |
| Q35 | You've got full sell pitches in `pitch-sells.md`. **Which front-runner?** A) **Driftbell Valley** B) **Snowglobe Shelf** C) **Chime Orchard** D) **Keep iterating** | **Partial (Discord):** Chime Orchard → log as need/shortlist. **Keep iterating** for more options. |
| Q36 | **Chime Orchard** on shortlist. **Iteration 2 sells** in `pitch-sells-iteration-2.md`. **Front-runner?** A) Mothlight B) Steamcup C) Puddleglint D) Chime (shortlist) E) Keep iterating | **E — keep iterating.** EP (Cursor Q37): Chime Orchard → **Build Candidates** list; continue for more neat ideas. |
| Q37 | **Iteration 3 sells** in `pitch-sells-iteration-3.md`. **Chime Orchard** on Build Candidates. **Pick?** A) Candlewick B) Bellgrass C) Sunshard D) Lock Chime E) Add to candidates + iterate F) Keep iterating | **F — keep iterating, new creative direction.** EP: stop same theme (pastel, notes, sounds, bells, motes). Want **different games, different loops/mechanics**. OK with cozy sometimes but diversify. |
| Q38 | **Iteration 4 sells** (creative pivot) in `pitch-sells-iteration-4.md`. **Pick?** A) Sortstop B) Ridgeline C) Kiln Shelf D) Lock Chime E) Keep iterating | **E — keep iterating.** EP (Q39): Build Candidates = **Grow a Garden Cosmic Edition** (Starlit) + **Chime Orchard** only. Continue for more ideas. |
| Q39 | **Iteration 5 sells** (final round) in `pitch-sells-iteration-5.md`. Build Candidates: **Starlit** + **Chime**. **Pick?** A) **Curio Counter** (8.68) B) **Skyline Post** (8.60) C) **Wobble Cart** (8.55) D) Lock **Starlit** E) Lock **Chime** F) Add iter-5 to candidates + decide later | _pending_ |
| Q40 | EP spark: meteor hunter + process feedback | Spark presentation + SPARK-MODE. |
| Q41 | Spark deck reaction | Only Curio scrub&sell stood out; EP leaning Starlit/GAG Cosmic. |
| Q42 | Lock front-runner? | **Locked** → now **Cosmic Bloom** |
| Q43 | Display name + Phase 02 approve | **Cosmic Bloom** locked; Phase 02 approved → Phase 03 GDD |
| Q44 | GDD foundation workshop v1 (EP) | Meadows, moonlight, meteors, day/night — see gdd history |
| Q45 | GDD foundation workshop v2 (EP) | Hub, feed planets, upgrades, retire Star Counter — see gdd history |
| Q46 | GDD foundation workshop v3 (EP) | Bloomdex, Stellar Nursery, Orbital Outpost, planet rounds, leaderboards, kid pitch |
| Q47 | GDD foundation workshop v4 (EP) | Stellar Nursery locked; collection names; 3 planets; uncapped leaderboards |
| Q48 | GDD foundation workshop v5 (EP) | Bloomdex shapes, Cosmic Coins, mutations, Community Feed, Spin Tokens, decor buffs |
| Q49 | Cosmic Spin social spec (EP) | Server-shared board; public legendary reveal; rotating legendary slot |
| Q50 | Cosmic Spin fairness (EP + kids) | **Client-triggered / server-authoritative**; **legendary snapshot on spin start**; in-flight spins keep same legendary+odds until claim rotates board for new spins |

---

## Session 3 — Cosmic Bloom GDD foundation grill (2026-06-28)

*Grilling `games/cosmic-bloom/docs/gdd.md`, `VISION.md`, `pitch-sells-cosmic-bloom.md`. One question at a time.*

| # | Question | Answer |
|---|----------|--------|
| Q51 | Bloomdex content scope — 21 stars vs 21 base breeds × 3 mutations? | **A — 21 star-map slots:** ~10 base breeds + ~10 signature mutation stars + 1 prize star. Full Bloomdex index can list ≥3 mutations/breed; collections highlight signature mutations only. |
| Q52 | Glimmer fruits before Glimmer planet unlock? | **A — Grow early, deliver later.** Stockpile OK; Outpost delivery linearly gated. |
| Q53 | How do players obtain early-tier seeds? | **B — Cross-breed primary; meteors + Community Feed secondary.** Seed Stand = common starters only. |
| Q54 | Community Feed manifest — include fruits most players can't grow yet? | **C — Rotating themes.** Lumina → Solara → Weaver loop; Weaver gated; Lumina always returns. |
| Q55 | Moonlight / sunlight nurture — active click or passive? | **C — Hybrid.** Passive slow growth + active phase bonus burst. |
| Q56 | What can Robux buy at launch? | **B — Convenience + cosmetics.** 3 passes, Coin packs, Bloom Rush; cosmetic skins with earn paths. |
| Q57 | First discoverer — per-server or global shout-out? | **A — Per-server only.** First discoverer on each server gets toast, Bloomdex frame, Spin Tokens. No global cross-server race at launch. |
| Q58 | Rename “Constellation Keeper” / “Constellation Chronicle”? | **Keep.** Fantasy-universe constellations; no real-Earth IAU names. |
| Q59 | Legendary Cosmic Spin — multiple winners same snapshot each get a copy? | **A — Yes, both get it.** Cosmetic legendaries are unlimited copies per rotation window; very rare double-hit. Player 3+ after first claim completes → next legendary snapshot only. |
| Q60 | Max players / garden lots per server? | **12** — tune after playtest. |
| Q61 | Offline growth cap? | **C — Per-plot buffer (1–2 harvests); upgradeable offline storage.** |
| Q62 | Pollen mingling limits? | **B — 3 swabs / 24h** from others; once per foreign plant per day. |
| Q64 | Splice wait at tier 1? | **B — ~3 min real time; offline continues; upgrades → ~1 min.** |
| Q65 | Community Feed cadence? | **B — Every ~30 min; Lumina ~every 90 min.** |
| Q66 | Legendary spin pool size? | **B — 7 per server weekly rotation.** |
| Q67 | Moth / firefly collectors? | **Cut from MVP.** No companion collectors. **Pollen is player-initiated only** — harvest (own) or swab (others, 3/day). No automated/NPC pollen. |
| Q68 | Display case cap at launch? | **B — 3 cases, 1 Prize Bloom each.** One case unlock per launch planet milestone (Lumina → Solara → Glimmer). |
| Q69 | Planet unlock round gates? | **R10 / R15.** Solara @ Lumina R10; Glimmer @ Solara R15. **Launch Pad** @ Glimmer R20 *(post-MVP; +5 pattern)*. |
| Q70 | Exact launch breed roster + cross-breed pairs? | **Approved as drafted.** 10 base breeds, 12 cross-breds, 10 signature map mutations + 1 prize star. See GDD §1.2b. |
| Q71 | Keeper Rank + daily quest structure? | **A — Light.** Rank 1–5; 5 one-time Keeper story beats; Daily Trio; explicit Outpost coin bonus lookup (max +25%). See GDD §3.1. |
| Q72 | Tutorial length & experience? | **A — Guided ~8 min.** Full plant → nurture → deliver → C1 splice; skippable for veterans; Keeper beats 1–2 → Rank 3. See GDD §2.1. |
| Q73 | Nurture tools — sun / twilight parity? | **Three tools:** Moon Lantern, Sun Scope, Twilight Lantern. Active burst in **correct phase only** (twilight: day or night, −20% burst). **Infinite Nurture** pass (renamed) removes cooldown on all three. See §1.5, §6.3. |
| Q74 | Private servers at launch? | **Yes — v1.** Roblox VIP servers for invite-only family/friend meadows. Community Feed scaled for small servers (§5.7). **100 R$/mo** target price. |
| Q75 | Robux Cosmic Coin pack SKU names? | **Cosmic Coin Pouch / Satchel / Vault** (99 / 249 / 499 R$). Spelled out for Roblox shop clarity; matches **Cosmic Coins** currency. |
| Q76 | Can private servers speed up progression? | **No.** VIP meadows scale the **shared Community Feed server goal only** — grow timers, personal Feed thresholds, Outpost payouts, nursery, spin, and gates **identical** to public. Time-skip remains Bloom Rush / Infinite Nurture SKUs. See GDD §5.7. |
| Q77 | Phase 03 naming cleanup after staff review? | **Adopted defaults pending EP final sign-off:** Glimmer Gathering, Community Table, Seed Stand, Prize Bloom, Pollen Basin, Halo Sprig, Glimmer Ivy, Extra Garden Beds (+2). See GDD §1, §5–§10. |
| Q63 | 9 planet fruits vs total plant count? | **9 = delivery menu only.** ~10 base breeds + **~12 cross-breds** at launch + mutations (Option B). |
