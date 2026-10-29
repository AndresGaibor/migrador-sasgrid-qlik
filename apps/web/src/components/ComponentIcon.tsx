import { useState } from "react";

type Props = { name: string; available?: boolean; className?: string };

export function ComponentIcon({ name, available = true, className = "" }: Props) {
  const [missingName, setMissingName] = useState("");
  if (!available || missingName === name || !/^[A-Za-z0-9]+$/.test(name)) return null;

  return (
    <img
      className={`component-icon ${className}`.trim()}
      src={`/api/talend/catalog/${encodeURIComponent(name)}/icon`}
      alt=""
      aria-hidden="true"
      width={32}
      height={32}
      loading="lazy"
      decoding="async"
      onError={() => setMissingName(name)}
    />
  );
}
