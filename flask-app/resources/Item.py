from flask_restful import Resource, reqparse


class Item(Resource):
    def get(self, name):
        try:
            return {"name": name}, 200
        except Exception as e:
            return {"error": e}, 500
