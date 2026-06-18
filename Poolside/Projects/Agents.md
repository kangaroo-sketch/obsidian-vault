---
source_path: /Users/matthew.fisher/poolsideai/agents
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project]
tech_stack: []
related_projects: [Forge, Poolside-Studio, Deck]
---

# Agents

Agent framework and experimental agent tooling.

## Source
`/Users/matthew.fisher/poolsideai/agents`

## Key Subsystems Used

- [[Subsystems/ACP-Runtime]] — agents communicate via ACP
- [[Subsystems/Agent-Loop]] — agent development follows this workflow

## Related Projects

- [[Projects/Forge]] — ACP runtime implementation
- [[Projects/Poolside-Studio]] — Studio runs agents via ACP
- [[Projects/Deck]] — Kubernetes platform for running agents at scale

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
