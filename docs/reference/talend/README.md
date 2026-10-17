# Documentación de componentes Talend (local)

Descargada de help.qlik.com con `uv run tools/fetch_talend_docs.py` (Markdown por componente + `index.json`).
No se versiona: es contenido de Qlik. Lo que sí se versiona es el catálogo estructurado `rules/talend/components.json`
(nombres internos de parámetros, campos, conectores, valores por defecto y drivers), generado desde las definiciones
XML de Talaxie (Apache-2.0) con `tools/build_talend_catalog.py`.
