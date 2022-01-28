from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
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
                self.find_by_name(name) if self.find_by_name(name) else ITEM_NOT_EXIST
            )
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @jwt_required()
    def post(self, name):
        try:
            if self.find_by_name(name):
                return {"Error": "Item already exists"}, 400
            data = Item.parser.parse_args()
            price = data.get("price", "")
            response = self.add_to_database(name, price)
            logging.warning(f"response: {response}")
            return response if response else INTERNAL_SERVER_ERROR

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @jwt_required()
    def delete(self, name):
        try:
            if self.find_by_name(name):
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
            if not self.find_by_name(name):
                return ITEM_NOT_EXIST

            data = Item.parser.parse_args()
            price = data.get("price", "")
            response = self.add_to_database(name, price)
            return response if response else INTERNAL_SERVER_ERROR

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect(FILE)
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        return ({"item": {"name": row[1], "price": row[2]}}, 200) if row else None

    @classmethod
    def add_to_database(cls, name: str, price: float):
        try:
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
            response = None

            if cls.find_by_name(name):
                query = "UPDATE items SET price = ? WHERE name = ?"
                cursor.execute(query, (price, name))
                response = {"Message": f"Item {name} updated successfully"}, 201
            else:
                query = "INSERT INTO items VALUES(NULL, ?, ?)"
                cursor.execute(query, (name, price))
                response = {"Message": f"Item {name} inserted successfully"}, 201

            connection.commit()
            connection.close()
            return response
        except Exception as e:
            logging.warning("Error {e}")
            return INTERNAL_SERVER_ERROR
