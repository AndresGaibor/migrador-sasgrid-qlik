import type { Param, ParamOption } from "./panel-types";

// Los controles son de solo lectura: muestran el valor que hay que escribir en Studio.
// `aria-readonly` y el onChange vacío evitan avisos de React sin dar sensación de editable.
const noop = () => {};

const REPOSITORY_OPTIONS: ParamOption[] = [
  { name: "BUILT_IN", label: "Built-In", value: "Built-In" },
  { name: "REPOSITORY", label: "Repository", value: "Repository" },
];

/** «BUILT_IN», «Built-In» o «built in» pasan a «Built-In»; lo demás se muestra tal cual. */
export function normalizeRepositoryValue(value: string): string {
  const key = value.replace(/[^a-z]/gi, "").toUpperCase();
  if (key === "BUILTIN") return "Built-In";
  if (key === "REPOSITORY") return "Repository";
  return value;
}

type Props = {
  param: Param;
  id: string;
  /** Valor que muestra el control (sugerencia o default). */
  value: string;
  /** Solo para SCHEMA_TYPE: abre el editor de esquema. */
  onOpenSchema?: () => void;
};

function Select({ id, value, options, label }: { id: string; value: string; options: ParamOption[]; label: string }) {
  const known = options.some((o) => o.value === value);
  return (
    <select id={id} className="studio-control studio-select" value={value} onChange={noop} aria-readonly="true" aria-label={label}>
      {!known && value !== "" && <option value={value}>{value}</option>}
      {options.map((o) => <option key={o.name} value={o.value}>{o.label || o.name}</option>)}
    </select>
  );
}

// Un control por tipo de campo de Talend. TABLE y LABEL se resuelven fuera de este componente.
export function ParamControl({ param, id, value, onOpenSchema }: Props) {
  const label = param.label || param.name;
  switch (param.field) {
    case "CHECK":
      return (
        <input
          id={id}
          type="checkbox"
          className="studio-control studio-check"
          checked={value === "true"}
          onChange={noop}
          aria-readonly="true"
          required={param.required}
        />
      );
    case "PROPERTY_TYPE":
    case "SCHEMA_TYPE": {
      // repositoryValue no sirve aquí: es el tipo de elemento del repositorio (p. ej. SCHEMA), no la opción del selector.
      const selected = normalizeRepositoryValue(value || "Built-In");
      return (
        <span className="studio-inline">
          <Select id={id} value={selected} options={REPOSITORY_OPTIONS} label={label} />
          {param.field === "SCHEMA_TYPE" && (
            <button type="button" className="studio-button studio-ellipsis" onClick={onOpenSchema} aria-label={`Editar esquema: ${label}`} title="Editar esquema">…</button>
          )}
        </span>
      );
    }
    case "OPENED_LIST":
    case "CLOSED_LIST":
    case "ENCODING_TYPE":
    case "COMPONENT_LIST":
      if (param.options && param.options.length > 0) {
        return <Select id={id} value={value} options={param.options} label={label} />;
      }
      return <input id={id} type="text" className="studio-control studio-input" value={value} readOnly aria-required={param.required || undefined} />;
    case "FILE":
      return (
        <span className="studio-inline">
          <input id={id} type="text" className="studio-control studio-input" value={value} readOnly aria-required={param.required || undefined} />
          <button type="button" className="studio-button studio-ellipsis" disabled title="Se elige en Studio con «...»" aria-label={`Examinar: ${label} (en Studio)`}>…</button>
        </span>
      );
    case "PASSWORD":
      return <input id={id} type="password" className="studio-control studio-input" value={value} readOnly autoComplete="off" aria-required={param.required || undefined} />;
    case "MEMO":
    case "MEMO_JAVA":
      return <textarea id={id} className="studio-control studio-memo" value={value} readOnly rows={3} aria-required={param.required || undefined} />;
    case "LABEL":
      return <span className="studio-static">{value || param.label}</span>;
    default:
      return <input id={id} type="text" className="studio-control studio-input" value={value} readOnly aria-required={param.required || undefined} />;
  }
}
