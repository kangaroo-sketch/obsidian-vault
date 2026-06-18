---
date: 2024-06-18
status: proposed
tags: [decision]
related_projects: [Deck, Forge, Poolside-Studio]
related_subsystems: [ACP-Runtime]
related_patterns: []
---

# DR-0004: Kubernetes CRDs for Agent Execution (Deck)

## Context

Running AI agents at scale requires orchestration: spinning up isolated pods per agent run, managing LLM provider routing, enforcing guardrails and spend limits, and supporting multi-step DAG workflows. Poolside needs a platform that handles this without building a custom scheduler.

## Decision

Build **Deck** as a Kubernetes operator with custom CRDs (`Agent`, `ModelProvider`, `ModelSelector`, `AgentRun`). Each `AgentRun` creates a Kubernetes pod that runs the agent container, communicates with the router, and terminates on completion.

## Rationale

- Kubernetes provides pod lifecycle management, resource limits, and namespace isolation for free
- CRDs make agent configuration declarative and GitOps-friendly
- The controller pattern (reconcile loop) naturally handles retries and status reporting
- Kubernetes RBAC and NetworkPolicy enforce security boundaries (split-pod topology)
- Existing Poolside Kubernetes expertise via Forge's `deploy/` infrastructure

## Consequences

- Requires a Kubernetes cluster to run; local development uses a local cluster (e.g. kind/k3d)
- P0 foundation tasks are complete; P1 (core execution) and P2 (DAG workflows, warm pools) are TODO — see `PLAN.md`
- ACP integration: Deck pods can run ACP-compatible agent containers, connecting to [[Subsystems/ACP-Runtime]]
- Spend tracking, guardrails, and RAG are built into the router rather than the agent container

## Related Projects

- [[Projects/Deck]] — the decision applies here
- [[Projects/Forge]] — ACP runtime that Deck agents may use
- [[Projects/Poolside-Studio]] — potential future integration for Deck-backed sessions
