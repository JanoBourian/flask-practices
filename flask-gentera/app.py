from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

## View functions
class Index(Resource):
    def get(self):
        return make_response(jsonify({"Message": "Welcome!"}), 200)

## Resources 
api.add_resource(Index, "/")

if __name__ == '__main__':
    app.run()