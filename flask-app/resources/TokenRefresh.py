from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt, create_access_token

class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt()
        new_token = create_access_token(identity = current_user, fresh = False)
        return {'access_token': new_token}, 200