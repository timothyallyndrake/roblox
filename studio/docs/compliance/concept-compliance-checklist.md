# Concept Compliance Checklist

Complete in **Phase 02** for the chosen game concept. Compliance Officer signs off before EP approval.

## Game concept

- **Display name:** Cosmic Bloom *(locked — ADR-002)*
- **Slug:** `cosmic-bloom`
- **Target maturity rating:** **Minimal / All ages**
- **Genre:** Cozy plant breeding / collection sim with open starlit meadows, Bloomdex, Orbital Outpost, Community Table, and earn-only Cosmic Spin

## Checklist

- [x] No romantic/sexual content (including implied) — *cozy sim; no romance mechanics or suggestive framing*
- [x] No real-money or Robux gambling mechanics planned — *no paid random; Cosmic Spin is earn-only and disclosed before spin*
- [x] Violence/gore level appropriate for target maturity rating — *no combat; cozy collection loop*
- [x] No social hangout private spaces (unless 17+ ID-verified path chosen) — *open meadow plots + Roblox VIP servers; not bedrooms/bathrooms; marketed as collection sim*
- [x] No adult-only settings (bars, clubs) unless 17+ path chosen — *open starlit meadows and hub only*
- [x] Monetization plan reviewed (Economy Designer + Compliance) — *Cozy Fair F2P: deterministic passes + dev products; no paid random at launch (see research/003)*
- [x] Paid random items (if any) have odds disclosure plan + PolicyService plan — *None at launch; PolicyService stub if peer trading added later; full odds stack documented only if paid random ever added (not recommended)*
- [x] Marketplace asset import plan includes security scan — *EP mesh-only checklist now; `scan-place-security.py` + pre-commit at Phase 06 bootstrap (see research/004)*
- [x] Content Maturity Questionnaire strategy documented for launch phase — *target Minimal; complete at Phase 15 launch; creator ID verify + 2FA + Plus for Kids/Select reach*

## Compliance Officer sign-off

- **Status:** **PASS (concept policy screen)** — 2026-06-28
- **Notes:** Phase 02 research remains historical under the Starlit Conservatory run, but Phase 03 canonical design is Cosmic Bloom. Medium-risk watch: (1) no custom text UGC at v1; (2) any future Robux random seed packs require paid-random compliance stack; (3) visit privacy ships v1; (4) private meadows are comfort-only and scale only the shared Community Feed server goal. Monetization aligned to GDD §6. Producer Step 7 + EP sign-off remain.

## Technical Director sign-off

- **Status:** **PASS (agent-only implementation feasible)** — 2026-06-28
- **Notes:** Historical Phase 02 feasibility remains directionally valid, but Phase 06 must use the Cosmic Bloom GDD §10 acceptance matrix and implementation addendum. v1 vertical slice feasible with ProfileService + Knit server-authoritative sim. Primary schedule risk: EP asset throughput and breadth of systems, not agent Luau.

## Economy / Monetization Designer sign-off

- **Status:** **APPROVED (Cozy Fair F2P model)** — 2026-06-28
- **Notes:** Robux = time-skip + convenience passes + cosmetics only; all breeds/biomes earnable. No paid random at launch. Launch stack: 3 game passes + deterministic dev products. Excludes GAG-style Robux steal. Current SKU names and guardrails live in GDD §6.

## Security Specialist sign-off

- **Status:** **PASS (acceptable risk with mitigations)** — 2026-06-28
- **Notes:** Historical security matrix contains retired Star Counter / moth concepts; Phase 06 security work must use Cosmic Bloom systems: Orbital Outpost, Community Table, pollen swabs, Cosmic Spin, private meadows, marketplace receipts. Requires server authority + remote middleware + EP import checklist; automated scan at Phase 06.

## Producer sign-off

- **Status:** **FINALIZED — pending EP approval** — 2026-06-28
- **Notes:** All 9 Phase 02 checklist items complete. Staff sign-offs: Compliance, TD, Economy, Security. Phase 03 GDD now supersedes Starlit-era mechanics; Step 7 still needs Producer Issues + EP sign-off.

## EP sign-off

- **Status:** **Pending Phase 03 Step 7** — review Cosmic Bloom GDD §10 acceptance matrix and open EP questions
