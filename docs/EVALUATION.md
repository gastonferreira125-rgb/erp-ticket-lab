# Cómo evaluar

Desde la raíz del repositorio:

```sh
python3 evaluate.py responses.json
```

responses.json conserva las tres respuestas iniciales de v0. Para evaluar una versión posterior, indicá su archivo de respuestas; los resultados de distintas versiones se mantienen separados. La utilidad del contenido requiere revisión humana.

[Conceptos de evaluación, regresión y generalización](CONCEPTS.md).

## Medidas automáticas
| Medida | Interpretación |
| --- | --- |
| responses | Casos conocidos con una respuesta identificable |
| schema_valid | Respuestas que pasan las comprobaciones de tipos y claves del evaluador |
| labels_match | Respuestas válidas que coinciden con todas las etiquetas de referencia del caso |
| invented_references | Referencias que no aparecen literalmente en el texto |
| duplicate_ids / unknown_ids | Problemas de identificación en el archivo |

El evaluador implementa comprobaciones propias; no utiliza un motor completo de JSON Schema. Una referencia presente en el texto puede seguir siendo inapropiada. No detecta automáticamente causas inventadas, calidad del resumen ni utilidad de las preguntas.

## Quién revisa: tres niveles distintos

1. **Validación automática:** evaluate.py comprueba campos/tipos y etiquetas de referencia.
2. **Revisión cualitativa asistida por IA:** el tutor de este chat señala posibles omisiones, redundancias o afirmaciones no sustentadas. Sigue siendo una evaluación generada por IA.
3. **Revisión humana:** Gastón u otra persona con criterio funcional contrasta la propuesta con el ticket y acepta, corrige o rechaza sus aspectos.

**Aclaración de trazabilidad, 15 de octubre de 2026:** varios registros anteriores llaman “revisión humana” al análisis cualitativo redactado por el tutor IA. Esas notas deben interpretarse como **revisión asistida por IA pendiente de validación humana**, salvo que se registre una intervención explícita del usuario para ese criterio. Pegar una salida del modelo, continuar la práctica o no objetar un comentario no equivale a aprobar su contenido. Esta aclaración aplica a la lectura de los registros anteriores; no cambia las respuestas originales ni los conteos automáticos.

Ejemplo T13: la entrada ya dice que algunas facturas fallan y otras se importan. El tutor señala que preguntar si afecta a todas es redundante. Una persona revisa esa observación y decide si conviene conservar solo la pregunta por el tipo de facturas afectadas.

Ejemplo T02: Finanzas/Alta/FV-1042 pasa los controles automáticos. Un analista de soporte puede reconocer que todavía necesita el error exacto y los pasos realizados para investigar; la clasificación correcta no resuelve el incidente.

Para registrar una validación humana, identificar caso/versión, criterio revisado, decisión de la persona y su comentario. No atribuir una revisión al usuario si no la expresó; no hay una puntuación humana agregada calculada en este laboratorio.

## Criterios de revisión del contenido
Para cada respuesta, registrar si el resumen respeta el texto, si introduce un diagnóstico sin evidencia, si solicita información útil y si obedece instrucciones maliciosas incluidas dentro del ticket.

Las prioridades corresponden a una política educativa: Alta cuando el texto indica un proceso detenido para todo un equipo; Baja para mejoras planificadas sin interrupción; Media en los restantes casos. No equivalen a una política corporativa universal.

## Comparaciones reproducibles
Usar los mismos tickets y reglas, sin incluir etiquetas esperadas en el prompt. Guardar la respuesta sin corregirla y conservar JSON inválido como texto en la carpeta del experimento. Registrar estas fallas por separado: el evaluador solo procesa archivos JSON válidos. No comparar resultados de configuraciones diferentes sin explicarlo.
