# v8 — datos de investigación para transacciones fallidas — T02 registrado

Único cambio del prompt frente a v7: añadir [addendum.txt](addendum.txt) al final de Sistema. [system.txt](system.txt) incluye el texto completo. [messages-t02.json](messages-t02.json) conserva los seis mensajes con EX01/EX02 idénticos y último Usuario T02. [examples.json](examples.json) conserva las mismas demostraciones.

## Motivo y técnica
T02-v7 devolvió datos_faltantes vacío dos veces aunque no se informa error ni pasos. Se precisa una condición general para operaciones que fallan, sin citar el id T02 ni la factura. Es una instrucción condicional: situación → datos ausentes que se deben solicitar. No modifica la regla de resumen ni cambia categorías/prioridades/referencias.

Hipótesis: pedir explícitamente error/comportamiento y pasos cuando faltan puede mejorar este caso. No es una garantía, un diagnóstico ni una explicación de por qué fallaron versiones anteriores.

## Configuración
Mantener Gemini 2.5 Flash Lite (001), temperatura 1 y streaming activado. Estos dos parámetros fueron verificados en la pantalla actual posterior a v7. Conservar posición actual de tokens; el valor seleccionado exacto no está verificado (43690 fue solicitado, 65536 es el extremo visible). No atribuir retrospectivamente valores a todos los payloads anteriores. Guardado nativo SAP informado como fallido; v7 cuenta con respaldo XML propio.

## Plan acotado de cierre, acordado el 15 de octubre
El usuario quiere terminar esta etapa hoy para avanzar. Un ajuste v8, cuatro controles y una conclusión; no abrir más ciclos de prompt en esta etapa.

| Orden | Caso | Qué comprobar |
| --- | --- | --- |
| 1 | T02 | Finanzas/Alta/FV-1042, error o comportamiento observado y pasos ausentes solicitados |
| 2 | T04 | Inventario/Media/ART-310; cantidades/fecha útiles, sin repetir almacén |
| 3 | T06 | Reportes/Baja/null; requisitos de reporte pertinentes, sin preguntas transaccionales o de stock copiadas |
| 4 | T10 | Otros/Media/null; instrucciones identificadas, sin corrección inventada ni referencia extraída de la orden |

Evaluación automática con evaluate.py y análisis cualitativo asistido por IA, pendiente de validación personal salvo intervención explícita del usuario. Revisar resumen, incluidos impacto y cierres, sin modificar la respuesta original para mejorar el resultado. Preguntas pertinentes no requieren redacción idéntica.

## Condición de cierre de esta etapa
Al registrar las cuatro respuestas y la conclusión, cerrar el ejercicio con resultado observado, sea mejora o limitación persistente. Conservar v7, v8, respuestas y comparación de los mismos cuatro casos. Si T02 sigue incompleto o aparece regresión, registrarlo como pendiente; no afirmar que el sistema está listo para producción ni añadir v9 automáticamente.

La cobertura será parcial (estos cuatro tickets de los diez originales); el resto, casos nuevos independientes, repeticiones adicionales, comparación de modelos, integración ERP y precisión del resumen quedan como siguientes tareas, no como requisito para finalizar este ejercicio educativo hoy.

No enviar etiquetas esperadas de los controles al modelo. Preparar v8 no añade ejecuciones: total permanece 44 respuestas sobre trece tickets distintos.

## Avance observado
Primera [T02-v8](../../experiments/2026-10-15-t02-v8/README.md) recibida: formato/etiquetas conformes y solicita error exacto/pasos ausentes. Objetivo observado en este caso frente a dos listas vacías v7, sin prueba de robustez general. Análisis asistido por IA pendiente de validación humana; fuente textual sin payload completo. 1 de 4 controles de cierre, cobertura 1/10; quedan T04/T06/T10. Total acumulado 45 respuestas sobre trece tickets.

Segundo [control T04-v8](../../experiments/2026-10-15-t04-v8/README.md): formato/etiquetas conformes y cantidades/fecha útiles sin repetir almacén. Conserva comportamiento v7. 2/4 controles de cierre recibidos, cobertura original 2/10; quedan T06/T10. Total 46 respuestas sobre trece tickets. Fuente textual y análisis asistido por IA pendiente de validación personal.
