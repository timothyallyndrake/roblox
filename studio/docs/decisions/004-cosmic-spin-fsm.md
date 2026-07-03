# ADR-004: Cosmic Spin Finite-State Machine

**Status:** Accepted
**Date:** 2026-07-01
**Deciders:** EP, Technical Director, Lead Roblox Engineer, Economy Designer

## Context

Cosmic Spin is a shared hub board with earned spins, public spectacle, and a weekly Legendary pool. Fairness depends on preserving the active Legendary and odds for players who start spinning before another player claims a Legendary.

## Decision

Implement Cosmic Spin as server-owned `SpinSession` records with a finite-state machine:

1. `Requested`
2. `Approved`
3. `Snapshot`
4. `Animating`
5. `Resolved`
6. `Claimed`
7. `Expired`

On approved start, the server snapshots:

- `legendaryId`
- `legendaryGeneration`
- odds table
- player ID
- cost source: free daily or Spin Token
- session start time

Resolution always uses the stored snapshot. Legendary board rotation affects only new spin sessions after claim completion.

## Consequences

- Multiple in-flight spins may target the same snapshotted Legendary.
- Duplicate Legendary copies are allowed when sessions overlap.
- Client animation is cosmetic; server result is authoritative.
- No Robux or Cosmic Coin spin purchase path exists in v1.
- Tests must cover overlapping sessions, late resolves, duplicate claims, token spend, free daily gating, and board rotation.

## References

- [Cosmic Bloom GDD §1.11](../../../games/cosmic-bloom/docs/gdd.md)
- [Phase 06 implementation addendum](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md)
