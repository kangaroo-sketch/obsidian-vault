# Welcome to Your Poolside Work Vault

A fully-linked knowledge graph of all Poolside work for review, analysis, and improvement.

## How to Navigate

**Start Here:**
- [[Projects/00-Index]] — All projects, subsystems, patterns, decisions in tables
- Switch to **Graph View** to see the visual connections

**Key Entry Points:**
| Node Type | Top Connectors |
|-----------|---------------|
| **Projects** | [[Projects/Poolside-Studio]] (20 links) · [[Projects/Forge]] (9 links) |
| **Subsystems** | [[Subsystems/ACP-Runtime]] (9 links) · [[Subsystems/MCP-Bridge]] (9 links) |
| **Patterns** | [[Patterns/Layer-Isolation]] (9 links) · [[Patterns/Service-Class]] (10 links) |
| **Decisions** | [[Decisions/DR-0005-HTTP-MCP-Bridge]] (8 links) |

## Graph View Colors

| Color | Meaning |
|-------|---------|
| Red | Projects (codebases) |
| Blue | Subsystems (technical systems) |
| Orange | Patterns (reusable architectures) |
| Green | Decisions (why choices were made) |
| Purple | Daily notes (work logs) |

## Quick Queries

```
Which projects use ACP?
→ Projects linked from Subsystems/ACP-Runtime

Which patterns affect all projects?
→ Patterns/Layer-Isolation, Patterns/Parse-at-Boundaries

How are skills implemented?
→ Subsystems/Skill-System → Patterns/Draft-First-Mutations
```

## Maintenance

Run `python3 sync-vault.py --daily` each evening to append git commits.

---

_Open the graph and zoom out. You should see:
- Blue ACP/MCP hubs in the center
- Red project nodes connecting to hubs
- Green decision nodes explaining major choices
- Orange pattern nodes crossing multiple projects_