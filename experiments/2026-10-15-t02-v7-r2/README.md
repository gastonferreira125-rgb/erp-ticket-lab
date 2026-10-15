# T02 — v7 — repetición 2 — 15 de octubre de 2026

## Entrada y diseño indicado
Mismo T02 original y [v7 con seis mensajes](../../prompts/v7-few-shot/messages-t02.json), sin cambios solicitados de Sistema, ejemplos o parámetros:
> La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.

Fuente: JSON pegado por el usuario. Sin captura final/payload ni parámetros numéricos actuales completos verificados. Conservar la [primera T02-v7](../2026-10-15-t02-v7/README.md).

## Resultado y evaluación automática
[Original exacto](raw-response.txt), [respuesta en lista](responses.json), [evaluación ejecutada](evaluation.json).

evaluate.py confirma campos/tipos y Finanzas/Alta/FV-1042. Sin ids desconocidos/duplicados ni referencia ausente literalmente.

## Análisis cualitativo asistido por IA, pendiente de validación humana
- datos_faltantes vuelve a quedar vacío pese a faltar error exacto y pasos realizados.
- El resumen conserva el bloqueo del equipo pero omite el cierre detenido. No inventa una causa o solución ejecutada.
- Una persona debe validar estos comentarios funcionales; no se atribuyen al usuario por haber pegado el JSON. [Distinción de revisores](../../docs/EVALUATION.md#quién-revisa-tres-niveles-distintos).

| Campo | Primera T02-v7 | Segunda T02-v7 |
| --- | --- | --- |
| Etiquetas | Conformes | Conformes |
| datos_faltantes | [] | [] |
| Resumen | Bloqueo del equipo y cierre | Bloqueo del equipo, omite cierre |

Dos observaciones conservan la omisión de datos útiles. No prueban determinismo ni explican la causa interna, y no justifican atribuir el problema exclusivamente a un prompt cuyo payload final no fue capturado.

## Conteos y siguiente paso
v7 tiene seis respuestas registradas: cinco ejecuciones del conjunto original sobre cuatro tickets únicos (T02 dos veces, T04/T06/T10 una vez) y T13 complementario aparte. No contar esta repetición como nuevo caso ni sumar T13 a la cobertura original 4/10. Todas las ejecuciones originales cumplen formato/etiquetas; utilidad requiere revisión por caso.

Total entre versiones: 44 respuestas sobre trece tickets distintos. Se preservan respuestas sin corregir y ambas T02 por separado.

Próximo: verificar en pantalla el montaje actual de seis mensajes, último Usuario T02 y parámetros, y guardar plantilla SAP si es posible antes de otra versión. No inferir que ya fue guardada ni que la ausencia de preguntas se deba a un error de copia. No se creó v8.
