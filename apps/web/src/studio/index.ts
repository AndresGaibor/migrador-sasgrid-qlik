// Punto de entrada del módulo studio: réplica de la UI de Talend Studio para el modo guiado.
export { ComponentPanel, type ComponentPanelProps } from "./ComponentPanel";
export { SchemaEditor } from "./SchemaEditor";
export { JobCanvas, type JobCanvasProps } from "./JobCanvas";
export { layoutJob, NODE_WIDTH, NODE_HEIGHT, type CanvasNode, type CanvasEdge, type CanvasLayout, type EdgeKind, type NodeStatus } from "./canvas-layout";
export { evaluateShowIf, evaluateNotShowIf, isParamVisible, parseCondition, type ValueMap } from "./show-if";
export { groupByRow, visibleParams, tabProgress, hasSuggestion, displayValue, rowsToTsv } from "./panel-model";
export { schemaColumnsFromRows, schemaToTsv, talendFamily, differsFromSas } from "./schema-model";
export type {
  Param,
  ParamField,
  ParamOption,
  ParamTable,
  TableColumn,
  ComponentSpec,
  ComponentTab,
  PanelsSnapshot,
  GuideValue,
  GuideValues,
  DoneFields,
  SchemaColumn,
} from "./panel-types";
