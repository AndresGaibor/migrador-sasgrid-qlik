import { describe, expect, test } from "bun:test";
import { buildArchiveTree } from "./archive-tree";

describe("estructura de carpetas del ZIP", () => {
  test("conserva las carpetas anidadas y normaliza rutas de Windows", () => {
    const tree = buildArchiveTree([
      { path: "cliente-a\\macros\\carga.sas", value: "macro" },
      { path: "cliente-a/programas/diario.sas", value: "program" },
      { path: "README.txt", value: "root" },
    ]);

    expect(tree.files.map((file) => file.path)).toEqual(["README.txt"]);
    expect(tree.folders.map((folder) => folder.name)).toEqual(["cliente-a"]);
    expect(tree.folders[0]?.folders.map((folder) => folder.name)).toEqual(["macros", "programas"]);
    expect(tree.folders[0]?.folders[0]?.files[0]?.value).toBe("macro");
  });
});
