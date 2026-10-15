# Proyecto y alcance

Autor: Gastón Ferreira. Aprendizaje aplicado y portafolio.

## Problema y resultado de la etapa
Los tickets ERP llegan con texto libre, detalles incompletos y distinto impacto. Se explora un modelo que propone categoría, prioridad, resumen, referencia y datos faltantes para revisión posterior.

Al 15 de octubre de 2026, la etapa de prompts y evaluación queda cerrada con v8. Se registraron 48 respuestas entre versiones sobre trece tickets distintos. Rondas completas: v3 coincide en todas las etiquetas para 7/10, v5 para 10/10; ambas cumplen formato 10/10. Controles finales v8: formato/etiquetas 4/4 entre ejecutados, cobertura 4/10. Casos complementarios y versiones no se mezclan para presentar exactitud general.

En T02, v7 dejó listas vacías dos veces y v8 pide error/pasos. T04/T06/T10 conservan comportamiento pertinente. Análisis de contenido asistido por IA, pendiente de validación personal salvo intervención explícita. [Cierre, evidencia y límites](../experiments/2026-10-15-v8-controls/README.md).

## Flujo realizado
1. Definir tickets sintéticos y etiquetas de referencia antes de observar su salida.
2. Versionar reglas, roles y luego ejemplos.
3. Ejecutar manualmente en SAP AI Launchpad.
4. Conservar originales sin corregir.
5. Evaluar campos/tipos y etiquetas mediante evaluate.py.
6. Analizar contenido y registrar límites de evidencia, diferenciando al tutor IA de una persona.
7. Hacer controles de regresión y casos nuevos; cerrar el último ciclo según alcance acordado.

La regla Alta/Baja/Media es una política de este laboratorio, no un estándar corporativo universal. Etiquetas de evaluación no se envían con el ticket real al modelo.

## Entregables
[Guía de conceptos](CONCEPTS.md), [roles](MESSAGE_ROLES.md), [evaluación](EVALUATION.md), [registro de aprendizaje](LEARNING_LOG.md), prompts v0–v8 y resultados por experimento. [XML v8](../prompts/v8-transaction-investigation/backup/ERP_Tickets_v8_FewShot.xml) conserva seis mensajes previstos para recuperación manual; no es export SAP nativo.

## Alcance técnico verificado
Modelo indicado Gemini 2.5 Flash Lite (001). Capturas posteriores de v7 confirmaron seis bloques/roles/ids, temperatura 1 y streaming activado. Máximo de tokens seleccionado y todos los payloads efectivos no verificados. Guardado nativo SAP informado como fallido.

No hay conexión operativa al ERP, cambios en datos reales, medición de ahorros, comparación de modelos ni RAG implementado. La skill propia y el MCP ERP son ejemplos conceptuales, no implementaciones.

## Próxima etapa
[Pendientes y transición](STAGE_1_CLOSURE.md): validación humana, evaluación ampliada, precisión del impacto, trazabilidad de parámetros y siguiente práctica de flujo/orquestación. No se crea v9 automáticamente; el cierre educativo no da por terminada una validación para producción.
