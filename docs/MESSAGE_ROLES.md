# Roles de mensajes en el laboratorio

## Concepto
- Sistema (System): comportamiento general, reglas y contrato de respuesta.
- Usuario (User): solicitud y datos del ticket que se quiere clasificar.
- Asistente (Assistant): respuestas previas del modelo o ejemplos de respuesta que se aportan como contexto. Seleccionar este rol en el editor añade una entrada de ese tipo; no es un botón para generar una respuesta.

SAP AI Launchpad permite especificar roles, instrucciones y ejemplos. Los mensajes de sistema orientan el comportamiento; no garantizan que el modelo siempre cumpla las reglas o resista instrucciones incluidas en los datos.

## Estado actual: v0
T01, T02 y T10 se probaron con un único mensaje Usuario que contiene reglas y ticket, según las instrucciones del laboratorio. No se usa un mensaje Asistente porque esta referencia inicial no incluye ejemplos ni historial.

No se concluye que los datos_faltantes vacíos de T02 se deban a ese diseño de roles.

## Siguiente comparación
1. T10 ya ejecutado con v0: prioridad errónea y contenido no sustentado; resultado conservado.
2. v1-roles preparada, pendiente de ejecución: mover el texto de instrucciones anterior a ENTRADA a Sistema y conservar id y ticket en Usuario. Mantener reglas, modelo y parámetros.
3. Repetir los mismos casos y guardar sus respuestas por separado.
4. Probar después otra versión que precise la regla de datos_faltantes.
5. Si se añaden ejemplos en Asistente (few-shot prompting), usar casos adicionales que no sean los tickets reservados para evaluar.

No cambiar roles y reglas a la vez si se quiere estudiar el efecto de separar roles. Cualquier mejora debe medirse; todavía no hay resultados de v1.

La preparación concreta está en [prompts/v1-roles](../prompts/v1-roles/README.md).

## Fuentes
- https://help.sap.com/docs/ai-launchpad/sap-ai-launchpad-user-guide/templating
- https://ai.google.dev/gemini-api/docs/text-generation
