---
tags: [subsystem, protocol]
related_projects: [Forge, Poolside-Studio, Deck]
key_decisions: [DR-0002-ACP-Protocol, DR-0004-K8s-Agent-Execution]
key_patterns: [Parse-at-Boundaries]
---

# ACP Runtime

Agent Communication Protocol — Poolside's standard for agent communication over stdio. `pool acp` is the server process; Poolside Studio is the client. Communication happens over stdin/stdout pipes using the `@agentclientprotocol/sdk` TypeScript SDK.

## Projects

- [[Projects/Forge]] — implements the `pool acp` server (`cmd/pool/acp_cmd.go`)
- [[Projects/Poolside-Studio]] — runs as the ACP client in Electron main process
- [[Projects/Deck]] — planned to execute ACP-compatible agents in Kubernetes pods

## How It Works

```
Poolside Studio (Electron)
  └── spawns ──▶ pool acp (subprocess)
                   ├── stdin/stdout pipes (ACP protocol)
                   ├── session/new → session/prompt → session updates
                   └── debug logs → /tmp/pool-acp-debug.log
```

Runtimes using ACP: **Pool**, **Goose**, **Hermes**. Pi uses a separate RPC adapter and is not ACP.

## Key Source Locations

**Forge (server side)**
- `cmd/pool/acp_cmd.go` — command entrypoint
- `cmd/pool/acp/acp_agent.go` — agent implementation

**Poolside Studio (client side)**
- `electron/acp/runtime-manager.ts` — subprocess lifecycle
- `src/lib/acp/client.ts` — ACP client callbacks
- `src/lib/acp/transport.ts` — stdio transport
- `src/lib/acp/turn-materializer.ts` — updates → UI events

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — agents call back into Studio via MCP over the ACP session
- [[Subsystems/Robot-CLI]] — inspects ACP sessions from the command line
- [[Subsystems/Skill-System]] — skills are injected into ACP session context

## Related Patterns

- [[Patterns/Parse-at-Boundaries]] — ACP payloads are validated at the Electron IPC boundary

## Decisions

- [[Decisions/DR-0002-ACP-Protocol]] — why ACP over other agent protocols
- [[Decisions/DR-0004-K8s-Agent-Execution]] — how Deck plans to integrate ACP

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
