# T03 — v3 — 2026-10-14

## Entrada
```text
ENTRADA:
ticket_id: T03
<ticket>
El pedido OV-2099 tiene una dirección incorrecta. Solo me ocurre con este pedido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T03",
  "categoria": "Ventas",
  "prioridad": "Media",
  "resumen": "El pedido OV-2099 tiene una dirección incorrecta.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Dirección correcta para el pedido OV-2099"
  ]
}
```

## Evaluación
| Campo | Esperado | Observado | Resultado |
| --- | --- | --- | --- |
| ticket_id | T03 | T03 | Correcto |
| categoria | Ventas | Ventas | Correcto |
| prioridad | Media | Media | Correcto |
| referencia_documento | OV-2099 | null | Incorrecto |

La respuesta respeta los seis campos y sus tipos. Falla la extracción de la referencia: OV-2099 aparece literalmente como el pedido afectado. El resumen es fiel y no inventa una solución; omite que el problema afecta solo a ese pedido. La dirección correcta es un dato útil para investigar o corregir el pedido.

Evaluación manual del JSON pegado por el usuario y confirmado visualmente en la captura. No se ejecutó el evaluador automático para este registro. La respuesta original se conserva sin corregir.

## Configuración y continuidad
Versión en uso según continuidad del laboratorio: v3-category-rule; reglas en Sistema y ticket en Usuario. Modelo solicitado: Gemini 2.5 Flash Lite (001). Temperatura solicitada: 1. Máximo de salida solicitado: 43690. Streaming solicitado: activado. La captura de la respuesta no confirma esos parámetros.

v3 lleva cuatro casos ejecutados: T05 y T06 coinciden en las etiquetas esperadas; T07 falla categoría; T03 falla referencia. Resultado parcial: 2/4 coincidencias completas. No equivale a una evaluación de los diez tickets ni a una garantía de generalización.

Mantener v3 sin cambios para terminar T04, T08 y T09. Luego ejecutar T01, T02 y T10 con v3 para completar los diez casos. Los resúmenes generales del repositorio siguen pendientes de actualización.

El usuario autorizó explícitamente guardar los tickets del laboratorio y sus evaluaciones en este repositorio.
