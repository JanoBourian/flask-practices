from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from utilities.constants import (FILE, INTERNAL_SERVER_ERROR, )
import sqlite3
import logging

class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
            query = "SELECT * FROM items"
            result = cursor.execute(query)
            row = result.fetchall()
            connection.close()
            items = []
            if row:
                for r in row:
                    items.append({"name": r[1], "price": r[2]})
            return {"items": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
