from flask import Flask 

app = Flask(__name__)
# app.config.from_pyfile('configurations/config.py')
app.config.from_object('configurations.config.DevConfig')

@app.route('/api/<string:cadena>')
def busqueda(cadena):
    return f"<h1> {cadena} </h1>"

@app.route('/despliega/<string:cadena>')
def despliega(cadena):
    return f"<h1> {cadena} </h1>"

if __name__ == '__main__':
    app.run()