# T02 — v6 — repetición 2 — 14 de octubre de 2026

## Entrada indicada, sin cambios
```text
ENTRADA:
ticket_id: T02
<ticket>
La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.
</ticket>
```

## Respuesta original, segunda ejecución
```json
{
  "ticket_id": "T02",
  "categoria": "Finanzas",
  "prioridad": "Alta",
  "resumen": "La factura FV-1042 no se contabiliza y detiene el cierre financiero.",
  "referencia_documento": "FV-1042",
  "datos_faltantes": []
}
```

## Evaluación
evaluate.py ejecutado: T02 presente, formato y etiquetas conformes (Finanzas, Alta, FV-1042). No se modificó la primera salida ni se mezclaron dos respuestas T02 en un archivo de benchmark. Fuente: JSON pegado, sin captura.

Objetivo humano de datos_faltantes no cumplido: lista vacía pese a faltar mensaje de error exacto y pasos para investigar. Resumen fiel al fallo y detención del cierre, sin causa o corrección inventada; omite bloqueo de todo el equipo.

## Repetición y comparación
| Campo | Ejecución 1 | Ejecución 2 |
| --- | --- | --- |
| Etiquetas | Conformes | Conformes |
| datos_faltantes | [] | [] |
| Resumen | Cierre del equipo de Finanzas detenido | Cierre financiero detenido |

Dos observaciones conservan el problema de lista vacía para T02, aunque cambia la redacción del resumen. No prueban incumplimiento universal ni permiten identificar causa interna. La coincidencia del campo en dos ejecuciones no es garantía de determinismo.

Antes de repetir, el usuario aportó Sistema completo y coincide con v6 guardada. [Verificación textual](../2026-10-14-t02-v6/system-confirmation.md). Configuración solicitada sin cambios: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690 y streaming activado. Sin captura/payload que confirme todos los valores enviados.

v6: dos ejecuciones de un mismo ticket original, ambas conformes en etiquetas y no conformes con el objetivo de datos faltantes. Cobertura única 1/10, no 2/10. Total entre versiones: 35 ejecuciones sobre doce tickets distintos.

Próximo: T04 con v6 sin cambios, para controlar información ya aportada (almacén central) y solicitudes concretas de cantidades. Luego T06/T10 según resultados antes de ajustar otra versión.
