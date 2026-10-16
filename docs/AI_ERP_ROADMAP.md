# Roadmap técnico de IA y arquitectura aplicada a ERP

Plan técnico de aprendizaje para ERP Ticket Lab. Actualizado el 15 de octubre de 2026.

## Modalidad de avance

Los hitos se realizan de forma flexible, uno por vez. Las semanas de la tabla son bloques de esfuerzo orientativos; no representan un calendario comprometido. Se mantiene un único proyecto activo.

El laboratorio puede servir como caso para estudiar arquitectura de soluciones con Dynamics 365 Finance and Operations e IA aplicada. Primera entrega propuesta: requisitos y diagrama de contexto del flujo de soporte. La integración a Dynamics no está implementada y las prácticas locales utilizan datos sintéticos.

La arquitectura de software se profundizará con C#/.NET, APIs, persistencia, pruebas, despliegue y observabilidad según las necesidades del prototipo. Los cursos complementarios y las extensiones quedan sujetos a su utilidad para cada hito.

Referencias: [rol de solution architect](https://learn.microsoft.com/en-us/dynamics365/guidance/roles/solution-architect) y [ruta Dynamics 365 y Power Platform](https://learn.microsoft.com/en-us/training/paths/become-solution-architect/).

## Punto de partida

La etapa de prompts se cerró con v8 como referencia. El README consultado registra 48 respuestas entre versiones sobre 13 tickets distintos. Los cuatro controles v8 cubren 4/10 casos originales; no demuestran fiabilidad general. La validación humana cualitativa sigue pendiente salvo intervenciones expresas.

La etapa 2 es diseño didáctico, todavía sin implementación del workflow. La documentación ya recoge la respuesta sobre gestionar T02 y solicitar datos en paralelo. El próximo ejercicio pendiente es T06, prioridad y tratamiento de una solicitud planificada.

Este roadmap no reabre la etapa 1 ni modifica el contrato de seis claves de v8.

## Método

Cada sesión combina un concepto en español con su término en inglés, un ejemplo ERP, una práctica pequeña y una comprobación de comprensión. El código o la documentación preparados por el tutor no acreditan comprensión del estudiante.

Mantener un proyecto activo y un curso complementario como máximo. Si una semana solo permite una hora, reducir el ejercicio y mover el calendario. Revisar alcance cada cuatro semanas.

## Bloques futuros de referencia

| Semanas | Foco | Entrega | Criterio de avance |
| --- | --- | --- | --- |
| 1 y 2 | Orquestación funcional, prioridad, estado y revisión humana | Resolver T06; simular T02 y T06; tabla de decisiones separada del JSON | Explicar la diferencia entre clasificar y atender; justificar atención y recopilación de datos en paralelo |
| 3 y 4 | Evaluación, conjunto reservado y variabilidad | Evaluar pendientes del conjunto original sin ajustar v8; preparar diez casos nuevos con rúbrica previa; repetir tres casos sensibles tres veces si hay acceso gratuito | Separar cobertura, formato, etiquetas y revisión semántica; informar conjuntos y versiones por separado |
| 5 y 6 | Python, validación, estados y errores | Workflow local con respuestas guardadas; interfaz mínima solo si el flujo funciona | Probar JSON inválido, datos insuficientes y rechazo humano; identificar el modo de reproducción de respuestas |
| 7 a 9 | Context engineering, grounding y recuperación documental | Extensión sobre cinco procedimientos ERP sintéticos; diez preguntas, incluidas tres sin respuesta documental | Citar fuentes y abstenerse; distinguir búsqueda, práctica manual con contexto y RAG automatizado |
| 10 a 12 | Tool calling, workflow frente a agente y orquestación SAP | Consulta local de documentos sintéticos; gestión de fallos; explorar un módulo SAP si hay acceso sin coste adicional | Explicar quién ejecuta herramientas y qué valida el código; identificar simulaciones y capacidades realmente implementadas |
| 13 a 16 | Demo, reproducibilidad y comunicación | README, resumen en inglés, demo breve, resultados y límites; revisión de un fallo relevante | Ejecutar y explicar la solución, sus pruebas y sus límites sin depender del tutor |

En la semana 8 se ajustará el alcance. Una extensión terminada puede reemplazar dos extensiones incompletas.

## Entregas del portafolio

1. **ERP Ticket Lab:** clasificación, evaluación y workflow simulado de atención.
2. **Asistente de procedimientos:** extensión de recuperación de información con fuentes y casos sin evidencia.
3. **Consulta con herramientas:** extensión de solo lectura sobre datos sintéticos y manejo de errores.

Las extensiones son trabajo propuesto. No existe todavía integración operativa a SAP o Dynamics, ni una medición de ahorro de tiempo.

Cada entrega debe contener problema, alcance, datos sintéticos, ejecución reproducible, resultados originales, criterios de evaluación y limitaciones. Una simulación local no se presentará como una integración ERP real.

## Evaluación

- Conservar v8 como referencia para el siguiente trabajo.
- No usar etiquetas esperadas de los tickets reales dentro del prompt.
- Fijar las etiquetas y la rúbrica del conjunto reservado antes de ejecutarlo.
- No ajustar el prompt sobre ese conjunto y después llamarlo prueba independiente.
- Reportar conjuntos, versiones y repeticiones por separado.
- Mantener las respuestas originales y registrar parámetros efectivos o incertidumbres.
- Separar verificaciones automáticas de revisión funcional humana.
- Medir fidelidad del resumen, referencias sin respaldo y utilidad de preguntas mediante una rúbrica humana explícita.
- No afirmar porcentajes generales, causalidad, ahorro o preparación para producción a partir de estos experimentos pequeños.

La comparación de modelos es una ampliación opcional si hay dos opciones disponibles sin coste adicional; no bloquea la ruta.

## Recursos gratuitos

Condiciones consultadas el 15 de octubre de 2026. Una credencial digital o un certificado de finalización no son equivalentes a una certificación profesional.

- [IBM SkillsBuild](https://skillsbuild.org/digital-credentials): Craft Precise Prompts for AI Models, credencial de cuatro horas en inglés. Primera opción complementaria.
- IBM Artificial Intelligence Fundamentals, con español y duración indicada de más de diez horas, solo si aparecen vacíos de fundamentos. Sustituye otra formación.
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction): curso y certificación de finalización gratuitos. Comenzar por la unidad 1 en la etapa de herramientas; el itinerario completo puede pasar al siguiente ciclo. Los costes de inferencia externa se revisan por separado.
- [SAP Generative AI Hub Learning Journey](https://learning.sap.com/learning-journeys/solving-business-problems-using-sap-s-generative-ai-hub): continuar las prácticas vinculadas al proyecto.
- [SAP Learning Hub student edition](https://learning.sap.com/helpcenter/learninghub-student-edition): beneficios gratuitos para estudiantes elegibles. Verificar acceso, vigencia y saldo real de intentos en la cuenta; no asumir gratuidad ilimitada.

La ruta básica no exige compras ni créditos. Si falta acceso a un modelo, se puede estudiar validación y workflow reproduciendo respuestas ya guardadas. Eso no cuenta como una nueva ejecución de IA. Las prácticas dependientes de servicios quedan condicionadas a su acceso real.

## Comunicación

Proponer como máximo una pieza cada dos semanas basada en evidencia y coordinarla con el calendario de comunicación existente. Temas: problema de soporte, JSON válido frente a contenido útil, fallo observado, prioridad frente a estado, demo reproducible y respuestas con fuentes.

Mantener los criterios de [LINKEDIN_PLAN.md](LINKEDIN_PLAN.md): datos sintéticos, resultados originales, límites y enlace reproducible. Este archivo no programa ni publica mensajes.

## Próxima práctica

Retomar el ejercicio 2 de [STAGE_2_ORCHESTRATION.md](STAGE_2_ORCHESTRATION.md): T06 pide un reporte mensual de ventas por cliente, sin interrupción del negocio. Faltan campos y filtros. El estudiante debe indicar prioridad, tratamiento y primer dato a solicitar.

No marcar comprensión ni actualizar el estado del ejercicio hasta recibir y revisar la respuesta.
