# T07 — v5 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T07
<ticket>
La integración de pedidos con la tienda está caída. Ningún pedido entra y todo el equipo de ventas está detenido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T07",
  "categoria": "Integraciones",
  "prioridad": "Alta",
  "resumen": "La integración de pedidos con la tienda está caída, impidiendo el ingreso de pedidos.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Detalles sobre la tienda con la que se integra",
    "Mensajes de error específicos de la integración",
    "Fecha y hora aproximada del inicio de la falla"
  ]
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T07 presente, formato y etiquetas conformes; Integraciones, Alta y null. Sin referencias ausentes literalmente, duplicados ni IDs desconocidos. Otros nueve casos de evaluation.json no ejecutados en este archivo.

Fuente de esta ejecución: JSON pegado por el usuario; no se recibió captura en este mensaje. No afirmar confirmación visual de salida, configuración o prompt.

Resumen fiel a caída y falta de ingreso de pedidos, sin causa o solución inventada. Omite la detención explícita de todo el equipo. Datos faltantes pertinentes: plataforma de tienda, error y momento de inicio.

## Regresión y continuidad
Conserva etiquetas conformes de T07-v4 después de añadir la aclaración de extracción de v5. Una respuesta conforme no demuestra ausencia de regresiones en otros casos ni consistencia entre repeticiones.

v5 tiene cuatro casos conformes del conjunto original, T03/T04/T07/T10 (4/4 entre ejecutados, cobertura 4/10), y un caso complementario conforme, T12 (1/1). v3 mantiene 7/10 de su ronda completa. No mezclar versiones/conjuntos.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración según continuidad solicitada: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Parámetros actuales y guardado SAP no confirmados.

Mantener v5 sin cambios y ejecutar T01, T02, T05, T06, T08 y T09 para completar el conjunto original. Después consolidar la ronda completa, y considerar en otra versión las mejoras de información faltante y precisión de resúmenes.
