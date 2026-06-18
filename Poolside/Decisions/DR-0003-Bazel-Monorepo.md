---
date: 2024-06-18
status: accepted
tags: [decision]
related_projects: [Forge]
related_subsystems: [Build-System]
related_patterns: []
---

# DR-0003: Bazel for the Go + Python Monorepo

## Context

Forge is a large monorepo containing Go binaries, Python data pipelines, TypeScript UI packages, and infrastructure code. Standard Go modules (`go build`) and vanilla Python packaging don't scale well across a repo of this size with cross-language dependencies and hermetic CI requirements.

## Decision

Use **Bazel** (via Bazelisk) as the primary build and test system for Go and Python in Forge. JavaScript/TypeScript uses Turborepo + pnpm inside the `ui/` directory.

## Rationale

- Bazel's hermetic builds ensure reproducibility across machines and CI
- Gazelle auto-generates `BUILD.bazel` files from Go/Python source, reducing manual upkeep
- Cross-compilation (Go + Zig for CGO) is handled by `hermetic_cc_toolchain`
- Cache-aware builds and remote execution scale to large codebases
- Atlantis + Bazel enables Terraform plan/apply in CI with target-level granularity
- Turborepo handles the JS/TS workspace separately where Node tooling is more natural

## Consequences

- Every new Go/Python file must be in a `BUILD.bazel` target — run `make gazelle` after adding files
- Learning curve for engineers unfamiliar with Bazel
- `MODULE.bazel.lock` is large (578 KB) and must be kept in sync
- Enables hermetic image publishing via GitHub Actions OCI targets
- [[Subsystems/Build-System]] documents the full set of commands
- [[Projects/Poolside-Studio]] uses Turborepo (different choice, same monorepo problem)

## Related Subsystems

- [[Subsystems/Agent-Loop]] — agent-loop in Studio uses similar verification patterns
- [[Subsystems/ACP-Runtime]] — Forge builds and publishes the ACP runtime

## Related Patterns

- [[Patterns/Service-Class]] — Bazel modules naturally align with one-class-per-file

## Related Projects

- [[Projects/Forge]] — primary consumer of this decision
- [[Projects/Poolside-Studio]] — parallel monorepo build choices (Turborepo instead of Bazel)
