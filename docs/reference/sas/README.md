# Manuales SAS 9.4 (solo locales)

Conversiones a Markdown de los PDF oficiales. Copyright de SAS Institute: están en `.gitignore` y no se versionan. Para regenerarlos, subirlos de nuevo o convertir los PDF de `~/code/javascript/qlikdojo/packages/web/public/descargas/sas-grid/`.

También está disponible localmente `gridref-9.4-fifth-edition.pdf`, descargado de la [página oficial de Grid Computing in SAS 9.4, Fifth Edition](https://go.documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/gridref/titlepage.htm). Está excluido de Git por copyright; si no aparece en tu clon, vuelve a descargarlo desde la página oficial. La guía mantenida y versionada del proyecto es [SAS Grid: soporte, análisis y migración](../../sas-grid-support.md).

| Archivo local | Fuente | Útil para |
| ------------- | ------ | --------- |
| `macro-language-reference.md` | Macro Language Reference, 5th ed. (602 pp.) | `macro_resolver`: `%LET`, `%MACRO`, `%INCLUDE`, `%DO`, `&&var&i`, `CALL EXECUTE`, resolución y escapes |
| `programmers-guide-essentials.md` | Programmer's Guide: Essentials (930 pp.) | `sas_parser`/`semantic_analysis`: DATA step, MERGE/BY, FIRST./LAST., RETAIN, arrays, PROC SORT/SQL, formatos |
| `language-reference-concepts.md` | Language Reference: Concepts, 6th ed. (916 pp.) | Reglas semánticas: valores missing, fechas, tipos/longitudes, LIBNAME, motor de ejecución del DATA step |
| `gridref-9.4-fifth-edition.pdf` | Grid Computing in SAS 9.4, Fifth Edition (374 pp.) | SAS Grid Manager, proveedores, SASGSUB, opciones, colas, estado/resultados, recuperación y diagnóstico |

Consultar con búsquedas dirigidas (`rg -n "FIRST\.variable" docs/reference/sas/...`), no leer enteros (1–1.7 MB cada uno).
