import { useRef, type KeyboardEvent } from "react";
import type { ComponentTab } from "./panel-types";

export const TAB_LABELS: Record<ComponentTab, string> = {
  basic: "Basic settings",
  advanced: "Advanced settings",
  dynamic: "Dynamic settings",
  view: "View",
  documentation: "Documentation",
};

export const STUDIO_TABS: ComponentTab[] = ["basic", "advanced", "dynamic", "view", "documentation"];

type Props = {
  tabs: ComponentTab[];
  active: ComponentTab;
  onChange: (tab: ComponentTab) => void;
  /** Prefijo para los id de tab y de panel (aria-controls / aria-labelledby). */
  idPrefix: string;
};

// Pestañas inferiores estilo Eclipse. Teclado: flechas izquierda/derecha, Inicio y Fin.
export function StudioTabs({ tabs, active, onChange, idPrefix }: Props) {
  const refs = useRef<Record<string, HTMLButtonElement | null>>({});

  const focusAndSelect = (tab: ComponentTab) => {
    onChange(tab);
    refs.current[tab]?.focus();
  };

  const onKeyDown = (event: KeyboardEvent<HTMLButtonElement>) => {
    const index = tabs.indexOf(active);
    let next: number | null = null;
    if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
    else if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
    else if (event.key === "Home") next = 0;
    else if (event.key === "End") next = tabs.length - 1;
    if (next === null) return;
    event.preventDefault();
    focusAndSelect(tabs[next]);
  };

  return (
    <div className="studio-tabs" role="tablist" aria-label="Pestañas del componente" aria-orientation="horizontal">
      {tabs.map((tab) => {
        const selected = tab === active;
        return (
          <button
            key={tab}
            ref={(el) => { refs.current[tab] = el; }}
            type="button"
            role="tab"
            id={`${idPrefix}-tab-${tab}`}
            aria-selected={selected}
            aria-controls={`${idPrefix}-panel`}
            tabIndex={selected ? 0 : -1}
            className={`studio-tab${selected ? " is-active" : ""}`}
            onClick={() => onChange(tab)}
            onKeyDown={onKeyDown}
          >
            {TAB_LABELS[tab]}
          </button>
        );
      })}
    </div>
  );
}
