# Studio Context

> **Agents: read this file first every session.**  
> Updated by the Technical Writer after every phase gate. Last updated: 2026-06-27.

## Current State

| Field | Value |
|-------|-------|
| **Active phase** | Phase 00 — Studio Framework (awaiting EP sign-off) |
| **Active game** | TBD (no `games/<name>/` yet) |
| **GitHub repo** | [timothyallyndrake/roblox](https://github.com/timothyallyndrake/roblox) ✅ Live |
| **Last gate passed** | — (initial setup) |

## Locked Decisions

| # | Decision | Source |
|---|----------|--------|
| D1 | **Hybrid goal:** learn seriously + aim for real traction | Grilling Q1 |
| D2 | **Agents write all Luau code.** EP creates assets (Blender/marketplace), builds in Studio, playtests. **15+ hrs/week.** | Grilling Q2 |
| D3 | **Target audience:** TBD — Market Research + Compliance recommend in Phase 01–02 | Grilling Q3 |
| D4 | **Monorepo:** `studio/` = company, `games/<name>/` = each game | Grilling Q4 |
| D5 | **Context inheritance:** this file (`studio/CONTEXT.md`) is the single living state doc | Grilling Q5 |
| D6 | **Repo:** `timothyallyndrake/roblox` at `github.com/timothyallyndrake/roblox` | Grilling Q6 |
| D7 | **Full agent roster** (22+ roles) including Marketing, Analytics, Technical Writer, Security, Moderation, Animator | Grilling Q7 |
| D8 | **18 SDLC phases (00–17)** with playtesting, analytics, performance, marketing as separate gates | Grilling Q8 |
| D9 | **Monetization:** Economy Designer + Compliance recommend in Phase 03 | Grilling Q9 |
| D10 | **Playtest feedback:** structured checklists + GitHub Issues + Projects Kanban | Grilling Q10 |
| D11 | **Project board:** Producer agent + GitHub Actions automation | Grilling Q11 |
| D12 | **Repo published in Phase 00** (immediate) | Grilling Q12 |
| D13 | **Son not involved now** — Junior Contributor slot reserved; peer-review ruleset disabled but ready | Grilling Q13 |
| D14 | **Infrastructure:** port everything relevant from the-laboratory, adapted for monorepo | Grilling Q14 |
| D15 | **Release-please:** per-game tags (`<game-name>-v<semver>`), each `games/<name>/` has own version + CHANGELOG | Grilling Q15 |
| D16 | **Local path:** `/Users/tim/Repositories/timothyallyndrake/roblox/` | Grilling Q16 |
| D17 | **Phase 01 creative grilling** deferred to Phase 01 session | Grilling Q17 |

## Open Questions

- [ ] What game are we building? (Phase 01)
- [ ] Target age rating / maturity? (Phase 01–02)
- [ ] Monetization model? (Phase 03)
- [ ] Game working title and folder name? (Phase 01)

## Active Agents (Phase 00)

| Role | Status |
|------|--------|
| Producer | Active — Phase 00 setup |
| Technical Director | Active — monorepo + CI scaffold |
| Technical Writer | Active — docs + this file |

## Grilling Status

- **Plan-level grilling (Q1–Q17):** Complete
- **Phase 01 creative grilling:** Not started — deferred to Phase 01 session

## Phase 00 Gate Checklist

- [x] `timothyallyndrake/roblox` published on GitHub
- [x] `studio/` skeleton with docs tree + templates
- [x] 25 agent skills in `.cursor/skills/` (repo root)
- [x] `.github/` workflows, templates, release-please scaffold
- [x] GitHub labels + branch rulesets configured
- [x] `studio/docs/compliance/roblox-policy-summary.md` written
- [ ] GitHub Projects board created (manual — see github-projects.md)
- [ ] EP sign-off on Phase 00 → begin Phase 01

## Pointers

| Doc | Path | Status |
|-----|------|--------|
| SDLC | [docs/company/sdlc.md](docs/company/sdlc.md) | Draft |
| Agent roster | [docs/company/roster.md](docs/company/roster.md) | Draft |
| Phase index | [docs/company/phase-index.md](docs/company/phase-index.md) | Draft |
| Grilling log | [docs/discovery/grilling-log.md](docs/discovery/grilling-log.md) | Seeded |
| Compliance | [docs/compliance/roblox-policy-summary.md](docs/compliance/roblox-policy-summary.md) | Draft |
| GDD | `docs/game-design/gdd.md` | TBD (Phase 03) |
| Architecture | `docs/technical/architecture.md` | TBD (Phase 05) |

## Lessons Learned

_(Append after each phase retrospective.)_
