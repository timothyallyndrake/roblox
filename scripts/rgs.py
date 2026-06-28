#!/usr/bin/env python3
"""
RGS — Roblox Game Studio CLI.
All /rgs-* skills delegate here. EP never runs raw mkdir/cp for loops.

Usage:
  python3 scripts/rgs.py status
  python3 scripts/rgs.py staff list
  python3 scripts/rgs.py games list
  python3 scripts/rgs.py loops list
  python3 scripts/rgs.py loop start discovery [--game SLUG] [--brief "plain english goals"]
  python3 scripts/rgs.py loop status [run_id]
  python3 scripts/rgs.py runs list
  python3 scripts/rgs.py phase status
  python3 scripts/rgs.py help
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDIO = ROOT / "studio"
SKILLS = ROOT / ".cursor" / "skills"
LOOPS = STUDIO / "loops"
RUNS = LOOPS / "runs"
GAMES = ROOT / "games"
CONTEXT = STUDIO / "CONTEXT.md"
ROSTER = STUDIO / "docs" / "company" / "roster.md"
REGISTRY = LOOPS / "registry.md"
PHASE_INDEX = STUDIO / "docs" / "company" / "phase-index.md"

LOOP_ALIASES: dict[str, str] = {
    "discovery": "discovery.game-ideas",
    "game-ideas": "discovery.game-ideas",
    "compliance": "compliance.feasibility",
    "feasibility": "compliance.feasibility",
    "gdd": "planning.gdd",
    "planning": "planning.gdd",
    "creative": "creative.bible",
    "bible": "creative.bible",
    "architecture": "technical.architecture",
    "technical": "technical.architecture",
    "bootstrap": "bootstrap.game-repo",
    "vertical-slice": "build.vertical-slice",
    "vertical": "build.vertical-slice",
    "alpha": "build.alpha",
    "beta": "build.beta",
    "playtest1": "playtest.round-1",
    "playtest2": "playtest.round-2",
    "analytics": "analytics.instrumentation",
    "performance": "quality.performance",
    "marketing": "marketing.prep",
    "launch-prep": "launch.prep",
    "launch": "launch.ship",
    "liveops": "liveops.cadence",
}

STAFF_SLUGS = [
    "creative-director", "producer", "game-designer", "systems-designer",
    "narrative-designer", "ux-ui-designer", "level-designer", "art-director",
    "asset-pipeline-specialist", "audio-director", "animator", "technical-director",
    "lead-roblox-engineer", "qa-lead", "analytics-data-engineer", "security-specialist",
    "market-research-analyst", "marketing-growth-director", "economy-monetization-designer",
    "compliance-officer", "moderation-trust-safety", "live-ops-producer",
    "community-manager", "technical-writer", "junior-contributor", "loop-runner",
]


def resolve_loop_id(name: str) -> str:
    n = name.strip().lower()
    if n in LOOP_ALIASES:
        return LOOP_ALIASES[n]
    return name


def find_manifest(loop_id: str) -> Path | None:
    # discovery.game-ideas -> discovery/game-ideas/manifest.md
    parts = loop_id.split(".")
    if len(parts) >= 2:
        candidate = LOOPS / parts[0] / parts[1] / "manifest.md"
        if candidate.exists():
            return candidate
    for path in LOOPS.rglob("manifest.md"):
        text = path.read_text()
        if f"loop_id: {loop_id}" in text:
            return path
    return None


def cmd_status(_: argparse.Namespace) -> None:
    print("=== RGS Status ===\n")
    if CONTEXT.exists():
        for line in CONTEXT.read_text().splitlines():
            if line.startswith("| **Active phase**") or line.startswith("| **Active game**"):
                print(line.strip())
    print()
    waiting = []
    if RUNS.exists():
        for d in sorted(RUNS.iterdir()):
            if not d.is_dir():
                continue
            sj = d / "state.json"
            if sj.exists():
                st = json.loads(sj.read_text())
                status = st.get("status", "?")
                loop = st.get("loop_id", "?")
                print(f"Run {d.name}: {status} ({loop})")
                if status == "WAITING_ON_EP":
                    waiting.append(d.name)
            elif (d / "state.md").exists():
                print(f"Run {d.name}: (see state.md)")
    if waiting:
        print(f"\n⏸ Waiting on EP: {', '.join(waiting)}")
    print("\nUse: /rgs-orchestrator for all commands")


def cmd_staff_list(_: argparse.Namespace) -> None:
    print("=== RGS Staff ===\n")
    for slug in STAFF_SLUGS:
        skill = SKILLS / slug / "SKILL.md"
        mark = "✓" if skill.exists() else "✗"
        print(f"  [{mark}] {slug}")
    print(f"\nTotal: {len(STAFF_SLUGS)} roles")
    print("Detail: python3 scripts/rgs.py staff show <slug>")


def cmd_staff_show(args: argparse.Namespace) -> None:
    slug = args.slug
    skill = SKILLS / slug / "SKILL.md"
    if not skill.exists():
        print(f"Unknown staff: {slug}", file=sys.stderr)
        sys.exit(1)
    print(skill.read_text())


def cmd_games_list(_: argparse.Namespace) -> None:
    print("=== RGS Games ===\n")
    if not GAMES.exists():
        print("  (no games/ directory)")
        return
    for item in sorted(GAMES.iterdir()):
        if item.name == "README.md" or not item.is_dir():
            continue
        has_src = (item / "src").exists()
        mark = "bootstrapped" if has_src else "planned"
        print(f"  • {item.name} ({mark})")
    readme = GAMES / "README.md"
    if readme.exists() and len(list(GAMES.iterdir())) <= 2:
        print("\n  (no game folders yet — discovery loop sets working title)")


def cmd_loops_list(_: argparse.Namespace) -> None:
    print("=== RGS Loops ===\n")
    if REGISTRY.exists():
        for line in REGISTRY.read_text().splitlines():
            if line.startswith("| ") and "`" in line and "Loop ID" not in line and "---" not in line:
                print(line)
    print("\nStart: /rgs-loop-start discovery")
    print("Alias: discovery, compliance, gdd, vertical-slice, ...")


def new_run_id(loop_id: str, game_slug: str | None) -> str:
    short = loop_id.replace(".", "-")
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    suffix = f"-{game_slug}" if game_slug else ""
    return f"{date}-{short}{suffix}"


def cmd_loop_start(args: argparse.Namespace) -> None:
    loop_id = resolve_loop_id(args.loop)
    manifest = find_manifest(loop_id)
    if not manifest:
        print(f"Loop not found: {loop_id}", file=sys.stderr)
        print("Available aliases:", ", ".join(sorted(LOOP_ALIASES.keys())), file=sys.stderr)
        sys.exit(1)

    game_slug = args.game
    run_id = args.run_id or new_run_id(loop_id, game_slug)
    run_dir = RUNS / run_id
    if run_dir.exists():
        print(f"Run already exists: {run_id}", file=sys.stderr)
        sys.exit(1)

    run_dir.mkdir(parents=True)
    (run_dir / "research").mkdir(exist_ok=True)

    brief_tpl = LOOPS / "templates" / "run-brief.template.md"
    state_tpl = LOOPS / "templates" / "run-state.template.md"
    brief_path = run_dir / "brief.md"
    state_path = run_dir / "state.md"

    brief_content = brief_tpl.read_text() if brief_tpl.exists() else "# Run Brief\n"
    brief_content = brief_content.replace("_(e.g. discovery.game-ideas)_", loop_id)
    brief_content = brief_content.replace("_(e.g. 2026-06-28-discovery-game-ideas)_", run_id)
    if game_slug:
        brief_content = brief_content.replace("_(null until title locked, then e.g. starlit-conservatory)_", game_slug)
    if args.brief:
        brief_content += f"\n## What I want\n\n{args.brief}\n"
    brief_path.write_text(brief_content)

    state_content = state_tpl.read_text() if state_tpl.exists() else ""
    state_content = state_content.replace("{run_id}", run_id)
    state_content = state_content.replace("{loop_id}", loop_id)
    state_content = state_content.replace("{game_slug}", game_slug or "null")
    state_content = state_content.replace("{ISO8601}", datetime.now(timezone.utc).isoformat())
    state_content = state_content.replace("CREATED | RUNNING | WAITING_ON_EP | FINISHED | BLOCKED | ERROR", "RUNNING")
    state_path.write_text(state_content)

    state_json = {
        "run_id": run_id,
        "loop_id": loop_id,
        "game_slug": game_slug,
        "status": "RUNNING",
        "iteration": 0,
        "started": datetime.now(timezone.utc).isoformat(),
        "updated": datetime.now(timezone.utc).isoformat(),
    }
    (run_dir / "state.json").write_text(json.dumps(state_json, indent=2))
    (run_dir / "log.md").write_text(f"# Run log — {run_id}\n\n")
    (run_dir / "grilling-log.md").write_text(f"# Grilling log — {run_id}\n\n")

    print(f"✅ Loop run created")
    print(f"   Run ID:   {run_id}")
    print(f"   Loop:     {loop_id}")
    print(f"   Manifest: {manifest.relative_to(ROOT)}")
    print(f"   Brief:    {brief_path.relative_to(ROOT)}")
    print()
    print("Next: agent runs /rgs-loop-continue or loop-runner skill on this run_id")
    print(f"      python3 scripts/rgs.py loop continue {run_id}")


def cmd_loop_status(args: argparse.Namespace) -> None:
    if args.run_id:
        run_dir = RUNS / args.run_id
        if not run_dir.exists():
            print(f"Run not found: {args.run_id}", file=sys.stderr)
            sys.exit(1)
        print((run_dir / "state.md").read_text() if (run_dir / "state.md").exists() else json.dumps(json.loads((run_dir / "state.json").read_text()), indent=2))
        return
    cmd_status(argparse.Namespace())


def cmd_runs_list(_: argparse.Namespace) -> None:
    print("=== RGS Loop Runs ===\n")
    if not RUNS.exists():
        print("  (none)")
        return
    for d in sorted(RUNS.iterdir(), reverse=True):
        if not d.is_dir():
            continue
        sj = d / "state.json"
        if sj.exists():
            st = json.loads(sj.read_text())
            print(f"  {d.name}  [{st.get('status')}]  {st.get('loop_id')}")
        else:
            print(f"  {d.name}")


def cmd_phase_status(_: argparse.Namespace) -> None:
    print("=== RGS SDLC Phases ===\n")
    if PHASE_INDEX.exists():
        print(PHASE_INDEX.read_text())
    else:
        print("(phase-index.md missing)")


def cmd_context(_: argparse.Namespace) -> None:
    if CONTEXT.exists():
        print(CONTEXT.read_text())
    else:
        print("CONTEXT.md missing", file=sys.stderr)
        sys.exit(1)


def cmd_help(_: argparse.Namespace) -> None:
    print("""RGS — Roblox Game Studio CLI

Studio:
  status                 Studio + active loop runs
  context                Print studio/CONTEXT.md
  phase status           SDLC phase index

Staff:
  staff list             List all agent roles
  staff show <slug>      Show agent skill file

Games:
  games list             List games/ folders

Loops:
  loops list             Loop registry
  loop start <id>        Create run (auto mkdir/brief/state)
           [--game SLUG] [--brief "text"] [--run-id ID]
  loop status [run_id]   Run or studio status
  runs list              All loop runs

Skills (in Cursor): /rgs-orchestrator, /rgs-loop-start, /rgs-list-staff, ...

See: studio/docs/company/rgs-commands.md
""")


def main() -> None:
    parser = argparse.ArgumentParser(prog="rgs", description="Roblox Game Studio CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("status").set_defaults(func=cmd_status)
    sub.add_parser("context").set_defaults(func=cmd_context)
    sub.add_parser("help").set_defaults(func=cmd_help)

    p = sub.add_parser("phase")
    p_sub = p.add_subparsers(dest="phase_cmd")
    p_sub.add_parser("status").set_defaults(func=cmd_phase_status)

    s = sub.add_parser("staff")
    s_sub = s.add_subparsers(dest="staff_cmd")
    s_sub.add_parser("list").set_defaults(func=cmd_staff_list)
    sh = s_sub.add_parser("show")
    sh.add_argument("slug")
    sh.set_defaults(func=cmd_staff_show)

    g = sub.add_parser("games")
    g_sub = g.add_subparsers(dest="games_cmd")
    g_sub.add_parser("list").set_defaults(func=cmd_games_list)

    lp_reg = sub.add_parser("loops", aliases=["loop-list"])
    lp_reg_sub = lp_reg.add_subparsers(dest="loops_cmd")
    lp_reg_sub.add_parser("list").set_defaults(func=cmd_loops_list)

    rp = sub.add_parser("runs")
    rp_sub = rp.add_subparsers(dest="runs_cmd")
    rp_sub.add_parser("list").set_defaults(func=cmd_runs_list)

    lp = sub.add_parser("loop")
    lp_sub = lp.add_subparsers(dest="loop_cmd")
    ls = lp_sub.add_parser("start")
    ls.add_argument("loop")
    ls.add_argument("--game", default=None)
    ls.add_argument("--brief", default=None)
    ls.add_argument("--run-id", default=None)
    ls.set_defaults(func=cmd_loop_start)
    lst = lp_sub.add_parser("status")
    lst.add_argument("run_id", nargs="?", default=None)
    lst.set_defaults(func=cmd_loop_status)

    args = parser.parse_args()
    if not args.cmd:
        cmd_help(args)
        return
    if args.cmd == "phase" and args.phase_cmd == "status":
        cmd_phase_status(args)
    elif args.cmd == "staff":
        if args.staff_cmd == "list":
            cmd_staff_list(args)
        elif args.staff_cmd == "show":
            cmd_staff_show(args)
        else:
            parser.error("staff subcommand required")
    elif args.cmd == "games":
        if args.games_cmd == "list":
            cmd_games_list(args)
        else:
            parser.error("games subcommand required (try: games list)")
    elif args.cmd in ("loops", "loop-list"):
        if args.loops_cmd == "list":
            cmd_loops_list(args)
        else:
            parser.error("loops subcommand required (try: loops list)")
    elif args.cmd == "runs":
        if args.runs_cmd == "list":
            cmd_runs_list(args)
        else:
            parser.error("runs subcommand required (try: runs list)")
    elif args.cmd == "loop":
        if args.loop_cmd == "start":
            cmd_loop_start(args)
        elif args.loop_cmd == "status":
            cmd_loop_status(args)
        else:
            parser.error("loop subcommand required")
    else:
        args.func(args)


if __name__ == "__main__":
    main()
