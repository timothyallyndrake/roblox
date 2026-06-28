# ADR-001: Monorepo Studio Architecture

**Status:** Accepted  
**Date:** 2026-06-27  
**Deciders:** EP, Producer, Technical Director

## Context

We need a permanent game development company infrastructure that supports multiple Roblox games over time, with full documentation and agent-driven development.

## Decision

Use monorepo `timothyallyndrake/roblox` with:

- `studio/` — company, agents, SDLC, CONTEXT.md
- `games/<name>/` — per-game code and place files
- Per-game release-please tags (`<game-name>-v<semver>`)
- Single CONTEXT.md as living state for all agent sessions

## Consequences

- Game #2+ reuses studio infrastructure without new org repos
- Phase 06 bootstraps games from the-laboratory into `games/<name>/`
- All agents read studio/CONTEXT.md before acting

## References

- [grilling-log.md](../discovery/grilling-log.md) Q4, Q6, Q15, Q16
- [phase-00-framework.md](../phases/phase-00-framework.md)
