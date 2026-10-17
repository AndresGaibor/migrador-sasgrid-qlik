import { useState } from "react";
import { api } from "../api";
import { useAsync } from "../hooks";
import { Load } from "./common";

export function ProjectsView({ go }: { go: (h: string) => void }) {
  const q = useAsync(api.projects, []);
  const [name, setName] = useState("");
  const [err, setErr] = useState<string>();
  const create = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const p = await api.createProject(name.trim());
      go(`/p/${p.id}/importar`);
    } catch (x) {
      setErr((x as Error).message);
    }
  };
  return (
    <>
      <h1>Proyectos</h1>
      <form onSubmit={create} className="row">
        <label>
          Nombre
          <input value={name} onChange={(e) => setName(e.target.value)} required />
        </label>
        <button disabled={!name.trim()}>Crear proyecto</button>
      </form>
      {err && <p className="error">{err}</p>}
      <Load q={q}>
        {(ps) =>
          ps.length === 0 ? (
            <p className="muted">Sin proyectos todavía.</p>
          ) : (
            <ul className="list">
              {ps.map((p) => (
                <li key={p.id}>
                  <a href={`#/p/${p.id}/resumen`}>{p.name}</a> <span className="muted">{p.id}</span>
                </li>
              ))}
            </ul>
          )
        }
      </Load>
    </>
  );
}
