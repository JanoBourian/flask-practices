from flask_restful import Resource, reqparse
from resources.User import User
from utilities.constants import (FILE, INTERNAL_SERVER_ERROR)
import sqlite3
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
            if User.find_by_username(data["username"]):
                return {"message": f"{data['username']} already registered!"}, 409

            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()

            query = "INSERT INTO users VALUES(NULL, ?, ?)"
            cursor.execute(
                query,
                (
                    data["username"],
                    data["password"],
                ),
            )

            connection.commit()
            connection.close()

            return {"message": f"User {data['username']} created successfully"}, 201
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500
