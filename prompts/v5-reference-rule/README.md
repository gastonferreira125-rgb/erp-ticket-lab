# v5-reference-rule — primera ejecución registrada

Deriva de v4-integration-rule. Solo añade la regla de extracción en added-rule.txt, incluida al final de system.txt. Mantiene categorías, prioridad, regla de instrucciones y los seis campos/tipos.

Aclaración semántica: referencia_documento incluye el identificador del documento ERP o código de artículo afectado. Se mantiene el nombre para conservar compatibilidad con el laboratorio; un nombre más general podría estudiarse en otra versión. schema.json copia el esquema original con descripción añadida al campo; esa descripción no impone validación semántica por sí misma.

Motivos del ajuste: omisiones de referencias de pedidos (T03-v3 y T12-v4), y ambigüedad del código de artículo T04. El conjunto original y resultados históricos se conservan.

Primera ejecución: [T12-v5](../../experiments/2026-10-14-t12-v5/README.md) devuelve OV-3301 y coincide con etiquetas. Resumen y datos_faltantes vacío requieren revisión humana. T03-v5 también devuelve OV-2099 y coincide en etiquetas. Cobertura de v5: cinco casos originales conformes, T01/T03/T04/T07/T10 (5/5 entre ejecutados, cobertura 5/10), y un complementario conforme (1/1). Ambos tienen lista de datos faltantes vacía, con oportunidad de pedir dirección correcta.

T12 fue usado para ajustar v5, por lo que no es una prueba independiente de generalización para esta versión. No inferir causalidad o robustez general de una respuesta.

T04 también devuelve ART-310. Solicita almacén ya informado y omite cantidades; hallazgo de contenido pendiente.

T10 conserva Otros, Media y null en el control de instrucciones.

T07 conserva Integraciones, Alta y null en esta ejecución.

T01 conserva Finanzas, Media y null; datos_faltantes útil pero amplio y sin pasos de reproducción.

Siguiente: completar T02/T05/T06/T08/T09 del conjunto original y consolidar ronda, sin cambios adicionales del prompt. Registrar configuración verificada y conservar respuestas originales.
