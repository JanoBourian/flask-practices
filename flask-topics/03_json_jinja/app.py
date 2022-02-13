import json
from flask import Flask, jsonify, render_template, abort, url_for, redirect
from functions.busqueda import (buscar_archivo,)

app = Flask(__name__)
# app.config.from_pyfile('configurations/config.py')
app.config.from_object('configurations.config.DevConfig')

ruta = 'data/alumnos.txt'
campos = ['nombre', 'primer_apellido', 'segundo_apellido']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<string:termino>')
def busqueda(termino):
    abort(404, "Message")
    # return jsonify(buscar_archivo(str(termino), ruta, campos))
    # return redirect("/")
    # return redirect(url_for("index"))

@app.route('/despliega/<string:termino>')
def despliega(termino):
    return render_template('busqueda.html', alumnos = buscar_archivo(str(termino), ruta, campos))

@app.errorhandler(404)
def no_encontrado(error):
    return render_template('404.html', error=error)

if __name__ == '__main__':
    app.run()