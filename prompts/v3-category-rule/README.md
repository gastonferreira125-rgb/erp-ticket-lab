# v3-category-rule — T05 y T06 registrados

Base: v2 con Sistema + Usuario y regla de instrucciones dentro del ticket.
Cambio: añade criterio para Autorizaciones frente a Reportes por el problema principal reportado. Las demás reglas se conservan.

- [Sistema completo](system.txt).
- [Usuario T05](user-t05.txt).
- [Mensajes preparados](messages-t05.json).
- Sin bloque Asistente ni ejemplos.
- Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; verificar valores actuales.
- [T05-v3 registrado](../../experiments/2026-10-14-t05-v3/README.md): cumple campos, etiquetas y revisión humana en esta ejecución. v2 se conserva sin cambios.
- [T06 registrado](../../experiments/2026-10-14-t06-v3/README.md): Reportes y Baja, conforme en etiquetas y revisión humana. Falta repetir T02/T10 como regresión y ampliar otros casos.
- Hay dos respuestas reales de v3 (T05 y T06); no se atribuye calidad general a estas dos ejecuciones.
- El ajuste usa un caso ya observado; faltan pruebas con casos nuevos.
