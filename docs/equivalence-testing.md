# Pruebas de equivalencia SAS ↔ Talend

El migrador no ejecuta SAS ni Talend: genera, por paso, los **casos de validación** (`ValidationCase`) que una persona ejecuta tras construir el Job. Un paso solo pasa a `validado_manualmente` cuando sus casos coinciden con SAS.

## Datos de prueba

1. Tomar una muestra **estable** y pequeña de cada dataset de entrada (idealmente con casos borde: nulos/missing, duplicados, fechas extremas, texto con mayúsculas/espacios, clave sin pareja en joins).
2. Congelar la muestra: mismo archivo para SAS y para Talend. Anotar la fecha y el `sha256` del extracto.
3. Ejecutar el programa SAS sobre la muestra (fuera de esta herramienta) y exportar cada dataset de salida a CSV con las mismas columnas y orden.

## Casos por tipo (`kind`)

| kind | Qué comparar | Tolerancia |
| ---- | ------------ | ---------- |
| `row_count` | Filas de salida por dataset | Exacta |
| `schema` | Nombres, tipos y longitudes de columnas | Exacta; documentar cambios de tipo |
| `nulls` | Cuántos nulos por columna; en SAS `.` y `""` son missing | Exacta |
| `duplicates` | Claves repetidas antes/después (`nodupkey`, `first./last.`) | Exacta |
| `numeric` | Sumas, medias, mínimos y máximos por columna | Definir epsilon (p. ej. 1e-9 relativo); SAS usa doble precisión, igual que Java `double`, pero **no** `BigDecimal` |
| `dates` | Valores de fecha/hora: SAS cuenta días desde 1960-01-01 y segundos desde 1960 | Exacta tras convertir |
| `ordering` | Orden tras `proc sort` / `order by` | Exacta si el orden está definido; empates: fijar clave secundaria |
| `aggregates` | Resultado de `group by`/`proc means` por grupo | Igual que `numeric` |
| `empty` | Entrada vacía produce salida vacía sin error | Exacta |

## Riesgos de semántica a revisar siempre

- **Missing numérico**: en SAS es menor que cualquier número (`x < 5` incluye missing); en Java `null` no se compara. El traductor lo avisa en cada expresión afectada.
- **Comparación de texto**: SAS ignora blancos finales al comparar; Java no.
- **Merge sin `by` exacto** y `first./last.`: dependen del orden previo; verificar con datos desordenados.
- **Macro con efectos** (`call execute`, `%include` dinámico): el plan los marca `por_determinar`; no hay caso automático.

## Procedimiento

1. Construir el Job en Talend Studio siguiendo `index.md` y el plan del programa.
2. Ejecutar con la muestra congelada y exportar salidas a CSV.
3. Comparar con una herramienta externa (diff de CSV ordenados, o script con tolerancias). Esta herramienta no compara datos: así no maneja datos de producción.
4. Registrar el resultado en la UI (estado del paso + nota con el `sha256` de la muestra).
5. Un Job pasa cuando **todos** sus pasos están `verificado`/`validado_manualmente`/`descartado` (con motivo).
