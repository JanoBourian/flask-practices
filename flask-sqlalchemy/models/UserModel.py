from constants import (FILE,)
from db import db
import sqlite3
import logging

class UserModel(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def add_to_database(self):
        try: 
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logging.error(f"Error {e}")            

    @classmethod
    def find_by_username(cls, username):
        try:
            return cls.query.filter_by(username = username).first()
        except Exception as e:
            logging.error(f"Error {e}")

    @classmethod
    def find_by_id(cls, _id):
        try:
            return cls.query.filter_by(id = _id).first()
        except Exception as e:
            logging.error(f"Error {e}")