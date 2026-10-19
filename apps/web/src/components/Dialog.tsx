import { useEffect, useId, useRef, type ReactNode } from "react";
import { Icon } from "./Icon";

export function Dialog({ title, onClose, children }: { title: string; onClose: () => void; children: ReactNode }) {
  const ref = useRef<HTMLDialogElement>(null);
  const titleId = useId();
  useEffect(() => {
    const previous = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    ref.current?.showModal();
    ref.current?.querySelector("input")?.focus();
    return () => { previous?.focus(); };
  }, []);
  return <dialog ref={ref} className="dialog" aria-labelledby={titleId} onClose={onClose}>
    <div className="dialog-heading"><h2 id={titleId}>{title}</h2><button type="button" className="icon-button" aria-label="Cerrar ventana" onClick={() => ref.current?.close()}><Icon name="close" /></button></div>
    {children}
  </dialog>;
}
