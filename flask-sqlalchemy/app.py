from datetime import (timedelta,)
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from Item import (
    Item,
    ItemList,
)

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

jwt = JWT(app, authenticate, identity)  # /auth


class Student(Resource):
    def get(self, name):
        return {"student": name}


# http://127.0.0.1:5000/student/Rolf
api.add_resource(Student, "/student/<string:name>")

# http://192.168.0.20:8080/item/<string:name>
api.add_resource(Item, "/item/<string:name>")

# http://192.168.0.20:8080/items
api.add_resource(ItemList, "/items")

# http://192.168.0.20:8080/register
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    host = "192.168.0.20"
    port = "8080"
    debug = True
    app.run(host=host, port=port, debug=debug)
