# Seguridad

- Archivos importados = entrada no confiable: límite de tamaño y cantidad (`SGM_MAX_FILE_BYTES`, `SGM_MAX_FILES`), rechazo de rutas que escapen del directorio del proyecto (zip-slip, symlinks), nada se ejecuta.
- ZIP: validar cada entrada antes de extraer.
- Sin conexión automática a sistemas de producción.
- Secretos (credenciales, claves, variables) no se copian a informes; enmascarar al leer configs.
- `talend-mcp`: solo local/transporte configurado, nunca expuesto a red pública. Solo lectura por defecto; escritura y ejecución exigen autorización explícita y están deshabilitadas en el adaptador.

## Controles implementados (F7)

- **Redacción de credenciales** (`domain/redaction.py`): `password=`, `pw=`, `pwd=`, `token=`, `secret=` en `libname`/`connect to`/`filename`/`options`, `%let` con nombre sensible y `NOMBRE=valor`/`-password valor` en scripts shell se enmascaran como `***` al leer cada archivo. Ningún análisis, dependencia, plan o informe contiene el original (test `test_no_secret_in_any_derived_output`). La **copia fuente** en `data/projects/<id>/src` es literal: es dato del usuario en su disco; no se expone por la API.
- **Importación**: sin symlinks, límites de tamaño/cantidad/total, rutas con `..` rechazadas (zip-slip), carpeta de datos dentro de la fuente excluida (evita copia recursiva) y fuente dentro de la propia copia rechazada (evitaba borrarla al reimportar).
- **API**: `SGM_IMPORT_ROOTS` limita las rutas importables (403 fuera de ellas). Si no se define, cualquier ruta local es importable: usar solo en máquina de un usuario, escuchando en `127.0.0.1`.
- **Talend**: allowlist de solo lectura (`policy.assert_allowed`) en cada llamada; `inspect_job` solo acepta rutas `.item`.
- El análisis y los planes funcionan sin Talend.
