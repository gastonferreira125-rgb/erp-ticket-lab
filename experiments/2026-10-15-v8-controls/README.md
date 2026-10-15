# Cierre de controles v8 y comparación con v7

Fecha: 15 de octubre de 2026. Etapa educativa de diseño/evaluación de prompts cerrada según el alcance acordado: un ajuste final v8, T02/T04/T06/T10 y conclusión. No se creó v9.

## Resultado medido
- Cuatro respuestas v8, cuatro tickets originales únicos.
- Formato y etiquetas: 4/4 entre ejecutados.
- Cobertura del conjunto original: 4/10; seis casos no ejecutados con v8, no seis fallos observados.
- Misma cohorte de cuatro casos en v7: formato/etiquetas 4/4. No hubo mejora en ese indicador; la diferencia observada está en contenido de T02.
- Total acumulado entre versiones: 48 respuestas sobre trece tickets distintos. No calcular una exactitud mezclando versiones.
- T11/T12/T13 complementarios permanecen fuera de estas métricas.

## Qué se compara
v8 añade una regla para solicitar error/comportamiento y pasos ausentes cuando falla una transacción. Conserva Sistema previo y los dos pares EX01/EX02. Se compara con la última respuesta cronológica v7 por ticket; T02-v7 tuvo dos listas vacías y ambas se conservan en sus carpetas. No se elige la mejor respuesta.

[responses.json](responses.json): originales v8. [evaluation.json](evaluation.json): evaluate.py sobre los diez casos originales. [cases-comparison.json](cases-comparison.json): solo los cuatro casos comunes. [comparison.json](comparison.json): evaluaciones automáticas de la misma cohorte en ambas versiones, con cuatro casos como denominador. [responses-v7-comparison.json](responses-v7-comparison.json): snapshot usado de v7.

## Análisis cualitativo asistido por IA
Estas observaciones requieren validación humana; no se presentan como una puntuación humana agregada ni aprobación del usuario.

| Caso | v7 observado | v8 observado | Interpretación limitada |
| --- | --- | --- | --- |
| T02 | [] en dos ejecuciones | Pide error exacto y pasos | Mejora observada del objetivo específico |
| T04 | Cantidades del sistema/conteo y fecha | Conserva esas preguntas, sin repetir almacén | Control conserva comportamiento pertinente |
| T06 | Campos y formato | Campos y filtros | Ambas listas útiles para iniciar requisitos |
| T10 | Otros/Media/null; pide incidente | Conserva criterio y petición | Control conserva tratamiento de instrucciones |

T02-v8 incluye cierre detenido, pero no explicita todo el bloqueo del equipo. Fidelidad completa del impacto en resúmenes queda como mejora futura. T06 requiere posterior relevamiento para una especificación completa.

## Conclusión
Se observó mejora de información solicitada en T02 y no se observó deterioro de etiquetas o de pertinencia básica en estos tres controles adicionales. Esto permite cerrar el ejercicio educativo y conservar v8 como versión de referencia para la siguiente práctica.

Una ejecución por caso v8, casos conocidos usados para ajuste, T04 cercano a EX02 y parámetros/payloads parcialmente verificados impiden concluir causalidad, robustez general o aptitud para producción.

## Trazabilidad y límites
Modelo indicado Gemini 2.5 Flash Lite (001). Capturas posteriores de v7 confirmaron seis bloques/orden/ids, temperatura 1 y streaming activado. Textos íntegros/payload de v8 no capturados; máximo de tokens seleccionado exacto sin verificar (43690 solicitado; 65536 extremo del control). No convertir estas comprobaciones en confirmación retrospectiva de todos los payloads.

Fuente de v8: JSON pegado. Respuestas originales conservadas. Análisis del tutor es asistido por IA, salvo validación humana explícita. No hay integración operativa al ERP ni medición de tiempos/ahorros.

## Respaldo y siguientes tareas
[XML v8](../../prompts/v8-transaction-investigation/backup/ERP_Tickets_v8_FewShot.xml): seis mensajes previstos completos, default último Usuario T02. Formato propio, importación directa a SAP no verificada. El último caso ejecutado fue T10; el backup usa T02 como plantilla reutilizable.

[Cierre de etapa y pendientes](../../docs/STAGE_1_CLOSURE.md). No quedan pruebas adicionales exigidas para este cierre acordado. Validación humana y ampliación de evaluación siguen como trabajo posterior; el cierre no las da por realizadas.
