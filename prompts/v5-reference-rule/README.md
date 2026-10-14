# v5-reference-rule — ronda original completa

Deriva de v4-integration-rule. Añade solo la regla de extracción de added-rule.txt, incluida al final de system.txt. Conserva categorías, prioridad, regla de instrucciones y seis claves/tipos.

referencia_documento incluye identificador del documento ERP o código de artículo afectado. El nombre se conserva para compatibilidad con el laboratorio; schema.json copia el esquema original con descripción añadida, que no valida semántica por sí misma. Conjunto original y respuestas históricas sin modificar.

[Ronda completa](../../experiments/2026-10-14-v5-round/README.md): diez respuestas originales, 10/10 en formato y etiquetas. v3 había dado 7/10 en etiquetas del mismo conjunto. Caso complementario T12 conforme (1/1), evaluado aparte. Los casos que motivaron ajustes no demuestran generalización independiente.

La revisión humana conserva hallazgos: pérdida de impacto en resumen T02, listas vacías T02/T03, solicitud redundante de almacén T04 y datos poco concretos T08. El acierto de etiquetas no equivale a calidad uniforme de todos los campos.

v5 queda congelada. [v6](../v6-missing-data-rule/README.md) busca mejorar únicamente datos_faltantes. Primera salida T02 conserva etiquetas y lista vacía; aplicación del bloque en SAP pendiente de verificar. Precisión del impacto en resumen queda para otro ajuste.
