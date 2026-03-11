---
name: privacy-by-design
description: Privacy by Design engineering practices — data minimisation, purpose limitation, consent, data subject rights, retention, and DPIA triggers. Use whenever building software that collects, stores, processes, or transmits personal data — regardless of project or jurisdiction.
---

# Privacy by Design

> Universal engineering skill for building privacy into software from the ground up. Applies to every project that touches personal data — not just GDPR-specific tools.
>
> For Belgian-specific regulation (GBA/APD, retention periods, NIS2), see `domains/belgian-legal.md`.

---

## The 7 Foundational Principles

> Based on Ann Cavoukian's Privacy by Design framework, codified in GDPR Art. 25.

| # | Principle | In Practice |
|---|-----------|-------------|
| 1 | **Proactive, not reactive** | Design privacy in before writing code — don't retrofit after a breach |
| 2 | **Privacy as the default** | Out-of-the-box settings must be the most private option. Opt-in, not opt-out |
| 3 | **Privacy embedded in design** | Privacy is a core requirement, not an add-on or afterthought |
| 4 | **Full functionality** | Privacy and functionality are not trade-offs — find solutions that deliver both |
| 5 | **End-to-end security** | Protect data across its entire lifecycle: collection → storage → use → deletion |
| 6 | **Visibility and transparency** | Users must know what data is collected, why, and how long it's kept |
| 7 | **Respect for user privacy** | User-centric design — give users control over their own data |

## Data Minimisation

**Collect only what you need. Store only what you must. Delete when you're done.**

### In Code

- Before adding a field to a model/form, ask: "Is this strictly necessary for the stated purpose?"
- If the answer is "might be useful later" — don't collect it
- Use aggregates/anonymised data for analytics instead of raw personal data
- Strip PII from logs, error reports, and analytics payloads

### Common Violations

| Pattern | Problem | Fix |
|---------|---------|-----|
| Collecting full name when only initials are needed | Excessive data | Use initials or pseudonym |
| Storing IP addresses for analytics | Not needed if using aggregates | Hash or drop IPs |
| Logging request bodies containing PII | PII in logs | Sanitise before logging |
| Keeping user data after account deletion | No retention justification | Hard-delete or anonymise |
| Asking for date of birth when only age verification is needed | Excessive data | Use age confirmation boolean |

## Purpose Limitation

Every piece of personal data must have a **documented, specific purpose**. Data collected for purpose A cannot be used for purpose B without new legal basis.

### Implementation Pattern

```python
# Document the purpose for every personal data field
class UserProfile:
    """Processing purpose: account management and authentication."""
    email: str        # Purpose: login, password recovery, account notifications
    name: str         # Purpose: personalisation of UI greeting
    # phone: str      # NOT COLLECTED — no current purpose requires it
```

### Purpose Limitation Rules

- When adding a new feature that uses existing personal data, check if the original purpose covers it
- If not, you need new consent or a new legal basis — this is a product decision, not just an engineering one
- Document purposes in the data model (comments, docstrings, or a separate data register)

## Consent Management

### When Consent Is the Legal Basis

- Consent must be **freely given, specific, informed, and unambiguous** (GDPR Art. 7)
- Pre-ticked boxes are never valid consent
- Bundled consent ("accept all to use the service") is not freely given
- Users must be able to withdraw consent as easily as they gave it

### Implementation Checklist

- [ ] Consent is recorded with: who, what, when, how, which version of the text
- [ ] Withdrawal mechanism exists and is as easy as granting consent
- [ ] Consent is granular — separate purposes get separate consent (e.g., marketing vs. analytics)
- [ ] Consent text is clear, plain language — no legal jargon walls
- [ ] Re-consent is triggered when purposes or processing change

### When Consent Is NOT the Right Basis

Don't default to consent for everything. Other lawful bases (GDPR Art. 6) are often more appropriate:

| Basis | Example |
|-------|---------|
| Contract performance | Processing order data to fulfil a purchase |
| Legal obligation | Tax record retention |
| Legitimate interest | Fraud prevention, network security |
| Vital interests | Emergency medical situations |

## Data Subject Rights

Every application handling personal data must support these rights. Plan for them in your architecture — they cannot be bolted on.

| Right | Article | Implementation |
|-------|---------|---------------|
| **Access** | Art. 15 | Export endpoint — user can download all their data |
| **Rectification** | Art. 16 | Edit profile/data — user can correct inaccuracies |
| **Erasure** | Art. 17 | Delete account — hard-delete or fully anonymise |
| **Restriction** | Art. 18 | Freeze processing — mark data as restricted, stop using it |
| **Portability** | Art. 20 | Machine-readable export (JSON, CSV) |
| **Object** | Art. 21 | Opt-out of specific processing (e.g., profiling, marketing) |

### Architecture Implications

- **Soft-delete is not erasure** — if the user requests deletion, the data must actually be gone (or irreversibly anonymised)
- **Backups complicate erasure** — have a strategy for purging specific records from backups, or document the backup retention as a justified exception
- **Cascading data** — when deleting a user, find ALL related data (orders, logs, analytics events, uploaded files) and handle each
- **Audit trail vs. erasure** — you may need to keep a record that a deletion happened (who requested, when) without keeping the deleted data itself

## Privacy-Aware Logging

Logs are a common source of privacy violations. Treat log output as a potential data breach surface.

### Logging Rules

- **Never log PII** directly — names, emails, phone numbers, IPs, session tokens
- Use redaction: `user_id=123` instead of `email=jan@example.com`
- If you must log PII for debugging, use a separate short-retention debug log with restricted access
- Structured logging (JSON) makes it easier to filter/redact fields consistently
- Error reporting services (Sentry, etc.) will capture request context — configure PII scrubbing

### Pattern

```python
import logging

logger = logging.getLogger(__name__)

# BAD — PII in logs
logger.info(f"User {user.email} submitted form with phone {user.phone}")

# GOOD — reference by ID, no PII
logger.info(f"User {user.id} submitted form")
```

## Encryption & Data Protection

| Layer | Requirement |
|-------|-------------|
| **In transit** | TLS 1.2+ for all connections. No HTTP, no unencrypted APIs |
| **At rest** | Encrypt databases containing personal data (SQLCipher, LUKS, cloud-native encryption) |
| **In backups** | Backups must be encrypted — they contain the same sensitive data |
| **Keys** | Store separately from encrypted data. Use a secrets manager, not config files |

See `skills/security.md` for detailed encryption and credential management rules.

## Retention & Deletion

- Every personal data category must have a **defined retention period**
- When the period expires, data must be **automatically deleted or anonymised**
- Document retention periods in a data register (for Belgian-specific periods, see `domains/belgian-legal.md`)

### Implementation

- Add `created_at` / `expires_at` fields to data models holding personal data
- Implement a scheduled cleanup job (cron, background task) that purges expired data
- Log deletions for audit trail (what was deleted, when — not the data itself)
- Test the deletion — verify cascading deletes actually work and don't leave orphaned PII

## DPIA Triggers

A Data Protection Impact Assessment is required (GDPR Art. 35) when processing is **likely to result in a high risk** to individuals. Check these triggers:

| Trigger | Example |
|---------|---------|
| Systematic, extensive profiling with significant effects | Credit scoring, automated hiring |
| Large-scale processing of special categories | Health data, biometric data |
| Systematic monitoring of public areas | CCTV, location tracking |
| New technology applied to personal data | AI/ML models trained on user data |
| Automated decision-making with legal effects | Loan approval, benefit eligibility |
| Large-scale processing of children's data | Educational platforms, gaming |
| Cross-referencing or combining datasets | Merging HR + performance + health data |

If **two or more** triggers apply, a DPIA is almost certainly required.

## Cookie & Tracking Checklist

For web projects (including PWAs):

- [ ] No tracking cookies loaded before user consent (not even analytics)
- [ ] Cookie banner with granular options (necessary / analytics / marketing)
- [ ] "Reject all" is as prominent as "Accept all"
- [ ] Consent preference stored and respected on return visits
- [ ] Third-party scripts (analytics, ads, social) blocked until consent given
- [ ] Server-side analytics preferred over client-side tracking where possible

## Third-Party Data Sharing

Before integrating any external service that receives personal data:

1. **Check the legal basis** — do you have consent or another basis for this sharing?
2. **Data Processing Agreement** — mandatory under GDPR Art. 28. No DPA = no data sharing
3. **Data transfer** — if the third party is outside the EU/EEA, check for adequacy decisions or Standard Contractual Clauses
4. **Minimise what you share** — send only the fields the service actually needs
5. **Document it** — add the third party to your processing register (Art. 30)

## Quick Reference — Privacy Review for New Features

Before shipping any feature that touches personal data, run through this:

- [ ] **What** personal data does it collect/process?
- [ ] **Why** — what's the specific, documented purpose?
- [ ] **Legal basis** — consent, contract, legitimate interest, or other?
- [ ] **Minimisation** — is every field strictly necessary?
- [ ] **Retention** — when and how is the data deleted?
- [ ] **Subject rights** — can the user access, export, correct, and delete this data?
- [ ] **Security** — encrypted at rest and in transit? Access controlled?
- [ ] **Third parties** — does any external service receive this data? DPA in place?
- [ ] **DPIA** — does this feature trigger any DPIA criteria?
- [ ] **Transparency** — is the user informed about this processing (privacy notice)?
