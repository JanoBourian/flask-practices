from constants import (FILE, INTERNAL_SERVER_ERROR)
from db import db
import sqlite3
import logging 

class ItemModel(db.Model): 
    
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def add_to_database(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 201
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR
    
    @classmethod
    def find_by_name(cls, name):
        try: 
            row =  cls.query.filter_by(name = name).first()
            if row:
                data = {"name": row.name, "price": row.price}
                return ({"item": data}, 200) 
            return None
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR
        
    @classmethod
    def update_to_database(cls, name, price):
        try:
            row = cls.query.filter_by(name=name).first()
            row.price=price 
            db.session.commit()
            return 201
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR
    
    @classmethod
    def delete_to_database(cls, name:str):
        row = cls.query.filter_by(name=name).first()
        db.session.delete(row)
        db.session.commit()
        return {"message": f"Item {name} removed"}, 201
    
    @classmethod
    def return_all_items(cls):
        try:
            items = []
            row = cls.query.all()
            if row:
                for r in row:
                    items.append({"name": r.name, "price": r.price})
            return {"items": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR