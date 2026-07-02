#!/usr/bin/env python3
"""Lightweight Cosmic Bloom v1 economy sanity model.

This is intentionally simple: it tests whether the current GDD targets are
plausible before implementation, not whether the final economy is solved.
Run from repo root:

    python3 games/cosmic-bloom/docs/economy/economy_sim.py
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "economy-v1-scenarios.csv"

KEEPER_BONUS = {1: 0.00, 2: 0.05, 3: 0.10, 4: 0.15, 5: 0.25}

# Known Lumina table from GDD §5.3.
KNOWN_ROUNDS = {
    1: (10, 0, 0, 150),
    2: (15, 8, 0, 280),
    3: (20, 12, 5, 420),
    5: (28, 18, 10, 650),
    10: (45, 35, 22, 1200),
    15: (60, 48, 30, 1800),
}


@dataclass(frozen=True)
class Scenario:
    name: str
    start_plots: int
    row_unlock_round: int = 5
    row_bonus_plots: int = 4
    avg_yield: float = 4.0
    grow_minutes: float = 8.0
    active_nurture_factor: float = 0.88
    keeper_rank: int = 3
    notes: str = ""


def interpolate_round(round_id: int) -> tuple[float, float, float, float]:
    if round_id in KNOWN_ROUNDS:
        return KNOWN_ROUNDS[round_id]
    lower = max(r for r in KNOWN_ROUNDS if r < round_id)
    upper = min(r for r in KNOWN_ROUNDS if r > round_id)
    ratio = (round_id - lower) / (upper - lower)
    return tuple(
        KNOWN_ROUNDS[lower][i] + (KNOWN_ROUNDS[upper][i] - KNOWN_ROUNDS[lower][i]) * ratio
        for i in range(4)
    )


def lumina_totals(start_round: int, end_round: int) -> tuple[float, float, float, float]:
    glow = moon = nebula = coins = 0.0
    for round_id in range(start_round, end_round + 1):
        g, m, n, c = interpolate_round(round_id)
        glow += g
        moon += m
        nebula += n
        coins += c
    return glow, moon, nebula, coins


def estimate_minutes_to_lumina_r10(scenario: Scenario) -> dict[str, float | str]:
    # Tutorial completes R1, so estimate R2-R10.
    effective_grow = scenario.grow_minutes * scenario.active_nurture_factor
    minutes = 0.0
    total_fruit = 0.0
    base_coins = 0.0
    for round_id in range(2, 11):
        glow, moon, nebula, coins = interpolate_round(round_id)
        round_fruit = glow + moon + nebula
        plots = scenario.start_plots
        if round_id >= scenario.row_unlock_round:
            plots += scenario.row_bonus_plots
        fruit_per_min = plots * scenario.avg_yield / effective_grow
        minutes += round_fruit / fruit_per_min
        total_fruit += round_fruit
        base_coins += coins
    harvests = total_fruit / scenario.avg_yield
    stardust = harvests  # 1 Stardust / harvest; mutation bonus excluded.
    coins = base_coins * (1 + KEEPER_BONUS[scenario.keeper_rank])
    return {
        "scenario": scenario.name,
        "plots": f"{scenario.start_plots}->{scenario.start_plots + scenario.row_bonus_plots}",
        "target": "Lumina R10",
        "minutes_est": round(minutes, 1),
        "coins_est": round(coins),
        "stardust_est": round(stardust),
        "pass": "YES" if 105 <= minutes <= 180 else "CHECK",
        "notes": scenario.notes,
    }


def feed_goal(server_type: str, players: int) -> int:
    if server_type == "private":
        return min(8000, 2000 + (750 * players))
    return min(14000, 4000 + (750 * players))


def estimate_feed_clear(server_type: str, players: int) -> dict[str, float | str]:
    goal = feed_goal(server_type, players)
    # Feed uses stockpiled fruit. Model assumes each engaged player can commit
    # roughly 750 fruit from inventory in a 12-minute window by mid-game.
    contribution = players * 750
    clear_rate = contribution / goal
    return {
        "scenario": f"{server_type}-{players}p-feed",
        "plots": "",
        "target": "Community Table clear",
        "minutes_est": 12,
        "coins_est": "",
        "stardust_est": "",
        "pass": "YES" if 0.4 <= clear_rate <= 0.7 else "CHECK",
        "notes": f"goal={goal}; modeled_contribution={contribution}; clear_rate={clear_rate:.0%}",
    }


def main() -> None:
    rows: list[dict[str, float | str]] = []
    rows.append(
        estimate_minutes_to_lumina_r10(
            Scenario(
                "f2p-solo-4-to-8-plots",
                4,
                notes="Baseline engaged solo; assumes second plot row around Lumina R5.",
            )
        )
    )
    rows.append(
        estimate_minutes_to_lumina_r10(
            Scenario(
                "active-solo-4-to-8-plots",
                4,
                avg_yield=4.5,
                active_nurture_factor=0.78,
                notes="Higher active nurture uptime and stronger harvest average.",
            )
        )
    )
    rows.append(
        estimate_minutes_to_lumina_r10(
            Scenario(
                "extra-garden-beds-6-to-10-plots",
                6,
                notes="Tests +2 paid beds plus coin row; should accelerate but not erase pacing.",
            )
        )
    )
    for server_type, counts in (("private", (2, 4)), ("public", (6, 12))):
        for players in counts:
            rows.append(estimate_feed_clear(server_type, players))

    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "scenario",
                "plots",
                "target",
                "minutes_est",
                "coins_est",
                "stardust_est",
                "pass",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(row)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
