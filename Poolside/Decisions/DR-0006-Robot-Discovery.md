---
date: 2024-06-18
status: accepted
tags: [decision]
related_projects: [Poolside-Studio]
related_subsystems: [Robot-CLI, MCP-Bridge, Agent-Loop]
related_patterns: [Robot-Discovery]
---

# DR-0006: Workspace-Scoped Robot Discovery

## Context

Developers run multiple Poolside Studio instances simultaneously — a primary dev window, agent-controlled windows, and git worktree windows. `pnpm robot` and `pnpm agent-loop` need to reliably find the *right* running instance for the current repository checkout without hardcoded ports or global state.

## Decision

The running app publishes a **workspace-scoped identity file** at `.poolside-studio/agent-instance.json`. CLI tools discover the right instance by walking up from cwd and matching `instanceRoot` to the current workspace path. Validate with Zod and check PID liveness before use.

## Rationale

- No port collisions: each instance uses a randomly assigned port, published in the discovery file
- Workspace-scoped: the CLI automatically targets the instance for the current checkout, not a random one
- Liveness check: stale files from crashed instances are detected and skipped
- Fallback chain: explicit env var → cwd walk → default app profile paths ensures both dev and CI work
- Security: discovery file stored in app userData (`0600` permissions); never in the workspace root where agents could read it

## Consequences

- App must write and clean up `.poolside-studio/agent-instance.json` on start/stop
- Stale lock files (`dev-agent.lock`) fail closed rather than silently treating them as "no lock"
- `pnpm dev` and `pnpm dev:agent` both publish the same identity contract — no special-casing in robot CLI
- [[Patterns/Robot-Discovery]] documents the algorithm for reuse

## Related Subsystems

- [[Subsystems/Robot-CLI]] — implements this discovery algorithm
- [[Subsystems/MCP-Bridge]] — robot connects to the bridge via discovered URL/token
- [[Subsystems/Agent-Loop]] — agent-loop uses the same discovery for workspace verification

## Related Patterns

- [[Patterns/Layer-Isolation]] — discovery lives outside the renderer, in Electron main only

## Related Projects

- [[Projects/Poolside-Studio]] — the decision applies here
- [[Projects/Forge]] — analogous workspace scoping in Bazel targets
