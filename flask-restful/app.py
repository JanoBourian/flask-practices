from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
import logging

INTERNAL_SERVER_ERROR = {"Error": "Internal Server Error"}

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth
items = []


class Student(Resource):
    def get(self, name):
        return {"student": name}


# http://127.0.0.1:5000/student/Rolf
api.add_resource(Student, "/student/<string:name>")


class Item(Resource):
    @jwt_required()
    def get(self, name):
        try:
            for item in items:
                if item["name"] == name:
                    return item, 200
            return {"message": "Item not found"}, 404
            # item = list(filter(lambda x: x['name'] == name, items))
            # item = next(filter(lambda x: x['name'] == name, items))
            # return (item, 200) if item else ({"message": "Item not found"}, 404)
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500

    @jwt_required()
    def post(self, name):
        try:
            data = request.get_json()
            price = data.get("price", "")

            if not price:
                return {"message": "Incorrect Payload"}, 400

            for item in items:
                if item["name"] == name:
                    return {"message": "Item already exists"}, 409
            item = {"name": name, "price": price}
            items.append(item)
            return item, 201

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500

    @jwt_required()
    def delete(self, name):
        try:
            for item in items:
                if item["name"] == name:
                    position = items.index(item)
                    del items[position]
                    return {"message": f"Item {name} removed"}, 201
            return {"message": "Item not exists"}, 409

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500

    @jwt_required()
    def put(self, name):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "price",
                type=float,
                required=True,
                help="This field cannot be left blank!",
            )
            # data = request.get_json()
            data = parser.parse_args()
            new_price = data.get("price", "")
            if new_price:
                for item in items:
                    if item["name"] == name:
                        item["price"] = new_price
                        return {"message": f"Item {name} - {new_price} changed"}, 201
            return {"message": "Item not exists"}, 409

        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500


# http://192.168.0.20:8080/item/<string:name>
api.add_resource(Item, "/item/<string:name>")


class ItemList(Resource):
    @jwt_required()
    def get(self):
        try:
            return {"items": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500


# http://192.168.0.20:8080/items
api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    host = "192.168.0.20"
    port = "8080"
    debug = True
    app.run(host=host, port=port, debug=debug)
