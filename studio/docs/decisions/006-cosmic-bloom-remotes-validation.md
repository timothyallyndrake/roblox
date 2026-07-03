# ADR-006: Cosmic Bloom Remotes And Validation

**Status:** Accepted
**Date:** 2026-07-01
**Deciders:** Technical Director, Lead Roblox Engineer, Security Specialist

## Context

Cosmic Bloom includes currency, inventory, spins, purchases, growth timers, and social interactions. Roblox clients cannot be trusted for any of these authoritative values.

## Decision

All gameplay remotes represent player intent only. The server validates eligibility and computes all state changes.

Remote families:

- Garden: plant, nurture, harvest
- Nursery: start splice, claim splice
- Outpost: deliver order
- Community Table: contribute fruit, claim tier rewards
- Cosmic Spin: request spin, resolve spin
- Events: claim meteor crate
- Social: swab pollen, visit board preferences
- Cosmetics: equip/unequip
- Marketplace: purchase prompt callbacks handled by server adapters

No remote may accept client-provided reward values, odds, timers, ownership flags, receipt grants, or inventory deltas.

## Consequences

- Server tests must be written for every remote before or alongside implementation.
- Invalid requests should fail silently or return kid-safe feedback; no detailed exploit hints.
- Rate limits are required for high-frequency remotes.
- Security review must include remote argument validation and replay attempts.

## References

- [Cosmic Bloom GDD §10](../../../games/cosmic-bloom/docs/gdd.md)
- [Phase 06 implementation addendum](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md)
