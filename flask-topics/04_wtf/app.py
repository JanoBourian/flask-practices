from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from forms.Moviment import MovimentClass
import logging

app = Flask(__name__)

app.config.from_object('config.config.DevConfig')

@app.route("/", methods=["GET", "POST"])
def index(): 
    forma = MovimentClass()
    if forma.validate_on_submit():
        print(f"{forma['tipo'].data} - {forma['cantidad'].data}")
        flash('Datos ingresados correctamente')
        return redirect(url_for('index'))
    else:
        print('Datos incorrectos.')
    return render_template("index.html", form = forma)

@app.route("/ingresos")
def ingresos(): 
    return render_template("ingresos.html")

@app.route("/egresos")
def egresos(): 
    return render_template("egresos.html")

@app.route("/reporte")
def reporte(): 
    return render_template("reporte.html")

@app.route("/documentos")
def documentos(): 
    return render_template("documentos.html")

if __name__ == "__main__":
    app.run()