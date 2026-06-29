# ADR-002: Game #1 — Cosmic Bloom

**Status:** Accepted *(amended Phase 03, 2026-06-28)*  
**Date:** 2026-06-28  
**Deciders:** EP, Creative Director, Producer

## Context

Phase 01 discovery selected a cosmic plant breeding sim. EP locked direction 2026-06-28; display name finalized same day after naming review (Cosmic Bloom over Galactic Garden / Grow a Galactic Garden).

Phase 03 GDD foundation grill (Sessions 3–4, Q51–Q74) and planning run Steps 1–5 refined world layout, economy, UX, and narrative. This amendment aligns ADR-002 with the canonical GDD.

## Decision

1. **Game #1:** **Cosmic Bloom** — cosmic plant breeding in **open starlit meadows**; **Bloomdex** collection; **Orbital Outpost** planet delivery; **Stellar Nursery** cross-breeding; **Community Feed** server co-op.
2. **Slug / folder:** `cosmic-bloom` → `games/cosmic-bloom/`.
3. **Former working titles:** Starlit Conservatory; informal "Grow a Garden Cosmic Edition."
4. **Phase 02 gate:** EP approved 2026-06-28 — Minimal/all ages, Cozy Fair F2P, compliance/feasibility/security PASS.
5. **Phase 03 handoff:** Full GDD at `games/cosmic-bloom/docs/gdd.md`; studio index at `studio/docs/game-design/gdd.md`.

## Supersedes *(original Phase 02 wording — do not use in new docs)*

| Retired | Replaced by |
|---------|-------------|
| Floating **glass domes** | **Open meadows** + personal garden plots |
| **Star Counter** polish-and-sell | **Orbital Outpost** supply capsules |
| **Constellation codex** *(only)* | **Bloomdex** *(constellation-shaped collection maps)* |
| Legacy soft-currency name *(retired)* | **Cosmic Coins** |
| Moth / firefly collectors | **Cut MVP** — player-initiated pollen only |

## Consequences

- Release tags: `cosmic-bloom-v<semver>` per ADR-001.
- Chime Orchard remains future wishlist only.
- Rojo/Knit bootstrap still Phase 06.
- Private **VIP meadows** at v1 launch (Cozy Fair — **social comfort**, not power). Feed contribution thresholds scale for small groups; **all other timers and earn rates identical** to public servers *(GDD §5.7)*.
- Robux **Cosmic Coin** packs: **Cosmic Coin Pouch / Satchel / Vault** — deterministic coin shortcuts, not random gacha *(GDD §6.4)*.

## References

- [pitch-sells-cosmic-bloom.md](../discovery/pitch-sells-cosmic-bloom.md)
- [games/cosmic-bloom/docs/gdd.md](../../../games/cosmic-bloom/docs/gdd.md)
- [games/cosmic-bloom/docs/VISION.md](../../../games/cosmic-bloom/docs/VISION.md)
- [grilling-log.md](../discovery/grilling-log.md) — Q51–Q74
- Compliance run `2026-06-28-compliance-feasibility-starlit-conservatory`
