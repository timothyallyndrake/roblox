"""Pluggable agent backends for RGS orchestration."""

from .base import AgentProvider, AgentResult
from .factory import get_provider, list_providers

__all__ = ["AgentProvider", "AgentResult", "get_provider", "list_providers"]
