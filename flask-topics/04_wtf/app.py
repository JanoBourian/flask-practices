from flask import Flask, render_template 

app = Flask(__name__)

app.config.from_object('config.config.DevConfig')

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/ingresos")
def ingresos(): 
    return render_template("ingresos.html")

@app.route("/egresos")
def egresos(): 
    return render_template("egresos.html")

@app.route("/general")
def general(): 
    return render_template("general.html")

if __name__ == "__main__":
    app.run()