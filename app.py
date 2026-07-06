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
            print(
                "ERROR, la opción ingresada es invalida. Por favor, ingrese una opción válida."
            )
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
                        the_m.buscar_rango_precio(
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
                            if the_m.validar_numero(
                                str(nuevo_precio), permitir_cero=False
                            ):
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
                        print("ERROR, el código ingresado no existe en el inventario.")

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
                codigo = input("Ingrese el codigo del nuevo producto:\n")
                if not the_m.validar_codigo_nuevo(codigo, productos):
                    print("ERROR, el código ingresado ya exise o se encuentra vacío.")
                    input("Presione Enter para continuar...")
                    continue
                nombre = input("Ingrese el nombre del nuevo producto:\n")
                if not the_m.validar_texto(nombre):
                    print("ERROR, el nombre del producto no puede estar vacío.")
                    input("Presione Enter para continuar...")
                    continue
                categoria = input("Ingrese la categoría del nuevo producto:\n")
                if not the_m.validar_texto(categoria):
                    print("ERROR, la categoría del producto no puede estar vacía.")
                    input("Presione Enter para continuar...")
                    continue
                precio_str = input("Ingrese el precio del nuevo producto:\n")
                if not the_m.validar_numero(precio_str, permitir_cero=False):
                    print("ERROR, el precio debe ser un número entero mayor a cero.")
                    input("Presione Enter para continuar...")
                    continue
                disponible_str = input(
                    "Ingrese la disponibilidad del nuevo producto. Disponible: 's' o No Disponible: 'n':\n"
                )
                if not the_m.validar_disponibilidad(disponible_str):
                    print(
                        "ERROR, ka disponibilidad deber ser 's' para Disponible o 'n' para No Disponible."
                    )
                    input("Presione Enter para continuar...")
                    continue
                stock_str = input("Ingrese la cantidad de stock del nuevo producto:\n")
                if not the_m.validar_numero(stock_str, permitir_cero=True):
                    print(
                        "ERROR, la cantidad de stock debe ser un número entero mayor o igual a cero."
                    )
                    input("Presione Enter para continuar...")
                    continue
                vendido_str = input(
                    "Ingrese la cantidad de preoductos vendidos del nuevo producto:\n"
                )
                if not the_m.validar_numero(vendido_str, permitir_cero=True):
                    print(
                        "ERROR, la cantidad de productos vendidos debe ser un número entero mayor o igual a cero."
                    )
                    input("Presione Enter para continuar...")
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
                    print("¡Producto agregado correctamente!")
                else:
                    print("Ocurrio un error al agregar el producto.")

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
                print("ERROR, opción no valida. Por favor ingrese una opción válida.")


# ------------------------el codigo casi me gana, no me ejecutava la prev y no entendi por que
# ------------------------tuve que pedirle ayuda a mi primo geminiardo y en resumidas cuentas me dijo
# ------------------------que eso hara que py llame si este archivo (app.py)
# ------------------------es el que el usuario ejecutó directamente
# ------------------------(y no un módulo importado) entonces arranca la función main()
# ------------------------batalle, no se lo negare arturo, pero me enseño mucho, solo que son muchos modulos y cosas que memorizar
# ------------------------y no me da la cabeza para tanto, pero bueno, lo importante es que aprendi y lo logre
# ------------------------gracias arturo, ojala poder conseguir el proximo semestre clases con usted
# ------------------------me gusta mucho su forma de enseñar y explicar
# ----------------------- y me hace sentir que puedo aprender mucho mas de lo que creia posible


if __name__ == "__main__":
    main()
