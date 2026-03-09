# Web / PWA — Language Skill

> Activate for projects using JavaScript, TypeScript, or Progressive Web Apps.
> (Placeholder — expand as web projects are added)

## Style

- **TypeScript preferred** over plain JavaScript
- **Strict mode**: `"strict": true` in `tsconfig.json`
- Use ESM (`import/export`) — avoid CommonJS (`require`) in new code

## Tools

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
