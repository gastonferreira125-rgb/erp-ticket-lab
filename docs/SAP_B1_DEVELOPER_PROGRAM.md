# Formación SAP Business One Developer, Integrations & AI
Fecha de preparación: 2026-10-27. Documento de trabajo; no acredita competencias todavía.
Fuente principal: SAP Business One Road Map, October 2026, PDF aportado por el alumno.

## Punto de reanudación
Módulo 1, Lección 1: arquitectura y selección de la vía de integración.
Estado: en estudio; ejercicio y herramientas del equipo pendientes de evidencia.
Siguiente intervención: el alumno identifica dónde consultar una orden de compra y aporta versiones de sus herramientas. No avanzar al laboratorio de API antes de comprobar comprensión.
Los módulos 2–8 están no iniciados en este programa. La experiencia previa no equivale a una validación nueva.

## Revisión del proyecto existente
Se revisaron el árbol main, README.md, evaluate.py y documentos STAGE_1_CLOSURE.md y STAGE_2_PRACTICE_02.md el 27/10/2026.
- Existen prompts v0–v8, contratos JSON, tickets sintéticos, respuestas originales, capturas y evaluaciones.
- Según los registros existentes: 48 respuestas de 13 tickets entre versiones; v8 tiene controles de cuatro de los diez casos originales. No se generalizan esas métricas al sistema completo.
- evaluate.py es código ejecutable con biblioteca estándar Python: valida campos/tipos, compara etiquetas y señala referencias no presentes literalmente. No llama a modelos ni valida por sí mismo la utilidad semántica.
- La orquestación está diseñada: recopilar datos y atender impacto pueden ocurrir en paralelo; información suficiente no equivale a resolución.
- No se identificó en el árbol inspeccionado una conexión operativa a B1, servidor MCP ni servicio de orquestación implementado. No se ejecutó el evaluador en esta preparación.
- El caso procurement-confirmations es un laboratorio separado; no se cambia.
- Se conserva v8 congelada. No se modifican archivos existentes ni métricas históricas.

## Roadmap: disponibilidad y planificación
Estas etiquetas describen cómo SAP presenta las capacidades en el PDF, no la disponibilidad en una instalación concreta. Antes de una práctica real registrar versión/FP/PL, motor, localización, componentes, autorizaciones y licencias.
La diapositiva 3 distingue innovaciones recientes, visión, dirección y planes. La 2 advierte que los planes pueden cambiar.

| Capacidad | Lectura del PDF | Referencia |
|---|---|---|
| Web Client: procesos y analítica, UDQ, Linked Views y General Overview | Presentadas como existentes; cobertura depende de versión | 15–16, 29 |
| Web Client UI API, VS Code, TypeScript, eventos, packaging y Extension Manager | Marco existente; no toda vista/control es extensible | 17 |
| AI UDQ: generar borrador SQL revisable y reutilizar dataset | Innovación reciente; requiere integración/configuración de IA | 18–19, 29 |
| Ask AI: preguntas sobre valores seleccionados y respuestas de texto | Innovación reciente; no implica agente autónomo sobre todo el ERP | 18–19, 29 |
| SAP AI Core y extensiones de partners | Habilitación existente; acceso/licencias externos por verificar | 19–20 |
| MCP para Service Layer | Código de ejemplo, no servicio productivo universal listo para usar | 19, 29 |
| Identity Authentication, IdP, 2FA y mejoras IAM | Capacidades existentes; confirmar configuración y versión | 21 |
| OpenTelemetry en Web Client y Service Layer | Innovación reciente; no clasificar todo el monitoreo como futuro | 22, 29 |
| Cloud Control Center multitenant | Existente; mejoras hasta CLD 1.1 PL23 en el PDF | 23 |
| Nuevas APIs, controles/vistas UI API, webhooks y ejemplos MCP | Ampliaciones planificadas | 31, 34, 36 |
| Ask AI ampliado y AI UDQ con generación de dashboards | Ampliaciones planificadas | 31, 34 |
| Joule con extensiones de partners B1 | Posibilidades mejoradas planificadas; no afirmar Joule nativo universal en B1 | 34 |
| Automatización creación factura proveedor mediante extracción documental en Web Client | Planificada | 29, 33 |
| SP 2611, FP 2702, SP 2705, FP 2708 | Entregas previstas en este documento; confirmar release efectivo antes de usarlas | 27, 30–31 |
| Versión 11, SLD unificado y evolución cloud | Preview inicial prevista para 2027; no disponibilidad general prometida | 27–28 |
| Contenedores en versión 11 | Exploración tecnológica; no arquitectura confirmada para instalar hoy | 28 |
| Escritorio, HANA y SQL Server en versión 11 | Continuidad prevista; el PDF no anuncia eliminación del cliente de escritorio | 28 |
| Forgot My Password, políticas y gestión central ampliada | Mejoras planificadas; no usarlas como instrucciones actuales | 37 |

## Entornos: revisión pública, sin aprovisionamiento
No se activaron cuentas, trials ni recursos de pago. Verificación pública el 27/10/2026; acceso personal y elegibilidad todavía no comprobados.

| Opción | Qué podemos usar | Límite y siguiente comprobación |
|---|---|---|
| SAP Learning: Service Layer | Curso público oficial con arquitectura, HTTP/OData, operaciones y mantenimiento | Leer curso no otorga un servidor B1 ni licencias; práctica requiere entorno |
| SAP Learning: Web Client UI API | Curso público oficial de creación, empaquetado y despliegue | Requiere herramientas y Web Client compatible para validar una extensión real |
| SAP BTP trial | SAP anuncia trial gratuito de 90 días, cuenta SAP y verificación telefónica | Servicios seleccionados, no B1 completo; el free tier comercial es otro modelo |
| SAP AI Core basic trial | SAP anuncia 30 días, AI Launchpad y experiencias guiadas de IA/RAG | No asumir credenciales API externas ni todas las integraciones; verificar condiciones al acceder |
| SAP Business One real | No se confirmó un sandbox oficial público gratuito autogestionado de B1 completo con acceso Service Layer | Explorar acceso educativo/partner autorizado más adelante; no usar entornos de antiguas empresas |
| Equipo local | VS/VS Code, Python, Git y .NET según inventario aportado por el alumno | Herramientas indicadas previamente; instalación y versiones actuales pendientes |
| Simulación local | Datos ficticios y API educativa sin conexión a ERP ni inferencia de pago | No emula íntegramente autorizaciones, transacciones, OData o licencias SAP |

No confundir BTP con una licencia B1. Una demo móvil o comercial no acredita permisos de desarrollo. No asumir que trial de IA permite ejecutar integraciones externas. Revisar condiciones vigentes antes de crear recursos.

Fuentes oficiales consultadas:
- https://learning.sap.com/courses/leveraging-the-sap-business-one-service-layer
- https://learning.sap.com/courses/leveraging-the-sap-business-one-service-layer/exploring-the-service-layer-api-architecture-and-capabilities
- https://learning.sap.com/courses/developing-ui-api-extensions-for-sap-business-one-web-client
- https://help.sap.com/doc/056f69366b5345a386bb8149f1700c19/10.0/en-US/Service%20Layer%20API%20Reference.html
- https://www.sap.com/products/technology-platform/trial.html
- https://www.sap.com/products/artificial-intelligence/core-ai-trial.html

## Secuencia y seguimiento
Se conserva la numeración solicitada. Seguridad básica se aplica desde el primer día; analítica introductoria del módulo 4 puede apoyar SQL después del módulo 2. No empezar por MCP antes de entender una API.
Escala por módulo: no iniciado → en estudio → laboratorio completado → validado.
Laboratorio completado significa ejecutado con evidencia; validado requiere interpretar resultado y explicar una decisión sin copiar la solución.

| Módulo / estado | Objetivo y prerrequisito | Teoría y ejercicio | Entregable / evidencia | Evaluación y competencia a validar |
|---|---|---|---|---|
| 1 / en estudio | Ubicar componentes; experiencia funcional | Clientes, bases, SLD, Service Layer, DI API/SDK, B1if, cloud; mapear una consulta de OC | Mapa, inventario de herramientas, explicación propia | ¿Dónde aplicar reglas y dónde persistir datos? Elegir una interfaz y reconocer límites |
| 2 / no iniciado | Consultar datos; M1 y SQL básico | OCRD/OITM, OPOR/POR1, ORDR/RDR1, OINV/INV1; JOIN, GROUP BY, CTE, parámetros, rendimiento, HANA vs SQL; UDF/UDT/UDO | Consultas de compras, stock, ventas y saldos con dataset sintético y resultados esperados | ¿Por qué un JOIN duplica totales? Consultas de lectura verificadas |
| 3 / no iniciado | Integrar por API; M1–2 y HTTP/JSON guiado | REST, sesiones, cookies, OAuth según entorno, OData v4, GET/POST/PATCH/DELETE, paginación, errores; Postman y Python, luego .NET | Mock local explícito y cliente de lectura; contrato, logs anonimizados y casos de error | Distinguir 401/403/404; evitar perder páginas; conexión real queda pendiente hasta tener acceso |
| 4 / no iniciado | Configurar analítica; M2 y entorno compatible | Vistas, filtros, UDQ, Linked Views, General Overview, KPIs, Crystal y Microsoft 365 según disponibilidad | Dashboard local educativo; réplica Web Client solo con acceso | ¿Qué filtro cambia el KPI? Identificar qué evidencia es local y cuál SAP |
| 5 / no iniciado | Extender UI; M3, JavaScript/TypeScript básico y Node | Proyecto VS Code, controles/eventos, inspector, debugging, webhooks, empaquetado y despliegue | Extensión documentada; prueba real pendiente si falta Web Client | Diferenciar evento UI de webhook; no llamar extensión SAP validada a una maqueta |
| 6 / no iniciado | Aplicar IA; contrato de M3, evaluación existente v8 | BTP/AI Core/hub, prompts, extracción, validación, AI UDQ/Ask AI y relación de Joule por producto | Asistente que propone consultas permitidas para revisión; evaluación y límites | Detectar SQL inventado y datos sensibles; ninguna escritura automática |
| 7 / no iniciado | Orquestar herramientas; M3 y M6 | MCP tools/resources/context, function calling, permisos, auditoría, inyección de instrucciones, revisión humana, Build Process Automation | Agente educativo con herramientas de lectura permitidas y pruebas de rechazo | ¿Una tool tiene acceso por existir? Separar capacidad, permiso y aprobación |
| 8 / no iniciado | Administrar y auditar; M1 y experiencia del resto | Usuarios/licencias, IAM/SSO/MFA, SLD, backups/restore, monitoreo/OpenTelemetry, CCC, actualizaciones y planes v11 | Guía de auditoría con evidencias ficticias y plan de restauración verificable | Un backup sin prueba de restore no demuestra recuperación; distinguir release de roadmap |

Pendientes comunes: verificar herramientas personales, disponibilidad real de SAP y comprensión del alumno. Ninguna competencia se marca adquirida por leer este documento.

## Evolución propuesta del proyecto
Mantener los contratos y experimentos históricos sin sobrescribirlos.
1. Continuar la orquestación en Python sin nuevas llamadas IA: recibir una respuesta v8 guardada, validar y proponer siguiente paso. Guardar estado del flujo aparte de las seis claves del clasificador.
2. Añadir repositorio de datos sintéticos para consulta: identificadores internos y números visibles explícitos.
3. Introducir un adaptador de lectura a una API local simulada con contrato reducido.
4. Añadir adaptador real Service Layer solo con entorno autorizado, autenticación y permisos comprobados.
5. Exponer dashboard de tickets y trazabilidad: entrada, clasificación, revisión, consulta y recomendación.
6. Incorporar recomendaciones fundadas y herramientas MCP con listas de operaciones permitidas, registro y supervisión.
7. Evaluar casos válidos, falta de datos, permiso denegado, documento inexistente y contenido malicioso. No ejecutar SQL propuesto por IA sin controles.

Carpetas futuras propuestas: src/orchestration, src/adapters, tests, labs/b1-integration y docs/architecture. No fueron creadas todavía. Ningún modelo ni gasto externo es necesario para los primeros ejercicios.

## Módulo 1 — Lección 1: arquitectura
Objetivo: ubicar interfaz, reglas del ERP, persistencia y componentes de administración antes de desarrollar.
Una arquitectura describe responsabilidades y comunicaciones. No significa que cada componente tenga su propio servidor.

- Cliente de escritorio y Web Client: interfaces con las que trabaja la persona; las capacidades no son idénticas.
- Base de empresa: datos persistentes de la compañía. Según instalación se usa SQL Server o SAP HANA; no son dos nombres para el mismo motor.
- Service Layer: servidor de aplicación que expone objetos y servicios de B1 mediante HTTP/OData y JSON. Una integración puede solicitar objetos de negocio sin manipular directamente sus tablas.
- DI API: interfaz de programación para lógica y objetos de negocio, muy usada desde aplicaciones/add-ons; sus requisitos se estudian por separado.
- SDK: conjunto de herramientas/documentación; no es una base ni una interfaz única.
- SLD (System Landscape Directory): registra y administra información del landscape; no almacena las líneas de las órdenes de compra.
- Integration Framework (B1if): plataforma para escenarios de integración; distinta de Service Layer.
- Cloud: describe despliegue/operación; no garantiza una API pública ni elimina requisitos de licenciamiento.
- Multitenancy: gestión de varios clientes/tenants con aislamiento. No autoriza mezclar sus datos.

Mapa conceptual de una futura integración de lectura:
Aplicación de soporte → Service Layer → servicios/objetos de negocio B1 → base de empresa.
SLD y servicios de identidad/licencias apoyan el landscape; no son pasos obligatorios de cada consulta de documento.
Este esquema no pretende describir el acceso interno del cliente de escritorio.

Ejemplo: un ticket pide revisar la OC 4500123. Nuestra aplicación consultará PurchaseOrders en Service Layer, si tiene autorización. En SQL, OPOR representa cabecera y POR1 líneas; DocEntry relaciona cabecera y líneas. DocNum es el número visible y no debe asumirse igual a DocEntry. En entornos reales puede requerirse además identificar empresa/serie.
Una consulta SQL de lectura sirve para análisis; crear o corregir documentos exige usar vías soportadas que apliquen lógica del ERP. No escribir directamente en tablas de negocio.

### Laboratorio B1-01A — inventario y decisión de arquitectura
Duración orientativa: 20–30 minutos. No requiere SAP ni instalaciones nuevas.

1. En Windows, abrir VS Code. Elegir Archivo → Abrir carpeta y crear/abrir una carpeta nueva llamada SAP-B1-Learning en Documentos. No modificar una carpeta de otro proyecto.
2. Crear arquitectura-01.md. Anotar:
   - Interfaz de usuario:
   - Componente para integrar aplicación externa:
   - Lugar donde persisten los documentos:
   - Componente para localizar/administrar el landscape:
   - Riesgo de escribir directamente en tablas:
   - Diferencia entre número de OC y clave interna:
3. Terminal → Nueva terminal. Si está usando PowerShell, ejecutar uno por uno:
   - `py --version`: muestra la versión del lanzador Python; si falla probar `python --version`. Anotar el resultado, no instalar todavía.
   - `git --version`: informa si Git está disponible desde esa terminal.
   - `dotnet --list-sdks`: lista SDKs .NET, no solo runtimes. Visual Studio instalado no garantiza un SDK concreto.
   - `code --version`: comprueba el comando de VS Code; su ausencia no demuestra que el editor no esté instalado.
4. No hace falta instalar Node/Postman/SQL Server para esta lección. Se comprobarán cuando corresponda.
5. Caso: una aplicación Python necesita consultar una OC y mostrar proveedor, fecha y líneas. Explicar qué componente elegiría y por qué. No ejecutar todavía una llamada ni compartir URL/credenciales de una empresa.
6. Aportar el texto del archivo y una captura de las versiones sin información sensible.

Validación: justificar Service Layer para el escenario de API; distinguir SLD de base de empresa; explicar que no se debe asumir DocNum=DocEntry. Si hay errores de herramientas, interpretarlos antes de instalar o cambiar configuración.
Evidencia actual: ninguna ejecución del alumno recibida. Laboratorio preparado, no completado ni validado.

### Inglés profesional
Pregunta: “How would you integrate an external application with SAP Business One?”
Respuesta modelo para una propuesta, no experiencia ya acreditada:
“I would first confirm the SAP Business One version, the available integration interfaces, and the required permissions. For a read-only web integration, I would consider Service Layer to access business objects. I would validate authentication, document identifiers, pagination, and error handling before connecting to a real environment.”
Vocabulario: landscape = conjunto de componentes; business object = objeto de negocio; company database = base de empresa; read-only integration = integración de lectura.

## Registro
| Fecha | Actividad | Estado | Evidencia / pendiente |
|---|---|---|---|
| 2026-10-27 | PDF y fuentes oficiales revisados; repositorio inspeccionado | Preparación completada | Referencias y archivos revisados arriba |
| 2026-10-27 | M1 / Lección 1 | En estudio | Lectura y respuesta del alumno pendientes |
| 2026-10-27 | B1-01A | No iniciado | Inventario, mapa y explicación pendientes |


## Base de experiencia previa recuperada — 27/10/2026
Ajuste solicitado por el alumno: la capacitación debe aprovechar su trabajo previo de soporte y análisis de SAP Business One sobre HANA. No tratar al alumno como principiante absoluto en SQL, tablas o procesos ERP. Presentar teoría técnica nueva antes de cada práctica, comprobar comprensión con casos y profundizar donde haya brechas.

Se recuperaron conversaciones históricas de septiembre y octubre sobre:
- Relevamiento mediante matriz maestra de usuarios, autorizaciones, licencias, componentes, cuentas técnicas e interfaces.
- Consultas sobre OUSR y actividad documental por usuario en OPOR, OPCH, OIGE, OIGN, ORCT, OVPM y OINV (conversación del 24/09).
- Reporte de órdenes de compra por período, cabecera/líneas OPOR y POR1, parámetros y estados pendientes.
- Investigación de notas de crédito y facturación electrónica mediante ORIN, OINV, tablas de usuario de una extensión y metadatos HANA SYS.TABLE_COLUMNS (30/09).
- Diagnóstico de integraciones, alertas, trazabilidad de documentos y distinción entre permisos y licenciamiento.
- Estudio posterior de UDF, UDT, UDO, búsquedas formateadas y circuito de compras (10/10).

Son antecedentes recuperados de conversaciones, no ejecuciones nuevas ni validación de dominio completo. La matriz histórica fue localizada en un archivo privado; la lectura de vista previa no devolvió celdas. No se atribuyen a sus celdas contenidos sin inspección. No se publican aquí la matriz, nombres de usuarios/servidores, cantidades de licencias, identificadores de documentos, datos de empresa ni SQL interno.

Aplicación al programa:
- M1: relacionar arquitectura con investigaciones y componentes ya conocidos; dedicar más tiempo a responsabilidades técnicas y vías de integración.
- M2: comenzar con un diagnóstico breve de cabecera/líneas, claves internas, JOIN, filtros y agregaciones usando datos ficticios; profundizar en CTE, rendimiento, metadatos y diferencias de dialecto según resultado.
- M3: convertir un caso conocido de consulta SQL de compras en una integración de lectura por API. La experiencia SQL no acredita todavía experiencia desarrollando Service Layer.
- M8: aprovechar la experiencia de relevamiento y auditoría para explicar IAM, monitoreo, licencias y administración técnica.
- Portafolio: reutilizar aprendizajes con ejemplos sintéticos, preservando la documentación empresarial privada.
El punto de reanudación continúa en M1, Lección 1, con este reconocimiento explícito de la experiencia previa.
