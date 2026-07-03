# Research 001 — Roblox Policy Screen: Starlit Conservatory

> **Historical note (2026-07-01):** This screened the earlier Starlit Conservatory concept. Cosmic Bloom supersedes floating domes, Star Counter, and old slug language. Use the current Cosmic Bloom GDD for launch questionnaire and policy answers.

**Agent:** Compliance Officer  
**Date:** 2026-06-28  
**Run:** `2026-06-28-compliance-feasibility-starlit-conservatory`

## Concept summary (screened)

Cosmic plant breeding sim in floating glass domes. Core loop: plant → nurture → cross-breed → constellation codex → polish rare blooms at Star Counter → sell to NPC visitors. Optional 2P co-op (adjacent plots). No PvP theft. Monetization intent (from VISION): everything earnable; Robux = currency/time-skip only.

## Sources

| Topic | URL |
|-------|-----|
| Content maturity & questionnaire | https://create.roblox.com/docs/en-us/production/promotion/content-maturity |
| Experience guidelines (age recommendations) | https://create.roblox.com/docs/en-us/production/promotion/experience-guidelines |
| Paid random items policy | https://create.roblox.com/docs/production/monetization/paid-random-items |
| Paid random items clarification (2025) | https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622 |
| PolicyService API | https://create.roblox.com/docs/reference/engine/classes/PolicyService |
| Text chat / UGC text guidelines | https://create.roblox.com/docs/en-us/chat/guidelines |
| Text filtering | https://create.roblox.com/docs/ui/text-filtering |
| Restricted content (private spaces, hangouts) | https://en.help.roblox.com/hc/en-us/articles/15869919570708-Restricted-Content-Policy |
| Romantic/sexual content policy (2025) | https://about.roblox.com/newsroom/2025/08/extending-roblox-policy-on-romantic-and-sexual-content |
| Publishing requirements (Roblox Kids/Select) | https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166 |
| Community Standards | https://about.roblox.com/community-standards |
| Free random rewards (no payment) — odds not required | https://devforum.roblox.com/t/guidelines-around-users-paying-for-random-virtual-items/307189 |

## Policy screen by feature

### Content & maturity

| Feature | Risk | Assessment |
|---------|------|------------|
| Night sky / glass domes / cosmic plants | Low | No violence, fear, or romantic themes. Suitable for **Minimal** maturity label / **All ages** age recommendation. |
| Constellation codex / Keeper NPC quests | Low | Educational-adjacent collection; no sensitive topics. |
| Meteor Shower event (rare seed drops) | Low | Gameplay event reward; not gambling if no Robux wager. |
| Moth/firefly collectors | Low | Non-violent collection mechanic (Bee Swarm lane). |
| Star Counter polish minigame | Low | Skill/timing interaction, not a game of chance for stakes. |
| Optional 2P co-op (shared dome wall) | Low | Cooperative gameplay space, **not** a social hangout (primary activity is sim progression, not open chat). |
| Async wishlist notes on breeds for sale | Medium | Player-authored text visible to others → **TextService filtering required** + rate limit (~1/min per Roblox chat guidelines). Not a policy blocker if implemented correctly. |

**Social hangout classification:** Avoid marketing copy that frames the experience as "chat with friends" or "hang out in domes." Title/description should emphasize plant breeding / collection sim. Questionnaire should answer **No** to social hangout unless design pivots.

**Private spaces (17+):** Glass domes and greenhouse plots are **not** bedrooms/bathrooms. No enclosed personal/secluded spaces for sleeping/changing/bathing. **Clear.**

### Prohibited content check

| Category | Status |
|----------|--------|
| Romantic/sexual content | **Clear** — no romance, dating, or suggestive plant/NPC framing planned |
| Violence/gore | **Clear** — cozy sim; no combat |
| Gambling (playable) | **Clear** — no Robux/currency wager on chance outcomes |
| Real-money gambling | **Clear** |
| Adult settings (bars, clubs) | **Clear** |
| Harassment vectors (PvP steal) | **Clear** — explicitly excluded vs GAG2 |
| Political/sensitive real-world events | **Clear** |

### Monetization & random outcomes

| Mechanic | Paid random item? | Requirement |
|----------|-------------------|-------------|
| Cross-breed lab (earn-only seeds/pollen) | **No** — reward for gameplay action without Robux payment | No odds disclosure required ([DevForum 307189](https://devforum.roblox.com/t/guidelines-around-users-paying-for-random-virtual-items/307189)) |
| Meteor Shower rare seeds (free event) | **No** | No odds disclosure |
| Robux-purchased seed packs / gacha eggs | **Yes, if added** | Numerical odds pre-purchase; `PolicyService.ArePaidRandomItemsRestricted`; declare in questionnaire |
| Robux-bought currency → random breed | **Yes, if added** | Indirect purchase rule applies — odds before spend |
| Time-skip / currency packs (deterministic) | **No** | Standard Developer Products / Game Pass compliance |

**Recommendation:** Keep all breeding RNG **earn-only**. If Phase 03 adds Robux seed packs, treat as paid random items with full odds UI + PolicyService gating + guaranteed-purchase alternative for restricted players.

**Locked vision constraint (D18/VISION):** "Everything earnable; Robux = currency/time-skip only" — aligns with lowest compliance risk path.

### Player trading / selling

- NPC stall sales (coins to NPC astronomers): **Clear** — no peer trading of paid random outcomes.
- If players ever trade bred plants with each other: honor `PolicyService.IsPaidItemTradingAllowed`; do not allow trading of items obtained via paid random generators for restricted users.

### Text & UGC safety

- Wishlist notes: filter via `TextService:FilterStringAsync` → `GetNonChatStringForBroadcastAsync`; rate-limit inputs; respect `CanUserChatAsync`.
- Any future free-form dome naming/signs: same filtering pipeline.

### Publishing & audience reach

To reach **Roblox Kids / Select (under-16)** audiences ([DevForum 4573166](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166)):

- Creator: ID verified, 2FA, active Roblox Plus/Premium
- Experience: complete Maturity & Compliance Questionnaire (target **Minimal**)
- Pass evaluation process (highly engaged 16+ users during trial period)

Plan questionnaire completion at **Phase 15 launch prep**; draft answers now for **Minimal / All ages**.

## Risk summary

| Level | Items |
|-------|-------|
| **High** | None identified for current concept |
| **Medium** | (1) Paid random seed packs if added later — mitigatable with odds + PolicyService; (2) Wishlist note UGC text — mitigatable with filtering |
| **Low** | Social hangout misclassification in listing copy; crowded genre moderation scrutiny (not policy, but discoverability) |

## Compliance Officer recommendation

**Policy screen: PASS** for Phase 02 concept approval path.

**Recommended target rating:** **Minimal** maturity / **All ages** age recommendation (pending Economy Designer monetization lock and Security asset pipeline in steps 3–4).

**Conditions for launch sign-off:**

1. Breeding RNG remains earn-only OR paid random compliance stack shipped before any Robux random purchase.
2. Wishlist notes (if shipped in v1) use server-side text filtering + rate limits.
3. Experience listing copy positions as **sim/collection**, not social hangout.
4. Maturity questionnaire completed before public launch; retake if paid random or social features added.
