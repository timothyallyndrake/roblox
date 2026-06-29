# Concept Compliance Checklist

Complete in **Phase 02** for the chosen game concept. Compliance Officer signs off before EP approval.

## Game concept

- **Working title:** Starlit Conservatory *(display name TBD — ADR-002)*
- **Working slug:** `starlit-conservatory`
- **Target maturity rating:** **Minimal / All ages** *(Compliance Officer recommendation — pending EP confirm)*
- **Genre:** Cozy plant breeding / collection sim (GAG cosmic lane)

## Checklist

- [x] No romantic/sexual content (including implied) — *cozy sim; no romance mechanics or suggestive framing*
- [x] No real-money or Robux gambling mechanics planned — *no wager-on-chance; polish minigame is skill-based*
- [x] Violence/gore level appropriate for target maturity rating — *no combat; cozy collection loop*
- [x] No social hangout private spaces (unless 17+ ID-verified path chosen) — *greenhouse plots, not bedrooms/bathrooms; not a social hangout*
- [x] No adult-only settings (bars, clubs) unless 17+ path chosen — *sky domes / greenhouse only*
- [x] Monetization plan reviewed (Economy Designer + Compliance) — *Cozy Fair F2P: deterministic passes + dev products; no paid random at launch (see research/003)*
- [x] Paid random items (if any) have odds disclosure plan + PolicyService plan — *None at launch; PolicyService stub if peer trading added later; full odds stack documented only if paid random ever added (not recommended)*
- [x] Marketplace asset import plan includes security scan — *EP mesh-only checklist now; `scan-place-security.py` + pre-commit at Phase 06 bootstrap (see research/004)*
- [x] Content Maturity Questionnaire strategy documented for launch phase — *target Minimal; complete at Phase 15 launch; creator ID verify + 2FA + Plus for Kids/Select reach*

## Compliance Officer sign-off

- **Status:** **PASS (concept policy screen)** — 2026-06-28
- **Notes:** Research: `studio/loops/runs/2026-06-28-compliance-feasibility-starlit-conservatory/research/001-roblox-policy-screen-starlit-conservatory.md`. Medium-risk watch: (1) wishlist notes need TextService filtering + rate limit; (2) any future Robux random seed packs require paid-random compliance stack. Monetization aligned (step 3). Security aligned (step 4). Producer finalize (step 5) + EP sign-off remain.

## Technical Director sign-off

- **Status:** **PASS (agent-only implementation feasible)** — 2026-06-28
- **Notes:** Research: `studio/loops/runs/2026-06-28-compliance-feasibility-starlit-conservatory/research/002-technical-feasibility-agent-scope.md`. v1 vertical slice feasible with ProfileService + Knit server-authoritative sim. Primary schedule risk: EP asset throughput, not agent Luau. Defer async wishlist notes; solo path critical for Phase 07, 2P co-op stretch/Alpha.

## Economy / Monetization Designer sign-off

- **Status:** **APPROVED (Cozy Fair F2P model)** — 2026-06-28
- **Notes:** Research: `studio/loops/runs/2026-06-28-compliance-feasibility-starlit-conservatory/research/003-monetization-model-recommendation.md`. Robux = time-skip + convenience passes + cosmetics only; all breeds/biomes earnable. No paid random at launch. Launch stack: 3 game passes + deterministic dev products. Excludes GAG-style Robux steal. Numbers refine in Phase 03 GDD.

## Security Specialist sign-off

- **Status:** **PASS (acceptable risk with mitigations)** — 2026-06-28
- **Notes:** Research: `studio/loops/runs/2026-06-28-compliance-feasibility-starlit-conservatory/research/004-security-risk-assessment.md`. Critical vectors: economy remotes, marketplace backdoors. Requires server authority + remote middleware + EP import checklist; automated scan at Phase 06. Defer wishlist notes until text filtering ready.

## Producer sign-off

- **Status:** **FINALIZED — pending EP approval** — 2026-06-28
- **Notes:** All 9 checklist items complete. Staff sign-offs: Compliance, TD, Economy, Security. Run report: `studio/loops/runs/2026-06-28-compliance-feasibility-starlit-conservatory/report.md`. No blockers to Phase 03 GDD handoff.

## EP sign-off

- **Status:** **Pending** — see run `grilling-log.md` Q1
