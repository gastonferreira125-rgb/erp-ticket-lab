# T06 con v3: solicitud normal de reporte

Fecha: 14 de octubre de 2026 (America/Montevideo). Salida original copiada por Gastón y contrastada con la captura del chat.

## Evidencia
- [Respuesta original sin cambios](response-original.json).
- [Respuesta en lista](responses.json).
- [Mensajes indicados](messages.json).
- [Evaluación automática](evaluation.json).
- Captura revisada en el chat, sin publicación.
- Se indicó mantener Sistema v3 y cambiar solo Usuario.
- Modelo y parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, salida máxima 43690, streaming activado.
- Prompt actual, valores numéricos y guardado en SAP no se confirman en esta captura del resultado.

## Resultado
Campos/tipos y etiquetas de T06: conformes según el evaluador.
- Reportes: se pide crear un reporte, sin bloqueo de acceso.
- Baja: mejora planificada sin interrupción, según la regla del laboratorio.
- Resumen: fiel; presenta la solicitud sin afirmar que el reporte fue creado.
- Referencia null: no hay número de documento.
- Datos faltantes: formato, campos y filtros son pertinentes para relevar la solicitud. No son un diagnóstico.

## Distinción observada en v3
| Caso | Problema principal | Categoria | Prioridad |
| --- | --- | --- | --- |
| T05 | Falta de permiso para ver un reporte. | Autorizaciones | Media |
| T06 | Solicitud de creación de reporte sin interrupción. | Reportes | Baja |

Esta ejecución no muestra una reclasificación indebida de todos los reportes hacia Autorizaciones.
T06 es un caso nuevo en las ejecuciones, con etiquetas ya definidas en el conjunto; no se afirma que se haya repetido una ejecución previa de T06.

## Límites y próximo paso
Una ejecución por caso no demuestra generalización ni causalidad. Se mantienen versiones y salidas originales separadas.
Próximo caso: T07, integración de pedidos caída con todo el equipo de ventas detenido. Clasificar por proceso e impacto reportados, sin inventar causa técnica.
Después completar los restantes y repetir T02/T10 con v3 como regresión.
