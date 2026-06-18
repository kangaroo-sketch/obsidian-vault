---
tags: [subsystem, feature]
related_projects: [Poolside-Studio, Public-Docs, Forge]
key_decisions: [DR-0001-Electron-Svelte]
key_patterns: [Draft-First-Mutations]
---

# Skill System

Skills are reusable prompt packages that agents load into session context. They can be created by users, imported from Poolside Console repositories, or drafted by agents via the MCP bridge.

## Projects

- [[Projects/Poolside-Studio]] — owns skill storage, UI, and MCP tools
- [[Projects/Public-Docs]] — documents the skill authoring format and Console integration
- [[Projects/Forge]] — `pool acp` runtime receives skill context injected by Studio

## How It Works

```
User activates skills in UI
  └── src/lib/skills → updates selectedSkillIds in session state
        └── IPC: updateBridgeSession
              └── electron/mcp/app-bridge-service.ts stores selection
                    └── ACP agent: next get_app_session_context reflects skills
                          └── buildSkillContextPrompt injects markdown into turn
```

## Skill Sources

| Source | Storage Location |
|--------|-----------------|
| User-created | Local filesystem, Studio-managed |
| Poolside Console | `~/.config/poolside-studio/console-skills/<repo>/<skill>/` |
| Agent-drafted | Drafts pending user approval |

## Key Source Locations

- `src/lib/skills/skill-library.ts` — core skill logic
- `src/lib/skills/skill-mirror.ts` — Node-compatible mirror (used by Electron main)
- `electron/mcp/domains/` — `list_skills`, `get_skill`, `create_skill`, `update_skill` tools
- `electron/console/` — Poolside Console REST client for importing skills

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — agents interact with skills via bridge tools
- [[Subsystems/ACP-Runtime]] — skills injected into ACP session context at prompt time

## Related Patterns

- [[Patterns/Draft-First-Mutations]] — agent skill writes are drafts until user approves

## Decisions

- [[Decisions/DR-0001-Electron-Svelte]] — Electron enables Node-compatible skill mirror shared between main and renderer

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
