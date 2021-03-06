from datetime import (timedelta,)
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.UserRegister import UserRegister
from resources.Item import Item 
from resources.ItemList import ItemList
from resources.Store import Store
from resources.StoreList import StoreList
from create_tables import create_tables
from constants import (FILE,)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + FILE
app.config['SQLALchemy_TRACK_MODIFICATIONS'] = False 
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)
app.secret_key = "jose"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth


class Student(Resource):
    def get(self, name):
        return {"student": name}


api.add_resource(Student, "/student/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    # create_tables()
    from db import db
    db.init_app(app)
    host = "192.168.0.20"
    port = "8080"
    debug = True
    app.run(host=host, port=port, debug=debug)
