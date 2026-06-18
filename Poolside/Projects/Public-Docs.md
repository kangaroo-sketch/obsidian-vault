---
source_path: /Users/matthew.fisher/poolsideai/public-docs
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project, documentation]
tech_stack: [Mintlify, MDX, Node.js, Docker, Caddy]
related_projects: [Forge, Poolside-Studio, Deck]
---

# Public Docs

Source for `docs.poolside.ai` — the Mintlify-hosted public documentation covering the Poolside platform: Console, API, CLI, IDE integration, skills, MCP servers, and agent orchestration.

## Source
`/Users/matthew.fisher/poolsideai/public-docs`

## Key Subsystems Used

- [[Subsystems/Skill-System]] — docs cover the skill authoring format and Console skill import
- [[Subsystems/ACP-Runtime]] — agent instructions and ACP integration guides live here

## What's Documented

| Section | Content |
|---------|---------|
| `get-started/` | Quickstart guides |
| `api/` | REST API reference |
| `cli/` | `pool` CLI reference |
| `console/` | Poolside Console (web UI) |
| `ide/` | VS Code / JetBrains / Zed integration |
| `skills.mdx` | Skill authoring and management |
| `mcp-servers.mdx` | MCP server configuration |
| `orchestration/` | Multi-agent orchestration |
| `deployment/` | Self-hosted deployment guides |
| `release-notes/` | Changelog |

## How the Site is Built

```bash
npm i -g mint
mint dev        # local preview
mint export     # production build → Docker image (Caddyfile serves at /docs/*)
```

The `Dockerfile` runs `mint export` and the `build/rewrite-*.js` scripts patch asset paths for the `/docs` subpath. `Caddyfile` serves the static output.

## Key Files

- `docs.json` — Mintlify site configuration and navigation
- `AGENTS.md` — agent workflow guide for doc PRs
- `CONTRIBUTING.md` — PR process, branching, release flow
- `Dockerfile` / `Caddyfile` — production packaging

## Related Projects

- [[Projects/Forge]] — REST API, CLI, and infrastructure docs sourced from Forge
- [[Projects/Poolside-Studio]] — IDE and Studio documentation
- [[Projects/Deck]] — agent orchestration documentation

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
