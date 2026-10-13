# Registro de aprendizaje

## 12 de octubre de 2026
Objetivo: acceder al sistema de práctica AIG02 y entender SAP AI Launchpad, Generative AI Hub, modelo y prompt.

Concepto trabajado: clasificar un ticket no determina su causa. Un mensaje incompleto sobre un pago a proveedor permite reconocer el proceso, pero no diagnosticar el error.

Acceso al entorno: pendiente de confirmar. Ejecuciones en modelos: pendientes.

Método de cada sesión: teoría en español con términos en inglés, ejemplo ERP, acción práctica y comprobación de comprensión antes de continuar.

## 13 de octubre de 2026
- Objetivo: retomar el laboratorio y ejecutar T01.
- Acceso a SAP AI Launchpad: confirmado por captura del editor.
- Modelo confirmado por captura posterior: Gemini 2.5 Flash Lite (001). Configuración actual capturada después de T01: temperatura 1; tokens de salida máximos 43690; streaming activado.
- Conceptos explicados: prompt, JSON y clasificación frente a diagnóstico.
- Acción realizada: primera ejecución manual de T01 en el bloque Usuario.
- Evidencia: respuesta original y captura del panel de respuesta aportadas por Gastón.
- Validación: 1 de 10 casos ejecutados; T01 cumple las comprobaciones del evaluador y coincide con las etiquetas de referencia.
- Revisión humana: resumen fiel, sin diagnóstico inventado; datos faltantes útiles, aunque “detalles del pago” es amplio.
- Comprobación de aprendizaje: Gastón identificó correctamente la condición de prioridad Alta del laboratorio (proceso detenido para todo un equipo).
- Próximo paso: ejecutar T02 con la misma configuración, cambiando únicamente id y texto.
- [Registro del experimento](../experiments/2026-10-13-t01/README.md).

## 13 de octubre de 2026 — T02
- Segunda ejecución manual observada mediante captura.
- Campos legibles: Finanzas, Alta, FV-1042 y datos_faltantes vacío.
- Aprendizaje: una salida puede cumplir tipos y etiquetas y aun así ser insuficiente para investigar un incidente.
- Observación: faltan error exacto, pasos de reproducción y verificaciones realizadas.
- Evidencia: captura del resultado; el resumen está cortado en el borde derecho.
- Salida original completa y evaluación automática: pendientes; responses.json conserva únicamente T01.
- Próximo paso: copiar el JSON completo desde SAP.
- [Registro preliminar de T02](../experiments/2026-10-13-t02/README.md).

## Plantilla para próximas sesiones
- Fecha y objetivo:
- Concepto aprendido:
- Acción realizada y entorno:
- Evidencia obtenida:
- Error o duda:
- Qué puede explicar Gastón con sus palabras:
- Próximo paso:
