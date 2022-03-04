from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from models.UserModel import UserModel 

class UserLogin(Resource):
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
    
    @classmethod
    def post(cls):
        # get data from parser 
        data = cls.parser.parse_args()
        
        # find user in db
        user = UserModel.find_by_username(data['username'])
        
        # check password
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity = user.id, fresh= True)
            refresh_token = create_refresh_token(user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
        
        return {"message": "Invalid credentials"}, 401       
            
        # create access token
        # create refresh token (we will look at this later)
        