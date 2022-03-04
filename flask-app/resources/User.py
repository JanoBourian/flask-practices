from flask_restful import Resource
from models.UserModel import UserModel

class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user: 
            return {"message": "User not found"}, 404
        response = {
            "id": user.id,
            "username": user.username
        }
        return response, 200
    
    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user: 
            return {"message": "User not found"}, 404
        UserModel.delete_to_database(user.username)
        response = {
            "mesagge": f"User {user.username} was deleted"
        }
        return response, 201