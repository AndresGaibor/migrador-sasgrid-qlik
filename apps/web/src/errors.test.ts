import { expect, test } from "bun:test";
import { ApiError } from "./api";
import { formatErrorMessage } from "./errors";

test("formats connectivity errors as a clear next step", () => {
  expect(formatErrorMessage(new ApiError(0, "Failed to fetch"))).toContain("Comprueba tu conexión");
});

test("keeps useful validation details in friendly language", () => {
  expect(formatErrorMessage(new ApiError(422, "solo se permiten archivos .zip"))).toBe(
    "Revisa el archivo o los datos. Solo se permiten archivos .zip",
  );
});

test("explains common project conflicts without hiding their cause", () => {
  expect(formatErrorMessage(new ApiError(409, "los planes aún no fueron generados"))).toBe(
    "Los planes aún no fueron generados",
  );
});

test("does not expose technical server details", () => {
  expect(formatErrorMessage(new ApiError(500, "Traceback: database error at 127.0.0.1"))).toContain(
    "problema inesperado",
  );
});
