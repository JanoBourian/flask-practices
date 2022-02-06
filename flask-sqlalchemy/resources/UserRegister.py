from flask_restful import Resource, reqparse
from models.UserModel import UserModel
from constants import (FILE, INTERNAL_SERVER_ERROR)
import logging

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="Username to register cannotn be left blank!",
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="Password to register cannotn be left blank!",
    )

    def post(self):
        try:
            data = UserRegister.parser.parse_args()
            if UserModel.find_by_username(data["username"]):
                return {"message": f"{data['username']} already registered!"}, 409
            user = UserModel(**data)
            user.add_to_database()
            return {"message": f"User {data['username']} created successfully"}, 201
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500
