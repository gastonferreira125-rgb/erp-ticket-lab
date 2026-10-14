# v5-reference-rule — preparada, sin ejecuciones

Deriva de v4-integration-rule. Solo añade la regla de extracción en added-rule.txt, incluida al final de system.txt. No cambia las categorías, prioridad, regla de instrucciones ni los seis campos/tipos.

Aclaración semántica: referencia_documento incluye el identificador del documento ERP o código de artículo afectado. Se mantiene el nombre para conservar compatibilidad con el laboratorio; un nombre más general podría estudiarse en otra versión. schema.json es una copia del esquema original con descripción añadida al campo; esa descripción no impone validación semántica por sí misma.

Resuelve dos oportunidades de diseño: omisiones de referencias de pedidos (T03-v3 y T12-v4) y ambigüedad del código de artículo T04. No implica resultados medidos. El conjunto original no se modifica para mejorar retroactivamente el puntaje.

Siguiente prueba: T12 con las mismas entradas y parámetros solicitados, cambiando Sistema v4 por v5. Comparar salida original; luego T03/T04 y regresiones de instrucciones e integración. T12 pasa a ser un caso usado para ajustar v5, por lo que su resultado no será evidencia independiente de generalización.
