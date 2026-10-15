# T13 — caso complementario v7 — 15 de octubre de 2026

## Expectativas previas y entrada
[Snapshot de entrada/etiquetas](cases.json), copiado sin cambios de [generalization-v7-t13.json](../../tickets/generalization-v7-t13.json). [Criterios humanos](../../tickets/generalization-v7-t13.md) registrados antes de la salida, en el commit 676702a7f3f8505f604767912debcdc02dd61047.

Se indicó conservar Sistema/EX01/EX02 de v7 y cambiar solo último Usuario por T13. Modelo visible en captura previa: Gemini 2.5 Flash Lite (001). Resultado pegado como texto, sin captura final, payload ni parámetros numéricos actuales completamente verificados.

Texto:
> Desde ayer, algunas facturas de la tienda no llegan al ERP. Otras sí se importan y el equipo de Finanzas sigue trabajando. La factura FV-2086 es un ejemplo afectado.

## Original y evaluación
[Texto exacto](raw-response.txt), [respuesta en lista](responses.json), [evaluación ejecutada](evaluation.json).

evaluate.py ejecutado con el conjunto complementario de un caso: formato 1/1 y etiquetas 1/1, referencia literal, sin ids duplicados/desconocidos. Se conserva separado del conjunto original v7 (4/10 de cobertura; 4/4 etiquetas entre ejecutados).

## Revisión humana contra criterios previos

| Aspecto | Observación |
| --- | --- |
| Categoría | Integraciones por intercambio entre sistemas pese a factura/Finanzas |
| Prioridad | Media: importación parcial, equipo sigue trabajando |
| Referencia | FV-2086 copiada, sin volver a pedir ejemplo de factura |
| Resumen | Conserva importación parcial sin inventar caída total/causa/corrección; omite explícitamente continuidad del equipo |
| Horario | Útil para precisar “desde ayer”; mejor formulación: hora aproximada de ayer en que empezó |
| Sistema de origen | Ausente y útil |
| Alcance/tipo | Pregunta parcialmente redundante: ya se sabe que algunas fallan y otras se importan; tipo específico es un detalle ausente útil |

Formulación de mejora humana, no salida del modelo ni cambio de prompt: “Qué tienen en común las facturas que fallan (tipo, estado o canal)”. No se afirma que el defecto tenga esa causa; se pide información para comparar.

La lista ofrece datos útiles, pero no usa perfectamente todo lo informado. Error o registros podrían ser útiles después; los criterios previos incluían ejemplos orientativos, no una lista textual obligatoria. No se inventa una puntuación humana agregada retrospectiva.

## Generalización y límites
Caso nuevo para v7 con expectativas previas y sin ajuste específico antes de la salida. Variante cercana a T11, no muestra representativa de producción. Aporta una observación de etiquetas conformes con revisión humana mixta; no prueba robustez general ni que few-shot causara el resultado. Si se usa después para ajustar, deja de ser independiente de esa versión.

v7: cuatro respuestas originales y un caso complementario, métricas separadas. Total entre versiones: 43 respuestas registradas sobre trece tickets distintos. EX01/EX02 no cuentan como ejecuciones.

## Próximo paso
Repetir T02 una vez con v7 sin cambios y conservar como segunda ejecución separada. Primera T02-v7 quedó con datos_faltantes vacío. Observar si se mantiene o varía antes de modificar reglas/ejemplos; una repetición no es nuevo ticket ni prueba de determinismo. [Usuario T02](../../prompts/v7-few-shot/user-t02.txt).
