# Loop Engine — Full Specification

## 1. Loop manifest schema

Each loop lives at `studio/loops/<category>/<name>/manifest.md` with YAML frontmatter:

```yaml
---
loop_id: discovery.game-ideas
version: 1
sdlc_phase: "01"
title: Discovery — Novel Game Ideas
game_scoped: false          # true = requires game_slug
default_game_slug: null

agents:
  - market-research-analyst   # lead
  - creative-director
  - game-designer
  - compliance-officer
  - technical-writer
  - producer

autonomy: maximum            # maximum | balanced | manual
grill_me: when_ep_input      # never | when_ep_input | each_major_step

inputs:
  - studio/CONTEXT.md
  - runs/{run_id}/brief.md

outputs:
  - runs/{run_id}/research/
  - studio/docs/discovery/concept-pitches.md
  - runs/{run_id}/report.md

stop_criteria:
  - id: pitch_count
    type: deliverable_count
    file: concept-pitches.md
    min_finalists: 3
  - id: pitch_quality
    type: min_score
    rubric: market_fit
    min: 8
    scale: 10
  - id: safety
    type: compliance_clear
    block_on: high_risk
  - id: iteration_cap
    type: max_iterations
    value: 5

stop_logic: any_complete     # all_required | any_complete (first wins)

discord:
  events: [step_complete, waiting_on_ep, finished, blocked, error]
  webhook: config/local.json#discord_webhook_url

handoff:
  next_loop: planning.gdd
  requires_ep_approval: true

github:
  create_issues: true
  labels: [phase-01, agent:producer]
  project_column: Backlog
---
```

## 2. Run brief (natural language → structured)

EP writes plain English in `runs/<run-id>/brief.md`. **Loop Runner** parses into `runs/<run-id>/criteria.json`:

**Brief (EP writes):**
```markdown
# Run Brief

Find 3 cozy pastel Roblox game ideas. Must be solo + optional 2P co-op.
Bee Swarm is my reference. Everything earnable. Stop when 3 score 8+ on market fit.
Max 5 research rounds.
```

**Parsed criteria.json (agent writes):**
```json
{
  "goals_nl": "...",
  "overrides": {
    "stop_criteria.pitch_count.min_finalists": 3,
    "stop_criteria.pitch_quality.min": 8,
    "stop_criteria.iteration_cap.value": 5
  },
  "constraints": ["cozy pastel", "solo + 2P co-op", "bee swarm reference", "fair f2p"]
}
```

**Override explained:** Manifest has defaults. Brief overrides only what EP specifies; rest stays default.

## 3. Run state machine

```
CREATED → RUNNING → [STEP] → (grill?) → WAITING_ON_EP → RUNNING
                ↓                              ↑
                └──────── stop criteria met ───┘
                ↓
           FINISHED | BLOCKED | ERROR
                ↓
           (EP approve handoff) → next loop CREATED
```

State file: `runs/<run-id>/state.md` (human-readable) + `state.json` (machine).

## 4. Step execution

Each step in manifest body:

| Step | Agent | Actions |
|------|-------|---------|
| research | market-research-analyst | WebSearch Roblox trends, competitors, compliance |
| synthesize | creative-director | Merge research + brief into pitches |
| score | market-research-analyst | Rubric score each pitch |
| compliance | compliance-officer | Flag high-risk pitches |
| document | technical-writer | Update concept-pitches.md, CONTEXT.md |
| grill | creative-director | `/grill-me` if manifest requires EP taste input |
| issues | producer | Create GitHub Issues from approved tasks |

After each step: Discord notify + append `runs/<run-id>/log.md`.

## 5. Research loop pattern

```
┌─────────────────────────────────────────┐
│  READ brief + CONTEXT + manifest        │
└─────────────────┬───────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│  RESEARCH (web) — Market Research lead    │
│  Write runs/<id>/research/NNN-topic.md   │
└─────────────────┬───────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│  SYNTHESIZE — assigned design agents     │
│  Iterate pitches / plans / roadmaps      │
└─────────────────┬───────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│  EVALUATE stop criteria                  │
│  Met? → FINISHED + Discord               │
│  Not? → iteration++ if under cap         │
└─────────────────┬───────────────────────┘
                  ▼
              (repeat)
```

## 6. SDLC loop chain (through roadmap issues)

See [registry.md](registry.md). Each SDLC phase 01–07+ has a loop; final steps create **GitHub Issues** on the Project board.

Game slug attaches at Phase 06 bootstrap; earlier loops use `game_slug: null` until title locked in discovery.

## 7. Agent execution (pluggable providers)

Loop steps run via **headless agent dispatch**, not manual in-chat execution:

```bash
python3 scripts/rgs.py loop continue <run_id>
```

Default backend: Cursor `agent` CLI (`-p --trust --output-format json`). Session IDs persist in `state.json` for `--resume`.

Swap backends in `studio/config/agent.local.json` (Ollama, OpenClaw stubs ready).

See [agent-providers.md](../docs/company/agent-providers.md).

## 8. Security

- Discord webhook URL in `config/local.json` — **gitignored**
- Never commit secrets; use `config.example.json` template
- Research cites sources in `research/*.md` for audit trail

## 9. Adding a new loop

1. Copy `templates/loop.manifest.template.md` → `studio/loops/<category>/<name>/manifest.md`
2. Register in `registry.md`
3. Add skill pointer in `.cursor/skills/loop-runner/SKILL.md` catalog
4. Test with a dry run id
