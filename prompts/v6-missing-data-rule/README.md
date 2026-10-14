# v6-missing-data-rule — T02 repetido; objetivo de datos faltantes aún no cumplido

Deriva de v5-reference-rule. added-rule.txt se añade al final de system.txt. La única regla nueva es calidad de datos_faltantes: datos ausentes útiles para investigar/definir el próximo paso, solicitudes concretas y sin repetir información ya aportada.

Conserva categorías, prioridad, extracción, resumen, seis claves/tipos y precedencia de la condición específica para mensajes de instrucciones. No añade ejemplos Asistente ni etiquetas esperadas al prompt.

Motivo: v5 alcanzó 10/10 en etiquetas originales, pero varias listas perdieron utilidad (T02/T03 vacías, T04 almacén ya informado, T08 procedimiento vago/fechas omitidas).

[Primera salida T02](../../experiments/2026-10-14-t02-v6/README.md): etiquetas y formato conformes (1/1 entre ejecutados, cobertura 1/10), pero datos_faltantes sigue vacío. Objetivo del ajuste no cumplido en esa respuesta. Resumen conserva cierre detenido. No atribuir causalidad ni concluir que la regla se aplicó en SAP: el usuario aportó después Sistema completo y coincide con el archivo previsto; no hay payload retrospectivo ni parámetros numéricos confirmados.

[Repetición T02](../../experiments/2026-10-14-t02-v6-r2/README.md): segunda salida con mismas etiquetas y lista vacía, resumen distinto. Dos ejecuciones del mismo caso; cobertura única 1/10. Ambas fallan el objetivo humano, sin demostrar fallo universal o determinismo.

Siguiente: T04 con mismo Sistema/configuración solicitada, sin añadir reglas; luego T06/T10 según lo observado. Revisar datos ausentes, útiles y concretos sin imponer lista textual fija. Añadir casos nuevos después; los usados para ajustar no prueban generalización independiente.

La precisión del impacto en resúmenes sigue reservada para otro ajuste. [Ronda completa v5](../../experiments/2026-10-14-v5-round/README.md).
