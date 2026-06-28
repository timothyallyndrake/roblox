## Summary

- <!-- 1-3 bullet points -->

## Test plan

- [ ] Studio docs updated (if `studio/` change)
- [ ] `selene src` / `stylua --check src` / `rojo build` (if `games/<name>/` change)
- [ ] 2-player Studio test (if gameplay change)
- [ ] Place file saved and committed (if Studio/map change)
- [ ] `studio/CONTEXT.md` updated (if phase gate or locked decision)

## Pre-merge checklist (required)

- [ ] PR title uses Conventional Commit format (`feat|fix|docs|refactor|test|chore|ci|build|perf|style|revert`)
- [ ] Scope matches changed area (`studio` or game folder name)
- [ ] GitHub Issue linked (if applicable)
- [ ] ADR created for architectural decisions

## Waivers (if any)

- <!-- If any checklist item is not complete, provide explicit waiver and rationale -->

---

## Merge Method Acknowledgement (required)

CI requires **exactly one** checkbox below. Use this table:

| PR direction | Check this box |
|--------------|----------------|
| Feature → **`dev`** | **Squash and merge** |
| **`dev` → `prod`** (promotion) | **Create a merge commit** |
| **Release Please** → **`prod`** | **Squash and merge** |
| **`prod` → `dev`** (back-sync) | **Create a merge commit** |

- [ ] I will use Squash and merge
- [ ] I will use Create a merge commit
