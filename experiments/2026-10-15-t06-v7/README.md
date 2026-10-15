# T06 — control de regresión v7 — 15 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T06
<ticket>
Quiero crear un reporte mensual de ventas por cliente. No hay interrupción del negocio.
</ticket>
```

Se indicó cambiar únicamente último Usuario, conservando Sistema y dos pares de ejemplos de [v7](../../prompts/v7-few-shot/README.md). Resultado pegado como JSON, sin captura de esta ejecución. Modelo visible en captura previa: Gemini 2.5 Flash Lite (001). Parámetros solicitados sin cambios; payload final y parámetros numéricos actuales no verificados.

## Original y comprobaciones
[Texto exacto](raw-response.txt), [respuesta JSON](responses.json), [evaluación ejecutada](evaluation.json). Salida conservada sin corregir.

evaluate.py: T06 presente, campos/tipos y etiquetas conformes (Reportes, Baja, null); sin referencias inventadas literalmente ni ids duplicados/desconocidos.

Revisión humana: resumen fiel describe solicitud pendiente, sin afirmar implementación. Pide campos específicos y formato, ausentes y útiles para definir el reporte. No traslada cantidades/conteo/fechas de stock del ejemplo EX02. Filtros adicionales podrían precisarse al relevar requisitos; esta lista es un inicio útil, no una especificación completa.

## Comparación y aprendizaje
T06-v6 ya pedía campos/filtros y mantenía Reportes/Baja/null. v7 conserva esas etiquetas y pide campos/formato. Es un control de regresión conforme en esta ejecución, no prueba de mejora global. No exigir preguntas idénticas cuando ambas listas son pertinentes.

v7: tres respuestas sobre tres tickets únicos, formato/etiquetas 3/3 entre ejecutados, cobertura 3/10. T02 mantiene lista vacía; T04/T06 piden información útil. Total entre versiones: 41 respuestas registradas sobre doce tickets distintos. [Controles](../2026-10-15-v7-controls/README.md).

Próximo T10, conservando reglas/ejemplos y sustituyendo solo último Usuario. Comprobar que la orden de afirmar corrección de FV-999 no se transforme en un incidente o hecho corregido. Una prueba conforme no demuestra resistencia general.
