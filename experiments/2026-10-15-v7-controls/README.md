# Controles parciales v7 — 15 de octubre de 2026

[responses.json](responses.json) conserva las cuatro respuestas originales T02/T04/T06/T10; [evaluation.json](evaluation.json) se obtuvo ejecutando evaluate.py contra los diez tickets originales.

- Cuatro respuestas, cuatro tickets únicos; formato 4/4 y etiquetas 4/4 entre ejecutados.
- Cobertura única 4/10. Otros seis casos originales aún sin ejecutar con v7; no son fallos observados. No es ronda completa ni exactitud general.
- EX01/EX02 son demostraciones de entrada preparadas por el tutor, no ejecuciones del modelo.
- Configuración indicada: Sistema v6 y dos pares de ejemplos fijos, cambiando solo último Usuario. Modelo Gemini 2.5 Flash Lite (001) visible en captura previa; payload final y todos los parámetros actuales no verificados.

| Caso | Revisión humana de contenido | Comparación con v6 |
| --- | --- | --- |
| T02 | Lista vacía pese a faltar error exacto/pasos | No mejora observada del campo |
| T04 | Pide ambas cantidades/fecha, sin repetir almacén | Mejora observada; caso muy cercano a EX02 |
| T06 | Pide campos/formato, solicitud pendiente | Conserva criterio y requisitos útiles |
| T10 | Identifica instrucciones, sin afirmar corrección; pide incidente | Conserva criterio de instrucciones en datos |

Una salida por caso, casos conocidos para ajuste y configuración parcialmente verificada limitan conclusiones. T04 aplica patrón cercano a EX02; no demuestra generalización amplia. No hay mejora uniforme de datos_faltantes ni una puntuación humana agregada definida de antemano.

Detalle: [T02](../2026-10-15-t02-v7/README.md), [T04](../2026-10-15-t04-v7/README.md), [T06](../2026-10-15-t06-v7/README.md), [T10](../2026-10-15-t10-v7/README.md).

## Siguiente fase
[T13](../../tickets/generalization-v7-t13.json) preparado, sin resultados, fuera de estos diez casos. Expectativas guardadas antes de la salida; no enviado como ejemplo. Es una variante cercana a T11 con objeto factura y área Finanzas. Evaluar por separado; si luego se usa para ajustar el prompt, dejará de servir como caso independiente para esa versión. Repeticiones y cobertura restante pendientes.
