import { useMemo, useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { CatalogComponent, CatalogItem, CatalogParam } from "../types";
import {
  catalogAudit,
  filterCatalogItems,
  getGuideCatalogItems,
  provenanceLabel,
  type AuditRecord,
  type GuideCatalogItem,
} from "../catalog-explorer";
import { Badge, Load } from "./common";

type DisplayItem = CatalogItem & { audit?: AuditRecord; guideScope?: "principal" | "alternativa" };

export function CatalogView({ name }: { name?: string }) {
  return name ? <ComponentDetail name={name} /> : <CatalogList />;
}

function CatalogList() {
  const [q, setQ] = useState("");
  const [family, setFamily] = useState("");
  const [verification, setVerification] = useState("");
  const [guideOnly, setGuideOnly] = useState(false);
  const res = useAsync(() => api.catalog(q, guideOnly ? "" : family), [q, family, guideOnly]);
  const guideItems = useMemo(() => getGuideCatalogItems(), []);
  const families = guideOnly
    ? [...new Set(guideItems.flatMap((item) => item.families))].sort()
    : Object.keys(res.data?.families ?? {}).sort();
  const guideDisplay: DisplayItem[] = guideItems.map((item) => ({
    name: item.name,
    description: item.description,
    families: item.families,
    parameters: item.parameters,
    audit: item.audit,
    guideScope: item.scope,
  }));
  const catalogDisplay: DisplayItem[] = (res.data?.components ?? []).map((item) => ({
    ...item,
    audit: catalogAudit.recommended_components[item.name],
  }));
  const visible = filterCatalogItems(guideOnly ? guideDisplay : catalogDisplay, {
    query: q,
    family,
    verification,
  });

  return (
    <>
      <div className="eyebrow">BIBLIOTECA DE RECURSOS</div>
      <h1>Catálogo de componentes Talend</h1>
      <p className="subtitle">Busca una pieza por nombre, función o familia. Revisa su referencia documental y comprueba si está validada en Studio antes de usarla.</p>
      <p className="muted">Los esquemas son candidatos derivados de las definiciones abiertas de Talend Open Studio. El inventario oficial de Qlik aparece a continuación; la documentación se descarga con <code>tools/fetch_talend_docs.py</code>.</p>
      <div className="catalog-filters">
        <label className="catalog-search">
          Buscar componente
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="tFilterRow, base de datos, agregar…" />
        </label>
        <label>
          Familia
          <select value={family} onChange={(e) => setFamily(e.target.value)}>
            <option value="">Todas las familias</option>
            {families.map((f) => <option key={f} value={f}>{f}</option>)}
          </select>
        </label>
        <label>
          Estado documental
          <select value={verification} onChange={(e) => setVerification(e.target.value)}>
            <option value="">Todos los estados</option>
            <option value="partially_verified">Referencia cotejada parcialmente</option>
            <option value="needs_review">Requiere revisión</option>
            <option value="unverified">Sin verificar</option>
          </select>
        </label>
      </div>
      <label className="catalog-guide-toggle">
        <input type="checkbox" checked={guideOnly} onChange={(e) => { setGuideOnly(e.target.checked); setFamily(""); }} />
        <span><strong>Mostrar componentes usados por la guía</strong><small>38 candidatos principales y 9 alternativas condicionales de los mappings actuales.</small></span>
      </label>
      {guideOnly ? (
        <CatalogResults items={visible} count={guideItems.length} />
      ) : (
        <Load q={res}>{(data) => <CatalogResults items={visible} count={data.count} />}</Load>
      )}
      {!guideOnly && res.data?.official_inventory && (
        <details>
          <summary>Inventario oficial Qlik {res.data.official_inventory.release} ({res.data.official_inventory.count} componentes)</summary>
          <p><a href={res.data.official_inventory.source} target="_blank" rel="noreferrer">Fuente oficial: componentes soportados y lineage</a></p>
          <table><thead><tr><th>Componente</th><th>Conectividad</th><th>Disponible desde</th><th>Nota</th></tr></thead>
            <tbody>{res.data.official_inventory.components.map((item) => (
              <tr key={item.name}><td><code>{item.name}</code></td><td>{item.connectivity ?? ""}</td><td>{item.available_from ?? ""}</td><td>{item.note ?? ""}</td></tr>
            ))}</tbody>
          </table>
        </details>
      )}
    </>
  );
}

function CatalogResults({ items, count }: { items: DisplayItem[]; count: number }) {
  return (
    <>
      <p className="muted" aria-live="polite">{items.length} resultados{count > items.length ? ` · catálogo: ${count} componentes` : ""}</p>
      {items.length === 0 ? (
        <div className="empty-state"><h2>No encontramos componentes</h2><p>Prueba otro nombre, familia o estado documental.</p></div>
      ) : (
        <div className="table-wrap"><table>
          <thead><tr><th>Componente</th><th>Función</th><th>Familia / versión</th><th>Uso en guía</th><th>Catálogo candidato</th><th>Verificación Studio</th></tr></thead>
          <tbody>{items.map((item) => <CatalogRow key={item.name} item={item} />)}</tbody>
        </table></div>
      )}
    </>
  );
}

function CatalogRow({ item }: { item: DisplayItem }) {
  const record = item.audit;
  return (
    <tr>
      <td><a href={`#/catalogo/${item.name}`}><ComponentIcon name={item.name} /> {item.name}</a></td>
      <td>{record?.official_purpose ?? item.description}</td>
      <td>{record?.official_family ?? item.families.join(", ")}{record?.official_version && <> · {record.official_version}</>}</td>
      <td>{item.guideScope ? <Badge tone={item.guideScope === "principal" ? "ok" : "neutral"}>{item.guideScope === "principal" ? "Principal" : "Alternativa"}</Badge> : <span className="muted">Fuera del alcance auditado</span>}</td>
      <td>{record ? <Badge tone={record.catalog_entry_present ? "ok" : "warn"}>{record.catalog_entry_present ? "En índice comunitario" : "Sin entrada comunitaria"}</Badge> : <Badge>Índice comunitario</Badge>}<div className="catalog-row-note">{provenanceLabel(record?.verification_status)}</div></td>
      <td><Badge tone="warn">Sin verificar en Studio</Badge></td>
    </tr>
  );
}

function Param({ p }: { p: CatalogParam }) {
  return (
    <tr>
      <td className="mono">{p.name}{p.required && " *"}</td>
      <td>{p.label ?? ""}</td>
      <td>{p.field}{p.advanced && <Badge>avanzado</Badge>}</td>
      <td className="mono">{p.default ?? ""}</td>
      <td>
        {p.items?.map((i) => <Badge key={i.name} tone={i.default ? "ok" : "neutral"}>{i.label ?? i.name}</Badge>)}
        {p.columns?.map((c) => <Badge key={c.name}>{c.name}</Badge>)}
      </td>
    </tr>
  );
}

function ComponentDetail({ name }: { name: string }) {
  const q = useAsync(() => api.component(name), [name]);
  const auditRecord = catalogAudit.recommended_components[name];
  const guideItem = getGuideCatalogItems().find((item) => item.name === name);
  if (q.loading && !q.data) return <div className="loading-state" role="status"><span className="spinner" /> Cargando información…</div>;
  if (!q.data && !auditRecord) return <Load q={q}>{(component) => <ComponentBody name={name} component={component} />}</Load>;
  return <ComponentBody name={name} component={q.data} audit={auditRecord} guideItem={guideItem} catalogError={q.error} />;
}

function ComponentBody({
  name,
  component,
  audit,
  guideItem,
  catalogError,
}: {
  name: string;
  component?: CatalogComponent;
  audit?: AuditRecord;
  guideItem?: GuideCatalogItem;
  catalogError?: string;
}) {
  const families = audit?.official_family ? [audit.official_family] : component?.families ?? audit?.catalog_family ?? [];
  return (
    <>
      <p><a href="#/catalogo">← Volver al catálogo</a></p>
      <div className="eyebrow">FICHA DEL COMPONENTE</div>
      <h1 className="component-heading"><ComponentIcon name={name} /> {name}</h1>
      <p className="subtitle">{audit?.official_purpose ?? component?.description ?? "Función oficial pendiente de confirmar."}</p>
      <div className="catalog-state-grid" aria-label="Estados del componente">
        <section className="catalog-state-card">
          <span className="catalog-state-icon" aria-hidden="true">📚</span>
          <div><strong>Candidato del catálogo</strong><p>{audit?.catalog_entry_present ? "El nombre aparece en el índice comunitario usado como semilla." : guideItem ? "Está citado por las reglas de la guía, pero no tiene entrada en el índice comunitario." : "Este componente no forma parte del alcance auditado de la guía."}</p></div>
          <Badge tone={audit?.catalog_entry_present ? "ok" : "warn"}>{audit?.catalog_entry_present ? "Disponible" : "Pendiente"}</Badge>
        </section>
        <section className="catalog-state-card">
          <span className="catalog-state-icon" aria-hidden="true">🧪</span>
          <div><strong>Verificación en Talend Studio</strong><p>No se ha comprobado en un Job real. La versión y edición instaladas no están disponibles en este entorno.</p></div>
          <Badge tone="warn">Sin verificar</Badge>
        </section>
      </div>

      <section className="panel catalog-audit-panel">
        <div className="section-heading"><h2>Referencia oficial</h2>{audit && <Badge tone={audit.verification_status === "partially_verified" ? "ok" : "warn"}>{provenanceLabel(audit.verification_status)}</Badge>}</div>
        <dl className="catalog-facts">
          <div><dt>Familia oficial</dt><dd>{families.join(", ") || "Pendiente de confirmar"}</dd></div>
          <div><dt>Versión documental</dt><dd>{audit?.official_version ?? "Sin cotejo"} · objetivo {catalogAudit.target_version.product} {catalogAudit.target_version.major_version} {catalogAudit.target_version.monthly_release}</dd></div>
          <div><dt>Revisado</dt><dd>{audit?.checked_at ?? "Sin fecha de verificación"}</dd></div>
          <div><dt>Uso en guía</dt><dd>{guideItem ? guideItem.scope === "principal" ? "Candidato principal" : "Alternativa condicional" : "Fuera del alcance auditado"}</dd></div>
        </dl>
        <p className="muted">Esta es la base documental; no confirma qué versión está instalada en tu entorno.</p>
        {audit?.official_url ? <p><a href={audit.official_url} target="_blank" rel="noreferrer">Abrir documentación oficial de Qlik/Talend ↗</a></p> : <p className="muted">No hay una página oficial específica confirmada para este componente.</p>}
        {audit?.official_essential_property_labels.length ? <>
          <h3>Propiedades relevantes según la documentación oficial</h3>
          <ul className="catalog-property-list">{audit.official_essential_property_labels.map((label) => <li key={label}>{label}</li>)}</ul>
        </> : <p className="muted">Las propiedades esenciales oficiales aún no están cotejadas.</p>}
        {audit?.catalog_internal_property_names.length ? <details><summary>Nombres internos del índice comunitario</summary><p className="muted">Estos nombres no se han cotejado con las claves internas de un Job real.</p><div className="chip-list">{audit.catalog_internal_property_names.map((property) => <code key={property}>{property}</code>)}</div></details> : null}
        {audit?.limitations.length ? <><h3>Alcance y pendientes</h3><ul>{audit.limitations.map((limitation) => <li key={limitation}>{limitation}</li>)}</ul></> : null}
      </section>

      {catalogError && <div className="notice warning">La API del catálogo no tiene una ficha técnica para este componente; se muestran solo los datos de auditoría disponibles.</div>}
      {component ? <>
        {component.variants.length > 0 && <><h2>Variantes por tecnología</h2><div className="chip-list">{component.variants.slice(0, 40).map((variant) => <a key={variant} href={`#/catalogo/${variant}`} className="chip">{variant}</a>)}</div></>}
        {component.connectors.length > 0 && <><h2>Conectores del índice</h2><p>{component.connectors.map((connector, index) => <Badge key={index}>{connector.name ? `${connector.type}:${connector.name}` : connector.type}</Badge>)}</p></>}
        <h2>Configuración disponible en el índice</h2>
        <p className="muted">La estructura comunitaria ayuda a explorar campos, pero no confirma su equivalencia con Talend Studio.</p>
        <div className="table-wrap"><table>
          <thead><tr><th>Nombre interno</th><th>Etiqueta</th><th>Campo</th><th>Por defecto</th><th>Opciones / columnas</th></tr></thead>
          <tbody>{component.parameters.map((p) => <Param key={p.name} p={p} />)}</tbody>
        </table></div>
        {component.imports && component.imports.length > 0 && <><h2>Drivers y librerías</h2><ul>{component.imports.map((item, index) => <li key={index}><code>{item.module}</code> {item.required_if && <span className="muted">si {item.required_if}</span>}</li>)}</ul></>}
        {component.doc_markdown ? <details><summary>Documentación local de Qlik Help</summary><pre className="doc">{component.doc_markdown}</pre></details> : null}
      </> : !audit?.catalog_entry_present && <div className="notice warning">No se muestran propiedades ni parámetros porque no existe una ficha de catálogo cotejada para este nombre.</div>}
    </>
  );
}
