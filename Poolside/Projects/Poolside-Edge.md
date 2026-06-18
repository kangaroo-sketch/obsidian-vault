---
source_path: /Users/matthew.fisher/poolsideai/poolside-edge
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project]
tech_stack: [Shell, Ansible]
related_projects: [Forge, Poolside-Studio, Server-DevOps]
---

# Poolside Edge

## Source
`/Users/matthew.fisher/poolsideai/poolside-edge`

## Overview

Edge infrastructure tooling and configuration. Related to Poolside's edge deployments and customer environments.

## Subsystems

- [[Subsystems/Build-System]] — likely uses shell-based deployment tooling
- [[Subsystems/MCP-Bridge]] — may expose edge services via MCP
- [[Subsystems/Robot-CLI]] — edge tooling may need CLI inspection

## Related Projects

- [[Projects/Forge]] — shares deployment patterns
- [[Projects/Poolside-Studio]] — Studio runs on edge infrastructure
- [[Projects/Server-DevOps]] — edge platform team overlaps

## Patterns

- [[Patterns/Parse-at-Boundaries]] — configuration parsing
- [[Patterns/Robot-Discovery]] — local inspection

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
