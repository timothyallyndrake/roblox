# ADR-005: Cosmic Bloom Rolling 24h Clock Policy

**Status:** Accepted
**Date:** 2026-07-01
**Deciders:** EP, Technical Director, Lead Roblox Engineer, Producer

## Context

Cosmic Bloom uses several daily or per-day mechanics: free Cosmic Spin, Keeper Daily Trio, pollen swabs, and some social limits. Mixing reset models can confuse players and create exploit paths.

## Decision

Use a unified rolling 24-hour per-account policy for v1 player limits:

- Free daily Cosmic Spin
- Keeper Daily Trio claim
- Pollen swab daily limits
- Per-plant foreign swab lockout

Use server time only. Store last-claim or per-target timestamps in the player profile. Do not use client local time for eligibility.

Weekly rotations, such as Cosmic Spin Legendary pool and Meteor Merchant catalog, use UTC schedule windows owned by the server/event scheduler.

## Consequences

- UI must say "ready in Xh Ym" instead of implying midnight reset.
- Returning players have predictable personal timers.
- Server tests must cover clock skew, rejoin, duplicate request, and boundary behavior.
- Weekly live-ops schedules are separate from personal rolling limits.

## References

- [Cosmic Bloom GDD](../../../games/cosmic-bloom/docs/gdd.md)
- [Phase 06 implementation addendum](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md)
