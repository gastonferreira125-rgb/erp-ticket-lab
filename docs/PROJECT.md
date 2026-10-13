# Proyecto y alcance

Autor: Gastón Ferreira. Proyecto de aprendizaje aplicado y portafolio.

## Problema
Los tickets ERP llegan con texto libre, detalles incompletos y distintos niveles de impacto. El proyecto explora cómo un LLM puede proponer categoría, prioridad, resumen y datos faltantes para facilitar la revisión humana.

## Primera versión
- Diez incidentes ficticios con etiquetas de referencia.
- Prompt inicial y contrato JSON.
- Evaluador local en Python sin dependencias externas.
- Práctica manual iniciada en SAP AI Launchpad y Generative AI Hub.

Estado al 13 de octubre de 2026: acceso al entorno confirmado y primera respuesta de modelo guardada (T01). El caso pasa las comprobaciones del evaluador y coincide con las etiquetas de referencia. Nueve casos siguen pendientes; la configuración actual posterior a T01 ya está documentada (temperatura 1; tokens de salida máximos 43690; streaming activado). No hay integración con ERP, medición de tiempos ni comparación de modelos.

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

## Próximas entregas
Ejecutar T02 con la misma configuración; los parámetros actuales ya se capturaron y Gastón identificó correctamente la regla de prioridad Alta. Después completar los diez casos, comparar versiones del prompt y construir una demo con resultados documentados.
