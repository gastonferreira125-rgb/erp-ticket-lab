# Prototipo Power Apps: comparación de cantidades

Guía técnica del laboratorio con datos completamente ficticios. Las fórmulas siguientes permiten reproducir un prototipo de comparación de cantidades. Este documento no contiene capturas, datos empresariales, identificadores de entorno ni credenciales.

## Alcance

Comparación manual de cantidades, registro temporal en una colección y visualización en galería. La persistencia, la integración ERP y la automatización de documentos requieren implementación posterior. La exportación .msapp no está incluida en este documento.

## Componentes

| Componente | Responsabilidad |
| --- | --- |
| txtCantidadSolicitada | Entrada de texto clásica con cantidad solicitada |
| txtCantidadConfirmada | Entrada de texto clásica con cantidad confirmada |
| Etiqueta del encabezado | Diferencia calculada y color |
| Button1 | Registro de una comparación en OnSelect |
| colComparaciones | Tabla temporal con filas de comparación |
| Gallery1 | Presentación de filas de la colección |
| Etiqueta del pie | Contador de filas |

Los controles se ubican dentro de HeaderContainer1, MainContainer1 y FooterContainer1 según su función. Insertar un control requiere seleccionar primero su contenedor de destino.

## Convención del signo

La interfaz v0 usa Diferencia = Solicitada - Confirmada:
- Positivo: unidades menos confirmadas.
- Cero: coincidencia de cantidades.
- Negativo: unidades más confirmadas.

El CSV y LESSON_01.md usan la variación Confirmada - Solicitada. Son convenciones inversas. Antes de integrar o persistir resultados, se deberá unificar el contrato o utilizar nombres explícitos, por ejemplo FaltanteCantidad y VariacionCantidad. El campo Diferencia de esta colección no debe intercambiarse como si usara la convención del CSV.

## Fórmulas del prototipo

Sintaxis para una configuración regional que utiliza punto y coma para separar argumentos y campos de registros. Aplican a controles clásicos.

### Texto y color del resultado

Propiedad Text:

```powerfx
"Diferencia: " &
Text(
    Value(txtCantidadSolicitada.Text) -
    Value(txtCantidadConfirmada.Text)
)
```

Propiedad Color:

```powerfx
If(
    Value(txtCantidadSolicitada.Text) <>
    Value(txtCantidadConfirmada.Text);
    Color.DarkOrange;
    Color.DarkGreen
)
```

Value convierte texto numérico a número; Text convierte el resultado para su presentación; & concatena cadenas. Estas propiedades se recalculan al cambiar sus dependencias.

### Registro de una fila

Button1.OnSelect:

```powerfx
Collect(
    colComparaciones;
    {
        Solicitada: Value(txtCantidadSolicitada.Text);
        Confirmada: Value(txtCantidadConfirmada.Text);
        Diferencia:
            Value(txtCantidadSolicitada.Text) -
            Value(txtCantidadConfirmada.Text)
    }
)
```

Collect agrega una fila con los valores evaluados al ejecutar el botón. Cambiar las entradas después no actualiza las filas anteriores. Una colección conserva estado en memoria; guardar el diseño no persiste esas filas para otra sesión.

### Galería y contador

Gallery1.Items: `colComparaciones`.

Title1.Text:

```powerfx
"Solicitada: " & Text(ThisItem.Solicitada) &
" | Confirmada: " & Text(ThisItem.Confirmada)
```

Subtitle1.Text:

```powerfx
"Diferencia: " & Text(ThisItem.Diferencia)
```

ThisItem representa la fila de la plantilla que está mostrando la galería.

Etiqueta del pie:

```powerfx
"Comparaciones registradas: " & Text(CountRows(colComparaciones))
```

## Validación de presencia: definida, pendiente de evidencia

Button1.DisplayMode:

```powerfx
If(
    IsBlank(Trim(txtCantidadSolicitada.Text)) ||
    IsBlank(Trim(txtCantidadConfirmada.Text));
    DisplayMode.Disabled;
    DisplayMode.Edit
)
```

Esta regla comprueba presencia; todavía se deben validar conversión numérica, signos, precisión y reglas de negocio. La validación también deberá aplicarse al registrar y en el almacenamiento definitivo.

## Evolución siguiente: propuesta, pendiente de ejecución

- Agregar identificación de orden, con txtOrdenCompra.
- Incorporar OrdenCompra, EstadoComparacion y FechaRegistro al registro.
- Usar los estados Sin diferencia de cantidad y Pendiente de revisión.
- Exigir orden y ambas cantidades antes de registrar.
- Distinguir el resultado automático de una decisión comercial: coincidencia de cantidad no equivale a aprobación de la confirmación.
- Agregar proveedor, línea y artículo para emparejamiento real.
- Persistir datos y verificar reapertura antes de afirmar continuidad entre sesiones.

## Casos sintéticos para verificación

Los resultados de esta tabla son esperados; ejecutar los casos en la aplicación para comprobarlos.

| Caso | Solicitada | Confirmada | Resultado esperado |
| --- | ---: | ---: | --- |
| Coincidencia | 120 | 120 | 0, verde |
| Diferencia y registro | 100 | 80 | 20; nueva fila y contador incrementado |
| Exceso | 100 | 110 | -10, naranja |
| Cantidad vacía | 100 | vacía | Registro deshabilitado con regla de presencia |
| Dos registros sucesivos | 100/200 | 80/200 | Dos filas conservan sus valores |

## Etiquetas visibles y accesibilidad

Crear lblCantidadConfirmada y lblCantidadSolicitada dentro del contenedor principal, inmediatamente antes de sus entradas. Sus propiedades Text deben indicar Cantidad confirmada y Cantidad solicitada. AccessibleLabel en cada entrada describe su propósito a los lectores de pantalla; no sustituye la etiqueta visible. En un contenedor automático, ordenar los controles mediante el árbol.

## Guardado y recuperación

Guardar con Ctrl+S y comprobar confirmación. Descargar una copia .msapp desde el menú junto a Guardar. Guardar, publicar y persistir registros son operaciones distintas. En edición, usar Alt+clic para ejecutar un botón, o abrir la vista previa.

## Fuentes técnicas

- [Controles de entrada clásicos](https://learn.microsoft.com/es-es/power-apps/maker/canvas-apps/controls/control-text-input)
- [Value](https://learn.microsoft.com/es-es/power-platform/power-fx/reference/function-value)
- [If](https://learn.microsoft.com/es-es/power-platform/power-fx/reference/function-if)
- [Collect](https://learn.microsoft.com/es-es/power-platform/power-fx/reference/function-clear-collect-clearcollect)
- [IsBlank](https://learn.microsoft.com/es-es/power-platform/power-fx/reference/function-isblank-isempty)
- [Guardar y publicar](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/save-publish-app)
