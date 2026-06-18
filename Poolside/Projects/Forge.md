---
source_path: /Users/matthew.fisher/poolsideai/forge
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project, codebase]
tech_stack: [Go, Bazel, Python, Svelte, TypeScript]
related_projects: [Poolside-Studio, Deck, Public-Docs]
---

# Forge

Poolside's primary monorepo: Go services, Python data pipelines (`pyforge/`), and TypeScript UI packages (`ui/`). Ships the `pool` CLI and the `pool acp` runtime that Poolside Studio uses as its agent backend.

## Source
`/Users/matthew.fisher/poolsideai/forge`

## Key Subsystems Used

- [[Subsystems/ACP-Runtime]] — Forge *implements* the `pool acp` server (`cmd/pool/acp/`)
- [[Subsystems/Build-System]] — Bazel for Go/Python; Turborepo + pnpm for UI
- [[Subsystems/Agent-Loop]] — Forge work follows the same worktree → verify → PR workflow

## Repository Map

| Area | Location |
|------|----------|
| REST API + backend | `pkg/backend/` |
| `pool` CLI + ACP server | `cmd/pool/` |
| Go business logic | `pkg/<name>/` |
| Python pipelines (eval, blender) | `pyforge/` |
| UI apps and packages | `ui/` |
| Infra (Terraform / OpenTofu) | `infra/` |
| K8s releases, Helm, Atlantis | `deploy/kube/releases/` |
| ArgoCD + Kargo promotion | `deploy/argocd/` |
| Developer docs | `doc/` |
| Image publishing | `artifacts/` |

## Key Files

- `README.md` — setup, build, test instructions
- `AGENTS.md` — agent workflow guide for this repo
- `BUILD.bazel` / `MODULE.bazel` — Bazel definitions
- `go.mod` — Go dependencies
- `pyforge/AGENTS.md` — Python pipeline guide

## Decisions

- [[Decisions/DR-0003-Bazel-Monorepo]] — why Bazel for this repo
- [[Decisions/DR-0002-ACP-Protocol]] — Forge implements the ACP server side

## Related Projects

- [[Projects/Poolside-Studio]] — consumes the `pool acp` binary Forge produces
- [[Projects/Deck]] — Deck agents may use ACP; shares Go patterns with Forge
- [[Projects/Public-Docs]] — Forge's `doc/` trees feed into public documentation

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
