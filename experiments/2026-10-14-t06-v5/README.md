# T06 — v5 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T06
<ticket>
Quiero crear un reporte mensual de ventas por cliente. No hay interrupción del negocio.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T06",
  "categoria": "Reportes",
  "prioridad": "Baja",
  "resumen": "Solicitud para crear un reporte mensual de ventas por cliente.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Especificación del reporte deseado (campos, filtros, ordenamiento)",
    "Formato de entrega del reporte"
  ]
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T06 presente, formato y etiquetas conformes (Reportes, Baja, null). Sin referencias ausentes literalmente ni IDs duplicados/desconocidos. Otros nueve tickets no se ejecutaron en este archivo.

Fuente: JSON pegado por el usuario, sin captura en este mensaje. Resumen fiel como solicitud pendiente, sin afirmar implementación realizada. Reconoce creación de reporte sin interrupción del negocio. Datos faltantes pertinentes para definir requisitos: campos, filtros, ordenamiento y formato. No son un diagnóstico.

## Regresión y continuidad
Conserva las etiquetas de T06-v3 en esta ejecución de v5. El recurso reporte se clasifica aquí como Reportes por solicitud de creación, a diferencia de T05 donde el problema es de permisos. Una sola respuesta por versión no demuestra consistencia ni ausencia de regresiones en otras entradas.

v5: ocho casos conformes del conjunto original T01/T02/T03/T04/T05/T06/T07/T10 (8/8 entre ejecutados, cobertura 8/10), y T12 complementario conforme (1/1). No mezclar versiones/conjuntos.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración solicitados: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Respuesta textual no confirma parámetros actuales, prompt completo enviado ni guardado SAP.

Restan T08/T09 con v5 sin cambios. Después consolidar diez respuestas y revisión humana. Mejoras de información faltante y precisión del impacto en otros casos siguen pendientes.
