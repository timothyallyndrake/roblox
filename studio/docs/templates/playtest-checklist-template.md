# Playtest Checklist: {{FEATURE_NAME}}

**Game:** {{GAME_NAME}}  
**PR/Issue:** #  
**Date:** YYYY-MM-DD  
**Tester:** EP

## Setup

1. Open `games/{{GAME_NAME}}/place/{{PlaceFile}}.rbxlx` in Studio
2. Run `rojo serve` + Rojo plugin Connect
3. <!-- additional setup steps -->

## Test cases

### TC-1: {{Description}}

- [ ] **Pass** / [ ] **Fail**
- **Expected:**
- **Actual:**
- **Screenshot/note:**

### TC-2: {{Description}}

- [ ] **Pass** / [ ] **Fail**
- **Expected:**
- **Actual:**

## Multiplayer (if applicable)

- [ ] 2-player Studio test (Server + Player)
- [ ] State syncs correctly between clients

## Summary

- **Overall:** Pass / Fail / Blocked
- **Blockers for merge:**

## Agent follow-up

Producer: create GitHub Issue from failures → assign Lead Roblox Engineer
