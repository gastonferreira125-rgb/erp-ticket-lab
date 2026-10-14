# Proyecto y alcance

Autor: Gastón Ferreira. Proyecto de aprendizaje aplicado y portafolio.

## Problema
Los tickets ERP llegan con texto libre, detalles incompletos y distintos niveles de impacto. El proyecto explora cómo un LLM puede proponer categoría, prioridad, resumen y datos faltantes para facilitar la revisión humana.

## Primera versión
- Diez incidentes ficticios con etiquetas de referencia.
- Prompt inicial y contrato JSON.
- Evaluador local en Python sin dependencias externas.
- Práctica manual iniciada en SAP AI Launchpad y Generative AI Hub.

Estado al 14 de octubre de 2026: 34 ejecuciones sobre doce tickets distintos. Ronda v3 completa: 10/10 respuestas conformes en formato y 7/10 coincidencias completas de etiquetas; categorías 9/10, prioridades 10/10, referencias 8/10. T03/T04 omiten referencias, y T07 falla categoría. T04 expone una ambigüedad del contrato para códigos de artículo. T01/T02/T10 conservan etiquetas previamente correctas en estas ejecuciones. [Ronda y revisión humana](../experiments/2026-10-14-v3-round/README.md).

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

v5 congelada. v6 añade únicamente calidad de datos_faltantes. Primera salida T02: etiquetas conformes, lista vacía; objetivo de contenido no cumplido. Texto completo de Sistema aportado posteriormente coincide con v6 guardada; no confirma retrospectivamente payload o parámetros de la primera ejecución. No inferir incumplimiento general o error de copia.

## Próximas entregas
Repetir T02 una vez con el mismo texto Sistema v6 confirmado por el usuario y Usuario/configuración solicitada sin cambios; conservar la nueva ejecución por separado. Observar variación/consistencia sin inferir causalidad ni robustez general. Luego controles T04/T06/T10. Evaluar datos ausentes, concretos y útiles además de etiquetas. Casos nuevos/repeticiones, impacto en resumen en ajuste separado, comparación de modelos y demo pendientes.
