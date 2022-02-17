from flask_restful import Resource, reqparse


class StoreList(Resource):
    def get(self):
        try:
            return {"stores": []}, 200
        except Exception as e:
            return {"error": e}, 500
