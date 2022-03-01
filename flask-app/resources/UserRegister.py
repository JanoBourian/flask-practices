from flask_restful import Resource, reqparse
from models.UserModel import UserModel
import logging


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="Username to register can not be left blank!",
    )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="Password to register can not be left blank!",
    )

    def post(self):
        try:
            data = UserRegister.parser.parse_args()
            username = data["username"]
            if UserModel.find_by_username(username):
                return {"error": f"{username} already exists"}, 404
            user = UserModel(**data)
            user.add_to_database()
            return {"message": f"{username} added to database"}, 201
        except Exception as e:
            logging.warning(f"Error: {e}")
            return {"error": f"{e}"}, 500
