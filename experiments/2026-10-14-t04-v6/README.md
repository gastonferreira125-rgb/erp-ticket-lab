# T04 — v6 — 14 de octubre de 2026

## Entrada indicada
```text
ENTRADA:
ticket_id: T04
<ticket>
Necesitamos revisar el stock del artículo ART-310 en el almacén central; difiere del conteo físico.
</ticket>
```

## Respuesta original
```json
{
  "ticket_id": "T04",
  "categoria": "Inventario",
  "prioridad": "Media",
  "resumen": "Se solicita revisar el stock del artículo ART-310 en el almacén central por discrepancia con el conteo físico.",
  "referencia_documento": "ART-310",
  "datos_faltantes": []
}
```

## Evaluación
evaluate.py confirma T04 presente, formato y etiquetas conformes: Inventario, Media y ART-310. Sin IDs duplicados/desconocidos ni referencias ausentes literalmente. Otros nueve tickets no se ejecutaron en este archivo.

Fuente: JSON pegado, sin captura. Resumen fiel, conserva artículo y almacén central, no inventa causa técnica ni solución.

Objetivo humano de datos_faltantes no cumplido: lista vacía pese a faltar cantidades de stock registrado y conteo físico para dimensionar la discrepancia. Fecha del conteo también es información útil. La entrada permite clasificar, pero no define esos datos para investigar.

## Comparación y límites
v5 pedía almacén ya indicado, fecha de conteo y última transacción, sin cantidades. v6 deja de pedir el dato redundante, pero vacía toda la lista. Eso no resuelve la calidad del campo.
El resumen v6 conserva más contexto que v5, aunque la nueva regla solo estaba dirigida a datos_faltantes; no atribuir causalmente ese cambio al ajuste a partir de una respuesta.

v6 lleva tres ejecuciones sobre dos tickets originales (T02 dos veces, T04 una): todas conformes en etiquetas, todas con lista vacía y objetivo humano no cumplido en estas observaciones. Cobertura única 2/10, no 3/10. No implica incumplimiento universal ni determinismo.

[Prompt v6](../../prompts/v6-missing-data-rule/system.txt). Usuario aportó Sistema completo previamente y coincide con el archivo previsto; sin payload/captura que confirme valores de esta ejecución. Configuración solicitada sin cambios: Gemini 2.5 Flash Lite (001), temperatura 1, máximo de salida 43690 y streaming activado.

Próximo: T06 con v6 sin cambios para observar una solicitud planificada que necesita requisitos, luego T10 para controlar el tratamiento de instrucciones. Guardar las salidas originales antes de decidir otro ajuste.
