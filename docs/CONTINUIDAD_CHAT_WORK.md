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

## Handoff — 28/10/2026, gate de contrato implementado y rechazo probado

- Se recibió un segundo export del Flujo 02: [flujo-02-v2-rechazo.json](../labs/n8n-json-contract/flujo-02-v2-rechazo.json), **10 nodos**, con dos ramas de `Contrato válido?` y nodo `Revisar contrato`.
- Prueba negativa observada en capturas: `categoria=NoExiste`, `prioridad=Alta`; rama false de Contrato válido? llega a Revisar contrato (1 item). No se recorren Validar prioridad ni If original. Ajustes de rechazo confirmados por captura y configuración del JSON.
- **Límite:** no se vio contenido OUTPUT final del rechazo; no asumir mensaje exacto mostrado al usuario. Export es configuración, no historial de ejecución.
- **Próximo paso:** prueba de regresión del caso válido cambiando solo categoría a `Finanzas` (verificar true → Validar prioridad → Edit Fields2), y después mejorar motivo dinámico de validación de errores. Mantener Flujo 01 y versión anterior del Flujo 02 sin cambios.


## Sesión de planificación — 03/11/2026: empleabilidad y SAP Business AI

- **Alcance de este chat:** aprendizaje técnico SAP B1 Developer, IA aplicada a ERP, n8n/Python/JavaScript, Joule Studio y arquitectura SAP Business AI; las búsquedas laborales y postulaciones se gestionan en **otro chat**, sin duplicarlas.
- **Propósito profesional:** fortalecer conocimientos demostrables y el portfolio para acceder a empleos de consultoría ERP, integraciones y automatización de IA a corto plazo; estudiar una certificación nueva no debe bloquear postulaciones.
- **Roadmap complementario propuesto (no realizado):** fundamentos de SAP Business AI -> arquitectura BAIPA1 -> desarrollo con Joule Studio -> metodologías BAIPAM -> preparación eventual para C_BAIPA. Integrar teoría al mismo ERP Ticket Lab y documentar evidencia; no dar certificaciones por obtenidas ni asumir vouchers disponibles.
- **Estado consultado:** último export comprobado es `labs/n8n-json-contract/flujo-02-v2-rechazo.json`, con diez nodos; el ejemplo configurado conserva `categoria=NoExiste`; hubo evidencia de recorrido de rechazo, pero no de JSON OUTPUT final.
- **Siguiente paso práctico único (todavía pendiente):** en el `Edit Fields` de Flujo 02 cambiar solo `categoria` de `NoExiste` a `Finanzas`, ejecutar el workflow, capturar lienzo y OUTPUT JSON del camino `Contrato válido?` true -> `Validar prioridad` true -> `If` true -> `Edit Fields2`; comprobar `validacion_contrato.valido=true` y `errores=[]`. No afirmar ejecución antes de evidencia.
- **Mejora posterior:** hacer dinámico `motivo_validacion` en `Revisar contrato` mediante `{{ $json.validacion_contrato.errores.join('; ') }}`, probar un caso inválido y exportar una nueva versión sin reemplazar los archivos históricos.
- **Modo de enseñanza:** teoría, términos en inglés, práctica paso a paso y pedido de capturas de evidencia, manteniendo este documento como fuente de verdad.


## Sesión — 03/11/2026: regresión positiva del Flujo 02

- **Modalidad:** chat normal. Usuario compartió dos capturas de n8n Cloud.
- **Entrada visualizada:** ticket T02, `categoria=Finanzas`, `prioridad=Alta`, `referencia_documento=FV-1042`, `datos_faltantes` como array de dos textos. Captura JSON con seis campos, aparentemente del primer `Edit Fields` (no salida enriquecida final).
- **Prueba de regresión positiva confirmada por lienzo:** `Manual Trigger → Edit Fields → Validar contrato JSON → Contrato válido?` rama true → `Validar prioridad` rama true → `If` rama true → `Edit Fields2`. Todos los nodos del recorrido figuran ejecutados (verde) y hay 1 item hasta el nodo final; se muestra mensaje `Workflow executed successfully`.
- **Evidencia pendiente:** captura de OUTPUT JSON en `Edit Fields2` con `validacion_contrato.valido=true`, `validacion_contrato.errores=[]` y `siguiente_accion`. No afirmar estos campos inspeccionados solo por éxito del lienzo.
- **Resultado real:** ruta de procesamiento correcto validada visualmente, además del rechazo de categoría inválida de la sesión anterior. No se han conectado IA real ni SAP.
- **Siguiente paso único:** abrir `Edit Fields2` → OUTPUT → JSON y compartir captura completa; luego parametrizar `motivo_validacion` dinámico en `Revisar contrato` con `{{ $json.validacion_contrato.errores.join('; ') }}`, probar `categoria=NoExiste` y aportar evidencia del mensaje exacto. Guardar nueva versión de export tras verificar.


## Sesión — 03/11/2026: OUTPUT final de regresión verificado

- **Evidencia visual recibida:** captura de n8n del OUTPUT JSON del nodo `Edit Fields2`, con ticket sintético `T02`, `categoria=Finanzas`, `prioridad=Alta` y `referencia_documento=FV-1042`.
- **Verificado en el JSON final:** `validacion_contrato.valido=true`, `validacion_contrato.errores=[]`, y `siguiente_accion="Proponer atención prioritaria y solicitar datos faltantes en paralelo"`. Los seis campos originales se conservan, y el ajuste `Include Other Input Fields` está activo.
- **Conclusión:** regresión del camino válido confirmada tanto por ejecución completa del lienzo como por valores del OUTPUT final. Esto NO prueba integración real con IA ni SAP.
- **Siguiente práctica (no ejecutada todavía):** en nodo `Revisar contrato`, cambiar valor de `motivo_validacion` a Expression `{{ $json.validacion_contrato.errores.join('; ') }}`; usar `categoria=NoExiste` en la entrada; ejecutar y verificar mensaje exacto en OUTPUT JSON del rechazo. Solicitar captura y nuevo export al finalizar, manteniendo historial previo.


## Sesión 03/11/2026 — Rechazo validado; expresión aún literal

- Captura: ticket T02 con categoria NoExiste, contrato valido=false y errores: Categoria no permitida.
- El flujo tomo la rama false y ejecuto Revisar contrato (1 item), con estado_validacion Rechazada.
- Pendiente: motivo_validacion se mostró como texto de fórmula, no como mensaje evaluado. Revisar el modo Expression del campo, volver a ejecutar y capturar el resultado.
- No declarar terminado el mensaje dinámico hasta ver motivo_validacion con la frase de error.


## Sesión 03/11/2026 — Mensaje dinámico confirmado en OUTPUT

- **Evidencia aportada:** captura del panel OUTPUT JSON tras ejecutar el rechazo del Flujo 02 con ticket sintético T02 y `categoria=NoExiste`, `prioridad=Alta`.
- **Contenido del OUTPUT verificado:** `validacion_contrato.valido=false`; `validacion_contrato.errores=["Categoría no permitida"]`; `estado_validacion="Rechazada"`; `motivo_validacion="Categoría no permitida"`.
- **Conclusión:** se corrigió el uso literal de la expresión y se observó su evaluación efectiva. La salida ahora entrega el motivo dinámico del rechazo. La prueba positiva previa con Finanzas/Alta también quedó confirmada.
- **Estado:** comprobado con capturas; todavía no se ha recibido el nuevo export JSON actualizado del Flujo 02 ni se ha integrado un modelo IA o SAP. Las capturas están en la conversación, no como archivos de evidencia del repositorio.
- **Siguiente paso único:** exportar desde n8n la versión actual del Flujo 02 (Download workflow / JSON), compartirla para comprobar estructura, sanitizar metadatos o secretos y versionarla sin sobrescribir `flujo-02-v2-rechazo.json`. Tras eso, comenzar conexión real a IA usando entrada sintética y validar la salida con el contrato ya probado.


## Sesión 03/11/2026 — Export verificado y versionado del Flujo 02 v3

- **Fuente:** export JSON entregado por el alumno, revisado y comparado contra la versión v2 del repositorio.
- **Artefacto nuevo:** [flujo-02-v3-errores-dinamicos.json](../labs/n8n-json-contract/flujo-02-v3-errores-dinamicos.json). Se conservan la v1 y la v2, sin sobrescribirlas.
- **Revisión estática:** 10 nodos, 9 conexiones correctas; nombres e identificadores de nodos únicos; sin credenciales configuradas y sin direcciones de correo en el export. Se retiró exclusivamente meta.instanceId para la versión pública.
- **Cambio respecto de v2:** el campo de mensaje del nodo Revisar contrato pasó de texto genérico a expresión dinámica que une los errores de validacion_contrato. El export utiliza la convención de expresiones de n8n tanto en el valor como en el nombre interno del campo. En captura previa, el OUTPUT se observó correctamente como motivo_validacion=Categoría no permitida.
- **Pruebas observadas en capturas (no contenidas en el export):** ticket T02 Finanzas/Alta recorre la rama true y termina con siguiente_accion prioritaria; ticket T02 NoExiste/Alta recorre rechazo, con valido=false, estado_validacion=Rechazada y motivo_validacion=Categoría no permitida.
- **Límites:** la revisión del archivo fue estática. No se ejecutó el export descargado en un entorno n8n nuevo. La entrada sigue siendo simulada; no hay IA real ni conexión a SAP.
- **Siguiente fase:** Lab 03, conectar un proveedor/modelo de IA usando exclusivamente tickets sintéticos y un contrato validado antes de enrutar; separar salida del modelo, normalización, controles y supervisión humana.


## Sesión 03/11/2026 — Inicio Flujo 03 por duplicación

- **Confirmación del participante:** informa que duplicó el workflow n8n para comenzar Flujo 03. No se recibió todavía captura ni export de la copia, por lo que el nombre y estructura aún no se han comprobado.
- **Propósito:** insertar un Basic LLM Chain y un Groq Chat Model en la copia para comenzar el laboratorio de clasificación real, sin alterar Flujo 02.
- **Paso guiado actual, pendiente de evidencia:** agregar ambos nodos y conectarlos mediante el puerto Model; no ejecutar ni reemplazar todavía el validador, que necesitará normalización de la respuesta del LLM.
- **Seguridad:** credenciales API se configuran directamente dentro de n8n; no publicar claves en capturas, exportaciones ni en GitHub.
- **Estado:** solo duplicación reportada; integración LLM no implementada ni probada.


## Sesión 03/11/2026 — Flujo 03: estructura LLM observada

- **Evidencia:** captura del lienzo n8n titulada `ERP Ticket Lab - Flujo 03 - Clasificación IA real`.
- **Comprobado visualmente:** copia del flujo con los diez nodos del ruteo y rechazo; nuevo nodo `Basic LLM Chain` con `Groq Chat Model` enlazado mediante conexión de subnodo `Model`. La cadena LLM todavía está desconectada de la ruta principal, intencionalmente.
- **Pendiente:** el subnodo Groq muestra advertencia roja; no se han verificado credenciales, modelo ni ejecuciones del LLM. Ninguna integración real confirmada aún. No copiar claves en el repositorio.
- **Siguiente paso de aprendizaje:** crear Groq API Key en la consola, configurar credential cifrada en n8n y seleccionar el modelo disponible, idealmente `llama-3.3-70b-versatile`; pedir captura del nodo mostrando credencial seleccionada y modelo pero no la clave. Conservar la cadena desconectada hasta definir entrada en lenguaje natural, prompt y normalización de salida antes del validador JSON.
- **Teoría abordada:** diferencia entre Basic LLM Chain (orquestación/prompt), Groq Chat Model (motor proveedor/modelo) y API Key (autenticación); separación de responsabilidades y seguridad de secretos.
