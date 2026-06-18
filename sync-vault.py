#!/usr/bin/env python3
"""
Obsidian Vault Sync Script
Scans poolsideai directories and updates the vault with project metadata and daily notes.
"""

import os
import json
import subprocess
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

VAULT_ROOT = Path(__file__).parent / "Poolside"
SOURCE_ROOT = Path("/Users/matthew.fisher/poolsideai")
PROJECTS_DIR = VAULT_ROOT / "Projects"
DAILY_DIR = VAULT_ROOT / "Daily"

PROJECTS = [
    "forge",
    "poolside-studio",
    "deck",
    "public-docs",
    "solutions-architecture",
    "poolside-server-devops",
    "poolside-city",
    "poolside-edge",
    "agents",
    "demos",
    "onboarding",
    "local-zsh-function",
]


def extract_readme_info(project_path: Path) -> Dict:
    """Extract description and key info from README.md"""
    result = {"description": "", "tech_stack": []}
    readme = project_path / "README.md"
    
    if not readme.exists():
        return result
    
    content = readme.read_text()
    lines = content.split('\n')
    
    # First non-empty line after title is description
    for i, line in enumerate(lines[1:], 2):
        line = line.strip()
        if line and not line.startswith('#'):
            result["description"] = line
            break
    
    # Extract tech stack hints from content
    tech_patterns = [
        r'Go', r'TypeScript', r'JavaScript', r'Svelte', r'React', r'Electron',
        r'Python', r'Bazel', r'Kubernetes', r'Docker', r'Ansible', r'Zsh',
        r'Node\.js', r'Vite', r'Vitest', r'pnpm', r'Mintlify'
    ]
    found_tech = set()
    for pattern in tech_patterns:
        if re.search(pattern, content, re.I):
            found_tech.add(pattern.replace(r'\.', '.'))
    
    result["tech_stack"] = sorted(found_tech)
    return result


def get_git_commits_today(project_path: Path) -> List[Dict]:
    """Get git commits from today for the project"""
    if not (project_path / ".git").exists():
        return []
    
    try:
        result = subprocess.run(
            ["git", "log", "--since=00:00", "--pretty=format:%H|%s|%ci", "--", "."],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=30
        )
        commits = []
        today = datetime.now().strftime("%Y-%m-%d")
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            parts = line.split('|')
            if len(parts) >= 3 and parts[2].startswith(today):
                commits.append({
                    "hash": parts[0][:8],
                    "message": parts[1],
                    "date": parts[2][:10]
                })
        return commits
    except Exception:
        return []


def update_project_note(project: str, info: Dict) -> None:
    """Update or create project note with extracted info"""
    note_path = PROJECTS_DIR / f"{project}.md"
    today = datetime.now().strftime("%Y-%m-%d")
    
    if note_path.exists():
        content = note_path.read_text()
        # Update date_updated in frontmatter
        content = re.sub(
            r'date_updated: \d{4}-\d{2}-\d{2}',
            f'date_updated: {today}',
            content
        )
        # Update tech_stack if we found more
        if info.get("tech_stack"):
            tech_str = json.dumps(info["tech_stack"])
            content = re.sub(
                r'tech_stack: \[\]',
                f'tech_stack: {tech_str}',
                content
            )
        note_path.write_text(content)
    else:
        # Create new note
        status = "active" if (SOURCE_ROOT / project / ".git").exists() else "archived"
        tech_str = json.dumps(info.get("tech_stack", []))
        
        content = f"""---
source_path: {SOURCE_ROOT / project}
date_added: {today}
date_updated: {today}
status: {status}
tags: [project]
tech_stack: {tech_str}
related_projects: []
key_docs: []
---

# {project.replace('-', ' ').title()}

## Overview

{info.get('description', 'No description available.')}

## Source Path
`{SOURCE_ROOT / project}`

## Key Subsystems


## Key Files

- README.md
- AGENTS.md (if exists)

## Key Directories

## Related Projects

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```

## Decisions

```dataview
LIST FROM "Decisions" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
"""
        note_path.write_text(content)


def create_daily_note() -> None:
    """Create today's daily note with work summary"""
    today = datetime.now().strftime("%Y-%m-%d")
    note_path = DAILY_DIR / f"{today}.md"
    
    if note_path.exists():
        return
    
    commits_by_project = {}
    for project in PROJECTS:
        project_path = SOURCE_ROOT / project
        if project_path.exists():
            commits = get_git_commits_today(project_path)
            if commits:
                commits_by_project[project] = commits
    
    content = f"""---
date: {today}
tags: [daily]
projects_worked: {json.dumps(list(commits_by_project.keys()))}
---

# Work Log - {today}

## Sessions

### Morning
"""

    for project, commits in commits_by_project.items():
        content += f"\n#### [[{project}]]\n"
        for commit in commits:
            content += f"- `{commit['hash']}` {commit['message']}\n"

    content += """
### Afternoon


### Evening

## Projects Referenced
```dataview
LIST FROM #project WHERE file.name IN this.projects_worked
```

## Notes
"""

    note_path.write_text(content)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Sync Obsidian vault with poolside work")
    parser.add_argument("--init", action="store_true", help="Initial setup - create all project notes")
    parser.add_argument("--daily", action="store_true", help="Create/update daily note")
    parser.add_argument("--scan", action="store_true", help="Rescan all projects")
    args = parser.parse_args()
    
    if args.init:
        print("Initializing vault...")
        for project in PROJECTS:
            project_path = SOURCE_ROOT / project
            if project_path.exists():
                info = extract_readme_info(project_path)
                print(f"  Creating note for {project}...")
                update_project_note(project, info)
        create_daily_note()
        print("Done!")
    
    elif args.daily:
        create_daily_note()
        print(f"Daily note created: {DAILY_DIR / datetime.now().strftime('%Y-%m-%d')}.md")
    
    elif args.scan:
        print("Scanning all projects...")
        for project in PROJECTS:
            project_path = SOURCE_ROOT / project
            if project_path.exists():
                info = extract_readme_info(project_path)
                update_project_note(project, info)
        print("Done!")


if __name__ == "__main__":
    main()