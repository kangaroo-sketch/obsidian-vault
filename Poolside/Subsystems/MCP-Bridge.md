---
tags: [subsystem, protocol]
related_projects: [Poolside-Studio, Forge]
key_decisions: [DR-0005-HTTP-MCP-Bridge]
key_patterns: [Parse-at-Boundaries, Draft-First-Mutations, Layer-Isolation]
---

# MCP Bridge

A localhost Streamable HTTP MCP server running inside Electron main. Exposes app-owned capabilities (skills, tasks, session context, git tools) to ACP agents via per-session bearer tokens.

## Projects

- [[Projects/Poolside-Studio]] — owns and runs the bridge inside `electron/mcp/`
- [[Projects/Forge]] — `pool acp` connects to it as an MCP client during sessions

## How It Works

```
Renderer (Svelte)
  └── IPC ──▶ Electron Main
                └── MCP HTTP server (127.0.0.1:<port>)
                      ├── bearer token per ACP session
                      └── tools: skills, tasks, context, git, observability
                            ▲
                    ACP Agent Runtime calls MCP tools over HTTP
```

## Tool Surface

| Domain | Key Tools |
|--------|-----------|
| Session | `get_app_session_context`, `get_agent_startup_context` |
| Skills | `list_skills`, `get_skill`, `create_skill`, `update_skill` |
| Tasks | `list_tasks`, `run_task`, `create_task`, `list_task_runs` |
| Memory | `manage_memory` |
| Attachments | `extract_attachment_text` |
| Observability (dev) | `get_build_output`, `get_test_results`, `get_app_logs` |
| Repository (dev) | `get_git_diff`, `create_pull_request`, `post_pr_review` |
| Meta | `search_tools` |

## Key Source Locations

- `electron/mcp/http-server.ts` — StreamableHTTP MCP server
- `electron/mcp/app-bridge-service.ts` — bridge session lifecycle
- `electron/mcp/domains/` — tool registrations by domain

## Related Subsystems

- [[Subsystems/ACP-Runtime]] — agents connect to MCP bridge after ACP session/new
- [[Subsystems/Robot-CLI]] — robot mode uses a dedicated MCP bridge session
- [[Subsystems/Skill-System]] — skills are listed/created/updated via bridge tools

## Related Patterns

- [[Patterns/Parse-at-Boundaries]] — MCP tool inputs validated via MCP SDK inputSchema
- [[Patterns/Draft-First-Mutations]] — agent skill writes go through draft approval
- [[Patterns/Layer-Isolation]] — bridge cannot talk directly to ACP runtime manager

## Decisions

- [[Decisions/DR-0005-HTTP-MCP-Bridge]] — why HTTP over stdio for the app bridge

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
