# T03 — v5 — 14 de octubre de 2026

## Entrada
```text
ENTRADA:
ticket_id: T03
<ticket>
El pedido OV-2099 tiene una dirección incorrecta. Solo me ocurre con este pedido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T03",
  "categoria": "Ventas",
  "prioridad": "Media",
  "resumen": "El pedido OV-2099 tiene una dirección incorrecta.",
  "referencia_documento": "OV-2099",
  "datos_faltantes": []
}
```

## Evaluación
evaluate.py ejecutado sobre responses.json: T03 presente, formato y etiquetas conformes. Coinciden Ventas, Media y OV-2099. Sin referencias ausentes del texto ni IDs duplicados/desconocidos. Los otros nueve tickets del evaluation.json no se ejecutaron en este archivo y no cuentan como fallos.

Captura coincide con JSON. Resumen fiel y sin causa o corrección inventada; omite el alcance limitado a un pedido. datos_faltantes vacío es válido en estructura, pero la dirección correcta sigue siendo información útil. La omisión también apareció en T12-v5; registrarla aparte del acierto en etiquetas.

## Comparación y límites
T03-v3 devolvió referencia null; T03-v5 devuelve OV-2099. Entre v3/v5 se añadieron tanto la regla de integración de v4 como la aclaración de extracción de v5; no atribuir causalidad únicamente a una regla ni a una sola ejecución. T03 forma parte de los casos usados para motivar el ajuste y no es una prueba independiente de generalización de v5.

v5: un caso conforme del conjunto original (T03; 1/1 entre ejecutados, cobertura 1/10) y un caso complementario conforme (T12; 1/1). Conservar métricas separadas de v4 y v3.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración según continuidad solicitada: Sistema con reglas y Usuario con ticket; Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Captura no confirma parámetros ni prompt completo enviado; guardado de plantilla SAP pendiente de confirmar.

Próximo: T04 con v5 sin cambios, luego controles T10/T07. No cambiar ahora la regla de datos_faltantes para no mezclar ajustes.
