# Calcula si un ingrediente es sano validando 2 parámetros el número de calorías y si es vegetariano
def ingrediente_es_sano(numero_calorias: int, es_vegetariano: bool) -> bool:
    return numero_calorias < 100 or es_vegetariano

# Cuenta las calorias de un producto basado en las calorias de los ingredientes que lo componen
def producto_contar_calorias(lista_calorias: list[int], factor_multiplicacion: float) -> float:
    calorias_totales = 0
    for caloria in lista_calorias:
        calorias_totales += caloria
    return round(calorias_totales * factor_multiplicacion, 2)

# Calcula el costo de producir un producto basado en un diccionario de los ingredientes que lo componen
def producto_calcular_costo(lista_ingredientes: list[dict]) -> int:
    costo_total = 0
    for ingrediente in lista_ingredientes:
        if isinstance(ingrediente.get("precio"), int):
            costo_total += int(ingrediente.get("precio"))
        else:
            print("El precio del ingrediente {} no es de tipo int".format(ingrediente.get("nombre")))
    return costo_total

# Calcula la rentabilidad de un producto haciendo la operación = el precio del producto - el costo de producir el producto
def producto_calcular_rentabilidad(precio: int, lista_ingredientes: list[dict]) -> int:
    return precio - producto_calcular_costo(lista_ingredientes)

# Calcula el producto más rentable de una lista de productos que recibe como parámetro
def producto_calcular_mas_rentable(lista_productos: list[dict]) -> (str, float):
    mayor_rentabilidad = 0
    producto_mas_rentable = ""
    for producto in lista_productos:
        if isinstance(producto.get("rentabilidad"), float):
            if producto.get("rentabilidad") >= mayor_rentabilidad:
                mayor_rentabilidad = float(producto.get("rentabilidad"))
                producto_mas_rentable = str(producto.get("nombre"))
        else:
            print("La rentabilidad del producto {} no es de tipo float".format(producto.get("nombre")))  
    return (producto_mas_rentable, mayor_rentabilidad)

def imprimir(mensaje: str, color: str):
    colores = {
        "negro": "\033[30m",
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m",
        "magenta": "\033[35m",
        "cian": "\033[36m",
        "blanco": "\033[37m",
    }
    print(colores.get(color) + mensaje)