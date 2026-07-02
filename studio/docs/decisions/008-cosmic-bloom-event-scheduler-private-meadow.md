# ADR-008: Cosmic Bloom Event Scheduler And Private Meadow Audit

**Status:** Accepted
**Date:** 2026-07-01
**Deciders:** EP, Technical Director, Lead Roblox Engineer, Producer

## Context

Cosmic Bloom has several timed shared events: Community Table, meteor showers, Cosmic Spin Legendary rotation, and Meteor Merchant windows. It also launches with Private Meadows, which must remain a social comfort feature rather than a hidden progression advantage.

## Decision

Use a server-owned event scheduler for:

- Community Table cadence and theme rotation
- Meteor shower windows and personal crate assignment
- Meteor Merchant window
- Weekly Cosmic Spin Legendary pool reset
- Cosmic Spin board rotation on Legendary claim

Event windows are computed from server time. Client clocks are never authoritative.

Private Meadow state may branch only inside Community Table server-goal calculation. No other gameplay formula may branch on VIP/private server state.

For v1 hardening, private Community Table goals use:

```
goalFruit = min(8000, 2000 + (750 * activePlayers))
```

Public Community Table goals use:

```
goalFruit = min(14000, 4000 + (750 * activePlayers))
```

Personal contribution thresholds and rewards remain identical in public and private servers.

## Consequences

- Private Meadows are comfort/family servers, not faster progression.
- Server code review must audit any use of `PrivateServerId`.
- Event participation and clear rates must be tracked separately for public and private servers.
- If private groups underperform, tune only the private server-goal constants unless EP explicitly reopens the fairness decision.

## References

- [Cosmic Bloom GDD §5.7](../../../games/cosmic-bloom/docs/gdd.md)
- [Economy v1 proof](../../../games/cosmic-bloom/docs/economy/economy-v1.md)
- [Phase 06 implementation addendum](../../../games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md)
