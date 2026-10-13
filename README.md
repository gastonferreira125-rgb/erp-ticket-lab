# ERP Ticket Lab

Proyecto de aprendizaje y portafolio de Gastón Ferreira. Clasificación de tickets ERP con IA generativa, datos sintéticos y revisión humana.

## Documentación
- [Alcance y flujo del proyecto](docs/PROJECT.md)
- [Evaluación y límites](docs/EVALUATION.md)
- [Registro de aprendizaje](docs/LEARNING_LOG.md)
- [Plan de publicaciones](docs/LINKEDIN_PLAN.md)
- [Plantilla para registrar experimentos](experiments/TEMPLATE.md)
- [Primera ejecución: T01](experiments/2026-10-13-t01/README.md)

Versión de documentación: 13 de octubre de 2026. Estado: primera ejecución manual registrada (T01); nueve casos pendientes. Configuración actual documentada mediante capturas posteriores a T01: temperatura 1, tokens de salida máximos 43690 y streaming activado. Cada sesión de práctica actualizará el registro de aprendizaje y, cuando corresponda, los experimentos.

## Qué incluye
- tickets.json: 10 tickets ficticios y etiquetas de referencia para el benchmark.
- prompt.txt: instrucciones iniciales listas para probar.
- schema.json: contrato de salida.
- responses.json: una respuesta real registrada para T01; nueve casos pendientes.
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
A learning starter for ERP ticket triage with synthetic cases, a prompt, JSON output contract and local evaluator. No SAP integration is included. One manually collected model response is documented; the current configuration is documented with screenshots captured after the run. Human review is required before operational use.

## Fuentes de estudio
https://learning.sap.com/learning-journeys/solving-business-problems-using-sap-s-generative-ai-hub
https://learning.sap.com/courses/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case
https://learning.sap.com/courses/discovering-sap-s-generative-ai-hub

