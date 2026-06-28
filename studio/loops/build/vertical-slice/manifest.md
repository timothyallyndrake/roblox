---
loop_id: build.vertical-slice
version: 1
sdlc_phase: "07"
title: Vertical Slice — Roadmap Issues
game_scoped: true

agents:
  - lead-roblox-engineer
  - level-designer
  - qa-lead
  - technical-director
  - producer

autonomy: maximum
grill_me: when_ep_input

outputs:
  - games/{game_slug}/docs/vertical-slice.md
  - runs/{run_id}/roadmap-issues.md

stop_criteria:
  - id: issues_created
    type: github_issues_created
    min: 1
  - id: ep_approval
    type: ep_approval

handoff:
  next_loop: playtest.round-1

github:
  create_issues: true
  labels: [phase-07]
  project_column: Backlog
---

# Loop: Vertical Slice → GitHub Issues

_Stub — expand when Phase 07 begins._

Produces **roadmap issues** on GitHub Project board. EP + agent pair per issue; EP works Blender/Studio.

## Final step

**producer** creates issues from `roadmap-issues.md` with acceptance criteria + playtest checklist links.
