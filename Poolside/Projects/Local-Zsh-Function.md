---
source_path: /Users/matthew.fisher/poolsideai/local-zsh-function
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project]
tech_stack: [Zsh, Shell]
related_projects: [Forge, Poolside-Studio, Agents]
---

# Local Zsh Function

Shell tooling and zsh functions for local Poolside development workflows.

## Source
`/Users/matthew.fisher/poolsideai/local-zsh-function`

## Subsystems

- [[Subsystems/Robot-CLI]] — shell functions may wrap CLI discovery
- [[Subsystems/Agent-Loop]] — local tooling supports the agent workflow

## Related Projects

- [[Projects/Forge]] — shell tooling may wrap Bazel/pool CLI commands
- [[Projects/Poolside-Studio]] — may wrap pnpm/robot commands
- [[Projects/Agents]] — tooling for agent interaction

## Patterns

- [[Patterns/Robot-Discovery]] — if it wraps robot commands, follows this pattern

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
