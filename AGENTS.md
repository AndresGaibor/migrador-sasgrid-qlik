# AGENTS.md

Guía para agentes de IA que trabajan en **migrador-sasgrid-qlik**, el portal que analiza
programas SAS y prepara Jobs de Talend. Si algo de este archivo choca con una costumbre tuya,
gana este archivo.

## Qué es cada carpeta

| Ruta | Qué es |
|---|---|
| `src/sas_grid_migrator/` | Núcleo Python: ingesta, parser SAS, análisis, planificador y adaptador de Talend. |
| `apps/api/` | API FastAPI (`apps.api.main:app`). No tiene lógica de negocio: llama al núcleo. |
| `apps/web/` | Interfaz React + Vite. El permiso de escritura vive en Configuración. |
| `contract/portal-tools.json` | Manifiesto del contrato con el MCP: tools de lectura, tool de escritura y campos obligatorios. |
| `mcp/talend-mcp/` | Servidor MCP, como `git subtree` del repositorio público [AndresGaibor/talend-mcp](https://github.com/AndresGaibor/talend-mcp). |
| `docs/superpowers/` | Planes y especificaciones del portal (incluidos los que antes vivían dentro del MCP). |
| `tests/` | Pruebas de Python con `pytest`. Las de web viven junto al código, en `apps/web/src/**/*.test.mjs`. |

El MCP es un proyecto aparte con sus propias reglas: lee
[mcp/talend-mcp/AGENTS.md](mcp/talend-mcp/AGENTS.md) antes de tocar nada dentro del subtree. Este
archivo no lo repite.

## Regla de oro: una tool nueva del portal

Toda tool del MCP que el portal use se declara en tres lugares y se comprueba con la prueba de
contrato:

1. `contract/portal-tools.json` (tools de lectura o la única tool de escritura).
2. El preset `portal` del MCP, en `mcp/talend-mcp/src/server/registered-tools/preset-sets.ts`.
3. La prueba `tests/integration/test_mcp_contract.py`, que arranca el MCP real con ese preset.

La allowlist de `src/sas_grid_migrator/talend_adapter/policy.py` se deriva del manifiesto: no la
edites a mano. Si el manifiesto cambia, cambia también el preset y la prueba en el mismo commit.

## Permisos y límites

- El permiso de escritura se administra **solo** desde la vista Configuración y se guarda en la
  base. Nunca lo controles con una variable de entorno.
- `TALEND_APPLY_FOLDER` debe quedar dentro de `Process/`.
- El portal crea y lee Jobs; **no** ejecuta, compila ni publica Jobs migrados.
- No recargues el Bridge de Studio (`bun run bridge:install`) con Jobs o diálogos en curso.

## Comandos de verificación

```bash
uv sync                                   # dependencias de Python
uv run pytest                             # pruebas de Python
cd apps/web && bun install && bun test && bun run typecheck
cd mcp/talend-mcp && bun install && bun test && bun run typecheck
```

Para levantar todo el entorno: `uv run sgm dev` (o `scripts/dev.ps1`, que lo invoca). Arranca el MCP con
el preset `portal` (`bun run start:server`), la API en `127.0.0.1:8000` y la web en `127.0.0.1:5173`;
`--no-mcp` omite el MCP. No reinstala el Bridge ni mata procesos ajenos: para instalar el plugin usa
`bun run bridge:install` en `mcp/talend-mcp` con Studio sin Jobs ni diálogos en curso.

## Subtree del MCP

Cómo traer cambios del upstream y cómo publicar los del portal: [docs/mcp-subtree.md](docs/mcp-subtree.md).
Un commit que toca `mcp/talend-mcp/` no toca nada fuera de esa carpeta salvo `contract/` y sus
pruebas.
