from db import db
from models.enum_ingredientes import Ingrediente_Enum
from models.enum_productos import Producto_Enum
import utils.funciones

#Tabla de rompimiento entre ingrediente y producto
class Productos_Ingredientes(db.Model):
    __tablename__ = 'productos_ingredientes'
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)

#Tabla ingrediente con sus metodos 
class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'
    id = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo_ingrediente = db.Column(db.String(50), nullable=False)
    sabor = db.Column(db.String(50))

    productos = db.relationship('Producto', secondary='productos_ingredientes')

    # Calcular si es sano
    def es_sano(self) -> bool:
        return utils.funciones.ingrediente_es_sano(self._calorias, self._es_vegetariano)
    
    #Abastecer de acuerdo al tipo de ingrediente
    def abastecer(self) -> None:
        if self.tipo_ingrediente.upper() == Ingrediente_Enum.COMPLEMENTO.name:
            self.inventario += 10
        else:
            self.inventario += 5

    #Renovar inventario solo si es de tipo complemento
    def renovar_inventario(self) -> None:
        if self.tipo_ingrediente.upper() == Ingrediente_Enum.COMPLEMENTO.name:
            self.inventario = 0

#Tabla Producto con sus metodos    
class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio_publico = db.Column(db.Integer, nullable=False)
    tipo_producto = db.Column(db.String(50), nullable=False)
    volumen = db.Column(db.Float)
    tipo_vaso = db.Column(db.String(50))

    ingredientes = db.relationship('Ingrediente', secondary='productos_ingredientes')

    # Metodos implementados dependendiendo del tipo de producto se realiza una implementación diferente
    def calcular_costo(self, tipo_producto: str, lista_ingredientes: list[dict]) -> int:
        if self.tipo_producto.upper() == Producto_Enum.MALTEADA.name:
            return utils.funciones.producto_calcular_costo(lista_ingredientes) + 500
        else:
            return utils.funciones.producto_calcular_costo(lista_ingredientes)
        
    def calcular_rentabilidad(self, tipo_producto: str, precio: int, lista_ingredientes: list[dict]) -> float:
        if self.tipo_producto.upper() == Producto_Enum.MALTEADA.name:
            return utils.funciones.producto_calcular_rentabilidad(precio, lista_ingredientes)
        else:
            return utils.funciones.producto_calcular_rentabilidad(precio, lista_ingredientes)
        
    def calcular_calorias(self, tipo_producto: str, lista_calorias: list[int]) -> float:
        if self.tipo_producto.upper() == Producto_Enum.MALTEADA.name:
            return utils.funciones.producto_contar_calorias(lista_calorias, 1.0) + 200
        else:
            return utils.funciones.producto_contar_calorias(lista_calorias, 0.95)