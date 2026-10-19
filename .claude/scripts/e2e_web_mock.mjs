// Smoke E2E de la experiencia guiada contra Vite y respuestas API fake. Uso:
// node .claude/scripts/e2e_web_mock.mjs <urlWeb> <rutaFixtures> <dirCapturas>
// Requiere Playwright instalado localmente o en %USERPROFILE%/.bun/install/global/node_modules.
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { mkdir, readFile, readdir } from "node:fs/promises";
import { basename, dirname, join, resolve } from "node:path";

const [baseArg, fixturesArg, shotsArg] = process.argv.slice(2);
if (!baseArg || !fixturesArg || !shotsArg) {
  console.error("Uso: node .claude/scripts/e2e_web_mock.mjs <urlWeb> <rutaFixtures> <dirCapturas>");
  process.exit(2);
}
const base = baseArg.replace(/\/$/, "");
const fixtures = resolve(fixturesArg);
const shots = resolve(shotsArg);
await mkdir(shots, { recursive: true });

function loadPlaywright() {
  const candidates = [
    process.env.PLAYWRIGHT_MODULE,
    join(process.cwd(), "node_modules", "playwright"),
    resolve(dirname(fileURLToPath(import.meta.url)), "../../apps/web/node_modules/playwright"),
    process.env.USERPROFILE && join(process.env.USERPROFILE, ".bun", "install", "global", "node_modules", "playwright"),
  ].filter(Boolean);
  for (const candidate of candidates) {
    try { return createRequire(import.meta.url)(candidate); } catch { /* prueba la siguiente ruta */ }
  }
  throw new Error("No se encontró Playwright. Instálalo en el proyecto o define PLAYWRIGHT_MODULE.");
}
const { chromium } = loadPlaywright();

// ZIP mínimo sin dependencias, método STORE. Permite que la prueba use buffers
// sintéticos (por ejemplo, ZIP inválido o sin archivos SAS) de forma reproducible.
const crcTable = new Uint32Array(256);
for (let n = 0; n < 256; n++) {
  let c = n;
  for (let k = 0; k < 8; k++) c = (c & 1) ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  crcTable[n] = c >>> 0;
}
function crc32(buffer) {
  let c = 0xffffffff;
  for (const byte of buffer) c = crcTable[(c ^ byte) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}
function zip(entries) {
  const locals = [];
  const centrals = [];
  let offset = 0;
  for (const entry of entries) {
    const name = Buffer.from(entry.name.replaceAll("\\", "/"));
    const data = Buffer.isBuffer(entry.data) ? entry.data : Buffer.from(entry.data);
    const crc = crc32(data);
    const local = Buffer.alloc(30 + name.length);
    local.writeUInt32LE(0x04034b50, 0); local.writeUInt16LE(20, 4); local.writeUInt16LE(0x800, 6);
    local.writeUInt16LE(0, 8); local.writeUInt32LE(crc, 14); local.writeUInt32LE(data.length, 18); local.writeUInt32LE(data.length, 22);
    local.writeUInt16LE(name.length, 26); name.copy(local, 30);
    locals.push(local, data);
    const central = Buffer.alloc(46 + name.length);
    central.writeUInt32LE(0x02014b50, 0); central.writeUInt16LE(20, 4); central.writeUInt16LE(20, 6);
    central.writeUInt16LE(0x800, 8); central.writeUInt16LE(0, 10); central.writeUInt32LE(crc, 16);
    central.writeUInt32LE(data.length, 20); central.writeUInt32LE(data.length, 24); central.writeUInt16LE(name.length, 28);
    central.writeUInt32LE(offset, 42); name.copy(central, 46);
    centrals.push(central);
    offset += local.length + data.length;
  }
  const centralSize = centrals.reduce((sum, part) => sum + part.length, 0);
  const end = Buffer.alloc(22);
  end.writeUInt32LE(0x06054b50, 0); end.writeUInt16LE(entries.length, 8); end.writeUInt16LE(entries.length, 10);
  end.writeUInt32LE(centralSize, 12); end.writeUInt32LE(offset, 16);
  return Buffer.concat([...locals, ...centrals, end]);
}

const firstSas = async (path) => {
  const entries = await readdir(path, { withFileTypes: true });
  for (const entry of entries) {
    const child = join(path, entry.name);
    if (entry.isDirectory()) {
      try { return await firstSas(child); } catch (error) { if (error.code !== "NO_SAS_FIXTURE") throw error; }
    } else if (/\.sas$/i.test(entry.name)) return { name: basename(entry.name), data: await readFile(child) };
  }
  const error = new Error(`No se encontró un archivo .sas en ${path}`); error.code = "NO_SAS_FIXTURE"; throw error;
};
const sasFixture = await firstSas(fixtures);
const sasZip = zip([sasFixture]);
const unsupportedZip = zip([{ name: "README.txt", data: "Este paquete no contiene programas SAS." }]);

const chrome = process.env.CHROMIUM || (process.platform === "win32" ? "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" : undefined);
const browser = await chromium.launch({ executablePath: chrome, headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, acceptDownloads: true });
const errors = [];
const projects = [];
const projectData = new Map();
let nextProject = 1;
const fixtureProgram = sasFixture.name;
const makePlan = (data) => ({
  program: fixtureProgram, job_name: `job_${fixtureProgram.replace(/\.sas$/i, "")}`, job_status: "proposed",
  steps: [{ id: "step-1", order: 1, subjob: "main", action: "configure", component_candidate: "tMap", alternatives: [], purpose: "Configura el mapeo de datos", properties: [{ name: "EXPRESSION", label: "Expresión", value: "row1.total", origin: "sas", verified: false, in_catalog: true, options: [] }], connections: [], expressions: [], assumptions: [], pending: [], tests: [], evidence: { file: fixtureProgram, line: 1 }, confidence: "medium", status: data.status ?? "propuesto", note: data.note ?? null, verified: false, in_catalog: true, doc_url: "https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap", variants: [], requires_semantic_validation: false }],
  children: [], validation_cases: [], context_variables: [], libraries_needed: [], unresolved: [],
});
const json = (route, payload, status = 200) => route.fulfill({ status, contentType: "application/json", body: JSON.stringify(payload) });
await page.route("**/api/**", async (route) => {
  const request = route.request();
  let pathname;
  try { pathname = new URL(request.url()).pathname; }
  catch { return json(route, { detail: "URL de solicitud no válida" }, 400); }
  const method = request.method();
  if (pathname === "/api/projects" && method === "GET") return json(route, projects);
  if (pathname === "/api/projects" && method === "POST") {
    const body = request.postDataJSON();
    const project = { id: `e2e-${nextProject++}`, name: body.name, created_at: new Date().toISOString() };
    projects.unshift(project);
    projectData.set(project.id, { manifest: { files: [], skipped: [] }, analyzed: false, generated: false, status: "propuesto", note: null });
    return json(route, project, 201);
  }
  const match = pathname.match(/^\/api\/projects\/([^/]+)(?:\/(.*))?$/);
  if (!match) return json(route, { detail: `Endpoint E2E no configurado: ${method} ${pathname}` }, 404);
  const [, id, tail = ""] = match;
  const data = projectData.get(id);
  if (!data) return json(route, { detail: "Proyecto de prueba no encontrado" }, 404);
  if (tail === "uploads" && method === "POST") {
    const body = (await request.postDataBuffer()).toString("latin1");
    if (body.includes("invalido.zip")) return json(route, { detail: "El archivo no es un ZIP válido." }, 422);
    data.manifest = body.includes("sin-soporte.zip")
      ? { files: [], skipped: [{ path: "README.txt", reason: "Extensión no compatible con el análisis SAS." }] }
      : { files: [{ path: fixtureProgram, sha256: "a".repeat(64), size: 128, kind: "sas", encoding: "utf-8" }], skipped: [] };
    return json(route, data.manifest, 201);
  }
  if (tail === "inventory" && method === "GET") return json(route, data.manifest);
  if (tail === "analyses" && method === "POST") {
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 350));
    data.analyzed = true;
    return json(route, { programs: 1, statements: 4, unrecognized: 0, macro_fragments: 0, findings_by_priority: { P0: 1 }, coverage: [{ tag: "DATA", priority: "P0", count: 1 }] });
  }
  if (tail === "programs" && method === "GET") return json(route, [{ file: fixtureProgram, statements: 4, findings: 1 }]);
  if (tail === "plans" && method === "POST") { data.generated = true; return json(route, { plans: 1 }); }
  if (tail === "plans" && method === "GET") return json(route, data.generated ? [{ program: fixtureProgram, job_name: `job_${fixtureProgram.replace(/\.sas$/i, "")}`, job_status: "proposed", steps: 1, pending: 1, done: data.status === "verificado" ? 1 : 0 }] : []);
  const decision = tail.match(/^plans\/([^/]+)\/steps\/([^/]+)$/);
  if (decision && method === "PATCH") {
    const body = request.postDataJSON();
    data.status = body.status;
    data.note = body.note;
    return json(route, makePlan(data));
  }
  const detail = tail.match(/^plans\/([^/]+)$/);
  if (detail && method === "GET") return json(route, makePlan(data));
  if (tail === "exports" && method === "POST") return json(route, { directory: "exports/e2e", files: ["guias-migracion.md", `${fixtureProgram}.md`, `${fixtureProgram}.json`, "pasos-migracion.csv"] });
  return json(route, { detail: `Endpoint E2E no configurado: ${method} ${pathname}` }, 404);
});
page.on("pageerror", (error) => errors.push(String(error)));
page.on("console", (message) => {
  if (message.type() === "error" && !/\b(422|503)\b/.test(message.text())) errors.push(message.text());
});
const step = async (name, fn) => {
  await fn();
  await page.screenshot({ path: join(shots, `${name}.png`), fullPage: true });
  console.log(`ok ${name}`);
};
const createProject = async (name) => {
  await page.goto(base);
  await page.getByRole("button", { name: /Nuevo proyecto/ }).first().click();
  await page.getByLabel("Nombre del proyecto").fill(name);
  await page.getByRole("button", { name: /Crear y cargar archivos/ }).click();
  await page.waitForURL(/#\/p\/[^/]+\/importar/);
  const match = page.url().match(/#\/p\/([^/]+)\/importar/);
  if (!match) throw new Error("El proyecto no llegó a la pantalla de carga.");
  return match[1];
};
const goTab = async (label) => {
  await page.getByRole("navigation", { name: "Secciones del proyecto" }).getByRole("link", { name: new RegExp(label, "i") }).click();
};

try {
  await step("01-proyecto-vacio", async () => {
    await createProject(`E2E guiado ${Date.now()}`);
    await goTab("Mis archivos");
    await page.getByRole("heading", { name: "Aún no hay archivos" }).waitFor();
    await page.getByRole("navigation", { name: "Secciones del proyecto" }).getByRole("link", { name: "Cargar archivos" }).waitFor();
  });

  await step("02-error-api-reintento", async () => {
    const projectId = new URL(page.url()).hash.match(/#\/p\/([^/]+)/)[1];
    const routePattern = `**/api/projects/${projectId}/inventory`;
    await page.route(routePattern, (route) => route.fulfill({ status: 503, contentType: "application/json", body: JSON.stringify({ detail: "Servicio E2E temporalmente no disponible" }) }));
    await goTab("Resumen");
    await page.getByRole("alert").getByText("No pudimos cargar esta información").waitFor();
    await page.unroute(routePattern);
    await page.getByRole("button", { name: "Volver a intentar" }).click();
    await page.getByRole("heading", { name: "Empecemos por tus archivos" }).waitFor();
  });

  await step("03-error-carga-zip", async () => {
    await goTab("Cargar archivos");
    await page.getByLabel("Archivo ZIP o programa SAS").setInputFiles({ name: "invalido.zip", mimeType: "application/zip", buffer: Buffer.from("esto no es un ZIP") });
    await page.getByRole("alert").waitFor();
    if (!(await page.getByRole("alert").innerText()).trim()) throw new Error("El error de carga no explica qué ocurrió.");
  });

  await step("04-carga-resumen-analisis", async () => {
    await page.getByLabel("Archivo ZIP o programa SAS").setInputFiles({ name: "fixture-e2e.zip", mimeType: "application/zip", buffer: sasZip });
    await page.getByRole("heading", { name: "Carga completada" }).waitFor({ timeout: 30000 });
    await page.getByRole("navigation", { name: "Secciones del proyecto" }).getByRole("link", { name: "Resumen" }).focus();
    await page.keyboard.press("Enter");
    await page.getByRole("heading", { name: "Tu proyecto está listo para analizar" }).waitFor();
    const analysis = page.waitForResponse((response) => response.url().includes("/analyses") && response.request().method() === "POST");
    await page.getByRole("button", { name: "Analizar proyecto" }).click();
    const inProgress = await page.getByRole("status").filter({ hasText: "Estamos revisando tus programas" }).waitFor({ state: "visible", timeout: 1000 }).then(() => true).catch(() => false);
    if (!inProgress) throw new Error("No se mostró el estado de análisis en curso.");
    await analysis;
    await page.getByText("Análisis completado.").waitFor({ timeout: 30000 });
  });

  await step("05-programas-guia-progreso", async () => {
    await goTab("Programas");
    await page.getByRole("heading", { name: "Tus programas SAS" }).waitFor();
    await goTab("Plan de migración");
    await page.getByRole("button", { name: /Preparar guías de migración/ }).click();
    await page.getByRole("link", { name: /Abrir guía/ }).first().waitFor({ timeout: 30000 });
    const guideLink = page.getByRole("link", { name: /Abrir guía/ }).first();
    const guideHref = await guideLink.getAttribute("href");
    await guideLink.click();
    await page.locator("article.step").first().waitFor();
    const progress = page.locator("article.step").first().getByLabel("Progreso del paso");
    const options = await progress.locator("option").allTextContents();
    for (const status of ["Pendiente", "En progreso", "Completado", "Bloqueado"]) {
      if (!options.includes(status)) throw new Error(`Falta la opción de progreso: ${status}`);
    }
    await progress.selectOption("in_progress");
    await page.waitForFunction(() => document.querySelector("article.step select")?.value === "in_progress");
    await page.waitForTimeout(250);
    await page.reload();
    await page.locator("article.step").first().waitFor();
    await page.waitForFunction(() => document.querySelector("article.step select")?.value === "in_progress");
    await page.keyboard.press("Tab");
    if (!guideHref) throw new Error("La guía no tiene destino navegable.");
  });

  await step("06-exportar-descargas", async () => {
    await goTab("Exportar");
    await page.getByRole("button", { name: "Exportar planes" }).click();
    await page.getByText("Exportación preparada.").waitFor({ timeout: 30000 });
    const download = page.waitForEvent("download");
    await page.getByRole("button", { name: "Markdown", exact: true }).first().click();
    const file = await download;
    const outputPath = join(shots, file.suggestedFilename());
    await file.saveAs(outputPath);
    const content = await readFile(outputPath, "utf8");
    if (!content.includes("En progreso") || !content.includes("Estado de la guía")) throw new Error("La guía descargada no conserva el estado guardado.");
    const jsonDownload = page.waitForEvent("download");
    await page.getByRole("button", { name: "JSON", exact: true }).first().click();
    const jsonFile = await jsonDownload;
    const jsonPath = join(shots, jsonFile.suggestedFilename());
    await jsonFile.saveAs(jsonPath);
    const exported = JSON.parse(await readFile(jsonPath, "utf8"));
    const exportedSteps = [...(exported.steps ?? []), ...(exported.children ?? []).flatMap((child) => child.steps ?? [])];
    if (!exportedSteps.some((step) => step.status === "in_progress")) throw new Error("El JSON no conserva el progreso guardado.");
  });

  await step("07-sin-archivos-compatibles", async () => {
    await createProject(`E2E sin soporte ${Date.now()}`);
    await page.getByLabel("Archivo ZIP o programa SAS").setInputFiles({ name: "sin-soporte.zip", mimeType: "application/zip", buffer: unsupportedZip });
    await goTab("Mis archivos");
    await page.getByRole("heading", { name: "No encontramos archivos compatibles" }).waitFor({ timeout: 30000 });
    await page.getByText(/Se omitieron 1 archivos/).waitFor();
  });

  await step("08-etiquetas-teclado-movil", async () => {
    await page.getByRole("navigation", { name: "Navegación principal" }).waitFor();
    await page.getByRole("navigation", { name: "Secciones del proyecto" }).waitFor();
    await page.setViewportSize({ width: 390, height: 844 });
    const horizontalOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
    if (horizontalOverflow) throw new Error("La vista móvil presenta desbordamiento horizontal.");
  });
} finally {
  await browser.close();
}
if (errors.length) {
  console.error("Errores de consola/navegador:", errors);
  process.exit(1);
}
console.log(`Recorrido E2E completado. ZIP SAS probado: ${sasFixture.name}. Evidencia: ${shots}`);
