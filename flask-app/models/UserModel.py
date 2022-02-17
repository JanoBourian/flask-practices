from db import db
import logging

class UserModel(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
       
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def add_to_database(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logging.warning(f"Error: {e}")
            return {"error": f"{e}"}, 500
        
    @classmethod
    def find_by_username(cls, username): 
        try:
            return cls.query.filter_by(username = username).first()
        except Exception as e:
            logging.warning(f"Error: {e}")
    
    @classmethod
    def find_by_id(cls, user_id):
        try:
            return cls.query.filter_by(id = user_id).first()
        except Exception as e:
            logging.warning(f"Error: {e}")
