---
date: 2024-06-18
status: accepted
tags: [decision]
related_projects: [Poolside-Studio]
related_subsystems: [ACP-Runtime, MCP-Bridge, Skill-System, Agent-Loop]
related_patterns: [Layer-Isolation, Service-Class]
---

# DR-0001: Electron + Vite + Svelte 5 for Desktop Client

## Context

Poolside Studio needs to be a desktop app that can spawn and manage subprocess agent runtimes (`pool acp`, `goose acp`), communicate over stdio pipes, manage local SQLite state, and serve a localhost MCP HTTP server — while also providing a rich reactive UI.

## Decision

Use **Electron** as the desktop host, **Vite 8** as the renderer build tool, and **Svelte 5** as the UI framework. TypeScript throughout.

## Rationale

- Electron gives direct Node.js subprocess management and filesystem APIs without a Rust bridge
- ACP transport (stdin/stdout) maps naturally to Node.js `child_process`
- Svelte 5 runes (`$state`, `$derived`) provide fine-grained reactivity with less boilerplate than React
- Vite's fast HMR and plugin ecosystem suits the renderer build
- TypeScript covers both Electron main and renderer with shared type imports
- `better-sqlite3` runs natively in Node for the local DB without a separate process

## Consequences

- Enables the [[Patterns/Layer-Isolation]] boundary between Node.js main and browser renderer
- Enables the [[Patterns/Service-Class]] pattern for Electron modules
- Requires [[Subsystems/Skill-System]] to expose a Node-compatible `skill-mirror.ts`
- App ships macOS arm64 only currently (Electron Builder); signing/notarization pending
- Bundle size is large (Electron ships Chromium)

## Related Projects

- [[Projects/Poolside-Studio]] — the decision applies here
