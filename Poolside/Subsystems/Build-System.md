---
tags: [subsystem, tooling]
related_projects: [Forge, Poolside-Studio, Deck]
key_decisions: [DR-0003-Bazel-Monorepo]
key_patterns: []
---

# Build System

Poolside uses different build systems per codebase: **Bazel** for the Go/Python monorepo (Forge), **Vite + Turborepo + pnpm** for TypeScript/Svelte (Poolside Studio), and **standard Go modules** for smaller Go projects (Deck).

## Projects

- [[Projects/Forge]] — Bazel for Go + Python; Turborepo + pnpm for TypeScript UI
- [[Projects/Poolside-Studio]] — Vite 8 + pnpm + Turborepo; Electron Builder for packaging
- [[Projects/Deck]] — standard Go modules with `go build` / `make`

## Forge (Bazel)

```bash
bazelisk build //...          # build all
bazelisk test //...           # test all
make gazelle                  # regenerate BUILD.bazel files after adding/removing files
make setup                    # install all tools via asdf
```

Key files: `BUILD.bazel`, `MODULE.bazel`, `.bazelrc`, `.tool-versions`

## Poolside Studio (Vite + pnpm)

```bash
pnpm dev          # start Vite dev server + Electron
pnpm build        # production build
pnpm test         # run Vitest suite
pnpm verify       # full CI: lint + typecheck + tests + build
pnpm lint-staged  # pre-commit hook
```

Key files: `vite.config.ts`, `turbo.json`, `package.json`, `pnpm-workspace.yaml`

## Related Subsystems

- [[Subsystems/Agent-Loop]] — agent-loop depends on build system for verify steps

## Decisions

- [[Decisions/DR-0003-Bazel-Monorepo]] — why Bazel for the Go/Python monorepo

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
