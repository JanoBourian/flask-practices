from constants import (INTERNAL_SERVER_ERROR,)
from db import db
import logging 

class ItemModel(db.Model): 
    
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
       
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
                data = {"name": row.name, "price": row.price, "store_id": row.store_id}
                return ({"item": data}, 200) 
            return None
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR
        
    @classmethod
    def update_to_database(cls, name, price, store_id):
        try:
            row = cls.query.filter_by(name=name).first()
            row.price=price 
            row.store_id = store_id
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
                    items.append({"name": r.name, "price": r.price, "store_id": r.store_id})
            return {"items": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR
    
    @classmethod
    def return_items_for_store(cls, store_id):
        try:
            items = []
            row = cls.query.all()
            if row:
                for r in row:
                    print(f'r.store_id: {r.store_id} - {store_id}') 
                    if r.store_id == store_id:
                        items.append({"name": r.name, "price": r.price, "store_id": r.store_id})
            return {"items": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR