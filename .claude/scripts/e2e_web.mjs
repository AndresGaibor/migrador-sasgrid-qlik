// Recorrido de humo del frontend contra API+Vite locales. Uso: node e2e_web.mjs <urlWeb> <rutaFixtures> <dirCapturas>
import { createRequire } from "node:module";
const require = createRequire(process.env.HOME + "/.bun/install/global/node_modules/");
const { chromium } = require("playwright");
const [base, fixtures, shots] = process.argv.slice(2);
const exe = process.env.CHROMIUM ?? undefined;
const b = await chromium.launch({ executablePath: exe });
const p = await b.newPage({ viewport: { width: 1200, height: 800 } });
const errors = [];
p.on("pageerror", (e) => errors.push(String(e)));
p.on("console", (m) => m.type() === "error" && errors.push(m.text()));
const step = async (name, fn) => { await fn(); await p.screenshot({ path: `${shots}/${name}.png` }); console.log("ok", name); };

await step("1-proyectos", async () => {
  await p.goto(base);
  await p.fill("input", "e2e");
  await p.click("text=Crear proyecto");
  await p.waitForURL(/importar/);
});
await step("2-importar", async () => {
  await p.fill("input[placeholder^='/ruta']", fixtures);
  await p.click("button:has-text('Importar')");
  await p.waitForSelector("text=archivos");
});
await step("3-resumen", async () => {
  await p.click("nav.tabs >> text=Resumen");
  await p.click("text=Analizar proyecto");
  await p.waitForSelector("text=sentencias");
});
await step("4-programas", async () => {
  await p.click("nav.tabs >> text=Programas");
  await p.click("a:has-text('p0_clientes_activos.sas')");
  await p.waitForSelector("h1:has-text('p0_clientes_activos')");
});
await step("5-dependencias", async () => {
  await p.click("nav.tabs >> text=Dependencias");
  await p.waitForSelector("h2:has-text('Orquestación')");
});
await step("6-planes", async () => {
  await p.click("nav.tabs >> text=Planes");
  await p.click("text=Generar / regenerar planes");
  await p.waitForSelector("a:has-text('job_p0_clientes_activos')");
});
await step("7-plan-detalle", async () => {
  await p.click("a:has-text('job_p0_clientes_activos')");
  await p.waitForSelector("article.step");
  await p.selectOption("article.step >> nth=0 >> select", "verificado");
  await p.waitForFunction(() => document.querySelector("article.step select").value === "verificado");
});
await step("8-exportar", async () => {
  await p.click("nav.tabs >> text=Exportar");
  await p.click("text=Exportar planes");
  await p.waitForSelector("text=steps.csv");
});
await step("9-catalogo", async () => {
  await p.click("nav >> text=Catálogo Talend");
  await p.fill("input[placeholder^='tFilterRow']", "tFilterRow");
  await p.click("a:has-text('tFilterRow')");
  await p.waitForSelector("h2:has-text('Parámetros')");
  await p.waitForSelector("td.mono:has-text('LOGICAL_OP')");
});
await b.close();
if (errors.length) { console.log("ERRORES", errors); process.exit(1); }
