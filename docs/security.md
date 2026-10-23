# Seguridad

- Archivos importados = entrada no confiable: límite de tamaño y cantidad (`SGM_MAX_FILE_BYTES`, `SGM_MAX_FILES`), rechazo de rutas que escapen del directorio del proyecto (zip-slip, symlinks), nada se ejecuta.
- ZIP: validar cada entrada antes de extraer.
- Sin conexión automática a sistemas de producción.
- Secretos (credenciales, claves, variables) no se copian a informes; enmascarar al leer configs.
- `talend-mcp`: solo en loopback/transporte configurado, nunca expuesto a red pública. El portal solo usa la tool de escritura `talend_job_apply_custom_spec` desde el botón explícito de una guía y se puede bloquear con `TALEND_MCP_READONLY=true`. No llama a tools de ejecución de Jobs.

## Controles implementados (F7)

- **Redacción de credenciales** (`domain/redaction.py`): `password=`, `pw=`, `pwd=`, `token=`, `secret=` en `libname`/`connect to`/`filename`/`options`, `%let` con nombre sensible y `NOMBRE=valor`/`-password valor` en scripts shell se enmascaran como `***` al leer cada archivo. Ningún análisis, dependencia, plan o informe contiene el original (test `test_no_secret_in_any_derived_output`). La **copia fuente** en `data/projects/<id>/src` es literal: es dato del usuario en su disco; no se expone por la API.
- **Importación**: sin symlinks, límites de tamaño/cantidad/total (`SGM_MAX_FILE_BYTES`, `SGM_MAX_FILES`, `SGM_MAX_TOTAL_BYTES`), rutas con `..` rechazadas (zip-slip), carpeta de datos dentro de la fuente excluida (evita copia recursiva) y fuente dentro de la propia copia rechazada (evitaba borrarla al reimportar). `POST /api/projects/uploads` crea un proyecto independiente por ZIP; la API no ejecuta el contenido importado.
- **API**: `SGM_IMPORT_ROOTS` limita las rutas importables (403 fuera de ellas). Si no se define, cualquier ruta local es importable: usar solo en máquina de un usuario, escuchando en `127.0.0.1`.
- **Talend**: allowlist `policy.assert_allowed` en cada llamada; `inspect_job` solo acepta rutas `.item`. La escritura se limita a la especificación estructurada de la guía y al destino aislado del proyecto. El resultado se guarda en SQLite para recuperación y deduplicación; un conflicto no sobrescribe un Job ajeno.
- El análisis y los planes funcionan sin Talend.
- **Despliegue**: `ops/systemd/` (API en `127.0.0.1:38421`, datos en `/var/lib/sgm`, `SGM_IMPORT_ROOTS=/var/lib/sgm/imports`, unidad endurecida). La app **no tiene autenticación**: el acceso remoto solo por Tailscale Serve (tailnet), nunca público. La subida de ZIP (`POST /api/projects/{id}/uploads`) pasa por las mismas validaciones que una carpeta.
