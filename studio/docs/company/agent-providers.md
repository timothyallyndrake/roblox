# Agent Providers — Pluggable AI Backends

RGS separates **orchestration** (loops, state, staff, Discord) from **agent execution** (who runs the work).

```
EP → /rgs-* skills → scripts/rgs.py → agent_providers/ → Cursor `agent` CLI (default)
                                                      → Ollama (future)
                                                      → OpenClaw (future)
```

## Default: Cursor `agent` CLI

Loop steps dispatch via headless Cursor Agent:

```bash
python3 scripts/rgs.py loop continue [run_id]
```

Under the hood this runs:

```bash
agent -p --trust --force --output-format json \
  --workspace /path/to/roblox \
  [--resume <session_id>] \
  "<loop-continue prompt>"
```

Session IDs are stored in `runs/<run_id>/state.json` → `agent.session_id` for multi-turn loop continuity.

## Configuration

Copy and customize (optional):

```bash
cp studio/config/agent.example.json studio/config/agent.local.json
```

```json
{
  "default_provider": "cursor",
  "providers": {
    "cursor": {
      "command": "agent",
      "model": null,
      "flags": ["-p", "--trust", "--force", "--output-format", "json"]
    }
  }
}
```

`agent.local.json` is gitignored.

## Swap providers

Change `default_provider` in `agent.local.json`:

| Provider | Status | Use case |
|----------|--------|----------|
| `cursor` | **Active** | Cursor Agent CLI (local, full tool access) |
| `ollama` | Stub | Local models, offline dev |
| `openclaw` | Stub | OpenClaw agent runtime |

Override per dispatch:

```bash
python3 scripts/rgs.py loop continue RUN_ID --provider cursor
```

Check health:

```bash
python3 scripts/rgs.py agent status
python3 scripts/rgs.py agent providers
```

## Adding a new provider

1. Create `scripts/agent_providers/<name>.py` implementing `AgentProvider`
2. Register in `scripts/agent_providers/factory.py` → `PROVIDER_CLASSES`
3. Add config block to `studio/config/agent.example.json`
4. Document here

Required interface:

```python
class AgentProvider(ABC):
    name: str

    def dispatch(self, prompt, *, cwd, session_id=None, model=None) -> AgentResult: ...
    def health(self) -> tuple[bool, str]: ...
```

## Architecture principles

| Layer | Responsibility | Swappable? |
|-------|----------------|------------|
| `/rgs-*` skills | EP-facing commands | Skills evolve; CLI stable |
| `scripts/rgs.py` | State, loops, staff, games | No |
| `scripts/rgs_agent.py` | Prompt templates, dispatch | No |
| `scripts/agent_providers/` | Run AI backend | **Yes** |
| Loop manifests | What to do | No |
| Staff skills | How agents behave | No |

Orchestration never imports Cursor-specific APIs directly — only through `AgentProvider`.

## Prompt templates

| Template | Used by |
|----------|---------|
| `studio/templates/agent/loop-continue.prompt.md` | `loop continue` |

Templates use `{{variable}}` placeholders filled by `rgs_agent.py`.

## EP vs headless agent

| Mode | When |
|------|------|
| **Headless** (`loop continue`) | Autonomous loop steps, background runs, Discord-driven workflows |
| **Interactive** (Cursor chat + `/rgs-*`) | EP pairing, creative direction, playtest review |

Both use the same loop state and manifests. Interactive sessions can also call `loop continue` to spawn a separate agent worker.

## Requirements

- Cursor Agent CLI on PATH (`agent --version`)
- `CURSOR_API_KEY` or `agent login` for headless runs
- Repo opened as workspace (`--workspace` points to monorepo root)
