import { Icon } from "../components/Icon";

export function HomeView() {
  return <div className="home-overview">
    <div className="page-heading"><div><h1>De SAS Grid a Talend</h1><p className="subtitle">Analiza tus programas SAS y prepara su migración a Talend Studio.</p></div><a className="button" href="#/projects/nuevo"><Icon name="upload" size={18} />Crear proyecto desde ZIP</a></div>
    <section className="journey" aria-labelledby="home-process-title">
      <div className="journey-heading"><h2 id="home-process-title">Cómo funciona</h2><p>Cada ZIP se analiza en un proyecto independiente, sin mezclar archivos.</p></div>
      <ol className="journey-steps">
        <li><span className="journey-icon"><Icon name="upload" size={23} /></span><div><h3>Carga tus programas</h3><p>Sube un ZIP. La extracción y el análisis comienzan automáticamente.</p></div></li>
        <li><span className="journey-icon"><Icon name="chart" size={23} /></span><div><h3>Revisa el análisis</h3><p>Consulta los programas, sus dependencias y los puntos pendientes.</p></div></li>
        <li><span className="journey-icon"><Icon name="flow" size={23} /></span><div><h3>Sigue el plan de migración</h3><p>Crea la estructura, completa y prueba los Jobs y configura su programación.</p></div></li>
      </ol>
    </section>
    <section className="home-continue"><div><h2>¿Ya tienes un proyecto?</h2><p>Abre sus archivos, revisa el análisis o continúa con las guías de migración.</p></div><a className="button secondary" href="#/projects">Ver mis proyectos <Icon name="arrow" size={17} /></a></section>
    <p className="home-scope-note"><Icon name="info" size={17} /><span>El MCP puede crear componentes y conexiones en Talend Studio. La revisión, las pruebas y la publicación de los Jobs siguen siendo necesarias.</span></p>
  </div>;
}
