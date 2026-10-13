# Segunda ejecución: T02 — revisión preliminar

Fecha: 13 de octubre de 2026 (America/Montevideo).

## Entrada indicada
ticket_id: T02

La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.

Se indicó mantener v0-baseline y cambiar únicamente id y texto. Modelo y parámetros de referencia: Gemini 2.5 Flash Lite (001), temperatura 1, tokens de salida máximos 43690 y streaming activado, según la configuración documentada después de T01. La captura de T02 muestra únicamente la respuesta, no confirma de nuevo el prompt ni los parámetros.

## Evidencia
![Respuesta de T02: el resumen queda cortado en el borde derecho](response-capture.png)

La salida completa copiada desde SAP está pendiente. No se reconstruye el final del resumen ni se agrega una respuesta parcial a responses.json.

## Revisión de los campos legibles
| Campo | Valor visible | Evaluación manual |
| --- | --- | --- |
| ticket_id | T02 | Coincide con el caso. |
| categoria | Finanzas | Coherente con el incidente. |
| prioridad | Alta | Todo el equipo está bloqueado y el cierre detenido. |
| referencia_documento | FV-1042 | Copia la referencia explícita. |
| datos_faltantes | [] | Observación de calidad: todavía faltan datos para investigar. |

El resumen visible describe la factura que no se contabiliza y el bloqueo del cierre/equipo. Su final está cortado en la captura; no se afirma una validación de la salida completa.

## Hallazgo funcional
El modelo propone correctamente las etiquetas legibles, pero no solicita información adicional. El incidente identifica el documento y el impacto; no proporciona el error exacto, los pasos para reproducir ni las verificaciones ya realizadas. Un array vacío está permitido por schema.json, pero eso no demuestra que el contenido sea suficiente para soporte.

Posible mejora para una futura versión del prompt: pedir datos concretos para investigar cuando no estén en el ticket, aunque categoría, prioridad y referencia estén claras. Se conserva v0 para continuar el experimento; aún no se modifica.

## Estado y próximo paso
- Dos ejecuciones manuales observadas (T01 y T02).
- T01 tiene salida original completa y evaluación automática.
- T02 queda pendiente de salida original completa y evaluación automática.
- Copiar la respuesta completa con el icono del panel Respuesta y pegarla al chat.
