---
source_path: /Users/matthew.fisher/poolsideai/solutions-architecture
date_added: 2024-06-18
date_updated: 2026-06-18
status: active
tags: [project]
tech_stack: [Ansible, Keycloak, Kubernetes, AWS]
related_projects: [Forge, Server-DevOps]
---

# Solutions Architecture

Customer-facing and internal artifacts from the Solutions Architecture team: deployment automation, identity provider integration, and release tooling.

## Source
`/Users/matthew.fisher/poolsideai/solutions-architecture`

## Artifacts

| Artifact | Audience | Description |
|----------|----------|-------------|
| `tools/sandbox-deployment-script/` | Internal | Automates sandbox env setup in the Poolside AWS account |
| `ansible_poolside_installer/` | Internal/External | Ansible-based Poolside installer |
| `keycloak_ldap/` | Internal/External | Keycloak LDAP identity provider integration |
| `keycloak_saml/` | Internal/External | Keycloak SAML authentication setup |
| `release-process/` | Internal | Release process documentation |

## Related Projects

- [[Projects/Forge]] — deploys into the infrastructure this team manages
- [[Projects/Server-DevOps]] — overlapping infrastructure ownership

## Daily Work References

```dataview
LIST FROM "Daily" WHERE contains(file.outlinks, link(this.file.name)) SORT file.name DESC
```
