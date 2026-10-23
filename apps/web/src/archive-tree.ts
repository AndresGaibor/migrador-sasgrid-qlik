export type ArchivePathEntry<T> = {
  path: string;
  value: T;
};

export type ArchiveFile<T> = ArchivePathEntry<T> & {
  name: string;
};

export type ArchiveFolder<T> = {
  name: string;
  path: string;
  files: ArchiveFile<T>[];
  folders: ArchiveFolder<T>[];
};

export function buildArchiveTree<T>(entries: readonly ArchivePathEntry<T>[]): ArchiveFolder<T> {
  const root: ArchiveFolder<T> = { name: "", path: "", files: [], folders: [] };
  const children = new Map<ArchiveFolder<T>, Map<string, ArchiveFolder<T>>>([[root, new Map()]]);

  for (const entry of entries) {
    const parts = entry.path.replace(/\\/g, "/").split("/").filter((part) => part && part !== ".");
    if (!parts.length || parts.includes("..")) continue;

    let folder = root;
    for (const part of parts.slice(0, -1)) {
      let byName = children.get(folder);
      if (!byName) {
        byName = new Map();
        children.set(folder, byName);
      }
      let next = byName.get(part);
      if (!next) {
        next = {
          name: part,
          path: folder.path ? `${folder.path}/${part}` : part,
          files: [],
          folders: [],
        };
        byName.set(part, next);
        children.set(next, new Map());
        folder.folders.push(next);
      }
      folder = next;
    }

    const name = parts.at(-1);
    if (!name) continue;
    folder.files.push({ path: [...(folder.path ? folder.path.split("/") : []), name].join("/"), name, value: entry.value });
  }

  const sort = (folder: ArchiveFolder<T>) => {
    folder.files.sort((left, right) => left.name.localeCompare(right.name));
    folder.folders.sort((left, right) => left.name.localeCompare(right.name));
    for (const child of folder.folders) sort(child);
  };
  sort(root);
  return root;
}

export function archiveFolderFileCount<T>(folder: ArchiveFolder<T>): number {
  return folder.files.length + folder.folders.reduce((total, child) => total + archiveFolderFileCount(child), 0);
}
