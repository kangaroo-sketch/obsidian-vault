---
date: 2024-06-18
status: accepted
tags: [decision]
related_projects: [Poolside-Studio]
related_subsystems: [MCP-Bridge, ACP-Runtime, Robot-CLI]
related_patterns: [Layer-Isolation, Parse-at-Boundaries]
---

# DR-0005: HTTP (Streamable HTTP) for the App Bridge MCP Server

## Context

Poolside Studio needs to expose app-owned capabilities (skills, tasks, session context) to ACP agent runtimes via MCP. MCP supports two transports: stdio (required by ACP) and HTTP (optional). The question is how to run the bridge server.

## Decision

Use **Streamable HTTP MCP** bound to `127.0.0.1` inside Electron main. Not stdio. Not a separate proxy process.

## Rationale

- Simpler than adding a separate proxy subprocess for the bridge
- Better fit for a long-lived, app-owned API (skills, tasks) with rich session state
- Electron main owns app state directly — no IPC round-trip to a proxy
- Per-session bearer tokens are trivial with HTTP headers; harder with stdio
- Agents that don't support HTTP MCP (`agentCapabilities.mcpCapabilities.http !== true`) gracefully get no bridge rather than a broken connection
- ACP already requires stdio MCP for the runtime channel — the bridge uses a distinct transport

## Consequences

- Bridge is local-only; security relies on `127.0.0.1` binding + bearer token + Origin validation
- Robot mode discovery publishes the MCP URL + token so CLI tools can connect without a renderer
- Pi sessions don't receive the bridge (Pi uses its own RPC adapter, not the ACP session path)
- [[Patterns/Layer-Isolation]] is enforced: `electron/mcp/` cannot call `electron/acp/` directly

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — the HTTP bridge is documented in full here
- [[Subsystems/Robot-CLI]] — robot mode relies on the HTTP discovery mechanism
- [[Subsystems/Skill-System]] — skills are exposed via this bridge

## Related Patterns

- [[Patterns/Parse-at-Boundaries]] — MCP tool schemas validate payloads via `inputSchema`
- [[Patterns/Draft-First-Mutations]] — skill mutations go through the bridge as drafts

## Related Projects

- [[Projects/Poolside-Studio]] — the decision applies here
- [[Projects/Forge]] — Pool's ACP server receives the bridge URL in session/new payloads
