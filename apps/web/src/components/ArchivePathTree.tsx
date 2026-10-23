import { useMemo, useState, type ReactNode, type SyntheticEvent } from "react";
import { Icon } from "./Icon";
import { archiveFolderFileCount, buildArchiveTree, type ArchiveFolder, type ArchivePathEntry } from "../archive-tree";
import { filterArchiveEntries } from "../project-workspace";

export function ArchivePathTree<T>({
  entries,
  renderEntry,
}: {
  entries: readonly ArchivePathEntry<T>[];
  renderEntry: (entry: { path: string; name: string; value: T }) => ReactNode;
}) {
  const [query, setQuery] = useState("");
  const visibleEntries = useMemo(() => filterArchiveEntries(entries, query), [entries, query]);
  const root = useMemo(() => buildArchiveTree(visibleEntries), [visibleEntries]);
  return (
    <div className="archive-path-browser">
      <label className="archive-path-search"><Icon name="search" size={17} /><span className="sr-only">Filtrar rutas del ZIP</span><input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Filtrar carpetas o archivos…" /></label>
      {query && <p className="archive-path-result-count">{visibleEntries.length} archivo(s) coinciden con la búsqueda.</p>}
      {!visibleEntries.length ? <p className="muted">No hay rutas que coincidan con «{query}».</p> : <div className="archive-path-tree">
      {root.files.length > 0 && <div className="archive-path-files">{root.files.map((file) => renderEntry(file))}</div>}
      {root.folders.map((folder) => (
        <ArchiveFolderGroup key={folder.path} folder={folder} renderEntry={renderEntry} expand={Boolean(query)} />
      ))}
      </div>}
    </div>
  );
}

function ArchiveFolderGroup<T>({
  folder,
  renderEntry,
  expand,
}: {
  folder: ArchiveFolder<T>;
  renderEntry: (entry: { path: string; name: string; value: T }) => ReactNode;
  expand: boolean;
}) {
  const [open, setOpen] = useState(false);
  const expanded = expand || open;
  const trackOpen = (event: SyntheticEvent<HTMLDetailsElement>) => {
    if (!expand) setOpen(event.currentTarget.open);
  };
  return (
    <details className="archive-path-folder" open={expanded || undefined} onToggle={trackOpen}>
      <summary>
        <Icon name="folder" size={17} />
        <span>{folder.name}</span>
        <small>{archiveFolderFileCount(folder)} archivos</small>
      </summary>
      {expanded && <>
        {folder.files.length > 0 && <div className="archive-path-files">{folder.files.map((file) => renderEntry(file))}</div>}
        {folder.folders.map((child) => (
          <ArchiveFolderGroup key={child.path} folder={child} renderEntry={renderEntry} expand={expand} />
        ))}
      </>}
    </details>
  );
}
