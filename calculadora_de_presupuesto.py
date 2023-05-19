def calcular_presupuesto():
    # Solicitar al usuario el total de sus ingresos mensuales
    ingresos = float(input("Ingrese el total de sus ingresos mensuales: "))

    # Inicializar un diccionario para almacenar los gastos por categoría
    categorias_gastos = {}

    # Inicializar la variable para almacenar el total de gastos
    total_gastos = 0

    # Ciclo principal para ingresar los gastos por categoría
    while True:
        # Solicitar al usuario la categoría de gasto o "fin" para terminar
        categoria = input("Ingrese la categoría de gasto (o 'fin' para terminar): ")

        # Verificar si el usuario ha ingresado "fin" para terminar el ingreso de gastos
        if categoria == "fin":
            break

        # Solicitar al usuario el monto del gasto
        monto = float(input("Ingrese el monto del gasto: "))

        # Verificar si la categoría ya existe en el diccionario
        if categoria in categorias_gastos:
            # Si la categoría existe, se agrega el monto del gasto al valor existente
            categorias_gastos[categoria] += monto
        else:
            # Si la categoría no existe, se crea una nueva clave en el diccionario con el monto del gasto
            categorias_gastos[categoria] = monto

        # Se actualiza el total de gastos sumando el monto del gasto actual
        total_gastos += monto

    # Calcular el presupuesto restando los gastos totales a los ingresos
    presupuesto = ingresos - total_gastos

    # Mostrar el resumen del presupuesto mensual
    print("\nResumen del presupuesto mensual:")
    print(f"Ingresos: {ingresos}")

    print("\nGastos por categoría:")
    for categoria, monto in categorias_gastos.items():
        print(f"{categoria}: {monto}")

    print(f"\nTotal de gastos: {total_gastos}")
    print(f"Presupuesto restante: {presupuesto}")


# Programa principal

print("Calculadora de presupuesto")
print("---------------------------")

# Llamar a la función calcular_presupuesto para iniciar el cálculo del presupuesto
calcular_presupuesto()
