# Proyecto y alcance

Autor: Gastón Ferreira. Proyecto de aprendizaje aplicado y portafolio.

## Problema
Los tickets ERP llegan con texto libre, detalles incompletos y distintos niveles de impacto. El proyecto explora cómo un LLM puede proponer categoría, prioridad, resumen y datos faltantes para facilitar la revisión humana.

## Primera versión
- Diez incidentes ficticios con etiquetas de referencia.
- Prompt inicial y contrato JSON.
- Evaluador local en Python sin dependencias externas.
- Práctica manual iniciada en SAP AI Launchpad y Generative AI Hub.

Estado al 14 de octubre de 2026: siete ejecuciones guardadas, cuatro tickets distintos y resultados por versión separados. T10-v2 cumple la regla explícita y T02-v2 pasa la revisión de regresión. T05-v2 falla categoría, aunque formato, prioridad y resumen son conformes. v3 está preparada con criterio Autorizaciones frente a Reportes. No hay integración operativa con ERP, medición de tiempos ni comparación de modelos. Faltan seis tickets del conjunto, repeticiones y casos nuevos; valores actuales y guardado en SAP pendientes de confirmar.

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
Repetir T05 con v3 y luego T06 como regresión. Mantener modelo, parámetros y las demás reglas; conservar salidas originales separadas por versión. Luego completar casos restantes, repetir pruebas, incluir casos nuevos y comparar modelos antes de preparar la demo y las publicaciones.
