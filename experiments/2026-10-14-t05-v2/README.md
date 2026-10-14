# T05 con v2: confusión entre acceso y reporte

Fecha: 14 de octubre de 2026 (America/Montevideo). Salida original copiada por Gastón y contrastada con captura en el chat.

## Evidencia y configuración
- [Respuesta original](response-original.json), sin corregir categoria Reportes.
- [Respuesta en lista](responses.json).
- [Mensajes indicados](messages.json).
- [Evaluación automática](evaluation.json).
- Captura examinada en el chat, sin publicar.
- Se indicó mantener Sistema v2 y cambiar solo Usuario. La captura muestra solo el resultado; no confirma prompt ni parámetros.
- Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, tokens de salida máximos 43690 y streaming activado. Guardado en SAP y valores actuales pendientes de confirmar.

## Criterio funcional del alumno
Antes de ejecutar, Gastón identificó que era un problema de acceso, no del reporte, y que no estaba detenido todo el equipo.
Eso corresponde a Autorizaciones y Media según las reglas y etiquetas de este laboratorio.

## Resultado
El evaluador comprueba campos/tipos: conforme. Coincidencia de etiquetas: no conforme por categoria.
- Reportes: incorrecto para el problema principal reportado de falta de permisos.
- Media: correcto; no se afirma interrupción de todo un equipo.
- Resumen: fiel al incidente, sin causa técnica inventada.
- Referencia null: correcto; no se proporcionó una referencia de documento.
- Datos faltantes: usuario afectado y nombre exacto del reporte son pertinentes. Una revisión más completa podría pedir error exacto y contexto de acceso.

El resumen reconoce la falta de permisos pero la categoría no refleja el criterio acordado. No se afirma conocer el razonamiento interno del modelo. Una hipótesis a probar es que la lista de categorías sin definiciones permite una interpretación por recurso afectado.

## Próximo experimento
v3 mantiene roles, reglas de prioridad y condición para instrucciones dentro del ticket. Añade un criterio general para distinguir Autorizaciones de Reportes por el problema principal reportado.
Está preparada, sin ejecuciones ni resultados.
Primero repetir T05. Después usar T06 (solicitud normal de reporte sin interrupción) como regresión para comprobar que no se reclasifiquen todos los reportes como Autorizaciones.
La regla se ajustó tras observar T05; repetirlo no demuestra generalización. Se necesitarán casos nuevos y repeticiones.
