# Cosmic Bloom — Producer Step 7 Issue Plan

**Date:** 2026-07-01
**Purpose:** Convert the hardened GDD §10 and pre-build artifacts into reviewable GitHub Issues before EP sign-off.

---

## Issue Creation Rules

- Use the GDD §10 acceptance matrix as the source of acceptance criteria.
- Link the relevant hardening artifact in each issue.
- Do not start Luau implementation until EP signs off or explicitly scopes an issue as pre-sign-off exploration.
- Keep family feedback as a gate: either run the live test or record an EP waiver.
- Keep Extra Garden Beds (+2) enabled only after economy/playtest approval.

---

## Recommended Issue Set

| # | Issue title | Primary source | Owner |
|---|-------------|----------------|-------|
| 1 | Step 7: EP Sign-Off On Hardened Cosmic Bloom GDD | GDD §10, open questions | Producer / EP |
| 2 | Phase 04: Art Lock From Creative Bible | Creative bible, content catalog | Art Director |
| 3 | Phase 04: Thumbnail Concepts And First-60-Seconds Positioning | Market scan, creative bible | Marketing / Art / UX |
| 4 | Phase 04: Live Family Feedback And Naming Decision | NotebookLM overview, family test packet | Producer / EP |
| 5 | Phase 06: Persistence Schema And Migration Tests | ADR-003, engineering addendum | Lead Engineer |
| 6 | Phase 06: Garden Growth, Harvest, Offline Buffer | GDD §5.2, ADR-006 | Lead Engineer / Systems |
| 7 | Phase 06: Stellar Nursery And Mutation Rolls | GDD §5.5–§5.6, content catalog | Lead Engineer / Systems |
| 8 | Phase 06: Orbital Outpost And Planet Rounds | GDD §5.3, economy proof | Systems / Engineering |
| 9 | Phase 06: Community Table And Private Meadow Scaling | GDD §5.7, ADR-008, economy proof | Engineering / QA |
| 10 | Phase 06: Cosmic Spin FSM And Earn-Only Tokens | ADR-004, GDD §1.11 | Engineering / Security |
| 11 | Phase 06: Event Scheduler, Meteors, Merchant Windows | ADR-008, GDD §5.8 | Engineering / Systems |
| 12 | Phase 06: Marketplace Receipt Idempotency And Purchase Caps | ADR-007, GDD §6 | Engineering / Economy |
| 13 | Phase 06: Server Remotes Validation Matrix | ADR-006, engineering addendum | Security / Engineering |
| 14 | Phase 07: QA Acceptance Matrix For v1 Slice | GDD §10 | QA Lead |
| 15 | Phase 07: Trust, Safety, Accessibility Checklist | GDD §7.7, §8.10 | UX / Compliance |
| 16 | Phase 09: Economy Tuning Spreadsheet Upgrade | Economy proof CSV/script | Systems / Producer |
| 17 | Phase 12: Playtest Extra Garden Beds (+2) Watchlist | Economy proof, family test | Producer / Economy / QA |

---

## EP Sign-Off Issue Body Draft

```markdown
## Summary
Review and sign off the hardened Cosmic Bloom GDD before Phase 04 art lock and Phase 06 implementation bootstrap.

## Required Review Docs
- `games/cosmic-bloom/docs/gdd.md`
- `games/cosmic-bloom/docs/market/2026-07-01-targeted-market-scan.md`
- `games/cosmic-bloom/docs/economy/economy-v1.md`
- `games/cosmic-bloom/docs/content/v1-content-catalog.md`
- `games/cosmic-bloom/docs/reviews/notebooklm-family-overview.md`
- `games/cosmic-bloom/docs/reviews/2026-07-01-family-read-aloud-test.md`
- `games/cosmic-bloom/docs/creative/phase04-creative-bible.md`
- `games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md`
- `studio/docs/decisions/003-cosmic-bloom-persistence-architecture.md` through `008-cosmic-bloom-event-scheduler-private-meadow.md`

## Sign-Off Decisions
- [ ] Accept Lumina R10 target: ~105-180 min engaged solo.
- [ ] Accept Private Meadow Feed floor: 2,000, with personal thresholds/timers/payouts/gates/odds unchanged.
- [ ] Keep Extra Garden Beds (+2) in v1 but playtest-gate public enablement.
- [ ] Run live family test or explicitly waive it.
- [ ] Confirm Sun Rawr stays or choose rename candidate.
- [ ] Confirm Cosmic Spin visual direction avoids casino energy.
- [ ] Confirm content catalog is sufficient for Phase 04/06.

## Exit Criteria
- EP comments resolved or converted into issues.
- Phase 04 art lock issue opened.
- Phase 06 bootstrap issues opened.
```

---

## Family Feedback Issue Body Draft

```markdown
## Summary
Run the Cosmic Bloom family read-aloud and naming test before build.

## Inputs
- `games/cosmic-bloom/docs/reviews/notebooklm-family-overview.md`
- `games/cosmic-bloom/docs/reviews/2026-07-01-family-read-aloud-test.md`

## Test Names
Sun Rawr, Planet Friends Fed, Prize Bloom, Glimmer Gathering, Seed Stand, Community Table, Extra Garden Beds (+2), Stardust, Bloomdex.

## Acceptance Criteria
- [ ] At least one kid can explain the first action without help.
- [ ] At least one kid can explain Bloomdex after one explanation.
- [ ] Extra Garden Beds does not read as required or unfair.
- [ ] Cosmic Spin does not read as real-money gambling.
- [ ] Community Table reads as helping, not pressure.
- [ ] Rename triggers are captured for EP decision.
```

---

## Engineering Bootstrap Issue Body Draft

```markdown
## Summary
Bootstrap Cosmic Bloom implementation from the hardened engineering addendum and ADRs.

## Sources
- `games/cosmic-bloom/docs/engineering/phase06-implementation-addendum.md`
- `studio/docs/decisions/003-cosmic-bloom-persistence-architecture.md`
- `studio/docs/decisions/004-cosmic-spin-fsm.md`
- `studio/docs/decisions/005-cosmic-bloom-rolling-clock-policy.md`
- `studio/docs/decisions/006-cosmic-bloom-remotes-validation.md`
- `studio/docs/decisions/007-cosmic-bloom-marketplace-idempotency.md`
- `studio/docs/decisions/008-cosmic-bloom-event-scheduler-private-meadow.md`

## Acceptance Criteria
- [ ] Server-owned profile schema drafted.
- [ ] Remote validation tests planned before gameplay implementation.
- [ ] Cosmic Spin session FSM test cases listed.
- [ ] Marketplace receipt idempotency test cases listed.
- [ ] Private Meadow audit rule added to code review checklist.
- [ ] Telemetry minimums added to implementation backlog.
```

---

## Producer Notes

- The family test cannot be considered truly complete until real family answers are captured or EP waives the gate.
- The economy proof intentionally changed the Lumina R10 target instead of shrinking v1 scope.
- The private server hardening change preserves the fairness rule: only the Community Table server goal scales.
- Do not create implementation tickets from superseded loop research without checking the hardened GDD first.
