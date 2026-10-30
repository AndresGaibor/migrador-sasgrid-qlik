# Módulo studio

Réplica de la interfaz de Talend Studio para el modo guiado de migración. Muestra, campo a campo,
qué valor escribir en Studio, y deja marcar cada campo como hecho.

Importa todo desde `@/studio` o desde `./studio` (`index.ts`).

## Componentes

- **`ComponentPanel`**: panel inferior del componente (cabecera, pestañas Basic/Advanced/Dynamic/View/Documentation, filas por `numRow`).
  - `component`, `stepLabel?`, `panels` (snapshot), `values` (sugerencias de la guía), `doneFields`, `onFieldDone(name, done)`.
  - `onOpenSchema?(paramName)`: si se pasa, el botón «...» de SCHEMA_TYPE lo llama y el integrador muestra el editor. Si no, el panel abre su propia ventana con `SchemaEditor`.
  - `initialTab?`: pestaña inicial (por defecto Basic settings).
- **`SchemaEditor`**: tabla «Edit schema». Props `columns: SchemaColumn[]`, `readOnly?` (por defecto true), `onChange?` (solo con `readOnly={false}`). Incluye botón para copiar la tabla en TSV.
- **`JobCanvas`**: lienzo SVG del Job. Props `nodes`, `edges`, `selectedId?`, `onSelect?(id)`. El layout es `layoutJob` (función pura en `canvas-layout.ts`).

## Guía de migración (paneles del plan)

- **`NotMigratedPanel`** (`plan`, `id`): «Lo que NO hace falta migrar». Agrupa `JobPlan.not_migrated` por `what`. Lógica en `not-migrated-model.ts`.
- **`JobletGuide`** (`plan`): una tarjeta por joblet con parámetros, pasos de creación en Studio, copia de nombres, uso por aparición y mini-diagrama. Lógica en `joblet-model.ts`.
- **`FusedBadge`** (`fusedFrom`, `why`): «Reúne N operaciones del SAS» para pasos con `fused_from` de dos o más elementos.
- Estilos en `studio-panels.css`.

## Datos

- `panel-types.ts`: tipos del snapshot (`PanelsSnapshot`), de la guía (`GuideValue`, `GuideValues`, `DoneFields`) y de columnas (`SchemaColumn`).
- `show-if.ts`: evaluador de SHOW_IF / NOT_SHOW_IF (`AND`, `OR`, `NOT`, `==`, `!=`, paréntesis). Lo que no entiende (por ejemplo `compareTo`) se muestra.
- `panel-model.ts`: filas por `numRow`, campos visibles y progreso por pestaña.
- `schema-model.ts`: conversión de filas de la guía a columnas, tipos Talend frente a SAS y TSV.

## Ejemplo

```tsx
import { ComponentPanel, JobCanvas } from "@/studio";

<ComponentPanel
  component="tFileInputDelimited"
  stepLabel="Paso 3 · Leer clientes"
  panels={snapshot}           // rules/talend/component-panels.json
  values={guide.values}       // lo que sugiere el planificador
  doneFields={guide.doneFields}
  onFieldDone={(name, done) => saveDone(name, done)}
/>

<JobCanvas nodes={nodes} edges={edges} selectedId={selected} onSelect={setSelected} />
```

## Notas

- Los controles son de solo lectura: el valor se escribe en Talend Studio, y el chip «Set to:» lo copia.
- Las etiquetas de los campos van en inglés, tal como vienen del snapshot.
- Los estilos están en `studio.css`. Los tres componentes montan su raíz con la clase `.studio-panel` (que define los colores de Studio), así que sus estilos no afectan al resto de la interfaz.
- Pruebas: `bun test src/studio`.
