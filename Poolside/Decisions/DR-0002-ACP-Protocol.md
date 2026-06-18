---
date: 2024-06-18
status: accepted
tags: [decision]
related_projects: [Forge, Poolside-Studio, Deck]
related_subsystems: [ACP-Runtime, MCP-Bridge]
related_patterns: [Parse-at-Boundaries]
---

# DR-0002: ACP as the Agent Communication Protocol

## Context

Poolside needs a standard protocol for how a desktop client (Studio) and backend tooling (Forge) communicate with AI agent runtimes. Multiple runtimes need to be supported: Pool, Goose, Hermes, and potentially others.

## Decision

Use **ACP (Agent Client Protocol)** over **stdin/stdout** as the standard agent communication protocol. Implement via the `@agentclientprotocol/sdk` TypeScript package on the client side; Go implementation in `cmd/pool/acp/` on the server side.

## Rationale

- stdio transport is simple, process-isolated, and requires no network configuration
- ACP defines standard session operations: `initialize`, `session/new`, `session/load`, `session/prompt`, `session/list`
- Runtimes that support ACP (Pool, Goose, Hermes) can be swapped without Studio code changes
- ACP's `mcpCapabilities.http` flag lets agents opt into the MCP bridge without requiring it
- Pi uses a different RPC adapter but is isolated behind an interface — Studio's chat code is ACP-agnostic at the facade layer

## Consequences

- All runtimes must implement the ACP server contract to work with Studio
- Pi is a special case: it uses `pi --mode rpc` and is adapted via a separate `ACPConnection`-shaped wrapper
- Enables [[Subsystems/MCP-Bridge]] injection by carrying MCP server URL in `session/new` payload
- Requires [[Patterns/Parse-at-Boundaries]] for all incoming ACP payloads

## Related Projects

- [[Projects/Forge]] — implements `pool acp` (server)
- [[Projects/Poolside-Studio]] — implements ACP client in Electron
- [[Projects/Deck]] — planned ACP-compatible agent pods
