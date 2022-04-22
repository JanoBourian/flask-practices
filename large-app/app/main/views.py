from flask import request, render_template
from . import main 

@main.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@main.route("/user/<string:name>")
def user(name:str):
    print(request.args)
    return f"<h1> Hello {name}</h1>"