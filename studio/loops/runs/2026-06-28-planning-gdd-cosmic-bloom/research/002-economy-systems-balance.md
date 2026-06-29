# Research 002 — Economy & Systems Balance

**Agent:** Systems Designer  
**Date:** 2026-06-28  
**Run:** `2026-06-28-planning-gdd-cosmic-bloom`  
**Step:** 2

## Mandate

Draft GDD **§5 Economy & systems balance** from locked foundation (Q51–Q72, §1.2b roster). Target pacing: Lumina R10 in ~60–90 min; cozy F2P; no paywalls on breeds.

## Sources

| Topic | Reference |
|-------|-----------|
| Locked roster & crosses | `games/cosmic-bloom/docs/gdd.md` §1.2b |
| Planet gates | Q69 — R10 / R15 / R20 |
| Splice timing | Q64 — 180s → 60s |
| Offline | Q61 — per-plot buffer |
| Co-op | §1.9 + §5.10 — solo-first, no P2P |
| GAG progression pacing | `research/001-core-loop-progression-achievements.md` *(adapted, not copied)* |

## Key decisions

1. **8 min** base grow (moonbound/sunbound) — ~2 harvests/hr/plot → 4 plots support Lumina R2–3 fruit demand.
2. **Delivery coins** scale linearly + planet mult (1.0 / 1.35 / 1.7) + Keeper rank %.
3. **Nursery T2** (~800 coins) reachable ~30 min — aligns with Keeper beat 3.
4. **Splice matrix pairs** 70% primary at T1 — cross-breed remains primary discovery path; meteors secondary with pity.
5. **Community Feed pool** scales with active players — 12-player cap at 14k fruit goal.
6. **Co-op model locked:** no shared plots/trading v1; stop criterion `co_op_model` satisfied in §5.10.

## Deliverable

`games/cosmic-bloom/docs/gdd.md` **§5** — full tables, formulas, playtest checklist.

## Next step

Step 3 — economy-monetization-designer: refine §6 Robux price bands, pass friction prompts, Bloom Rush tuning against §5 earn rates.
