from flask import render_template
from flask_restful import Resource
from models.models_bd import Producto
import utils

class ControllerProducto(Resource):
    def get(self):
        productos = Producto.query.all()
        #Obtener el listado de productos con sus datos (Se llama método calcular_calorias() que llama a funciones.producto_contar_calorias)
        for producto in productos:
            lista_ingredientes_calorias = []
            for ingrediente in producto.ingredientes:
                lista_ingredientes_calorias.append(ingrediente.calorias)
                producto.calorias= producto.calcular_calorias(producto.tipo_producto, lista_ingredientes_calorias)

        html_content = render_template('productos.html', productos=productos, ventas=utils.variables_generales.get_variable_ventas_del_dia())
        return utils.formatearHtml.convertirStringToHtml(html_content)