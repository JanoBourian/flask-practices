from flask import Flask, render_template
import jinja2

app = Flask(__name__)

# Config our app 
app.config['TESTING'] = True
app.config.from_pyfile('settings.cfg')

# Routes 
@app.route("/", methods=['GET'])
def home():
    numero = 10
    return render_template('index.html', numero = numero, iterable = [5, 9, 7, 10])

@app.route("/saludo/<string:usuario>", methods=['GET'])
def saludo(usuario):
    template = jinja2.Template("Hola, {{usuario}}.")
    template.render(usuario = usuario)
    # return f"<h1> Hola {usuario} </h1>"

@app.route("/operacion/<int:a>_suma_<int:b>", methods=['GET'])
def suma(a, b):
    return f"<h1> SUMA: {a+b} </h1>"

if __name__ == '__main__':
    port = "8000"
    host = "192.168.0.20"
    debug = True
    app.run(host = host, debug = debug, port = port)