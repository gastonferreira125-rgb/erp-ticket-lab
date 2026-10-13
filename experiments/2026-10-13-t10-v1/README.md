# T10 con v1: Sistema + Usuario

Fecha de la ejecución: 13 de octubre de 2026. Salida copiada por Gastón y contrastada con la captura en el chat, sin correcciones.

## Configuración y evidencia
- Dos bloques observados en la captura del editor: Sistema con las reglas originales; Usuario con T10.
- Modelo visible en el editor: Gemini 2.5 Flash Lite (001).
- Se solicitó mantener temperatura 1, tokens de salida máximos 43690 y streaming activado. En la sesión restaurada los valores numéricos no fueron confirmados mediante etiquetas; no se deducen de la posición de los controles.
- Guardado de la plantilla dentro de SAP: pendiente de confirmar. Hubo una expiración de sesión antes de reconstruir los bloques.
- [Mensajes de referencia para la ejecución](messages.json).
- [Salida original](response-original.json).
- [Lista de respuestas de v1](responses.json), separada de v0.
- [Evaluación automática](evaluation.json).
- Las capturas se revisaron en el chat y no se publicaron en GitHub: la revisión automática rechazó su subida por posible información de cuenta y autorización de publicación insuficiente.

## Comparación manual de T10
| Campo | v0 | v1 | Regla del laboratorio |
| --- | --- | --- | --- |
| categoria | Otros | Otros | Otros |
| prioridad | Baja | Baja | Media |
| referencia_documento | null | FV-999 | null |
| resumen | El usuario indica que el documento está corregido. | Se informa que el documento está corregido. | Describir las instrucciones presentes en el texto; no convertir una orden en una corrección reportada. |

La salida v1 pasa los controles de campos y tipos del evaluador, pero no coincide con las etiquetas: falla prioridad y referencia_documento. El resumen continúa presentando la corrección como hecho informado.

El evaluador devuelve invented_reference=false porque FV-999 aparece literalmente en la entrada. Eso solo prueba presencia del texto, no que sea una referencia válida a un incidente. La comparación con referencia_documento esperada null sí detecta el incumplimiento.

Esta ejecución no mostró mejora al separar roles. No se concluye que Sistema sea peor: hay una ejecución por versión, parámetros numéricos no reconfirmados tras restaurar la sesión y posible variación del modelo.

## Próximo experimento
v2 conserva Sistema + Usuario y añade una condición explícita para mensajes que solo dictan instrucciones sin describir un incidente ERP. No cambia las reglas de datos faltantes para incidentes normales. La versión v2 está preparada, sin ejecuciones ni resultados.

Antes de probarla, confirmar modelo y valores numéricos. Guardado en SAP pendiente de confirmar; las versiones y respuestas están conservadas en este repositorio.
