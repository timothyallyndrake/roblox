#!/usr/bin/env python3
"""
Studio Discord bridge — bidirectional loop communication.

Outbound: webhook embeds (step complete, waiting on EP, finished)
Inbound:  bot polls channel for EP replies when a run is WAITING_ON_EP

Setup:
  cp studio/loops/config/config.example.json studio/loops/config/local.json
  # Fill in webhook URL, bot token, channel ID (never commit local.json)
  # In Discord Developer Portal → Bot → enable **Message Content Intent**
  # (required for the bot to read EP reply text)

Usage:
  python3 scripts/studio-discord-bridge.py notify --event waiting_on_ep --run-id ID --loop discovery.game-ideas --message "Question here"
  python3 scripts/studio-discord-bridge.py listen   # poll EP replies + auto-dispatch loop continue
"""
from __future__ import annotations

import argparse
import os
import json
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "studio" / "loops" / "config" / "local.json"
RUNS_DIR = ROOT / "studio" / "loops" / "runs"
DISPATCH_TIMEOUT = 600  # seconds — agent turns can run several minutes
DISPATCH_LOG = Path("/tmp/rgs-discord-dispatch.log")

EVENT_COLORS = {
    "step_complete": 3447003,
    "waiting_on_ep": 16776960,
    "finished": 3066993,
    "blocked": 15158332,
    "error": 10038562,
}

EVENT_TITLES = {
    "step_complete": "Loop Step Complete",
    "waiting_on_ep": "Waiting on EP — reply in this channel",
    "finished": "Loop Finished",
    "blocked": "Loop Blocked",
    "error": "Loop Error",
}

# Discord blocks urllib's default User-Agent (Cloudflare 1010). Required format:
# https://discord.com/developers/docs/reference#user-agent
DISCORD_USER_AGENT = "DiscordBot (https://github.com/timothyallyndrake/roblox, 1.0)"


def discord_headers(**extra: str) -> dict:
    headers = {"User-Agent": DISCORD_USER_AGENT}
    headers.update(extra)
    return headers


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(f"Missing {CONFIG_PATH} — copy from config.example.json", file=sys.stderr)
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text())


def post_webhook(cfg: dict, event: str, run_id: str, loop_id: str, message: str, game_slug: str = "") -> None:
    url = cfg.get("discord_webhook_url", "")
    if not url or "REPLACE_ME" in url:
        print("Webhook not configured — skipping Discord notify", file=sys.stderr)
        return

    title = EVENT_TITLES.get(event, "Studio Loop Event")
    color = EVENT_COLORS.get(event, 9807270)
    game_line = f"**Game:** `{game_slug}`\n" if game_slug else ""
    reply_hint = ""
    if event == "waiting_on_ep":
        reply_hint = (
            "\n\n_Reply in this channel — the loop **resumes automatically**. "
            f"Include `run:{run_id}` if multiple runs are active._"
        )

    payload = {
        "embeds": [{
            "title": title,
            "color": color,
            "description": (
                f"**Loop:** `{loop_id}`\n**Run:** `{run_id}`\n{game_line}\n{message}{reply_hint}"
            ),
            "footer": {"text": f"run:{run_id} | loop:{loop_id}"},
        }]
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers=discord_headers(**{"Content-Type": "application/json"}),
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        resp.read()
    print(f"Discord webhook sent ({event})")


def api_get_messages(cfg: dict, after: str | None = None) -> list:
    token = cfg.get("discord_bot_token", "").strip()
    channel = cfg.get("discord_channel_id", "").strip()
    if not token or "REPLACE_ME" in token:
        return []

    url = f"https://discord.com/api/v10/channels/{channel}/messages?limit=10"
    if after:
        url += f"&after={after}"

    req = urllib.request.Request(
        url,
        headers=discord_headers(Authorization=f"Bot {token}"),
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def api_get_me(cfg: dict) -> dict:
    token = cfg.get("discord_bot_token", "").strip()
    req = urllib.request.Request(
        "https://discord.com/api/v10/users/@me",
        headers=discord_headers(Authorization=f"Bot {token}"),
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def run_status(run_dir: Path) -> str | None:
    """Read status from state.json; fall back to state.md if missing or stale."""
    state_json = run_dir / "state.json"
    state_md = run_dir / "state.md"

    md_status: str | None = None
    if state_md.exists():
        text = state_md.read_text()
        for status in ("WAITING_ON_EP", "RUNNING", "FINISHED", "BLOCKED", "ERROR"):
            if f"**Status:** {status}" in text:
                md_status = status
                break

    if state_json.exists():
        json_status = json.loads(state_json.read_text()).get("status")
        # Agent updates can desync files; prefer WAITING_ON_EP from either source.
        if json_status == "WAITING_ON_EP" or md_status == "WAITING_ON_EP":
            return "WAITING_ON_EP"
        return json_status or md_status

    return md_status


def find_waiting_runs() -> list[Path]:
    waiting = []
    if not RUNS_DIR.exists():
        return waiting
    for run_dir in RUNS_DIR.iterdir():
        if not run_dir.is_dir():
            continue
        if run_status(run_dir) == "WAITING_ON_EP":
            waiting.append(run_dir)
    return waiting


def extract_run_id(content: str, footer_text: str = "") -> str | None:
    m = re.search(r"run:([\w\-]+)", content)
    if m:
        return m.group(1)
    m = re.search(r"run:([\w\-]+)", footer_text)
    if m:
        return m.group(1)
    return None


def sync_state_md_status(run_dir: Path, status: str) -> None:
    state_md = run_dir / "state.md"
    if not state_md.exists():
        return
    text = state_md.read_text()
    new_text = re.sub(r"\*\*Status:\*\* \S+", f"**Status:** {status}", text, count=1)
    if new_text != text:
        state_md.write_text(new_text)


def load_run_state(run_dir: Path) -> dict:
    state_json = run_dir / "state.json"
    if state_json.exists():
        return json.loads(state_json.read_text())
    return {}


def save_run_state(run_dir: Path, state: dict) -> None:
    state["updated"] = datetime.now(timezone.utc).isoformat()
    (run_dir / "state.json").write_text(json.dumps(state, indent=2))


def clear_dispatch_lock(run_dir: Path) -> None:
    state = load_run_state(run_dir)
    if not state:
        return
    state.pop("dispatch_in_flight", None)
    state.pop("dispatch_source", None)
    state.pop("dispatch_started", None)
    save_run_state(run_dir, state)


def dispatch_in_flight(run_dir: Path) -> bool:
    return bool(load_run_state(run_dir).get("dispatch_in_flight"))


def record_ep_reply(run_dir: Path, content: str, message_id: str) -> bool:
    """Record EP reply. Returns True when loop continue should be dispatched."""
    if dispatch_in_flight(run_dir):
        print(f"Dispatch already in flight for {run_dir.name}, skipping", file=sys.stderr)
        return False

    state = load_run_state(run_dir)
    if state.get("last_discord_message_id") == message_id:
        return False

    if run_status(run_dir) != "WAITING_ON_EP":
        print(f"Run {run_dir.name} is not WAITING_ON_EP, skipping", file=sys.stderr)
        return False

    log = run_dir / "grilling-log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    entry = f"\n| EP (Discord) | {ts} | {content.strip()} |\n"
    if log.exists():
        log.write_text(log.read_text() + entry)
    else:
        log.write_text(f"# Grilling log\n\n| Source | Time | Answer |\n|--------|------|--------|\n{entry}")

    state["status"] = "RUNNING"
    state["ep_reply"] = content.strip()
    state["last_discord_message_id"] = message_id
    state["dispatch_in_flight"] = True
    state["dispatch_source"] = "discord"
    state["dispatch_started"] = datetime.now(timezone.utc).isoformat()
    save_run_state(run_dir, state)
    sync_state_md_status(run_dir, "RUNNING")

    print(f"Recorded EP reply for run {run_dir.name}")
    return True


def _dispatch_event_for_status(status: str | None) -> str:
    if status == "WAITING_ON_EP":
        return "waiting_on_ep"
    if status == "FINISHED":
        return "finished"
    if status == "BLOCKED":
        return "blocked"
    if status == "ERROR":
        return "error"
    return "step_complete"


def spawn_loop_continue(run_id: str, cfg: dict) -> None:
    """Background thread: run `rgs.py loop continue` and notify Discord on result."""
    run_dir = RUNS_DIR / run_id
    loop_id = load_run_state(run_dir).get("loop_id", "unknown")

    def worker() -> None:
        log_line = f"\n=== dispatch {run_id} {datetime.now(timezone.utc).isoformat()} ===\n"
        try:
            post_webhook(
                cfg,
                "step_complete",
                run_id,
                loop_id,
                "Reply received — resuming loop autonomously (this may take 1–3 minutes)…",
            )
            with DISPATCH_LOG.open("a") as logf:
                logf.write(log_line)
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / "rgs.py"), "loop", "continue", run_id],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    timeout=DISPATCH_TIMEOUT,
                    env=os.environ.copy(),
                )
                logf.write(f"exit={proc.returncode}\n")
                if proc.stdout:
                    logf.write("--- stdout ---\n")
                    logf.write(proc.stdout[-8000:])
                    logf.write("\n")
                if proc.stderr:
                    logf.write("--- stderr ---\n")
                    logf.write(proc.stderr[-4000:])
                    logf.write("\n")
            status = run_status(run_dir)
            if proc.returncode == 0:
                tail = "\n".join(proc.stdout.strip().splitlines()[-8:])[:1500]
                event = _dispatch_event_for_status(status)
                if event == "waiting_on_ep":
                    msg = f"Agent turn complete — waiting on you again.\n\n{tail}"
                elif event == "finished":
                    msg = f"Loop finished.\n\n{tail}"
                else:
                    msg = f"Agent turn complete.\n\n{tail}"
                post_webhook(cfg, event, run_id, loop_id, msg)
            else:
                clear_dispatch_lock(run_dir)
                sync_state_md_status(run_dir, "ERROR")
                err = (proc.stderr or proc.stdout or "unknown error").strip()[:500]
                post_webhook(cfg, "error", run_id, loop_id, f"Loop continue failed:\n```\n{err}\n```")
        except subprocess.TimeoutExpired:
            clear_dispatch_lock(run_dir)
            sync_state_md_status(run_dir, "ERROR")
            post_webhook(cfg, "error", run_id, loop_id, "Loop continue timed out after 10 minutes.")
        except Exception as exc:  # noqa: BLE001
            clear_dispatch_lock(run_dir)
            sync_state_md_status(run_dir, "ERROR")
            post_webhook(cfg, "error", run_id, loop_id, f"Dispatch error: {exc}")

    threading.Thread(
        target=worker,
        daemon=True,
        name=f"loop-continue-{run_id}",
    ).start()


def listen_loop(poll_seconds: int = 5) -> None:
    cfg = load_config()
    bot = api_get_me(cfg)
    bot_id = bot["id"]
    last_id: str | None = None
    print(f"Listening as {bot.get('username')} — poll every {poll_seconds}s (auto-dispatch ON, Ctrl+C to stop)")

    while True:
        try:
            messages = api_get_messages(cfg, after=last_id)
            messages.reverse()
            for msg in messages:
                last_id = msg["id"]
                author = msg.get("author", {})
                if author.get("id") == bot_id:
                    continue
                if author.get("bot"):
                    continue

                content = msg.get("content", "").strip()
                if not content:
                    continue

                waiting = find_waiting_runs()
                if not waiting:
                    continue

                run_id = extract_run_id(content)
                run_dir = None
                if run_id:
                    candidate = RUNS_DIR / run_id
                    if candidate.is_dir():
                        run_dir = candidate
                if run_dir is None and len(waiting) == 1:
                    run_dir = waiting[0]

                if run_dir:
                    if record_ep_reply(run_dir, content, msg["id"]):
                        spawn_loop_continue(run_dir.name, cfg)
        except urllib.error.HTTPError as e:
            print(f"Discord API error: {e.code} {e.reason}", file=sys.stderr)
        except Exception as e:
            print(f"Listen error: {e}", file=sys.stderr)

        time.sleep(poll_seconds)


def cmd_notify(args: argparse.Namespace) -> None:
    cfg = load_config()
    post_webhook(cfg, args.event, args.run_id, args.loop or "", args.message or "", args.game or "")


def main() -> None:
    parser = argparse.ArgumentParser(description="Studio Discord bridge")
    sub = parser.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("notify", help="Send webhook notification")
    n.add_argument("--event", required=True)
    n.add_argument("--run-id", required=True)
    n.add_argument("--loop", default="")
    n.add_argument("--message", default="")
    n.add_argument("--game", default="")
    n.set_defaults(func=cmd_notify)

    l = sub.add_parser("listen", help="Poll channel for EP replies")
    l.add_argument("--poll", type=int, default=5)
    l.set_defaults(func=lambda a: listen_loop(a.poll))

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
