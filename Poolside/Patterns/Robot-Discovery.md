---
tags: [pattern]
projects_using: [Poolside-Studio, Forge]
subsystems_using: [Robot-CLI, ACP-Runtime]
---

# Robot Discovery

CLI tools and external agents locate a running app instance by walking up from the current working directory for a workspace-scoped JSON identity file, rather than relying on hardcoded ports or global config.

## Problem

Multiple Studio instances (dev, agent, worktrees) can run simultaneously. Hardcoded ports cause collisions. Global config can't distinguish which instance belongs to which repository checkout.

## Solution

The running app publishes a discovery file scoped to its workspace. The CLI walks up from cwd to find the right instance automatically.

```
App starts
  └── writes .poolside-studio/agent-instance.json
        └── contains: MCP URL, bearer token, instanceRoot, workspace path

pnpm robot <command>
  └── discovery algorithm:
        1. --discovery <path>  or  POOLSIDE_ROBOT_DISCOVERY
        2. walk up cwd for .poolside-studio/agent-instance.json
        3. default app profile paths
  └── validates: parse with Zod, check PID alive, prefer instanceRoot matching cwd
```

## Discovery File Contents

- MCP server URL and bearer auth headers
- App PID (for liveness check)
- Instance root, kind, and label
- Workspace / project path
- Bridge session ID

## Where Applied

| Tool | Project | Uses Pattern |
|------|---------|-------------|
| `pnpm robot` | [[Projects/Poolside-Studio]] | Primary consumer |
| `pnpm agent-loop` | [[Projects/Poolside-Studio]] | Verifies workspace identity |
| `pool acp logs` | [[Projects/Forge]] | Analogous discovery for ACP debug logs |

## Related Subsystems

- [[Subsystems/Robot-CLI]] — built on this pattern
- [[Subsystems/Agent-Loop]] — uses workspace identity to scope verify and review steps

## Decisions

- [[Decisions/DR-0006-Robot-Discovery]] — detailed rationale for workspace-scoped discovery

## Tradeoffs

- **Cost**: App must write and clean up discovery files; stale files can confuse the CLI
- **Benefit**: Multiple simultaneous instances work correctly; no port collision; repo checkout = correct instance

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
