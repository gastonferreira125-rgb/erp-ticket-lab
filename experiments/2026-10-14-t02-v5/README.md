# T02 — v5 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T02
<ticket>
La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T02",
  "categoria": "Finanzas",
  "prioridad": "Alta",
  "resumen": "La factura FV-1042 no se contabiliza.",
  "referencia_documento": "FV-1042",
  "datos_faltantes": []
}
```

## Evaluación automática
evaluate.py ejecutado sobre responses.json: T02 presente, formato y etiquetas conformes (Finanzas, Alta, FV-1042). Alta sustentada por detención explícita del cierre y bloqueo de todo el equipo en la entrada. Sin IDs duplicados/desconocidos o referencias ausentes literalmente. Otros nueve tickets no ejecutados en este archivo.

## Revisión humana
Fuente: JSON pegado por el usuario, sin captura en este mensaje. Resumen fiel al problema de contabilización y sin inventar causa o solución, pero omite el impacto explícito (todo el equipo bloqueado y cierre detenido). Pierde información importante para priorización humana.
datos_faltantes vacío cumple estructura, pero no reúne información útil para investigar. Falta mensaje de error exacto y pasos para reproducir. Una clasificación completa no implica un ticket listo para atender.

T02-v3 preservaba al menos afectación del equipo/cierre y pedía error, momento y usuario; esta ejecución v5 reduce detalle del resumen y datos faltantes. Es una observación de deterioro cualitativo, no prueba de que una regla de extracción haya causado el cambio. Una respuesta por versión y parámetros no reconfirmados limitan inferencias.

## Continuidad
Etiquetas conservadas respecto de v0/v2/v3. v5: seis casos conformes del conjunto original (T01/T02/T03/T04/T07/T10; 6/6 entre ejecutados, cobertura 6/10) y un complementario T12 conforme (1/1). Mantener métricas separadas de versiones/conjuntos.

[Prompt v5](../../prompts/v5-reference-rule/system.txt). Roles/configuración solicitados: Sistema/Usuario, Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado. Respuesta textual no confirma esos parámetros, prompt completo ni guardado SAP.

Restan T05/T06/T08/T09 con v5 sin cambios. Siguiente T05. Mejoras de precisión del impacto en resúmenes y datos faltantes quedan para una versión posterior a la ronda completa.
