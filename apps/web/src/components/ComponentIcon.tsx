type Props = { name: string };

export function ComponentIcon({ name }: Props) {
  if (!/^t[A-Za-z0-9]+$/.test(name)) return null;

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
      title={name === "tDynamicGuessSchema" ? "Icono vectorial de sustitución; no se encontró uno en la fuente abierta" : undefined}
    />
  );
}
