# ERP Ticket Lab

Proyecto de aprendizaje y portafolio de Gastón Ferreira. Clasificación de tickets ERP con IA generativa, datos sintéticos y revisión humana.

## Documentación
- [Alcance y flujo del proyecto](docs/PROJECT.md)
- [Evaluación y límites](docs/EVALUATION.md)
- [Registro de aprendizaje](docs/LEARNING_LOG.md)
- [Roles de los mensajes](docs/MESSAGE_ROLES.md)
- [Plan de publicaciones](docs/LINKEDIN_PLAN.md)
- [Plantilla para registrar experimentos](experiments/TEMPLATE.md)
- [Primera ejecución: T01](experiments/2026-10-13-t01/README.md)
- [Segunda ejecución: T02](experiments/2026-10-13-t02/README.md)
- [T10 con v0: fallo observado](experiments/2026-10-13-t10-v0/README.md)
- [v1 con roles separados: resultado T10](experiments/2026-10-13-t10-v1/README.md)
- [v2 con regla explícita: resultado T10](experiments/2026-10-14-t10-v2/README.md)
- [T02-v2: prueba de regresión](experiments/2026-10-14-t02-v2/README.md)
- [T05-v2: fallo de categoría](experiments/2026-10-14-t05-v2/README.md)
- [T05-v3: categoría conforme](experiments/2026-10-14-t05-v3/README.md)
- [T06-v3: solicitud de reporte](experiments/2026-10-14-t06-v3/README.md)

Versión de documentación: 14 de octubre de 2026. Estado: 38 ejecuciones sobre doce tickets distintos. **Ronda v3 completa: 10/10 respuestas cumplen controles de formato y 7/10 coinciden con todas las etiquetas esperadas.** Categorías 9/10, prioridades 10/10, referencias 8/10. T03 y T04 omiten referencias; T07 devuelve Ventas en lugar de Integraciones. T04 presenta además ambigüedad entre el nombre del campo referencia_documento y el código de artículo esperado. Revisión humana y casos pendientes de mejora están documentados en la ronda.

- [Ronda completa v3: respuestas, evaluación y límites](experiments/2026-10-14-v3-round/README.md)
- [T10-v3: prueba de regresión](experiments/2026-10-14-t10-v3/README.md)
- [T04-v3: referencia y ambigüedad del contrato](experiments/2026-10-14-t04-v3/README.md)

T01, T02 y T10 conservan etiquetas previamente correctas en las ejecuciones de v3. Las versiones anteriores tienen cobertura distinta y no constituyen una comparación completa. La configuración solicitada es Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690 y streaming activado; valores actuales y guardado de plantilla SAP pendientes de confirmar. Las respuestas originales se conservan sin corregir.

## Avance de v4 y siguiente versión
Conjunto original: T07/T08/T10 conformes, 3/3 entre ejecutados y cobertura 3/10. Complementarios: [T11](experiments/2026-10-14-t11-v4/README.md) conforme y [T12](experiments/2026-10-14-t12-v4/README.md) falla referencia (null en lugar de OV-3301): 1/2 coincidencias completas. T12 clasifica correctamente Ventas pese a mencionar la tienda. v3 conserva 7/10 por separado.

[v5-reference-rule](prompts/v5-reference-rule/README.md) con primera ejecución registrada: aclara copia de referencias y alcance del campo para documentos/códigos de artículo. Conservar versiones y resultados sin corregir. No sumar conjuntos distintos para presentar exactitud general.

## Ronda v5 completa
[Ronda v5 y comparación con v3](experiments/2026-10-14-v5-round/README.md): 10/10 respuestas originales cumplen formato y coinciden con todas las etiquetas, frente a 7/10 en v3 sobre el mismo conjunto. Categorías, prioridades y referencias: 10/10 cada una en v5. T12 complementario conforme (1/1), separado.

Revisión humana: siguen faltando impacto en resumen T02, datos útiles en listas vacías, y concreción/uso de información ya aportada en T04/T08. No es exactitud general ni respuesta perfecta; una ejecución por caso y casos usados para ajustar limitan generalización. La configuración actual no se reconfirmó totalmente y hubo restauración de sesión.

[Controles v6 consolidados](experiments/2026-10-14-v6-controls/README.md): cinco ejecuciones sobre cuatro tickets únicos, todas conformes en formato/etiquetas; cobertura única 4/10. T02 (dos veces) y T04 dejan listas vacías, T06/T10 piden información pertinente. La regla general no mejoró uniformemente datos_faltantes en estos casos. No es ronda completa ni exactitud general.

[v7-few-shot](prompts/v7-few-shot/README.md) preparada, sin resultados: mismo System v6 y dos pares de ejemplos Usuario/Asistente externos al benchmark, antes del ticket real. Las respuestas de ejemplos son demostraciones del tutor, no resultados medidos. Próximo T02 con seis mensajes.

## Qué incluye
- tickets.json: 10 tickets ficticios y etiquetas de referencia para el benchmark.
- prompt.txt: instrucciones iniciales listas para probar.
- schema.json: contrato de salida.
- responses.json: salidas originales completas de T01, T02 y T10 con v0.
- evaluate.py: evaluación local de respuestas guardadas, sin dependencias externas.
- experiments/2026-10-14-v3-round/: diez salidas originales de v3 y evaluación consolidada.

Los scripts no se conectan a SAP Business One ni llaman a un modelo. Las pruebas se ejecutan manualmente en SAP AI Launchpad y se guardan para evaluación. La primera respuesta y sus límites de trazabilidad están documentados en el experimento.

## Primer ejercicio, sin programar
1. Abrí prompt.txt.
2. Identificá tarea, reglas, formato y dato de entrada.
3. Reescribí la instrucción con tus palabras.
4. Proba un ticket en un modelo disponible y pegá el JSON que devolvió.
5. Revisá si inventó información. Repetí con los casos 02 y 10.

## Guardar y evaluar
responses.json debe contener una lista JSON. Cada elemento es la respuesta real de un modelo a un ticket.
Ejemplo de estructura, no resultado medido:
```json
[{
  "ticket_id": "T01",
  "categoria": "Finanzas",
  "prioridad": "Media",
  "resumen": "El usuario no puede registrar un pago a un proveedor.",
  "referencia_documento": null,
  "datos_faltantes": ["Mensaje exacto de error", "Pasos para reproducir", "Alcance del impacto"]
}]
```
Ejecutá:
```sh
python3 evaluate.py experiments/2026-10-14-v3-round/responses.json
```
Se informa cobertura, cumplimiento del esquema, coincidencia de etiquetas y referencias no presentes en el texto.
La exactitud del resumen y la utilidad de los datos faltantes deben revisarse manualmente.
Las etiquetas son convenciones de esta demo; no constituyen una política universal de SAP o de soporte.

## Comparación de modelos
Registrá proveedor, modelo, versión, fecha, parámetros, prompt exacto y cada respuesta sin corregirla.
Usá los mismos casos y reglas. Conservá respuestas con JSON inválido para documentar el error; el evaluador requiere un archivo JSON válido y esas fallas se registran aparte.
No uses respuestas esperadas como si fueran salidas del modelo.
No prometas ahorros o exactitud antes de medirlos.

## Tres publicaciones futuras
1. Problema y diseño: cómo convertir tickets libres en información útil para soporte ERP.
2. Experimento: comparación de modelos, casos que fallan y ajustes al prompt.
3. Demo y límites: validación humana, datos sintéticos y próximos pasos de integración.

Prepará las publicaciones cuando existan resultados reales. El primer post puede mostrar el diseño y decir que el experimento está en curso.

## English overview
A learning portfolio for ERP ticket triage with synthetic cases, versioned prompts, a JSON contract and a local evaluator. Complete rounds cover the same ten original cases: v3 matches all reference labels in 7/10 responses; v5 in 10/10. Both pass format checks. v5 also clarifies the contract for item identifiers. Human review still finds lost business impact, missing useful information and redundant or vague requests. A separate T12 result is not included in original-set metrics. One response per case, calibration on evaluation cases and partially unverified parameters do not establish general production accuracy. No operational ERP integration or model comparison is included. Five v6 responses cover four unique original cases (T02 twice, T04, T06 and T10), all matching labels. T02/T04 omit useful investigation data; T06/T10 request relevant information. Unique coverage is 4/10. v7 is prepared with two synthetic user/assistant demonstrations outside the evaluation set; no v7 result has been received. User-provided system text matches v6; actual payloads and numerical parameters remain unverified.

## Fuentes de estudio
https://learning.sap.com/learning-journeys/solving-business-problems-using-sap-s-generative-ai-hub
https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case
https://learning.sap.com/courses/discovering-sap-s-generative-ai-hub

