from constants import (INTERNAL_SERVER_ERROR,)
from models.ItemModel import ItemModel
from db import db 
import logging 

class StoreModel(db.Model): 
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    
    items = db.relationship("ItemModel", lazy= 'dynamic')
    
    def __init__(self, name):
        self.name = name
       
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
                items = ItemModel.return_items_for_store(row.id)
                print(items)
                data = {"store": row.name, "information": items[0]}
                return ({"item": data}, 200) 
            return None
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR
        
    @classmethod
    def update_to_database(cls, name):
        try:
            row = cls.query.filter_by(name=name).first()
            row.name=name 
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
        return {"message": f"Store {name} removed"}, 201
    
    @classmethod
    def return_all_items(cls):
        try:
            items = []
            row = cls.query.all()
            if row:
                for r in row:
                    items.append({"name": r.name})
            return {"Stores": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR