---
name: security
description: Credential management, secret scanning, encryption standards, and audit trail rules. Use whenever handling API keys, environment variables, authentication, encryption, or any security-sensitive code.
---

# Security

## Credentials & Secrets

### Golden Rules

1. **Never hardcode credentials in source code** — not even temporarily. A single committed secret persists in git history forever, even after deletion
2. **Never log credentials** — logs get aggregated to SIEMs, shipped to third parties, and retained beyond your control. Use `[REDACTED]` or character-count only:
   ```
   print("token: [REDACTED] ({len(token)} chars)")
   ```
3. **Never commit secrets to git** — even if you delete them later, they're in history. Rotation is the only fix and it's expensive
4. **Use environment variables** or a secrets manager (Firestore, Vault, .env files) — this keeps secrets out of the codebase and makes rotation a config change, not a code change
5. **`.env` files are always gitignored** — commit `.env.example` with placeholder values so new developers know what's needed without seeing real secrets

### If Credentials Were Exposed

- Rotate immediately (or as soon as all deployments support the new path)
- Scan git history with `trufflehog` or `gitleaks`
- Document rotation status in the project's known issues section

### API Keys

- Distinguish between **public keys** (safe to embed, security via backend rules) and **secret keys** (never expose)
- Document which keys are which in the project's security section

## Encryption

- Prefer encryption at rest for sensitive data (SQLCipher, encrypted Firestore, etc.)
- Use industry-standard algorithms — never roll your own crypto
- Store encryption keys separately from encrypted data

## Scanning Tools

| Tool | Purpose | Language |
|------|---------|----------|
| `pip-audit` | Python dependency CVEs | Python |
| `safety` | Python dependency CVEs | Python |
| `trivy` | Filesystem & container scanning | Universal |
| `npm audit` | Node.js dependency CVEs | JavaScript |
| `trufflehog` | Secret scanning in git history | Universal |
| `gitleaks` | Secret scanning in git history | Universal |

## Audit Trail

- Log security-relevant actions (auth, access, changes) with timestamps
- Never log PII or credentials in audit logs
- Retain audit logs per applicable regulation (GDPR: purpose-limited retention)
