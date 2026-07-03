# ADR-003: Cosmic Bloom Persistence Architecture

**Status:** Accepted
**Date:** 2026-07-01
**Deciders:** EP, Technical Director, Lead Roblox Engineer, Producer

## Context

Cosmic Bloom has many persistent systems: garden plots, inventories, Bloomdex discoveries, planet rounds, Keeper Rank, cooldowns, purchases, and receipt history. The game also has child-safety and economy constraints that require server authority and recoverable saves.

## Decision

Use a single server-owned player profile as the persistence boundary for v1. Services may own their own schema sections, but all loads, saves, migrations, and receipt history go through one persistence wrapper.

Minimum profile sections:

- `currencies`
- `items`
- `inventory`
- `garden`
- `nursery`
- `bloomdex`
- `planets`
- `keeper`
- `daily`
- `spin`
- `social`
- `purchases`

Profiles include `schemaVersion`; migrations are explicit and one-way.

## Consequences

- No client writes directly to persistent state.
- Service ownership must be documented before content tables are implemented.
- Receipt IDs live in the profile so dev product grants are idempotent.
- Phase 06 tests must include migration, load failure, and duplicate receipt cases.

## References

- [Cosmic Bloom GDD](../../../games/cosmic-bloom/docs/gdd.md)
- [Phase 06 implementation addendum](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md)
