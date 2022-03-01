from flask_restful import Resource
from models.ItemModel import ItemModel
from flask_jwt import jwt_required


class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            rows = ItemModel.get_all_elements()
            response = []
            for row in rows:
                data = {
                    "sku": row.sku,
                    "name": row.name,
                    "price": row.price,
                    "store_id": row.store_id,
                }
                response.append(data)
            return {"Items": response}, 200
        except Exception as e:
            return {"error": e}, 500
