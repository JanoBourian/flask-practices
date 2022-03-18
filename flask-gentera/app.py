from flask import Flask, jsonify, make_response, render_template
from config.config import DevConfig
from flask_restful import Resource, Api
# resources
from resources.Dispositivo import Dispositivo
from resources.TipoDispositivo import TipoDispositivo
from resources.StatusDispositivo import StatusDispositivo
from db import db
from os import path

ROOT = path.abspath(path.dirname(__file__))

# Configuration
app = Flask(__name__)
app.config.from_object(DevConfig)

# sqlalchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + ROOT + "\data\data.db"
app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

# Before first request
@app.before_first_request
def create_tables():
    db.create_all()

## View functions
class Index(Resource):
    def get(self):
        return make_response(jsonify({"Message": "Welcome!"}), 200)

## Resources 
api.add_resource(Index, "/")
api.add_resource(Dispositivo, "/dispositivo")
api.add_resource(TipoDispositivo, "/tipo")
api.add_resource(StatusDispositivo, "/status")

if __name__ == '__main__':
    db.init_app(app)
    app.run()