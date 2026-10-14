# Ronda completa v3 — 14 de octubre de 2026

Diez respuestas originales de diez tickets sintéticos ejecutados manualmente con v3-category-rule. Hay 17 ejecuciones acumuladas entre v0, v1, v2 y v3, sobre diez tickets distintos. No mezclar versiones al calcular métricas.

## Resultado del evaluador
| Comprobación | Resultado |
| --- | --- |
| Cobertura | 10/10 |
| Campos, tipos y valores permitidos | 10/10 |
| Categoría | 9/10 |
| Prioridad | 10/10 |
| Referencia | 8/10 |
| Coincidencia completa de etiquetas | 7/10 |
| Referencias ausentes del texto | 0 |
| Identificadores duplicados o desconocidos | 0 |

El 70% es coincidencia completa en estos diez casos y una ejecución por caso; no es exactitud general en producción. La comprobación de referencias ausentes solo busca presencia literal; no valida su pertinencia semántica.

## Diferencias observadas
| Ticket | Campo | Esperado | Observado |
| --- | --- | --- | --- |
| T03 | referencia_documento | OV-2099 | null |
| T04 | referencia_documento | ART-310 | null |
| T07 | categoria | Integraciones | Ventas |

T04 identifica un artículo, no un documento. El conjunto original espera ART-310, pero el nombre y definición del campo son ambiguos. Conservar el resultado 7/10 contra el conjunto original y revisar el contrato en una versión futura, sin cambiar retroactivamente las etiquetas para mejorar el puntaje.

## Revisión humana
- T01: resumen fiel e información útil, incluidos pasos de reproducción.
- T02: etiquetas correctas; "afectando" pierde precisión frente a equipo bloqueado y cierre detenido.
- T03: menciona OV-2099 en el resumen, pero omite la referencia en su campo.
- T04: resumen fiel; fecha y diferencia de cantidades útiles. Logs no necesariamente indispensables.
- T05: reconoce permisos como Autorizaciones aunque el recurso sea un reporte.
- T06: reconoce solicitud de reporte planificada y pide requisitos.
- T07: el problema principal es la integración; Ventas es el área afectada. Prioridad Alta correcta.
- T08: etiquetas y referencia correctas; fechas actual y esperada útiles.
- T09: mejora planificada, Baja; lista vacía válida, pero faltaría alcance para preparar documentación/capacitación.
- T10: describe instrucciones como contenido del ticket, sin afirmar corrección; Otros, Media, null. La frase "sin afirmar..." es innecesaria en un resumen para soporte, pero no inventa una acción.

## Trazabilidad
[Prompt v3](../../prompts/v3-category-rule/system.txt). Reglas en Sistema y ticket en Usuario; no ejemplos Asistente en esta ronda. La reconstrucción de cada entrada sigue el formato:
```text
ENTRADA:
ticket_id: Txx
<ticket>
texto literal de tickets.json
</ticket>
```
Las etiquetas esperadas no se enviaron al modelo. [Respuestas originales](responses.json) y [evaluación automática](evaluation.json).
Comando ejecutado desde la raíz del proyecto:
```sh
python3 evaluate.py experiments/2026-10-14-v3-round/responses.json
```

Modelo solicitado: Gemini 2.5 Flash Lite (001); temperatura solicitada 1; máximo de salida solicitado 43690; streaming solicitado activado. Las capturas de las respuestas no confirman todos los parámetros actuales y el guardado de plantilla SAP no se confirmó.

T01 y T02 conservan etiquetas previamente correctas; T10 conserva el resultado conforme de v2. Cada uno es una observación de regresión, no garantía sobre otras entradas. T05 y T10 fueron usados para ajustar versiones previas, por lo que este conjunto no es una prueba independiente de generalización. No hay comparación de modelos, repetición sistemática ni integración operativa al ERP.

## Próximo paso
Crear una versión nueva con una sola mejora en categorías: aclarar que una caída o falla de intercambio entre sistemas se clasifica como Integraciones, aunque afecte Ventas o Compras. Repetir T07 y controles; no cambiar referencias simultáneamente. Después aclarar el alcance de referencia_documento y alinear esquema, prompt y conjunto esperado. Añadir casos nuevos para evaluar generalización y repetir casos para observar variabilidad.
