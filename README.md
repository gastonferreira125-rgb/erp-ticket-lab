# ERP Ticket Lab

Proyecto de aprendizaje y portafolio de Gastón Ferreira: clasificación de tickets ERP con IA generativa, casos sintéticos, prompts versionados y evaluación.

## Estado — 15 de octubre de 2026
**Etapa de prompts cerrada con v8 como referencia.** Se completaron los cuatro controles finales acordados, sin abrir otra versión. [Conclusión y pendientes](docs/STAGE_1_CLOSURE.md).

- 48 respuestas registradas entre versiones, sobre trece tickets distintos: diez originales y tres complementarios.
- Últimos controles v8: formato/etiquetas 4/4 entre ejecutados, cobertura 4/10 del conjunto original.
- T02 ahora pide error exacto y pasos; con v7 dejó lista vacía en dos ejecuciones.
- T04/T06/T10 conservan comportamiento pertinente en los controles observados.
- Análisis cualitativo asistido por IA pendiente de validación humana, salvo intervenciones explícitas. No hay una puntuación humana agregada.

[Comparación completa de los cuatro casos v7–v8](experiments/2026-10-15-v8-controls/README.md). Estos resultados no prueban exactitud general, causalidad o preparación para producción.

## Etapa 2 — aprendizaje de orquestación
[Lección y diseño funcional](docs/STAGE_2_ORCHESTRATION.md): clasificar, validar y decidir el tratamiento. [Práctica 2: reglas y transiciones con T02/T06](docs/STAGE_2_PRACTICE_02.md). Diseño didáctico sin implementación; v8 permanece congelada. Gastón respondió el criterio de atención y recopilación en paralelo para T02; en el ejercicio de transiciones identificó que cambia el estado de la información. La guía aclara que eso permite investigar sin demostrar resolución.

## Recuperar la plantilla
- [Sistema v8 completo](prompts/v8-transaction-investigation/system.txt).
- [Seis mensajes con ejemplos y último Usuario T02](prompts/v8-transaction-investigation/messages-t02.json).
- [Respaldo XML v8](prompts/v8-transaction-investigation/backup/ERP_Tickets_v8_FewShot.xml).
- [Instrucciones del respaldo](prompts/v8-transaction-investigation/backup/README.md).
- [Respaldo XML anterior v7](prompts/v7-few-shot/backup/ERP_Tickets_v7_FewShot.xml).

El usuario informó que el guardado nativo en Launchpad no conserva su plantilla. Los XML son formato propio legible para reconstrucción manual; importación directa a SAP no verificada. No contienen credenciales ni capturas.

## Resultados por versión, sin mezclar conjuntos
| Versión | Alcance original | Formato / etiquetas entre ejecutados | Referencia |
| --- | --- | --- | --- |
| v3 | Ronda completa, 10 casos | 10/10 formato; 7/10 etiquetas | [Ronda](experiments/2026-10-14-v3-round/README.md) |
| v5 | Ronda completa, 10 casos | 10/10 formato y etiquetas | [Ronda y revisión](experiments/2026-10-14-v5-round/README.md) |
| v6 | 5 ejecuciones, 4 casos únicos | 5/5 formato y etiquetas; cobertura 4/10 | [Controles](experiments/2026-10-14-v6-controls/README.md) |
| v7 | 5 ejecuciones, 4 casos únicos | 5/5 formato y etiquetas; cobertura 4/10 | [Controles y repetición](experiments/2026-10-15-v7-controls/README.md) |
| v8 | 4 ejecuciones, 4 casos únicos | 4/4 formato y etiquetas; cobertura 4/10 | [Cierre](experiments/2026-10-15-v8-controls/README.md) |

Casos complementarios se informan aparte: [T11-v4](experiments/2026-10-14-t11-v4/README.md), [T12-v4](experiments/2026-10-14-t12-v4/README.md), [T12-v5](experiments/2026-10-14-t12-v5/README.md) y [T13-v7](experiments/2026-10-15-t13-v7/README.md). No se agregan al denominador de diez casos originales.

Una coincidencia de etiquetas no demuestra fidelidad completa del resumen ni utilidad de las preguntas. Los errores originales se conservan; el análisis del tutor IA no equivale a aprobación de una persona.

## Documentación de estudio
- [Conceptos con ejemplos de nuestros tickets](docs/CONCEPTS.md).
- [Alcance y flujo del proyecto](docs/PROJECT.md).
- [Evaluación y distinción de revisores](docs/EVALUATION.md).
- [Registro completo de aprendizaje](docs/LEARNING_LOG.md).
- [Roles de los mensajes](docs/MESSAGE_ROLES.md).
- [Plan de publicaciones](docs/LINKEDIN_PLAN.md).
- [Plantilla de experimentos](experiments/TEMPLATE.md).

Cada práctica combina teoría en español, término en inglés, ejemplo ERP y comprobación de comprensión. Las preguntas didácticas no se consideran respondidas automáticamente.

## Archivos y ejecución local
- tickets.json: diez tickets originales con etiquetas de referencia.
- schema.json: contrato de seis campos; evaluate.py implementa chequeos propios, no un motor completo de JSON Schema.
- prompt.txt: prompt inicial v0; las versiones posteriores están en prompts/.
- responses.json: tres respuestas iniciales v0, no los resultados finales.
- experiments/: respuestas originales por versión y sus evaluaciones.

Ejemplo:
```sh
python3 evaluate.py experiments/2026-10-15-v8-controls/responses.json
```

El evaluador informa cobertura, campos/tipos, coincidencia de etiquetas, ids y presencia literal de referencias. No evalúa por sí solo la fidelidad del resumen, causa inventada, validez semántica de referencias o utilidad de datos_faltantes. Casos no ejecutados se identifican como ausentes; no son fallos observados.

Las etiquetas esperadas del ticket real no se incluyen en el prompt. EX01/EX02 son demostraciones preparadas, externas al conjunto original; no son ejecuciones medidas ni fine-tuning.

## Entorno y límites
Pruebas manuales en SAP AI Launchpad / Generative AI Hub. Modelo indicado: Gemini 2.5 Flash Lite (001). Configuración actual verificada en capturas posteriores de v7: seis bloques/roles/ids, temperatura 1, streaming activado. El valor seleccionado exacto de tokens no quedó visible: 43690 fue solicitado y 65536 es el extremo del control. No se verificaron todos los textos íntegros/payloads efectivos, ni retrospectivamente todas las ejecuciones.

No hay integración operativa al ERP, medición de tiempos/ahorros ni comparación de modelos. Skill y MCP se estudiaron; no hay skill propia instalada o MCP ERP implementado. [Pendientes](docs/STAGE_1_CLOSURE.md#pendientes-posteriores-sin-bloquear-este-cierre-educativo).

## English overview
Educational ERP ticket triage portfolio with synthetic cases, versioned prompts, original model outputs, a six-field JSON contract and a local evaluator. The prompt stage is closed with v8 as the reference for the next exercise. Four v8 controls pass format/reference-label checks (4/10 original-set coverage). T02 requests missing error information and reproduction steps after two empty v7 lists; T04/T06/T10 preserve relevant behavior in the observed controls. AI-assisted qualitative comments still require human validation. One response per v8 case, calibration on known cases and incomplete payload/parameter verification do not establish broad reliability or production readiness. Forty-eight recorded responses span thirteen distinct tickets across versions; complementary cases and version metrics stay separate.

## Fuentes de estudio
- https://learning.sap.com/learning-journeys/solving-business-problems-using-sap-s-generative-ai-hub
- https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case
- https://learning.sap.com/courses/discovering-sap-s-generative-ai-hub
