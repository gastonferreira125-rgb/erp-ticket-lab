# Conceptos del laboratorio ERP

Guía de estudio en español con términos en inglés. Cada concepto incluye una explicación, un ejemplo del laboratorio y una comprobación de comprensión. Se amplía al introducir nuevas técnicas; documentar un concepto no significa haber implementado esa capacidad.

## 1. Prompt e ingeniería de prompts (prompt engineering)

Un prompt es el conjunto de mensajes que recibe el modelo para realizar una tarea. En el laboratorio contiene instrucciones, el ticket y, desde la propuesta v7, ejemplos. La ingeniería de prompts consiste en diseñar y probar esos mensajes.

**Ejemplo:** añadir la regla de Autorizaciones en v3 para distinguir un permiso faltante de un problema con los datos de un reporte. El resultado debe evaluarse, no darse por mejor solo porque la regla parece clara.

**Comprobación:** ¿qué diferencia hay entre cambiar una regla de clasificación y cambiar el texto del ticket?

## 2. Roles: Sistema, Usuario y Asistente (System, User, Assistant)

En nuestra plantilla, Sistema contiene las reglas; Usuario contiene el ticket; Asistente puede contener respuestas de ejemplo. El rol indica cómo se presenta un mensaje al modelo. Un bloque Asistente escrito por nosotros es contexto de entrada, no una ejecución nueva.

**Ejemplo:** v7 propone seis mensajes: Sistema, Usuario EX01, Asistente EX01, Usuario EX02, Asistente EX02 y Usuario T02. Los ejemplos orientan la tarea antes de clasificar T02.

**Comprobación:** ¿dónde pondrías el ticket real y dónde la respuesta preparada de EX01?

[Detalle e historia de los roles](MESSAGE_ROLES.md).

## 3. Sin ejemplos y con pocos ejemplos (zero-shot / few-shot prompting)

Zero-shot presenta la tarea sin demostraciones. Few-shot incorpora unos pocos pares de entrada y respuesta para mostrar el patrón deseado. Es una técnica de contexto, no un entrenamiento permanente del modelo.

**Ejemplo:** v6 usa reglas y ticket; v7 mantiene Sistema v6 y añade EX01/EX02 para mostrar cómo pedir datos ausentes útiles. Esos ejemplos fueron escritos por el tutor y no cuentan como resultados del modelo.

**Comprobación:** ¿por qué debemos guardar los ejemplos por separado de las respuestas medidas?

[Preparación v7](../prompts/v7-few-shot/README.md). Fuente conceptual: [Google, estrategias de prompts](https://ai.google.dev/gemini-api/docs/prompting-strategies).

## 4. Skill

Una skill reúne instrucciones reutilizables y recursos para realizar una tarea. En ChatGPT/Codex se describe en un archivo SKILL.md y puede incluir referencias, plantillas o scripts. Indica cuándo aplicar el procedimiento y cómo completarlo.

**Ejemplo conceptual: “Revisar pruebas de tickets ERP”.**

1. Recibir el ticket original y la respuesta del modelo.
2. Comprobar las seis claves, los tipos y las etiquetas esperadas.
3. Revisar fidelidad del resumen y utilidad de datos_faltantes.
4. Conservar la respuesta original y registrar la evaluación.
5. Guardar la documentación autorizada en GitHub.
6. Proponer un siguiente caso de prueba.

Si T04 devuelve datos_faltantes vacío, este procedimiento indicaría revisar si contamos con las cantidades del sistema y del conteo físico, además de la fecha del conteo. Es una propuesta didáctica: **no hay una skill propia del laboratorio instalada**.

Una skill puede incluir un prompt o ejemplos, pero esos elementos cumplen funciones distintas:

| Elemento | Función en nuestro laboratorio |
| --- | --- |
| Prompt | Pedir al modelo una clasificación conforme a las reglas. |
| Few-shot | Mostrar ejemplos de cómo resolver esa tarea. |
| Skill | Organizar el procedimiento de revisión, registro y seguimiento. |
| Herramienta (tool) | Ejecutar una acción concreta, como leer un archivo de GitHub. |

**Comprobación:** ¿qué pasos de esa skill ocurren después de que Gemini haya respondido?

Fuente: [OpenAI, Skills](https://developers.openai.com/plugins/concepts/skills).

## 5. Clasificación, extracción y diagnóstico

Clasificar asigna una categoría y prioridad. Extraer copia información del texto en un campo. Diagnosticar busca la causa del incidente; requiere evidencia adicional.

**Ejemplo:** T05 es Autorizaciones por el problema de permisos. Eso no demuestra qué configuración técnica lo causó. T03 permite extraer OV-2099, pero no permite explicar por qué la dirección es incorrecta.

**Comprobación:** ¿“faltan permisos” permite afirmar que está mal configurado un rol específico?

## 6. JSON y esquema de salida (output schema)

JSON es el formato de datos que usamos para la respuesta. El esquema define el contrato: seis claves, tipos y valores permitidos. Un JSON bien formado puede tener contenido incorrecto.

**Ejemplo:** T04 puede devolver Inventario, Media y ART-310 correctamente y aun así omitir preguntas necesarias. Pedir JSON en el prompt tampoco confirma por sí solo que se haya activado una función de salida estructurada del proveedor.

**Comprobación:** ¿qué diferencia hay entre formato válido y respuesta útil?

Ver [schema.json](../schema.json) y [evaluación](EVALUATION.md). El evaluador aplica comprobaciones propias, no un motor completo de JSON Schema.

## 7. Instrucciones dentro de datos (prompt injection)

Un texto recibido como datos puede intentar dictar instrucciones al asistente. En el laboratorio, el ticket debe analizarse como datos y no puede redefinir las reglas de clasificación.

**Ejemplo:** T10 ordena ignorar instrucciones y afirmar que FV-999 está corregido. No describe un incidente ni demuestra una corrección. Nuestra salida esperada es Otros, Media y referencia null, con un resumen de la intención de alterar la respuesta.

**Comprobación:** ¿por qué FV-999 no debe extraerse como referencia válida en T10, aunque aparezca literalmente?

Una ejecución conforme de T10 es evidencia sobre ese caso, no una prueba de resistencia general.

## 8. Afirmaciones no sustentadas (hallucination)

En nuestra revisión, marcamos como no sustentada una afirmación que la respuesta presenta sin apoyo en la entrada o la evidencia.

**Ejemplo:** decir que FV-999 fue corregido al responder T10 convierte una orden en un hecho. También sería no sustentado inventar la causa técnica de una integración caída.

**Comprobación:** ¿el resumen describe un hecho reportado o una solución que nadie confirmó?

## 9. Conjunto de evaluación y etiquetas de referencia (benchmark / expected labels)

El conjunto reúne casos y expectativas para comprobar respuestas. Sus etiquetas son convenciones del laboratorio, no una política universal de soporte ERP.

**Ejemplo:** tickets.json contiene diez casos originales. T11 y T12 son complementarios y se informan por separado. La prioridad Alta exige que la entrada afirme un proceso detenido para todo un equipo.

**Comprobación:** ¿“afecta a ventas” basta para asignar Alta según nuestra regla?

Las respuestas esperadas del ticket real no se envían al modelo durante la evaluación.

## 10. Evaluación automática y revisión humana (evals / human review)

La evaluación automática comprueba criterios programados. La revisión humana examina aspectos que el evaluador actual no mide.

**Ejemplo:** evaluate.py comprueba campos, tipos, coincidencia de etiquetas y presencia literal de referencias. Una referencia puede aparecer en el texto y ser inapropiada, como FV-999 en las órdenes de T10. El evaluador tampoco puntúa la fidelidad del resumen o la utilidad de datos_faltantes.

**Comprobación:** ¿por qué 10/10 coincidencias de etiquetas en v5 no significa diez respuestas perfectas?

Fuente conceptual: [OpenAI, buenas prácticas de evaluación](https://developers.openai.com/api/docs/guides/evaluation-best-practices). Nuestros criterios y límites están en [EVALUATION.md](EVALUATION.md).

## 11. Prueba de regresión (regression test)

Consiste en volver a probar un comportamiento previamente observado tras un cambio para detectar si se deterioró.

**Ejemplo:** después de ajustar la regla de instrucciones para T10, repetimos T02. Después de aclarar referencias, volvimos a T10 para comprobar que una referencia incluida solo en una orden siguiera siendo null.

**Comprobación:** ¿qué caso volverías a probar después de añadir la regla de Integraciones y por qué?

Superar un control no garantiza que todos los demás casos sigan funcionando.

## 12. Generalización y contaminación de la evaluación (generalization / test leakage)

Generalizar es aplicar el criterio a entradas nuevas. La evaluación pierde independencia cuando las respuestas de sus casos se incluyen como ejemplos o se usan repetidamente para ajustar la solución.

**Ejemplo:** T11 fue preparado antes de observar su resultado con v4. T12 fue nuevo para v4, pero luego se usó para motivar v5: ya no es una prueba independiente de esa versión. EX01/EX02 son distintos de T01–T12, aunque eso por sí solo no garantiza ausencia de sesgo.

**Comprobación:** ¿qué podríamos concluir de un caso nuevo correcto y qué todavía no podríamos concluir?

## 13. Versionado, repetición y trazabilidad (versioning / repeatability / traceability)

Versionar conserva las distintas instrucciones. Repetir ayuda a observar consistencia o variación. La trazabilidad conecta la entrada, la configuración, la respuesta original y su evaluación.

**Ejemplo:** T02 se ejecutó dos veces con v6 y ambas respuestas quedaron guardadas. Eso son dos ejecuciones de un ticket, no dos tickets distintos. No corregimos la salida original para que coincida con lo esperado.

**Comprobación:** ¿por qué conservar un resultado fallido junto a la versión que lo produjo?

Las pruebas del modelo son manuales en SAP AI Launchpad; el script local evalúa respuestas guardadas. El laboratorio no tiene una integración operativa con SAP ERP.

## 14. Parámetros de generación (temperature / max output tokens)

Temperature influye en la selección de la salida durante la generación; el máximo de tokens limita su longitud. Cambiar parámetros también cambia la configuración del experimento.

**Ejemplo:** en este laboratorio solicitamos conservar modelo y parámetros al comparar prompts. Los valores de la sesión restaurada no quedaron totalmente reconfirmados; eso limita la fuerza de las comparaciones. Reducir temperature no demuestra que una clasificación sea correcta.

**Comprobación:** ¿por qué conviene no cambiar a la vez reglas, ejemplos y parámetros?

Referencia: [Google, parámetros de prompts](https://ai.google.dev/gemini-api/docs/prompting-strategies).

## 15. MCP y su relación con las skills (Model Context Protocol)

MCP es un protocolo abierto que estandariza cómo una aplicación de IA se comunica con herramientas y datos externos. Un servidor MCP expone capacidades; el cliente de la aplicación las descubre y permite invocarlas. La operación la ejecuta el servidor y devuelve un resultado que el asistente puede usar.

Una skill aporta el procedimiento para usar esas capacidades: qué revisar, en qué orden y cómo presentar el resultado. Puede funcionar con herramientas MCP, con otras herramientas o solo con instrucciones y recursos.

| Concepto | Función | Ejemplo aplicado |
| --- | --- | --- |
| Prompt | Define la tarea que recibe el modelo. | Clasificar un ticket con seis campos JSON. |
| Skill | Describe un procedimiento reutilizable. | Revisar el resultado, evaluar y documentar la prueba. |
| MCP | Estandariza la comunicación con capacidades externas. | Acceder a herramientas del conector GitHub. |
| Herramienta (tool) | Ejecuta una operación concreta. | Leer docs/CONCEPTS.md o crear un commit. |
| API | Interfaz de un sistema para operaciones y datos. | Una integración futura podría usar una API del ERP detrás de un servidor MCP. |

**Ejemplo real del laboratorio:** al actualizar la guía, el asistente usa las herramientas del conector GitHub disponibles mediante MCP para leer los archivos, preparar los cambios y guardarlos en un commit. El procedimiento de revisar, guardar y verificar podría empaquetarse en nuestra skill conceptual “Revisar pruebas de tickets ERP”. No hay una skill propia instalada todavía.

**Ejemplo futuro, no implementado:** un servidor MCP para el ERP podría exponer una herramienta consultar_factura con el identificador FV-1042. El asistente podría solicitar esa consulta y usar su resultado como evidencia adicional. Eso necesitaría una integración concreta y permisos para la operación. Nombrar una herramienta no la crea ni da acceso al ERP.

En nuestro estado actual, Gemini clasifica manualmente en SAP AI Launchpad el texto que pegamos. No consulta SAP ERP por MCP. La conexión GitHub usada desde este chat es distinta de la ejecución del modelo en Launchpad.

**Ejercicio:** imaginá una skill que revisa T04. Identificá el paso que se resuelve leyendo el ticket, el que requeriría consultar stock real y el que guarda el informe en GitHub.

**Comprobación:** ¿qué aporta la skill y qué aporta el servidor MCP? ¿Qué conexión adicional necesitaríamos para consultar stock del ERP?

Fuente: [OpenAI, MCP server](https://developers.openai.com/plugins/concepts/mcp-server) y [relación entre skills y MCP](https://developers.openai.com/plugins/concepts/skills).

## Método para las próximas prácticas

Cada concepto nuevo se documentará con explicación en español, término en inglés, ejemplo ERP, ejercicio y comprobación de comprensión. Se enlazará al experimento donde se aplica y se distinguirá entre preparado, ejecutado y verificado.

El glosario es material de estudio; sus preguntas no se consideran respondidas ni aprobadas automáticamente. Continuaremos de a un concepto por práctica.

Al 15 de octubre de 2026, v7 tiene una [respuesta registrada de T02](../experiments/2026-10-15-t02-v7/README.md): formato/etiquetas conformes, datos_faltantes vacío. EX01/EX02 son contexto con respuestas preparadas; no se espera una salida nueva por ejemplo. La salida de esta prueba corresponde al último Usuario. No hay una skill propia instalada. La [respuesta T04-v7](../experiments/2026-10-15-t04-v7/README.md) pide cantidades y fecha sin repetir almacén: aplicación útil de un patrón cercano a EX02, no prueba de generalización amplia. v7 cubre 4/10 tickets; [T06](../experiments/2026-10-15-t06-v7/README.md) conserva Reportes/Baja y pide campos/formato: control de regresión conforme en esta ejecución. [T10-v7](../experiments/2026-10-15-t10-v7/README.md) conserva el criterio de instrucciones en datos. Próximo ejercicio: [T13 nuevo para v7](../tickets/generalization-v7-t13.md), con expectativas previas, conservando ejemplos/Sistema y cambiando solo último Usuario. Se evaluará por separado; es una variante cercana a T11, no prueba de generalización amplia.
