// Fixture pequeño y realista para las pruebas de src/studio. No es el snapshot real.
import type { GuideValues, Param, PanelsSnapshot, ParamField } from "../panel-types";

type Partial_ = Partial<Param> & { name: string; field: ParamField };

// Rellena los campos que el snapshot siempre trae, para escribir cada parámetro en una línea.
function p(input: Partial_): Param {
  return {
    label: input.name,
    required: false,
    show: true,
    showIf: null,
    notShowIf: null,
    defaultValue: null,
    numRow: null,
    group: null,
    repositoryValue: null,
    options: null,
    table: null,
    ...input,
  };
}

const fileInputBasic: Param[] = [
  p({ name: "PROPERTY_TYPE", label: "Property Type", field: "PROPERTY_TYPE", numRow: 1, repositoryValue: "REPOSITORY", defaultValue: "BUILT_IN" }),
  p({ name: "SCHEMA_TYPE", label: "Edit schema", field: "SCHEMA_TYPE", numRow: 2, repositoryValue: "SCHEMA", required: true }),
  p({ name: "FILENAME", label: "File name/Stream", field: "FILE", numRow: 3, required: true, defaultValue: "" }),
  p({ name: "ROWSEPARATOR", label: "Row separator", field: "TEXT", numRow: 4, defaultValue: "\"\\n\"" }),
  p({ name: "FIELDSEPARATOR", label: "Field separator", field: "TEXT", numRow: 4, defaultValue: "\";\"" }),
  p({ name: "HEADER", label: "Header", field: "TEXT", numRow: 5, defaultValue: "0" }),
  p({ name: "FOOTER", label: "Footer", field: "TEXT", numRow: 5, defaultValue: "0" }),
  p({ name: "LIMIT", label: "Limit", field: "TEXT", numRow: 5, defaultValue: "" }),
  p({ name: "REMOVE_EMPTY_ROW", label: "Remove empty row", field: "CHECK", numRow: 6, defaultValue: "false" }),
  p({ name: "UNCOMPRESS", label: "Uncompress as zip file", field: "CHECK", numRow: 7, defaultValue: "false" }),
  p({ name: "DIE_ON_ERROR", label: "Die on error", field: "CHECK", numRow: 8, defaultValue: "false" }),
];

const fileInputAdvanced: Param[] = [
  p({ name: "CSV_OPTION", label: "CSV options", field: "CHECK", numRow: 1, defaultValue: "false" }),
  p({ name: "ESCAPE_CHAR", label: "Escape char", field: "TEXT", numRow: 2, showIf: "CSV_OPTION == 'true'", defaultValue: "\"\\\"\"" }),
  p({ name: "TEXT_ENCLOSURE", label: "Text enclosure", field: "TEXT", numRow: 2, showIf: "CSV_OPTION == 'true'", defaultValue: "\"\\\"\"" }),
  p({ name: "ENCODING", label: "Encoding", field: "ENCODING_TYPE", numRow: 3, defaultValue: "\"UTF-8\"", options: [
    { name: "UTF8", label: "UTF-8", value: "\"UTF-8\"" },
    { name: "ISO", label: "ISO-8859-15", value: "\"ISO-8859-15\"" },
    { name: "CUSTOM", label: "CUSTOM", value: "\"CUSTOM\"" },
  ] }),
  p({ name: "ENCODING_CUSTOM", label: "Custom encoding", field: "TEXT", numRow: 3, showIf: "ENCODING == '\"CUSTOM\"'", defaultValue: "" }),
  p({ name: "SPLITRECORD", label: "Split record", field: "CHECK", numRow: 4, defaultValue: "false" }),
  p({ name: "CHECK_FIELDS_NUM", label: "Check the number of fields in each row", field: "CHECK", numRow: 5, defaultValue: "false" }),
  p({ name: "CHECK_DATE", label: "Check date", field: "CHECK", numRow: 6, defaultValue: "false" }),
  p({ name: "TRIMSELECT", label: "Trim all columns", field: "TABLE", numRow: 7, table: { columns: [
    { name: "SCHEMA_COLUMN", label: "Column", defaultValue: null, options: null },
    { name: "TRIM", label: "Trim", defaultValue: "false", options: null },
  ] } }),
  p({ name: "HELP_NOTE", label: "Nota", field: "LABEL", numRow: 8 }),
];

const dbBasic: Param[] = [
  p({ name: "PROPERTY_TYPE", label: "Property Type", field: "PROPERTY_TYPE", numRow: 1, repositoryValue: "REPOSITORY", defaultValue: "BUILT_IN" }),
  p({ name: "USE_EXISTING_CONNECTION", label: "Use an existing connection", field: "CHECK", numRow: 2, defaultValue: "false" }),
  p({ name: "DB_TYPE", label: "Database Type", field: "CLOSED_LIST", numRow: 3, required: true, defaultValue: "\"PostgreSQL\"", options: [
    { name: "PG", label: "PostgreSQL", value: "\"PostgreSQL\"" },
    { name: "MSSQL", label: "MS SQL Server", value: "\"MSSQL\"" },
  ] }),
  p({ name: "HOST", label: "Host", field: "TEXT", numRow: 4, required: true, showIf: "USE_EXISTING_CONNECTION == 'false'", defaultValue: "\"localhost\"" }),
  p({ name: "PORT", label: "Port", field: "TEXT", numRow: 4, showIf: "USE_EXISTING_CONNECTION == 'false'", defaultValue: "\"5432\"" }),
  p({ name: "DBNAME", label: "Database", field: "TEXT", numRow: 5, showIf: "USE_EXISTING_CONNECTION == 'false'", defaultValue: "\"\"" }),
  p({ name: "USER", label: "Username", field: "TEXT", numRow: 6, showIf: "USE_EXISTING_CONNECTION == 'false'", defaultValue: "\"\"" }),
  p({ name: "PASS", label: "Password", field: "PASSWORD", numRow: 6, showIf: "USE_EXISTING_CONNECTION == 'false'", defaultValue: "\"\"" }),
  p({ name: "SCHEMA_TYPE", label: "Edit schema", field: "SCHEMA_TYPE", numRow: 7, repositoryValue: "SCHEMA", required: true }),
  p({ name: "TABLE", label: "Table Name", field: "TEXT", numRow: 8, required: true, defaultValue: "\"\"" }),
  p({ name: "QUERY", label: "Query", field: "MEMO_JAVA", numRow: 9, required: true, defaultValue: "\"\"" }),
  p({ name: "EXISTING_CONN_NOTE", label: "Conexión existente", field: "LABEL", numRow: 10, notShowIf: "USE_EXISTING_CONNECTION == 'false'" }),
];

const dbAdvanced: Param[] = [
  p({ name: "TRIM_ALL_COLUMNS", label: "Trim all columns", field: "CHECK", numRow: 1, defaultValue: "false" }),
  p({ name: "ENABLE_DICTIONARY", label: "Enable dictionary", field: "CHECK", numRow: 2, defaultValue: "false" }),
  p({ name: "STATEMENT_LABEL", label: "Statement label", field: "TEXT", numRow: 3, notShowIf: "ENABLE_DICTIONARY == 'true'", defaultValue: "\"\"" }),
  p({ name: "USE_CURSOR", label: "Use cursor", field: "CHECK", numRow: 4, defaultValue: "false", notShowIf: "ENABLE_DICTIONARY == 'true'" }),
];

export const panelsFixture: PanelsSnapshot = {
  version: 1,
  generatedFrom: "fixture-test",
  components: {
    tFileInputDelimited: {
      label: "Delimited file input",
      family: "File/Input",
      tabs: { basic: fileInputBasic, advanced: fileInputAdvanced },
    },
    tDBInput: {
      label: "Database input",
      family: "Databases/DB Generic",
      tabs: { basic: dbBasic, advanced: dbAdvanced },
    },
  },
};

/** Sugerencias de la guía para tFileInputDelimited: una ruta, separador y cabecera. */
export const fileInputGuide: GuideValues = {
  FILENAME: { value: "context.CLIENTES_DIR + \"/clientes.csv\"", why: "El SAS lee la librería CLIENTES." },
  FIELDSEPARATOR: { value: "\";\"", why: "El DATA step usa DLM=';'." },
  HEADER: { value: "1" },
  ENCODING: { value: "\"UTF-8\"" },
  SCHEMA_TYPE: { value: "Built-In", rows: [{ name: "ID", type: "Integer", key: "true" }, { name: "NOMBRE", type: "String", nullable: "true" }] },
  TRIMSELECT: { rows: [{ SCHEMA_COLUMN: "NOMBRE", TRIM: "true" }] },
};

/** Sugerencias para tDBInput con conexión propia. */
export const dbGuide: GuideValues = {
  USE_EXISTING_CONNECTION: { value: "false", why: "Se usa la conexión que indica el SAS (LIBNAME)." },
  DB_TYPE: { value: "\"PostgreSQL\"" },
  HOST: { value: "\"db.ejemplo.local\"" },
  PORT: { value: "\"5432\"" },
  PASS: { value: "context.DB_PASSWORD", why: "No escribas la contraseña en claro: usa una variable de contexto." },
  QUERY: { value: "SELECT id, nombre FROM clientes WHERE activo = 1" },
};
