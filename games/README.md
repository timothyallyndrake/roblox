# Games

Each Roblox game lives in its own folder under `games/`.

## Status

No games bootstrapped yet (Rojo/Knit in **Phase 06**). **First game:** [cosmic-bloom/](cosmic-bloom/) — **Cosmic Bloom** (Phase 03 GDD, 2026-06-28).

## Future layout

```
games/
└── <game-name>/
    ├── src/                  # Knit game code (agent-written)
    ├── place/                # Studio place file (human-built)
    ├── docs/                 # Game-specific technical docs
    ├── version.txt           # Per-game semver (release-please)
    ├── CHANGELOG.md          # Per-game changelog
    ├── default.project.json
    ├── wally.toml
    └── scripts/              # setup, serve-rojo, etc.
```

## Bootstrap source

Games are forked from [the-laboratory](https://github.com/timothyallyndrake/the-laboratory) — infrastructure and toolchain only, not place files or game-specific logic.
