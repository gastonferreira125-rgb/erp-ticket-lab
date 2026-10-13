# Proyecto y alcance

Autor: Gastón Ferreira. Proyecto de aprendizaje aplicado y portafolio.

## Problema
Los tickets ERP llegan con texto libre, detalles incompletos y distintos niveles de impacto. El proyecto explora cómo un LLM puede proponer categoría, prioridad, resumen y datos faltantes para facilitar la revisión humana.

## Primera versión
- Diez incidentes ficticios con etiquetas de referencia.
- Prompt inicial y contrato JSON.
- Evaluador local en Python sin dependencias externas.
- Práctica manual iniciada en SAP AI Launchpad y Generative AI Hub.

Estado al 13 de octubre de 2026: acceso al entorno confirmado, T01, T02 y T10 guardados y evaluados. Tres salidas cumplen los controles de formato y dos coinciden con las etiquetas. T02 no pide datos faltantes; T10 falla en prioridad y presenta una corrección no confirmada como hecho reportado. Una cuarta ejecución total corresponde a T10 con v1: falla prioridad y referencia, y mantiene el problema del resumen. Son tres tickets distintos observados; siete casos aún no se ejecutaron; la configuración actual posterior a T01 ya está documentada (temperatura 1; tokens de salida máximos 43690; streaming activado). No hay integración con ERP, medición de tiempos ni comparación de modelos.

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
Ejecutar T10 con v2-instruction-guard preparada, confirmando valores numéricos y conservando las demás condiciones. v1 ya tiene un resultado separado que no mostró mejora; una única ejecución no permite atribuir causalidad a los roles. Después probar una mejora específica para los datos faltantes. Los parámetros actuales ya se capturaron y Gastón identificó correctamente la regla de prioridad Alta. Después completar los diez casos, comparar versiones del prompt y construir una demo con resultados documentados.
