---
source_path: /Users/matthew.fisher/poolsideai/poolside-city
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project]
tech_stack: []
related_projects: [Forge, Poolside-Studio]
---

# Poolside City

## Source
`/Users/matthew.fisher/poolsideai/poolside-city`

## Overview

City is a separate app/service in the Poolside ecosystem. Likely related to user interface or experience. See the source for details as they emerge.

## Subsystems

- [[Subsystems/ACP-Runtime]] — may need to communicate via ACP
- [[Subsystems/MCP-Bridge]] — may need MCP tool integrations
- [[Subsystems/Build-System]] — likely uses similar tooling to Studio

## Related Projects

- [[Projects/Forge]] — shared infrastructure and deployment patterns
- [[Projects/Poolside-Studio]] — potential UI/service integration
- [[Projects/Poolside-Edge]] — adjacent edge/city products

## Patterns

- [[Patterns/Layer-Isolation]] — if Electron-based, follows layer rules
- [[Patterns/Service-Class]] — Electron services via typed classes
- [[Patterns/Robot-Discovery]] — for dev experience

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
