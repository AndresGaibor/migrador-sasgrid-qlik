# Progreso

| Fase | Estado | Notas |
| ---- | ------ | ----- |
| F0 | hecha | corpus 50 archivos reales + 8 sintéticos |
| F1 | hecha | importación segura, SQLite, CLI, API |
| F2 | hecha | parser a nivel de sentencia, P0/P1/P2 |
| F3 | hecha | dependencias, capas, Grid |
| F4 | hecha | IR, reglas, planes, exports |
| F5 | hecha | adaptador solo lectura; sin servidor vivo (ver architecture.md) |
| F6 | hecha | `apps/web` React + TS + Vite + Bun, probado con Playwright (`.claude/scripts/e2e_web.mjs`) |
| F7 | hecha | redacción de secretos, importador endurecido, rendimiento, golden tests, guías |

Tests Python: 69 (unit, integration, golden). Tests web: `cd apps/web && bun test`. Nada commiteado: todo en el índice de git.

Pendiente fuera de alcance: servidor talend-mcp vivo para marcar componentes `verified`; piloto con programas reales del cliente (`docs/pilot-report.md`).
