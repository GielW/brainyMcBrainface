# CI/CD

## GitHub Actions — Standard Patterns

### Trigger Patterns

```yaml
# On push to main
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# On version tag
on:
  push:
    tags: ['v*']

# Scheduled (weekly)
on:
  schedule:
    - cron: '0 6 * * 1'  # Monday 06:00 UTC
```

### Standard Jobs

| Job | Purpose | Tools |
|-----|---------|-------|
| Lint | Code quality gate | ruff, flutter analyze, eslint |
| Test | Run test suite | pytest, flutter test, jest |
| Security scan | Dependency vulnerabilities | pip-audit, trivy, npm audit |
| Build | Compile/package | language-specific |
| SBOM | Software Bill of Materials | cyclonedx-bom, syft |
| Release | Create GitHub Release | gh, artifact upload |

### Artifacts

- Upload scan results, reports, and builds as GitHub Actions artifacts
- Use 90-day retention for security reports
- Post summary verdicts to step summary (🟢 ALL CLEAR / 🔴 ACTION REQUIRED)

## Release Pipelines

For projects with release scripts:
1. Version bump (config files + CHANGELOG)
2. Build (all target platforms)
3. Package (zip/tar/installer)
4. Git commit + tag
5. GitHub Release (with assets)
6. Post-release update (e.g., Firebase version doc, npm publish)

## Dependabot

Enable Dependabot for automatic dependency update PRs:

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"  # or "pub", "npm"
    directory: "/"
    schedule:
      interval: "weekly"
```
