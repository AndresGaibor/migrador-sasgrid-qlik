import { useMemo, useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import { ComponentIcon } from "../components/ComponentIcon";
import type { CatalogComponent, CatalogItem } from "../types";
import { filterCatalogItems, getGuideCatalogItems } from "../catalog-explorer";
import { Badge, Load } from "./common";

type DisplayItem = CatalogItem & { guideScope?: "principal" | "alternativa" };

export function CatalogView({ name }: { name?: string }) {
  return name ? <ComponentDetail name={name} /> : <CatalogList />;
}

function CatalogList() {
  const [q, setQ] = useState("");
  const [family, setFamily] = useState("");
  const [guideOnly, setGuideOnly] = useState(false);
  const res = useAsync(() => api.catalog(q, guideOnly ? "" : family), [q, family, guideOnly]);
  const globalConfig = useAsync(() => api.studioConfiguration(), []);
  const officialNames = res.data?.official_component_names ?? [];
  const officialNameSet = useMemo(() => new Set(officialNames), [officialNames]);
  const guideItems: DisplayItem[] = useMemo(() => getGuideCatalogItems()
    .filter((item) => officialNameSet.has(item.name))
    .map((item) => ({
      name: item.name,
      description: "Candidato de una guía de migración; abre la ficha actual de Studio 8.",
      families: [],
      documentation_status: "guide",
      lifecycle_status: "current",
      frameworks: [],
      license_profile: { code: "TP_ALL", label: "Talend Data Fabric" },
      guideScope: item.scope,
    })), [officialNameSet]);
  const guideCandidates = guideItems.filter((item) => item.guideScope === "principal").length;
  const alternatives = guideItems.length - guideCandidates;
  const families = Object.keys(res.data?.families ?? {}).sort();
  const catalogItems = (res.data?.components ?? []) as DisplayItem[];
  const visible = filterCatalogItems(guideOnly ? guideItems : catalogItems, {
    query: q,
    family: guideOnly ? "" : family,
  });

  return (
    <>
      <div className="eyebrow">BIBLIOTECA DE RECURSOS</div>
      <h1>Catálogo de Talend Studio 8</h1>
      <p className="subtitle">Catálogo oficial contrastado con el inventario de tu Studio, incluidas todas las paletas. Si no existe un SVG nativo, el componente se muestra sin icono.</p>
      <div className="catalog-filters">
        <label className="catalog-search">
          Buscar componente
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="tFilterRow, base de datos, agregar…" />
        </label>
        {!guideOnly && <label>
          Familia
          <select value={family} onChange={(e) => setFamily(e.target.value)}>
            <option value="">Todas las familias</option>
            {families.map((f) => <option key={f} value={f}>{f}</option>)}
          </select>
        </label>}
      </div>
      <label className="catalog-guide-toggle">
        <input type="checkbox" checked={guideOnly} onChange={(e) => { setGuideOnly(e.target.checked); setFamily(""); }} />
        <span><strong>Mostrar componentes usados por la guía</strong><small>{guideCandidates} candidatos principales y {alternatives} alternativas incluidas en esta instalación.</small></span>
      </label>
      <Load q={res}>{(data) => <CatalogResults
        items={visible}
        count={guideOnly ? guideItems.length : data.count}
        hasMore={!guideOnly && data.has_more}
      />}</Load>
      {!guideOnly && res.data?.official_documentation_inventory && (
        <p className="muted">Perfil: {res.data.official_documentation_inventory.license_profile.label} · {res.data.official_documentation_inventory.count} componentes de este catálogo presentes en Studio; {res.data.official_documentation_inventory.documented} con ficha Qlik y {res.data.official_documentation_inventory.exception} excepciones documentales. <a href={res.data.official_documentation_inventory.source} target="_blank" rel="noreferrer">Ver disponibilidad oficial ↗</a></p>
      )}
      {!guideOnly && <details>
        <summary>Configuración global de Talend Studio 8</summary>
        <Load q={globalConfig}>{(data) => <>
          <p className="muted">{data.target}. <a href={data.source} target="_blank" rel="noreferrer">Índice oficial de configuración ↗</a></p>
          <pre className="doc">{data.markdown}</pre>
        </>}</Load>
      </details>}
    </>
  );
}

function CatalogResults({ items, count, hasMore = false }: { items: DisplayItem[]; count: number; hasMore?: boolean }) {
  return (
    <>
      <p className="muted" aria-live="polite">{items.length} resultados{hasMore ? " · hay más de 300; refina la búsqueda" : count > items.length ? ` · catálogo: ${count} componentes` : ""}</p>
      {items.length === 0 ? (
        <div className="empty-state"><h2>No encontramos componentes</h2><p>Prueba otro nombre o familia.</p></div>
      ) : (
        <div className="table-wrap"><table className="catalog-table">
          <thead><tr><th>Componente</th><th>Función</th><th>Familia</th><th>Uso en guía</th><th>Documentación Studio 8</th></tr></thead>
          <tbody>{items.map((item) => <CatalogRow key={item.name} item={item} />)}</tbody>
        </table></div>
      )}
    </>
  );
}

function CatalogRow({ item }: { item: DisplayItem }) {
  return (
    <tr>
      <td><a className="catalog-component-link" href={`#/catalogo/${item.name}`}><ComponentIcon name={item.name} className="catalog-component-icon" /><code>{item.name}</code></a></td>
      <td>{item.description}</td>
      <td>{item.families.join(", ")}</td>
      <td>{item.guideScope ? <Badge tone={item.guideScope === "principal" ? "ok" : "neutral"}>{item.guideScope === "principal" ? "Principal" : "Alternativa"}</Badge> : <span className="muted">—</span>}</td>
      <td>
        <Badge tone={item.documentation_status === "documented" ? "ok" : item.documentation_status === "guide" ? "neutral" : "warn"}>
          {item.documentation_status === "documented" ? "Ficha Qlik 8.0" : item.documentation_status === "guide" ? "En guía de migración" : "Revisión documental"}
        </Badge>
        <div className="catalog-row-note">{item.frameworks.join(", ")}</div>
      </td>
    </tr>
  );
}

function ComponentDetail({ name }: { name: string }) {
  const query = useAsync(() => api.component(name), [name]);
  if (query.loading && !query.data) return <div className="loading-state" role="status"><span className="spinner" /> Cargando información…</div>;
  return <Load q={query}>{(component) => <ComponentBody name={name} component={component} />}</Load>;
}

function ComponentBody({ name, component }: { name: string; component: CatalogComponent }) {
  const doc = component.official_documentation;
  const routePages = doc?.routes?.flatMap((route) => route.pages) ?? [];
  const componentPage = doc?.status === "documented" ? routePages.find((page) => page.status === "ok") : undefined;
  const configurationPages = (doc?.configuration_pages ?? [])
    .filter((page) => page.status === "ok" && !page.title?.toLowerCase().includes("deprecated"))
    .filter((page, index, pages) => pages.findIndex((candidate) => candidate.url === page.url) === index);
  const configurationSections = (doc?.configuration_sections ?? [])
    .filter((section) => !section.heading.toLowerCase().includes("deprecated"))
    .filter((section, index, sections) => sections.findIndex((candidate) => candidate.url === section.url && candidate.heading === section.heading) === index);
  return (
    <>
      <p><a href="#/catalogo">← Volver al catálogo</a></p>
      <div className="eyebrow">TALEND STUDIO 8 · FICHA OFICIAL</div>
      <h1 className="component-heading"><ComponentIcon name={name} className="catalog-component-icon" />{name}</h1>
      <p className="subtitle">{component.description}</p>
      <div className="catalog-state-grid" aria-label="Estados del componente">
        <section className="catalog-state-card">
          <span className="catalog-state-icon" aria-hidden="true"><Icon name="book" size={22} /></span>
          <div><strong>Disponibilidad oficial</strong><p>Disponible para el perfil Talend Data Fabric seleccionado. Esto no confirma que esté instalado en tu entorno.</p></div>
          <Badge tone="ok">Data Fabric</Badge>
        </section>
        <section className="catalog-state-card">
          <span className="catalog-state-icon" aria-hidden="true"><Icon name="check" size={22} /></span>
          <div><strong>Verificación del entorno</strong><p>No se ha probado en un Job real ni confirmado contra la licencia instalada.</p></div>
          <Badge tone="warn">Sin verificar</Badge>
        </section>
      </div>
      <section className="panel catalog-audit-panel">
        <div className="section-heading"><h2>Referencia de Talend Studio 8.0 R2026-09</h2>
          {doc?.status === "documented" ? <Badge tone="ok">Ficha Qlik localizada</Badge> : <Badge tone="warn">Revisión documental</Badge>}
        </div>
        <dl className="catalog-facts">
          <div><dt>Familia</dt><dd>{component.families.join(", ") || "Sin familia en la disponibilidad oficial"}</dd></div>
          <div><dt>Perfil de licencia</dt><dd>{component.official_availability?.license_profile.label ?? "Sin datos"}</dd></div>
          <div><dt>Frameworks vigentes</dt><dd>{component.official_availability?.frameworks.map((item) => item.label).join(", ") || "Sin datos"}</dd></div>
          <div><dt>Guía de migración</dt><dd>{doc?.status === "documented" ? "Consulta las páginas oficiales enlazadas abajo." : "No se encontró una ficha específica vigente; no se sustituyó por documentación antigua o comunitaria."}</dd></div>
        </dl>
        {componentPage && <p><a href={componentPage.url} target="_blank" rel="noreferrer">Abrir ficha oficial del componente ↗</a></p>}
        {doc?.status === "documented" && <>
          {configurationPages.length > 0 && <>
            <h3>Páginas de configuración</h3>
            <ul>{configurationPages.map((page) => <li key={page.url}><a href={page.url} target="_blank" rel="noreferrer">{page.title ?? page.url}</a></li>)}</ul>
          </>}
          {configurationSections.length > 0 && <details><summary>{configurationSections.length} secciones oficiales de configuración</summary>
            <ul>{configurationSections.map((section, index) => <li key={`${section.url}-${section.heading}-${index}`}><a href={section.url} target="_blank" rel="noreferrer">{section.heading}</a></li>)}</ul>
          </details>}
        </>}
        {doc?.status === "exception" && <p className="notice warning">No se encontró una ficha específica de Qlik que coincida con este componente en Studio 8. Se mantiene como excepción; no se usa contenido comunitario ni de otra versión.</p>}
      </section>
    </>
  );
}
