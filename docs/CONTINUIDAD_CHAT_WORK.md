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
