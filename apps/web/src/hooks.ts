import { useCallback, useEffect, useState } from "react";

export type Async<T> = { data?: T; error?: string; loading: boolean; reload: () => void };

export function useAsync<T>(fn: () => Promise<T>, deps: unknown[]): Async<T> {
  const [state, set] = useState<{ data?: T; error?: string; loading: boolean }>({ loading: true });
  const [tick, setTick] = useState(0);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => {
    let live = true;
    set((s) => ({ ...s, loading: true }));
    fn()
      .then((data) => live && set({ data, loading: false }))
      .catch((e: Error) => live && set((s) => ({ ...s, error: e.message, loading: false })));
    return () => {
      live = false;
    };
  }, [...deps, tick]);
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
