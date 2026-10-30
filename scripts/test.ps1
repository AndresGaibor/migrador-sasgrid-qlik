# Pruebas de Python del portal. Detalle en la sección «Tests» de AGENTS.md.
#
#   scripts/test.ps1               rápida: en paralelo, con caché, sin las pruebas `slow` (ciclo de desarrollo)
#   scripts/test.ps1 -Incremental  solo lo afectado por los cambios de código (pytest-testmon)
#   scripts/test.ps1 -Full         todo, incluidas las `slow` (MCP real, corpus completo); es lo que corre el CI
#   scripts/test.ps1 -Clean        borra .test-cache y los datos de pytest-testmon
#   Cualquier otro argumento se pasa a pytest: scripts/test.ps1 tests/unit/test_golden.py -k p0
#
# Usa `uv run --no-sync` porque `uv run` sin --no-sync falla si un proceso bloquea sgm.exe.
# Si el proyecto no tiene .venv, ejecuta `uv sync` una vez antes.

param(
    [switch]$Incremental,
    [switch]$Full,
    [switch]$Clean,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PytestArgs = @()
)

$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    if ($Clean) {
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue (Join-Path $root ".test-cache")
        Get-ChildItem -Force -Path $root -Filter ".testmondata*" -ErrorAction SilentlyContinue | Remove-Item -Force
        Write-Host "Cache de pruebas y datos de testmon borrados."
        exit 0
    }

    $pyArgs = @("run", "--no-sync", "pytest")
    if ($Full) { $pyArgs += "--runslow" }
    if ($Incremental) { $pyArgs += "--testmon" }
    $pyArgs += $PytestArgs

    & uv @pyArgs
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
