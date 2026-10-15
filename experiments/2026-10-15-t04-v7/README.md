# T04 — v7 — 15 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T04
<ticket>
Necesitamos revisar el stock del artículo ART-310 en el almacén central; difiere del conteo físico.
</ticket>
```

Se indicó conservar Sistema v6 y los dos pares Usuario/Asistente de [v7](../../prompts/v7-few-shot/README.md), sustituyendo únicamente el último Usuario T02 por T04. Modelo visible en captura previa Gemini 2.5 Flash Lite (001). Parámetros solicitados sin cambios; valores actuales y payload final de seis bloques no verificados. Fuente de esta salida: JSON pegado, sin captura final.

## Resultado y evaluación
[Texto original exacto](raw-response.txt), [lista de respuestas](responses.json), [evaluación](evaluation.json). No se corrigió la respuesta.

Se ejecutó evaluate.py del repositorio: T04 presente, seis claves/tipos y etiquetas conformes (Inventario, Media, ART-310); referencia literal, sin ids desconocidos/duplicados.

Revisión humana: resumen fiel conserva artículo, almacén y diferencia de stock, sin causa ni solución inventada. datos_faltantes solicita cantidad del sistema, cantidad física y fecha del conteo; son datos ausentes concretos y útiles. No vuelve a pedir el almacén central ya informado.

| Campo | T04-v6 | T04-v7 |
| --- | --- | --- |
| Etiquetas | Conformes | Conformes |
| datos_faltantes | [] | Cantidad del sistema, cantidad física, fecha del conteo |
| Almacén en resumen | Central | Central |

Frente a v6 mejora observada en utilidad de datos faltantes para este caso. La lista coincide con la estructura del ejemplo EX02, un caso de stock muy similar con distinto artículo y depósito. Esto demuestra aplicación del patrón en un caso cercano, no generalización amplia ni entrenamiento permanente. T04 ya se usó para ajustar el laboratorio; no es un caso nuevo independiente. Una ejecución y configuración parcialmente verificada impiden atribuir causalidad o robustez general.

## Estado y siguiente paso
v7: dos respuestas de dos tickets originales, ambas conformes en formato/etiquetas; cobertura 2/10. T02 mantiene lista vacía, T04 pide información útil: mejora no uniforme. Total entre versiones: 40 respuestas registradas sobre doce tickets distintos. [Controles consolidados](../2026-10-15-v7-controls/README.md).

Próximo T06 original, cambiando solo el último Usuario. Sirve para comprobar que la solicitud de reporte planificado mantiene su criterio y obtiene requisitos útiles, sin trasladar preguntas de stock de EX02. Luego T10.
