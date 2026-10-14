# v3-category-rule — preparada, sin ejecutar

Base: v2 con Sistema + Usuario y regla de instrucciones dentro del ticket.
Cambio: añade criterio para Autorizaciones frente a Reportes por el problema principal reportado. Las demás reglas se conservan.

- [Sistema completo](system.txt).
- [Usuario T05](user-t05.txt).
- [Mensajes preparados](messages-t05.json).
- Sin bloque Asistente ni ejemplos.
- Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado; verificar valores actuales.
- Próximo paso: repetir T05 y guardar salida original sin reemplazar v2.
- Prueba de regresión prevista: T06, solicitud de creación de reporte sin interrupción.
- No hay salidas reales ni métricas de v3.
- El ajuste usa un caso ya observado; faltan pruebas con casos nuevos.
