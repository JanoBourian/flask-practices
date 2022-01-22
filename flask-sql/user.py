import sqlite3 
import os 
import logging

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "data.db"
FILE = PATH + "\\" + DATABASE
print(FILE)

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
        
        
        
        
