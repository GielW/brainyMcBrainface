---
name: git-workflow
description: Commit conventions, branching strategy, and PR rules. Use whenever writing commit messages, creating branches, reviewing PRs, or resolving merge conflicts — even for small changes.
---

# Git Workflow

## Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/) in **all** repositories:

```text
<type>(<scope>): <description>

<optional body>
```

### Types

| Type | Use for |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `refactor` | Code change that neither fixes nor adds |
| `test` | Adding/updating tests |
| `chore` | Maintenance (deps, CI, config) |
| `style` | Formatting, no logic change |
| `sync` | Sync operations (claude.md, config files) |

### Commit Rules

- Scope is optional but encouraged — use the module/area name
- Description is imperative, lowercase, no trailing period: `add user auth`, not `Added user auth.`
- Body for breaking changes or detailed context

## Branching

- `main` is the default branch and always deployable
- Feature branches: `feat/<short-name>` or `fix/<short-name>`
- No direct force-push to `main`

## Pre-Commit Check — Always Verify Changes Exist

**Before every `git commit`, check that there are actual staged changes.** Never blindly run `git add && git commit` — the working tree may already be clean (e.g., CI sync already applied the change, or a copy produced identical content).

```bash
# Safe commit pattern — only commit if there are staged changes
git add -A
if git diff --cached --quiet; then
  echo "No changes to commit — skipping"
else
  git commit -m "type(scope): description"
fi
```

This prevents:

- Empty commit errors ("nothing to commit, working tree clean")
- Redundant commits that duplicate what CI already pushed
- Confusion when `git push` says "Everything up-to-date" after a commit that looked like it had changes

**Apply this especially during sync operations** (brain recompile → copy to project repos → commit) where CI workflows or other sessions may have already applied the same content.

## Common Git Commands

```bash
git add -A && git status              # Stage & review
git diff --cached --quiet || git commit -m "feat(scope): description"  # Commit only if changes exist
git push origin main                  # Push
git log --oneline -10                 # Quick history
```

## Pull Requests

- Title follows conventional commit format
- Reference related issues: `Closes #123`
- Squash merge preferred for clean history
