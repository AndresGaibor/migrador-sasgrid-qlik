// Browser smoke against the local API and Vite app.
// Usage: node .claude/scripts/e2e_web.mjs <urlWeb> <sasFixtures> <screenshotsDir>
import { createRequire } from "node:module";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { mkdirSync } from "node:fs";
import { spawnSync } from "node:child_process";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(scriptDir, "../..");
const home = process.env.HOME ?? process.env.USERPROFILE;
if (!home) throw new Error("Set HOME or USERPROFILE so the Playwright install can be located");
const require = createRequire(join(home, ".bun/install/global/node_modules/"));
const { chromium } = require("playwright");
const [base, fixtures, screenshotArg] = process.argv.slice(2);
if (!base || !fixtures || !screenshotArg) throw new Error("Expected web URL, fixture directory, and screenshot directory");
const shots = resolve(screenshotArg);
mkdirSync(shots, { recursive: true });
const zipPath = join(shots, "grid-project.zip");
const python = process.env.SGM_PYTHON ?? (process.platform === "win32" ? join(root, ".venv/Scripts/python.exe") : "python3");
const makeZip = String.raw`import pathlib, sys, zipfile
source, target = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
names = ["grid/ejecutar_lote.sh", "grid/coverage_variants.sh", "p0_clientes_activos.sas"]
with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
    for name in names:
        archive.write(source / name, name)
`;
const zipped = spawnSync(python, ["-c", makeZip, fixtures, zipPath], { encoding: "utf8" });
if (zipped.status !== 0) throw new Error(zipped.stderr || "Could not create fixture ZIP");

const browser = await chromium.launch({ executablePath: process.env.CHROMIUM ?? undefined });
const page = await browser.newPage({ viewport: { width: 1200, height: 800 } });
const errors = [];
page.on("pageerror", (error) => errors.push(String(error)));
page.on("console", (message) => message.type() === "error" && errors.push(message.text()));
const step = async (name, fn) => {
  await fn();
  await page.screenshot({ path: join(shots, `${name}.png`) });
  console.log("ok", name);
};

try {
  await step("1-create-project", async () => {
    await page.goto(base);
    await page.getByLabel("Nombre").fill("e2e-guided");
    await page.getByRole("button", { name: "Crear proyecto" }).click();
    await page.waitForURL(/importar/);
  });
  await step("2-upload-zip-and-error", async () => {
    const input = page.locator('input[type="file"]');
    await input.setInputFiles({ name: "invalid.txt", mimeType: "text/plain", buffer: Buffer.from("bad") });
    await page.getByRole("alert").waitFor();
    await input.setInputFiles(zipPath);
    await page.getByRole("heading", { name: "Inventario" }).waitFor();
    await page.getByText("3 archivos").waitFor();
  });
  await step("3-summary", async () => {
    await page.getByRole("link", { name: "Resumen", exact: true }).click();
    await page.getByRole("button", { name: "Analizar proyecto" }).click();
    await page.getByText(/programas.*sentencias/).waitFor();
  });
  await step("4-open-program", async () => {
    await page.getByRole("link", { name: "Programas", exact: true }).click();
    await page.getByRole("link", { name: "p0_clientes_activos.sas" }).click();
    await page.getByRole("heading", { name: "p0_clientes_activos.sas" }).waitFor();
  });
  await step("5-dependencies", async () => {
    await page.getByRole("link", { name: "Dependencias", exact: true }).click();
    await page.getByRole("heading", { name: /Orquestaci/ }).waitFor();
    await page.getByText("unsupported_scheduler").waitFor();
  });
  await step("6-generate-guide", async () => {
    await page.getByRole("link", { name: "Planes", exact: true }).click();
    await page.getByRole("button", { name: /Generar \/ regenerar/ }).click();
    await page.getByText("sasgsub.unverified_options").waitFor();
    await page.getByText("unsupported", { exact: true }).first().waitFor();
    await page.getByRole("link", { name: "job_p0_clientes_activos" }).waitFor();
  });
  await step("7-guide-progress-evidence", async () => {
    await page.getByRole("link", { name: "job_p0_clientes_activos" }).click();
    await page.locator("article.step").first().waitFor();
    const [evidence] = await Promise.all([
      page.waitForEvent("popup"),
      page.getByRole("link", { name: /Ver evidencia/ }).first().click(),
    ]);
    await evidence.getByText("sasgsub").waitFor();
    await evidence.close();
    const status = page.locator("article.step select").first();
    const response = page.waitForResponse((res) => res.request().method() === "PATCH" && res.ok());
    await status.selectOption("descartado");
    await response;
    await page.locator("article.step input").first().fill("E2E review note");
    const noteSave = page.waitForResponse((res) => res.request().method() === "PATCH" && res.ok());
    await page.locator("article.step input").first().blur();
    await noteSave;
    await page.reload();
    await page.locator("article.step select").first().waitFor();
    if (await page.locator("article.step select").first().inputValue() !== "descartado") throw new Error("Step status was not persisted");
    if (await page.locator("article.step input").first().inputValue() !== "E2E review note") throw new Error("Step note was not persisted");
  });
  await step("8-export-download", async () => {
    await page.getByRole("link", { name: "Exportar", exact: true }).click();
    await page.getByRole("button", { name: "Exportar planes" }).click();
    await page.getByRole("link", { name: "steps.csv" }).waitFor();
    const [download] = await Promise.all([
      page.waitForEvent("download"),
      page.getByRole("link", { name: "steps.csv" }).click(),
    ]);
    if (download.suggestedFilename() !== "steps.csv") throw new Error("Wrong export filename");
  });
  await step("9-official-catalog", async () => {
    await page.getByRole("link", { name: "Catálogo Talend" }).click();
    await page.locator('input[placeholder^="tFilterRow"]').fill("tRunJob");
    await page.getByRole("link", { name: /tRunJob/ }).click();
    await page.getByRole("heading", { name: "Parámetros" }).waitFor();
    await page.getByRole("link", { name: "documentación oficial" }).waitFor();
    await page.getByText(/derivados de la comunidad/).waitFor();
  });
  await step("10-mobile-layout", async () => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(100);
    const fits = await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1);
    if (!fits) throw new Error("Page overflows horizontally on a mobile viewport");
  });
  if (errors.length) throw new Error(`Browser errors: ${errors.join("; ")}`);
} finally {
  await browser.close();
}
