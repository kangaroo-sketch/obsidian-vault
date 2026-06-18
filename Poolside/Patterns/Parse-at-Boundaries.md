---
tags: [pattern]
projects_using: [Poolside-Studio, Forge]
subsystems_using: [ACP-Runtime, MCP-Bridge]
---

# Parse at Boundaries

Validate untrusted data at every boundary entry point using a schema library (Zod in TypeScript, struct tags in Go). Never pass raw `unknown` inward or cast `JSON.parse` results directly to a type.

## Problem

Data arriving from external sources (agents, IPC, databases, network) may not match the expected shape. Blind type casts hide errors until runtime deep inside the system, making them hard to diagnose.

## Solution

Validate at the boundary, reject early, and only pass typed values into internal logic.

```typescript
// Bad: blind cast
const data = JSON.parse(raw) as MyType;

// Good: Zod parse
const data = MySchema.parse(JSON.parse(raw));
```

## Where Applied

| Boundary | Project | Mechanism |
|----------|---------|-----------|
| MCP tool inputs | [[Projects/Poolside-Studio]] | MCP SDK validates via `inputSchema` |
| IPC handler inputs | [[Projects/Poolside-Studio]] | Zod in `electron/ipc/` |
| Database reads (SQLite) | [[Projects/Poolside-Studio]] | Explicit Zod guards on row results |
| ACP protocol payloads | [[Projects/Poolside-Studio]] | Validated before entering session state |
| Robot discovery file | [[Projects/Poolside-Studio]] | Zod parse of `robot-mode.json` |

## Related Subsystems

- [[Subsystems/ACP-Runtime]] — ACP payloads validated at the IPC boundary
- [[Subsystems/MCP-Bridge]] — MCP SDK provides inputSchema validation for bridge tools

## Tradeoffs

- **Cost**: Minor validation overhead at boundaries
- **Benefit**: Runtime type safety, clear error messages, prevents data from spreading bad shapes into the core

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
