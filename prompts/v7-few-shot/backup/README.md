# Respaldo XML de v7

[ERP_Tickets_v7_FewShot.xml](ERP_Tickets_v7_FewShot.xml) es un formato propio del laboratorio para conservar y reconstruir la plantilla. No es un export nativo de SAP y no se verificó importación directa en Launchpad.

Contiene:
- Seis mensajes completos con orden y roles.
- Modelo indicado y parámetros conocidos: temperatura 1 y streaming activado.
- Máximo de tokens solicitado 43690, separado del valor seleccionado, que sigue sin verificarse. 65536 es el extremo del control, no una selección confirmada.
- Instrucciones de restauración manual y último Usuario T02.

Origen: [mensajes versionados](../messages-t02.json); no es un volcado del payload efectivo de SAP. Las capturas confirman estructura/roles, no todos los textos íntegros.

## Recuperación
1. Abrir el XML en un editor de texto.
2. Crear seis bloques en SAP AI Launchpad.
3. Para cada message, seleccionar el rol ui_role y copiar únicamente el texto de content, sin etiquetas XML ni delimitadores CDATA.
4. Mantener los primeros cinco bloques; el último Usuario contiene T02.
5. Revisar modelo/parámetros y ejecutar cuando esté completo.

Validación realizada: XML bien formado; seis posiciones/roles correctos; contenido recuperado del XML idéntico a los seis mensajes de messages-t02.json. No hubo nueva ejecución del modelo.

El usuario informó que el guardado nativo no conserva la plantilla. No se determinó la causa. Este respaldo permite conservar los textos aunque falle ese guardado.
