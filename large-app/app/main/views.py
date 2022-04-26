from flask import request, render_template
from . import main 

assigments_values = [
    {
        "id": 1,
        "deadline": "27/04/22",
        "time": 120,
        "student": "Lorem",
        "description": "Lorem",
        "works": "Lorem",
        "active": True,
        "paid": True,
        "done": False
    },
    {
        "id": 2,
        "deadline": "27/04/22",
        "time": 120,
        "student": "Lorem",
        "description": "Lorem",
        "works": "Lorem",
        "active": True,
        "paid": True,
        "done": True
    }
    ]
schedules_values = []
followed_values = []
students_values = []
information_values = []

@main.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@main.route("/user/<string:name>")
def user(name:str):
    print(request.args)
    return render_template("user.html", name=name)

@main.route("/assigments", methods=['GET'])
def assigments():
    print(request.args)
    print(assigments)
    return render_template("assigments.html", assigments_values = assigments_values)

@main.route("/schedules", methods=['GET'])
def schedules():
    print(request.args)
    return render_template("schedules.html")

@main.route("/followed", methods=['GET'])
def followed():
    print(request.args)
    return render_template("followed.html")

@main.route("/students", methods=['GET'])
def students():
    print(request.args)
    return render_template("students.html")

@main.route("/information", methods=['GET'])
def information():
    print(request.args)
    return render_template("information.html")