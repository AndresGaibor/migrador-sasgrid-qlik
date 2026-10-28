# Subtree del MCP

`mcp/talend-mcp/` es un `git subtree` del repositorio
[AndresGaibor/talend-mcp](https://github.com/AndresGaibor/talend-mcp), rama `main`. El portal lo
versiona junto con su propio código, pero el MCP se publica por separado y no debe contener nada
del portal: ni datos de clientes, ni rutas locales, ni código SAS.

Ambos repositorios son propios y se pueden modificar. Además del subtree, existe un clon
independiente del MCP en `../talend-mcp/` (`~/code/talend-mcp`), con `origin` en el mismo GitHub.
El flujo para no pisarse:

```text
portal/mcp/talend-mcp  --subtree push-->  talend-mcp (GitHub)  <--push--  ../talend-mcp
portal/mcp/talend-mcp  <--subtree pull--  talend-mcp (GitHub)  --pull-->  ../talend-mcp
```

GitHub (`AndresGaibor/talend-mcp`, `main`) es el punto de encuentro: el cambio viaja siempre por
él, nunca copiando archivos a mano entre carpetas.

Remotos:

```bash
git remote -v
# origin               https://github.com/AndresGaibor/migrador-sasgrid-qlik.git
# talend-mcp-upstream  https://github.com/AndresGaibor/talend-mcp.git
```

## Traer cambios del upstream

Con el árbol limpio (`git status` sin cambios):

```bash
git subtree pull --prefix=mcp/talend-mcp talend-mcp-upstream main --squash
```

Después del pull, corre las pruebas del MCP y la prueba de contrato del portal antes de commitear:

```bash
cd mcp/talend-mcp && bun test && bun run typecheck
cd ../.. && uv run pytest tests/integration/test_mcp_contract.py
```

## Publicar cambios del portal en el MCP

Es un repositorio propio: el cambio puede ir directo a `main` o por una rama con PR, y el agente
puede fusionar el PR él mismo (`gh pr merge <n> --repo AndresGaibor/talend-mcp --merge`). Usa
la rama con PR cuando quieras dejar el cambio revisable o que corra el CI antes de entrar a
`main`; usa `main` directo para cambios pequeños y ya verificados. El permiso para hacer commit y
push sigue siendo del usuario: se ejecuta cuando él lo pide.

Directo a `main` (con el árbol limpio, y tras `bun test` y `bun run typecheck` en el MCP):

```bash
git subtree pull --prefix=mcp/talend-mcp talend-mcp-upstream main --squash   # partir al día
git subtree push --prefix=mcp/talend-mcp talend-mcp-upstream main
```

Por rama y PR, y fusión del PR:

```bash
git subtree push --prefix=mcp/talend-mcp talend-mcp-upstream fix/<nombre>
gh pr create --repo AndresGaibor/talend-mcp --base main --head fix/<nombre> --fill
gh pr merge <n> --repo AndresGaibor/talend-mcp --merge
```

Si la rama ya existe en el remoto, `git subtree push` falla: borra la rama remota
(`git push talend-mcp-upstream --delete fix/<nombre>`) y vuelve a empujar, o crea otra rama.
Después de fusionar, actualiza el clon (`git pull --ff-only` en `../talend-mcp`) y trae `main`
al portal con `git subtree pull`.

## Trabajar en el clon `../talend-mcp/`

Para cambios que solo tocan el MCP:

```bash
cd ../talend-mcp && git pull --ff-only     # partir de main al día
# ...editar, bun test && bun run typecheck, commit, push...
cd ../migrador-sasgrid-qlik
git subtree pull --prefix=mcp/talend-mcp talend-mcp-upstream main --squash
```

Si el clon tiene archivos sin trackear o cambios sin commitear que no son tuyos, no los toques.
`git subtree pull` exige el árbol del portal limpio: commitea o guarda antes lo pendiente.

## Reglas de convivencia

- Un commit que toca `mcp/talend-mcp/` no toca nada fuera de esa carpeta, salvo `contract/` y sus
  pruebas (el manifiesto y el preset se cambian juntos).
- Nada del portal dentro del subtree: ni nombres de clientes, ni rutas de una máquina concreta,
  ni contenido de ZIP de SAS. Los planes y especificaciones del portal viven en
  `docs/superpowers/` de este repositorio.
- No recargues el Bridge (`bun run bridge:install`) con Jobs o diálogos abiertos en Studio.
- Antes de commitear: `uv run pytest`, `bun test` en `apps/web` y `bun test` en `mcp/talend-mcp`.
