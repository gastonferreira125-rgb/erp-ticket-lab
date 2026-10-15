# Respaldo XML final v8
[ERP_Tickets_v8_FewShot.xml](ERP_Tickets_v8_FewShot.xml) conserva los seis mensajes previstos, con último Usuario T02 para restaurar la plantilla. La última prueba de cierre fue T10; el archivo no pretende ser export del payload de esa ejecución.

Abrir en editor de texto, crear seis bloques en Launchpad, elegir roles por ui_role y copiar contenido íntegro de cada content sin etiquetas XML/delimitadores CDATA. Mantener los primeros cinco al cambiar ticket.

Temperatura 1 y streaming activado verificados previamente; máximo de tokens seleccionado no verificado (43690 solicitado; 65536 extremo visible). Revisar ese valor al restaurar. Modelo indicado Gemini 2.5 Flash Lite (001).

Formato propio del laboratorio; no export nativo SAP ni importación directa verificada. Validado con parser XML y recuperación exacta de los seis mensajes respecto de messages-t02.json. Sin credenciales/capturas. [Cierre](../../../docs/STAGE_1_CLOSURE.md).
