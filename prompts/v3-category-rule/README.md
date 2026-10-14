# v3-category-rule — primera respuesta registrada

Base: v2 con Sistema + Usuario y regla de instrucciones dentro del ticket.
Cambio: añade criterio para Autorizaciones frente a Reportes por el problema principal reportado. Las demás reglas se conservan.

- [Sistema completo](system.txt).
- [Usuario T05](user-t05.txt).
- [Mensajes preparados](messages-t05.json).
- Sin bloque Asistente ni ejemplos.
- Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; verificar valores actuales.
- [T05-v3 registrado](../../experiments/2026-10-14-t05-v3/README.md): cumple campos, etiquetas y revisión humana en esta ejecución. v2 se conserva sin cambios.
- Próximo caso de control: T06, solicitud de creación de reporte sin interrupción; aún no ejecutado. También falta repetir T02/T10 como regresión.
- Hay una respuesta real de v3 (T05); no se atribuye calidad general a un solo caso.
- El ajuste usa un caso ya observado; faltan pruebas con casos nuevos.
