# T05 — v5 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T05
<ticket>
Mi usuario no tiene permiso para ver el reporte de compras. Otros usuarios sí pueden verlo.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T05",
  "categoria": "Autorizaciones",
  "prioridad": "Media",
  "resumen": "Usuario no tiene permiso para ver el reporte de compras.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Usuario afectado",
    "Nombre del reporte específico"
  ]
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T05 presente, formato y etiquetas conformes; Autorizaciones, Media y null. Sin referencias ausentes literalmente ni IDs duplicados/desconocidos. Los otros nueve tickets no se ejecutaron en este archivo.

Fuente: JSON pegado, sin captura en este mensaje. Resumen fiel al problema de permisos, sin causa técnica o corrección inventada. Usuario afectado y nombre exacto del reporte son datos útiles, no dados específicamente en la entrada. No hay afirmación de bloqueo de todo un equipo.

## Regresión y continuidad
Conserva categoría conforme de T05-v3 después de las reglas de integración y extracción posteriores. Caso antes usado para ajustar la categoría en v3, no prueba independiente de generalización.

v5: siete casos conformes del conjunto original T01/T02/T03/T04/T05/T07/T10 (7/7 entre ejecutados, cobertura 7/10), y T12 complementario conforme (1/1). Mantener métricas separadas; comparación completa con v3 todavía pendiente.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración solicitados: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Respuesta textual no confirma parámetros, prompt completo ni guardado SAP.

Restan T06/T08/T09 sin modificar v5. Siguiente T06 para contrastar solicitud de reporte planificada frente a problema de permisos.
