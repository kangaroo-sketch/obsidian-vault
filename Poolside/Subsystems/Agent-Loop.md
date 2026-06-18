---
tags: [subsystem, workflow]
related_projects: [Poolside-Studio, Forge]
key_decisions: [DR-0001-Electron-Svelte]
key_patterns: [Robot-Discovery]
---

# Agent Development Loop

The canonical workflow for making code changes with an AI agent: `worktree → agent → verify → review → PR`. Owned primarily by Poolside Studio's scripts but used across both Forge and Studio development.

## Projects

- [[Projects/Poolside-Studio]] — `pnpm agent-loop` script, worktree management, review agent
- [[Projects/Forge]] — same loop pattern applies; uses Bazel instead of pnpm verify

## The Loop

```
1. pnpm agent-loop --task "description"
      └── creates isolated git worktree
      └── installs deps, writes agent-bootstrap.md

2. Run agent (Pool, Claude Code, Codex, Goose) in worktree

3. pnpm agent-loop --continue --worktree <path>
      └── runs pnpm verify:agent (harness ratchets, lint, typecheck, tests)
      └── agent-to-agent review vs golden-principles
      └── opens PR if review approves
```

## Key Commands

```bash
pnpm agent-loop --task "add rate limiting to the MCP bridge"
pnpm agent-loop --continue --worktree <path>
pnpm agent-loop --verify-only
pnpm agent-loop --status --json
pnpm review-agent --base main
pnpm agent:doctor
```

## Key Source Locations

- `scripts/agent-loop.mjs` — main orchestration script
- `scripts/review-agent.mjs` — agent-to-agent review
- `.poolside-studio/agent-bootstrap.md` — per-worktree context file
- `docs/workflows/agent-dev-loop.md` — full documentation

## Related Subsystems

- [[Subsystems/Robot-CLI]] — `pnpm robot` inspects the running app during agent work
- [[Subsystems/MCP-Bridge]] — in-app agents use the bridge during sessions
- [[Subsystems/Build-System]] — verify step runs the build system

## Related Patterns

- [[Patterns/Robot-Discovery]] — agent-loop uses workspace-scoped discovery

## Decisions

- [[Decisions/DR-0001-Electron-Svelte]] — Studio architecture enables headless task runner for unattended agent sessions

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
