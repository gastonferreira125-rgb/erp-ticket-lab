# T06 — v6 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T06
<ticket>
Quiero crear un reporte mensual de ventas por cliente. No hay interrupción del negocio.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T06",
  "categoria": "Reportes",
  "prioridad": "Baja",
  "resumen": "Solicitud de creación de un reporte mensual de ventas por cliente.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Detallar los campos y filtros necesarios para el reporte mensual de ventas por cliente."
  ]
}
```

## Evaluación
evaluate.py confirma T06 presente, formato y etiquetas conformes: Reportes, Baja y null. Sin IDs duplicados/desconocidos ni referencias ausentes literalmente. Otros nueve casos no ejecutados en este archivo.

Fuente: JSON pegado, sin captura. Resumen fiel como solicitud pendiente, sin afirmar creación realizada. datos_faltantes pide campos y filtros, información ausente, concreta y útil para definir requisitos del reporte.

## Comparación y límites
v5 también pedía requisitos útiles y añadía ordenamiento/formato. Esta salida v6 conserva información pertinente, pero no permite afirmar mejora global frente a v5 ni que todo el alcance necesario esté definido.
T02 y T04 quedaron con listas vacías bajo el procedimiento v6; T06 no. Registrar resultados distintos por caso, sin concluir que la regla se cumple o falla siempre.

v6: cuatro ejecuciones sobre tres tickets originales (T02 dos veces, T04 y T06), todas conformes en etiquetas. Cobertura única 3/10. T06 pide información útil; objetivo humano no cumplido en T02/T04. No convertir la muestra parcial en una exactitud general.

[Prompt v6](../../prompts/v6-missing-data-rule/system.txt). Texto Sistema aportado por usuario coincide con archivo previsto; sin payload/captura que confirme configuración de esta ejecución. Parámetros solicitados: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690, streaming activado.

Siguiente: T10 con v6 sin cambios para controlar que la regla específica de instrucciones mantenga precedencia y solicite descripción de incidente. Después revisar resultados antes de otro ajuste.
