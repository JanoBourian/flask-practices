from flask_restful import Resource, reqparse
import sqlite3 
import os 
import logging

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "data.db"
FILE = PATH + "\\" + DATABASE
print(FILE)
INTERNAL_SERVER_ERROR = {"Error": "Internal Server Error"}

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod    
    def find_by_username(cls, username):
        try:
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
        
            query = "SELECT * FROM users WHERE username = ?"
            result = cursor.execute(query, (username,))
            row = result.fetchone()
        
            # user = cls(result[0], result[1], result[2], result[3]) if result else None
            user = cls(*row) if row else None
        
            connection.close()
            return user 
        except Exception as e:
            logging.error(f"Error {e}")
    
    @classmethod
    def find_by_id(cls, _id):
        try:
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
        
            query = "SELECT * FROM users WHERE id = ?"
            result = cursor.execute(query, (_id,))
            row = result.fetchone()
        
            # user = cls(result[0], result[1], result[2], result[3]) if result else None
            user = cls(*row) if row else None
        
            connection.close()
            return user
        except Exception as e:
            logging.error(f"Error {e}")
        
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", 
        type = str, 
        required = True, 
        help = "Username to register cannotn be left blank!"
        )
    parser.add_argument(
        "password", 
        type = str, 
        required = True, 
        help = "Password to register cannotn be left blank!"
        )
    
    def post(self):
        try: 
            data = UserRegister.parser.parse_args()
            if User.find_by_username(data['username']):
                return {"message": f"{data['username']} already registered!"}, 409
            
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
            
            query = "INSERT INTO users VALUES(NULL, ?, ?)"
            cursor.execute(query, (data['username'], data['password'],))
            
            connection.commit()
            connection.close()
            
            return {"message": f"User {data['username']} created successfully"}, 201
        except Exception as e: 
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR, 500
        
        
