from flask_restful import Resource, reqparse 
from flask_jwt import jwt_required 
from models.StoreModel import StoreModel
from constants import (INTERNAL_SERVER_ERROR, STORE_NOT_EXIST)
import logging

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'new_name',
        type = str,
        required = True,
        help = "If you want changes needs new_name field"
        )
    
    @jwt_required()
    def get(self, name): 
        try: 
            return (
                StoreModel.find_by_name(name) if StoreModel.find_by_name(name) else STORE_NOT_EXIST
            )
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
    
    @jwt_required()
    def post(self, name): 
        try: 
            if StoreModel.find_by_name(name):
                return {"Error": f"Store {name} already exists"}, 400
            store = StoreModel(name = name)
            response = store.add_to_database()
            return {"Message": f"Item {name} inserted successfully"}, 201 if response==201 else response
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
    
    @jwt_required()
    def delete(self, name): 
        try: 
            if StoreModel.find_by_name(name):
                return StoreModel.delete_to_database(name)
            return STORE_NOT_EXIST
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
        
    @jwt_required()
    def put(self, name): 
        try: 
            if not StoreModel.find_by_name(name):
                return STORE_NOT_EXIST
            data = Store.parser.parse_args()
            new_name = data['new_name']
            response = StoreModel.update_to_database(name = new_name)
            return {"Message": f"Store {name} updated successfully"}, 201 if response==201 else response
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR