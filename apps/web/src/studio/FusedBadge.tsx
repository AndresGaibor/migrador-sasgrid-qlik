// Etiqueta de un paso que reúne varias operaciones SAS en un solo tMap.
import "./studio-panels.css";

export function FusedBadge({ fusedFrom, why }: { fusedFrom?: string[]; why?: string | null }) {
  const count = fusedFrom?.length ?? 0;
  if (count < 2) return null;
  return (
    <div className="fused-badge" role="note">
      <span className="badge info">Reúne {count} operaciones del SAS</span>
      {why && <span className="muted"> {why}</span>}
    </div>
  );
}
