# Atajo de `uv run sgm dev`: levanta el MCP (preset portal), la API y la web.
#
# El lanzador vive en src/sas_grid_migrator/cli/dev.py. Agrupa los procesos en un
# Job de Windows para que Ctrl+C no deje hijos vivos y no mata servidores ajenos.
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 --no-mcp

Set-Location (Split-Path -Parent $PSScriptRoot)
uv run sgm dev @args
exit $LASTEXITCODE
