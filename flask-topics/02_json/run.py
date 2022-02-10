from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({'Nombre': 'Juan', 
        'Primer Apellido': 'Pérez', 
        'Segundo Apellido': None})

#Si no se define el parámetro host, flask sólo será visible desde localhost
# app.run(host='localhost')
app.run(host='0.0.0.0')