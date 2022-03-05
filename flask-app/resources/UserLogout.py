from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from blacklist import BLACKLIST

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        print(f'jti: {jti}') 
        jti = get_jwt()
        print(f'jti: {jti}') 
        input('Press any key to cotinue...')
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}, 201