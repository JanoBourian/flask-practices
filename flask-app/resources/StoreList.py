from flask_restful import Resource
from models.StoreModel import StoreModel


class StoreList(Resource):
    def get(self):
        try:
            stores = StoreModel.get_all_elements()
            res = []
            for store in stores:
                data = {"name": store.name, "description": store.description}
                res.append(data)
            return {"stores": res}, 200
        except Exception as e:
            return {"error": e}, 500
