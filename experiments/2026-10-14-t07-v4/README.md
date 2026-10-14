# T07 — v4 — 14 de octubre de 2026

## Entrada
```text
ENTRADA:
ticket_id: T07
<ticket>
La integración de pedidos con la tienda está caída. Ningún pedido entra y todo el equipo de ventas está detenido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T07",
  "categoria": "Integraciones",
  "prioridad": "Alta",
  "resumen": "La integración de pedidos con la tienda no está funcionando y afecta al equipo de ventas.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Detalles específicos de la caída de la integración (fechas, horas).",
    "Mensajes de error observados, si los hay.",
    "Información sobre el sistema de tienda y el sistema ERP involucrados."
  ]
}
```

## Resultado
| Campo | Esperado | Observado | Resultado |
| --- | --- | --- | --- |
| categoria | Integraciones | Integraciones | Conforme |
| prioridad | Alta | Alta | Conforme |
| referencia_documento | null | null | Conforme |

evaluate.py ejecutado sobre responses.json: una respuesta presente, una válida y una coincidencia completa de etiquetas; sin IDs duplicados o desconocidos ni referencias ausentes del texto. Los otros nueve tickets no se han ejecutado con v4 y no cuentan como fallos del modelo.

La captura coincide con el JSON pegado. Resumen sin causa o solución inventada, pero "afecta" pierde el impacto explícito: ningún pedido entra y todo el equipo está detenido. Datos faltantes pertinentes: momento de la caída, error si existe y sistemas involucrados.

## Comparación y límites
T07-v3 devolvió Ventas. Esta ejecución v4 devuelve Integraciones después de añadir una regla explícita de categoría por problema de intercambio entre sistemas. Una respuesta de cada versión no prueba causalidad ni generalización; T07 es el caso usado para ajustar la regla.

v3 permanece como ronda de diez tickets, 7/10 coincidencias completas. v4 tiene un solo caso ejecutado, conforme (1/1 entre ejecutados, cobertura 1/10). No sumar T07-v4 a los resultados de v3 ni presentar 8/10 como resultado medido de v4.

[Prompt v4](../../prompts/v4-integration-rule/system.txt). messages.json reconstruye las entradas indicadas al usuario; la captura del resultado no verifica el texto completo realmente enviado a SAP. Modelo y parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; no confirmados por esta captura.

Siguiente: T08 con v4 sin cambios, como control de regresión de Compras, luego controles de otras reglas y casos nuevos. La mejora de referencias T03/T04 queda separada para otra versión.
