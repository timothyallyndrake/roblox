from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from .base import AgentProvider, AgentResult


class CursorAgentProvider(AgentProvider):
    """Cursor `agent` CLI — default RGS backend."""

    name = "cursor"

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        cfg = config or {}
        self.command = cfg.get("command", "agent")
        self.model = cfg.get("model")
        self.flags: list[str] = cfg.get(
            "flags",
            ["-p", "--trust", "--force", "--output-format", "json"],
        )

    def _resolve_command(self) -> list[str]:
        if Path(self.command).exists():
            return [self.command]
        found = shutil.which(self.command)
        if not found:
            raise FileNotFoundError(
                f"Cursor agent CLI not found: {self.command!r}. "
                "Install Cursor Agent or set providers.cursor.command in agent.local.json"
            )
        return [found]

    def dispatch(
        self,
        prompt: str,
        *,
        cwd: Path,
        session_id: str | None = None,
        model: str | None = None,
    ) -> AgentResult:
        cmd = self._resolve_command()
        cmd.extend(self.flags)
        cmd.extend(["--workspace", str(cwd.resolve())])
        use_model = model or self.model
        if use_model:
            cmd.extend(["--model", use_model])
        if session_id:
            cmd.extend(["--resume", session_id])
        cmd.append(prompt)

        try:
            proc = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=3600,
            )
        except subprocess.TimeoutExpired:
            return AgentResult(
                ok=False,
                text="",
                provider=self.name,
                error="agent timed out after 3600s",
            )
        except FileNotFoundError as exc:
            return AgentResult(ok=False, text="", provider=self.name, error=str(exc))

        stdout = proc.stdout.strip()
        stderr = proc.stderr.strip()

        if not stdout:
            return AgentResult(
                ok=False,
                text=stderr,
                provider=self.name,
                error=f"agent exited {proc.returncode} with no stdout",
            )

        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError:
            return AgentResult(
                ok=proc.returncode == 0,
                text=stdout,
                provider=self.name,
                raw={"stdout": stdout, "stderr": stderr, "returncode": proc.returncode},
                error=None if proc.returncode == 0 else stderr or "non-json agent output",
            )

        is_error = payload.get("is_error", proc.returncode != 0)
        result_text = payload.get("result", stdout)
        sid = payload.get("session_id")

        return AgentResult(
            ok=not is_error and proc.returncode == 0,
            text=result_text if isinstance(result_text, str) else json.dumps(result_text),
            session_id=sid,
            provider=self.name,
            raw=payload,
            error=None if not is_error else (stderr or "agent reported error"),
        )

    def health(self) -> tuple[bool, str]:
        try:
            cmd = self._resolve_command() + ["--version"]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if proc.returncode == 0:
                version = proc.stdout.strip() or proc.stderr.strip() or "ok"
                return True, f"cursor agent: {version}"
            return False, proc.stderr.strip() or f"exit {proc.returncode}"
        except Exception as exc:  # noqa: BLE001
            return False, str(exc)
