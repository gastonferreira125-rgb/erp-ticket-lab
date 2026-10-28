# Continuidad entre ChatGPT Work y el chat de estudio

**Actualizado:** 2026-10-28  
**Proyecto:** ERP Ticket Lab — SAP Business One Developer, Integrations & AI  
**Objetivo:** continuar el mismo recorrido de aprendizaje al alternar sesiones de Work y chat normal sin repetir trabajo ni asumir resultados no verificados.

## Fuente de verdad

Este repositorio es el registro verificable; los chats aportan tutoría y ejecución, pero no se sincronizan automáticamente.

Antes de iniciar una sesión:
1. Leer este archivo y los documentos enlazados más abajo.
2. Comprobar el estado real del repositorio y, cuando corresponda, de la herramienta externa.
3. Distinguir **completado con evidencia**, **documentado solamente**, **pendiente** y **no iniciado**.
4. Continuar un único siguiente paso concreto, explicando teoría, herramienta, configuración y conceptos en español con términos relevantes en inglés.
5. Al terminar, actualizar este archivo con fecha, cambios, capturas/evidencia, resultados, dudas y próximo paso. No sobrescribir experimentos históricos.

**No hacer:** inventar acceso SAP, declarar ejecuciones no observadas, contar una propuesta textual como integración implementada, ni publicar secretos o datos reales.

## Estado verificable al 28/10/2026

### Laboratorio n8n de ruteo de tickets

Documentación: [labs/n8n-ticket-routing/README.md](../labs/n8n-ticket-routing/README.md)

- Flujo educativo creado en n8n Cloud: Manual Trigger → Edit Fields → If → dos salidas Edit Fields.
- Entrada: ticket_id, categoria, prioridad, resumen (campos sintéticos); salida agrega siguiente_accion.
- Condición: `{{ $json.prioridad }}` **is equal to** `Alta`.
- T06/Baja: rama false comprobada; T02/Alta: rama true comprobada.
- Se documentaron correcciones: campo comparado, conservar campos de entrada, cableado false y actualización de OUTPUT mediante nueva ejecución.
- Capturas y límites documentados en [índice de evidencias](../labs/n8n-ticket-routing/evidence/2026-10-28/README.md).
- **Completado:** se recibió el export de n8n, se verificaron 5 nodos/conexiones, se retiró solo meta.instanceId y se guardó [workflow.json](../labs/n8n-ticket-routing/workflow.json). El export mantiene T02/Alta. No incluye historial de ejecución.
- **Próximo paso de formación:** añadir validación de prioridad con valores permitidos Alta / Media / Baja; evitar que vacío o desconocido se enrute por false. La captura del OUTPUT final de T06 posterior al cableado corregido sigue pendiente de forma no bloqueante.
- No existe en este laboratorio conexión live a ERP, modelo IA, MCP ni orquestación en paralelo.

### Clasificador ERP con IA

Referencias: [registro de aprendizaje](LEARNING_LOG.md), [etapa 2](STAGE_2_PRACTICE_02.md), [README principal](../README.md).

- Hay prompts versionados v0–v8, tickets sintéticos, respuestas registradas, contrato JSON y evaluador Python.
- La v8 se mantiene congelada; no modificar resultados históricos sin experimento nuevo.
- El diseño de orquestación no prueba implementación ni resolución de incidentes.
- No integrar automáticamente la salida del clasificador con n8n antes de validar contrato, valores y supervisión humana.

### Formación SAP Business One Developer

Referencia: [programa](SAP_B1_DEVELOPER_PROGRAM.md).

- Módulo 1, Lección 1: arquitectura SAP B1 y criterios de integración.
- Pendiente comprobar las versiones instaladas de Python, Git y SDK .NET si no hay evidencia posterior en el repositorio.
- Próximos ejes: tablas de B1 (por ejemplo OPOR/POR1), SQL, Service Layer y HTTP/OData; luego extensiones y AI, con práctica guiada.
- No asumir que la lectura del roadmap otorga acceso real a B1.

## Protocolo de cierre de cada sesión

Actualizar este bloque con:
- **Fecha y modalidad:** Work / chat.
- **Tema y objetivo:** qué se intentó.
- **Práctica realizada:** acciones concretas y enlaces al código/archivo.
- **Evidencias:** capturas, datos sintéticos, resultados de pruebas; nunca credenciales.
- **Aprendizaje:** teoría y términos técnicos aprendidos.
- **Estado real:** completado / parcial / pendiente / bloqueado.
- **Siguiente paso único:** acción que retoma el otro chat.

Cuando no se hayan modificado archivos, la respuesta final debe incluir un breve resumen de continuidad para poder copiarlo al otro chat.

## Instrucción para pegar al cambiar de chat

> Continuá mi programa ERP Ticket Lab / SAP B1 Developer, Integrations & AI. Antes de avanzar, leé `docs/CONTINUIDAD_CHAT_WORK.md` en el repositorio `gastonferreira125-rgb/erp-ticket-lab` y los documentos enlazados. Verificá el estado real, evitá repetir prácticas, explicame teoría y términos técnicos durante cada ejercicio, pedime capturas como evidencia y actualizá el registro al cerrar. No des por completado lo que solo esté diseñado o pendiente.

## Cierre de sesión de chat — 28/10/2026: exportación del workflow

- **Modalidad:** chat normal.
- **Evidencia:** archivo JSON exportado por el participante y revisado; cinco nodos y conexiones verificados contra la práctica. [Copia para importar](../labs/n8n-ticket-routing/workflow.json).
- **Seguridad:** sin secciones credentials en nodos; retirada de meta.instanceId de la copia pública.
- **Resultado:** configuración registrada en GitHub; no se han ejecutado pruebas adicionales del workflow importado.
- **Siguiente paso:** Input Validation en n8n (Alta / Media / Baja), con pruebas de prioridad Media, texto vacío y valor desconocido. Evitar repetir T02 y T06 ya documentados, salvo requerimiento específico.

## Sesión chat normal — 28/10/2026, validación de prioridad

- **Estado:** el participante agregó un If llamado `Validar prioridad` y mostró dos capturas de configuración y ejecución.
- **Prueba confirmada:** T02 / Alta produce true en validador, llega a If original y continúa a Edit Fields2; se observó un item en esa ruta.
- **Pendientes:** rama false de Validar prioridad sin tratamiento, crear salida de rechazo y probar valor `Urgente`; luego probar `Media` y vacío. No atribuir estos resultados hasta ver su ejecución.
- **Próximo paso único:** conectar un nodo de revisión en false del validador, conservando campos de entrada y marcando el estado de validación; después ejecutar entrada inválida.

## Sesión chat normal — 28/10/2026, prueba negativa de prioridad

- **Configuración mostrada:** se creó `Revisar prioridad` en false del validador, con `estado_validacion=Rechazada`, `motivo_validacion=Prioridad fuera del catálogo permitido` e inclusión de demás campos.
- **Prueba con evidencia:** entrada T02 con prioridad `Urgente`; el lienzo muestra ruta false a `Revisar prioridad`, 1 item y ejecución exitosa. No pasó al `If` original.
- **Límite de la evidencia:** otra captura del panel mostraba `No output data`, presumiblemente distinta ejecución; falta ver JSON OUTPUT del último recorrido, sin afirmar que los seis campos resultantes están comprobados.
- **Próximo paso único:** abrir `Revisar prioridad`, capturar OUTPUT JSON de la última ejecución de `Urgente`; luego probar Media y vacío. Mantener separado el export anterior de cinco nodos.

### Aclaración de captura previa

- **Aclaración posterior del participante:** el panel `No output data` era de una ejecución anterior, realizada antes de cambiar la prioridad a `Urgente`. Después cambió el dato y ejecutó el workflow, mostrando 1 item en la rama false de validación hacia `Revisar prioridad`. No se observó un fallo de ejecución; sigue sin recibirse una captura JSON del contenido de los campos de salida.


## Handoff — 28/10/2026: laboratorio n8n validación v2

- **Estado:** export nuevo guardado en [workflow-v2-validacion.json](../labs/n8n-ticket-routing/workflow-v2-validacion.json). La versión original de cinco nodos permanece sin sustituir.
- **Arquitectura comprobada:** siete nodos; validación previa de prioridad mediante `includes` para Alta/Media/Baja; false hacia Revisar prioridad; true hacia If que distingue Alta de no Alta.
- **Evidencia visual:** T02 Alta por ruta prioritaria, T02 Media por ruta no Alta, T02 con Urgente por rechazo, T02 con prioridad vacía por rechazo (1 item); T06 Baja fue probado en el laboratorio v1, no con el validador nuevo.
- **Versión exportada:** entrada `prioridad=""`; sin credenciales, copia pública sin `meta.instanceId`. El export representa configuración, no historial ni datos OUTPUT.
- **No declarar comprobado:** el contenido final del OUTPUT JSON de Rechazar prioridad en ejecución, conexión a IA ni conexión a SAP.
- **Próximo paso:** iniciar diseño educativo de entrada automática del clasificador IA (contrato, normalización y tratamiento de entradas inválidas), sin reejecutar pruebas cubiertas salvo que se necesite evidencia nueva. Explicar la teoría junto a cada implementación.

## Inicio Lab 02 — 28/10/2026
Se recibió una captura del usuario que confirma la existencia de una copia en n8n llamada 'ERP Ticket Lab - Flujo 02 - Integración IA'. Se observan los siete nodos del Lab 01 y las conexiones del enrutamiento y rechazo. No hay una exportación JSON de esta copia, ni evidencia de integración real con un modelo. Paso siguiente de tutoría: en el nodo Edit Fields de la copia, cambiar Manual Mapping a JSON Output, cargar un objeto sintético compatible con schema.json de seis campos, ejecutar y revisar el OUTPUT. Registrar luego el resultado observado. Conservar Flujo 01 sin modificar.

## Flujo 02 — entrada JSON simulada (28/10/2026)
- Captura recibida del nodo Edit Fields de n8n en el Flujo 02; Mode=JSON. El OUTPUT muestra un item con seis claves: ticket_id=T02, categoria=Finanzas, prioridad=Alta, resumen sintético, referencia_documento=FV-1042 y datos_faltantes como array de dos strings.
- El nodo produjo correctamente JSON sintácticamente interpretable. No se ha validado aún el documento con el schema.json completo; no hay conexión con un modelo ni con SAP.
- No se ha compartido un export JSON actualizado del Flujo 02, solo captura. El Flujo 01 original se conserva.
- **Próximo paso:** crear una etapa de validación integral del contrato con JavaScript (nodo Code) antes del validador de prioridades y comprobar la salida con casos válidos e inválidos. Enseñar sintaxis y tipos mientras se desarrolla.

## Handoff — 28/10/2026: Flujo 02 con Code JavaScript (8 nodos)

- **Archivos:** [export del Flujo 02](../labs/n8n-json-contract/flujo-02-v1.json), [manual del Lab 02](../labs/n8n-json-contract/README.md) y contrato [schema.json](../schema.json).
- **Evidencia:** captura del nodo Edit Fields con los seis campos JSON de T02; captura de ejecución que muestra Validar contrato JSON, Validar prioridad, If y Edit Fields2 con un item. Export real inspeccionado con 8 nodos, Code en Run Once for Each Item, sin credenciales observadas. Se eliminó meta.instanceId en la copia pública.
- **Límite:** el Code valida y agrega `validacion_contrato`, pero aún no se verifica por captura su OUTPUT JSON; no existe una rama de rechazo de contratos inválidos. No afirmar integración con modelo IA o SAP.
- **Próximo paso único:** insertar If `Contrato válido?` después del Code, condición `{{ $json.validacion_contrato.valido }}` is true; true hacia Validar prioridad, false hacia nuevo Edit Fields `Revisar contrato`. Probar caso válido e inválido y exportar otra versión.

## Handoff — 28/10/2026: revisión del If de contrato (capturas)

- Se observa INPUT del nodo `Contrato válido?` con `validacion_contrato.valido=true` y array `errores` vacío (T02 válido), además de condición Boolean `is true` sobre `{{ $json.validacion_contrato.valido }}`.
- `Revisar contrato` aún presenta el campo predeterminado `name/value`, aunque `Include Other Input Fields` está activado. Conexiones y ejecución del nuevo If no confirmadas visualmente.
- **Siguiente acción única:** configurar dos campos de salida del rechazo (`estado_validacion=Rechazada`, `motivo_validacion=Contrato JSON inválido`), verificar enlaces true/false y probar con categoría inválida en el JSON simulado.
