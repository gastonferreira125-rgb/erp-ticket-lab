# T07 con v3: fallo de categoría

Fecha: 14 de octubre de 2026. Salida copiada por Gastón y contrastada con la captura del chat, sin correcciones.
Se indicó mantener Sistema v3. Configuración solicitada: Gemini 2.5 Flash Lite (001), temperatura 1, salida máxima 43690 y streaming activado; valores actuales y guardado en SAP no confirmados por esta captura.

## Entrada
La integración de pedidos con la tienda está caída. Ningún pedido entra y todo el equipo de ventas está detenido.

## Respuesta original
```json
{
  "ticket_id": "T07",
  "categoria": "Ventas",
  "prioridad": "Alta",
  "resumen": "La integración de pedidos con la tienda está caída e impide la entrada de pedidos.",
  "referencia_documento": null,
  "datos_faltantes": [
    "Detalles de la tienda o plataforma de e-commerce",
    "Mensajes de error específicos de la integración",
    "Fecha y hora aproximada del inicio de la caída"
  ]
}
```

## Evaluación
```json
{
  "ticket_id": "T07",
  "present": true,
  "schema_valid": true,
  "labels_match": false,
  "invented_reference": false
}
```

La categoría esperada en el laboratorio es Integraciones; la salida Ventas no coincide. Alta es correcta por el bloqueo del equipo. El resumen es fiel sin inventar causa, la referencia null es correcta y los datos faltantes son pertinentes.

Área afectada (Ventas) y tipo de problema (Integraciones) son dimensiones distintas. No se afirma conocer el razonamiento interno del modelo ni la causa técnica de la caída.

## Continuación
Mantener v3 sin cambios al completar T03, T04, T08 y T09, antes de ajustar el criterio de Integraciones. Después repetir T01/T02/T10 para cobertura y regresión de v3.
Son diez ejecuciones sobre seis tickets distintos; v3 tiene dos coincidencias de etiquetas entre tres casos.
La actualización general de README y registro de aprendizaje quedó pendiente por tiempos de espera en la revisión automática. Este archivo conserva el resultado y la continuación.
