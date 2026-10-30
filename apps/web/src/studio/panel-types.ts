// Tipos del snapshot de paneles de Talend (rules/talend/component-panels.json) y de la guía de migración.

/** Tipos de widget conocidos. Cualquier otro texto se trata como TEXT. */
export type KnownParamField =
  | "TEXT"
  | "FILE"
  | "CHECK"
  | "OPENED_LIST"
  | "CLOSED_LIST"
  | "TABLE"
  | "PROPERTY_TYPE"
  | "SCHEMA_TYPE"
  | "LABEL"
  | "PASSWORD"
  | "ENCODING_TYPE"
  | "COMPONENT_LIST"
  | "MEMO"
  | "MEMO_JAVA";

export type ParamField = KnownParamField | (string & {});

export type ParamOption = { name: string; label: string; value: string };

export type TableColumn = {
  name: string;
  label: string;
  defaultValue: string | null;
  options: ParamOption[] | null;
};

export type ParamTable = { columns: TableColumn[] };

export type Param = {
  name: string;
  label: string;
  field: ParamField;
  required: boolean;
  show: boolean;
  showIf: string | null;
  notShowIf: string | null;
  defaultValue: string | null;
  numRow: number | null;
  group: string | null;
  repositoryValue: string | null;
  options: ParamOption[] | null;
  table: ParamTable | null;
};

export type ComponentTab = "basic" | "advanced" | "dynamic" | "view" | "documentation";

export type ComponentSpec = {
  label: string | null;
  family: string;
  tabs: { basic: Param[]; advanced: Param[] };
};

export type PanelsSnapshot = {
  version: 1;
  generatedFrom: string;
  components: Record<string, ComponentSpec>;
};

/** Lo que el planificador sugiere para un campo. Sin `value` ni `rows` no hay sugerencia. */
export type GuideValue = {
  value?: string;
  rows?: Record<string, string>[];
  why?: string;
};

/** Sugerencias por nombre de parámetro. */
export type GuideValues = Record<string, GuideValue>;

/** Estado «hecho» por nombre de parámetro. */
export type DoneFields = Record<string, boolean>;

/** Columna de esquema (Edit schema de Studio). */
export type SchemaColumn = {
  name: string;
  key?: boolean;
  type: string;
  nullable?: boolean;
  length?: number | null;
  precision?: number | null;
  pattern?: string | null;
  default?: string | null;
  /** Tipo SAS de origen, por ejemplo «char», «num», «date». */
  sasType?: string | null;
  /** Formato SAS de origen, por ejemplo «DATE9.». */
  sasFormat?: string | null;
  comment?: string | null;
};
