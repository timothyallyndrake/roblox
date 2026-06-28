# GitHub Projects

Operational Kanban for the virtual game studio. Producer agent maintains issues; EP reviews board for status.

## Setup (one-time, after repo publish)

1. GitHub → **Projects** → **New project** → Kanban template
2. Name: **Roblox Virtual Game Studio**
3. Link to `timothyallyndrake/roblox` repository

## Recommended columns

| Column | Meaning |
|--------|---------|
| Backlog | Planned, not started |
| In Progress | Agent actively working |
| Playtest Ready | Merged to `dev`, needs EP playtest |
| Playtest Feedback | EP submitted feedback |
| Review | Awaiting EP gate sign-off |
| Done | Complete |

## Labels

Created by `./scripts/setup-github.sh`:

- `phase-00` … `phase-17` — SDLC phase
- `type:playtest`, `type:playtest-ready`, `type:docs`
- `gate:blocked` — needs EP sign-off
- `feat`, `fix`, `chore`

Add `agent:<role>` labels as needed (e.g. `agent:game-designer`).

## Automation

`.github/workflows/project-automation.yml` adds `type:playtest-ready` to PRs that touch `games/*/src/`.

## Views

- **Kanban** — default workflow
- **Roadmap** — group by milestone / phase label
- **Timeline** — target dates on phase issues
