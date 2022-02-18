from db import db


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

    # Create

    # Read

    # Update

    # Delete
