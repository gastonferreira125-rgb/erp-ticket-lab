# T12 — v5 — 14 de octubre de 2026

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
  "resumen": "El pedido de venta OV-3301 tiene una dirección incorrecta cargada manualmente.",
  "referencia_documento": "OV-3301",
  "datos_faltantes": []
}
```

## Evaluación automática
Función evaluate de evaluate.py aplicada al conjunto complementario cases.json: cobertura 1/1, formato 1/1, etiquetas completas 1/1. Coinciden Ventas, Media y OV-3301. Sin referencias ausentes del texto, duplicados o IDs desconocidos. Captura coincide con JSON pegado.

## Revisión humana
La referencia se extrae ahora en su campo específico; en T12-v4 era null. Resumen: el texto original atribuye carga manual al pedido. "Dirección incorrecta cargada manualmente" vincula ese atributo a la dirección, un detalle más específico que la entrada; sería más fiel mantener la descripción del pedido con dirección incorrecta sin trasladar el atributo. No se afirma una corrección realizada.

datos_faltantes vacío es válido en estructura y no falla las etiquetas, pero la dirección correcta sigue siendo información útil para atender la solicitud. T12-v4 sí la pedía. Hay una reducción de utilidad en este campo en esta ejecución; no atribuirla causalmente a la regla de referencias a partir de una sola respuesta por versión.

## Comparación y límites
T12-v4: etiquetas completas no conformes por referencia null. T12-v5: conformes por OV-3301. El cambio preparado entre v4/v5 fue la regla de extracción y aclaración de alcance. Una ejecución por versión, sin reconfirmación de todos los parámetros, no permite demostrar causalidad ni consistencia.

T12 se usó para ajustar v5 y ya no es un caso nuevo independiente para esa versión. v5 cubre solo este caso complementario (1/1 conforme); ninguno de los diez tickets del conjunto original se ejecutó todavía con v5. No mezclar con v4 o v3. Acierto de etiquetas no sustituye revisión del resumen o información faltante.

[Prompt v5](../../prompts/v5-reference-rule/system.txt), [esquema semántico versionado](../../prompts/v5-reference-rule/schema.json). Misma estructura de seis claves. Configuración solicitada en continuidad: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Captura no confirma esos parámetros ni el prompt completo realmente enviado.

Próximo: T03 con v5 sin cambios; después T04 y controles T10/T07. Mantener respuestas originales sin corregir.
