from flask import Flask, request
from flask import render_template
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from controllers.controller_ingrediente import ControllerIngrediente
from controllers.controller_producto import ControllerProducto
from controllers.controller_heladeria import Heladeria
from models.models_bd import Ingrediente
from heladeria import Heladeria
import utils
import os
import utils.variables_generales

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_SCHEMA")}'
db.init_app(app)
api = Api(app)

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
    #Hacer commit
    vendido=heladeria.vender(producto)
    if vendido: utils.variables_generales.set_variable_ventas_del_dia(1)
    session.commit()
    return render_template('vender.html', ventas=utils.variables_generales.get_variable_ventas_del_dia(), producto=producto, vendido=vendido)

#Abastecer un ingrediente
@app.route("/abastecer")
def abastecer():
    session = db.session
    ingredientes = Ingrediente.query.all()
    ingrediente = request.args.get('ingrediente')
    ingrediente_abastecer = ""
    for ing in ingredientes:
        if ing.nombre == ingrediente:
            ingrediente_abastecer = ing
            break
    ingrediente_abastecer.abastecer()
    session.commit()
    ingredientes = Ingrediente.query.all()
    return render_template('ingredientes.html', ingredientes=ingredientes, ventas=utils.variables_generales.get_variable_ventas_del_dia())

api.add_resource(ControllerIngrediente, '/ingredientes')
api.add_resource(ControllerProducto, '/productos')

if __name__ == '__main__':
    app.run(debug=True)