---
tags: [pattern]
projects_using: [Poolside-Studio]
subsystems_using: [Skill-System, MCP-Bridge]
---

# Draft-First Mutations

Agents create drafts of mutations (skill creates, skill updates); users explicitly approve before changes are committed to production state. Prevents agents from silently overwriting live data.

## Problem

If agents can directly mutate production state (skills, tasks, settings), a mistaken or malicious agent operation is immediately destructive with no human checkpoint.

## Solution

Treat all agent-initiated writes as drafts. Surface pending drafts in the UI. Require explicit user approval before promotion to canonical state.

```
Agent calls create_skill (MCP tool)
  └── Creates skill_draft record (not live)
        └── UI shows pending draft notification
              └── User clicks Approve
                    └── Draft promoted to live skill
```

## Where Applied

| Mutation | Project | Status |
|----------|---------|--------|
| Skill creation | [[Projects/Poolside-Studio]] | Draft-first |
| Skill updates | [[Projects/Poolside-Studio]] | Draft-first (revision drafts) |
| Task creation | [[Projects/Poolside-Studio]] | Direct (lower risk) |

## Related Subsystems

- [[Subsystems/Skill-System]] — primary application of this pattern
- [[Subsystems/MCP-Bridge]] — the `create_skill` / `update_skill` tools implement draft behaviour

## Tradeoffs

- **Cost**: Extra UI step for skill changes; requires draft storage layer
- **Benefit**: Users stay in control; agent mistakes are reversible before they land

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
