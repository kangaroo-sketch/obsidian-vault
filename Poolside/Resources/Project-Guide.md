---
tags: [guide, resource]
---

# Adding New Projects

When you create new work directories under `/Users/matthew.fisher/poolsideai/`, follow these steps:

1. Create symlink in `_sources/`:
   ```bash
   cd Poolside/_sources/
   ln -s ../../../../../../poolsideai/<new-project> <new-project>
   ```

2. Create project note:
   ```bash
   cp _templates/Project.md Projects/<new-project>.md
   ```

3. Edit the frontmatter and add details

4. Link to related projects

## Vault Maintenance

Run the sync script daily:
```bash
cd /Users/matthew.fisher/poolsideai/obsidian-vault
python3 sync-vault.py --daily
```

Or set up cron:
```
0 18 * * * cd /Users/matthew.fisher/poolsideai/obsidian-vault && python3 sync-vault.py --daily
```