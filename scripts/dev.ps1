# Levanta el MCP, la API y la web del portal con una sola orden.
#
# El MCP arranca con el preset `portal` desde el subtree `mcp/talend-mcp`; la API
# y la web usan sus comandos de desarrollo. Solo gestiona los procesos que crea:
# si un puerto está ocupado, se detiene y avisa en vez de matar al intruso.
#
# Uso:
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1
#   powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 -SkipMcp

[CmdletBinding()]
param(
    [switch]$SkipMcp,
    [switch]$SkipWeb
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$mcpDir = Join-Path $root "mcp\talend-mcp"
$webDir = Join-Path $root "apps\web"

function Assert-Command {
    param([string]$Name, [string]$Hint)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Falta '$Name' en el PATH. $Hint"
    }
}

function Test-PortFree {
    param([int]$Port)
    $listening = Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue
    return -not $listening
}

Assert-Command "bun" "Instálalo desde https://bun.sh y vuelve a ejecutar el script."
Assert-Command "uv" "Instálalo con 'winget install astral-sh.uv' y vuelve a ejecutar el script."

$ports = @()
if (-not $SkipMcp) { $ports += @{ Port = 3927; Label = "MCP" } }
$ports += @{ Port = 8000; Label = "API" }
if (-not $SkipWeb) { $ports += @{ Port = 5173; Label = "web" } }

foreach ($entry in $ports) {
    if (-not (Test-PortFree $entry.Port)) {
        throw ("El puerto $($entry.Port) ($($entry.Label)) ya está en uso. Este script no reinicia " +
            "procesos ajenos: detén el proceso que lo ocupa o usa -SkipMcp/-SkipWeb.")
    }
}

$started = @()

try {
    if (-not $SkipMcp) {
        Write-Host "MCP   http://127.0.0.1:3927/mcp (preset portal)" -ForegroundColor Cyan
        $env:TALEND_MCP_FILTER = "portal"
        $started += Start-Process -FilePath "bun" -ArgumentList "run", "start" `
            -WorkingDirectory $mcpDir -NoNewWindow -PassThru
    }

    Write-Host "API   http://127.0.0.1:8000" -ForegroundColor Cyan
    $started += Start-Process -FilePath "uv" `
        -ArgumentList "run", "uvicorn", "apps.api.main:app", "--host", "127.0.0.1", "--port", "8000" `
        -WorkingDirectory $root -NoNewWindow -PassThru

    if (-not $SkipWeb) {
        Write-Host "Web   http://127.0.0.1:5173" -ForegroundColor Cyan
        $started += Start-Process -FilePath "bun" -ArgumentList "run", "dev", "--", "--host", "127.0.0.1" `
            -WorkingDirectory $webDir -NoNewWindow -PassThru
    }

    if (-not $SkipMcp) {
        Start-Sleep -Seconds 8
        Write-Host "`nDiagnóstico del MCP:" -ForegroundColor Cyan
        Push-Location $mcpDir
        try {
            & bun run doctor
        }
        finally {
            Pop-Location
        }
    }

    Write-Host "`nProcesos en marcha. Ctrl+C detiene solo los que inició este script." -ForegroundColor Green
    Wait-Process -Id $started.Id
}
finally {
    foreach ($process in $started) {
        if (-not $process.HasExited) {
            Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
        }
    }
}
