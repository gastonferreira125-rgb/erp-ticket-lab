# T01 — v3 — 2026-10-14

## Entrada
```text
ENTRADA:
ticket_id: T01
<ticket>
No puedo registrar un pago a un proveedor. No anoté el mensaje de error.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T01",
  "categoria": "Finanzas",
  "prioridad": "Media",
  "resumen": "El usuario no puede registrar un pago a un proveedor.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Mensaje de error exacto",
    "Pasos para reproducir el problema",
    "Captura de pantalla del error",
    "Nombre del proveedor",
    "Detalle del pago que intenta registrar"
  ]
}
```

## Evaluación manual
Seis campos y tipos correctos. Coinciden T01, Finanzas, Media y referencia null con el conjunto esperado. No hay referencia explícita ni evidencia de un proceso detenido para todo un equipo.

Resumen fiel, sin inventar causa o solución. Mensaje de error, pasos para reproducir y detalles del pago son información útil; captura e identificación del proveedor pueden ayudar y deben solicitarse con el alcance necesario.

## Prueba de regresión
T01 ya coincidía en etiquetas en v0. Esta ejecución de v3 conserva esa coincidencia. La lista de información faltante ahora incluye pasos para reproducir y captura, además de proveedor y pago. No atribuir esa variación exclusivamente al cambio de prompt: es una sola ejecución y los parámetros numéricos no se verificaron en esta captura.

No demuestra ausencia de regresiones en otros casos ni consistencia entre repeticiones. La captura coincide con el JSON pegado. Evaluación manual; no se ejecutó evaluate.py para este registro.

## Continuidad
v3-category-rule, reglas en Sistema y ticket en Usuario según continuidad. Modelo y parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; esta captura no confirma esos parámetros.

Ocho tickets ejecutados con v3. Cinco coinciden completamente: T01, T05, T06, T08, T09. T07 falla categoría; T03 y T04 fallan referencia respecto del conjunto actual. Resultado parcial: 5/8. T04 requiere además revisar la ambigüedad de referencia_documento para códigos de artículo.

Restan T02 y T10 con v3. Mantener la versión hasta completar los diez casos. El registro independiente de T04 y los resúmenes generales siguen pendientes.
