from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from constants import (FILE, INTERNAL_SERVER_ERROR, )
from models.ItemModel import ItemModel
import logging

class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            return ItemModel.return_all_items()
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
