# T04 — v3 — 2026-10-14

Entrada: Necesitamos revisar el stock del artículo ART-310 en el almacén central; difiere del conteo físico.

## Respuesta original
```json
{
  "ticket_id": "T04",
  "categoria": "Inventario",
  "prioridad": "Media",
  "resumen": "Se necesita revisar el stock del artículo ART-310 en el almacén central debido a discrepancias con el conteo físico.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Fecha del conteo físico.",
    "Detalles de la diferencia de stock observada (cantidad esperada vs. cantidad física).",
    "Capturas de pantalla o logs del sistema que muestren el stock actual del artículo."
  ]
}
```

Captura revisada y coincidente. Campos/tipos correctos. Inventario y Media coinciden; referencia esperada por el conjunto original ART-310, observada null. Resumen fiel; fecha y cantidades útiles; captura del stock puede ayudar y logs no necesariamente indispensables.

Ambigüedad de diseño: ART-310 identifica un artículo, no un documento. Revisar el alcance del campo referencia_documento en una versión futura. No atribuir este caso únicamente al modelo ni alterar el conjunto original retroactivamente.

El guardado inicial venció en revisión automática. Este registro recupera la respuesta original sin modificaciones. Ahora evaluado automáticamente junto con la [ronda completa](../2026-10-14-v3-round/README.md), donde se registra configuración solicitada y límites.
