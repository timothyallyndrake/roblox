# Roblox Policy Summary

Maintained by the **Compliance Officer** agent. Review before any player-facing concept is approved.

**Official sources:**

- [Community Standards](https://about.roblox.com/community-standards)
- [Terms of Use](https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use)
- [Paid Random Items](https://create.roblox.com/docs/production/monetization/paid-random-items)
- [Romantic/Sexual Content Policy (2025)](https://about.roblox.com/newsroom/2025/08/extending-roblox-policy-on-romantic-and-sexual-content)

## Prohibited (all experiences)

- Romantic or sexual content, including **implied** sexual content
- Exploitation, discrimination, harassment, bullying
- Real-world sensitive events, political figures (unauthorized)
- Cheating, scams, misleading content
- Real-money gambling; **Robux or in-experience currency gambling**
- Illegal or regulated goods and activities
- Excessive violence/gore (severity depends on maturity rating)

## High-risk (17+ ID-verified only)

- Social hangouts with **private spaces** (bedrooms, bathrooms)
- Experiences primarily in **adult settings** (bars, nightclubs)
- Bathroom simulators

## Required for public access

- **Content Maturity & Compliance Questionnaire** must be completed
- Unrated experiences restricted to developers + active collaborators only

## Monetization rules

| Mechanic | Requirement |
|----------|-------------|
| Paid random items (Robux or Robux-bought currency) | Disclose **numerical odds** before purchase |
| Indirect random purchases (buy coin → spend on random) | Odds disclosure still required |
| Free random rewards (no payment) | No odds disclosure required |
| Regional restrictions | Use `PolicyService:GetPolicyInfoForPlayerAsync()` |
| Paid random outcomes | Must not be tradable for Robux/real value |

## Marketplace assets

- Run `scan-place-security.py` on imported `.rbxlx` / `.rbxm` files
- Security Specialist owns audit process
- See `studio/docs/assets/pipeline.md` (TBD)

## Concept evaluation checklist

Use [`concept-compliance-checklist.md`](concept-compliance-checklist.md) in Phase 02 for each game pitch.
