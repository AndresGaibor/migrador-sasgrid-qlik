import { useState, type ReactNode } from "react";
import { copyText } from "./clipboard";

type Props = {
  /** Nombre del campo, para los aria-label. */
  name: string;
  /** Texto del chip, por ejemplo «Set to: <code>valor</code>» o «3 filas». */
  label: ReactNode;
  /** Lo que se copia al portapapeles. */
  copyValue: string;
  why?: string;
  done: boolean;
  /** Es el siguiente campo pendiente: se resalta. */
  active: boolean;
  onDone: (done: boolean) => void;
};

// Chip con el valor sugerido, botón copiar, casilla «hecho» y el porqué de la sugerencia.
export function SuggestionChip({ name, label, copyValue, why, done, active, onDone }: Props) {
  const [copyState, setCopyState] = useState<"idle" | "ok" | "error">("idle");

  const onCopy = async () => {
    const ok = await copyText(copyValue);
    setCopyState(ok ? "ok" : "error");
  };

  return (
    <div className={`studio-suggestion${active ? " is-active" : ""}${done ? " is-done" : ""}`} data-field={name}>
      <span className="studio-chip">{label}</span>
      <button type="button" className="studio-button studio-copy" onClick={() => void onCopy()} aria-label={`Copiar valor de ${name}`}>
        Copiar
      </button>
      <label className="studio-done">
        <input type="checkbox" checked={done} onChange={(e) => onDone(e.target.checked)} aria-label={`Marcar ${name} como hecho`} />
        <span>Hecho</span>
      </label>
      {why && (
        <details className="studio-why">
          <summary>¿Por qué?</summary>
          <p>{why}</p>
        </details>
      )}
      {copyState !== "idle" && (
        <span className="studio-copy-status" role="status">
          {copyState === "ok" ? "Copiado al portapapeles." : "No se pudo copiar. Selecciona el valor y copia a mano."}
        </span>
      )}
    </div>
  );
}
