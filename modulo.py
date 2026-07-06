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
