---
tags: [pattern]
projects_using: [Poolside-Studio]
subsystems_using: [MCP-Bridge, ACP-Runtime, Robot-CLI, Skill-System]
---

# Layer Isolation

Strict import boundaries between Electron main, renderer (Svelte), and feature modules. Each layer has a defined owner, a clear public interface, and ESLint-enforced rules preventing upward or cross-feature imports.

## Problem

In Electron apps the renderer assumes a browser environment (DOM, Vite client, Svelte reactivity) while main runs in Node.js. Mixing them causes runtime crashes, makes code hard to test, and creates invisible coupling between features.

## Solution

Define four layers with explicit rules enforced by ESLint:

```
Renderer (Svelte features)   ← no cross-feature imports
  ↑ src/lib/ only
src/lib/ (shared libraries)  ← no feature imports
  ↑ IPC boundary (preload.ts)
Electron Main (Node.js)      ← no src/features/ imports
  ↓ spawns
Agent Runtime (external)
```

## Enforced Rules

```
electron/**     → src/features/**    FORBIDDEN
src/lib/**      → src/features/**    FORBIDDEN
src/features/A  → src/features/B     FORBIDDEN
electron/mcp/** → electron/acp/**    FORBIDDEN (go through main.ts)
```

## Communication Between Layers

| From | To | Mechanism |
|------|----|-----------|
| Renderer feature | Another feature | Shared store in `src/lib/` |
| Renderer | Electron main | IPC via `src/lib/desktop/` |
| Electron main | Agent runtime | stdio (ACP) or HTTP (MCP) |

## Related Subsystems

- [[Subsystems/MCP-Bridge]] — bridge in Electron main cannot directly call ACP manager; must go through `main.ts` services
- [[Subsystems/ACP-Runtime]] — runtime is an external process, explicitly outside the layer boundary
- [[Subsystems/Robot-CLI]] — robot discovery follows workspace scoping outside feature layer
- [[Subsystems/Skill-System]] — skill mirror is a Node-compatible lib module

## Related Projects

- [[Projects/Poolside-Studio]] — primary application of this pattern
- [[Projects/Forge]] — also has layer-like boundaries between cmd/ and pkg/
- [[Projects/Deck]] — controller pattern mirrors layer isolation for Go

## Decisions

- [[Decisions/DR-0001-Electron-Svelte]] — Studio's choice of Electron enabled this pattern
- [[Decisions/DR-0005-HTTP-MCP-Bridge]] — HTTP bridge avoids cross-layer calls

## Tradeoffs

- **Cost**: More wiring through `main.ts`; requires extracting shared logic to `src/lib/`
- **Benefit**: Features are independently testable; Electron/renderer boundary is safe; refactors don't cascade unexpectedly

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
