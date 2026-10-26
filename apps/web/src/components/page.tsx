import type { ReactNode } from "react";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Icon, type IconName } from "./Icon";

export function PageTitle({ title, children, actions }: { title: string; children?: ReactNode; actions?: ReactNode }) {
  return (
    <div className="mb-4 flex items-start justify-between gap-4">
      <div><h1>{title}</h1>{children && <p className="mt-0.5 text-muted-foreground">{children}</p>}</div>
      {actions && <div className="flex shrink-0 gap-2">{actions}</div>}
    </div>
  );
}

export function Notice({ icon = "info", tone = "default", children }: { icon?: IconName; tone?: "default" | "destructive"; children: ReactNode }) {
  return <Alert variant={tone} className="my-3"><Icon name={icon} /><AlertDescription>{children}</AlertDescription></Alert>;
}

export function Stat({ value, label }: { value: ReactNode; label: string }) {
  return <div className="rounded-md border bg-card px-3 py-2"><div className="text-xl font-semibold tabular-nums">{value}</div><div className="text-muted-foreground">{label}</div></div>;
}
