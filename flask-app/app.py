from datetime import timedelta
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
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
from resources.TokenRefresh import TokenRefresh
from resources.UserLogout import UserLogout
from blacklist import BLACKLIST
from constants import ROOT
from db import db

# Configurations
app = Flask(__name__)
app.config.from_object(DevConfig)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + ROOT + "\data\data.db"
app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['JWT_AUTH_URL_RULE'] = '/login'
# app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=3600)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=3600)
# cors = CORS(app)
CORS(app, resources={f"/*":{"origins":"http://192.168.0.20:8080/"}})
# app.config['CORS_HEADERS'] = 'Content-Type'
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

# The following callbacks are used for customizing jwt response/error messages.
# The original ones may not be in a very pretty format (opinionated)
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'description': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(jwt_header, jwt_payload):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'description': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'description': 'The token has been revoked.',
        'error': 'token_revoked'
    }), 401


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    app.logger.info("hello ")
    app.logger.info(jwt_payload)
    id_iam_looking_for = jwt_payload['jti']
    return id_iam_looking_for in BLACKLIST

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
        return make_response({"message": "Hello world!"}, 200)


# Endpoints
api.add_resource(Index, "/")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
# api.add_resource(UserLogout, "/logout")

# Functions
if __name__ == "__main__":
    db.init_app(app)
    app.run()
