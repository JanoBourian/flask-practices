from constants import (FILE,)
from db import db
import sqlite3
import logging

class UserModel(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(80))
    
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

            user = cls(*row) if row else None

            connection.close()
            return user
        except Exception as e:
            logging.error(f"Error {e}")