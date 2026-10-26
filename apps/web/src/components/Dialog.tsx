import type { ReactNode } from "react";
import { Icon } from "./Icon";
import { Dialog as RadixDialog, DialogContent, DialogTitle } from "./ui/dialog";

// Ventana modal con Radix (shadcn) y la forma de styles.css: una sola forma en toda la app.
export function Dialog({ title, onClose, children }: { title: string; onClose: () => void; children: ReactNode }) {
  return (
    <RadixDialog open onOpenChange={(open) => { if (!open) onClose(); }}>
      <DialogContent className="dialog" showCloseButton={false} aria-describedby={undefined}>
        <div className="dialog-heading">
          <DialogTitle>{title}</DialogTitle>
          <button type="button" className="icon-button" aria-label="Cerrar ventana" onClick={onClose}><Icon name="close" /></button>
        </div>
        {children}
      </DialogContent>
    </RadixDialog>
  );
}
