import { expect, test } from "bun:test";
import { renderToStaticMarkup } from "react-dom/server";
import { ProjectStepper } from "./ProjectStepper";
import type { ProjectStage } from "../types";

const stages: ProjectStage[] = [
  { key: "upload", label: "Cargar archivos", status: "done", detail: "12 archivos" },
  { key: "analysis", label: "Analizar", status: "done", detail: "Análisis completado" },
  { key: "guides", label: "Preparar guías", status: "current", detail: "3 Jobs por preparar" },
  { key: "studio", label: "Crear en Studio", status: "todo", detail: "Pendiente" },
  { key: "complete", label: "Completar guías", status: "todo", detail: "Pendiente" },
  { key: "verify", label: "Verificar en Studio", status: "blocked", detail: "Requiere Studio" },
];

test("marks exactly one current stage and lists all six stages", () => {
  const html = renderToStaticMarkup(<ProjectStepper stages={stages} />);
  expect(html.match(/aria-current="step"/g)).toHaveLength(1);
  expect(html).toContain("<ol");
  for (const stage of stages) expect(html).toContain(stage.label);
});

test("has no current stage when every stage is done", () => {
  const done = stages.map((stage) => ({ ...stage, status: "done" as const }));
  const html = renderToStaticMarkup(<ProjectStepper stages={done} />);
  expect(html).not.toContain("aria-current");
});

test("shows a status word for each stage so colour is not the only signal", () => {
  const html = renderToStaticMarkup(<ProjectStepper stages={stages} />);
  for (const word of ["Hecho", "En curso", "Pendiente", "Bloqueado"]) expect(html).toContain(word);
});
