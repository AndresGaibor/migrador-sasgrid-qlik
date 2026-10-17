# Manuales SAS 9.4 (solo locales)

Conversiones a Markdown de los PDF oficiales. Copyright de SAS Institute: están en `.gitignore` y no se versionan. Para regenerarlos, subirlos de nuevo o convertir los PDF de `~/code/javascript/qlikdojo/packages/web/public/descargas/sas-grid/`.

| Archivo local | Fuente | Útil para |
| ------------- | ------ | --------- |
| `macro-language-reference.md` | Macro Language Reference, 5th ed. (602 pp.) | `macro_resolver`: `%LET`, `%MACRO`, `%INCLUDE`, `%DO`, `&&var&i`, `CALL EXECUTE`, resolución y escapes |
| `programmers-guide-essentials.md` | Programmer's Guide: Essentials (930 pp.) | `sas_parser`/`semantic_analysis`: DATA step, MERGE/BY, FIRST./LAST., RETAIN, arrays, PROC SORT/SQL, formatos |
| `language-reference-concepts.md` | Language Reference: Concepts, 6th ed. (916 pp.) | Reglas semánticas: valores missing, fechas, tipos/longitudes, LIBNAME, motor de ejecución del DATA step |

Consultar con búsquedas dirigidas (`rg -n "FIRST\.variable" docs/reference/sas/...`), no leer enteros (1–1.7 MB cada uno).
