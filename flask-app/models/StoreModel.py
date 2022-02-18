from db import db
from models.ItemModel import ItemModel
import logging

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    items = db.relationship("ItemModel", lazy= 'dynamic')
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def add_to_database(self):
        try: 
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logging.warning(f"ERROR: {e}")
        
    @classmethod
    def find_by_name(cls, name):
        try:
            print(f"Data {cls.query.filter_by(name = name).first()}")
            return cls.query.filter_by(name = name).first()
        except Exception as e:
            logging.warning(f"Error: {e}")
    
    @classmethod
    def update_to_database(cls,name, description):
        try: 
            store = cls.find_by_name(name = name)
            store.name = name
            store.description = description
            db.session.commit()
        except Exception as e:
            logging.warning(f"Error: {e}")
    
    @classmethod
    def delete_to_database(cls, name):
        try: 
            store = cls.find_by_name(name = name)
            db.session.delete(store)
            db.session.commit()
        except Exception as e:
            logging.warning(f"Error: {e}")
    
    @classmethod
    def get_all_elements(cls):
        try: 
            return StoreModel.query.all()
        except Exception as e:
            logging.warning(f"Error: {e}")