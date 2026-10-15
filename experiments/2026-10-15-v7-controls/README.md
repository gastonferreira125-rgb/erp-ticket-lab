# Controles parciales v7 — 15 de octubre de 2026

[responses.json](responses.json) y [evaluation.json](evaluation.json) conservan la primera ronda dirigida de cuatro respuestas T02/T04/T06/T10. [runs.json](runs.json) añade la repetición T02 sin sobrescribir la primera; [responses-latest.json](responses-latest.json) usa la última ejecución por ticket como convención cronológica, no selección de la mejor. [evaluation-latest.json](evaluation-latest.json) evalúa esa vista con evaluate.py.

- Primera ronda: cuatro respuestas, cuatro tickets únicos; formato/etiquetas 4/4. Con repetición T02: cinco ejecuciones sobre los mismos cuatro tickets; todas conformes en formato/etiquetas. Última por ticket: 4/4.
- Cobertura única 4/10. Otros seis casos originales aún sin ejecutar con v7; no son fallos observados. No es ronda completa ni exactitud general.
- EX01/EX02 son demostraciones de entrada preparadas por el tutor, no ejecuciones del modelo.
- Configuración indicada: Sistema v6 y dos pares de ejemplos fijos, cambiando solo último Usuario. Modelo Gemini 2.5 Flash Lite (001) visible en captura previa; payload final y todos los parámetros actuales no verificados.

| Caso | Revisión humana de contenido | Comparación con v6 |
| --- | --- | --- |
| T02 | Lista vacía en dos ejecuciones; segunda omite cierre detenido en resumen | No mejora observada del campo |
| T04 | Pide ambas cantidades/fecha, sin repetir almacén | Mejora observada; caso muy cercano a EX02 |
| T06 | Pide campos/formato, solicitud pendiente | Conserva criterio y requisitos útiles |
| T10 | Identifica instrucciones, sin afirmar corrección; pide incidente | Conserva criterio de instrucciones en datos |

Una salida por caso, casos conocidos para ajuste y configuración parcialmente verificada limitan conclusiones. T04 aplica patrón cercano a EX02; no demuestra generalización amplia. No hay mejora uniforme de datos_faltantes ni una puntuación humana agregada definida de antemano.

Detalle: [T02](../2026-10-15-t02-v7/README.md), [T04](../2026-10-15-t04-v7/README.md), [T06](../2026-10-15-t06-v7/README.md), [T10](../2026-10-15-t10-v7/README.md).

## Revisión de contenido y siguiente fase

Los comentarios cualitativos redactados por el tutor son análisis asistidos por IA pendientes de validación humana, salvo intervención explícita del usuario para un criterio. [Aclaración de trazabilidad](../../docs/EVALUATION.md#quién-revisa-tres-niveles-distintos). No hay puntuación humana agregada.

[T13](../2026-10-15-t13-v7/README.md) ejecutado fuera de estos diez casos: formato/etiquetas 1/1 en su conjunto separado; revisión humana con preguntas útiles y alcance parcialmente redundante. Expectativas guardadas antes de la salida; no enviado como ejemplo. Es una variante cercana a T11 con objeto factura y área Finanzas. Evaluar por separado; si luego se usa para ajustar el prompt, dejará de servir como caso independiente para esa versión. [Segunda T02-v7](../2026-10-15-t02-v7-r2/README.md) registrada, también vacía y omite cierre en resumen. Próximo verificar montaje actual de seis mensajes/parámetros y guardado de plantilla antes de modificar el prompt. Cobertura restante pendiente.
