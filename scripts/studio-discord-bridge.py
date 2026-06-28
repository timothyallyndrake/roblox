#!/usr/bin/env python3
"""
Studio Discord bridge — bidirectional loop communication.

Outbound: webhook embeds (step complete, waiting on EP, finished)
Inbound:  bot polls channel for EP replies when a run is WAITING_ON_EP

Setup:
  cp studio/loops/config/config.example.json studio/loops/config/local.json
  # Fill in webhook URL, bot token, channel ID (never commit local.json)

Usage:
  python3 scripts/studio-discord-bridge.py notify --event waiting_on_ep --run-id ID --loop discovery.game-ideas --message "Question here"
  python3 scripts/studio-discord-bridge.py listen   # poll for EP replies (run in background during loops)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "studio" / "loops" / "config" / "local.json"
RUNS_DIR = ROOT / "studio" / "loops" / "runs"

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
            "\n\n_Reply in this channel to answer. Start with "
            f"`run:{run_id}` or reply to this message._"
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
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        resp.read()
    print(f"Discord webhook sent ({event})")


def api_get_messages(cfg: dict, after: str | None = None) -> list:
    token = cfg.get("discord_bot_token", "")
    channel = cfg.get("discord_channel_id", "")
    if not token or "REPLACE_ME" in token:
        return []

    url = f"https://discord.com/api/v10/channels/{channel}/messages?limit=10"
    if after:
        url += f"&after={after}"

    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bot {token}"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def api_get_me(cfg: dict) -> dict:
    token = cfg.get("discord_bot_token", "")
    req = urllib.request.Request(
        "https://discord.com/api/v10/users/@me",
        headers={"Authorization": f"Bot {token}"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def find_waiting_runs() -> list[Path]:
    waiting = []
    if not RUNS_DIR.exists():
        return waiting
    for run_dir in RUNS_DIR.iterdir():
        if not run_dir.is_dir():
            continue
        state_json = run_dir / "state.json"
        if state_json.exists():
            state = json.loads(state_json.read_text())
            if state.get("status") == "WAITING_ON_EP":
                waiting.append(run_dir)
        else:
            state_md = run_dir / "state.md"
            if state_md.exists() and "WAITING_ON_EP" in state_md.read_text():
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


def record_ep_reply(run_dir: Path, content: str) -> None:
    log = run_dir / "grilling-log.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    entry = f"\n| EP (Discord) | {ts} | {content.strip()} |\n"
    if log.exists():
        log.write_text(log.read_text() + entry)
    else:
        log.write_text(f"# Grilling log\n\n| Source | Time | Answer |\n|--------|------|--------|\n{entry}")

    state_json = run_dir / "state.json"
    if state_json.exists():
        state = json.loads(state_json.read_text())
        state["status"] = "RUNNING"
        state["ep_reply"] = content.strip()
        state["updated"] = ts
        state_json.write_text(json.dumps(state, indent=2))

    state_md = run_dir / "state.md"
    if state_md.exists():
        text = state_md.read_text()
        text = text.replace("WAITING_ON_EP", "RUNNING")
        state_md.write_text(text)

    print(f"Recorded EP reply for run {run_dir.name}")


def listen_loop(poll_seconds: int = 5) -> None:
    cfg = load_config()
    bot = api_get_me(cfg)
    bot_id = bot["id"]
    last_id: str | None = None
    print(f"Listening as {bot.get('username')} — poll every {poll_seconds}s (Ctrl+C to stop)")

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
                    record_ep_reply(run_dir, content)
                    post_webhook(
                        cfg,
                        "step_complete",
                        run_dir.name,
                        "discord-bridge",
                        f"EP reply recorded: {content[:200]}",
                    )
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
