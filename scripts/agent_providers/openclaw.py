from __future__ import annotations

from pathlib import Path
from typing import Any

from .base import AgentProvider, AgentResult


class OpenClawProvider(AgentProvider):
    """Future: OpenClaw agent runtime. Stub — swap provider when ready."""

    name = "openclaw"

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        cfg = config or {}
        self.config_path = cfg.get("config_path", "~/.openclaw/config")

    def dispatch(
        self,
        prompt: str,
        *,
        cwd: Path,
        session_id: str | None = None,
        model: str | None = None,
    ) -> AgentResult:
        _ = prompt, cwd, session_id, model
        return AgentResult(
            ok=False,
            text="",
            provider=self.name,
            error=(
                "OpenClaw provider not implemented yet. "
                "See studio/docs/company/agent-providers.md to add it."
            ),
        )

    def health(self) -> tuple[bool, str]:
        return False, "openclaw provider stub (not implemented)"
