import { useEffect, useState } from "react";
import type { PlanRow } from "../../types";

// Los ZIP de Mac traen basura «__MACOSX»; se oculta aunque venga de proyectos ya importados.
export const real = (rows: PlanRow[]) => rows.filter((r) => !r.program.includes("__MACOSX/"));
export const PARENT_PATTERN = /include_dispatch|sysin|submit/;
export function useDesktopLayout() {
  const [isDesktop, setIsDesktop] = useState(() => window.matchMedia("(min-width: 601px)").matches);
  useEffect(() => {
    const desktop = window.matchMedia("(min-width: 601px)");
    const update = () => setIsDesktop(desktop.matches);
    desktop.addEventListener("change", update);
    return () => desktop.removeEventListener("change", update);
  }, []);
  return isDesktop;
}

export function visible(rows: PlanRow[], programOrder?: string[]) {
  const todo = real(rows).filter((row) => row.steps > 0);
  if (!programOrder) return todo;
  const rank = new Map(programOrder.map((program, index) => [program, index]));
  return todo.sort((a, b) => (rank.get(a.program) ?? programOrder.length) - (rank.get(b.program) ?? programOrder.length));
}
