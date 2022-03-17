from flask import Flask, jsonify, make_response, render_template
from flask_restful import Resource, Api
# resources
from resources.Dispositivo import Dispositivo
from resources.TipoDispositivo import TipoDispositivo
from resources.StatusDispositivo import StatusDispositivo

# Configuration
app = Flask(__name__)
api = Api(app)

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
    app.run()