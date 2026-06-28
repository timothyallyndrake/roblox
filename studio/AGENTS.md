# AGENTS.md — Roblox Virtual Game Studio

## Bootstrap (every session)

1. Read [`CONTEXT.md`](CONTEXT.md) — current phase, locked decisions, open questions
2. Read your role skill: `.cursor/skills/<role>/SKILL.md`
3. Check GitHub Issues / Project board for assigned work
4. Produce deliverables; update docs; never contradict locked decisions without an ADR

## Purpose

Virtual game development company building Roblox games in the `games/` monorepo folder. Code in Cursor (`games/<name>/src/`), world in Studio (`games/<name>/place/`). Server-authoritative, multiplayer-ready.

## Monorepo layout

```
roblox/
├── studio/          ← YOU ARE HERE — company, agents, SDLC, CONTEXT.md
└── games/
    └── <game-name>/ ← per-game code, place, toolchain (Phase 06+)
```

## Rules

1. **Read CONTEXT.md first** — single source of truth for studio state
2. **Code in Cursor, world in Studio** — never edit Rojo-managed scripts in Studio
3. **`--!strict`** on all new Luau modules
4. **Server authority** — clients request; server validates and owns state
5. **Conventional commits** — PR title must be `type(scope): description`
6. **Squash merge** to `dev` and `prod`; **merge commit** for `prod` → `dev` back-sync
7. **Document every decision** — ADR in `studio/docs/decisions/` + update CONTEXT.md
8. **Track work in GitHub Issues** — Producer maintains Project board

## Agent roster

See [`docs/company/roster.md`](docs/company/roster.md) — 22+ roles with skills in `.cursor/skills/`.

## SDLC

18 phases (00–17). See [`docs/company/sdlc.md`](docs/company/sdlc.md). No phase gate passes without docs + CONTEXT.md update.

## Pull requests

- Use merge acknowledgement checkboxes in PR template
- Prefer: `./scripts/create-pr.sh` from game folder (Phase 06+)
- See `.cursor/rules/pr-creation.mdc` (studio) and per-game rules

## CI (must pass before merge)

- Lint, Format, Build (per changed game)
- Conventional Commit Messages
- PR Title Conventional
- Merge Method Acknowledgement

## Karpathy principles

See `.cursor/rules/karpathy-guidelines.mdc`
