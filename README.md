# roblox

Monorepo for the **Roblox Virtual Game Studio** — a reusable game development company (`studio/`) and one or more Roblox games (`games/`).

**GitHub:** [timothyallyndrake/roblox](https://github.com/timothyallyndrake/roblox)

## Structure

```
roblox/
├── studio/          # Game development company — agents, SDLC, docs, CONTEXT.md
├── .cursor/         # Cursor rules + agent skills (repo root — required for discovery)
└── games/           # One folder per game (bootstrapped from the-laboratory)
    └── <game-name>/
```

## Quick start

1. Read [`studio/CONTEXT.md`](studio/CONTEXT.md) — current state of the studio
2. Read [`studio/docs/company/sdlc.md`](studio/docs/company/sdlc.md) — 18-phase SDLC
3. Read [`studio/AGENTS.md`](studio/AGENTS.md) — agent bootstrap instructions

## Branches

| Branch | Purpose |
|--------|---------|
| `dev` (default) | Integration |
| `prod` | Releases |

All changes via PR. See [`studio/docs/company/git-workflow.md`](studio/docs/company/git-workflow.md).

## Current phase

**Phase 00 — Studio Framework** (in progress)

No games bootstrapped yet. See [`games/README.md`](games/README.md).
