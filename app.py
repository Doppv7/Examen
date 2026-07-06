import os
import modulo as the_m


def main():
    # Creo los diccionarios del anunciado
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, True],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }

    inventario = {"P101": [30, 15], "P102": [120, 50], "P103": [0, 10], "P104": [0, 25]}

    while True:
        os.system("cls")
        print("""
        ========== MENÚ PRINCIPAL ==========
        1. Stock por Categoría 
        2. Buscar rango de Precio
        3. Actualizar Precio
        4. Agregar Producto 
        5. Eliminar Producto 
        6. Mostrar Productos
        7. Salir
        ====================================
            """)
        opcion = the_m.leer_opcion()
        if opcion == -1:
            print(
                "ERROR, la opción ingresada es invalida. Por favor, ingrese una opción válida."
            )
            continue

        match opcion:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case 7:
                os.system("cls")
                print("===== SALIR =====")
                print("Gracias por utilizar nuestra app!! :)")
                os.system("pause")

            case _:
                print("ERROR, opción no valida. Por favor ingrese una opción válida.")
