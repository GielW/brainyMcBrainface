---
name: web-design
description: Frontend craft rules for building and reviewing visual web pages. Use whenever writing HTML/CSS, designing UI, taking screenshots, matching a reference image, or making any visual web change — even small tweaks.
---

# Web Design — Frontend Craft Skill

> Universal rules for frontend website design. Apply whenever building or reviewing visual web pages.

---

## Session Start

**Invoke this skill before writing any frontend code — every session, no exceptions.**

## Reference Image Workflow

### When a reference image is provided

- Match layout, spacing, typography, and color **exactly**
- Swap in placeholder content (images via `https://placehold.co/`, generic copy)
- Do **not** improve or add to the design

### When no reference image is provided

- Design from scratch with high craft (see Anti-Generic Guardrails below)

### Comparison Loop

1. Screenshot your output
2. Compare against the reference — be specific: "heading is 32px but reference shows ~24px", "card gap is 16px but should be 24px"
3. Fix mismatches, re-screenshot
4. Do **at least 2 comparison rounds**. Stop only when no visible differences remain or user says so

### What to Check

- Spacing / padding
- Font size / weight / line-height
- Colors (exact hex)
- Alignment
- Border-radius
- Shadows
- Image sizing

## Local Server Rule

- **Always serve on localhost** — never screenshot a `file:///` URL
- Start the dev server in the background before taking any screenshots
- If the server is already running, do not start a second instance
- Project-specific server command goes in the project file (e.g., `node serve.mjs`)

## Screenshot Tooling

- Use Puppeteer (or project-specific screenshot script) to capture from `localhost`
- Screenshots should auto-increment (`screenshot-N.png`) and never overwrite
- After screenshotting, read the PNG with the image analysis tool to compare
- Project-specific paths (Puppeteer cache, script location) belong in the project file, not here

## Output Defaults

- Single `index.html` file, all styles inline, unless user says otherwise
- **Tailwind CSS via CDN**: `<script src="https://cdn.tailwindcss.com"></script>`
- Placeholder images: `https://placehold.co/WIDTHxHEIGHT`
- **Mobile-first responsive**

## Brand Assets

- Always check the `brand_assets/` folder (or equivalent) before designing
- May contain logos, color guides, style guides, or images
- If assets exist, **use them** — do not use placeholders where real assets are available
- If a logo is present, use it. If a color palette is defined, use those exact values — do not invent brand colors

## Anti-Generic Guardrails

| Element | Rule |
|---------|------|
| **Colors** | Never use default Tailwind palette (indigo-500, blue-600, etc.). Pick a custom brand color and derive from it |
| **Shadows** | Never use flat `shadow-md`. Use layered, color-tinted shadows with low opacity |
| **Typography** | Never use the same font for headings and body. Pair a display/serif with a clean sans. Tight tracking (`-0.03em`) on large headings, generous line-height (`1.7`) on body |
| **Gradients** | Layer multiple radial gradients. Add grain/texture via SVG noise filter for depth |
| **Animations** | Only animate `transform` and `opacity`. Never `transition-all`. Use spring-style easing |
| **Interactive states** | Every clickable element needs hover, focus-visible, and active states — no exceptions |
| **Images** | Add gradient overlay (`bg-gradient-to-t from-black/60`) and color treatment layer with `mix-blend-multiply` |
| **Spacing** | Use intentional, consistent spacing tokens — not random Tailwind steps |
| **Depth** | Surfaces need a layering system (base → elevated → floating) — not all at the same z-plane |

## Hard Rules

- Do **not** add sections, features, or content not in the reference — scope creep breaks client trust and makes comparison impossible
- Do **not** "improve" a reference design — match it. The client chose that design; unsolicited changes waste review cycles
- Do **not** stop after one screenshot pass — first passes always miss spacing/color details that only show up on comparison
- Do **not** use `transition-all` — it triggers expensive layout recalculations and animates properties you didn't intend (width, height, padding)
- Do **not** use default Tailwind blue/indigo as primary color — it instantly signals "undesigned template" to anyone who's seen Tailwind defaults

## Accessibility (a11y)

> Source: Gap identified during cross-repo research (March 2026). WCAG 2.1 AA is the baseline for all web projects.

Accessibility is not optional. Every page shipped must be usable by people who navigate with keyboards, screen readers, or assistive technology.

### Non-Negotiable Rules

1. **Semantic HTML first** — use `<nav>`, `<main>`, `<article>`, `<button>`, `<label>` etc. for their intended purpose. Never use `<div>` with `onClick` as a button
2. **All images need `alt` text** — decorative images get `alt=""` (empty, not missing). Informative images get descriptive alt text
3. **All form inputs need labels** — use `<label for="...">` or `aria-label`. Placeholder text is **not** a label
4. **Colour is never the only indicator** — if red means error, also add an icon or text. People with colour blindness need a second signal
5. **Contrast ratios** — text must meet WCAG AA minimums: 4.5:1 for normal text, 3:1 for large text (18px+ bold or 24px+ regular)

### Keyboard Navigation

- Every interactive element must be focusable and operable with keyboard alone
- Tab order must follow visual reading order (don't override `tabindex` unless necessary)
- Custom components (dropdowns, modals, tabs) need proper `role`, `aria-*` attributes, and keyboard handlers
- Focus trapping in modals — Tab cycles within the modal, Escape closes it
- Always provide visible `:focus-visible` styles — never remove outlines without a replacement

### ARIA — Use Sparingly

- ARIA supplements, it doesn't replace, semantic HTML
- If a native HTML element does what you need (`<button>`, `<select>`, `<details>`), use it — don't recreate it with ARIA
- Common patterns:
  - `aria-expanded` for collapsible sections
  - `aria-live="polite"` for dynamic content updates (toast notifications, live search results)
  - `role="alert"` for urgent error messages
  - `aria-describedby` to associate error messages with form inputs

### Testing Accessibility

| Method | Tool | Catches |
|--------|------|---------|
| Automated scan | Lighthouse, axe-core | Missing alt text, contrast, ARIA misuse |
| Keyboard walkthrough | Manual (Tab, Enter, Escape) | Focus order, trapped focus, unreachable elements |
| Screen reader test | NVDA (Windows), VoiceOver (Mac) | Reading order, missing announcements, confusing labels |

- Run Lighthouse accessibility audit as part of screenshot comparison loop
- Fix any score below 90 before delivering
