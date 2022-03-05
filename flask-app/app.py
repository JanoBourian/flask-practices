from datetime import timedelta
from flask import Flask, jsonify
from flask_restful import Resource, Api
# from flask_jwt import JWT, JWTError
from flask_jwt_extended import JWTManager
# from security import authenticate, identity
from config.config import DevConfig
from resources.Item import Item
from resources.ItemList import ItemList
from resources.Store import Store
from resources.StoreList import StoreList
from resources.UserRegister import UserRegister
from resources.User import User
from resources.UserLogin import UserLogin
from constants import ROOT
from db import db

# Configurations
app = Flask(__name__)
app.config.from_object(DevConfig)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + ROOT + "\data\data.db"
app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=3600)
api = Api(app)

# Before first request
@app.before_first_request
def create_tables():
    db.create_all()


# jwt = JWT(app, authenticate, identity)  # /auth
jwt = JWTManager(app)
"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.
"""
@jwt.additional_claims_loader
def add_claims_to_jwt(identity):  # Remember identity is what we define when creating the access token
    if identity == 1:   # instead of hard-coding, we should read from a config file or database to get a list of admins instead
        return {'is_admin': True}
    return {'is_admin': False}

# @app.errorhandler(JWTError)
# def auth_error_handler(error):
#     return (
#         jsonify(
#             {
#                 "message": f"Could not authorize. Did you include a valid Authorization header? \n Error: {error}"
#             }
#         ),
#         400,
#     )


# View functions
class Index(Resource):
    def get(self):
        return jsonify({"message": "Hello world!"})


# Endpoints
api.add_resource(Index, "/")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")

# Functions
if __name__ == "__main__":
    db.init_app(app)
    app.run()
