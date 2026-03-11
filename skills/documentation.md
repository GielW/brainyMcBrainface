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

## Markdown Lint

All markdown source files must pass **markdownlint** with zero errors. Configuration lives in `.markdownlint.json` at the repo root.

### Key Rules

| Rule | What It Enforces |
| --- | --- |
| **MD024** | No duplicate headings at the same level (siblings only — after compilation, headings demote and can collide) |
| **MD032** | Blank line before and after lists |
| **MD040** | Code fences must specify a language (`python`, `bash`, `dart`, `text`, `markdown`, `yaml`, `json`) |
| **MD031** | Blank line before and after fenced code blocks inside list items |
| **MD022** | Blank line before and after headings |
| **MD038** | No spaces inside inline code spans |

### Disabled Rules

| Rule | Why |
| --- | --- |
| MD013 (line length) | We use soft-wrap, no hard line length limit |
| MD033 (inline HTML) | We use HTML comments for guardrails and metadata |
| MD041 (first line heading) | Files start with YAML frontmatter, not a heading |
| MD036 (emphasis as heading) | We use bold text for emphasis in tables and lists |
| MD060 (table column style) | Our compact table style intentionally omits column padding |

### When to Lint

- **Locally**: `npx markdownlint-cli2 "skills/**/*.md" "languages/**/*.md" "domains/**/*.md" "projects/**/*.md"`
- **CI**: Runs automatically on push/PR via the Validate Brain workflow
- **After compilation**: `compile-brain.py` checks compiled output when markdownlint-cli2 is available

### Heading Uniqueness (MD024)

The compiler demotes headings when assembling compiled files (`# → ###`). Generic headings like `Anti-Patterns`, `Tools`, `Rules`, `Style`, `Imports` will collide after compilation. **Always prefix with the section context**:

- `Anti-Patterns` → `Search-First Anti-Patterns`, `Debugging Anti-Patterns`
- `Tools` → `Python Tools`, `Dart Tools`, `Testing Tools`
- `Rules` → `Commit Rules`, `Logging Rules`

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
- For brainyMcBrainface specifically: when a skill or convention originates from an external source (blog post, GitHub repo, community prompt), note it at the top of the file or inline
- Give credit where credit is due — don't pass off external work as your own
