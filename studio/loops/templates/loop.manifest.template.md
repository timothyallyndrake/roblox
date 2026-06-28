---
loop_id: CHANGE_ME.category.name
version: 1
sdlc_phase: "00"
title: Human Readable Loop Title
game_scoped: false
default_game_slug: null

agents:
  - producer

autonomy: maximum
grill_me: when_ep_input

inputs:
  - studio/CONTEXT.md
  - runs/{run_id}/brief.md

outputs:
  - runs/{run_id}/report.md

stop_criteria:
  - id: example
    type: max_iterations
    value: 5

stop_logic: all_required

discord:
  events: [step_complete, waiting_on_ep, finished, blocked, error]

handoff:
  next_loop: null
  requires_ep_approval: true

github:
  create_issues: false
  labels: []
  project_column: Backlog
---

# Loop: {{TITLE}}

## Objective

_One paragraph._

## Steps

### Step 1 — research

- **Agent:** market-research-analyst
- **Actions:** Web research; write `runs/{run_id}/research/001-topic.md`
- **Grill:** false

### Step 2 — synthesize

- **Agent:** _(role)_
- **Actions:** _
- **Grill:** false

### Step N — create issues

- **Agent:** producer
- **Actions:** Create GitHub Issues from loop output; notify Discord `finished`
- **Grill:** false

## Rubrics

_(Scoring tables if using min_score stop criteria.)_

## Notes

_(Loop-specific guidance.)_
