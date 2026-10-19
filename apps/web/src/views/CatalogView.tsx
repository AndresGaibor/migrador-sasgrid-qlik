import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { ComponentIcon } from "../components/ComponentIcon";
import type { CatalogComponent, CatalogParam } from "../types";
import { Badge, Load } from "./common";

export function CatalogView({ name }: { name?: string }) {
  return name ? <ComponentDetail name={name} /> : <CatalogList />;
}

function CatalogList() {
  const [q, setQ] = useState("");
  const [family, setFamily] = useState("");
  const res = useAsync(() => api.catalog(q, family), [q, family]);
  return (
    <>
      <h1>Catálogo de componentes Talend</h1>
      <p className="muted">
        Esquemas estructurados derivados de las definiciones abiertas de Talend Open Studio (Talaxie). El inventario oficial de Qlik aparece abajo; la documentación se descarga con <code>tools/fetch_talend_docs.py</code>.
      </p>
      <div className="row">
        <label>
          Buscar
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="tFilterRow, oracle, join…" />
        </label>
        <label>
          Familia
          <select value={family} onChange={(e) => setFamily(e.target.value)}>
            <option value="">Todas</option>
            {Object.entries(res.data?.families ?? {}).map(([f, n]) => (
              <option key={f} value={f}>{f} ({n})</option>
            ))}
          </select>
        </label>
      </div>
      <Load q={res}>
        {(d) => (
          <>
            <p className="muted">{d.components.length} de {d.count} componentes</p>
            <table>
              <thead><tr><th>Componente</th><th>Descripción</th><th>Familias</th><th>Parámetros</th></tr></thead>
              <tbody>
                {d.components.map((c) => (
                  <tr key={c.name}>
                    <td><a href={`#/catalogo/${c.name}`}><ComponentIcon name={c.name} /> {c.name}</a></td>
                    <td>{c.description}</td>
                    <td>{c.families.join(", ")}</td>
                    <td className="num">{c.parameters}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </>
        )}
      </Load>
      {res.data?.official_inventory && (
        <details>
          <summary>
            Inventario oficial Qlik {res.data.official_inventory.release} ({res.data.official_inventory.count} componentes)
          </summary>
          <p><a href={res.data.official_inventory.source} target="_blank" rel="noreferrer">Fuente oficial: componentes soportados y lineage</a></p>
          <table>
            <thead><tr><th>Componente</th><th>Conectividad</th><th>Disponible desde</th><th>Nota</th></tr></thead>
            <tbody>{res.data.official_inventory.components.map((c) => (
              <tr key={c.name}>
                <td><code>{c.name}</code></td><td>{c.connectivity ?? ""}</td>
                <td>{c.available_from ?? ""}</td><td>{c.note ?? ""}</td>
              </tr>
            ))}</tbody>
          </table>
        </details>
      )}
    </>
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
  return (
    <>
      <p><a href="#/catalogo">← Catálogo</a></p>
      <Load q={q}>{(c) => <Body c={c} />}</Load>
    </>
  );
}

function Body({ c }: { c: CatalogComponent }) {
  return (
    <>
      <h1 className="component-heading"><ComponentIcon name={c.name} /> {c.name}</h1>
      <p>{c.description}</p>
      <p className="muted">Los esquemas y parametros son candidatos derivados de la comunidad. El enlace oficial no significa que el componente o sus propiedades se hayan probado en Studio.</p>
      <p className="muted">
        Familias: {c.families.join(", ")} · versión {c.version} · {c.status}
        {c.doc_url && <> · <a href={c.doc_url} target="_blank" rel="noreferrer">documentación oficial</a></>}
      </p>
      {c.variants.length > 0 && (
        <p>
          Variantes (otra tecnología, mismo rol):{" "}
          {c.variants.slice(0, 40).map((v) => <a key={v} href={`#/catalogo/${v}`} className="chip">{v}</a>)}
        </p>
      )}
      <h2>Conectores</h2>
      <p>{c.connectors.map((k, i) => <Badge key={i}>{k.name ? `${k.type}:${k.name}` : k.type}</Badge>)}</p>
      <h2>Parámetros</h2>
      <table>
        <thead><tr><th>Nombre interno</th><th>Etiqueta</th><th>Campo</th><th>Por defecto</th><th>Opciones / columnas</th></tr></thead>
        <tbody>{c.parameters.map((p) => <Param key={p.name} p={p} />)}</tbody>
      </table>
      {c.imports && c.imports.length > 0 && (
        <>
          <h2>Drivers y librerías</h2>
          <ul>{c.imports.map((i, k) => <li key={k}><code>{i.module}</code> {i.required_if && <span className="muted">si {i.required_if}</span>}</li>)}</ul>
        </>
      )}
      {c.doc_markdown ? (
        <details>
          <summary>Documentación local (help.qlik.com)</summary>
          <pre className="doc">{c.doc_markdown}</pre>
        </details>
      ) : (
        <p className="muted">Documentación local no descargada: <code>uv run tools/fetch_talend_docs.py</code>.</p>
      )}
    </>
  );
}
