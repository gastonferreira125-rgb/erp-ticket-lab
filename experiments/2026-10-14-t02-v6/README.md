# T02 — versión indicada v6 — 14 de octubre de 2026

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
  "resumen": "La factura FV-1042 no se contabiliza, deteniendo el cierre del equipo de Finanzas.",
  "referencia_documento": "FV-1042",
  "datos_faltantes": []
}
```

## Evaluación
evaluate.py confirma T02 presente, formato y etiquetas conformes: Finanzas, Alta y FV-1042. Sin referencias ausentes literalmente ni IDs duplicados/desconocidos. Los otros nueve tickets no se ejecutaron en este archivo.

La prueba de contenido dirigida a datos_faltantes no cumple su objetivo en la salida recibida: lista vacía pese a faltar error exacto y pasos para investigar la contabilización. No contabilizar acierto de etiquetas como mejora del campo.
El resumen vuelve a conservar la detención del cierre, sin inventar causa/solución. Esa diferencia frente a v5 no puede atribuirse a una regla que modifica datos_faltantes a partir de una sola respuesta.

## Trazabilidad y verificación pendiente
Fuente: JSON pegado, sin captura. La versión v6 es la indicada en el procedimiento; no se verificó visualmente que el usuario haya incorporado la regla al Sistema de SAP. El archivo de GitHub sí contiene la regla, lo que no confirma lo realmente enviado al modelo desde Launchpad. No asumir incumplimiento general del modelo ni que faltó copiar el bloque.

[Prompt previsto](../../prompts/v6-missing-data-rule/system.txt). Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; parámetros actuales y guardado SAP sin confirmar.

v6 tiene una salida recibida del conjunto original (T02): etiquetas 1/1 entre ejecutados, cobertura 1/10. Objetivo humano de datos faltantes no cumplido en esta salida. v5 permanece 10/10 del conjunto original, separado.

Verificación posterior: el usuario pegó Sistema completo y coincide con v6 guardada, tras normalizar saltos de línea/extremos. [Evidencia textual](system-confirmation.md). No hay captura ni payload retrospectivo; el contenido aportado sí incluye la regla completa.

Próximo: repetir T02 una vez sin cambios, guardar ejecución separada, luego controles T04/T06/T10 según lo observado.
