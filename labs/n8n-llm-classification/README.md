# Lab 03 — Clasificación real de tickets ERP con LLM

**Fecha inicial:** 2026-11-03  
**Estado:** primera inferencia confirmada por capturas; contrato de salida todavía no integrado al validador ni verificado end-to-end.

## Objetivo de aprendizaje

Combinar un modelo de lenguaje con reglas determinísticas de validación para clasificar tickets ficticios en formato compatible con [schema.json](../../schema.json), manteniendo separado el análisis del modelo y la lógica de negocio del ERP.

## Evidencia recibida y verificada

- El workflow duplicado se llama `ERP Ticket Lab - Flujo 03 - Clasificación IA real`.
- Se observó una rama de prueba separada desde Manual Trigger hacia `Basic LLM Chain`, vinculado por el puerto `Model` al subnodo `Groq Chat Model`.
- La ejecución observada figura exitosa en ambos nodos y el Basic LLM Chain devuelve **1 item**.
- El OUTPUT de Basic LLM Chain contiene una propiedad `text` con el **JSON serializado como cadena de texto** (todavía no objeto con seis campos directamente accesibles).
- El resultado mostrado para ticket ficticio T03 propone categoría Finanzas y prioridad Alta, con resumen del incidente de contabilización en cierre mensual. El modelo devolvió `referencia_documento=null` pese a que la descripción contiene `FV-1042`: **error semántico detectado**.
- La rama de ruteo anterior aparece ejecutada por separado para un ticket inválido; no existe todavía una integración de la salida del modelo al nodo `Validar contrato JSON`.

## Arquitectura actual observada

```text
Manual Trigger ──► Edit Fields ──► Validar contrato JSON ──► ... (circuito v2)
             └──► Basic LLM Chain [Groq Chat Model] ──► (aún sin conectar)
```

## Próximo paso único

Agregar un nodo `Code` después de `Basic LLM Chain`, configurado en `Run Once for Each Item` (JavaScript), para transformar la cadena devuelta en `$input.item.json.text` a objeto JSON mediante `JSON.parse`, manteniendo la rama separada por ahora. Verificar OUTPUT con captura antes de conectar con validación.

## Aprendizajes por confirmar

- **JSON serialization vs JSON parsing**: un texto que contiene llaves no equivale automáticamente a un objeto manipulable.
- **Validación estructural**: tipos, campos y valores permitidos según schema.json.
- **Validación semántica**: contrastar valores extraídos contra información realmente mencionada por el usuario.
- **Seguridad**: usar datos sintéticos, nunca publicar claves ni datos personales de tickets de clientes.

## Límites y siguientes hitos

No se recibió aún export del Flujo 03 ni evidencia de ejecución completa con un modelo y el validador conectados. Después del parsing, ajustar el prompt sobre extracción de `referencia_documento` y repetir pruebas con múltiples incidentes sintéticos; añadir control de parseo fallido y supervisión humana antes de presentar el laboratorio como solución empresarial.


## Actualización 03/11/2026 — Recorrido completo exitoso de IA a reglas ERP


- **Evidencia del lienzo:** `Manual Trigger → Basic LLM Chain [Groq Chat Model] → Parsear respuesta IA → Validar contrato JSON → Contrato válido? (true) → Validar prioridad (true) → If (true) → Edit Fields2` (1 item). `Edit Fields` anterior está aislado.
- **Evidencia OUTPUT del validador:** ticket ficticio T03, `Finanzas`, `Alta`, referencia `FV-1042`, datos_faltantes con dos elementos, `validacion_contrato.valido=true` y `errores=[]`.
- **Confirmado:** parsing, esquema contractual y enrutamiento positivo tras una inferencia real de Groq. **No confirmado por OUTPUT:** valor exacto de `siguiente_accion` de Edit Fields2 en esta ejecución (solo nodo final verde y 1 item en el lienzo).
- **Pendiente:** export Flujo 03; control de errores de formato (JSON.parse arroja excepción si el texto es inválido); pruebas de fallos, reconciliación semántica contra texto original, entradas dinámicas y datos ERP reales.
- **Siguiente paso recomendado:** crear punto de restauración mediante export de n8n y registrar versión sin secretos; luego prueba dirigida de JSON inválido con manejo seguro de errores y rechazo explícito.


## 03/11/2026 — Primer punto de restauración publicado

[Descargar/consultar Flujo 03 v1 — Groq](flujo-03-v1-groq-clasificacion.json).

- 13 nodos y 11 conexiones verificados contra el export compartido. Modelo `openai/gpt-oss-20b`.
- Cadena activa: Manual Trigger → Basic LLM Chain (Groq) → Parsear respuesta IA → Validar contrato JSON → Contrato válido? → Validar prioridad → If → siguiente acción. Las ramas de rechazo siguen conectadas. El antiguo Edit Fields de ejemplo permanece aislado.
- Export público sanitizado: sin `credentials`, sin ID de instancia n8n, sin ID ni versión internos del workflow; la copia deberá reconectar Groq tras importar. No se detectaron claves API en el archivo original.
- Prueba previa observada: LLM → validador → ruta Alta hasta Edit Fields2. Resultado de validador para T03 correcto en captura; el export es configuración, no historial de ejecución.
- Límite actual: prompt fijo, `JSON.parse` sin excepción capturada, clasificación susceptible a omisión semántica, sin datos reales ni conexión SAP. Próximo trabajo: `try/catch`, revisión de respuestas no parseables, pruebas negativas y versionado v2.



## Prueba negativa de parseo — 03/11/2026

- Captura de n8n: el OUTPUT del nodo Parsear respuesta IA devolvió tipo_error=SyntaxError, error_parseo=true y motivo_error=La IA devolvió JSON inválido.
- Se confirmó el uso de catch para convertir una excepción de JSON.parse en una respuesta de datos controlada. La ejecución fue únicamente del nodo; no prueba todavía el circuito de rechazo completo.
- Próximo paso: restaurar la entrada normal del LLM, ejecutar un caso positivo, agregar un IF de error_parseo antes de Validar contrato JSON y diseñar la rama de revisión de IA.
