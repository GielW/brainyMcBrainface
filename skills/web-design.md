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

- Do **not** add sections, features, or content not in the reference
- Do **not** "improve" a reference design — match it
- Do **not** stop after one screenshot pass
- Do **not** use `transition-all`
- Do **not** use default Tailwind blue/indigo as primary color
