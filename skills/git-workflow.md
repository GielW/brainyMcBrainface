# Git Workflow

## Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/) in **all** repositories:

```
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

### Rules

- Scope is optional but encouraged — use the module/area name
- Description is imperative, lowercase, no trailing period: `add user auth`, not `Added user auth.`
- Body for breaking changes or detailed context

## Branching

- `main` is the default branch and always deployable
- Feature branches: `feat/<short-name>` or `fix/<short-name>`
- No direct force-push to `main`

## Common Git Commands

```bash
git add -A && git status              # Stage & review
git commit -m "feat(scope): description"  # Commit
git push origin main                  # Push
git log --oneline -10                 # Quick history
```

## Pull Requests

- Title follows conventional commit format
- Reference related issues: `Closes #123`
- Squash merge preferred for clean history
