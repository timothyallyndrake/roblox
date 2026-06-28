from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class AgentResult:
    """Normalized result from any agent provider."""

    ok: bool
    text: str
    session_id: str | None = None
    provider: str = ""
    raw: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class AgentProvider(ABC):
    """Backend that runs an autonomous agent turn (Cursor CLI, Ollama, OpenClaw, …)."""

    name: str

    @abstractmethod
    def dispatch(
        self,
        prompt: str,
        *,
        cwd: Path,
        session_id: str | None = None,
        model: str | None = None,
    ) -> AgentResult:
        """Run one agent turn. Return normalized result."""

    @abstractmethod
    def health(self) -> tuple[bool, str]:
        """Return (healthy, message) for status checks."""
