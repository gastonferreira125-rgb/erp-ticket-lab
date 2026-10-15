# Proyecto y alcance

Autor: Gastón Ferreira. Proyecto de aprendizaje aplicado y portafolio.

## Problema
Los tickets ERP llegan con texto libre, detalles incompletos y distintos niveles de impacto. El proyecto explora cómo un LLM puede proponer categoría, prioridad, resumen y datos faltantes para facilitar la revisión humana.

## Primera versión
- Diez incidentes ficticios con etiquetas de referencia.
- Prompt inicial y contrato JSON.
- Evaluador local en Python sin dependencias externas.
- Práctica manual iniciada en SAP AI Launchpad y Generative AI Hub.

Estado al 15 de octubre de 2026: 42 ejecuciones sobre doce tickets distintos. Ronda v3 completa: 10/10 respuestas conformes en formato y 7/10 coincidencias completas de etiquetas; categorías 9/10, prioridades 10/10, referencias 8/10. T03/T04 omiten referencias, y T07 falla categoría. T04 expone una ambigüedad del contrato para códigos de artículo. T01/T02/T10 conservan etiquetas previamente correctas en estas ejecuciones. [Ronda y revisión humana](../experiments/2026-10-14-v3-round/README.md).

No hay integración operativa con ERP, medición de tiempos ni comparación de modelos. Faltan repeticiones y casos nuevos independientes del ajuste; valores actuales y guardado en SAP pendientes de confirmar.

## Flujo experimental
1. Seleccionar un ticket y copiar únicamente su id y texto al modelo.
2. Ejecutar el prompt y conservar la salida original.
3. Registrar modelo, versión, parámetros, fecha y versión del prompt.
4. Evaluar formato y etiquetas; revisar contenido manualmente.
5. Documentar errores y ajustar el prompt en una versión nueva.

Las etiquetas esperadas se usan después de generar la respuesta, nunca como entrada al modelo. El conjunto pequeño sirve como prueba educativa, no permite demostrar calidad general en producción.

## Criterios de aceptación
- Salida con los campos y tipos definidos.
- Clasificación coherente con las reglas publicadas.
- Resumen sin causas o soluciones inventadas.
- Identificadores copiados del ticket.
- Información faltante útil para investigar.
- Revisión humana previa a cualquier uso operativo.

## Avance v4
T07/T08/T10 conformes del conjunto original (3/3 entre ejecutados, cobertura 3/10). Complementarios T11/T12: 1/2 coincidencias completas. T12 conserva Ventas y Media pero omite OV-3301 en referencia_documento. El contraste de categoría pasa; la extracción falla. [Resultado T12](../experiments/2026-10-14-t12-v4/README.md).

v5 completó los diez tickets del conjunto original: 10/10 en formato y todas las etiquetas. v3: 7/10 en etiquetas del mismo conjunto. T12 complementario conforme (1/1), aparte. La aclaración de códigos de artículo resolvió una ambigüedad del contrato; no atribuir toda diferencia únicamente a capacidad del modelo. Revisión humana mantiene pérdidas de impacto y utilidad de datos faltantes. [Comparación y límites](../experiments/2026-10-14-v5-round/README.md).

v5 congelada. v6 añade únicamente calidad de datos_faltantes. Cinco ejecuciones sobre cuatro tickets (T02 dos veces, T04, T06 y T10): etiquetas conformes, cobertura única 4/10. T02/T04 tienen listas vacías pese a faltar información útil; T06 pide campos/filtros pertinentes para el reporte. No demostrar mejora global del campo frente a v5. Texto completo de Sistema aportado posteriormente coincide con v6 guardada; no confirma retrospectivamente payload o parámetros de la primera ejecución. No inferir incumplimiento general o error de copia.

## Próximas entregas
v7 cierra controles dirigidos con cuatro respuestas T02/T04/T06/T10: formato/etiquetas 4/4 entre ejecutados, cobertura 4/10. T02 mantiene lista vacía, T04 solicita cantidades/fecha, T06/T10 conservan comportamiento pertinente. No demuestra mejora uniforme ni generalización amplia; payload/parámetros no totalmente verificados. [Controles v7](../experiments/2026-10-15-v7-controls/README.md).

Diseño v7 con System v6 idéntico y dos pares de ejemplos Usuario/Asistente EX01/EX02, externos al benchmark. Continuar T13 complementario, preparado con expectativas previas y sin resultado, como último Usuario con ejemplos fijos. [Plan T13](../tickets/generalization-v7-t13.md). Conservar respuestas y comprobar id, formato, etiquetas e información faltante útil. Demostraciones diseñadas no son ejecuciones medidas ni fine-tuning. Casos nuevos/repeticiones, precisión del impacto en resumen, comparación de modelos y demo pendientes. [v6 consolidada](../experiments/2026-10-14-v6-controls/README.md), [diseño v7](../prompts/v7-few-shot/README.md).
