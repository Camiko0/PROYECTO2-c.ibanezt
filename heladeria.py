import utils.funciones
#from base import Base
#from complemento import Complemento

from models.models_bd import Producto
from models.models_bd import Ingrediente
from models.enum_ingredientes import Ingrediente_Enum

#Clase Heladeria que gestiona los Producto e Ingrediente
class Heladeria():
    def __init__(self) -> None:
        self.__productos = Producto.query.all()
        self.__ingredientes = Ingrediente.query.all()
        self.__ventas_del_dia = 0

    # Otros metodos
    def calcular_producto_mas_rentable(self) -> str:
        # Llama los metodos producto_calcular_costo, producto_calcular_rentabilidad y producto_calcular_mas_rentable de utils.funciones
        lista_productos  = []
        for producto in self.__productos:
            utils.funciones.imprimir("Producto: {}".format(producto.nombre), "amarillo")
            lista_ingredientes = []
            for ingrediente in producto.obtener_ingredientes():
                lista_ingredientes.append({"nombre": ingrediente.nombre, "precio": ingrediente.precio})
            utils.funciones.imprimir("-- Listado de ingredientes: {} ".format(lista_ingredientes), "verde")
            # Calcular costo
            utils.funciones.imprimir("-- El costo de producir el producto es: {}".format(utils.funciones.producto_calcular_costo(lista_ingredientes)), "azul")
            # Calcular rentabilidad
            rentabilidad = utils.funciones.producto_calcular_rentabilidad(ingrediente.precio_publico, lista_ingredientes)
            print("-- El rentabilidad del producto es: {}".format(rentabilidad))
            lista_productos.append({"nombre": producto.obtener_nombre(), "rentabilidad": rentabilidad})
        # Calcular producto más rentable
        utils.funciones.imprimir("-- Listado de productos: {} ".format(lista_productos), "magenta")
        return utils.funciones.producto_calcular_mas_rentable(lista_productos)
    
    def vender(self, nombre_producto: str) -> bool:
        producto_existe = False
        producto_vender = ""
        # Validar si el producto existe
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                producto_existe = True
                producto_vender = producto
                break

        # Si el producto existe, validar si hay disponibilidad de los ingredientes
        if producto_existe:
            utils.funciones.imprimir("-- El producto '{}' existe dentro de los productos de la heladeria".format(nombre_producto), "amarillo")
            # Validar uno a uno los ingredientes
            ingredientes_existentes = True
            for ingrediente in producto_vender.ingredientes:
                # Si es Base necesita 0.2
                if ingrediente.tipo_ingrediente.upper() == Ingrediente_Enum.BASE.name:
                    print("-- El ingrediente '{}' es de tipo Base y su inventario actual es {}".format(
                        ingrediente.nombre, ingrediente.inventario))
                    # Si un ingrediente no tiene existencia romper el bucle (En tal caso no se puede crear el producto)
                    if (ingrediente.inventario - 0.2) < 0:
                        ingredientes_existentes = False
                # Si es Complemento necesita 1
                elif ingrediente.tipo_ingrediente.upper() == Ingrediente_Enum.COMPLEMENTO.name:
                    print("-- El ingrediente '{}' es de tipo Complemento y su inventario actual es {}".format(
                        ingrediente.nombre, ingrediente.inventario))
                    # Si un ingrediente no tiene existencia romper el bucle (En tal caso no se puede crear el producto)
                    if (ingrediente.inventario - 1) < 0:
                        ingredientes_existentes = False
            
            # Restar existencias de los ingredientes en el inventario para crear el producto
            if ingredientes_existentes:
                for ingrediente in producto_vender.ingredientes:
                    # Si es Base necesita 0.2
                    if ingrediente.tipo_ingrediente.upper() == Ingrediente_Enum.BASE.name:
                        ingrediente.inventario = round(ingrediente.inventario - 0.2, 2)
                        print("-- El ingrediente '{}' es de tipo Base y su inventario luego de crear el producto es {}".format(
                            ingrediente.nombre, ingrediente.inventario))
                    # Si es Complemento necesita 1
                    elif ingrediente.tipo_ingrediente.upper() == Ingrediente_Enum.COMPLEMENTO.name:
                        ingrediente.inventario = round(ingrediente.inventario - 1, 2)
                        print("-- El ingrediente '{}' es de tipo Complemento y su inventario luego de crear el producto es {}".format(
                            ingrediente.nombre, ingrediente.inventario))
                self.__ventas_del_dia += 1
                utils.funciones.imprimir(">>>> El numero de ventas de hoy son: {}".format(self.__ventas_del_dia), "verde")
                return True
            else:
                utils.funciones.imprimir("-- El producto '{}' no tiene los ingredientes necesarios para fabricarlo".format(nombre_producto), "rojo")
                return False
        else:
            utils.funciones.imprimir("-- El producto '{}' no existe dentro de los productos de la heladeria".format(nombre_producto), "rojo")
            return False

    # Getters
    def obtener_ingredientes(self) -> list[Ingrediente]:
        return self.__ingredientes
    
    def obtener_productos(self) -> list[Producto]:
        return self.__productos
    
    def obtener_ventas_del_dia(self) -> int:
        return self.__ventas_del_dia

    # Setters
    def cargar_ingredientes(self, ingredientes: list[Ingrediente]) -> None:
        self.__ingredientes = ingredientes

    def cargar_productos(self, productos: list[Producto]) -> None:
        self.__productos = productos