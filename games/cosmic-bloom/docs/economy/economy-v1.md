# Cosmic Bloom — Economy v1 Proof

**Date:** 2026-07-01
**Artifacts:** [`economy_sim.py`](./economy_sim.py), [`economy-v1-scenarios.csv`](./economy-v1-scenarios.csv)
**Status:** Pre-build hardening pass complete; numbers remain playtest-tunable.

---

## What This Proves

This proof checks whether the current v1 economy is plausible before Luau implementation:

- Lumina R10 / Solara unlock pacing
- Stardust earn and upgrade pressure
- Extra Garden Beds (+2) impact
- Private Meadow Community Table scaling
- Public server Community Table scaling
- Spin Token faucet watchpoints

This is not the final balancing spreadsheet. It is the minimum sanity artifact needed before implementation starts.

---

## Hardening Decisions

| Area | Decision |
|------|----------|
| **Lumina R10 target** | Revise from **60–90 min** to **~105–180 min engaged solo**. The original target was too fast for the listed fruit orders unless order quantities were cut sharply. |
| **Second row assumption** | Baseline pacing assumes players buy the coin-unlocked second plot row around Lumina R5. |
| **Extra Garden Beds (+2)** | Keep in v1, but treat as **watchlisted**. It accelerates Lumina R10 to ~115 min in the model, which is faster but still not an instant unlock. |
| **Private Meadow scaling** | Keep personal thresholds identical. Lower only the private Community Table server-goal floor from **2,500** to **2,000** so 2-player private groups land in the 40–70% clear window. |
| **Spin Tokens** | No Robux spins. Weekly faucet remains acceptable only if Community Table tier 3, server clear, meteors, first discoverer, milestones, and Daily Trio are monitored together. |

---

## Scenario Results

| Scenario | Target | Result | Pass? |
|----------|--------|--------|-------|
| F2P solo, 4→8 plots | Lumina R10 | ~151 min | Yes |
| Active solo, 4→8 plots | Lumina R10 | ~119 min | Yes |
| Extra Garden Beds, 6→10 plots | Lumina R10 | ~115 min | Yes / watchlist |
| Private Meadow, 2 players | Community Table clear | ~43% modeled clear | Yes |
| Private Meadow, 4 players | Community Table clear | ~60% modeled clear | Yes |
| Public, 6 players | Community Table clear | ~53% modeled clear | Yes |
| Public, 12 players | Community Table clear | ~69% modeled clear | Yes |

See the generated CSV for exact rows.

---

## Pass / Fail Thresholds

| Metric | Pass | Fail / action |
|--------|------|---------------|
| **Lumina R10** | 105–180 min engaged solo | Under 105 min: progression too compressed. Over 180 min: first planet drags. |
| **Solara R15 → Glimmer unlock** | 3–6 hr engaged after Solara unlock | Under 3 hr: twilight comes too soon. Over 6 hr: Glimmer feels out of reach. |
| **Nursery T2** | Reachable before or near Lumina R5 | If delayed past Lumina R8, lower Stardust or coin costs. |
| **Nursery T3** | Meaningful mid-game chase after 12 Bloomdex stars | If reached before Solara unlock, raise Stardust gate. |
| **Second plot row** | Around Lumina R4–R6 | If later than R7, row no longer supports R10 pacing. |
| **Private Meadow Feed clear** | 40–70% clear rate at 2–4 active players | Change only server-goal floor/cap, never personal thresholds. |
| **Public Feed clear** | 40–70% clear rate at 6–12 active players | Tune public floor/cap if needed. |
| **Extra Garden Beds (+2)** | Speeds progress without dropping Lumina R10 under 105 min | Disable/pass-gate if it causes runaway Stardust, mutation, or Spin Token access. |
| **Spin Token weekly faucet** | Enough for excitement, not enough to spam Cosmic Spin | Reduce Feed tier 3/server-clear token sources first. |

---

## Implementation Notes

- Use server-owned economy constants; do not let clients submit payout, timer, or reward values.
- Track private server state only inside Community Table server-goal config.
- Record telemetry for: first harvest time, first delivery time, Lumina R5, Lumina R10, second row purchase, Nursery T2/T3 purchase, Feed contribution tier, Spin Token earns/spends, and Extra Garden Beds ownership.
- Keep the CSV simple enough for Producer/Economy to compare against future Phase 09 spreadsheet tuning.
