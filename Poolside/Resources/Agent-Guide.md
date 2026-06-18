---
tags: [guide, agent]
---

# Agent Guide for Vault Updates

This guide teaches agents how to extend the vault correctly. Follow the patterns established here.

## Adding a New Project

### Step 1: Identify the Project
Check `/Users/matthew.fisher/poolsideai/` for new directories. Each repo-level work needs a note.

### Step 2: Create the Project Note
```markdown
---
source_path: /Users/matthew.fisher/poolsideai/<new-project>
date_added: YYYY-MM-DD
date_updated: YYYY-MM-DD
status: active
tags: [project]
tech_stack: [<extracted from README/package.json/go.mod>]
related_projects: [related-project-names, comma-separated]
---

# <Project Name>

## Source
`/Users/matthew.fisher/poolsideai/<new-project>`

## Overview
<First paragraph from README.md>

## Subsystems
- [[Subsystems/ACP-Runtime]] — if it communicates via ACP
- [[Subsystems/MCP-Bridge]] — if it exposes MCP tools
- [[Subsystems/Build-System]] — for build tooling
- [[Subsystems/Skill-System]] — if it manages skills
- [[Subsystems/Robot-CLI]] — if it has CLI inspection
- [[Subsystems/Agent-Loop]] — if it uses worktree workflow

## Key Files
- `README.md` — overview
- `AGENTS.md` — agent workflow (if exists)

## Related Projects
- [[Projects/Related-Project]] — bidirectional links only
- [[Projects/Another-Project]]

## Patterns
- [[Patterns/Layer-Isolation]] — if Electron-based
- [[Patterns/Parse-at-Boundaries]] — if it validates inputs
- [[Patterns/Draft-First-Mutations]] — if agents write to it

## Decisions
- [[Decisions/DR-XXXX]] — if affected by any decision

## Daily Work References
```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
```

### Step 3: Add Bidirectional Links
Edit the `related_projects` frontmatter in any projects mentioned above.

## Adding a Meeting Note

### Location
`Meetings/YYYY-MM-DD <Topic>.md`

### Template
```markdown
---
date: YYYY-MM-DD
tags: [meeting, external|internal]
participants: [Person 1, Person 2]
related_projects: [<project-names>]
decisions_made: [<decision-numbers>]
---

# <Meeting Name> — YYYY-MM-DD

## Attendees
- Person 1
- Person 2

## Topics Discussed
### Topic 1
- Discussion points
- Action items

## Related Projects
```dataview
LIST FROM #project WHERE file.name IN this.related_projects
```

## Decisions
- [[Decisions/DR-XXXX]] — if a decision record was created

## Follow-up Tasks
- [ ] Task 1
- [ ] Task 2
```

### Step 2: Update Related Projects
Add the meeting date to any project's `related_projects` or create a backlink section.

## Adding a Decision Record

### Location
`Decisions/DR-XXXX-<Short-Title>.md`

### Template
```markdown
---
date: YYYY-MM-DD
status: proposed|accepted|deprecated
tags: [decision]
related_projects: [<projects-affected>]
related_subsystems: [<subsystems-affected>]
related_patterns: [<patterns-affected>]
---

# DR-XXXX: <Decision Title>

## Context
<Situation requiring decision>

## Decision
<What was chosen>

## Rationale
<Why this choice>

## Consequences
<What this enables/disables>

## Related Projects
```dataview
LIST FROM #project WHERE file.name IN this.related_projects
```

## Related Subsystems
```dataview
LIST FROM #subsystem WHERE file.name IN this.related_subsystems
```

## Daily Work References
```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
```

### Step 2: Update Affected Notes
Add a link to the decision in all `related_projects`, `related_subsystems`, and `related_patterns` notes.

## Key Rules for Agents

1. **Always maintain bidirectional links** — if A links to B, B's `related_projects` should list A
2. **Use consistent naming** — project notes use `PascalCase` filenames (matching the wikilink syntax)
3. **Update frontmatter arrays** — `related_projects`, `tech_stack`, etc. enable Dataview queries
4. **Run `python3 sync-vault.py --daily`** after adding notes to verify Dataview links work

## Commands to Run

```bash
# Sync daily note
python3 sync-vault.py --daily

# Verify link structure (check for orphaned notes)
# In Obsidian: Graph view → show orphans

# Check today's daily note exists
ls Daily/YYYY-MM-DD.md

# Check Dataview queries render
# In Obsidian: Open 00-Index.md → verify tables show data
```