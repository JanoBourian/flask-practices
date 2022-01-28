from datetime import (timedelta,)
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.UserRegister import UserRegister
from resources.Item import Item 
from resources.ItemList import ItemList
from create_tables import create_tables

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

jwt = JWT(app, authenticate, identity)  # /auth


class Student(Resource):
    def get(self, name):
        return {"student": name}


api.add_resource(Student, "/student/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    create_tables()
    host = "192.168.0.20"
    port = "8080"
    debug = True
    app.run(host=host, port=port, debug=debug)
