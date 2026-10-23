import { toast } from "sonner";
import { ApiError } from "./api";

const GENERAL_ERROR = "No pudimos completar la acción. Vuelve a intentarlo. Si el problema continúa, contacta al equipo de soporte.";
const CONNECTION_ERROR = "No pudimos conectar con el servicio. Comprueba tu conexión e inténtalo de nuevo.";
const TECHNICAL_DETAIL = /traceback|stack trace|exception|internal server error|failed to fetch|networkerror|localhost|127\.0\.0\.1|\bSQL\b|[A-Z]:\\|\/(?:home|var)\//i;

function safeDetail(message: string): string | undefined {
  const detail = message.trim();
  if (!detail || detail.length > 240 || TECHNICAL_DETAIL.test(detail)) return undefined;
  return detail;
}

function sentence(message: string): string {
  const text = message.trim();
  return `${text.charAt(0).toLocaleUpperCase("es")}${text.slice(1)}`;
}

export function formatErrorMessage(error: unknown, fallback = GENERAL_ERROR, status?: number): string {
  const message = error instanceof Error ? error.message : typeof error === "string" ? error : "";
  const code = status ?? (error instanceof ApiError ? error.status : undefined);
  if (code === 0 || /failed to fetch|networkerror|load failed/i.test(message)) return CONNECTION_ERROR;

  const detail = safeDetail(message);
  if (code === 401) return "Tu sesión ya no es válida. Vuelve a cargar la página e inténtalo de nuevo.";
  if (code === 403) return detail ? `No tienes permiso para realizar esta acción. ${sentence(detail)}` : "No tienes permiso para realizar esta acción.";
  if (code === 404) {
    if (/proyecto no encontrado/i.test(detail ?? "")) return "No encontramos el proyecto. Puede que se haya eliminado o que el enlace ya no sea válido.";
    return detail ? `No encontramos lo que buscas. ${sentence(detail)}` : "No encontramos lo que buscas. Comprueba que el enlace siga vigente.";
  }
  if (code === 409) return detail ? sentence(detail) : "El estado del proyecto cambió. Actualiza la información e inténtalo de nuevo.";
  if (code === 413) return "El archivo supera el tamaño permitido. Reduce su tamaño o divide el paquete e inténtalo de nuevo.";
  if (code === 422) return detail ? `Revisa el archivo o los datos. ${sentence(detail)}` : "El archivo o los datos no tienen un formato válido. Revísalos e inténtalo de nuevo.";
  if (code === 429) return detail ? sentence(detail) : "Hay varias tareas en curso. Espera un momento e inténtalo de nuevo.";
  if (code !== undefined && code >= 500) return "El servicio tuvo un problema inesperado. Inténtalo de nuevo en unos minutos.";
  if (code === 400) return detail ? `No pudimos aceptar los datos. ${sentence(detail)}` : "Revisa los datos e inténtalo de nuevo.";
  return detail ? sentence(detail) : fallback;
}

export function notifyError(error: unknown, title: string, fallback?: string): string {
  const message = formatErrorMessage(error, fallback);
  toast.error(title, { description: message, duration: 7000 });
  return message;
}

export function notifySuccess(title: string, description?: string): void {
  toast.success(title, { description, duration: 4500 });
}
