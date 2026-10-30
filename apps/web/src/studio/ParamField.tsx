import type { ReactNode } from "react";
import type { GuideValues, Param } from "./panel-types";
import { displayValue, hasSuggestion, paramLabel, rowsToTsv } from "./panel-model";
import { ParamControl } from "./ParamControl";
import { SuggestionChip } from "./SuggestionChip";
import { TableField } from "./TableField";

type Props = {
  param: Param;
  /** Prefijo de los id del componente, para no repetir ids en la página. */
  idPrefix: string;
  values: GuideValues;
  done: boolean;
  active: boolean;
  onDone: (name: string, done: boolean) => void;
  onOpenSchema: (name: string) => void;
};

// Una celda del panel: etiqueta a la izquierda, control a la derecha y, si hay sugerencia, el chip.
export function ParamField({ param, idPrefix, values, done, active, onDone, onOpenSchema }: Props) {
  const id = `${idPrefix}-f-${param.name}`;
  const label = paramLabel(param);
  const suggestion = values[param.name];
  const suggested = hasSuggestion(param.name, values);
  const isTable = param.field === "TABLE";
  const rows = suggestion?.rows ?? [];
  const isLabelField = param.field === "LABEL";

  let chipLabel: ReactNode = null;
  let copyValue = "";
  if (suggested && suggestion) {
    if (suggestion.value !== undefined) {
      chipLabel = <>Set to: <code>{suggestion.value}</code></>;
      copyValue = suggestion.value;
    } else {
      const columns = isTable
        ? (param.table?.columns ?? []).map((c) => ({ name: c.name, label: c.label }))
        : Object.keys(rows[0] ?? {}).map((k) => ({ name: k, label: k }));
      chipLabel = `${rows.length} ${rows.length === 1 ? "fila" : "filas"}`;
      copyValue = rowsToTsv(columns, rows);
    }
  }

  return (
    <div className={`studio-field${active ? " is-active" : ""}`} data-field={param.name} data-field-type={param.field}>
      <div className="studio-field-label">
        {isTable || isLabelField ? (
          <span className="studio-label-text">{label}</span>
        ) : (
          <label htmlFor={id} className="studio-label-text">{label}</label>
        )}
        {param.required && (
          <span className="studio-required" title="Campo obligatorio">
            <span aria-hidden="true">*</span> <span className="studio-required-tag">required</span>
          </span>
        )}
      </div>
      <div className="studio-field-control">
        {isTable ? (
          <TableField param={param} id={id} rows={rows} />
        ) : (
          <ParamControl param={param} id={id} value={displayValue(param, values)} onOpenSchema={() => onOpenSchema(param.name)} />
        )}
        {param.field === "PASSWORD" && (
          <p className="studio-warning">Usa una variable de contexto (por ejemplo context.DB_PASSWORD), no la contraseña en claro.</p>
        )}
        {suggested && suggestion && (
          <SuggestionChip
            name={param.name}
            label={chipLabel}
            copyValue={copyValue}
            why={suggestion.why}
            done={done}
            active={active}
            onDone={(value) => onDone(param.name, value)}
          />
        )}
      </div>
    </div>
  );
}
