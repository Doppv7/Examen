def validar_codigo(codigo, productos):
    if not codigo or codigo.strip() == "":
        return False
    return codigo.strip().upper() not in productos


def validar_nombre(nombre):
    return len(nombre.strip()) > 0


def validar_categoria(categoria):
    return len(categoria.strip()) > 0


def validar_precio(precio):
    try:
        valor = int(precio)
        return valor > 0
    except ValueError:
        return False


def validar_disponibilidad(opcion):
    return opcion.strip().lower() in ["s", "n"]


def validar_stock(stock):
    try:
        valor = int(stock)
        return valor >= 0
    except ValueError:
        return False


def validar_vendidos(vendidos):
    try:
        valor = int(vendidos)
        return valor >= 0
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


# ------------------------------------------------------------ OPERACIONES
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


def buscar_precio(precio_min, precio_max, productos, inventario):
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
        print(f"{nombre}--{codigo}")


def buscar_codigo(codigo, productos):
    return codigo.strip().upper() in productos


def actualizar_precio(codigo, nuevo_precio, productos):
    llave = codigo.strip().upper()
    if llave in productos:
        productos[llave][2] = nuevo_precio
        return True
    return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):
    if not validar_codigo(codigo, productos):
        return False

    llave_final = codigo.strip().upper()
    bool_disponible = disponible.strip().lower() == "s"

    productos[llave_final] = [
        nombre.strip(),
        categoria.strip(),
        int(precio),
        bool_disponible,
    ]
    inventario[llave_final] = [int(stock), int(vendidos)]
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
    for codigo, datos in productos.items():
        print(f"CODIGO: {codigo} --------------------------")
        print(f"Nombre: {datos[0]}")
        print(f"Categoría: {datos[1]}")
        print(f"Precio: ${datos[2]}")
        print(f"Disponible: {datos[3]}")
        print(f"Stock: {inventario[codigo][0]}")
        print(f"Vendidos: {inventario[codigo][1]} --------------------------")
