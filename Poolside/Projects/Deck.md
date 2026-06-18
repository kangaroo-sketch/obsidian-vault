---
source_path: /Users/matthew.fisher/poolsideai/deck
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project, codebase]
tech_stack: [Go, Kubernetes, Docker, Helm]
related_projects: [Forge, Poolside-Studio]
---

# Deck

Kubernetes-based agent execution platform. Provides custom CRDs (`Agent`, `ModelProvider`, `ModelSelector`, `AgentRun`) so agent runs can be declared in YAML, scheduled by a controller, and executed in isolated pods.

## Source
`/Users/matthew.fisher/poolsideai/deck`

## Key Subsystems Used

- [[Subsystems/ACP-Runtime]] — Deck pods can run ACP-compatible agent containers
- [[Subsystems/Build-System]] — standard Go modules + Makefile + Helm charts

## Custom Resource Definitions

| CRD | Purpose |
|-----|---------|
| `ModelProvider` | LLM provider credentials and endpoint |
| `ModelSelector` | Routes requests across providers with weights/fallback |
| `Agent` | Agent definition: model selector + runtime image |
| `AgentRun` | Single execution: input, tools, output, status |

## Built-in Tool Handlers (Router)

`_done` · `_fail` · `_handoff` · `_clarify` · `_spawn` · `_emit_event`  
`_write_state` · `_read_state` · `_rag_search` · `_rag_ingest` · `_memory_store`

## Implementation Status

- **P0 — Foundation**: complete (controllers, SA token, model resolution)
- **P1 — Core Execution**: TODO (tool dispatch, guardrails, spend tracking, callbacks)
- **P2 — Advanced**: TODO (warm pools, DAG workflows, split-pod topology, RAG)

See `PLAN.md` for full task breakdown.

## Key Files

- `PLAN.md` — implementation roadmap with P0/P1/P2 tasks
- `BUILD_SPEC.md` — build specifications
- `charts/` — Helm charts for Kubernetes deployment
- `cmd/` — CLI commands
- `internal/` — Go controller logic

## Decisions

- [[Decisions/DR-0004-K8s-Agent-Execution]] — why Kubernetes CRDs for agent execution

## Related Projects

- [[Projects/Forge]] — ACP runtime Deck agents may use; shares Go patterns
- [[Projects/Poolside-Studio]] — potential future integration for Deck-backed sessions

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
