# Práctica 2 — de la clasificación al siguiente paso

Fecha: 17 de octubre de 2026. Diseño didáctico manual; todavía no es una automatización. Se reutilizan respuestas v8 ya registradas, sin nuevas llamadas al modelo.

## Objetivo
Convertir una clasificación revisada en una propuesta de atención y distinguir prioridad, información disponible y resolución.

## Concepto: regla de decisión (decision rule)
Una regla de decisión expresa qué hacer cuando se cumple una condición. En esta práctica, la aplicación podría comprobar condiciones mediante código; no hace falta volver a consultar al modelo para cada decisión.

Ejemplo: si una clasificación fue revisada y el ticket describe un proceso detenido para todo un equipo, proponer atención prioritaria. Si además faltan datos útiles, preparar su solicitud en paralelo. Esto no identifica una causa ni ejecuta una solución.

Las reglas siguientes son convenciones educativas del laboratorio, no una política universal de soporte.

## Comparación guiada
Las prioridades de esta tabla proceden de las respuestas v8 y coinciden con la política del ejercicio. La propuesta de atención es una explicación del tutor, pendiente de aplicación y revisión; no registra acciones ejecutadas.

| Aspecto | T02 | T06 |
| --- | --- | --- |
| Entrada | FV-1042 no se contabiliza; todo Finanzas bloqueado y cierre detenido | Solicitud de reporte mensual de ventas por cliente, sin interrupción |
| Clasificación v8 | Finanzas / Alta / FV-1042 | Reportes / Baja / sin referencia |
| Información solicitada por v8 | Mensaje de error exacto y pasos realizados | Campos a incluir y filtros deseados |
| Tratamiento propuesto tras revisión | Organizar atención prioritaria y recopilar evidencia en paralelo | Acordar requisitos para planificar el reporte |
| Evidencia que permitiría avanzar | Error/comportamiento y pasos de la transacción | Campos y filtros acordados; comprobar si falta formato u otro requisito útil |
| Lo que todavía no demuestra | Que la factura se haya contabilizado o el cierre se haya recuperado | Que el reporte se haya creado y aceptado |

T06 corresponde a prioridad Baja por ser una solicitud planificada sin interrupción. La prioridad y el tratamiento siguen la política explícita del laboratorio.

## Reglas iniciales del flujo
1. Si el formato es inválido, registrar el problema y pasar a revisión; no tratar campos ausentes como decisiones válidas.
2. Si el formato es válido, contrastar contenido e impacto con el ticket. Hasta entonces la propuesta está pendiente de revisión funcional.
3. Si la revisión confirma un bloqueo de proceso para todo un equipo, proponer atención prioritaria. Pedir información ausente en paralelo cuando sea útil.
4. Si confirma una solicitud planificada sin interrupción, proponer definición de requisitos y planificación.
5. Para los demás casos, aplicar el tratamiento de prioridad Media definido por el laboratorio; no inventar urgencias.
6. Cuando llegan datos, incorporarlos y comprobar si alcanzan para investigar o definir la solicitud. Recibir una respuesta no garantiza que la información sea suficiente.
7. Una lista vacía, una clasificación correcta o un error recibido no prueban resolución. El cierre requiere evidencia de que se atendió el problema o solicitud y una validación de la persona responsable.

## Transiciones: qué cambia con cada evento
Una transición (state transition) es un cambio de estado provocado por un evento y permitido por una condición.

| Evento | Condición que hay que comprobar | Cambio propuesto |
| --- | --- | --- |
| Llega una clasificación | Formato y contenido revisados | Preparar el tratamiento apropiado |
| Llegan error y pasos de T02 | Son utilizables para el siguiente paso | Actualizar información disponible y continuar investigación; no resolver automáticamente |
| Se acuerdan campos y filtros de T06 | Requisitos suficientes para el siguiente paso | Pasar de definición a planificación; no declarar el reporte entregado |
| Se aporta evidencia de recuperación de T02 | La persona responsable verifica recuperación del proceso afectado | Proponer cierre y registrar la validación |
| Aparece nueva información de impacto | Confirmar si cambió el alcance | Revisar prioridad; no cambiarla solo porque llegaron datos |

Los estados y acciones del flujo se guardarían en un registro separado. El clasificador v8 mantiene sus seis claves. En esta lección no se cambia ningún ticket externo ni se envían solicitudes.

## Ejemplo de transición por nueva información
Escenario nuevo y simulado, no es una ejecución del modelo:

T02 recibe el mensaje de error exacto y los pasos realizados. Esa información alcanza para comenzar la investigación, pero la factura sigue sin contabilizarse y el cierre de todo Finanzas continúa detenido.

La recepción de información suficiente actualiza el estado de información disponible. Mientras continúe el bloqueo, no cambia por sí sola la prioridad ni permite cerrar el ticket.

Recibir el error y los pasos permite comenzar la investigación. Todavía no demuestra una causa identificada, una solución definida o una corrección ejecutada. La prioridad sigue Alta mientras continúe el bloqueo y el ticket permanece abierto.

## Puente hacia código: condición y acción
Una regla determinista aplica la misma decisión cuando recibe las mismas condiciones. Para esta transición educativa podemos expresarla así, sin otra llamada al modelo:

```text
SI la información recibida alcanza para el siguiente paso:
    estado_informacion = "Suficiente para iniciar investigación"
    siguiente_accion = "Investigar"
```

La suficiencia debe ser evaluada; no se deduce únicamente de que llegó un mensaje. La regla no cambia por sí sola prioridad o resolución. Este pseudocódigo explica la decisión; todavía no es una automatización ejecutable ni prueba que un ticket haya sido actualizado.
