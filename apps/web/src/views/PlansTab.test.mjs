import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const source = await readFile(new URL("./PlansTab.tsx", import.meta.url), "utf8");
const hooksSource = await readFile(new URL("../hooks.ts", import.meta.url), "utf8");

test("project plans expose one ZIP-level Talend action and no per-guide write action", () => {
  assert.match(source, /Crear Jobs en Talend Studio/);
  assert.match(source, /api\.talendApplyBatch\(id, confirmation\.revision_hash\)/);
  assert.match(source, /no ejecutará los Jobs/i);
  assert.match(source, /no se ejecutan ni se publican en Qlik Talend Cloud/);
  assert.match(source, /canStartBatch/);
  assert.match(source, /!health\.data\.write_enabled/);
  assert.match(source, /disabled=\{!canStartBatch\}/);
  assert.doesNotMatch(source, /api\.applyTalend\(id, file\)/);
  assert.doesNotMatch(source, /Implementar flujo directo en Talend/);
});

test("the ZIP-level operation shows durable progress, current job, and each result grouped by folder", () => {
  assert.match(source, /api\.talendApplyBatchStatus\(id\)/);
  assert.match(source, /role="progressbar"/);
  assert.match(source, /aria-valuenow=/);
  assert.match(source, /completed_jobs/);
  assert.match(source, /current_program/);
  assert.match(source, /ArchivePathTree/);
  assert.match(source, /talendApplyBatchLabel/);
  assert.match(source, /job\.error/);
  assert.match(source, /setInterval\(batch\.reload/);
  assert.match(source, /result\?\.result\.itemPath/);
});

test("the ZIP-level action checks current Talend destinations and shows create/update/conflict decisions", () => {
  assert.match(source, /api\.talendApplyBatchPreflight\(id\)/);
  assert.match(source, /preflightReady/);
  assert.match(source, /create_count/);
  assert.match(source, /update_count/);
  assert.match(source, /conflict_count/);
  assert.match(source, /existing_path/);
  assert.match(source, /Volver a comprobar/);
  assert.match(source, /Recrear Jobs faltantes/);
});

test("a saved conflict cleared by live Talend inventory is presented as retryable, not current", () => {
  assert.match(source, /staleConflictResolved/);
  assert.match(source, /El conflicto anterior ya no está en Talend/);
  assert.match(source, /Aplicar según inventario actual/);
  assert.match(source, /!staleConflictResolved && batchState\.error/);
});

test("transient batch polling errors retain the last state and report automatic retries", () => {
  assert.match(hooksSource, /preserveDataOnError\s*\?\s*\{ \.\.\.s, error: message, errorStatus: status, loading: false \}/);
  assert.match(source, /preserveDataOnError: true/);
  assert.match(source, /setInterval\(batch\.reload, 1200\)/);
  assert.match(source, /No se pudo actualizar el progreso del lote/);
  assert.match(source, /Se volverá a intentar automáticamente/);
});

test("an interrupted active Job is shown as retryable after a server restart", () => {
  assert.match(source, /interrupted: "Interrumpido; puede reintentarse"/);
});

test("individual guides show only their batch or legacy result and retain the read-only preview", () => {
  assert.match(source, /api\.talendApplyPreview\(id, file\)/);
  assert.match(source, /api\.talendApplyBatchStatus\(id\)/);
  assert.match(source, /api\.talendApplyStatus\(id, file\)/);
  assert.doesNotMatch(source, /onClick=\{\(\) => void applyGuide\(\)\}/);
  assert.doesNotMatch(source, /api\.applyTalend\(/);
  assert.match(source, /Información técnica pendiente/);
  assert.match(source, /Talend no ejecutará los Jobs/);
});

test("the project batch asks for confirmation with a human-review summary before writing", () => {
  assert.match(source, /api\.talendApplyBatchSummary\(id\)/);
  assert.match(source, /setConfirmation\(summary\.data\)/);
  assert.match(source, /TalendPreflight/);
  assert.match(source, /Confirmar creación en Talend Studio/);
  assert.match(source, /api\.talendApplyBatch\(id, confirmation\.revision_hash\)/);
  assert.match(source, /review_required|review_warnings/);
  assert.match(source, /Cancelar/);
  assert.doesNotMatch(
    source,
    /className="talend-implement-button talend-batch-button" onClick=\{\(\) => void implementProject\(\)\}/,
    "the main button must open the confirmation instead of starting the batch directly",
  );
});

test("each job reports its creation phase and the Studio verification result", () => {
  assert.match(source, /phase === "applying"/);
  assert.match(source, /phase === "inspecting"/);
  assert.match(source, /Fase: creando componentes/);
  assert.match(source, /Fase: verificando el Job en Studio/);
  assert.match(source, /Inspeccionado en Studio/);
  assert.match(source, /verification\.missing_components/);
  assert.match(source, /verification\.studio_problems/);
  assert.match(source, /Verificación no disponible/);
});
