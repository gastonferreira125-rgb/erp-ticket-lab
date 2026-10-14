# T11 — v4 — 14 de octubre de 2026

## Entrada
```text
ENTRADA:
ticket_id: T11
<ticket>
Desde esta mañana, algunos pedidos de la tienda no llegan al ERP. Otros pedidos sí se importan y el equipo de ventas continúa trabajando.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T11",
  "categoria": "Integraciones",
  "prioridad": "Media",
  "resumen": "Algunos pedidos de la tienda no llegan al ERP.",
  "referencia_documento": null,
  "datos_faltantes": [
    "URL o sistema de origen de los pedidos",
    "Ejemplo de pedido que no se importó",
    "Ejemplo de pedido que sí se importó",
    "Hora aproximada del primer pedido afectado"
  ]
}
```

## Evaluación
Las etiquetas esperadas de T11 se guardaron en tickets/generalization-v4.json antes de recibir el resultado. Se evaluó la respuesta con la función evaluate de evaluate.py y el conjunto complementario, conservado en cases.json. Cobertura 1/1, formato 1/1, etiquetas 1/1; sin referencias ausentes del texto, duplicados ni IDs desconocidos.

Integraciones corresponde al intercambio de pedidos entre tienda y ERP. Media corresponde a impacto parcial: otros pedidos se importan y el equipo continúa trabajando. No hay referencia explícita.
Captura coincide con el JSON pegado. Resumen fiel y breve, sin causa o solución inventada; puede conservar además el impacto parcial y continuidad del equipo. Datos faltantes pertinentes. Comparar ejemplos que se importan y que no se importan ayuda a buscar diferencias sin presuponer una causa.

## Límites
Caso nuevo respecto del ajuste de v4, sin usarlo para cambiar el prompt antes de ejecutarlo. Es una observación positiva de generalización, no demuestra robustez general ni consistencia entre repeticiones. No atribuir el resultado de forma causal a la regla añadida.

v4: tres casos conformes del conjunto original (T07, T08 y T10; cobertura 3/10), y un caso complementario conforme (T11; 1/1). Mantener métricas separadas. v3 permanece 7/10 del conjunto original.

[Prompt v4](../../prompts/v4-integration-rule/system.txt). Roles y configuración según continuidad solicitada: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. La captura no confirma esos parámetros ni el prompt completo realmente enviado; guardado SAP pendiente de confirmar.

## Próximo caso
T12 preparado antes de observar respuesta para contrastar una mención de tienda sin incidente de intercambio: [caso y etiquetas](../../tickets/generalization-v4-t12.json). No enviar etiquetas esperadas al modelo. Mantener v4 sin cambios. T12 no ejecutado todavía. Las mejoras de referencia T03/T04 siguen pendientes.
