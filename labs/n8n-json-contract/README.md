# ERP Ticket Lab — Flujo 02: integración IA (simulada) y contrato JSON

**Fecha:** 28/10/2026  
**Estado:** entrada JSON sintética, validación JavaScript y recorrido de caso Alta observados. Falta bloqueo explícito de contratos inválidos.

## Archivo reproducible

[flujo-02-v1.json](flujo-02-v1.json) — export real recibido del participante, ocho nodos. Se eliminó `meta.instanceId` de la copia pública; no se observaron credenciales de nodos. No contiene historial de ejecuciones.

## Evidencia mostrada

Capturas compartidas en el chat (no publicadas como archivos en el repositorio):
- `Edit Fields` en modo JSON: seis campos con tipos esperados, ticket sintético T02 / Finanzas / Alta, documento FV-1042 y lista de dos datos faltantes. Un item producido.
- Primera captura del lienzo: `Validar contrato JSON` agregado entre entrada y validador de prioridades, antes de ejecutarlo en esa imagen.
- Segunda captura: `Validar contrato JSON` se ejecuta con 1 item, seguido de `Validar prioridad` true, `If` true y `Edit Fields2`, con un item final.
- No se recibió captura del **JSON OUTPUT del nodo Code**, por lo que aún no se ha verificado visualmente el valor `validacion_contrato.valido` ni mensajes de error.

## Arquitectura actual

`Manual Trigger → Edit Fields (JSON) → Validar contrato JSON (Code) → Validar prioridad (If) → If de Alta → Edit Fields de ruta`.

El nodo Code usa JavaScript, modo `Run Once for Each Item`. Comprueba existencia de seis campos, valores permitidos de categoría y prioridad, tipos de ticket_id/resumen/referencia_documento/datos_faltantes y campos extra. Agrega `validacion_contrato: {valido, errores}` preservando los datos originales.

La implementación refleja controles principales de [schema.json](../../schema.json), **no utiliza todavía un validador formal de JSON Schema**. El objeto extendido con `validacion_contrato` no debe confundirse con el objeto original de seis claves definido por el esquema.

## Riesgo identificado y próximo paso

El flujo actual **no separa los contratos inválidos**. Incluso con `validacion_contrato.valido=false`, el item sigue hacia `Validar prioridad`. Para impedirlo, añadir un nodo If llamado `Contrato válido?` inmediatamente después de `Validar contrato JSON`, con condición Boolean `{{ $json.validacion_contrato.valido }}` `is true`. Su salida true debe conectar a `Validar prioridad`; false a un nuevo nodo `Revisar contrato` que preserve datos y marque `estado_validacion=Rechazada`, `motivo_validacion=Contrato JSON inválido`. No reutilizar `Revisar prioridad` para errores de esquema.

Probar primero T02 válido y luego un caso con `categoria=NoExiste` o un campo extra, confirmando que el rechazo ocurre antes del enrutamiento por prioridad. Una vez comprobado, volver a exportar el Flujo 02 como nueva versión.

## 28/10/2026 — control del contrato y salida de rechazo (capturas)

- El alumno muestra el nodo `Contrato válido?` con expresión `{{ $json.validacion_contrato.valido }}` y operador Boolean `is true`. Su INPUT muestra `validacion_contrato.valido = true` y una colección `errores` sin elementos para T02. Esto confirma visualmente la salida del Code en el caso válido.
- La captura del nodo `Revisar contrato` muestra `Include Other Input Fields` activado, pero el campo aún conserva el marcador `name` / `value`; falta configurar `estado_validacion` y `motivo_validacion`.
- No se ve un lienzo completo de las nuevas conexiones ni una ejecución posterior del nodo If; `No output data` por sí solo no confirma un fallo.
- **Próximo paso:** terminar los campos de rechazo, confirmar rama true a Validar prioridad y false a Revisar contrato, ejecutar caso sintético con `categoria = NoExiste`, y verificar `validacion_contrato.valido = false`, mensaje `Categoría no permitida` y salida de rechazo. No afirmar ejecución hasta recibir evidencia.
