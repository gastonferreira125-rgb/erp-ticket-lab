# T02 — primera respuesta con v7 — 15 de octubre de 2026

## Entrada y configuración indicada

Se indicó [v7-few-shot](../../prompts/v7-few-shot/README.md): System v6 idéntico, dos pares de demostraciones EX01/EX02 y un último Usuario con T02. [Seis mensajes previstos](../../prompts/v7-few-shot/messages-t02.json).

Texto T02:
> La factura FV-1042 no se contabiliza. Todo el equipo de Finanzas está bloqueado y el cierre está detenido.

Modelo visible en captura previa: Gemini 2.5 Flash Lite (001). Parámetros solicitados sin cambios: temperatura 1, máximo de salida 43690, streaming activado. Los valores numéricos actuales no se verificaron. La captura previa mostraba tres bloques y panel vacío; se explicó cómo completar los seis. El resultado posterior fue pegado como texto. No se recibió captura final de seis bloques ni payload completo; se registra como prueba v7 indicada, con esa limitación de trazabilidad.

Los intentos sin salida verificable no se incorporan a las métricas de respuestas. No se publica la captura.

## Respuesta original

[Texto exacto pegado](raw-response.txt), [respuesta en lista JSON](responses.json). Se conserva sin corregir.

## Evaluación automática

Se ejecutó evaluate.py obtenido del repositorio sobre tickets.json y esta respuesta. [Resultado completo](evaluation.json):
- T02 presente; seis claves/tipos conformes.
- Finanzas, Alta y FV-1042 coinciden con referencia.
- Sin referencia inventada literalmente, ids desconocidos o duplicados.
- Una respuesta conforme entre una ejecutada; cobertura única 1/10. Los otros nueve casos no están ejecutados con v7, no son nueve fallos del modelo.

## Revisión humana y comparación

| Aspecto | T02 v6, repetición 2 | T02 v7 |
| --- | --- | --- |
| Etiquetas | Conformes | Conformes |
| datos_faltantes | [] | [] |
| Impacto en resumen | Cierre financiero detenido; omite equipo | Bloqueo del equipo de Finanzas y cierre |

El resumen v7 conserva el fallo y el bloqueo sin inventar causa o solución. No reproduce explícitamente “todo” el equipo. La lista vacía sigue siendo insuficiente: error exacto y pasos realizados serían datos ausentes útiles para investigar. No se afirma una causa técnica.

No se observa mejora en datos_faltantes frente a las dos respuestas T02-v6, también vacías. Una ejecución, un caso usado para ajuste y configuración parcialmente verificada no permiten concluir que few-shot sea ineficaz en general ni atribuir causalidad a las diferencias del resumen.

## Aprendizaje: por qué los ejemplos no generan resultados separados

El usuario preguntó por qué EX01/EX02 no dieron resultados. Sus respuestas Asistente están escritas como contexto de entrada. En la prueba configurada, la salida nueva es la continuación correspondiente al último Usuario T02. Seis mensajes de entrada no equivalen a seis clasificaciones nuevas. Las dos demostraciones siguen sin contarse como ejecuciones del modelo.

Total acumulado de respuestas registradas entre versiones: 39 ejecuciones sobre doce tickets distintos.

## Próximo control

Mantener Sistema y los cuatro mensajes de ejemplo. Sustituir únicamente el último Usuario por T04 original:

```text
ENTRADA:
ticket_id: T04
<ticket>
Necesitamos revisar el stock del artículo ART-310 en el almacén central; difiere del conteo físico.
</ticket>
```

Revisar especialmente si pide cantidades del sistema/conteo y fecha útil sin volver a pedir almacén ya informado. Después T06/T10 y repeticiones/casos nuevos, sin modificar v7 entre controles.
