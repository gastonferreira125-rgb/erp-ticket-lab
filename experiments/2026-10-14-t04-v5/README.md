# T04 — v5 — 14 de octubre de 2026

## Entrada
```text
ENTRADA:
ticket_id: T04
<ticket>
Necesitamos revisar el stock del artículo ART-310 en el almacén central; difiere del conteo físico.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T04",
  "categoria": "Inventario",
  "prioridad": "Media",
  "resumen": "Se necesita revisar el stock de un artículo que difiere del conteo físico.",
  "referencia_documento": "ART-310",
  "datos_faltantes": [
    "Almacén específico",
    "Fecha del conteo físico",
    "Fecha de la última transacción del artículo"
  ]
}
```

## Evaluación automática
evaluate.py ejecutado sobre responses.json: T04 presente, formato y etiquetas conformes; Inventario, Media y ART-310. Sin referencias ausentes literalmente, duplicados ni IDs desconocidos. Los otros nueve tickets del evaluation.json no se ejecutaron en este archivo.

## Revisión humana
Captura coincide con JSON. Resumen fiel, sin causa o solución inventada, aunque omite el almacén central y usa "un artículo" (ART-310 sí está en su campo específico).
datos_faltantes pide "Almacén específico", pero la entrada ya informa almacén central. Si se necesita un código único, debe pedirlo explícitamente en vez de volver a solicitar el almacén sin aclaración.
Fecha de conteo es útil. Última transacción puede ayudar a conciliar movimientos, pero no es necesariamente indispensable. Falta solicitar stock registrado en sistema y cantidad del conteo físico, útiles para dimensionar la diferencia.

## Comparación y límites
T04-v3 devolvió null y el contrato para códigos de artículo era ambiguo. v5 aclara expresamente el alcance y esta ejecución devuelve ART-310, coincidiendo con el conjunto original que se conserva sin modificar. No es una mejora atribuible únicamente al modelo: también se aclaró el contrato. Entre v3/v5 hay dos cambios de prompt; no inferir causalidad de una sola respuesta por versión.

v5: T03/T04 conformes del conjunto original (2/2 entre ejecutados, cobertura 2/10), y T12 conforme complementario (1/1). Controles T10/T07 pendientes. Casos usados para motivar el ajuste, sin generalización independiente demostrada.

[Prompt v5](../../prompts/v5-reference-rule/system.txt) y [esquema descriptivo](../../prompts/v5-reference-rule/schema.json). Roles/configuración solicitados: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Captura no verifica esos parámetros ni el prompt completo realmente enviado.

Próximo: T10 para verificar que la extracción no toma como válida una referencia incluida solo en una instrucción de dictar la respuesta; después T07 para conservar la regla de Integraciones. No modificar v5 todavía. Mejora de datos faltantes registrada para una versión posterior.
