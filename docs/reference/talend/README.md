# Documentación de componentes Talend (local)

Las páginas Markdown descargadas de help.qlik.com con `tools/fetch_talend_docs.py` se mantienen localmente y no se
versionan porque son contenido de Qlik. El catálogo estructurado `rules/talend/components.json` se genera con
`tools/build_talend_catalog.py` desde las definiciones XML de Talaxie (Apache-2.0), un espejo comunitario que no es
fuente oficial de Qlik/Talend.

La auditoría oficial inicial de los componentes recomendados está versionada en `rules/talend/catalog-audit.json` y
se incorpora al catálogo generado. Registra referencias de Qlik Help, fecha, versión documental, estado y limitaciones.
`partially_verified` significa que nombre/familia/propósito y la página de propiedades se contrastaron documentalmente;
no implica que las claves internas del XML coincidan ni que el componente se haya probado en Talend Studio.
`needs_review` indica que falta confirmar una ficha oficial vigente o cotejar propiedades esenciales.

## Alcance de versión y mappings

La versión documental objetivo de este alcance es **Talend Studio 8.0 R2026-09**, según las [notas oficiales de esa
versión](https://help.qlik.com/talend/en-US/release-notes/8.0/r2026-09-studio), con Jobs Standard como marco base. Esta
es una referencia documental elegida para la auditoría. Se detectó Talend Studio Lite **8.0.1 patch R2026-08v1** en
`C:\Talend\8.0.1\studio`; la edición/licencia y el acceso a un workspace no se confirmaron. La validación interactiva
de componentes sigue pendiente y el parche instalado no coincide con la línea mensual documental R2026-09. Consulta
[`talend-studio-validation.md`](../talend-studio-validation.md) para la evidencia y el resultado registrado.

`catalog-audit.json` delimita el trabajo usando las opciones concretas de `rules/mappings/talend-components.json` y las
entradas/salidas configuradas por motor, sin editar ese archivo. El primer conjunto contiene **38 candidatos principales**
y **9 alternativas condicionales** (47 nombres únicos). Una alternativa no equivale a una recomendación aprobada; los
casos `stateful`, `dynamic_code`, `unsupported` y `report` siguen fuera del alcance del catálogo hasta definir diseño.
`maintenance` queda con decisión pendiente aunque `tDBRow` se conserva en el conjunto por estar nombrado en la regla.

La auditoría conserva `needs_review` cuando la evidencia oficial no confirma el componente para el framework requerido.
Por ejemplo, Qlik indica que `tHiveOutput` no existe en Jobs Standard y documenta `tHiveLoad` como la opción Standard;
por ello la discrepancia del mapping Hive queda pendiente y no se sustituye automáticamente. La lista de alcance no
declara compatibilidad de ejecución ni equivalencia semántica. No se copian parámetros propietarios: las propiedades
solo se incorporarán cuando exista evidencia oficial comprobable.
