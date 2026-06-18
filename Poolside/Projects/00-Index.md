---
tags: [index, moc]
---

# Poolside Work — Map of Contents

This index connects to all major subsystems, patterns, and decisions. Use the links below to navigate the graph.

## Key Subsystems

- [[Subsystems/ACP-Runtime]] — Agent Communication Protocol
- [[Subsystems/MCP-Bridge]] — App Bridge for agent tools
- [[Subsystems/Robot-CLI]] — CLI for app inspection
- [[Subsystems/Skill-System]] — Skill management
- [[Subsystems/Build-System]] — Bazel/Vite/Turborepo
- [[Subsystems/Agent-Loop]] — Development workflow

## Key Patterns

- [[Patterns/Layer-Isolation]] — Electron/renderer boundaries
- [[Patterns/Draft-First-Mutations]] — User approval for agent writes
- [[Patterns/Parse-at-Boundaries]] — Input validation
- [[Patterns/Service-Class]] — Service modules
- [[Patterns/Feature-Communication]] — Cross-feature interaction
- [[Patterns/Robot-Discovery]] — Instance discovery

## Key Decisions

- [[Decisions/DR-0001-Electron-Svelte]] — Desktop stack choice
- [[Decisions/DR-0002-ACP-Protocol]] — Agent communication standard
- [[Decisions/DR-0003-Bazel-Monorepo]] — Build system
- [[Decisions/DR-0004-K8s-Agent-Execution]] — Kubernetes agents
- [[Decisions/DR-0005-HTTP-MCP-Bridge]] — Bridge transport
- [[Decisions/DR-0006-Robot-Discovery]] — Discovery mechanism

## Projects

```dataview
TABLE tech_stack AS "Stack", status AS "Status", date_updated AS "Updated"
FROM #project
WHERE file.name != "00-Index"
SORT status ASC, file.name ASC
```

## Subsystems

```dataview
TABLE related_projects AS "Projects", key_decisions AS "Decisions"
FROM #subsystem
SORT file.name ASC
```

## Patterns

```dataview
TABLE projects_using AS "Used By", subsystems_using AS "Subsystems"
FROM #pattern
SORT file.name ASC
```

## Decisions

```dataview
TABLE status AS "Status", related_projects AS "Projects"
FROM #decision
SORT file.name ASC
```

## Recent Daily Notes

```dataview
LIST FROM "Daily"
SORT file.name DESC
LIMIT 14
```

## Cross-Analysis Queries

### Which projects share ACP?
```dataview
LIST FROM #project
WHERE contains(file.outlinks, link("Subsystems/ACP-Runtime"))
```

### Which projects use the MCP Bridge?
```dataview
LIST FROM #project
WHERE contains(file.outlinks, link("Subsystems/MCP-Bridge"))
```

### Which patterns apply to Poolside Studio?
```dataview
LIST FROM #pattern
WHERE contains(projects_using, "Poolside-Studio")
```
