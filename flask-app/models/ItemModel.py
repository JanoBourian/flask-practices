from db import db
import logging

class ItemModel(db.Model):
    
    __tablename__ ="items"
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(30))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship('StoreModel')
    
    def __init__(self, sku, name, price, store_id):
        self.sku = sku
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def add_to_database(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logging.warning(f"ERROR {e}")
    
    @classmethod
    def find_by_name(cls, name):
        try:
            return cls.query.filter_by(name=name).first()
        except Exception as e:
            logging.warning(f"ERROR {e}")
    
    @classmethod
    def find_by_sku(cls, sku):
        try:
            return cls.query.filter_by(sku = sku).first()
        except Exception as e:
            logging.warning(f"ERROR {e}")
    
    @classmethod
    def update_to_database(cls, name, **data):
        try:
            item = cls.find_by_name(name)
            item.name = name
            item.price = data['price']
            item.store_id = data['store_id']
            db.session.commit()
        except Exception as e:
            logging.warning(f"ERROR {e}")
    
    @classmethod
    def delete_to_database(cls, name):
        try:
            item = cls.find_by_name(name)
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            logging.warning(f"ERROR {e}")
    
    @classmethod
    def get_all_elements(cls):
        try:
            return cls.query.all()
        except Exception as e:
            logging.warning(f"ERROR {e}")