---
source_path: /Users/matthew.fisher/poolsideai/poolside-server-devops
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project, infrastructure]
tech_stack: [Kubernetes, Terraform, AWS]
related_projects: [Forge, Solutions-Architecture, Deck]
---

# Server DevOps

Infrastructure and server configuration for Poolside's hosted environments.

## Source
`/Users/matthew.fisher/poolsideai/poolside-server-devops`

## Subsystems

- [[Subsystems/Build-System]] — infrastructure as code with Atlantis/Terraform
- [[Subsystems/ACP-Runtime]] — deployed services expose ACP endpoints
- [[Subsystems/MCP-Bridge]] — production MCP endpoints for remote agents

## Related Projects

- [[Projects/Forge]] — services deployed onto this infrastructure
- [[Projects/Solutions-Architecture]] — customer-facing deployment artifacts
- [[Projects/Deck]] — requires Kubernetes clusters to be provisioned

## Patterns

- [[Patterns/Robot-Discovery]] — applies to app profile management

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
