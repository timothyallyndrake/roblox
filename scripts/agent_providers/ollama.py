from __future__ import annotations

from pathlib import Path
from typing import Any

from .base import AgentProvider, AgentResult


class OllamaProvider(AgentProvider):
    """Future: local Ollama models. Stub — swap provider in agent.local.json when ready."""

    name = "ollama"

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        cfg = config or {}
        self.base_url = cfg.get("base_url", "http://localhost:11434")
        self.model = cfg.get("model", "llama3.2")

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
                "Ollama provider not implemented yet. "
                "See studio/docs/company/agent-providers.md to add it."
            ),
        )

    def health(self) -> tuple[bool, str]:
        return False, "ollama provider stub (not implemented)"
