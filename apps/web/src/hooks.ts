import { useCallback, useEffect, useState } from "react";

export type Async<T> = { data?: T; error?: string; errorStatus?: number; loading: boolean; reload: () => void };

export function useAsync<T>(
  fn: () => Promise<T>,
  deps: unknown[],
  options: { preserveDataOnError?: boolean } = {},
): Async<T> {
  const [state, set] = useState<{ data?: T; error?: string; errorStatus?: number; loading: boolean }>({ loading: true });
  const [tick, setTick] = useState(0);
  const preserveDataOnError = options.preserveDataOnError ?? false;
  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => {
    let live = true;
    set((s) => ({ ...s, loading: true }));
    fn()
      .then((data) => live && set({ data, loading: false }))
      .catch((error: unknown) => {
        if (!live) return;
        const message = error instanceof Error ? error.message : "Error inesperado";
        const status = typeof error === "object" && error !== null && "status" in error && typeof error.status === "number"
          ? error.status
          : undefined;
        set((s) => preserveDataOnError
          ? { ...s, error: message, errorStatus: status, loading: false }
          : { error: message, errorStatus: status, loading: false });
      });
    return () => {
      live = false;
    };
  }, [...deps, tick, preserveDataOnError]);
  return { ...state, reload: useCallback(() => setTick((t) => t + 1), []) };
}

export function decodeHash(hash: string): string {
  const raw = hash.slice(1);
  if (!raw) return "/";
  try { return decodeURIComponent(raw); } catch { return raw; }
}

export function useHash(): [string, (h: string) => void] {
  const read = () => decodeHash(location.hash);
  const [h, setH] = useState(read);
  useEffect(() => {
    const on = () => setH(read());
    window.addEventListener("hashchange", on);
    return () => window.removeEventListener("hashchange", on);
  }, []);
  return [h, (v) => (location.hash = encodeURI(v))];
}
