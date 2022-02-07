from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ItemModel import ItemModel
from constants import (INTERNAL_SERVER_ERROR, ITEM_NOT_EXIST)
import logging

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be left blank!",
    )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="All item nees a store_id",
    )

    @jwt_required()
    def get(self, name):
        try:
            return (
                ItemModel.find_by_name(name) if ItemModel.find_by_name(name) else ITEM_NOT_EXIST
            )
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @jwt_required()
    def post(self, name):
        try:
            if ItemModel.find_by_name(name):
                return {"Error": f"Item {name} already exists"}, 400
            data = Item.parser.parse_args()
            price = data.get("price", "")
            store_id = data.get("store_id", "")
            item = ItemModel(name=name, price=price, store_id=store_id)
            response = item.add_to_database()
            return {"Message": f"Item {name} inserted successfully"}, 201 if response==201 else response
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @jwt_required()
    def delete(self, name):
        try:
            if ItemModel.find_by_name(name):
                return ItemModel.delete_to_database(name)
            return ITEM_NOT_EXIST

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @jwt_required()
    def put(self, name):
        try:
            if not ItemModel.find_by_name(name):
                return ITEM_NOT_EXIST
            data = Item.parser.parse_args()
            price = data.get("price", "")
            store_id = data.get("store_id", "")
            response = ItemModel.update_to_database(name=name, price=price, store_id=store_id)
            return {"Message": f"Item {name} updated successfully"}, 201 if response==201 else response
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

