# v1-roles — primera ejecución registrada

Objetivo: comparar T10 contra v0 cambiando únicamente la distribución de los mensajes.
- Sistema: [system.txt](system.txt), texto de instrucciones de v0 sin cambios.
- Usuario: [user-t10.txt](user-t10.txt), entrada T10 sin etiquetas esperadas.
- [Mensajes preparados](messages-t10.json).
- Sin mensajes Asistente ni ejemplos.
- Mantener Gemini 2.5 Flash Lite (001), temperatura 1, tokens de salida máximos 43690 y streaming activado.
- [Primera respuesta original de T10 y revisión](../../experiments/2026-10-13-t10-v1/README.md). La captura se revisó en el chat, sin publicarla. No reemplazar la salida v0 de T10 en responses.json.
- Se requieren repeticiones para estudiar variación; una única nueva respuesta no demuestra por sí sola un efecto causal de los roles.
- La eventual mejora de datos_faltantes se estudiará separadamente.
