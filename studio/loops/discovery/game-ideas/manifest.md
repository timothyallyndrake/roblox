---
loop_id: discovery.game-ideas
version: 1
sdlc_phase: "01"
title: Discovery — Novel Roblox Game Ideas
game_scoped: false
default_game_slug: null

agents:
  - market-research-analyst
  - creative-director
  - game-designer
  - compliance-officer
  - economy-monetization-designer
  - technical-writer
  - producer

autonomy: maximum
grill_me: when_ep_input

inputs:
  - studio/CONTEXT.md
  - studio/docs/discovery/grilling-log.md
  - runs/{run_id}/brief.md

outputs:
  - runs/{run_id}/research/
  - runs/{run_id}/report.md
  - studio/docs/discovery/genre-scorecard.md
  - studio/docs/discovery/concept-pitches.md

stop_criteria:
  - id: pitch_count
    type: deliverable_count
    file: studio/docs/discovery/concept-pitches.md
    field: final_three
    min: 3
  - id: pitch_quality
    type: min_score
    rubric: composite
    rubrics: [market_fit, agent_feasibility, ep_asset_fit, compliance_safety, differentiation]
    min: 8
    scale: 10
  - id: compliance
    type: compliance_clear
    block_on: high_risk
  - id: iteration_cap
    type: max_iterations
    value: 5

stop_logic: any_complete

discord:
  events: [step_complete, waiting_on_ep, finished, blocked, error]

handoff:
  next_loop: compliance.feasibility
  requires_ep_approval: true

github:
  create_issues: false
  labels: [phase-01]
  project_column: Backlog
---

# Loop: Discovery — Novel Game Ideas

## Objective

Autonomously research Roblox market + compliance, iterate on game concepts, and deliver **3 scored finalist pitches** matching EP brief criteria. Uses web research and agent synthesis. Pauses for `/grill-me` only when EP taste input is required.

## Steps

### Step 0 — initialize

- **Agent:** producer
- **Actions:** Parse `brief.md` → `criteria.json`; create `state.md`; Discord `step_complete`
- **Grill:** false

### Step 1 — market research

- **Agent:** market-research-analyst
- **Actions:**
  - WebSearch: Roblox trends, top games, genre CCU, platform incentives, compliance updates
  - Write `runs/{run_id}/research/001-market-landscape.md` with citations
  - Write `runs/{run_id}/research/002-genre-opportunities.md`
  - Update `studio/docs/discovery/genre-scorecard.md`
- **Grill:** false

### Step 2 — synthesize pitches

- **Agent:** creative-director + game-designer
- **Actions:**
  - Read research + brief + CONTEXT locked constraints
  - Produce/update finalist pitches in `concept-pitches.md`
  - Score each pitch on rubrics (1–10)
- **Grill:** false

### Step 3 — compliance screen

- **Agent:** compliance-officer
- **Actions:** Flag high-risk pitches; annotate concept-pitches.md; Discord `blocked` if any high-risk unmitigated
- **Grill:** false

### Step 4 — evaluate stop criteria

- **Agent:** producer
- **Actions:** Check stop criteria; if not met and iteration < cap → goto Step 1 with refined research queries; else goto Step 5
- **Grill:** false

### Step 5 — EP taste grill (if needed)

- **Agent:** creative-director
- **Actions:** If finalists within 1 point or EP brief requests taste input → `/grill-me` one question; Discord `waiting_on_ep`; log to `runs/{run_id}/grilling-log.md`
- **Grill:** true

### Step 6 — finalize

- **Agent:** technical-writer
- **Actions:** Write `runs/{run_id}/report.md`; update CONTEXT.md open questions; Discord `finished`
- **Grill:** false

## Scoring rubric (composite ≥ 8.0 to pass pitch_quality)

| Rubric | Weight | Source agent |
|--------|--------|--------------|
| market_fit | 25% | market-research-analyst |
| agent_feasibility | 25% | technical-director (consulted) |
| ep_asset_fit | 20% | asset-pipeline-specialist (consulted) |
| compliance_safety | 20% | compliance-officer |
| differentiation | 10% | creative-director |

## Brief override examples

| EP writes in brief | Maps to |
|--------------------|---------|
| "5 ideas not 3" | `stop_criteria.pitch_count.min: 5` |
| "Stop at score 7+" | `stop_criteria.pitch_quality.min: 7` |
| "Max 3 research rounds" | `stop_criteria.iteration_cap.value: 3` |
| "Must include co-op" | `constraints[]: optional_live_coop` |

## Handoff

EP approves one finalist → lock `game_slug` working title in CONTEXT.md → start `compliance.feasibility` loop with `game_slug` set.
