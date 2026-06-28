from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .base import AgentProvider
from .cursor import CursorAgentProvider
from .ollama import OllamaProvider
from .openclaw import OpenClawProvider

ROOT = Path(__file__).resolve().parents[2]
AGENT_CONFIG = ROOT / "studio" / "config" / "agent.local.json"
AGENT_EXAMPLE = ROOT / "studio" / "config" / "agent.example.json"

PROVIDER_CLASSES: dict[str, type[AgentProvider]] = {
    "cursor": CursorAgentProvider,
    "ollama": OllamaProvider,
    "openclaw": OpenClawProvider,
}


def load_agent_config() -> dict[str, Any]:
    path = AGENT_CONFIG if AGENT_CONFIG.exists() else AGENT_EXAMPLE
    if not path.exists():
        return {"default_provider": "cursor", "providers": {}}
    return json.loads(path.read_text())


def list_providers() -> list[str]:
    return sorted(PROVIDER_CLASSES.keys())


def get_provider(name: str | None = None) -> AgentProvider:
    cfg = load_agent_config()
    provider_name = (name or cfg.get("default_provider", "cursor")).lower()
    if provider_name not in PROVIDER_CLASSES:
        raise ValueError(
            f"Unknown agent provider: {provider_name!r}. "
            f"Available: {', '.join(list_providers())}"
        )
    provider_cfg = cfg.get("providers", {}).get(provider_name, {})
    return PROVIDER_CLASSES[provider_name](provider_cfg)
