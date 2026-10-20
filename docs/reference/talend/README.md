# Catálogo Talend Studio 8 — Talend Data Fabric

## Alcance activo

La referencia documental elegida es **Talend Studio 8.0 R2026-09**. El catálogo y el planificador están limitados al perfil **Talend Data Fabric (`TP_ALL`)** que seleccionó el usuario. Ese perfil es una decisión de alcance: no demuestra que la licencia esté instalada en un entorno concreto. La UI lo indica expresamente.

La fuente de disponibilidad es Qlik Help: [componentes y licencias](https://help.qlik.com/talend/en-US/studio-components-availability/8.0/), con los datos dinámicos de `https://help.qlik.com/talend/js/components/componentList.json`. El snapshot `rules/talend/official-component-inventory.json` conserva la respuesta oficial completa —versión `8.0.1.20261015_1208-patch`, 1.192 nombres y 1.399 registros— para poder aplicar el filtro de licencia. **No todo ese inventario se publica ni alimenta el planificador**.

El índice de guías `rules/talend/component-documentation-index.json` registra los **1.147 componentes actuales del perfil `TP_ALL`** y conserva el estado de instalación. La selección de usuario es archivar por defecto todo lo que Studio no instala de fábrica: quedan **870 componentes activos**, con **856 fichas documentadas y 14 excepciones**. Se archivan **268 componentes opcionales** y **9 retirados del release** en `rules/archive/talend/studio8-default-install-exclusions.json`; las razones y fuentes de Qlik se conservan ahí. El recolector, catálogo, API, planificador y pruebas de candidatos filtran por el estado activo. La ficha completa del índice no hace que un componente archivado aparezca en la UI. Este archivo es una decisión revisada a partir de páginas oficiales; actualízalo solo tras volver a comprobar la disponibilidad en Studio 8.0 R2026-09.

El índice excluye además componentes de otros perfiles, frameworks no vigentes y nombres heredados fuera de la disponibilidad actual. Del inventario bruto se mantienen fuera del perfil 44 nombres de Studio no vigentes (42 de Spark Streaming y 2 obsoletos) y `tQVDInput`, cuya disponibilidad registrada es solo Qlik Talend Cloud. Cada guía mantiene framework y páginas/secciones oficiales; no copia la prosa de Qlik. Una excepción documental no se presenta como compatibilidad comprobada.

El XML comunitario usado para algunos metadatos internos no es una autoridad de compatibilidad ni una fuente documental. `rules/talend/components.json` conserva 539 registros internos; `load_catalog` cruza sus nombres con el índice y excluye los que no estén activos antes de que lleguen al adaptador/planificador. El catálogo de la UI usa las fichas y URLs de Qlik. Los nombres no vigentes y los datos solo comunitarios están en `rules/archive/talend/non-current-studio8-components.json` y `rules/archive/talend/non-current-component-data.json`; el audit anterior está en `rules/archive/talend/catalog-audit-r2026-09.json`. Los tests activos verifican que los nombres archivados no se conviertan en candidatos.

La caché Markdown y `docs/reference/talend/index.json` son locales e ignorados por Git. Pueden conservar resultados históricos del recolector, pero no son el catálogo activo. El índice operativo es la lista permitida para UI, API y planificador.

## Recolectar y regenerar

1. Actualiza la disponibilidad oficial: `.venv/bin/python tools/sync_talend_official_inventory.py`.
2. Revisa `rules/archive/talend/studio8-default-install-exclusions.json` contra la disponibilidad y la instalación predeterminada documentadas por Qlik. Resincroniza páginas oficiales y subpáginas de configuración solo para componentes activos: `uv run --script tools/fetch_talend_docs.py --workers 4 --refresh`. Para una prueba acotada usa `--only tMap,cAMQP`; ese modo no representa cobertura completa.
3. Regenera el índice de guías: `.venv/bin/python tools/build_talend_component_guides.py`. El proceso limita la selección a `TP_ALL`, los frameworks vigentes y los componentes no archivados.
4. Ejecuta las pruebas Python relevantes y el chequeo de tipos/tests de `apps/web` antes de publicar cambios.

`index.json` conserva estado por página, URL solicitada/resuelta, redirecciones y ciclo de vida. Los estados `partial`, `truncated`, `not_found`, `page_mismatch`, `network_error` y `external_redirect` requieren revisión; no cuentan como una ficha válida. `redirected: null` significa que un registro antiguo no conservó la URL original.

## Configuración global de Studio

[`studio-configuration.md`](studio-configuration.md) reúne las 12 áreas del apéndice oficial y las 23 preferencias enlazadas: preferencias de Studio, ajustes de proyecto y personalización del workspace. Fuente: Talend Studio 8.0 R2026-09; las páginas índice estaban actualizadas al 1 de octubre de 2026. Qlik documenta que algunas preferencias son valores predeterminados para Jobs nuevos y que los ajustes de proyecto se pueden exportar/importar como XML.

## Límites de la evidencia

La disponibilidad oficial y la ficha documental no prueban que el componente esté instalado, que la licencia efectiva coincida con `TP_ALL`, ni que una migración sea semánticamente equivalente. Las propiedades derivadas de XML comunitario son metadatos auxiliares y requieren validación en Talend Studio; no se presentan como propiedades oficiales verificadas. La lista de alcance de migración tiene **33 candidatos principales y 9 alternativas condicionales**; ninguna referencia nombres archivados. Una alternativa no es una recomendación aprobada, y los casos que requieren diseño siguen fuera del alcance.
