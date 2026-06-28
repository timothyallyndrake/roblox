# Git Branching & PR Workflow

Adapted from [the-laboratory](https://github.com/timothyallyndrake/the-laboratory) for the `timothyallyndrake/roblox` monorepo.

## Branches

| Branch | Purpose |
|--------|---------|
| `dev` (default) | Integration — all feature PRs target here |
| `prod` | Releases — promotion from `dev`, release-please merges |

## PR flow

```
feature/* ──squash──► dev ──merge commit──► prod
                         ▲                      │
                         └── merge commit ────┘
                              (back-sync)
```

| PR direction | Merge method |
|--------------|--------------|
| Feature → `dev` | **Squash and merge** |
| `dev` → `prod` (promotion) | **Create a merge commit** |
| Release Please → `prod` | **Squash and merge** |
| `prod` → `dev` (back-sync) | **Create a merge commit** |

## PR requirements

CI must pass:

- Lint, Format, Build (per changed game, or studio validation)
- Conventional Commit Messages
- PR Title Conventional
- Merge Method Acknowledgement (exactly one checkbox in PR body)

## Scope in commit messages

Use scope to indicate area:

- `feat(studio): ...` — company docs, agents, SDLC
- `feat(cosmic-garden): ...` — game-specific (use game folder name)

## Game-specific PRs

Once `games/<name>/` exists, game PRs should include:

- [ ] `selene src` passes
- [ ] `stylua --check src` passes
- [ ] `rojo build` succeeds
- [ ] Playtest checklist if gameplay change
- [ ] Place file committed if Studio changes

## GitHub setup

Run `./scripts/setup-github.sh --apply-rulesets` after repo creation (requires `gh auth login`).
