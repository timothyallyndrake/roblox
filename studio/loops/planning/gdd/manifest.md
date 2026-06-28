---
loop_id: planning.gdd
version: 1
sdlc_phase: "03"
title: Game Design Document
game_scoped: true

agents:
  - game-designer
  - systems-designer
  - ux-ui-designer
  - economy-monetization-designer
  - narrative-designer
  - technical-writer
  - producer

autonomy: maximum
grill_me: when_ep_input

outputs:
  - studio/docs/game-design/gdd.md
  - games/{game_slug}/docs/gdd.md
  - runs/{run_id}/report.md

stop_criteria:
  - id: gdd_complete
    type: checklist_complete
    items: [core_loop, progression, monetization, achievements, co_op_model]
  - id: ep_approval
    type: ep_approval

handoff:
  next_loop: creative.bible

github:
  create_issues: true
  labels: [phase-03]
---

# Loop: GDD Planning

_Stub — expand when Phase 03 begins._

Final step: **producer** creates GitHub Issues for GDD implementation tasks on Project board.
