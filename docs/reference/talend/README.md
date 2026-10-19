# Documentación de componentes Talend (local)

Descargada de help.qlik.com con `uv run tools/fetch_talend_docs.py --refresh` (Talend 8.0, Markdown por componente + `index.json`; sigue redirecciones para obtener las versiones vigentes). Actualizada contra la documentación oficial el 2026-10-19: 577/577 páginas descargadas.
No se versiona: es contenido de Qlik. Lo que sí se versiona es el catálogo estructurado `rules/talend/components.json`
(nombres internos de parámetros, campos, conectores, valores por defecto y drivers), generado desde las definiciones
XML de Talaxie (Apache-2.0) con `tools/build_talend_catalog.py`. El inventario oficial Qlik R2026-01 cuenta con 693
componentes; 295 no tienen definición de parámetros en el origen abierto y se muestran como inventario, no como esquema.
