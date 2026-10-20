import { useState } from "react";

type Props = { name: string; available?: boolean };

export function ComponentIcon({ name, available = true }: Props) {
  const [missing, setMissing] = useState(false);
  if (!available || missing || !/^t[A-Za-z0-9]+$/.test(name)) return null;

  const extension = name === "tDynamicGuessSchema" ? "svg" : "png";
  return (
    <img
      className="component-icon"
      src={`/talend-icons/${encodeURIComponent(name)}_icon32.${extension}`}
      alt=""
      aria-hidden="true"
      width={32}
      height={32}
      loading="lazy"
      decoding="async"
      onError={() => setMissing(true)}
      title={name === "tDynamicGuessSchema" ? "Icono vectorial de sustitución; no se encontró uno en la fuente abierta" : undefined}
    />
  );
}
