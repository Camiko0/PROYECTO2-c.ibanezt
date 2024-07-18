from flask import Flask, request, render_template
from flask_restful import Api
from controllers.controller_ingrediente import ControllerIngrediente
from controllers.controller_producto import ControllerProducto
from models.models_bd import Ingrediente
from heladeria import Heladeria
import utils.variables_generales
import utils
import os
from dotenv import load_dotenv
from db import db

#Cargar variables de entorno
load_dotenv()

#Cargar configuración de la base de datos
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_SCHEMA")}'
db.init_app(app)
api = Api(app)

#Pantalla de inicio
@app.route("/")
def main():
    return render_template('index.html', ventas=utils.variables_generales.get_variable_ventas_del_dia())

#Reiniciar las ventas de la heladeria
@app.route("/reiniciar-ventas")
def ventas():
    utils.variables_generales.reset_ventas_del_dia()
    return render_template('index.html', ventas=utils.variables_generales.get_variable_ventas_del_dia())

#Vender producto
@app.route("/heladeria/vender")
def vender():
    session = db.session
    producto = request.args.get('producto')
    heladeria = Heladeria()
    try:
        vendido=heladeria.vender(producto)
        if vendido: utils.variables_generales.set_variable_ventas_del_dia(1)
        #Hacer commit
        session.commit()
        #Enviar a pantalla de venta
        return render_template('vender.html', ventas=utils.variables_generales.get_variable_ventas_del_dia(), producto=producto, vendido=vendido)
    except ValueError as e:
        return render_template('vender.html', ventas=utils.variables_generales.get_variable_ventas_del_dia(), producto=producto, vendido=False, response=e)

#Abastecer un ingrediente o renovar un ingrediente
@app.route("/abastecer")
def abastecer():
    session = db.session
    ingredientes = Ingrediente.query.all()
    ingrediente = request.args.get('ingrediente')
    renovar = request.args.get('renovar')
    ingrediente_abastecer = ""
    #Buscar ingrediente a modificar inventario
    for ing in ingredientes:
        if ing.nombre == ingrediente:
            ingrediente_abastecer = ing
            break
    #Si tiene el parametro renovar (renovar inventario) sino abastecer
    if renovar:
        ingrediente_abastecer.renovar_inventario()
    else:
        ingrediente_abastecer.abastecer()
    #Hacer commit
    session.commit()
    ingredientes = Ingrediente.query.all()
    #Enviar a pantalla de ingredientes
    return render_template('ingredientes.html', ingredientes=ingredientes, ventas=utils.variables_generales.get_variable_ventas_del_dia(), 
                           renovar=True, ingrediente_abastecer=ingrediente)

#Calcular el producto más rentable
@app.route("/producto-mas-rentable")
def producto_mas_rentable():
    heladeria = Heladeria()
    producto = heladeria.calcular_producto_mas_rentable()

    return render_template('index.html', ventas=utils.variables_generales.get_variable_ventas_del_dia(), producto=producto)

#Agregar controladores para ingrediente y producto
api.add_resource(ControllerIngrediente, '/ingredientes')
api.add_resource(ControllerProducto, '/productos')

if __name__ == '__main__':
    app.run(debug=True)