import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Icon } from "../components/Icon";
import type { Summary } from "../types";
import { Badge, Load, link, prioTone } from "./common";

export function SummaryTab({ id }: { id: string }) {
  const inventory = useAsync(() => api.inventory(id), [id]);
  const [s, setS] = useState<Summary>();
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string>();
  const run = async () => {
    setBusy(true); setErr(undefined);
    try { setS(await api.analyze(id)); }
    catch (x) { setErr((x as Error).message); }
    finally { setBusy(false); }
  };
  return <>
    <h1>Conoce tu punto de partida</h1>
    <p className="subtitle">Analiza tus programas para descubrir cómo funcionan y qué necesita atención antes de migrar.</p>
    <Load q={inventory}>{(m) => <section className="panel">
      <div className="panel-heading"><Icon name={m.files.length ? "chart" : "upload"} size={28} /><div><h2>{m.files.length ? "Tu proyecto está listo para analizar" : "Empecemos por tus archivos"}</h2><p>{m.files.length ? `${m.files.length} archivos cargados. El análisis identifica programas, instrucciones y aspectos por revisar.` : "Carga tus programas SAS para obtener un resumen de tu proyecto."}</p></div></div>
      {m.files.length ? <button onClick={run} disabled={busy}><Icon name="play" size={16} />{busy ? "Analizando proyecto…" : s ? "Volver a analizar" : "Analizar proyecto"}</button> : <a className="button" href={link(id, "importar")}><Icon name="upload" size={18} /> Cargar mis archivos <Icon name="arrow" size={16} /></a>}
      {busy && <p role="status" className="loading-state"><span className="spinner" /> Estamos revisando tus programas. Puedes esperar en esta pantalla.</p>}
    </section>}</Load>
    {err && <div className="notice error-notice" role="alert"><Icon name="warning" /><span>{err}</span></div>}
    {s ? <>
      <div className="notice" role="status"><Icon name="check" /><span><strong>Análisis completado.</strong> Ya puedes explorar tus programas y generar el plan de migración.</span></div>
      <div className="metrics"><div className="metric"><strong>{s.programs}</strong><span>Programas analizados</span></div><div className="metric"><strong>{s.statements}</strong><span>Instrucciones encontradas</span></div><div className="metric"><strong>{s.unrecognized}</strong><span>Instrucciones sin reconocer</span></div><div className="metric"><strong>{s.macro_fragments}</strong><span>Fragmentos de macros</span></div></div>
      <div className="next-actions"><a className="button" href={link(id, "planes")}>Preparar plan de migración <Icon name="arrow" size={17} /></a><a className="button secondary" href={link(id, "dependencias")}><Icon name="flow" size={18} /> Explorar flujo de datos</a></div>
      <h2>Resultado por tipo de instrucción</h2><p className="muted">Prioridades de revisión: P0 = cobertura básica · P1 = revisión adicional · P2 = requiere decisión manual.</p>
      <p>{Object.entries(s.findings_by_priority).map(([p, n]) => <Badge key={p} tone={prioTone(p)}>{p}: {n} hallazgos</Badge>)}</p>
      <table><thead><tr><th>Tipo de instrucción</th><th>Prioridad</th><th className="num">Cantidad</th></tr></thead><tbody>{s.coverage.map((c) => <tr key={c.tag}><td>{c.tag}</td><td><Badge tone={prioTone(c.priority)}>{c.priority}</Badge></td><td className="num">{c.count}</td></tr>)}</tbody></table>
    </> : <div className="notice"><Icon name="info" /><span><strong>¿Qué obtendrás?</strong> Un inventario de programas, un mapa de sus conexiones y una base para preparar tu plan. Si ya analizaste este proyecto, consulta los resultados en las pestañas de arriba.</span></div>}
  </>;
}
