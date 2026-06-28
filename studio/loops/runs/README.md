# Run artifacts

Each loop execution creates a folder: `studio/loops/runs/<run-id>/`

```
runs/<run-id>/
├── brief.md           # EP natural-language goals
├── criteria.json      # Parsed structured criteria (agent-generated)
├── state.md           # Human-readable state
├── state.json         # Machine state
├── log.md             # Append-only step log
├── grilling-log.md    # Grill-me Q&A for this run
├── research/          # Web research outputs with citations
│   └── 001-topic.md
└── report.md          # Final summary for EP
```

Run folders may be gitignored except this README — or commit significant runs for audit trail.

**Naming:** `YYYY-MM-DD-<loop-id-short>-<optional-game-slug>`

Example: `2026-06-28-discovery-game-ideas`
