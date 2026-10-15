# Controles parciales v7 — 15 de octubre de 2026

[responses.json](responses.json) conserva las dos respuestas originales T02/T04; [evaluation.json](evaluation.json) se obtuvo ejecutando evaluate.py contra los diez casos originales.

- Dos respuestas, dos tickets únicos; formato 2/2 y etiquetas 2/2 entre ejecutados.
- Cobertura única 2/10, no ronda completa ni exactitud general. Otros ocho casos aún sin ejecutar en v7.
- T02: datos_faltantes vacío; objetivo no cumplido.
- T04: cantidades del sistema/conteo y fecha; objetivo básico de utilidad cumplido, sin pedir almacén ya informado.
- Ejemplos EX01/EX02 son contexto preparado, no ejecuciones ni tickets evaluados.
- Diseño indicado: Sistema v6 y dos pares de ejemplos fijos; cambiar solo último Usuario. Sin payload final ni todos los parámetros actuales verificados.

T04 aplica un patrón muy cercano al ejemplo EX02. No demuestra generalización amplia. Resultados humanos distintos según caso: no afirmar mejora uniforme.

[Detalle T02](../2026-10-15-t02-v7/README.md), [detalle T04](../2026-10-15-t04-v7/README.md). Próximo T06 y después T10 sin cambiar ejemplos/reglas.
