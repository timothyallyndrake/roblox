# Loop System — Grilling Log

---

## Session 1 — Loop engine design (2026-06-28)

| # | Question | Answer |
|---|----------|--------|
| LQ1 | Autonomy — how often loop waits for EP? | **Maximum autonomy.** Unsure what "phase gates" meant — minimal EP interruption; only when needed. Agents use `/grill-me`. **Discord webhook** notify each step + when waiting on EP or finished. |
| LQ2 | Stop criteria format? | **Natural language brief** → parsed to structured criteria in manifest/run. Asked what "override per run" means — brief merges with manifest defaults. **Loop per SDLC step** through roadmap issue creation. **Game-aware** (`game_slug`) for multi-game repo. EP implements via Blender + Studio + agent pairing per issue. |

## Open (next grilling)

| # | Topic |
|---|-------|
| LQ4 | GitHub issue creation — fully automated `gh` vs draft-for-approval |
| LQ3 | Discord setup | **Full bidirectional Discord.** Webhook notify + bot listener for EP replies in channel. Convo AI bot. Credentials in `local.json` (gitignored). **Rotate bot token** — was exposed in chat. |
