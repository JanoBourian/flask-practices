from db import db


class ItemModel(db.Model):
    def __init__(self, sku, name, price, store_id):
        self.sku = sku
        self.name = name
        self.price = price
        self.store_id = store_id

    # Create

    # Read

    # Update

    # Delete
