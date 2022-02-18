from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from forms.Moviment import MovimentClass
from models.MovimentModel import MovimentModel
from constants import ROOT
from db import db
import logging

app = Flask(__name__)

app.config.from_object('config.config.DevConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + ROOT +'\data\data.db'
app.config['SQLALchemy_TRACK_MODIFICATIONS'] = False 

@app.before_first_request
def create_tables():
    db.create_all()
    
@app.route("/", methods=["GET", "POST"])
def index(): 
    forma = MovimentClass()
    if forma.validate_on_submit():
        print(f"forma: {forma.cantidad.data}")
        print(f"forma: {forma.tipo.data}")
        print(f"forma: {forma.concepto.data}")
        print(f"forma: {forma.fecha.data}")
        moviment = MovimentModel(forma.cantidad.data, forma.tipo.data, forma.concepto.data, forma.fecha.data)
        print(moviment)
        moviment.add_to_database()
        flash('Datos ingresados correctamente')
        return redirect(url_for('index'))
    else:
        print('Datos incorrectos.')
    return render_template("index.html", form = forma)

@app.route("/ingresos")
def ingresos():
    items = MovimentModel.get_all_elements()
    response = []
    for item in items: 
        if item.tipo == 'Ingreso':
            data = {
            'id': item.id,
            'tipo': item.tipo,
            'cantidad': item.cantidad,
            'concepto': item.concepto,
            'fecha': item.fecha
            }
            response.append(data)
    return render_template("ingresos.html", data = reversed(response))

@app.route("/egresos")
def egresos(): 
    items = MovimentModel.get_all_elements()
    response = []
    for item in items: 
        if item.tipo == 'Egreso':
            data = {
            'id': item.id,
            'tipo': item.tipo,
            'cantidad': item.cantidad,
            'concepto': item.concepto,
            'fecha': item.fecha
            }
            response.append(data)
    return render_template("egresos.html", data = reversed(response))

@app.route("/reporte")
def reporte(): 
    items = MovimentModel.get_all_elements()
    print(f'items: {items}') 
    response = []
    for item in items: 
        data = {
            'id': item.id,
            'tipo': item.tipo,
            'cantidad': item.cantidad,
            'concepto': item.concepto,
            'fecha': item.fecha
        }
        response.append(data)
    return render_template("reporte.html", data = reversed(response))

@app.route("/documentos")
def documentos(): 
    return render_template("documentos.html")

if __name__ == "__main__":
    db.init_app(app)
    app.run()