# T12 — v4 — 14 de octubre de 2026

## Entrada
```text
ENTRADA:
ticket_id: T12
<ticket>
El pedido de venta OV-3301 tiene una dirección incorrecta. Fue cargado manualmente en el ERP; la tienda se usa solo para consultar el catálogo. Solo ocurre con este pedido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T12",
  "categoria": "Ventas",
  "prioridad": "Media",
  "resumen": "El pedido de venta OV-3301 tiene una dirección incorrecta.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Dirección correcta del pedido de venta OV-3301",
    "Detalles de cómo se cargó manualmente el pedido"
  ]
}
```

## Evaluación
Caso y etiquetas guardados antes de ejecutar. Función evaluate de evaluate.py aplicada al conjunto complementario cases.json: cobertura 1/1, formato 1/1 y etiquetas completas 0/1. Ventas y Media conformes. Referencia esperada OV-3301; observada null.

La captura coincide con el JSON. Resumen fiel y sin causa o corrección inventada. Referencia presente en resumen y datos_faltantes, omitida en el campo específico. Dirección correcta y procedimiento de carga son datos útiles.

El contraste de categoría pasa: la mención de tienda como consulta de catálogo no se convierte en Integraciones. El caso completo falla por extracción de referencia. Es un patrón observable similar a T03-v3; no permite concluir la causa interna del modelo.

## Métricas separadas
v4: conjunto original 3/3 conformes entre ejecutados, cobertura 3/10. Complementarios T11/T12: formato 2/2, categorías 2/2, prioridades 2/2, referencias 1/2, etiquetas completas 1/2. v3 conserva 7/10 del conjunto original. No mezclar versiones/conjuntos para construir una exactitud general.

Modelo y parámetros solicitados según continuidad: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; Sistema v4 y Usuario con ticket. La captura no verifica esos parámetros ni el prompt completo. [Prompt](../../prompts/v4-integration-rule/system.txt).

## Siguiente versión
v5 preparada con una aclaración de extracción y alcance de referencia_documento. Mismas seis claves y tipos; se explicita que el campo incluye códigos de artículo, alineándose con ART-310 del conjunto original. Etiquetas históricas y respuestas originales sin modificar. Repetir T12 con v5; después T03/T04 y controles T10/T07. v5 no ejecutada todavía.
