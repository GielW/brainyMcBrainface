---
name: obsidian-vault
description: Obsidian vault structure, Maps of Content, note standards, tagging, and graph view conventions. Use whenever working in a project that uses an Obsidian knowledge vault, creating MOCs, or managing wiki-linked notes.
---

# Obsidian Vault — Domain Skill

> Activate for projects that use an Obsidian knowledge vault.

## Vault Structure

Every Obsidian-enabled project opens its **repo root** as the vault. Standard layout:

```text
project-root/
├── .obsidian/                    # Vault config (committed)
│   ├── app.json                  # Vault settings
│   ├── appearance.json           # Theme
│   ├── graph.json                # Graph colour groups
│   ├── templates.json            # Template folder config
│   └── templates/                # Note templates
├── docs/obsidian/
│   ├── 000 - Vault Index.md      # Main entry point
│   ├── MOC - *.md                # Maps of Content
│   └── modules/                  # Module/topic notes
```

## Maps of Content (MOCs)

MOCs are index notes that link to all notes in a category. Standard MOCs:

| MOC | Purpose |
|-----|---------|
| `MOC - Project` | Roadmap, charter, progress |
| `MOC - Architecture` | Tech stack, design patterns |
| `MOC - Modules` | Feature/requirement modules |
| `MOC - Security` | CVE tracking, scanning, security design |
| `MOC - Legal & GDPR` | Legal references (if applicable) |

## Note Standards

Every note must have:

1. **YAML frontmatter** with `tags`, `aliases`, `created`
2. **Wikilink navigation** — link back to the relevant MOC and Vault Index
3. **Consistent tags** from the project's approved tag list

## Tags

Use hierarchical tag prefixes:

- `#type/` — note, guide, reference, template
- `#status/` — todo, exploring, draft, done
- `#domain/` — project-specific domains
- `#module` — feature/requirement notes
- `#moc` — Maps of Content
- `#architecture` — tech stack, design
- `#security` — security-related
- `#project-definition` — charter, specs

## Graph View Colour Groups

Configure in `.obsidian/graph.json`. Standard scheme:

| Tag | Colour | Content |
|-----|--------|---------|
| `#project-definition` | Green | Charter, requirements |
| `#module` | Purple | Feature/module notes |
| `#architecture` | Orange | Tech stack, design |
| `#security` | Red | Security notes |
| `#moc` | Cyan | Maps of Content |

## Conventions

- **Attachments** go in `docs/attachments/`
- `workspace.json` is **gitignored** (user-specific layout)
- `plugins/` and `themes/` are **gitignored** (user-specific)
- Use **Insert Template** command for new notes (ensures consistent frontmatter)
