from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from flask_jwt_extended import jwt_required
from models.ItemModel import ItemModel
from models.StoreModel import StoreModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("sku", type=str, required=True, help="sku field is necessary")
    parser.add_argument(
        "price", type=float, required=True, help="price field is necessary"
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="store_id field is necessary"
    )

    # get
    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
            if item:
                response = {
                    "sku": item.sku,
                    "price": item.price,
                    "store_id": item.store_id,
                }
                return response, 200
            return {"message": f"Item {name} not exists"}, 200
        except Exception as e:
            return {"error": e}, 500

    # post
    @jwt_required()
    def post(self, name):
        data = Item.parser.parse_args()
        try:
            item = ItemModel.find_by_name(name)
            if item:
                return {"message": f"Item {name} already exists"}, 404
            if ItemModel.find_by_sku(data["sku"]):
                return {"message": f"Sku {data['sku']} already exists"}, 404
            item = ItemModel(
                sku=data["sku"],
                name=name,
                price=data["price"],
                store_id=data["store_id"],
            )
            if StoreModel.find_by_id(data["store_id"]):
                item.add_to_database()
                return {"message": f"Item {name} added."}
            return {"message": f"store_id {data['store_id']} no exists"}, 404
        except Exception as e:
            return {"error": e}, 500

    # put
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        try:
            item = ItemModel.find_by_name(name)
            if not item:
                return {"message": f"Item {name} not exists"}, 404
            ItemModel.update_to_database(name, **data)
            return {"Message": f"Item {name} was updated"}
        except Exception as e:
            return {"error": e}, 500

    # delete
    @jwt_required()
    def delete(self, name):
        try:
            item = ItemModel.find_by_name(name)
            if not item:
                return {"message": f"Item {name} not exists"}, 404
            ItemModel.delete_to_database(name)
            return {"Message": f"Item {name} was deleted"}, 201
        except Exception as e:
            return {"error": e}, 500
