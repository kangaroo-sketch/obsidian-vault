---
source_path: <%= source_path %>
date_added: <%= date_added %>
date_updated: <% tp.date.now("YYYY-MM-DD") %>
status: active
tags: [project]
tech_stack: []
related_projects: []
key_docs: []
---

# <%= project_name %>

## Overview

<%= description %>

## Source Path
`<%= source_path %>`

## Key Subsystems

- [ ] Add key subsystems from AGENTS.md or README

## Key Files

- [ ] Add important files for quick navigation

## Progress Log

### 2024-06-XX
- 

## Related Projects

```dataview
LIST FROM #project WHERE contains(related_projects, this.file.name)
```

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```

## Decisions

```dataview
LIST FROM "Decisions" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```