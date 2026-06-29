# Research 004 — Security Risk Assessment

**Agent:** Security Specialist  
**Date:** 2026-06-28  
**Run:** `2026-06-28-compliance-feasibility-starlit-conservatory`

## Mandate

Risk assessment for planned Starlit Conservatory features; marketplace asset import security plan; exploit prevention requirements for Phase 06+ implementation.

## Sources

| Topic | URL |
|-------|-----|
| Roblox security tactics | https://create.roblox.com/docs/en-us/scripting/security/security-tactics |
| Client-server boundary | https://create.roblox.com/docs/en-us/scripting/security/client-server-boundary |
| Third-party asset vulnerabilities | https://github.com/Roblox/creator-docs/blob/main/content/en-us/scripting/security/third-party-vulnerabilities.md |
| Anti-exploit patterns | https://simplified.media/guides/roblox-anti-exploit |
| RemoteEvent securing (DevForum) | https://devforum.roblox.com/t/how-to-secure-your-remoteevent-and-remotefunction/3345363 |
| Malicious model identification | https://devforum.roblox.com/t/how-to-identify-a-malicious-model/470670 |
| Technical architecture (this run) | `research/002-technical-feasibility-agent-scope.md` |
| Monetization model (this run) | `research/003-monetization-model-recommendation.md` |
| Monorepo pre-commit hook | `scripts/install-git-hooks.sh` |
| Policy summary | `studio/docs/compliance/roblox-policy-summary.md` |

## Executive summary

**Verdict: PASS (acceptable risk with documented mitigations).**

No feature in the v1 concept requires architecture that is inherently unsecurable. Risk concentrates in **economy remotes** (harvest, breed, sell, polish) and **EP-imported marketplace assets**. Standard server authority + ProfileService + remote middleware addresses gameplay exploits. Asset pipeline requires **mesh-only imports**, sandboxing, and `scan-place-security.py` at Phase 06 bootstrap (the-laboratory port per D14).

---

## Threat model (Phase 02)

| Actor | Capability | Goal |
|-------|------------|------|
| Exploiter (client) | Fire remotes with arbitrary args; spoof ProximityPrompt; decompile client modules | Free items, infinite coins, rare breeds |
| Malicious asset author | Hide backdoors in Toolbox models | Remote code execution, data exfiltration |
| Legitimate player | Spam inputs | Remote queue exhaustion, server lag |

**Assumption (locked D2):** All gameplay Luau is agent-written under `games/starlit-conservatory/src/`; EP does not add gameplay scripts in Studio.

---

## Feature risk matrix

| Feature | Vector | Severity | Required mitigation |
|---------|--------|----------|---------------------|
| **Plant / water / harvest** | Spam harvest without planted crop; harvest others' plots | **High** | Server owns plot state; validate plotId ownership; cooldown + rate limit per remote |
| **Cross-breed lab** | Client selects outcome breedId; duplicate pollen | **Critical** | Server rolls RNG from earn-only inputs; validate pollen/seeds consumed server-side; never accept outcome ID from client |
| **Constellation codex** | Client unlocks all pieces | **Medium** | Server updates codex only after validated breed event |
| **Star Counter polish** | Client sends max quality / instant polish | **High** | Server records polish session start; validate duration window; reject out-of-band quality scores |
| **NPC sell + price band** | Client sets price above band or sells non-owned bloom | **Critical** | Server reads inventory; clamp price to config band; server executes coin grant |
| **Cosmic Coins / inventory** | Direct "add coins" remote | **Critical** | **No remote grants currency** — only server services mutate profile after validated actions |
| **Game passes** | Client claims pass without purchase | **Medium** | `UserOwnsGamePassAsync` on server; refresh on `PromptGamePassPurchaseFinished` |
| **Developer products** | Duplicate receipt grant | **High** | Idempotent `ProcessReceipt` with PurchaseId in DataStore ([Simplified Media monetization guide](https://simplified.media/guides/roblox-monetization)) |
| **Offline pollen cap** | Client sends fake `lastSeen` | **Medium** | Timestamp server-written only; cap computed on join server-side |
| **Meteor Shower drops** | Client spawns rare seeds | **Low** | Event scheduler + drop table server-only |
| **Moth collector** | Client triggers spawn | **Low** | Server gates on codex state |
| **Biome / plot unlocks** | Client unlocks without payment/progress | **Medium** | Server checks coin balance + codex flags before unlock |
| **2P co-op cross-pollinate** (stretch) | Pollinate others' plots without consent | **Medium** | Validate adjacency + mutual opt-in flag in server state |
| **Wishlist notes** (deferred) | Long string lag; unfiltered text | **Medium** | Max string length; `TextService:FilterStringAsync`; 1/min rate limit |
| **ProximityPrompt / ClickDetector** on plots | Activate from any distance | **Medium** | Re-validate distance and ownership in handler ([client-server boundary](https://create.roblox.com/docs/en-us/scripting/security/client-server-boundary)) |

**Top 3 failure modes (security):**

1. **Client-trusted economy** — any coin/breed/inventory mutation accepting client values.
2. **Unscanned marketplace imports** — backdoor in plant mesh pack compromises entire experience.
3. **Unprotected remotes** — breed/harvest spam causing dupes or DataStore corruption under load.

---

## Remote security standard (Phase 06 mandatory)

All Knit service methods exposed to clients must pass shared middleware:

1. **Type validation** — assert argument types; reject silently + suspicion counter.
2. **Rate limiting** — per-player token bucket per remote (e.g. 5–10 harvests/sec max).
3. **Sanity checks** — ownership, distance (≤ MaxActivationDistance + tolerance), game state.
4. **No client authority** — never accept coin amounts, breed outcomes, inventory deltas from client.

Reference: [Roblox security tactics](https://create.roblox.com/docs/en-us/scripting/security/security-tactics) — treat every client call as hostile.

---

## Marketplace asset import plan

`scan-place-security.py` is **not yet in repo** (Phase 06 bootstrap from the-laboratory). Pre-commit hook in `scripts/install-git-hooks.sh` already scans staged `.rbxlx`/`.rbxm` when scanner exists.

### EP import checklist (effective immediately)

| Step | Action |
|------|--------|
| 1 | **Prefer EP-authored Blender exports** over Toolbox for gameplay props |
| 2 | If using Toolbox/marketplace: choose mesh/texture-only assets **with no scripts** |
| 3 | Before insert: confirm Toolbox UI shows **no embedded scripts** |
| 4 | After insert: Explorer search `classname:Script` — delete unexpected scripts |
| 5 | Search project for `require(`, `loadstring`, `getfenv`, `HttpService`, hidden off-screen code |
| 6 | Set imported model **`Sandboxed = true`**; minimal **Capabilities** ([third-party vulnerabilities doc](https://github.com/Roblox/creator-docs/blob/main/content/en-us/scripting/security/third-party-vulnerabilities.md)) |
| 7 | Never grant DataStore, HttpService, or LoadString capabilities to third-party models |
| 8 | Disable **Allow Third Party Sales** in game settings unless explicitly needed |
| 9 | Export place to `games/starlit-conservatory/place/`; commit triggers scan when Phase 06 ready |

### Phase 06 automation

| Control | Owner | When |
|---------|-------|------|
| Port `scan-place-security.py` from the-laboratory | Lead Engineer | Phase 06 bootstrap |
| Pre-commit hook (already in repo) | EP runs `scripts/install-git-hooks.sh` once | Phase 06 |
| CI place scan on changed `.rbxlx`/`.rbxm` | Lead Engineer | Phase 06 CI |
| Full asset pipeline SOP | Asset Pipeline Specialist | Phase 04 (`studio/docs/assets/pipeline.md`) |

### Scan scope (planned script)

Flag **CRITICAL** on: obfuscated scripts, `require(assetId)` to unknown modules, `loadstring`, HttpService in imported models, scripts under hidden services. Block commits on CRITICAL per pre-commit hook.

---

## Monetization security (Cozy Fair F2P)

| Surface | Risk | Control |
|---------|------|---------|
| Game pass perks | Client-side gating only | Server re-check ownership before plot slot bonus / cooldown skip |
| Dev products | Double grant on receipt retry | Idempotent `ProcessReceipt`; store processed PurchaseIds |
| Bloom Rush time-skip | Product fired without purchase | Grant only inside verified receipt handler |
| Cosmic Coin packs | Same | Receipt handler only; never client-triggered |

No paid random at launch reduces PolicyService exploit surface; stub module for future.

---

## Data security

| Concern | Mitigation |
|---------|------------|
| Profile duplication | ProfileService session locks (TD research 002) |
| Inventory dupes via race | Single server session per profile; atomic profile mutations |
| Sensitive data in client | Replicate display-only state; full inventory server-side |
| Admin/backdoor | No admin commands in client; EP does not add hidden scripts |

---

## Security Specialist recommendation

**Risk assessment: PASS** for Phase 02 gate — concept is buildable securely with standard Roblox patterns.

**Conditions for implementation (Phase 06+):**

1. Remote middleware on all gameplay services before vertical slice playtest.
2. EP follows marketplace import checklist; mesh-only preference for v1 props.
3. `scan-place-security.py` ported and pre-commit enabled before first `place/` commit with imports.
4. Economy remotes never accept client-supplied amounts or RNG outcomes.
5. Defer wishlist notes until TextService + rate-limit pipeline exists.

**Residual risk (accepted):** Exploiters in popular sims are inevitable; goal is no client-trusted economy and clean asset pipeline — not zero cheating.
