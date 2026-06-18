---
tags: [subsystem, tooling]
related_projects: [Poolside-Studio, Forge]
key_decisions: [DR-0006-Robot-Discovery]
key_patterns: [Robot-Discovery]
---

# Robot CLI

`pnpm robot` — a standalone CLI for external agents and scripts to inspect a running Poolside Studio instance over the app-bridge MCP surface without a renderer UI.

## Projects

- [[Projects/Poolside-Studio]] — owns the robot CLI (`scripts/robot.mjs`, `pnpm robot`)
- [[Projects/Forge]] — `pool acp logs` / `pool acp` are the runtime counterpart

## How It Works

```
pnpm robot <command>
  └── discovers running Studio via:
        1. --discovery <path> or POOLSIDE_ROBOT_DISCOVERY env var
        2. .poolside-studio/agent-instance.json in cwd
        3. default app profile paths
  └── connects to MCP bridge with robot-profile bearer token
  └── calls bridge tools and prints results (--json for scripts)
```

Robot sessions automatically receive the **developer diagnostics profile** — full access to health, logs, runtime status, git diff, and `gh` tools without needing `POOLSIDE_APP_BRIDGE_DEV_TOOLS=1`.

## Key Commands

| Command | Description |
|---------|-------------|
| `health` | Build/test/runtime/git summary |
| `logs` | Tail app logs for current workspace |
| `runtime` | ACP runtime status and MCP port |
| `diff` | Git diff vs base ref |
| `session state` | Latest session switch state |
| `tools search <q>` | Search offline MCP tool catalog |
| `pi doctor` | Read-only Pi runtime diagnosis |
| `startup` | Agent startup context (falls back to static) |

## Key Source Locations

- `scripts/robot.mjs` — CLI entry point
- `.poolside-studio/agent-instance.json` — workspace discovery pointer
- `electron/mcp/app-bridge-service.ts` — robot session provisioning

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — robot CLI connects to this bridge
- [[Subsystems/ACP-Runtime]] — robot can inspect ACP session state

## Related Patterns

- [[Patterns/Robot-Discovery]] — how the CLI finds a running Studio instance

## Decisions

- [[Decisions/DR-0006-Robot-Discovery]] — workspace-scoped discovery design

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
