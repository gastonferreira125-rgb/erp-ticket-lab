# Proyecto y alcance

Autor: Gastón Ferreira. Proyecto de aprendizaje aplicado y portafolio.

## Problema
Los tickets ERP llegan con texto libre, detalles incompletos y distintos niveles de impacto. El proyecto explora cómo un LLM puede proponer categoría, prioridad, resumen y datos faltantes para facilitar la revisión humana.

## Primera versión
- Diez incidentes ficticios con etiquetas de referencia.
- Prompt inicial y contrato JSON.
- Evaluador local en Python sin dependencias externas.
- Práctica manual iniciada en SAP AI Launchpad y Generative AI Hub.

Estado al 14 de octubre de 2026: 20 ejecuciones sobre diez tickets distintos. Ronda v3 completa: 10/10 respuestas conformes en formato y 7/10 coincidencias completas de etiquetas; categorías 9/10, prioridades 10/10, referencias 8/10. T03/T04 omiten referencias, y T07 falla categoría. T04 expone una ambigüedad del contrato para códigos de artículo. T01/T02/T10 conservan etiquetas previamente correctas en estas ejecuciones. [Ronda y revisión humana](../experiments/2026-10-14-v3-round/README.md).

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
T07, T08 y T10 coinciden con etiquetas esperadas (3/3 entre ejecutados, cobertura 3/10). T08 conserva la clasificación de Compras; T10 conserva el manejo conforme de instrucciones dentro del ticket en estas ejecuciones. Oportunidades humanas: precisión del impacto de T07 y fechas de T08. No mezclar con v3. Caso complementario T11 preparado, sin respuesta, con valores esperados definidos antes de ejecutar.

## Próximas entregas
v4 ya aclara Integraciones como problema principal de intercambio entre sistemas y T07 devuelve la categoría esperada. T08 y T10 ya conservan sus etiquetas en estos controles; ejecutar T11 como caso nuevo sin modificar v4. Hacer una mejora por versión para facilitar la comparación. Luego revisar el alcance de referencia_documento, alineando prompt, esquema y conjunto esperado sin alterar retroactivamente v3. Repetir casos, añadir entradas nuevas y comparar modelos antes de preparar la demo y publicaciones.
