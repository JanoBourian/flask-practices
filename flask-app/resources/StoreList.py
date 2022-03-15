from flask_restful import Resource
from flask_cors import cross_origin
from flask import jsonify, make_response
from models.StoreModel import StoreModel
from flask_jwt_extended import jwt_required, get_jwt_identity
import json 

class StoreList(Resource):
    # @jwt_required(optional=True)
    def get(self):
        try:
            # user_id = get_jwt_identity()
            stores = StoreModel.get_all_elements()
            res = []
            for store in stores:
                data = {"name": store.name, "description": store.description}
                res.append(data)
            if True:
                print({"stores": res})
                # return make_response(jsonify({"stores": res}), 200)
                # return jsonify([{"stores": res}]), 200
                var = make_response({"stores": res}, 200)
                print(type(var))
                # return make_response(jsonify({"stores": res}), 200)
                return make_response(jsonify({"stores": res}), 200)
            return {"Message": "For more information user register is necessary"}, 401
        except Exception as e:
            return {"error": e}, 500
