# T08 — v4 — 14 de octubre de 2026

## Entrada
```text
ENTRADA:
ticket_id: T08
<ticket>
El pedido de compra PC-778 tiene una fecha de entrega equivocada. Necesito revisar el procedimiento.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T08",
  "categoria": "Compras",
  "prioridad": "Media",
  "resumen": "El pedido de compra PC-778 tiene una fecha de entrega equivocada.",
  "referencia_documento": "PC-778",
  "datos_faltantes": [
    "Fecha de entrega original",
    "Fecha de entrega deseada"
  ]
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T08 presente, formato conforme, etiquetas coincidentes y sin referencia ausente del texto. Los nueve casos sin respuesta en evaluation.json corresponden a entradas no ejecutadas en este archivo, no a fallos del modelo.
La captura coincide con el JSON. Categoría Compras, prioridad Media y referencia PC-778 conservan el resultado de v3. El resumen es fiel, sin causa o solución inventada, y omite la solicitud de revisar el procedimiento.

La lista de fechas es pertinente, pero "original" puede referirse a la primera fecha histórica, y "deseada" a una nueva preferencia. "Fecha registrada actualmente" y "fecha correcta esperada" serían más precisas para investigar un dato incorrecto. No corregir la respuesta original ni convertir esa oportunidad de redacción en fallo de etiquetas.

## Regresión y continuidad
Una sola ejecución conforme de T08 con v4 no demuestra ausencia de regresiones en otros casos ni explica por sí sola la variación de datos_faltantes. v4 tiene dos casos ejecutados, T07 y T08, ambos conformes (2/2 entre ejecutados, cobertura 2/10). v3 mantiene por separado 7/10; no mezclar versiones.

[Prompt v4](../../prompts/v4-integration-rule/system.txt). Roles y parámetros según continuidad solicitada: Sistema con reglas y Usuario con ticket; Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690 y streaming activado. Esta captura no confirma esos parámetros ni el prompt completo realmente enviado.

Próximo control: T10 con v4, conservando prompt y parámetros; después un caso nuevo de integración con impacto parcial. La extracción de T03/T04 queda pendiente para una mejora separada.
