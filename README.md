# Calculadora de presupuesto

Este programa de Python permite a los usuarios realizar un seguimiento de sus ingresos y gastos, y proporciona un resumen del presupuesto mensual. El usuario debe ingresar el total de sus ingresos mensuales y luego ingresar los gastos por categoría. Al final, se mostrará un resumen del presupuesto mensual.

## Funcionalidades

- Solicita al usuario el total de sus ingresos mensuales.
- Permite al usuario ingresar los gastos por categoría.
- Calcula el presupuesto restando los gastos totales a los ingresos.
- Muestra un resumen del presupuesto mensual, incluyendo los ingresos, los gastos por categoría, el total de gastos y el presupuesto restante.

## Requisitos

- Python 3.x instalado en tu sistema.
- Las siguientes bibliotecas Python: `csv`, `os`, y `matplotlib`.

## Uso

1. Ejecuta el programa en Python.
2. Elige si deseas cargar un presupuesto existente o crear uno nuevo.
3. Si decides crear uno nuevo, ingresa tus ingresos mensuales y luego registra tus gastos por categoría. Para finalizar el registro de gastos, ingresa "fin".
4. El programa mostrará un resumen del presupuesto mensual, incluyendo ingresos, gastos por categoría, el total de gastos y el presupuesto restante.
5. Además, se generará un gráfico de barras que muestra la distribución de gastos por categoría.
6. Si decides cargar un presupuesto existente, proporciona el nombre del archivo CSV que contiene los datos.
7. El programa cargará los datos y mostrará el resumen del presupuesto cargado desde el archivo.

## Ejemplo

```python
Calculadora de presupuesto
---------------------------

Ingrese el total de sus ingresos mensuales: 2500

Ingrese la categoría de gasto (o 'fin' para terminar): Alimentos
Ingrese el monto del gasto: 500

Ingrese la categoría de gasto (o 'fin' para terminar): Transporte
Ingrese el monto del gasto: 200

Ingrese la categoría de gasto (o 'fin' para terminar): Finanzas
Ingrese el monto del gasto: 100

Ingrese la categoría de gasto (o 'fin' para terminar): fin

Resumen del presupuesto mensual:
Ingresos: 2500.0

Gastos por categoría:
Alimentos: 500.0
Transporte: 200.0
Finanzas: 100.0

Total de gastos: 800.0
Presupuesto restante: 1700.0
```


En este ejemplo, el usuario ingresó un total de ingresos mensuales de 2500. Luego, ingresó gastos en las categorías de Alimentos, Transporte y Finanzas. El programa calculó el presupuesto restante, que fue de 1700, y mostró un resumen del presupuesto mensual.

## Nota: 
Asegúrate de tener Python instalado en tu sistema para poder ejecutar el programa.
