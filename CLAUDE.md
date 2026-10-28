# CLAUDE.md

Las instrucciones de este repositorio viven en **[AGENTS.md](AGENTS.md)**. Léelas primero: son la
fuente de verdad para cualquier agente de IA.

Lo imprescindible:

- **Dos repositorios, ambos editables.** Este portal (`migrador-sasgrid-qlik`) y el MCP
  [AndresGaibor/talend-mcp](https://github.com/AndresGaibor/talend-mcp), que vive aquí como
  `mcp/talend-mcp/` (git subtree) y también como clon independiente en `../talend-mcp/`. Si una
  tarea necesita tocar el MCP, hazlo; no hace falta pedir permiso aparte.
- **Antes de editar el MCP:** lee [mcp/talend-mcp/AGENTS.md](mcp/talend-mcp/AGENTS.md) y parte de
  `main` al día (`git pull` en el clon o `git subtree pull` en el portal). No edites lo mismo en
  las dos copias a la vez.
- **Flujo cruzado:** MCP primero (commit y push), luego `git subtree pull`, luego el commit del
  portal. Detalle en [docs/mcp-subtree.md](docs/mcp-subtree.md).
- **Tool nueva del portal:** manifiesto `contract/portal-tools.json`, preset `portal` del MCP y
  `tests/integration/test_mcp_contract.py`, en el mismo commit.
- **Verifica:** `uv run pytest`, `bun test` y `bun run typecheck` en `apps/web` y en
  `mcp/talend-mcp`.
- **Commits y push** solo cuando el usuario lo pide. Al terminar, di qué repos tocaste y qué quedó
  sin empujar.
