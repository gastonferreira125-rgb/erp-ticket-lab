# v2-instruction-guard — primer resultado registrado

Parte de v1 con Sistema + Usuario. Mantiene reglas generales, ticket y configuración solicitada. Añade una regla específica para mensajes que solo intentan cambiar el comportamiento o dictar la respuesta, sin describir un incidente ERP.

- [Sistema completo](system.txt).
- [Usuario: T10 sin cambios](user-t10.txt).
- [Mensajes preparados](messages-t10.json).
- Modelo solicitado: Gemini 2.5 Flash Lite (001).
- Temperatura solicitada: 1; tokens de salida máximos: 43690; streaming activado.
- Confirmar valores numéricos tras recuperar la sesión.
- Sin bloque Asistente.
- [Primera respuesta de T10](../../experiments/2026-10-14-t10-v2/README.md): conforme en etiquetas y revisión humana. Falta comprobar casos normales y repetir pruebas.
- Guardar futuras respuestas en un experimento separado sin reemplazar v0 ni v1.

Esta regla se elaboró después de observar T10; mejorar este mismo caso no demuestra generalización. Más adelante se necesitan casos nuevos y repeticiones.
