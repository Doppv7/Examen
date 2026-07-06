def validar_texto(texto):
    return len(texto.strip()) > 0


def validar_numero(numero_str, permitir_cero=False):
    try:
        valor = int(numero_str)
        if permitir_cero:
            return valor >= 0
        else:
            return valor > 0
    except ValueError:
        return False


def leer_opcion():
    try:
        opcion = int(input("Ingrese una opción:\n"))
        if 1 <= opcion <= 7:
            return opcion
        else:
            return -1
    except ValueError:
        return -1


def validar_codigo_nuevo(codigo, productos):
    if not validar_texto(codigo):
        return False
    codigo_limpio = codigo.strip().lower()
    return not any(llave.lower() == codigo_limpio for llave in productos)


def validar_disponibilidad(opcion):
    return opcion.strip().lower() in ["s", "n"]


# -------------------------------------------------------------------Modulo Principal


def buscar_rango_precio(precio_min, precio_max, productos, inventario):
    encontrados = []
    for codigo, datos in productos.items():
        precio = datos[2]
        stock = inventario[codigo][0]
        if precio_min <= precio <= precio_max and stock > 0:
            encontrados.append((datos[0], codigo))
    if not encontrados:
        print(
            "No se encontraron productos en el rango de precio especificado con stock disponible."
        )
        return
    encontrados.sort()
    print(f"Productos entre ${precio_min} y ${precio_max} con stock disponible:")
    for nombre, codigo in encontrados:
        print(f"- {nombre} (Código: {codigo})")
    return encontrados


def buscar_codigo(codigo, productos):
    return codigo.strip().upper() in productos


def stock_categoria(categoria, productos, inventario):
    stock_total = 0
    categoria_buscar = categoria.strip().lower()
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria_buscar:
            if codigo in inventario:
                stock_total += inventario[codigo][0]
    print(
        f"El stock total de la categoría '{categoria_buscar.capitalize()}' es: {stock_total}"
    )


def actualizar_precio(codigo, nuevo_precio, productos):
    codigo_buscar = codigo.strip().lower()
    for llave, datos in productos.items():
        if llave.lower() == codigo_buscar:
            datos[2] = nuevo_precio
            return True
    return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible_str,
    stock,
    vendido,
    productos,
    inventario,
):
    if not validar_codigo_nuevo(codigo, productos):
        return False
    try:
        precio_num = int(precio)
        stock_num = int(stock)
        vendido_num = int(vendido)
    except ValueError:
        print("Error: El precio, stock y vendido deben ser números válidos.")
        return False

    llave_final = codigo.strip().upper()
    bool_disponible = disponible_str.strip().lower() == "s"

    productos[llave_final] = [
        nombre.strip(),
        categoria.strip(),
        precio_num,
        bool_disponible,
    ]
    inventario[llave_final] = [stock_num, vendido_num]
    return True


def eliminar_producto(codigo, productos, inventario):
    llave_buscar = codigo.strip().upper()
    if llave_buscar in productos:
        del productos[llave_buscar]
        if llave_buscar in inventario:
            del inventario[llave_buscar]
        return True
    return False


def mostrar_productos(productos, inventario):
    if not productos:
        print("El sistema no tiene productos registrados.")
        return
    print("Listado de productos:")
    for codigo, datos in productos.items():
        print(f"""----------------------------------
Código: {codigo}
Nombre: {datos[0]}
Categoría: {datos[1]}
Precio: ${datos[2]}
Disponible: {'Sí' if datos[3] else 'No'}
Stock: {inventario[codigo][0]}
Vendidos: {inventario[codigo][1]}
----------------------------------""")
