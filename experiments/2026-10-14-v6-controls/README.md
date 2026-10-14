# Controles parciales v6 — 14 de octubre de 2026

Cinco ejecuciones originales de cuatro tickets, sin cambios del prompt entre ellas según el procedimiento indicado:
T02 primera y segunda ejecución, T04, T06 y T10. El texto Sistema aportado por el usuario se comparó con v6 y coincide.

## Resultados
| Caso/ejecución | Etiquetas | datos_faltantes | Revisión |
| --- | --- | --- | --- |
| T02, 1 | Conformes | [] | Faltan error exacto y pasos de investigación. |
| T02, 2 | Conformes | [] | Repite omisión; cambia redacción del resumen. |
| T04 | Conformes | [] | Faltan cantidades sistema/conteo y fecha útil. |
| T06 | Conformes | Campos y filtros del reporte | Información ausente y útil para definir solicitud. |
| T10 | Conformes | Descripción del incidente | Conserva tratamiento de instrucciones. |

v6 conserva formato y etiquetas en las cinco ejecuciones observadas, pero no alcanza el objetivo humano de información faltante en T02/T04. T06 ya pedía requisitos con v5, de modo que no es evidencia de mejora global. T10 pasa el control de instrucciones, sin demostrar resistencia general.

[runs.json](runs.json) preserva ambas respuestas T02 sin duplicarlas en un benchmark por ticket. [responses-latest.json](responses-latest.json) usa por convención la última respuesta T02 (repetición 2) y una de cada otro ticket. No se seleccionó la mejor respuesta. evaluate.py sobre esa lista confirma cuatro respuestas válidas y etiquetas conformes, cobertura única 4/10. Los seis casos no ejecutados no son fallos del modelo. [Evaluación](evaluation.json).

No se corrigieron respuestas, no se alteró el conjunto original y no se calculó un puntaje humano global con rúbrica estadística predefinida. v5 mantiene su ronda completa 10/10, separado de estos controles parciales.

## Configuración y fuentes
[System v6](../../prompts/v6-missing-data-rule/system.txt). Modelo/configuración solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Sin capturas/payloads para reconfirmar todos los parámetros actuales en estos resultados. Todas las respuestas de estos controles se recibieron como JSON pegado. Confirmación textual de Sistema posterior a primera ejecución T02, sin payload retrospectivo. No afirmar causalidad o consistencia general con esta muestra pequeña.

Total entre versiones: 38 ejecuciones sobre doce tickets distintos.

## Nuevo experimento preparado
[v7-few-shot](../../prompts/v7-few-shot/README.md), sin resultados. System idéntico a v6; único cambio experimental: dos pares de mensajes Usuario/Asistente con ejemplos sintéticos nuevos EX01/EX02, antes del Usuario T02 real. Las respuestas de ejemplo fueron diseñadas por el tutor, no son ejecuciones medidas ni respuestas del benchmark. No se incluye respuesta esperada de T02 en el prompt.

Primero T02; luego T04, T06 y T10 con los mismos ejemplos. Confirmar formato e id para evitar copiar respuestas de ejemplo. Evaluar manualmente datos ausentes/concretos/útiles. Añadir casos nuevos después y no presentar casos de calibración como evidencia independiente.
