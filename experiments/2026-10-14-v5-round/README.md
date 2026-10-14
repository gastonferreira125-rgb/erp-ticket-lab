# Ronda completa v5 — 14 de octubre de 2026

Diez respuestas originales de los diez tickets sintéticos del conjunto inicial. Ejecutadas manualmente con Sistema v5 y Usuario con id/texto, según las instrucciones del laboratorio. El caso complementario T12 se evalúa por separado.

Acumulado al cerrar esta ronda: 33 ejecuciones entre versiones, sobre doce tickets distintos. v5 tiene diez respuestas del conjunto original y una de T12.

## Comparación automática con v3
| Comprobación | v3 | v5 |
| --- | --- | --- |
| Cobertura del conjunto original | 10/10 | 10/10 |
| Campos, tipos y valores permitidos | 10/10 | 10/10 |
| Categoría | 9/10 | 10/10 |
| Prioridad | 10/10 | 10/10 |
| Referencia | 8/10 | 10/10 |
| Todas las etiquetas coinciden | 7/10 | 10/10 |
| Referencias ausentes literalmente del ticket | 0 | 0 |

Se ejecutó la función evaluate de evaluate.py sobre las dos rondas y el mismo tickets.json. No se cambiaron etiquetas originales para mejorar el puntaje. Ninguna ronda tiene IDs duplicados o desconocidos.
La búsqueda literal de referencias no verifica pertinencia semántica, y las métricas automáticas no puntúan precisión del resumen ni utilidad de datos_faltantes.

Diferencias conformes observadas: T07 devuelve Integraciones en v5 frente a Ventas en v3; T03 devuelve OV-2099 frente a null; T04 devuelve ART-310 frente a null.
En T04, v5 también aclaró el alcance del contrato para códigos de artículo. Esa diferencia combina aclaración de diseño y extracción observada, y no debe atribuirse únicamente a capacidad del modelo.

## Revisión humana comparativa
| Ticket | Observación de contenido en v5 frente a v3 |
| --- | --- |
| T01 | Resumen fiel; pide error y detalles de pago, pero pierde pasos de reproducción y usa "etc." abierto. |
| T02 | Pierde toda mención al equipo/cierre en el resumen y devuelve datos_faltantes vacío; v3 mencionaba el impacto y pedía error/momento/usuario. |
| T03 | Mejora referencia en su campo, pero lista vacía omite dirección correcta, pedida en v3. |
| T04 | Extrae ART-310; pide almacén pese a estar informado como central y no pide cantidades de sistema/conteo, que sí pedía v3. |
| T05 | Conserva problema de permisos, datos de usuario/reporte útiles y ausencia de causa inventada. |
| T06 | Conserva solicitud pendiente y datos de requisitos útiles; incluye ordenamiento. |
| T07 | Conserva caída y falta de ingreso; omite detención de todo el equipo. Datos de tienda/error/inicio útiles. |
| T08 | Conserva etiquetas y resumen, pero "Procedimiento a revisar" es poco concreto; omite fechas actual/esperada pedidas en v3. |
| T09 | Conserva solicitud planificada; lista vacía en ambas versiones. Falta alcance para preparar documentación y capacitación; omite que son dos usuarios nuevos. |
| T10 | Conserva tratamiento de instrucciones, null y solicitud de incidente; resumen más breve que v3, sin afirmar corrección. |

10/10 en etiquetas de esta ronda no significa respuesta perfecta ni que el sistema esté listo para atender tickets. No se calculó un puntaje global de calidad humana con una rúbrica previamente definida.

## Reproducibilidad y límites
[Prompt v5](../../prompts/v5-reference-rule/system.txt), [descripción de esquema v5](../../prompts/v5-reference-rule/schema.json), [respuestas originales](responses.json), [evaluación automática](evaluation.json).
Las entradas indicadas siguen:
```text
ENTRADA:
ticket_id: Txx
<ticket>
texto literal de tickets.json
</ticket>
```
Etiquetas esperadas usadas después de generar, no enviadas al modelo. No se corrigieron salidas.

Modelo solicitado: Gemini 2.5 Flash Lite (001). Parámetros solicitados: temperatura 1, máximo de salida 43690, streaming activado. No se reconfirmaron todos los valores numéricos por ejecución. Hubo cierre/restauración de Launchpad entre casos y se recuperó Sistema v5 desde GitHub. Guardado de plantilla SAP no confirmado.
Capturas revisadas en T03/T04/T10; los restantes originales de v5 se recibieron como JSON pegado sin captura en esos mensajes. No afirmar confirmación visual global del prompt o configuración. Las imágenes no se publican aquí.

Una respuesta por caso y versión, casos usados para ajustes, parámetros no completamente confirmados y cambios acumulados de reglas no permiten demostrar causalidad ni generalización en producción. No hay comparación de modelos, repetición sistemática, medición de ahorro ni integración operativa ERP. T12 fue usado para ajustar v5 y no es prueba independiente de generalización de esa versión.

## Siguiente versión preparada
[v6-missing-data-rule](../../prompts/v6-missing-data-rule/README.md), sin ejecuciones. Añade solo una regla de calidad de datos_faltantes: usar lo ya informado, pedir información ausente útil y concreta, reservar [] cuando baste para investigar/definir el siguiente paso.
No modifica categorías, prioridades, referencias ni regla de resumen. La precisión del impacto en resúmenes se tratará después como ajuste separado.
Primer caso propuesto: T02. Después controles T04/T06/T10. Registrar mejora de contenido manualmente además de etiquetas, sin asumir que todas las salidas mejorarán.
