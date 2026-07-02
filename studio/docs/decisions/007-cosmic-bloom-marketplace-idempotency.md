# ADR-007: Cosmic Bloom Marketplace Idempotency

**Status:** Accepted
**Date:** 2026-07-01
**Deciders:** EP, Technical Director, Lead Roblox Engineer, Economy Designer

## Context

Cosmic Bloom sells deterministic convenience and cosmetic products. It must avoid paid random, paid spins, exclusive breeds, and duplicate dev product grants from receipt retries.

## Decision

Handle all Roblox Marketplace grants through a server adapter that enforces:

- Dev product receipt idempotency by receipt ID.
- Server-side grant tables for every product.
- Purchase caps where applicable.
- Game pass ownership checks before applying persistent pass effects.
- No purchase grant path for Spin Tokens, Cosmic Spin pulls, random seeds, Comet Shards, exclusive breeds, Prize Blooms, or marketplace-only power.

Allowed v1 purchase categories:

- Game passes: Meadow Express, Infinite Nurture, Extra Garden Beds (+2)
- Dev products: Bloom Rush time advance, Cosmic Coin Pouch/Satchel/Vault, Meadow Starter Kit once
- Cosmetics: tool skins, nursery exteriors, plaques, avatar flair, hub emotes
- VIP server: Private Meadow, with no progression multiplier

## Consequences

- Duplicate receipts must return success without duplicate grants.
- Failed grants must retry safely.
- Meadow Starter Kit requires a once-per-account flag.
- Extra Garden Beds (+2) remains economy/playtest gated before public enablement.
- Marketplace tests are required before any product goes live.

## References

- [Cosmic Bloom GDD §6](../../../games/cosmic-bloom/docs/gdd.md)
- [Economy v1 proof](../../../games/cosmic-bloom/docs/economy/economy-v1.md)
- [Phase 06 implementation addendum](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md)
