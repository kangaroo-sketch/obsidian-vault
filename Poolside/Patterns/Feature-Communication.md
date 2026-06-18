---
tags: [pattern]
projects_using: [Poolside-Studio]
subsystems_using: [MCP-Bridge, Robot-CLI, Skill-System, ACP-Runtime]
---

# Feature Communication

Renderer features (chat, skills, tasks, connectors, etc.) must not import directly from each other. They communicate through three explicit channels: shared stores in `src/lib/`, IPC via `src/lib/desktop/`, or URL/navigation state.

## Problem

Direct feature-to-feature imports create invisible coupling. Changing one feature breaks another. Features become impossible to develop or test independently.

## Solution

```
src/features/chat     ←─── NO DIRECT IMPORT ───→ src/features/skills
       │                                                  │
       └──── shared store (src/lib/skills) ────────────┘
       │                                                  │
       └──── IPC (src/lib/desktop/) ────────────────────┘
```

## Channels

| Channel | When to Use |
|---------|-------------|
| `src/lib/` shared store | Reactive state one feature reads from another |
| IPC via `src/lib/desktop/` | Calling Electron main from renderer |
| URL / navigation state | Navigating between feature views |

## Where Applied

All features in [[Projects/Poolside-Studio]]:
- `src/features/chat` — reads skill state via `src/lib/skills`
- `src/features/skills` — reads project state via `src/lib/projects`
- `src/features/tasks` — invokes MCP tools via IPC bridge, not direct import

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — bridge is reached via IPC from renderer
- [[Subsystems/Skill-System]] — skills are read/written via shared stores
- [[Subsystems/Robot-CLI]] — robot discovery avoids cross-feature coupling
- [[Subsystems/ACP-Runtime]] — chat sends to runtime via IPC, not direct import

## Related Patterns

- [[Patterns/Layer-Isolation]] — renderer-side specialization
- [[Patterns/Draft-First-Mutations]] — skill changes flow through chat → shared state → IPC

## Tradeoffs

- **Cost**: Must extract shared logic to `src/lib/` even for small utilities
- **Benefit**: Features are independently deployable units; clean dependency graph; easier to refactor

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
