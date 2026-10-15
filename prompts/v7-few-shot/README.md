# v7-few-shot — controles parciales T02/T04

Único cambio frente a v6: añadir dos ejemplos sintéticos mediante pares de mensajes Usuario/Asistente. system.txt es idéntico al System v6; mismo modelo y parámetros solicitados. No se añaden nuevas reglas ni se cambian esquema/etiquetas.

Estructura de seis mensajes:
1. Sistema: reglas v6 completas.
2. Usuario: ejemplo EX01, factura que no se contabiliza.
3. Asistente: JSON diseñado para EX01, con error exacto/pasos como datos faltantes.
4. Usuario: ejemplo EX02, diferencia de stock.
5. Asistente: JSON diseñado para EX02, con cantidades/fecha y sin pedir depósito ya informado.
6. Usuario: ticket T02 real del conjunto de evaluación, sin su respuesta esperada.

[messages-t02.json](messages-t02.json) contiene los seis mensajes; [examples.json](examples.json) los pares de ejemplo con sus entradas/respuestas; [user-t02.txt](user-t02.txt) el caso real. Cambiar solo último Usuario para futuros casos y conservar ejemplos.

Los JSON Asistente son demostraciones preparadas por el tutor, no salidas de modelo medidas ni predicciones de tickets T01–T12. EX01/EX02 no pertenecen al conjunto de evaluación. Se comprobaron campos/tipos con valid de evaluate.py y presencia literal de referencias; revisión humana: no inventan soluciones y piden datos ausentes útiles.

Objetivo: observar si los ejemplos ayudan a pedir información concreta y útil en T02/T04, donde v6 dejó listas vacías. Hipótesis de mejora, no garantía. Los ejemplos también muestran formato/resumen/etiquetas; cualquier cambio de salida no debe atribuirse causalmente a un campo aislado con una sola ejecución.

Pruebas previstas: T02, T04, T06 y T10. Revisar id/etiquetas y datos faltantes sin exigir lista textual idéntica al ejemplo. No guardar respuestas de demostración como resultados del modelo. Luego casos nuevos y repeticiones.

## Resultados y siguiente paso

15 de octubre: [T02-v7](../../experiments/2026-10-15-t02-v7/README.md), formato y etiquetas conformes; datos_faltantes vacío, sin mejora observada de ese campo frente a T02-v6. Cobertura 1/10. Resultado pegado como texto tras instrucciones de completar seis bloques; payload final y parámetros numéricos actuales no verificados.

EX01/EX02 tienen respuestas Asistente preparadas, por lo que se usan como contexto; la salida nueva de esta prueba corresponde a T02. No son tres ejecuciones medidas. [T04-v7](../../experiments/2026-10-15-t04-v7/README.md) añade preguntas útiles de cantidades y fecha sin volver a pedir almacén. Patrón muy cercano a EX02; mejora observada del caso, no generalización amplia. [Consolidación](../../experiments/2026-10-15-v7-controls/README.md): dos respuestas conformes en etiquetas/formato, cobertura 2/10; contenido no mejora uniformemente porque T02 sigue vacío. Próximo T06 cambiando solo el último Usuario; conservar reglas/ejemplos/configuración solicitada.

## Fuentes de la técnica
- SAP: https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/few-shot-learning-7ffdf9a6d89c465d8058634e7c4bb19c
- SAP Launchpad Templating: https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad/11d44e657b5946f6880729da08eba0da.html
- Google Gemini prompt design, zero-shot/few-shot: https://ai.google.dev/gemini-api/docs/prompting-strategies

La documentación SAP muestra System, ejemplos User/Assistant y un último User real. Estos ejemplos influyen en el contexto del prompt; no constituyen fine-tuning ni entrenamiento permanente de pesos.
