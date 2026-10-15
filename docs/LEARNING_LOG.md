# Registro de aprendizaje

## 12 de octubre de 2026
Objetivo: acceder al sistema de práctica AIG02 y entender SAP AI Launchpad, Generative AI Hub, modelo y prompt.

Concepto trabajado: clasificar un ticket no determina su causa. Un mensaje incompleto sobre un pago a proveedor permite reconocer el proceso, pero no diagnosticar el error.

Acceso al entorno: pendiente de confirmar. Ejecuciones en modelos: pendientes.

Método de cada sesión: teoría en español con términos en inglés, ejemplo ERP, acción práctica y comprobación de comprensión antes de continuar.

## 13 de octubre de 2026
- Objetivo: retomar el laboratorio y ejecutar T01.
- Acceso a SAP AI Launchpad: confirmado por captura del editor.
- Modelo confirmado por captura posterior: Gemini 2.5 Flash Lite (001). Configuración actual capturada después de T01: temperatura 1; tokens de salida máximos 43690; streaming activado.
- Conceptos explicados: prompt, JSON y clasificación frente a diagnóstico.
- Acción realizada: primera ejecución manual de T01 en el bloque Usuario.
- Evidencia: respuesta original y captura del panel de respuesta aportadas por Gastón.
- Validación: 1 de 10 casos ejecutados; T01 cumple las comprobaciones del evaluador y coincide con las etiquetas de referencia.
- Revisión humana: resumen fiel, sin diagnóstico inventado; datos faltantes útiles, aunque “detalles del pago” es amplio.
- Comprobación de aprendizaje: Gastón identificó correctamente la condición de prioridad Alta del laboratorio (proceso detenido para todo un equipo).
- Próximo paso: ejecutar T02 con la misma configuración, cambiando únicamente id y texto.
- [Registro del experimento](../experiments/2026-10-13-t01/README.md).

## 13 de octubre de 2026 — T02
- Segunda ejecución manual observada mediante captura.
- Campos legibles: Finanzas, Alta, FV-1042 y datos_faltantes vacío.
- Aprendizaje: una salida puede cumplir tipos y etiquetas y aun así ser insuficiente para investigar un incidente.
- Observación: faltan error exacto, pasos de reproducción y verificaciones realizadas.
- Evidencia: captura del resultado; el resumen está cortado en el borde derecho.
- Salida original completa recibida posteriormente, guardada sin correcciones y añadida a responses.json. Evaluador: T01 y T02 cumplen las comprobaciones y etiquetas; cobertura 2 de 10.
- Pregunta de Gastón: por qué no se usan Sistema y Asistente. Concepto explicado: reglas generales en Sistema, ticket en Usuario, ejemplos/historial en Asistente. La versión inicial contiene todo en Usuario como referencia.
- Próximo paso: T10 con v0; luego comparar una versión que cambie únicamente la distribución de roles.
- [Registro de T02](../experiments/2026-10-13-t02/README.md).

## 13 de octubre de 2026 — T10 con v0
- Salida original y captura recibidas y guardadas.
- Formato: cumple las comprobaciones del evaluador.
- Etiquetas: falla prioridad (Baja, mientras la referencia y regla indican Media).
- Revisión humana: resume una orden de inventar una corrección como hecho reportado y pregunta por una corrección realizada sin evidencia.
- Conceptos explicados: instrucciones dentro de datos (prompt injection), revisión por campo y separación de roles.
- Evaluación acumulada: 3 de 10 casos; 3 salidas pasan controles de formato; 2 coinciden con etiquetas.
- v1-roles preparada sin ejecuciones; mismas reglas, Sistema + Usuario, sin Asistente.
- Próximo paso: repetir T10 con v1 y guardar el resultado por separado.
- [Experimento T10-v0](../experiments/2026-10-13-t10-v0/README.md).

## 13 de octubre de 2026 — recuperación de sesión y T10-v1
- Gastón informó pérdida del editor por expiración de sesión; se reconstruyeron Sistema y Usuario.
- Dos bloques y modelo confirmados visualmente. Temperatura y tokens solicitados como antes, sin etiquetas numéricas confirmadas en la sesión restaurada.
- Respuesta original de T10-v1 recibida: Otros, Baja, FV-999, resumen de corrección como hecho y datos_faltantes vacío.
- Evaluación automática: formato correcto; etiquetas incorrectas por prioridad y referencia.
- Aprendizaje: separar roles no garantiza cumplir reglas; presencia literal de un identificador no demuestra que sea una referencia válida al incidente.
- Guardado de plantilla en SAP pendiente de confirmar.
- Capturas revisadas en el chat; su publicación fue bloqueada por revisión automática. Se conserva la salida textual del modelo.
- Próximo paso: v2 con regla condicional explícita, sin cambiar modelo ni parámetros; preparada, sin ejecutar.
- [Resultado v1](../experiments/2026-10-13-t10-v1/README.md).

## 14 de octubre de 2026 — T10 con v2
- Respuesta original recibida y contrastada con captura.
- Salida: Otros, Media, referencia null; resumen identifica instrucciones para alterar la respuesta.
- datos_faltantes solicita la descripción del incidente, sin presuponer una corrección.
- Evaluador: campos/tipos y etiquetas conformes para T10; revisión humana conforme en esta ejecución.
- Resultado guardado por separado de v0 y v1; cinco ejecuciones totales sobre tres tickets distintos.
- Limitación: caso usado para ajustar el prompt; una ejecución por versión y parámetros actuales no reconfirmados no demuestran causalidad ni robustez general.
- Concepto del próximo paso: prueba de regresión, comprobar que una mejora no perjudique casos normales.
- Próximo paso: T02 con Sistema v2 sin cambios; revisar también datos_faltantes.
- Guardado en SAP y valores actuales: pendientes de confirmar; versiones y respuestas conservadas en GitHub.
- [Resultado T10-v2](../experiments/2026-10-14-t10-v2/README.md).

## 14 de octubre de 2026 — T02-v2 y explicación de regresión
- Gastón pregunta cuál fue la mejora y qué significa regression test en este caso.
- Mejora dirigida a T10: condición explícita para no transformar instrucciones del ticket en hechos reportados.
- Prueba de regresión: volver a ejecutar T02 después del cambio del prompt para comprobar que conserva la clasificación y el resumen correctos.
- Respuesta T02-v2 guardada sin correcciones; cumple controles de formato y etiquetas.
- Revisión humana: resumen fiel; lista de datos faltantes más útil que la lista vacía de v0.
- No se afirma que la regla de instrucciones haya causado la nueva lista; la regla de datos faltantes para incidentes normales no se modificó.
- Seis ejecuciones totales sobre tres tickets distintos; resultados de v0, v1 y v2 separados.
- Guardado en SAP y parámetros actuales pendientes de confirmar.
- [Prueba de regresión T02-v2](../experiments/2026-10-14-t02-v2/README.md).

## 14 de octubre de 2026 — T05-v2 y criterio de categoría
- Antes de ejecutar, Gastón identificó correctamente problema de acceso, no del reporte, y ausencia de bloqueo de todo el equipo.
- Respuesta modelo: Reportes, Media, resumen fiel, referencia null, usuario y nombre del reporte como datos faltantes.
- Evaluador: formato conforme; categoría incorrecta frente a Autorizaciones esperada.
- Aprendizaje: distinguir el recurso mencionado del problema principal reportado; no diagnosticar la causa técnica del permiso faltante.
- v3 preparada con regla de categoría, sin resultados. Mantiene prioridad y regla de instrucciones de v2.
- Próximo paso: T05-v3; luego T06 como regresión.
- Siete ejecuciones sobre cuatro tickets distintos; seis casos del conjunto aún no ejecutados.
- [Fallo T05-v2](../experiments/2026-10-14-t05-v2/README.md).

## 14 de octubre de 2026 — T05-v3
- Salida original y captura recibidas. Autorizaciones, Media, referencia null, resumen fiel y datos faltantes pertinentes.
- Evaluador: campos/tipos y etiquetas conformes para T05.
- Comparación: v2 había devuelto Reportes; v3 coincide con el criterio funcional previamente expresado por Gastón.
- Límite: caso usado para ajustar el prompt; una ejecución no demuestra generalización.
- Ocho ejecuciones totales sobre cuatro tickets distintos; seis casos del conjunto todavía no ejecutados.
- Próximo caso: T06, solicitud de reporte sin interrupción. Luego repetir casos previos como regresión.
- [Resultado T05-v3](../experiments/2026-10-14-t05-v3/README.md).

## 14 de octubre de 2026 — T06-v3
- Respuesta original y captura recibidas: Reportes, Baja, resumen de solicitud, referencia null, formato/campos/filtros como datos faltantes.
- Evaluador: campos/tipos y etiquetas conformes.
- Revisión humana: reconoce solicitud sin afirmar que ya fue implementada.
- Comparación conceptual con T05: recurso reporte puede corresponder a Autorizaciones por permiso, o a Reportes por creación/modificación.
- T06 es un caso nuevo ejecutado con v3; no se repitió una ejecución previa de T06.
- Nueve ejecuciones sobre cinco tickets distintos; cinco casos del conjunto todavía no ejecutados.
- Próximo paso: T07-v3, luego completar casos y repetir T02/T10 como regresión.
- [Resultado T06-v3](../experiments/2026-10-14-t06-v3/README.md).

## 14 de octubre de 2026 — ronda v3 completa
- T07: Ventas en lugar de Integraciones; área afectada y problema principal no son equivalentes.
- T03: referencia null aunque OV-2099 aparece en el resumen.
- T04: referencia null frente a ART-310 esperado; ambigüedad del esquema, pues el identificador corresponde a un artículo.
- T08: Compras, Media y PC-778 conformes; extraer una referencia aquí no corrige por sí solo T03.
- T09: Inventario, Baja y null conformes; lista vacía válida, pero conviene definir alcance para preparar documentación y capacitación.
- T01-v3: conserva etiquetas de v0 e incluye pasos para reproducir como información útil.
- T02-v3: conserva etiquetas previas; "afectando" pierde precisión frente a bloqueo del equipo y cierre detenido.
- T10-v3: Otros, Media y null; identifica instrucciones sin afirmar corrección. Conserva comportamiento conforme de v2 en esta ejecución.
- Conceptos: extracción de información (information extraction), esquema de salida (output schema), pasos para reproducir (steps to reproduce) y prueba de regresión (regression test).
- Evaluador ejecutado sobre diez respuestas originales de v3: cobertura 10/10, formato 10/10, coincidencia completa 7/10, categorías 9/10, prioridades 10/10, referencias 8/10; cero referencias ausentes literalmente y sin IDs duplicados/desconocidos.
- Acumulado: 17 ejecuciones entre versiones, diez tickets distintos. No mezclar versiones para calcular métricas. Una ronda pequeña y casos usados para ajustes no prueban exactitud en producción ni generalización.
- Gastón autorizó explícitamente guardar tickets y evaluaciones en este repositorio. Capturas revisadas, sin publicar imágenes. Registro de T04 recuperado tras vencimientos iniciales de revisión automática.
- Próximo paso: nueva versión para categoría Integraciones, sin cambiar a la vez las reglas de referencia. Después alinear contrato, prompt y conjunto esperado; repetir y añadir casos nuevos.
- [Ronda consolidada](../experiments/2026-10-14-v3-round/README.md).

## 14 de octubre de 2026 — primera ejecución v4
- Regla añadida únicamente para categorías de integración; no cambia la extracción de referencias.
- T07 devuelve Integraciones, Alta y null, frente a Ventas observado con v3. Formato y etiquetas conformes según evaluate.py.
- Captura coincide con el JSON original, conservado sin correcciones. Resumen fiel pero menos preciso sobre el bloqueo total; datos faltantes útiles.
- 18 ejecuciones acumuladas; v4 cubre solo T07 (1/1 conforme entre ejecutados, cobertura 1/10). v3 conserva 7/10. No construir una métrica mezclando versiones.
- Una prueba dirigida al mismo caso usado para ajustar el prompt no demuestra generalización ni causalidad.
- Próximo paso: T08 como control de regresión de Compras con v4; luego otros controles y casos nuevos.
- [Experimento T07-v4](../experiments/2026-10-14-t07-v4/README.md).

## 14 de octubre de 2026 — T08-v4, control de regresión
- T08 conserva Compras, Media y PC-778. evaluate.py confirma campos/tipos y etiquetas; captura coincide con JSON original.
- Fechas original y deseada son pertinentes, pero registrada actualmente y correcta esperada serían términos más precisos. Revisión humana independiente del acierto de etiquetas.
- v4 tiene dos casos conformes entre ejecutados, cobertura 2/10. v3 mantiene 7/10. Acumulado entre versiones: 19 ejecuciones.
- Una regresión superada no garantiza ausencia de fallos en el resto del conjunto. Siguiente: T10 con v4, luego caso nuevo de integración con impacto parcial.
- [T08-v4](../experiments/2026-10-14-t08-v4/README.md).

## 14 de octubre de 2026 — T10-v4 y preparación de generalización
- T10 conserva Otros, Media, null y un resumen que identifica instrucciones sin afirmar una corrección. evaluate.py confirma campos/tipos y etiquetas; captura coincide con JSON original.
- v4 cubre 3/10 del conjunto original, 3/3 conformes entre ejecutados. v3 conserva 7/10. Acumulado: 20 ejecuciones sobre diez tickets distintos.
- Preparado T11: pedidos que no llegan al ERP de forma parcial mientras el equipo sigue trabajando; etiquetas de referencia registradas antes de observar salida del modelo. No usado para ajustar el prompt v4 y todavía sin ejecutar.
- Concepto: generalización (generalization), evaluar entradas nuevas; un solo caso adicional no demuestra robustez general. Mantener versiones y conjuntos separados.
- [T10-v4](../experiments/2026-10-14-t10-v4/README.md), [caso complementario T11](../tickets/generalization-v4.json).

## 14 de octubre de 2026 — T11-v4, primer caso nuevo
- T11 devuelve Integraciones, Media y null, coincidiendo con valores esperados guardados antes de la ejecución. Captura y JSON coinciden; evaluate.py aplicado al conjunto complementario confirma formato y etiquetas (1/1).
- Categoría por intercambio entre sistemas; prioridad por impacto parcial, conservando Media aunque la integración falle. Resumen fiel; pares de ejemplos que entran/no entran son datos útiles para comparar.
- v4: 3/3 entre casos ejecutados del conjunto original (cobertura 3/10) y 1/1 caso complementario. No mezclar conjuntos con v3. Total entre versiones: 21 ejecuciones, once tickets distintos.
- Generalización: observación de un caso nuevo sin cambiar antes el prompt para ese caso. No demuestra robustez general.
- T12 preparado sin respuesta para contrastar mención de tienda frente a problema en pedido cargado manualmente; valores esperados registrados antes de generación. Próximo paso: ejecutar con v4.
- [Resultado T11](../experiments/2026-10-14-t11-v4/README.md), [T12 preparado](../tickets/generalization-v4-t12.json).

## 14 de octubre de 2026 — T12-v4 y preparación de v5
- T12 devuelve Ventas y Media conformes; referencia null frente a OV-3301 esperado. evaluate.py aplicado al conjunto complementario confirma formato correcto y falla de etiquetas. Captura coincide con respuesta original.
- La mención de tienda no desvió la categoría, pero el identificador aparece en resumen/datos_faltantes y falta en referencia_documento. Patrón similar a T03-v3, sin atribuir causa interna al modelo.
- v4: 3/3 conformes entre ejecutados del conjunto original (cobertura 3/10) y 1/2 complementarios conformes. Total entre versiones: 22 ejecuciones, doce tickets distintos. v3 conserva 7/10.
- v5 preparada, sin ejecutar: extracción literal de identificadores del incidente y alcance explícito del campo para documentos/códigos de artículo. Misma estructura; descripción de esquema versionada, sin cambiar retrospectivamente etiquetas o respuestas.
- Próximo: repetir T12 con v5, después T03/T04 y controles T10/T07. T12 ahora se usa para ajustar v5 y deja de ser una prueba independiente de generalización para esa versión.
- [T12-v4](../experiments/2026-10-14-t12-v4/README.md), [v5 preparada](../prompts/v5-reference-rule/README.md).

## 14 de octubre de 2026 — primera ejecución T12-v5
- T12 ahora devuelve OV-3301 en referencia_documento y coincide con Ventas/Media. evaluate.py sobre conjunto complementario: formato y etiquetas 1/1. Captura coincide con original.
- Revisión humana: el resumen vincula carga manual a dirección cuando la entrada la vincula al pedido. datos_faltantes vacío omite la dirección correcta, útil para atender la solicitud y pedida en v4.
- Extracción mejor en esta observación; contenido no mejora uniformemente. No atribuir causalidad a una sola ejecución por versión ni a parámetros no reconfirmados.
- v5 solo tiene este caso complementario (1/1 conforme), usado para ajustar el prompt. Todavía sin casos del conjunto original; mantener métricas separadas de v4/v3.
- Acumulado: 23 ejecuciones sobre doce tickets distintos. Próximo: T03, T04 y controles T10/T07 con v5 sin cambios.
- [T12-v5](../experiments/2026-10-14-t12-v5/README.md).

## 14 de octubre de 2026 — T03-v5
- T03 devuelve Ventas, Media y OV-2099. evaluate.py confirma campos/tipos y etiquetas; captura coincide con original.
- Referencia null en v3, OV-2099 en v5. La comparación cruza dos cambios de reglas (v4 y v5); no demuestra causalidad de una regla aislada. Caso usado para motivar el ajuste, no nuevo independiente.
- Resumen fiel, pero omite alcance a un pedido. datos_faltantes vacío omite dirección correcta, patrón también observado en T12-v5.
- v5: 1/1 conforme entre ejecutados del conjunto original (cobertura 1/10), y 1/1 complementario. Total entre versiones: 24 ejecuciones sobre doce tickets distintos.
- Próximo: T04 y controles T10/T07 sin modificar v5. Mejora de datos faltantes pendiente para otra versión.
- [T03-v5](../experiments/2026-10-14-t03-v5/README.md).

## 14 de octubre de 2026 — T04-v5
- T04 devuelve Inventario, Media y ART-310. evaluate.py confirma formato y etiquetas; captura coincide con original. Contrato ahora explícito para códigos de artículo, alineado con conjunto original sin modificarlo.
- Resumen fiel pero omite almacén. datos_faltantes solicita almacén pese a la entrada "almacén central"; si se requiere código, debe pedirlo específicamente. Fecha de conteo útil; falta stock del sistema y cantidad física para dimensionar diferencia.
- v5: 2/2 conformes entre ejecutados del conjunto original (cobertura 2/10), y 1/1 complementario. Total entre versiones: 25 ejecuciones sobre doce tickets distintos.
- Aclaración del contrato y extracción observada no prueban robustez ni causalidad del modelo. Datos faltantes necesitan usar lo ya informado y solicitar información útil restante.
- Próximo: T10 y T07 sin modificar v5; mejora de datos faltantes queda separada.
- [T04-v5](../experiments/2026-10-14-t04-v5/README.md).

## 14 de octubre de 2026 — recuperación de sesión y T10-v5
- Tras cierre del Launchpad, se recuperó Sistema v5 desde GitHub y se volvió a entregar Usuario T10 y configuración solicitada. Captura no confirma parámetros completos ni guardado SAP.
- T10 devuelve Otros, Media, referencia null y resumen de instrucciones, sin afirmar corrección. evaluate.py confirma formato y etiquetas; captura coincide con original.
- Regresión conforme en este caso después de aclarar extracción: FV-999 dentro de una orden no se convierte en referencia de incidente. No demuestra resistencia general ni consistencia entre repeticiones.
- v5: 3/3 conformes entre ejecutados del conjunto original (T03/T04/T10, cobertura 3/10) y 1/1 complementario (T12). Total entre versiones: 26 ejecuciones sobre doce tickets distintos.
- Próximo: T07 con v5 sin cambios y completar cobertura. Hallazgos de datos faltantes pendientes para ajuste posterior.
- [T10-v5](../experiments/2026-10-14-t10-v5/README.md).

## 14 de octubre de 2026 — T07-v5 y cierre de controles dirigidos
- T07 conserva Integraciones, Alta y null de v4. evaluate.py confirma campos/tipos y etiquetas. Fuente: JSON pegado, sin captura en este mensaje.
- Resumen refleja caída y falta de ingreso de pedidos, omite detención total del equipo. Datos faltantes útiles: tienda, error y momento de inicio.
- v5: 4/4 conformes entre ejecutados del conjunto original (cobertura 4/10) y 1/1 complementario. Total entre versiones: 27 ejecuciones sobre doce tickets distintos.
- Controles T07/T10 conformes en estas observaciones; no garantizan ausencia de regresiones fuera de esos casos.
- Mantener v5 sin cambios para T01/T02/T05/T06/T08/T09 y consolidar diez casos. Mejoras de datos faltantes y resumen pendientes para otra versión.
- [T07-v5](../experiments/2026-10-14-t07-v5/README.md).

## 14 de octubre de 2026 — T01-v5
- Finanzas, Media y null conformes. evaluate.py confirma campos/tipos y etiquetas. Fuente: JSON pegado, sin captura.
- Resumen fiel e información faltante útil pero amplia ("etc."); faltan pasos de reproducción pedidos en v3. Registrar variación de contenido sin atribuirla causalmente al ajuste de referencias.
- v5: 5/5 conformes entre ejecutados del conjunto original (cobertura 5/10) y 1/1 complementario. Total entre versiones: 28 ejecuciones sobre doce tickets distintos.
- Próximo: T02/T05/T06/T08/T09 sin modificar v5, empezando por T02. Hallazgos de información faltante pendientes para otra versión.
- [T01-v5](../experiments/2026-10-14-t01-v5/README.md).

## 14 de octubre de 2026 — T02-v5
- Finanzas, Alta y FV-1042 conformes. evaluate.py confirma formato y etiquetas. Fuente: JSON pegado, sin captura.
- Resumen pierde bloqueo de todo el equipo y cierre detenido; datos_faltantes vacío omite error exacto y reproducción. Registrar deterioro cualitativo frente a v3 sin inferir causalidad de una regla específica.
- Aprendizaje: coincidencia de etiquetas y utilidad para atender el ticket se evalúan por separado. La ronda puede mejorar etiquetas sin mejorar uniformemente otros campos.
- v5: 6/6 conformes entre ejecutados del conjunto original (cobertura 6/10), y 1/1 complementario. Total entre versiones: 29 ejecuciones sobre doce tickets distintos.
- Próximo: T05/T06/T08/T09 sin modificar v5. Después consolidar y preparar mejora de impacto en resumen e información faltante.
- [T02-v5](../experiments/2026-10-14-t02-v5/README.md).

## 14 de octubre de 2026 — T05-v5
- Autorizaciones, Media y null conformes. evaluate.py confirma formato y etiquetas. Fuente: JSON pegado, sin captura.
- Reconoce problema de permisos pese al recurso reporte de compras; resumen fiel y datos faltantes pertinentes (usuario y reporte exacto), sin diagnosticar causa técnica.
- Conserva categoría de v3 en esta observación; caso usado para ajustar v3, no nuevo independiente.
- v5: 7/7 conformes entre ejecutados del conjunto original (cobertura 7/10), y 1/1 complementario. Total entre versiones: 30 ejecuciones sobre doce tickets distintos.
- Próximo: T06/T08/T09 sin modificar v5, empezando por solicitud de reporte T06.
- [T05-v5](../experiments/2026-10-14-t05-v5/README.md).

## 14 de octubre de 2026 — T06-v5
- Reportes, Baja y null conformes; evaluate.py confirma formato y etiquetas. Fuente: JSON pegado, sin captura.
- Resumen reconoce solicitud pendiente sin afirmar implementación. Pide requisitos pertinentes (campos/filtros/ordenamiento/formato), conserva datos útiles para definir un reporte.
- Contraste T05/T06: problema de permisos frente a creación de reporte. T06 conserva etiquetas de v3 en esta ejecución.
- v5: 8/8 conformes entre ejecutados del conjunto original (cobertura 8/10), y 1/1 complementario. Total entre versiones: 31 ejecuciones sobre doce tickets distintos.
- Próximo: T08/T09 sin modificar v5; luego consolidar ronda completa y revisión humana.
- [T06-v5](../experiments/2026-10-14-t06-v5/README.md).

## 14 de octubre de 2026 — T08-v5
- Compras, Media y PC-778 conformes. evaluate.py confirma formato y etiquetas. Fuente: JSON pegado, sin captura.
- Resumen fiel. datos_faltantes "Procedimiento a revisar" es poco concreto; faltan fecha registrada y fecha correcta esperada, pedidas en versiones previas. Registrar deterioro de utilidad sin causalidad demostrada.
- v5: 9/9 conformes entre ejecutados del conjunto original (cobertura 9/10), y 1/1 complementario. Total entre versiones: 32 ejecuciones sobre doce tickets distintos.
- Resta T09 con v5 sin cambios; luego consolidar diez salidas originales, métricas separadas y revisión humana.
- [T08-v5](../experiments/2026-10-14-t08-v5/README.md).

## 14 de octubre de 2026 — T09 y ronda v5 completa
- T09: Inventario, Baja, null; resumen de solicitud pendiente y datos_faltantes vacío. Fuente: JSON pegado, sin captura. Falta alcance para preparar documentación/capacitación; lista vacía también observada en v3.
- Evaluación consolidada ejecutada sobre respuestas originales v3/v5 y mismo tickets.json: formato 10/10 ambas; etiquetas completas 7/10 v3 y 10/10 v5. Categoría 9/10→10/10; prioridad 10/10→10/10; referencia 8/10→10/10. No se modificaron etiquetas históricas. T12 complementario aparte.
- Revisión humana comparativa: v5 mejora etiquetas y extracción, pero T02 pierde impacto/error, T03 pierde dirección correcta, T04 pide almacén ya dado y omite cantidades, T08 omite fechas y pide procedimiento vago. Otros casos mantienen datos útiles; no se calculó calidad humana global con rúbrica previa.
- Límites: casos usados para ajustes, una respuesta por versión, parámetros no reconfirmados totalmente, restauración de sesión y ambigüedad aclarada T04. No demostrar causalidad ni exactitud general de producción.
- Total: 33 ejecuciones entre versiones, doce tickets distintos. v5 congelada con ronda original completa 10/10.
- v6 preparada, sin resultados: solo calidad de datos_faltantes (usar información aportada, pedir datos ausentes útiles/concretos, reservar lista vacía cuando baste para siguiente paso). Resumen se ajustará aparte.
- Próximo: T02-v6 y controles T04/T06/T10; luego casos nuevos/repeticiones.
- [Ronda v5](../experiments/2026-10-14-v5-round/README.md), [v6 preparada](../prompts/v6-missing-data-rule/README.md).

## 14 de octubre de 2026 — primera salida bajo procedimiento v6, T02
- Finanzas, Alta y FV-1042 conformes según evaluate.py. Fuente: JSON pegado, sin captura.
- datos_faltantes sigue vacío: objetivo dirigido no cumplido en esta respuesta, ya que faltan error exacto y reproducción. Resumen conserva cierre detenido; no atribuir causalidad al cambio de regla.
- No se verificó aplicación del bloque v6 en Sistema SAP; el archivo GitHub previsto sí contiene la regla. No asumir que faltó copiar ni que el modelo incumple de forma general.
- Versión indicada v6: una salida recibida, etiquetas 1/1 entre ejecutados, cobertura 1/10. Revisión humana del objetivo desfavorable; v5 permanece 10/10 aparte.
- Total entre versiones: 34 ejecuciones sobre doce tickets distintos. Próximo: captura del final de Sistema con bloque de calidad, luego repetición/control T02 y T04/T06/T10 según verificación. No añadir regla nueva todavía.
- [T02-v6](../experiments/2026-10-14-t02-v6/README.md).

## 14 de octubre de 2026 — verificación textual de Sistema v6
- Usuario pegó Sistema completo. Comparación con system.txt guardado: coincide tras normalizar saltos de línea/extremos; bloque de calidad completo.
- Fuente textual, sin captura ni payload retrospectivo. Confirma contenido aportado, no todos los parámetros de la primera ejecución. No cambia el conteo: siguen 34 ejecuciones, doce tickets distintos.
- Mantener v6 y repetir T02 una vez sin cambiar entrada/configuración solicitada; conservar ejecución aparte para observar consistencia o variación antes de otro ajuste.
- [Verificación](../experiments/2026-10-14-t02-v6/system-confirmation.md).

## 14 de octubre de 2026 — T02-v6 repetición 2
- Sistema/Usuario y configuración solicitada sin cambios; previamente se comparó el texto Sistema aportado con v6. Fuente del resultado: JSON pegado, sin captura ni payload que confirme parámetros.
- evaluate.py: formato y etiquetas conformes. datos_faltantes sigue vacío; objetivo de contenido no cumplido en segunda observación. Resumen cambió, mantiene cierre detenido y omite bloqueo total del equipo.
- Dos ejecuciones T02 conservan lista vacía; no demostrar incumplimiento universal, determinismo o causa interna. Guardado separado, primera salida intacta.
- v6: dos ejecuciones de un ticket, cobertura única 1/10. Total entre versiones: 35 ejecuciones, doce tickets distintos. No contar una repetición como nuevo ticket.
- Próximo T04 sin cambiar v6 para evaluar dato ya informado y concreción; luego T06/T10 según resultados.
- [Repetición 2](../experiments/2026-10-14-t02-v6-r2/README.md).

## 14 de octubre de 2026 — T04-v6
- Inventario, Media y ART-310 conformes según evaluate.py. Fuente: JSON pegado, sin captura.
- Resumen fiel conserva artículo y almacén central. datos_faltantes vacío: objetivo no cumplido; faltan cantidades del sistema/conteo y fecha de conteo útil.
- Frente a v5, deja de pedir almacén ya informado pero elimina toda información faltante. No es mejora suficiente del campo; no atribuir causalidad a variación del resumen.
- v6: tres ejecuciones sobre dos tickets, todas con etiquetas correctas y listas vacías. Cobertura única 2/10, no 3/10. Total entre versiones: 36 ejecuciones sobre doce tickets distintos.
- Próximo: T06 y luego T10 con v6 sin cambios antes de decidir otro ajuste.
- [T04-v6](../experiments/2026-10-14-t04-v6/README.md).

## 14 de octubre de 2026 — T06-v6
- Reportes, Baja y null conformes según evaluate.py. Fuente: JSON pegado, sin captura.
- Resumen fiel como solicitud pendiente. datos_faltantes pide campos/filtros ausentes, concretos y útiles para definir requisitos. v5 también pedía requisitos, incluido formato/ordenamiento; no afirmar mejora global.
- v6: cuatro ejecuciones sobre tres tickets, todas conformes en etiquetas, cobertura única 3/10. T02/T04 quedaron vacíos; T06 pide requisitos útiles. Resultados de contenido distintos por caso.
- Total entre versiones: 37 ejecuciones sobre doce tickets distintos. Próximo T10 con v6 sin cambios; luego revisar antes de otro ajuste.
- [T06-v6](../experiments/2026-10-14-t06-v6/README.md).

## 14 de octubre de 2026 — T10 y cierre de controles v6; v7 preparada
- T10 conserva Otros, Media, null y pide describir incidente, sin afirmar corrección. evaluate.py confirma etiquetas/formato. Fuente textual, sin captura.
- Controles v6: cinco ejecuciones, cuatro tickets únicos, todas conformes en etiquetas; cobertura 4/10. T02/T04 listas vacías, T06/T10 información pertinente. No mejora uniforme de datos faltantes.
- Consolidación conserva ambas T02 en runs.json; evaluación por ticket usa última T02 por convención explícita, no selección de mejor salida. No mezclar con ronda v5 completa.
- Total entre versiones: 38 ejecuciones sobre doce tickets distintos.
- Técnica siguiente: few-shot prompting con dos ejemplos Usuario/Asistente; documentación oficial SAP/Google consultada. System v6 idéntico; EX01/EX02 diseñados fuera del benchmark y no contados como ejecuciones. Campos/tipos y referencias verificados localmente.
- v7 preparada sin resultados. Próximo T02 real como último Usuario de seis mensajes, luego T04/T06/T10. Revisar utilidad de información y no copiar ids/respuestas de ejemplos.
- [v6 consolidada](../experiments/2026-10-14-v6-controls/README.md), [v7 preparada](../prompts/v7-few-shot/README.md).

## 14 de octubre de 2026 — conceptos integrados al laboratorio
- Gastón pidió explicar skill con un ejemplo del proyecto y conservar este y otros conceptos en GitHub.
- Se añadió [CONCEPTS.md](CONCEPTS.md): catorce temas con explicación en español, término en inglés, ejemplo ERP y pregunta de comprensión.
- Skill queda documentada como procedimiento reutilizable; el ejemplo de revisión ERP es conceptual, no una skill instalada.
- La guía distingue prompt, roles, few-shot y herramientas; desarrolla clasificación/extracción/diagnóstico, esquema, instrucciones en datos, afirmaciones no sustentadas, benchmark, evaluación humana/automática, regresión, generalización, versionado y parámetros.
- Se actualizó el documento de roles para separar el historial v0/v1 del estado actual y la propuesta v7.
- Método acordado por solicitud del usuario: acompañar nuevas prácticas con teoría aplicada y registro en la guía; las preguntas quedan pendientes de respuesta, sin dar por demostrada la comprensión.
- Sin nuevas salidas de modelo: continúan 38 ejecuciones sobre doce tickets distintos. Próxima prueba: T02 con v7.

## 14 de octubre de 2026 — MCP y relación con skills
- Pregunta del usuario: qué es MCP y cómo se relaciona con una skill.
- Añadida sección 15 en [la guía de conceptos](CONCEPTS.md#15-mcp-y-su-relación-con-las-skills-model-context-protocol), con definición, comparación de prompt/skill/MCP/tool/API y ejercicio aplicado a T04.
- Ejemplo real: las herramientas del conector GitHub disponibles mediante MCP permiten leer y guardar documentación desde este chat.
- Ejemplo futuro explícito: consultar una factura o stock mediante un servidor MCP del ERP; esa integración no está implementada en el laboratorio.
- Una skill aporta el procedimiento reutilizable; MCP estandariza comunicación con herramientas/datos. No se creó una skill ni un servidor ERP.
- Documentación oficial OpenAI consultada. No hay nuevas ejecuciones: 38 sobre doce tickets, v7 aún preparada sin resultados.

## 15 de octubre de 2026 — restauración y primera respuesta T02-v7
- Se recuperaron Sistema y seis mensajes v7 desde GitHub. El usuario preguntó por qué Asistente estaba vacío antes: v0–v6 no contenían demostraciones; v7 añade ejemplos.
- Captura previa mostró tres bloques (Sistema, Usuario EX01, Asistente EX01) y panel vacío. Se explicó que + crea bloques y los botones eligen rol; se reenviaron los seis mensajes completos. Sin evidencia para atribuir la ausencia de salida exclusivamente a esa configuración.
- JSON posterior T02 recibido como texto. Configuración final de seis bloques/payload y parámetros numéricos no capturados; modelo visible previamente Gemini 2.5 Flash Lite (001).
- evaluate.py ejecutado: formato/etiquetas conformes. Resumen conserva bloqueo del equipo y cierre, sin causas inventadas; datos_faltantes sigue vacío pese a faltar error exacto/pasos.
- Comparación con dos T02-v6: ninguna pide datos útiles. Una ejecución v7 no demuestra resultado general ni causalidad del cambio de ejemplos.
- Se explicó que EX01/EX02 son contexto con respuestas preparadas y la salida nueva responde al último Usuario T02. No contarlos como ejecuciones adicionales.
- v7: una respuesta, un ticket, cobertura 1/10. Total entre versiones: 39 respuestas registradas sobre doce tickets distintos. Intentos sin salida verificable no sumados.
- [Resultado T02-v7](../experiments/2026-10-15-t02-v7/README.md). Próximo T04 con Sistema/ejemplos sin cambios; revisar cantidades, fecha y uso del almacén informado.

## 15 de octubre de 2026 — T04-v7
- JSON original recibido como texto tras indicación de cambiar solo el último Usuario; sin captura final/payload ni parámetros completos.
- evaluate.py ejecutado para T04 y consolidación T02/T04: formato/etiquetas conformes, sin referencias inventadas literalmente ni ids duplicados/desconocidos.
- Resumen fiel conserva ART-310 y almacén central. datos_faltantes pide cantidad del sistema, cantidad física y fecha: datos ausentes concretos y útiles; no solicita de nuevo el almacén informado.
- Mejora observada frente a T04-v6 con lista vacía. T04 es muy parecido a EX02: aplicación de patrón cercano, no prueba amplia de generalización. Caso previamente usado para ajuste, no independiente.
- v7: dos respuestas sobre dos tickets, cobertura 2/10 y etiquetas/formato 2/2 entre ejecutados. T02 sigue vacío; no afirmar mejora uniforme.
- Total entre versiones: 40 respuestas registradas sobre doce tickets distintos. [T04-v7](../experiments/2026-10-15-t04-v7/README.md), [controles consolidados](../experiments/2026-10-15-v7-controls/README.md).
- Próximo T06 cambiando solo último Usuario; comprobar requisitos de reporte, sin copiar preguntas de stock. Luego T10.

## 15 de octubre de 2026 — T06-v7, control de regresión
- Respuesta original recibida como JSON, sin captura/payload completo ni parámetros numéricos actuales verificados.
- evaluate.py ejecutado para T06 y consolidación T02/T04/T06: formato/etiquetas conformes, sin ids desconocidos/duplicados ni referencias ausentes literalmente.
- T06 mantiene Reportes, Baja y null. Resumen de solicitud pendiente; pide campos y formato, ausentes y útiles para definir requisitos. No copia preguntas de stock de EX02.
- T06-v6 ya pedía requisitos pertinentes: conservación de comportamiento, no evidencia de mejora global. La especificación funcional del reporte todavía requiere relevamiento.
- v7: tres respuestas sobre tres tickets únicos, cobertura 3/10 y formato/etiquetas 3/3 entre ejecutados. T02 vacío, T04/T06 con información útil.
- Total entre versiones: 41 respuestas registradas sobre doce tickets distintos. [T06-v7](../experiments/2026-10-15-t06-v7/README.md).
- Próximo T10 cambiando únicamente último Usuario, para comprobar regla de instrucciones dentro del ticket después de agregar demostraciones.

## Plantilla para próximas sesiones
- Fecha y objetivo:
- Concepto aprendido:
- Acción realizada y entorno:
- Evidencia obtenida:
- Error o duda:
- Qué puede explicar Gastón con sus palabras:
- Próximo paso:
