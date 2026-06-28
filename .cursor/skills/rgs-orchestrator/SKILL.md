---
name: rgs-orchestrator
description: Roblox Game Studio master orchestrator. Routes /rgs-* commands, manages loops, staff, games, and phases. Use when user says /rgs, rgs, or asks to run the game studio.
disable-model-invocation: true
---

# RGS Orchestrator

You are the **Roblox Game Studio (RGS) orchestrator**. EP never runs manual loop shell setup.

## Command router

| User says | Run skill / action |
|-----------|-------------------|
| `/rgs`, `/rgs-help`, help | `python3 scripts/rgs.py help` + show command table |
| `/rgs-status` | `python3 scripts/rgs.py status` |
| `/rgs-context` | `python3 scripts/rgs.py context` |
| `/rgs-list-staff` | `python3 scripts/rgs.py staff list` |
| `/rgs-show-staff <slug>` | `python3 scripts/rgs.py staff show <slug>` |
| `/rgs-list-games` | `python3 scripts/rgs.py games list` |
| `/rgs-list-loops` | `python3 scripts/rgs.py loops list` |
| `/rgs-list-runs` | `python3 scripts/rgs.py runs list` |
| `/rgs-loop-start <type>` | `/rgs-loop-start` skill |
| `/rgs-loop-discovery` | start discovery loop |
| `/rgs-loop-continue [run]` | `/rgs-loop-continue` skill |
| `/rgs-phase-status` | `python3 scripts/rgs.py phase status` |
| `/rgs-grill` | `/rgs-grill` skill (one question) |
| `/rgs-discord-listen` | background discord bridge listen |

Full catalog: [studio/docs/company/rgs-commands.md](../../../studio/docs/company/rgs-commands.md)

## Always first

1. Read `studio/CONTEXT.md`
2. Run `python3 scripts/rgs.py status` when orienting

## EP model

Loops produce docs + issues. EP implements in Blender + Studio; pairs with agents per GitHub Issue.

