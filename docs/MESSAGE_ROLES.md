# Roles de mensajes en el laboratorio

## Concepto

- Sistema (System): en nuestra plantilla contiene comportamiento general, reglas y contrato de respuesta.
- Usuario (User): solicitud y datos del ticket que se quiere clasificar.
- Asistente (Assistant): respuestas previas o ejemplos aportados como contexto. Escribir un mensaje con este rol no genera una nueva respuesta del modelo.

Separar roles ayuda a expresar la tarea, pero no garantiza cumplimiento. [Guía de conceptos y ejemplos](CONCEPTS.md).

## Historia de las pruebas

v0 usó un único Usuario con reglas y ticket. v1 mantuvo las reglas y las distribuyó en Sistema y Usuario; T10 siguió fallando. No se atribuyen las listas vacías de T02 al diseño de roles.

Las versiones v2–v6 precisaron distintas reglas y conservaron Sistema/Usuario. Los resultados y límites están en el [registro de aprendizaje](LEARNING_LOG.md); el diseño histórico v1 está en [v1-roles](../prompts/v1-roles/README.md).

## v7: diseño y primeras respuestas (historial)

Sistema v6 se conserva íntegro. Se añaden dos pares de demostraciones, con esta secuencia:

| Posición | Rol | Contenido |
| --- | --- | --- |
| 1 | Sistema | Reglas v6 completas. |
| 2 | Usuario | Ejemplo EX01: factura que no se contabiliza. |
| 3 | Asistente | JSON preparado para EX01. |
| 4 | Usuario | Ejemplo EX02: diferencia de stock. |
| 5 | Asistente | JSON preparado para EX02. |
| 6 | Usuario | T02 real, sin su respuesta esperada. |

Los ejemplos son few-shot prompting. EX01/EX02 no son ejecuciones del modelo ni tickets del conjunto de evaluación. Cambiar solo el último Usuario permite probar los siguientes casos manteniendo las demostraciones.

Ver [v7-few-shot](../prompts/v7-few-shot/README.md) y [mensajes completos para T02](../prompts/v7-few-shot/messages-t02.json). Añadir ejemplos es un cambio del prompt. La [primera respuesta T02](../experiments/2026-10-15-t02-v7/README.md) conserva etiquetas y datos_faltantes vacío; no muestra mejora de ese campo en esta ejecución. No se verificó el payload final de seis mensajes.

Los dos mensajes Asistente de ejemplo forman parte de la entrada. La salida nueva corresponde al último Usuario; no se espera un resultado separado por cada ejemplo. Seis mensajes de entrada no son seis ejecuciones del modelo.

## Fuentes

- [SAP, few-shot learning](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/few-shot-learning-7ffdf9a6d89c465d8058634e7c4bb19c).
- [SAP Launchpad, Templating](https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad/11d44e657b5946f6880729da08eba0da.html).
- [Google, estrategias de prompts](https://ai.google.dev/gemini-api/docs/prompting-strategies).

## Estado al cierre de la etapa
v8 conserva los mismos seis roles y ejemplos; solo añade la regla de transacciones fallidas al Sistema. Se completaron T02/T04/T06/T10 cambiando el último Usuario. [Seis mensajes v8](../prompts/v8-transaction-investigation/messages-t02.json), [XML](../prompts/v8-transaction-investigation/backup/ERP_Tickets_v8_FewShot.xml), [cierre](STAGE_1_CLOSURE.md). Los Asistente de ejemplo siguen siendo contexto, no respuestas medidas.
