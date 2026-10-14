# T02 — v3 — 2026-10-14

## Entrada
```text
ENTRADA:
ticket_id: T02
<ticket>
La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T02",
  "categoria": "Finanzas",
  "prioridad": "Alta",
  "resumen": "La factura FV-1042 no se contabiliza, afectando al equipo de Finanzas y al proceso de cierre.",
  "referencia_documento": "FV-1042",
  "datos_faltantes": [
    "Detalles del error al intentar contabilizar la factura.",
    "Fecha y hora del incidente.",
    "Nombre de usuario que intentó la contabilización."
  ]
}
```

## Evaluación manual
Los seis campos y sus tipos son correctos. Coinciden T02, Finanzas, Alta y FV-1042 con los valores esperados. Alta está sustentada por el bloqueo explícito de todo el equipo y la detención del cierre.

El resumen no inventa causa ni solución ejecutada, pero sustituye bloqueo y detención por "afectando", perdiendo precisión sobre el impacto. Oportunidad de mejora humana, independiente del acierto de etiquetas. Los detalles del error son útiles; fecha/hora y usuario pueden ayudar a reproducir o localizar evidencia.

Prueba de regresión: T02 ya coincidía en etiquetas con v0 y v2, y conserva ese resultado en esta ejecución de v3. No demuestra consistencia en repeticiones ni ausencia de regresiones en otros casos. No atribuir cambios de resumen o datos faltantes exclusivamente al prompt.

Captura revisada y coincidente con el JSON pegado. No se ejecutó el evaluador automático en este registro.

## Continuidad
v3-category-rule; reglas en Sistema y ticket en Usuario. Modelo y parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. La captura no confirma esos parámetros.

Nueve tickets ejecutados con v3: seis coincidencias completas (T01, T02, T05, T06, T08, T09). T07 falla categoría; T03 y T04 fallan referencia respecto del conjunto actual. Resultado parcial: 6/9. T04 tiene además una ambigüedad de diseño del campo referencia_documento para un código de artículo.

Resta T10 con v3. Mantener la versión hasta terminar los diez casos y luego revisar categorías, extracción y coherencia de esquema y conjunto esperado. Guardado independiente de T04 y resúmenes generales pendientes.
