# T08 — v3 — 2026-10-14

## Entrada
```text
ENTRADA:
ticket_id: T08
<ticket>
El pedido de compra PC-778 tiene una fecha de entrega equivocada. Necesito revisar el procedimiento.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T08",
  "categoria": "Compras",
  "prioridad": "Media",
  "resumen": "El pedido de compra PC-778 tiene una fecha de entrega equivocada.",
  "referencia_documento": "PC-778",
  "datos_faltantes": [
    "Fecha de entrega actual",
    "Fecha de entrega esperada",
    "Módulo o pantalla donde se visualiza el pedido de compra"
  ]
}
```

## Evaluación manual
Los seis campos y sus tipos son correctos. Coinciden ticket_id T08, categoría Compras, prioridad Media y referencia PC-778 con los valores esperados del conjunto. No se afirma interrupción de todo un equipo ni una mejora planificada sin incidente.

El resumen describe el problema sin inventar causa ni corrección ejecutada. Omite la solicitud de revisar el procedimiento. Fecha actual y esperada son datos útiles; la pantalla ayuda a ubicar dónde se observa la diferencia.

El JSON pegado coincide con la captura revisada. No se ejecutó el evaluador automático para este registro.

## Continuidad
Versión v3-category-rule. Reglas en Sistema y ticket en Usuario según continuidad del laboratorio. Modelo y parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. No confirmados por esta captura.

Seis casos ejecutados con v3: T05, T06 y T08 coinciden completamente; T07 falla categoría; T03 y T04 fallan referencia respecto del conjunto actual. Resultado parcial: 3/6 coincidencias completas. T04 tiene además una ambigüedad de diseño: el campo referencia_documento se usa en el conjunto para un código de artículo.

T08 demuestra que en esta ejecución sí se extrajo una referencia de pedido. No prueba que T03 esté corregido ni permite determinar la causa de su omisión.

Siguiente: T09 sin modificar v3. Después ejecutar T01, T02 y T10 con v3 para completar los diez casos. El guardado independiente de T04 y los resúmenes generales siguen pendientes tras los vencimientos de revisión automática.
