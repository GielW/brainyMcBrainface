---
name: documentation
description: Markdown conventions, YAML frontmatter templates, changelog format, version numbering, file naming, and source attribution rules. Use whenever writing or editing markdown files, READMEs, changelogs, or any project documentation.
---

# Documentation Standards

## Markdown Conventions

- **Headers**: `# Title` → `## Section` → `### Subsection` (max 3 levels in most docs)
- **Tables** for structured data; **code blocks** with language hints (`python`, `bash`, `dart`, `text`)
- **Compact table style** — no column padding:
  - Header separator: `| --- | --- | --- |` (not padded)
  - Data cells: `| value | value |` (not padded)
- **Line length**: No hard wrap for prose; let editor soft-wrap
- **Lists**: Blank line before and after list blocks (MD032)
- **Code fences**: Blank line before and after (MD031), always specify language (MD040), use `text` for plain text

## YAML Frontmatter

Every documentation `.md` file should have YAML frontmatter:

```yaml
---
tags:
  - type/note
  - status/draft
  - domain/some-domain
aliases:
  - Short Name
created: 2026-03-09
---
```

## Links

- **Obsidian vault notes**: Use `[[wikilinks]]` — `[[path/to/note|Display Text]]`
- **Root-level docs** (README, CONTRIBUTING, CHANGELOG): Use standard Markdown links `[text](path)` for GitHub compatibility
- **Cross-references**: Before finishing any edit, search for `[[filename]]` and `[text](path)` references to changed files and verify they still make sense

## File & Folder Naming

- Documentation files: `kebab-case.md` or `UPPER-CASE.md` for root-level standards
- Use descriptive names: `01-PROJECT-CHARTER.md` with numeric prefixes for ordered docs

## Changelog Format

- Follow [Keep a Changelog](https://keepachangelog.com/)
- Sections: Added, Changed, Deprecated, Removed, Fixed, Security
- Reference issue IDs and commit scopes in entries

## Version Numbering

- Follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`
- Keep version in sync across: project config, CHANGELOG, CLAUDE.md, and any charter/progress docs

## Source Attribution

- **Always reference data sources** — when using external knowledge, templates, prompts, frameworks, or data, record where it came from
- Credit format: a simple `Source:` line, footnote, or link to the original
- This applies to: research findings, copied/adapted prompts, design patterns borrowed from other projects, legal references, third-party templates
- For brainyMcBrain specifically: when a skill or convention originates from an external source (blog post, GitHub repo, community prompt), note it at the top of the file or inline
- Give credit where credit is due — don't pass off external work as your own
