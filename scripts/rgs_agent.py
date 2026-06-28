#!/usr/bin/env python3
"""RGS agent dispatch helpers — provider-agnostic prompt building + execution."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from agent_providers import AgentResult, get_provider  # noqa: E402

STUDIO = ROOT / "studio"
LOOPS = STUDIO / "loops"
RUNS = LOOPS / "runs"
PROMPT_TEMPLATE = STUDIO / "templates" / "agent" / "loop-continue.prompt.md"


def find_manifest(loop_id: str) -> Path | None:
    parts = loop_id.split(".")
    if len(parts) >= 2:
        candidate = LOOPS / parts[0] / parts[1] / "manifest.md"
        if candidate.exists():
            return candidate
    for path in LOOPS.rglob("manifest.md"):
        if f"loop_id: {loop_id}" in path.read_text():
            return path
    return None


def render_prompt(template_path: Path, variables: dict[str, str]) -> str:
    text = template_path.read_text()
    for key, value in variables.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def load_run_state(run_dir: Path) -> dict:
    sj = run_dir / "state.json"
    if sj.exists():
        return json.loads(sj.read_text())
    return {}


def save_run_state(run_dir: Path, state: dict) -> None:
    state["updated"] = datetime.now(timezone.utc).isoformat()
    (run_dir / "state.json").write_text(json.dumps(state, indent=2))


def build_loop_continue_prompt(run_id: str) -> tuple[str, dict, Path]:
    run_dir = RUNS / run_id
    if not run_dir.exists():
        raise FileNotFoundError(f"Run not found: {run_id}")

    state = load_run_state(run_dir)
    loop_id = state.get("loop_id", "unknown")
    manifest = find_manifest(loop_id)
    if not manifest:
        raise FileNotFoundError(f"Manifest not found for loop: {loop_id}")

    variables = {
        "run_id": run_id,
        "loop_id": loop_id,
        "game_slug": str(state.get("game_slug") or "null"),
        "status": state.get("status", "RUNNING"),
        "manifest_path": str(manifest.relative_to(ROOT)),
    }
    prompt = render_prompt(PROMPT_TEMPLATE, variables)
    return prompt, state, run_dir


def dispatch_loop_continue(
    run_id: str,
    *,
    provider_name: str | None = None,
    dry_run: bool = False,
) -> AgentResult | str:
    prompt, state, run_dir = build_loop_continue_prompt(run_id)

    if dry_run:
        return prompt

    agent_cfg = state.setdefault("agent", {})
    provider = get_provider(provider_name or agent_cfg.get("provider"))
    session_id = agent_cfg.get("session_id")

    result = provider.dispatch(prompt, cwd=ROOT, session_id=session_id)

    agent_cfg["provider"] = provider.name
    if result.session_id:
        agent_cfg["session_id"] = result.session_id
    agent_cfg["last_dispatch"] = datetime.now(timezone.utc).isoformat()
    agent_cfg["last_ok"] = result.ok
    if not result.ok and result.error:
        agent_cfg["last_error"] = result.error
        state["status"] = "ERROR"
    save_run_state(run_dir, state)

    log_path = run_dir / "log.md"
    entry = (
        f"\n## Agent dispatch — {agent_cfg['last_dispatch']}\n\n"
        f"- Provider: {provider.name}\n"
        f"- Session: {result.session_id or session_id or 'new'}\n"
        f"- OK: {result.ok}\n"
    )
    if result.error:
        entry += f"- Error: {result.error}\n"
    entry += f"\n{result.text[:2000]}\n"
    log_path.write_text(log_path.read_text() + entry)

    return result
