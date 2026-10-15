# T02 — primera ejecución v8 — 15 de octubre de 2026

## Entrada y cambio indicado
T02 original: “La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.”

Se indicó añadir solo la regla de transacciones fallidas al Sistema v7, conservando EX01/EX02 y último Usuario T02. [v8 y plan previo](../../prompts/v8-transaction-investigation/README.md).

Modelo Gemini 2.5 Flash Lite (001); temperatura 1 y streaming activado visibles en captura previa de la configuración actual. Máximo de tokens seleccionado exacto no verificado. Fuente de resultado: JSON pegado sin captura de esta ejecución ni payload completo de v8.

## Original y evaluación
[Texto exacto](raw-response.txt), [respuesta en lista](responses.json), [evaluación ejecutada](evaluation.json). Original sin corregir.

evaluate.py: T02 presente, formato y Finanzas/Alta/FV-1042 conformes; sin ids desconocidos/duplicados ni referencias ausentes literalmente.

## Análisis cualitativo asistido por IA
Objetivo previo cumplido en esta salida: solicita mensaje de error exacto y pasos de contabilización, ambos ausentes en la entrada. No inventa causa ni solución. Resumen conserva factura fallida y cierre detenido; no explicita “todo el equipo bloqueado”. Comentarios pendientes de validación humana, ver [quién revisa](../../docs/EVALUATION.md#quién-revisa-tres-niveles-distintos).

| Campo | T02-v7, dos ejecuciones | T02-v8 |
| --- | --- | --- |
| Etiquetas | Conformes | Conformes |
| datos_faltantes | [] en ambas | Error exacto y pasos |
| Resumen | Primera incluye cierre; segunda lo omite | Incluye cierre detenido |

Mejora observada de datos_faltantes para este caso. Una ejecución de un caso usado para ajuste no prueba robustez o causalidad general. Los mensajes efectivos completos de v8 no se verificaron por payload.

## Plan de cierre
1 de 4 controles previstos recibido. Próximos T04, T06 y T10, sin cambiar reglas/ejemplos/parámetros. Después comparación y cierre, sin v9 automática.

v8: una respuesta de un ticket original, formato/etiquetas 1/1 entre ejecutados, cobertura 1/10. Total entre versiones: 45 respuestas sobre trece tickets distintos.
