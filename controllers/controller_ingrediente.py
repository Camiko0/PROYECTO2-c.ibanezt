from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from models.models_bd import Ingrediente
from db import db
import utils.formatearHtml
import utils.variables_generales

class ControllerIngrediente(Resource):
    def get(self):
        ingredientes = Ingrediente.query.all()
        html_content = render_template('ingredientes.html', ingredientes=ingredientes, ventas=utils.variables_generales.get_variable_ventas_del_dia())
        return utils.formatearHtml.convertirStringToHtml(html_content)