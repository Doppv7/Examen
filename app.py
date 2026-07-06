import os
import modulo as the_m


def main():
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
            print("Debe seleccionar una opción válida")
            os.system("pause")
            continue

        match opcion:
            case 1:
                os.system("cls")
                print("===== STOCK POR CATEGORÍA =====")
                categoria = input(
                    "Ingrese la categoría la cual desea consultar su stock:\n"
                )
                the_m.stock_categoria(categoria, productos, inventario)
                os.system("pause")

            case 2:
                os.system("cls")
                print("===== BUSCAR RANGO DE PRECIO =====")
                try:
                    precio_min = int(input("Ingrese el precio mínimo:\n"))
                    precio_max = int(input("Ingrese el precio máximo:\n"))
                    if precio_min > precio_max:
                        print(
                            "ERROR, el precio mínimo no puede ser mayor al precio máximo."
                        )
                    else:
                        the_m.buscar_precio(
                            precio_min, precio_max, productos, inventario
                        )
                except ValueError:
                    print(
                        "ERROR, debe ingresar un valor númerico entero para los precios."
                    )
                os.system("pause")

            case 3:
                os.system("cls")
                while True:
                    print("===== ACTUALIZAR PRODUCTO =====")
                    codigo = input(
                        "Ingrese el código del producto que desea actualizar su precio:\n"
                    )
                    if the_m.buscar_codigo(codigo, productos):
                        try:
                            nuevo_precio = int(
                                input("Ingrese el nuevo precio del producto:\n")
                            )
                            if the_m.validar_precio(str(nuevo_precio)):
                                the_m.actualizar_precio(codigo, nuevo_precio, productos)
                                print("¡El precio se actualizo correctamente!")
                            else:
                                print(
                                    "ERROR, el precio debe ser un número entero mayor a cero."
                                )
                        except ValueError:
                            print(
                                "ERROR, debe ingresar un valor númerico entero para el precio."
                            )
                    else:
                        print("Código inexistente")

                    continuar = (
                        input("¿Desea actualizar otro producto?: (s/n):\n")
                        .strip()
                        .lower()
                    )
                    if continuar != "s":
                        break
                    os.system("cls")
                os.system("pause")

            case 4:
                os.system("cls")
                print("===== AGREGAR PRODUCTO =====")
                codigo = input("Ingrese el CÓDIGO del nuevo producto:\n")
                if not the_m.validar_codigo(codigo, productos):
                    print(
                        "ERROR: El código ya existe, está vacío o contiene solo espacios."
                    )
                    os.system("pause")
                    continue
                nombre = input("Ingrese el NOMBRE del nuevo producto:\n")
                if not the_m.validar_nombre(nombre):
                    print("ERROR: El nombre del producto no puede estar vacío.")
                    os.system("pause")
                    continue
                categoria = input("Ingrese la CATEGORÍA del nuevo producto:\n")
                if not the_m.validar_categoria(categoria):
                    print("ERROR: La categoría del producto no puede estar vacía.")
                    os.system("pause")
                    continue
                precio_str = input("Ingrese el PRECIO del nuevo producto:\n")
                if not the_m.validar_precio(precio_str):
                    print("ERROR: El precio debe ser un número entero mayor que cero.")
                    os.system("pause")
                    continue
                disponible_str = input(
                    "Ingrese la disponibilidad ('s' para Disponible / 'n' para No Disponible):\n"
                )
                if not the_m.validar_disponibilidad(disponible_str):
                    print("ERROR: La disponibilidad debe ser estrictamente 's' o 'n'.")
                    os.system("pause")
                    continue
                stock_str = input("Ingrese la cantidad de STOCK inicial:\n")
                if not the_m.validar_stock(stock_str):
                    print(
                        "ERROR: El stock debe ser un número entero mayor o igual a cero."
                    )
                    os.system("pause")
                    continue
                vendido_str = input("Ingrese la cantidad de productos VENDIDOS:\n")
                if not the_m.validar_vendidos(vendido_str):
                    print(
                        "ERROR: La cantidad de vendidos debe ser un número entero mayor o igual a cero."
                    )
                    os.system("pause")
                    continue
                exito = the_m.agregar_producto(
                    codigo,
                    nombre,
                    categoria,
                    precio_str,
                    disponible_str,
                    stock_str,
                    vendido_str,
                    productos,
                    inventario,
                )
                if exito:
                    print("¡Producto guardado y registrado con éxito en el sistema!")
                else:
                    print("Ocurrió un error inesperado al procesar el registro.")
                os.system("pause")

            case 5:
                os.system("cls")
                print("===== ELIMINAR PRODUCTO =====")
                codigo = input("Ingrese el código del producto que desea eliminar: \n")
                fue_eliminado = the_m.eliminar_producto(codigo, productos, inventario)
                if fue_eliminado:
                    print("¡Producto eliminado con éxito de ambos registros!")
                else:
                    print("Código ingresado no existe")
                os.system("pause")

            case 6:
                os.system("cls")
                print("===== MOSTRAR PRODUCTOS =====")
                the_m.mostrar_productos(productos, inventario)
                os.system("pause")

            case 7:
                os.system("cls")
                print("===== SALIR =====")
                print("Gracias por utilizar nuestra app!! :)")
                os.system("pause")
                break

            case _:
                print("Debe seleccionar una opción válida")
                os.system("pause")


if __name__ == "__main__":
    main()
