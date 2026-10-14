# v6-missing-data-rule — preparada, sin ejecuciones

Deriva de v5-reference-rule. added-rule.txt se añade al final de system.txt. La única regla modificada por esta versión es la calidad de datos_faltantes: información útil para el próximo paso de investigación/definición, sin pedir de nuevo datos ya aportados y con elementos concretos.

Conserva categorías, prioridad, extracción, resumen, seis claves y tipos; la condición específica para mensajes de instrucciones conserva precedencia. No añade ejemplos Asistente ni respuestas esperadas al prompt.

Motivo: la ronda v5 alcanzó 10/10 en etiquetas del conjunto original, pero varios campos de información faltante perdieron utilidad. T02/T03 tenían lista vacía, T04 pidió almacén ya informado, T08 pidió procedimiento sin precisar y omitió fechas. No hay resultados de v6 todavía.

Primera prueba: T02 con igual entrada y configuración solicitada. Revisión humana: ¿solicita información ausente y útil para investigar, como error exacto/pasos? ¿Evita inventar? Evaluar además las etiquetas del mismo conjunto. No imponer una lista textual idéntica a una respuesta esperada.

Luego controles T04 (usar almacén conocido y pedir detalle útil), T06 (requisitos para solicitud), T10 (conservar regla de instrucciones). Los casos usados para ajustar esta versión no constituyen pruebas independientes de generalización; añadir casos nuevos después. La precisión del impacto en resúmenes queda para otra versión.

[Ronda completa v5](../../experiments/2026-10-14-v5-round/README.md).
