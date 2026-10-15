# T04 — segundo control v8 — 15 de octubre de 2026

Entrada indicada: “Necesitamos revisar el stock del artículo ART-310 en el almacén central; difiere del conteo físico.”

Se indicó conservar Sistema y ejemplos v8, cambiando solo último Usuario. Fuente: JSON pegado; sin captura/payload completo de esta ejecución. Modelo indicado Gemini 2.5 Flash Lite (001), temperatura 1 y streaming confirmados en pantalla previa; tokens seleccionados no verificados.

[Texto original](raw-response.txt), [respuesta en lista](responses.json), [evaluación ejecutada](evaluation.json).

evaluate.py: campos/tipos y etiquetas Inventario/Media/ART-310 conformes, referencia literal y sin ids desconocidos/duplicados.

Análisis cualitativo asistido por IA, pendiente de validación humana: resumen fiel, conserva almacén/artículo y no inventa causas ni soluciones. Pide cantidades del sistema/conteo y fecha, ausentes y útiles. No vuelve a pedir almacén ni aplica innecesariamente preguntas de transacción fallida. Conserva la lista pertinente de T04-v7; control de regresión conforme en esta ejecución. Caso cercano a EX02, no evidencia de generalización amplia.

v8: 2/4 controles de cierre recibidos, formato/etiquetas 2/2 entre ejecutados, cobertura original 2/10. Total entre versiones: 46 respuestas sobre trece tickets distintos. Quedan T06/T10 sin cambiar v8 y después cierre/comparación, sin v9 automática.
