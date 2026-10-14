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

## Plantilla para próximas sesiones
- Fecha y objetivo:
- Concepto aprendido:
- Acción realizada y entorno:
- Evidencia obtenida:
- Error o duda:
- Qué puede explicar Gastón con sus palabras:
- Próximo paso:
