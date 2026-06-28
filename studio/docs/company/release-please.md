# Release Please — Per-Game Configuration

Each game under `games/<name>/` gets its own release-please component at **Phase 06 (Game Bootstrap)**.

## Tag format

`<game-name>-v<semver>` — e.g. `cosmic-garden-v1.2.0`

## Per-game files

```
games/<name>/
├── version.txt
└── CHANGELOG.md
```

## Adding a component (Phase 06)

Add to `release-please-config.json`:

```json
"games/<name>": {
  "release-type": "simple",
  "component": "<name>",
  "changelog-path": "games/<name>/CHANGELOG.md",
  "extra-files": ["games/<name>/version.txt"]
}
```

Add to `.release-please-manifest.json`:

```json
"games/<name>": "0.1.0"
```

Release-please creates PRs titled `chore(<name>): release vX.Y.Z` targeting `prod`.
