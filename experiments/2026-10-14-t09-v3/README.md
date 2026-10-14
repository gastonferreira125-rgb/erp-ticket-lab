# T09 — v3 — 2026-10-14

## Entrada
```text
ENTRADA:
ticket_id: T09
<ticket>
Necesito documentar cómo recibir mercadería y capacitar a dos usuarios nuevos. Es una mejora planificada.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T09",
  "categoria": "Inventario",
  "prioridad": "Baja",
  "resumen": "Solicitud de documentación para recepción de mercadería y capacitación a usuarios.",
  "referencia_documento": null,
  "datos_faltantes": []
}
```

## Evaluación manual
Formato y tipos correctos. Coinciden ticket_id T09, categoría Inventario, prioridad Baja y referencia null con los valores esperados. La recepción de mercadería define el área funcional y el texto describe una mejora planificada, sin afirmar interrupción.

Resumen fiel: no afirma que la documentación o capacitación ya estén realizadas. Omite que son dos usuarios nuevos.
datos_faltantes vacío es válido en estructura y no afecta la comparación de etiquetas. Para preparar la documentación y capacitación, sería útil conocer el ERP/módulo y el procedimiento o alcance de recepción. La regla actual pide información para investigar y no define con precisión los requisitos para solicitudes planificadas; registrar esta oportunidad sin convertirla en fallo de etiquetas.

JSON confirmado visualmente en la captura; no se ejecutó el evaluador automático en este registro.

## Continuidad
v3-category-rule; reglas en Sistema y ticket en Usuario. Modelo y parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. La captura no confirma esos parámetros.

Siete casos ejecutados con v3: T05, T06, T08 y T09 coinciden completamente; T07 falla categoría; T03 y T04 fallan referencia respecto del conjunto actual. Resultado parcial: 4/7 coincidencias completas. T04 tiene una ambigüedad adicional en el campo referencia_documento, que el conjunto usa para un código de artículo.

Restan T01, T02 y T10 con v3 para evaluar los diez tickets bajo la misma versión. Mantener el prompt sin cambios hasta completar esa ronda. Guardado independiente de T04 y actualizaciones generales del repositorio pendientes.
