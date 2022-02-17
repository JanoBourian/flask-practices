from flask_restful import Resource, reqparse


class ItemList(Resource):
    def get(self):
        try:
            return {"items": []}, 200
        except Exception as e:
            return {"error": e}, 500
