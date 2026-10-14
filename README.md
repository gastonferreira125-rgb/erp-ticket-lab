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

Versión de documentación: 14 de octubre de 2026. Estado: ocho ejecuciones guardadas sobre cuatro tickets distintos. En v0 se ejecutaron T01, T02 y T10; T10 falló prioridad y revisión de contenido. T10-v1 mantuvo el fallo y añadió una referencia no válida. En v2, T10 y T02 cumplen etiquetas y revisión humana; T05 falla categoría (Reportes en lugar de Autorizaciones). T05-v3 devuelve Autorizaciones y pasa etiquetas y revisión humana. T06 y las regresiones de v3 siguen pendientes. Seis casos del conjunto aún no se ejecutaron. Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690 y streaming activado. Los valores actuales y el guardado de plantilla en SAP siguen pendientes de confirmar. Cada sesión conserva respuestas originales, revisión humana y límites del experimento.

## Qué incluye
- tickets.json: 10 tickets ficticios y etiquetas de referencia para el benchmark.
- prompt.txt: instrucciones iniciales listas para probar.
- schema.json: contrato de salida.
- responses.json: salidas originales completas de T01, T02 y T10 con v0.
- evaluate.py: evaluación local de respuestas guardadas, sin dependencias externas.

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
python3 evaluate.py responses.json
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
A learning starter for ERP ticket triage with synthetic cases, a prompt, JSON output contract and local evaluator. No SAP integration is included. Three complete manual runs pass format checks; two match reference labels. T02 has a missing-information finding and T10 fails priority and human content review. A separate T10 run with system/user roles still fails priority and summary review, and also fails document reference. The explicit-rule version has one T10 response matching reference labels and passing human content review; a T02 regression check also passes labels and human review. T05-v2 fails category (Reports instead of Authorizations), and the first T05-v3 response matches labels and passes human review. These cases do not establish general protection; the current configuration is documented with screenshots captured after the run. Human review is required before operational use.

## Fuentes de estudio
https://learning.sap.com/learning-journeys/solving-business-problems-using-sap-s-generative-ai-hub
https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case
https://learning.sap.com/courses/discovering-sap-s-generative-ai-hub

