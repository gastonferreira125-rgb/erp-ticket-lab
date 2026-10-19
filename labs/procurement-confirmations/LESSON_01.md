# Fundamentos de Power Platform para control de confirmaciones

## Objetivo funcional

Detectar diferencias entre una orden de compra y la confirmación del proveedor, presentar las excepciones a Compras y conservar una decisión trazable.

## Documentos del proceso

- **Cotización (quotation):** oferta de condiciones de un proveedor utilizada para evaluar una compra.
- **Orden de compra (purchase order):** documento con los artículos, cantidades, precios y fechas solicitados.
- **Confirmación de proveedor (order acknowledgment):** comunicación con las condiciones que el proveedor confirma para esa orden.

Una confirmación puede diferir de lo solicitado. El sistema conserva ambos documentos y presenta las discrepancias para revisión.

## Responsabilidades de Power Platform

| Componente | Responsabilidad en el diseño |
| --- | --- |
| Power Apps | Interfaz para consultar documentos y registrar la decisión de Compras |
| Power Automate | Flujo con disparador, acciones y condiciones para comparar y registrar resultados |
| Dataverse | Gestión de tablas, relaciones, permisos y registros |
| Power BI | Indicadores posteriores sobre resultados y tiempos observados |

Power Platform es la familia de herramientas. Una aplicación, un flujo y una plataforma de datos resuelven responsabilidades distintas dentro de la misma solución.

Un disparador (trigger) inicia un flujo. Una acción (action) realiza una operación. Una condición (condition) selecciona el tratamiento según un criterio explícito.

## Ejemplo sintético de referencia

OC-1001, proveedor PROV-DEMO-01, línea 1, artículo ART-310. Ambos documentos usan USD, unidad UN y precio unitario sin impuestos.

| Campo | Orden | Confirmación | Diferencia confirmación menos orden |
| --- | --- | --- | --- |
| Cantidad | 100 UN | 80 UN | -20 UN |
| Precio unitario | USD 12.00 | USD 13.00 | +USD 1.00 por unidad |
| Entrega | 2026-11-05 | 2026-11-12 | +7 días naturales |

La diferencia de cantidad muestra 20 unidades menos confirmadas; no demuestra cancelación del saldo. La diferencia de fecha indica una entrega posterior a la solicitada.

Fuente de los valores: [datos sintéticos CSV](data/lesson-01.csv). La tabla es una referencia calculada de diseño, no una salida de una aplicación ya ejecutada.

## Cálculos y condiciones

- Diferencia de cantidad = cantidad confirmada menos cantidad solicitada.
- Diferencia de precio = precio unitario confirmado menos precio unitario solicitado.
- Diferencia de fecha = fecha confirmada menos fecha solicitada, expresada en días naturales.
- Comparar cantidades solo con unidades compatibles.
- Comparar precios solo con moneda y base de precio compatibles.
- Identificar orden, proveedor, línea y artículo antes de comparar.
- Usar representación decimal adecuada para importes en la implementación.
- Si faltan datos o no son comparables, registrar la incidencia para revisión.

## Tratamiento propuesto

En el primer prototipo, cualquier diferencia se envía a revisión de Compras. Se conserva el documento recibido, la orden original y el detalle de diferencias.

Compras puede aceptar, rechazar o solicitar aclaración de las nuevas condiciones. La decisión, la persona responsable y su fecha se registrarán de forma separada del resultado de comparación.

No se sobrescribe automáticamente la orden original. La aceptación de un cambio y la actualización del ERP requieren un proceso explícito y evidencia de ejecución.

## Criterios de aceptación

1. El sistema debe relacionar la confirmación con la orden y línea correctas.
2. El caso de referencia debe producir las tres diferencias indicadas.
3. Los documentos originales deben permanecer disponibles.
4. Toda diferencia debe quedar en una cola de revisión.
5. Un problema de datos debe identificarse sin inventar valores.
6. La decisión comercial debe poder distinguirse del resultado automático.

## Estado técnico

Fundamentos y datos de referencia preparados. La implementación y sus pruebas en Power Platform están pendientes. No hay integración operativa a SAP, Dynamics o n8n.

## Referencias

- [Introducción al valor de negocio de Power Platform](https://learn.microsoft.com/en-us/training/paths/describe-business-value-microsoft-power-platform/).
- [Arquitectura de cotejo de confirmaciones con SAP](https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/order-acknowledgment-validation).
