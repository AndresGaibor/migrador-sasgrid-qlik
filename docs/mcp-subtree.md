# Subtree del MCP

`mcp/talend-mcp/` es un `git subtree` del repositorio público
[AndresGaibor/talend-mcp](https://github.com/AndresGaibor/talend-mcp), rama `main`. El portal lo
versiona junto con su propio código, pero el MCP se publica por separado y no debe contener nada
del portal: ni datos de clientes, ni rutas locales, ni código SAS.

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

Nunca se empuja a `main`. El cambio viaja a una rama y se abre un PR en
`AndresGaibor/talend-mcp`:

```bash
git subtree push --prefix=mcp/talend-mcp talend-mcp-upstream feat/<nombre>
```

El comando imprime la URL del PR. Si la rama ya existe en el remoto, `git subtree push` falla:
borra la rama remota (`git push talend-mcp-upstream --delete feat/<nombre>`) y vuelve a empujar,
o crea otra rama.

## Reglas de convivencia

- Un commit que toca `mcp/talend-mcp/` no toca nada fuera de esa carpeta, salvo `contract/` y sus
  pruebas (el manifiesto y el preset se cambian juntos).
- Nada del portal dentro del subtree: ni nombres de clientes, ni rutas de una máquina concreta,
  ni contenido de ZIP de SAS. Los planes y especificaciones del portal viven en
  `docs/superpowers/` de este repositorio.
- No recargues el Bridge (`bun run bridge:install`) con Jobs o diálogos abiertos en Studio.
- Antes de commitear: `uv run pytest`, `bun test` en `apps/web` y `bun test` en `mcp/talend-mcp`.
