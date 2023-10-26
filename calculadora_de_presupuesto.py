import csv
import os
import matplotlib.pyplot as plt

def calcular_presupuesto():
    archivo = input("Ingrese el nombre del archivo para guardar los datos: ")
    ingresos = float(input("Ingrese el total de sus ingresos mensuales: "))
    categorias_gastos = {}
    total_gastos = 0

    while True:
        categoria = input("Ingrese la categoría de gasto (o 'fin' para terminar): ")
        if categoria == "fin":
            break
        monto = float(input("Ingrese el monto del gasto: "))
        if categoria in categorias_gastos:
            categorias_gastos[categoria] += monto
        else:
            categorias_gastos[categoria] = monto
        total_gastos += monto

    presupuesto = ingresos - total_gastos

    print("\nResumen del presupuesto mensual:")
    print(f"Ingresos: {ingresos}")
    print("\nGastos por categoría:")
    for categoria, monto in categorias_gastos.items():
        print(f"{categoria}: {monto}")
    print(f"\nTotal de gastos: {total_gastos}")
    print(f"Presupuesto restante: {presupuesto}")

    with open(archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Categoría", "Monto"])
        for categoria, monto in categorias_gastos.items():
            writer.writerow([categoria, monto])
        writer.writerow(["Total de gastos", total_gastos])
        writer.writerow(["Presupuesto restante", presupuesto])

    # Crear un gráfico de barras para mostrar la distribución de gastos por categoría
    categorias = list(categorias_gastos.keys())
    montos = list(categorias_gastos.values())

    fig, ax = plt.subplots()

    ax.bar(categorias, montos)
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Monto")
    ax.set_title("Distribución de Gastos por Categoría")
    ax.tick_params(axis='x', rotation=45)  # Rotar las etiquetas en el eje X para una mejor legibilidad

    # Agregar anotaciones para ingresos y gastos
    ax.annotate(f"Ingresos: {ingresos}", xy=(0.5, 0.9), xycoords='axes fraction', ha='center')
    ax.annotate(f"Total de Gastos: {total_gastos}", xy=(0.5, 0.8), xycoords='axes fraction', ha='center')
    ax.annotate(f"Presupuesto Restante: {presupuesto}", xy=(0.5, 0.7), xycoords='axes fraction', ha='center')

    # Agregar datos numéricos junto a las barras
    for i, mont in enumerate(montos):
        ax.annotate(f"{mont:.2f}", xy=(i, mont), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

def cargar_presupuesto():
    try:
        archivo = input("Ingrese el nombre del archivo que desea cargar: ")
        if os.path.exists(archivo):
            with open(archivo, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                print("\nPresupuesto cargado desde el archivo:")
                for row in reader:
                    print(f"{row[0]}: {row[1]}")
        else:
            print(f"\nNo se encontró el archivo '{archivo}'. Intente nuevamente.")
    except FileNotFoundError:
        print("\nNo se encontró el archivo de presupuesto. Intente nuevamente.")

print("Calculadora de presupuesto")
print("---------------------------")

cargar = input("¿Desea cargar un presupuesto existente? (s/n): ").lower()

if cargar == "s":
    cargar_presupuesto()
else:
    calcular_presupuesto()
