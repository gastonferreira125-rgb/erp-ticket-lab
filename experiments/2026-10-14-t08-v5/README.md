# T08 — v5 — 14 de octubre de 2026

## Entrada indicada
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
    "Procedimiento a revisar"
  ]
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T08 presente, formato y etiquetas conformes; Compras, Media y PC-778. Sin IDs duplicados/desconocidos o referencias ausentes literalmente. Los otros nueve tickets no se ejecutaron en este archivo.

Fuente: JSON pegado por el usuario, sin captura en este mensaje. Resumen fiel al error de fecha, sin causa ni solución inventada; omite solicitud de revisar el procedimiento.
datos_faltantes "Procedimiento a revisar" puede pedir aclaración del alcance, pero es poco concreto. Falta fecha registrada y fecha correcta esperada para investigar la diferencia. Conviene pedir paso o pantalla donde se registra/observa la fecha si se necesita ubicar el procedimiento.
T08-v3 y v4 pedían fechas; esta ejecución v5 reduce utilidad de la lista. Registrar deterioro cualitativo observado sin atribuir causalidad a la regla de extracción.

## Regresión y continuidad
Conserva etiquetas de T08-v3/v4; una coincidencia de etiquetas no implica que todos los campos mejoraron.
v5: nueve casos conformes del conjunto original T01/T02/T03/T04/T05/T06/T07/T08/T10 (9/9 entre ejecutados, cobertura 9/10), y un complementario T12 conforme (1/1). Mantener métricas separadas.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración solicitados: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Respuesta textual no confirma parámetros actuales, prompt completo enviado ni guardado SAP.

Resta T09 con v5 sin cambios. Después consolidar diez respuestas y revisión humana, preservando hallazgos de datos faltantes y pérdida de impacto en otros casos.
