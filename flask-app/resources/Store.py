from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from flask_jwt_extended import jwt_required
from models.StoreModel import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "description", type=str, required=True, help="description fiels is required"
    )

    # get
    @jwt_required()
    def get(self, name):
        try:
            store = StoreModel.find_by_name(name=name)
            if store:
                result = {"name": store.name, "description": store.description}
                return {"response": result}, 200
            return {"Error": f"Store {name} not exists"}, 404
        except Exception as e:
            return {"error": e}, 500

    # post
    @jwt_required()
    def post(self, name):
        data = Store.parser.parse_args()
        try:
            store = StoreModel.find_by_name(name=name)
            if store:
                return {"Error": f"Store {name} already exists"}, 404
            store = StoreModel(name=name, description=data["description"])
            store.add_to_database()
            return {"message": f"Store {name} added to database"}, 201
        except Exception as e:
            return {"error": f"{e}"}, 500

    # put
    @jwt_required()
    def put(self, name):
        data = Store.parser.parse_args()
        try:
            store = StoreModel.find_by_name(name=name)
            if not store:
                return {"Error": f"Store {name} not exists"}, 404
            StoreModel.update_to_database(name, data["description"])
            return {"message": f"Store {name} updated to database"}, 201
        except Exception as e:
            return {"error": f"{e}"}, 500

    # delete
    @jwt_required()
    def delete(self, name):
        try:
            if not StoreModel.find_by_name(name=name):
                return {"Error": f"Store {name} not exists"}, 404
            StoreModel.delete_to_database(name)
            return {"Message": f"Store {name} was deleted"}, 201
        except Exception as e:
            return {"error": f"{e}"}, 500
