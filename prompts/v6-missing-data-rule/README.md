# v6-missing-data-rule — listas vacías en T02/T04; controles en curso

Deriva de v5-reference-rule. added-rule.txt se añade al final de system.txt. La única regla nueva es calidad de datos_faltantes: datos ausentes útiles para investigar/definir el próximo paso, solicitudes concretas y sin repetir información ya aportada.

Conserva categorías, prioridad, extracción, resumen, seis claves/tipos y precedencia de la condición específica para mensajes de instrucciones. No añade ejemplos Asistente ni etiquetas esperadas al prompt.

Motivo: v5 alcanzó 10/10 en etiquetas originales, pero varias listas perdieron utilidad (T02/T03 vacías, T04 almacén ya informado, T08 procedimiento vago/fechas omitidas).

[Primera salida T02](../../experiments/2026-10-14-t02-v6/README.md): etiquetas y formato conformes (1/1 entre ejecutados, cobertura 1/10), pero datos_faltantes sigue vacío. Objetivo del ajuste no cumplido en esa respuesta. Resumen conserva cierre detenido. No atribuir causalidad ni concluir que la regla se aplicó en SAP: el usuario aportó después Sistema completo y coincide con el archivo previsto; no hay payload retrospectivo ni parámetros numéricos confirmados.

[Repetición T02](../../experiments/2026-10-14-t02-v6-r2/README.md): segunda salida con mismas etiquetas y lista vacía, resumen distinto. Dos ejecuciones del mismo caso; cobertura única 1/10. Ambas fallan el objetivo humano, sin demostrar fallo universal o determinismo.

[T04-v6](../../experiments/2026-10-14-t04-v6/README.md) también conserva etiquetas y lista vacía, pese a faltar cantidades/fecha útiles. Conserva contexto en resumen y no vuelve a pedir almacén; no inferir causalidad del ajuste. Estado global v6: tres ejecuciones sobre dos tickets, cobertura única 2/10, objetivo humano no cumplido en esas salidas.

Siguiente: T06 con mismo Sistema/configuración solicitada para solicitud planificada; luego T10. No añadir reglas todavía. Revisar datos ausentes, útiles y concretos sin imponer lista textual fija. Casos usados para ajustes no prueban generalización independiente.

La precisión del impacto en resúmenes sigue reservada para otro ajuste. [Ronda completa v5](../../experiments/2026-10-14-v5-round/README.md).
