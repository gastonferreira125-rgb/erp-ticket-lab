# T06 — tercer control v8 — 15 de octubre de 2026

Entrada indicada: “Quiero crear un reporte mensual de ventas por cliente. No hay interrupción del negocio.”

Se indicó conservar Sistema/ejemplos v8 y cambiar solo último Usuario. Fuente: JSON pegado, sin captura/payload completo de esta ejecución. Modelo indicado Gemini 2.5 Flash Lite (001); temperatura 1/streaming visibles en pantalla previa, máximo de tokens seleccionado no verificado.

[Texto original](raw-response.txt), [respuesta en lista](responses.json), [evaluación ejecutada](evaluation.json). Salida sin corregir.

evaluate.py: formato y Reportes/Baja/null conformes; sin ids desconocidos/duplicados ni referencias ausentes literalmente.

Análisis cualitativo asistido por IA, pendiente de validación humana: resumen fiel de solicitud pendiente, sin implementación inventada. Pide campos y filtros, ausentes y útiles para definir requisitos; no traslada preguntas de error/pasos de transacción ni de conteo de stock. v7 pedía campos/formato; ambas listas son pertinentes y no se exige identidad textual. Control de regresión conforme en esta ejecución; no es una especificación completa del reporte.

v8: 3/4 controles de cierre recibidos, formato/etiquetas 3/3 entre ejecutados, cobertura original 3/10. Total entre versiones: 47 respuestas sobre trece tickets distintos.

Solo queda T10 sin cambiar reglas/ejemplos/parámetros. Después consolidar, comparar mismos cuatro casos con v7 y cerrar, sin v9 automática; pendientes posteriores separados.
