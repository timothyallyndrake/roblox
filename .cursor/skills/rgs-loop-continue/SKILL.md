---
name: rgs-loop-continue
description: Continues an active or waiting RGS loop run. Use for /rgs-loop-continue [run_id].
disable-model-invocation: true
---

1. `python3 scripts/rgs.py runs list` if run_id unknown
2. Read `studio/loops/runs/<run_id>/state.json` + brief.md
3. Execute next step per loop manifest + loop-runner skill
4. If WAITING_ON_EP and EP just replied (Discord or chat), log answer → set RUNNING → continue
5. Discord notify each step
