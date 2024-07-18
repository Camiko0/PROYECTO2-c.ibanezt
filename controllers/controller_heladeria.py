from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from models.models_bd import Ingrediente
from heladeria import Heladeria
from db import db
import utils.formatearHtml
import utils.variables_generales
from app import app

def vender():
    heladeria = Heladeria()
    producto = request.args.get('producto')
    utils.variables_generales.set_variable_ventas_del_dia(1)
    return render_template('vender.html', ventas=utils.variables_generales.get_variable_ventas_del_dia(), producto=producto, vendido=heladeria.vender(producto))