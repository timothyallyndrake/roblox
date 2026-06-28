---
name: rgs-discord-listen
description: Start Discord listener for EP replies to loop grill questions. Use for /rgs-discord-listen.
disable-model-invocation: true
---

Run in background:
```bash
python3 scripts/studio-discord-bridge.py listen
```
Tell EP to reply in Discord channel when loops are WAITING_ON_EP.
