# T01 — v5 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T01
<ticket>
No puedo registrar un pago a un proveedor. No anoté el mensaje de error.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T01",
  "categoria": "Finanzas",
  "prioridad": "Media",
  "resumen": "El usuario no puede registrar un pago a un proveedor.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Mensaje de error",
    "Detalles del pago (proveedor, importe, fecha, etc.)"
  ]
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T01 presente, formato y etiquetas conformes; Finanzas, Media y null. No hay referencia explícita ni afirmación de bloqueo de todo un equipo. Sin IDs duplicados/desconocidos o referencias ausentes literalmente. Otros nueve casos no ejecutados en este archivo.

Fuente: JSON pegado por el usuario, sin captura en este mensaje. Resumen fiel, sin causa ni solución inventada. Error y detalles del pago son información útil. La formulación "etc." es abierta; sería más preciso pedir error exacto, pasos para reproducir y detalles concretos del pago.
T01-v3 solicitaba pasos de reproducción, que no aparecen en esta ejecución v5. Registrar reducción de detalle, sin concluir causalidad del cambio de prompt a partir de una respuesta por versión.

## Regresión y continuidad
Conserva etiquetas previamente conformes de v0 y v3. v5: cinco casos conformes del conjunto original T01/T03/T04/T07/T10 (5/5 entre ejecutados, cobertura 5/10), y un complementario T12 conforme (1/1). No mezclar versiones/conjuntos; la comparación completa con v3 requiere terminar v5.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración solicitados: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Parámetros actuales, prompt completo enviado y guardado SAP no confirmados por esta respuesta textual.

Restan T02/T05/T06/T08/T09 sin modificar v5. Siguiente T02. Hallazgos de datos_faltantes y precisión de resumen pendientes para otro ajuste.
