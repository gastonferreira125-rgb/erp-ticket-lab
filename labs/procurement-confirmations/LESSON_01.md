# Lección 1 de Power Platform aplicada a compras

Fecha: 19 de octubre de 2026. Estado: explicación y ejercicio preparados; respuestas y comprensión pendientes.

## Objetivo

Distinguir pantalla, datos y automatización, e identificar discrepancias entre dos documentos. No requiere Python, un entorno Microsoft ni instalación local.

## Conceptos

**Power Platform:** conjunto de herramientas Microsoft para construir aplicaciones, automatizaciones y análisis de negocio.

**Power Apps:** herramienta para construir aplicaciones. En el caso propuesto, una persona de Compras usará una pantalla para ver documentos y registrar su decisión.

**Power Automate:** herramienta para construir flujos. Un flujo tiene un disparador (trigger), acciones (actions) y condiciones (conditions). En este caso podría comenzar cuando se registra una confirmación y luego comparar sus datos.

**Dataverse:** plataforma para almacenar y gestionar datos en tablas, relaciones y permisos. En este caso mantendría documentos y decisiones. No es la pantalla del usuario.

Una pantalla puede pedir que se inicie un proceso y un flujo puede crear registros. La distinción didáctica es la responsabilidad principal de cada componente, no que las herramientas sean incapaces de colaborar.

## Caso sintético

Referencia: OC-1001, proveedor PROV-DEMO-01, línea 1, artículo ART-310. Misma moneda USD, misma unidad UN y mismo criterio de precio unitario sin impuestos.

| Campo | Orden de compra OC-1001 | Confirmación CONF-001 |
| --- | --- | --- |
| Cantidad | 100 | 80 |
| Precio unitario USD | 12.00 | 13.00 |
| Fecha de entrega | 2026-11-05 | 2026-11-12 |

Los datos completos están en [lesson-01.csv](data/lesson-01.csv). Son datos preparados, no información real de un proveedor ni salida de un modelo.

## Actividad 1 de teoría

¿Qué componente usarías para la pantalla de revisión de Compras y cuál para ejecutar la comparación cuando llega una confirmación? Explicá brevemente por qué.

## Actividad 2 de práctica

Compará los dos registros y anotá qué cambió en cantidad, precio y fecha. Para cada campo, expresá también la magnitud de la diferencia. Podés usar calculadora; no hace falta código.

## Actividad 3 de decisión

¿La confirmación recibida debería sobrescribir automáticamente la orden de compra? Explicá qué registrarías y qué dejarías pendiente de una persona.

## Cómo responder

Enviar en el chat:

1. Pantalla y automatización: ...
2. Diferencias: ...
3. Decisión y motivo: ...

El tutor revisará la respuesta y registrará los aciertos y las correcciones. Una respuesta parcial se continúa desde ese punto; no se marca toda la lección aprobada automáticamente.

## Evidencia de aprendizaje

Se completará después de recibir las respuestas. Todavía no existe ejecución en Power Platform, n8n, SAP o Dynamics.

## Próxima sesión

Tras revisar el ejercicio, verificar el acceso real a Power Apps y el entorno disponible. Después crear una tabla o una pantalla pequeña en ese entorno. La secuencia exacta se adapta a la pantalla observada; no se presupone que ya exista una cuenta o licencia.

## Fuente de estudio

[Introducción al valor de negocio de Power Platform](https://learn.microsoft.com/en-us/training/paths/describe-business-value-microsoft-power-platform/).
