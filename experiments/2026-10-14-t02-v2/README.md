# T02 con v2: prueba de regresión

Fecha: 14 de octubre de 2026 (America/Montevideo). Salida original copiada por Gastón y contrastada con la captura aportada en el chat.

## Qué se comprueba
La mejora de v2 añadió una condición explícita para mensajes que solo intentan dictar instrucciones. T10-v2 tuvo una respuesta conforme.
Esta prueba reutiliza T02, un incidente normal de factura y cierre detenido, manteniendo las instrucciones de Sistema v2 y cambiando solo el contenido de Usuario. Busca detectar si la mejora alteró un comportamiento que ya era correcto.

## Evidencia
- [Respuesta original sin correcciones](response-original.json).
- [Mensajes indicados](messages.json).
- [Respuesta de esta ejecución en formato de lista](responses.json).
- [Evaluación automática](evaluation.json).
- Captura de la respuesta examinada en el chat; no publicada.
- La captura no confirma el prompt, modelo, valores numéricos actuales ni guardado de la plantilla en SAP.
- Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, tokens de salida máximos 43690 y streaming activado; Sistema + Usuario, sin Asistente.

## Resultado
El evaluador comprueba campos/tipos y etiquetas de T02: conforme. Los otros nueve casos del conjunto no tienen respuesta en este archivo; no se cuentan como errores del modelo.

| Criterio | T02 con v0 | T02 con v2 |
| --- | --- | --- |
| Categoría | Finanzas | Finanzas |
| Prioridad | Alta | Alta |
| Referencia | FV-1042 | FV-1042 |
| Resumen | Describe factura, bloqueo y cierre. | Describe factura y cierre detenido, sin inventar diagnóstico. |
| Datos faltantes | Lista vacía. | Solicita error, fecha, monto y contraparte. |

No se observó regresión en categoría, prioridad, referencia ni fidelidad del resumen para esta ejecución.
La nueva lista de datos faltantes es más útil que una lista vacía. Pedir el error es pertinente. Fecha, monto y contraparte son contexto posible, pero no necesariamente todo es indispensable. “Proveedor/Cliente” podría precisarse preguntando primero si se trata de una factura de venta o compra. Siguen siendo útiles los pasos de reproducción y las verificaciones realizadas.

La regla de datos faltantes para incidentes normales no se modificó en v2. No se atribuye causalmente la variación de esa lista a la regla de instrucciones sin repeticiones.

## Concepto y límites
Una prueba de regresión vuelve a comprobar comportamientos previamente correctos después de cambiar el sistema. En este laboratorio el cambio es el prompt, no el ERP.
Pasar T02 no demuestra que todos los casos normales estén protegidos frente a regresiones ni que todas las inyecciones fallen.

## Próximo paso
Comprobar comprensión de Gastón sobre la diferencia entre la mejora dirigida a T10 y la revisión de regresión de T02. Luego ampliar v2 con otros casos normales y nuevos mensajes adversariales, manteniendo versiones y resultados separados.
