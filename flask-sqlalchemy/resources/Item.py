from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ItemModel import ItemModel
from utilities.constants import (FILE, INTERNAL_SERVER_ERROR, ITEM_NOT_EXIST)
import sqlite3
import logging

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be left blank!",
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
                return {"Error": "Item already exists"}, 400
            data = Item.parser.parse_args()
            price = data.get("price", "")
            response = ItemModel.add_to_database(name, price)
            logging.warning(f"response: {response}")
            return response if response else INTERNAL_SERVER_ERROR

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @jwt_required()
    def delete(self, name):
        try:
            if ItemModel.find_by_name(name):
                connection = sqlite3.connect(FILE)
                cursor = connection.cursor()
                query = "DELETE FROM items WHERE name = ?"
                cursor.execute(query, (name,))
                connection.commit()
                connection.close()
                return {"message": f"Item {name} removed"}, 201
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
            response = ItemModel.add_to_database(name, price)
            return response if response else INTERNAL_SERVER_ERROR

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

