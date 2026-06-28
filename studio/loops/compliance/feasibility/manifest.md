---
loop_id: compliance.feasibility
version: 1
sdlc_phase: "02"
title: Compliance & Feasibility Gate
game_scoped: true
default_game_slug: null

agents:
  - compliance-officer
  - technical-director
  - economy-monetization-designer
  - security-specialist
  - producer

autonomy: maximum
grill_me: when_ep_input

inputs:
  - studio/CONTEXT.md
  - studio/docs/discovery/concept-pitches.md
  - games/{game_slug}/docs/
  - runs/{run_id}/brief.md

outputs:
  - studio/docs/compliance/concept-compliance-checklist.md
  - runs/{run_id}/report.md

stop_criteria:
  - id: checklist_signed
    type: deliverable_complete
    file: concept-compliance-checklist.md
  - id: ep_approval
    type: ep_approval

stop_logic: all_required

handoff:
  next_loop: planning.gdd
  requires_ep_approval: true

github:
  create_issues: false
---

# Loop: Compliance & Feasibility

_Stub — expand when Phase 02 begins. Requires `game_slug` from discovery handoff._

## Steps

1. **compliance-officer** — screen chosen pitch against Roblox policy; research current rules via web
2. **technical-director** — feasibility for agent-only implementation scope
3. **economy-monetization-designer** — monetization model recommendation
4. **security-specialor** — risk assessment for planned features
5. **producer** — finalize checklist; Discord `finished` or `waiting_on_ep`
