from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from constants import (INTERNAL_SERVER_ERROR, )
from models.StoreModel import StoreModel
import logging

class StoreList(Resource):
    @jwt_required()
    def get(self):
        try:
            return StoreModel.return_all_items()
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
