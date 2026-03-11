---
name: web-pwa
description: JavaScript/TypeScript and Progressive Web App conventions — ESM, Vite, eslint, prettier, service workers, and caching strategies. Activate for any web or PWA project.
---

# Web / PWA — Language Skill

> Activate for projects using JavaScript, TypeScript, or Progressive Web Apps.
> (Placeholder — expand as web projects are added)

## Web Style

- **TypeScript preferred** over plain JavaScript
- **Strict mode**: `"strict": true` in `tsconfig.json`
- Use ESM (`import/export`) — avoid CommonJS (`require`) in new code

## Web Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `eslint` | Linting | `npx eslint .` |
| `prettier` | Formatting | `npx prettier --write .` |
| `tsc` | Type checking | `npx tsc --noEmit` |
| `vitest` / `jest` | Testing | `npm test` |
| `npm audit` | Security | `npm audit` |

## PWA Patterns

- Service worker for offline support
- Web App Manifest for installability
- Cache-first strategy for static assets
- Network-first for API calls

**Minimal service worker example (cache-first for static, network-first for API):**

```js
const CACHE_NAME = "v1";
const STATIC_ASSETS = ["/", "/index.html", "/style.css", "/app.js"];

self.addEventListener("install", (e) =>
  e.waitUntil(caches.open(CACHE_NAME).then((c) => c.addAll(STATIC_ASSETS)))
);

self.addEventListener("fetch", (e) => {
  if (e.request.url.includes("/api/")) {
    // Network-first for API calls
    e.respondWith(
      fetch(e.request).catch(() => caches.match(e.request))
    );
  } else {
    // Cache-first for static assets
    e.respondWith(
      caches.match(e.request).then((r) => r || fetch(e.request))
    );
  }
});
```

## Build Tools

- **Vite** preferred for new projects (fast dev server, ESM-native)
- **esbuild** for library bundling
- Configure in `vite.config.ts` or `esbuild.mjs`

## Project Setup Pattern

```bash
npm install                # Install deps
npm run dev                # Dev server
npm run build              # Production build
npm run preview            # Preview production build
```
