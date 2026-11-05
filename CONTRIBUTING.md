# Contributing

Thanks for helping. The project is intentionally small and dependency-free.

## Principles

1. Everything stays on the device. No analytics, accounts, servers or AI calls.
2. The app stays a single HTML file under `src/`.
3. It must keep working offline.

## Workflow

1. Fork and create a branch.
2. Edit `src/app.html`, then run `python3 build.py` and serve `dist/` to test.
3. Check the main flows: add a piece, edit colours, generate a week, back up and restore.
4. Bump `VERSION` (patch for small changes, for example `V0.1.38` to `V0.1.39`).
5. Open a pull request describing what changed and why.

## Code style

- Plain JavaScript, no frameworks or build tools
- Short, clear names; keep functions small
- Prefer self-explanatory code over comments
