from flask import Flask 

app = Flask(__name__)

# Config our app 
app.config['TESTING'] = True
app.config.from_pyfile('settings.cfg')

# Routes 
@app.route("/", methods=['GET'])
def home():
    return """
<h1> Hello world </h1>
"""

@app.route("/saludo/<string:usuario>", methods=['GET'])
def saludo(usuario):
    return f"<h1> Hola {usuario} </h1>"

if __name__ == '__main__':
    port = "8000"
    host = "192.168.0.20"
    debug = True
    app.run(host = host, debug = debug, port = port)