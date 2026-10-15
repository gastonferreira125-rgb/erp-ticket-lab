# Cierre de etapa 1 — prompts y evaluación de tickets ERP

Fecha: 15 de octubre de 2026. Estado: ejercicio educativo cerrado; v8 conservada como referencia. [Evidencia y comparación](../experiments/2026-10-15-v8-controls/README.md).

## Qué se completó
- Diez tickets originales y tres complementarios, sintéticos; 48 respuestas registradas entre versiones.
- Contrato JSON de seis claves y evaluación local sin llamadas al modelo.
- Prompts versionados v0–v8, separación de roles, reglas condicionales y demostraciones few-shot.
- Ejecución manual en SAP AI Launchpad, conservación de originales y registros de errores.
- Rondas completas v3/v5 y controles parciales v6/v7/v8, sin mezclar sus métricas.
- Guía de conceptos aplicada: prompt, roles, few-shot, skill, MCP, extracción, evaluación, regresión, generalización y trazabilidad.
- Respaldo XML v7/v8 con textos completos, validado por parseo y comparación exacta de mensajes.
- Distinción entre chequeos automáticos, análisis cualitativo asistido por IA y validación humana.

## Resultado del último experimento
v8 completó los cuatro controles acordados: T02/T04/T06/T10. Formato/etiquetas 4/4 entre ejecutados; cobertura 4/10 del conjunto original.

T02-v7 dejó datos_faltantes vacío dos veces. T02-v8 pide error exacto y pasos. T04 conserva cantidades/fecha; T06 solicita campos/filtros; T10 identifica instrucciones sin inventar corrección. Es mejora observada en un caso y conservación de controles, no garantía general.

No se abre v9 automáticamente. Se cierra el ciclo acordado para avanzar.

## Pendientes posteriores, sin bloquear este cierre educativo
1. Validación personal de los comentarios cualitativos: no inferir aceptación por pegar una salida o continuar el chat.
2. Ampliar cobertura v8, repeticiones y casos nuevos independientes de ajustes; incluir transacciones con error/pasos ya informados para comprobar que no se repitan.
3. Conservar todos los detalles críticos del impacto en resúmenes.
4. Capturar configuración/payload completo, valor exacto de tokens y resolver guardado nativo SAP.
5. Comparar modelos con protocolo común y medir costes/tiempos si la siguiente etapa lo requiere.
6. Diseñar una siguiente práctica de flujo/orquestación y, si corresponde, acceso a documentación o herramientas; antes de implementar, definir entrada, pasos, salida y qué decide una persona.

Skill y MCP fueron estudiados y documentados. No se creó una skill propia instalada ni un servidor MCP para el ERP. No hay conexión operativa a SAP ERP, RAG implementado ni correcciones ejecutadas en sistemas reales.

## Recuperación
- [Sistema v8](../prompts/v8-transaction-investigation/system.txt).
- [Seis mensajes v8](../prompts/v8-transaction-investigation/messages-t02.json).
- [XML v8](../prompts/v8-transaction-investigation/backup/ERP_Tickets_v8_FewShot.xml).
- [Guía de conceptos](CONCEPTS.md).
- [Cómo se evalúa y quién revisa](EVALUATION.md).

XML es formato propio legible para restauración manual, no un export SAP de importación directa verificada.
