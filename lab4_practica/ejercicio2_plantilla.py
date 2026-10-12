# SECCIÓN A: clasificación y visualización

def clasificar_existencia(cantidad):
    # TODO A1: retornar la clasificación correspondiente.
    if cantidad == 0:
        return "Agotado"
    elif 1 <= cantidad <= 5:
        return "Existencia baja" 
    else:
        return "Existencia suficiente"


def mostrar_inventario(existencias):
    print("\n--- INVENTARIO ---")

    # TODO A2:
    # Mostrar número de producto, cantidad y clasificación.
    for i in range (len(existencias)):
        numero_producto = i + 1
        cantidad = existencias[i]
        clasificación = clasificar_existencia(cantidad)
        print(f"Producto {numero_producto}: {cantidad} unidades - {clasificación}")


# SECCIÓN B: validación de entradas

def pedir_entero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: debes escribir un número entero.")
            continue

        if minimo <= valor <= maximo:
            return valor

        print(f"Error: el valor debe estar entre {minimo} y {maximo}.")


# SECCIÓN C: operaciones de inventario


def retirar_unidades(disponible, cantidad):
    # Si no hay unidades suficientes, informar y retornar disponible
    if cantidad > disponible:
        print(f"Error: Stock insuficiente. Solo hay {disponible} unidades disponibles.")
        return disponible
    # Si hay suficientes, retornar disponible - cantidad
    return disponible - cantidad


def reponer_unidades(disponible, cantidad):
    # Retornar disponible + cantidad
    return disponible + cantidad






# SECCIÓN D: programa principal

existencias = [8, 0, 4]

while True:
    # TODO D1: mostrar el menú de opciones.
       print("n--- GESTOR DE MATERIALES---")
       print("1. consultar inventario")
       print("2. retirar unidades de un  producto")
       print("3. reponer unidades de un producto")
       print("4. salir")

     
match opcion:
        case "1":
            mostrar_inventario(existencias)

        case "2" | "3":
            numero_producto = pedir_entero_en_rango(
                f"Número de producto (1 a {len(existencias)}): ",
                1,
                len(existencias)
            )

            cantidad = pedir_entero_en_rango(
                "Cantidad de unidades (1 a 20): ",
                1,
                20
            )

            indice = numero_producto - 1

            if opcion == "2":
                existencias[indice] = retirar_unidades(
                    existencias[indice],
                    cantidad
                )
            else:
                existencias[indice] = reponer_unidades(
                    existencias[indice],
                    cantidad
                )

            print(f"Existencia actual: {existencias[indice]}")

        case "4":
            print("Programa finalizado.")
s
        case _:
            print("Error: selecciona una opción entre 1 y 4.")