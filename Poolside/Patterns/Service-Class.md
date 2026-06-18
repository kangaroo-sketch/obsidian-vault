---
tags: [pattern]
projects_using: [Poolside-Studio]
subsystems_using: [MCP-Bridge, ACP-Runtime, Robot-CLI]
---

# Service Class

Every new Electron module exports a single typed service class with a clear public interface. Dependencies are injected through the constructor. All services are wired together in `electron/main.ts`.

## Problem

Ad-hoc modules with exported functions and shared mutable state are hard to test, hard to mock, and create implicit coupling through globals.

## Solution

One file = one class. Constructor injection for dependencies. Wire everything in `main.ts`.

```typescript
// Good pattern — from golden-principles.md
export class FooService {
  constructor(private readonly db: AppDatabase) {}

  async getFoo(id: string): Promise<FooRecord | null> { ... }
}

// In main.ts
const fooService = new FooService(db);
```

## Where Applied

| Service | Project | Location |
|---------|---------|----------|
| MCP bridge | [[Projects/Poolside-Studio]] | `electron/mcp/app-bridge-service.ts` |
| ACP runtime manager | [[Projects/Poolside-Studio]] | `electron/acp/runtime-manager.ts` |
| Connector service | [[Projects/Poolside-Studio]] | `electron/connectors/` |
| Task service | [[Projects/Poolside-Studio]] | `electron/tasks/service.ts` |
| Console client | [[Projects/Poolside-Studio]] | `electron/console/` |

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — `AppBridgeService` is the canonical example
- [[Subsystems/ACP-Runtime]] — `RuntimeManager` follows this pattern
- [[Subsystems/Robot-CLI]] — robot discovery uses workspace-scoped service pattern

## Related Patterns

- [[Patterns/Layer-Isolation]] — service in main cannot import from renderer
- [[Patterns/Robot-Discovery]] — discovery file is managed by a service class

## Tradeoffs

- **Cost**: More boilerplate for simple modules
- **Benefit**: Easy to unit test with mock constructor args; explicit dependency graph; safe to refactor `main.ts` wiring without touching logic

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
