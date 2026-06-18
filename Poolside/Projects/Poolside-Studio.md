---
source_path: /Users/matthew.fisher/poolsideai/poolside-studio
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project, codebase]
tech_stack: [TypeScript, Svelte, Electron, Vite, Vitest]
related_projects: [Forge, Deck, Public-Docs]
---

# Poolside Studio

Electron desktop client for ACP agent runtimes. Spawns `pool acp` (or Goose/Hermes/Pi) as a subprocess, runs a localhost MCP bridge server, and provides a Svelte UI for chat, skills, tasks, and connectors.

## Source
`/Users/matthew.fisher/poolsideai/poolside-studio`

## Key Subsystems Used

- [[Subsystems/ACP-Runtime]] — Studio is the ACP *client*; spawns `pool acp`, `goose acp`
- [[Subsystems/MCP-Bridge]] — Studio *owns* the MCP HTTP bridge in `electron/mcp/`
- [[Subsystems/Robot-CLI]] — `pnpm robot` inspects Studio from the CLI
- [[Subsystems/Skill-System]] — Studio manages skills and injects them into ACP sessions
- [[Subsystems/Agent-Loop]] — `pnpm agent-loop` is the canonical dev workflow for this repo
- [[Subsystems/Build-System]] — Vite 8, pnpm, Turborepo, Electron Builder

## Architecture Layers

```
Renderer (Svelte 5 + Vite)  src/features/*, src/lib/*
  ↕ IPC (preload.ts)
Electron Main (Node.js)     electron/acp/, electron/mcp/, electron/db/
  ↕ stdio / HTTP
Agent Runtime               pool acp | goose acp | pi --mode rpc
```

## Feature Modules (`src/features/`)

`chat` · `connectors` · `feedback` · `memory` · `projects` · `setup` · `skills` · `tasks` · `terminals` · `trajectory`

## Key Files

- `README.md` — setup, commands, packaging, troubleshooting
- `AGENTS.md` — agent workflow guide for this repo
- `ACP.md` — ACP protocol, session flow, troubleshooting
- `docs/architecture.md` — layer diagram and dependency rules
- `docs/golden-principles.md` — ESLint-enforced coding rules

## Patterns Applied

- [[Patterns/Layer-Isolation]] — strict Electron/renderer/feature import boundaries
- [[Patterns/Service-Class]] — every Electron module is a typed service class
- [[Patterns/Feature-Communication]] — features share state via `src/lib/`, not direct imports
- [[Patterns/Parse-at-Boundaries]] — Zod at IPC, MCP, DB, and ACP entry points
- [[Patterns/Draft-First-Mutations]] — agent skill writes go through user approval
- [[Patterns/Robot-Discovery]] — workspace-scoped `.poolside-studio/agent-instance.json`

## Decisions

- [[Decisions/DR-0001-Electron-Svelte]] — why Electron + Vite + Svelte 5
- [[Decisions/DR-0002-ACP-Protocol]] — Studio implements the ACP client
- [[Decisions/DR-0005-HTTP-MCP-Bridge]] — HTTP over stdio for the app bridge
- [[Decisions/DR-0006-Robot-Discovery]] — workspace-scoped CLI discovery

## Related Projects

- [[Projects/Forge]] — provides the `pool acp` binary Studio bundles
- [[Projects/Deck]] — potential future agent execution backend
- [[Projects/Public-Docs]] — Studio is documented at docs.poolside.ai

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
