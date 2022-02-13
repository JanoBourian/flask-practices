import json
from flask import Flask, jsonify, render_template 
from functions.busqueda import (buscar_archivo,)

app = Flask(__name__)
# app.config.from_pyfile('configurations/config.py')
app.config.from_object('configurations.config.DevConfig')

ruta = 'data/alumnos.txt'
campos = ['nombre', 'primer_apellido', 'segundo_apellido']

@app.route('/api/<string:termino>')
def busqueda(termino):
    return jsonify(buscar_archivo(str(termino), ruta, campos))

@app.route('/despliega/<string:termino>')
def despliega(termino):
    return render_template('busqueda.html', alumnos = buscar_archivo(str(termino), ruta, campos))

if __name__ == '__main__':
    app.run()