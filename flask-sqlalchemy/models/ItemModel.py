from utilities.constants import (FILE, INTERNAL_SERVER_ERROR)
import sqlite3
import logging 

class ItemModel: 
    def __init__(self, _id, name, price):
        self._id = _id
        self.name = name
        self.price = price
    
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_by_name(cls, name):
        try: 
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()

            query = "SELECT * FROM items WHERE name = ?"
            result = cursor.execute(query, (name,))
            row = result.fetchone()
            connection.close()
            
            return ({"item": cls(*row).json()}, 200) if row else None
        
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR

    @classmethod
    def add_to_database(cls, name: str, price: float):
        try:
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
            response = None

            if cls.find_by_name(name):
                query = "UPDATE items SET price = ? WHERE name = ?"
                cursor.execute(query, (price, name))
                response = {"Message": f"Item {name} updated successfully"}, 201
            else:
                query = "INSERT INTO items VALUES(NULL, ?, ?)"
                cursor.execute(query, (name, price))
                response = {"Message": f"Item {name} inserted successfully"}, 201

            connection.commit()
            connection.close()
            return response
        except Exception as e:
            logging.warning(f"Error {e}")
            return INTERNAL_SERVER_ERROR
    
    @classmethod
    def return_all_items(cls):
        try:
            connection = sqlite3.connect(FILE)
            cursor = connection.cursor()
            query = "SELECT * FROM items"
            result = cursor.execute(query)
            row = result.fetchall()
            connection.close()
            items = []
            if row:
                for r in row:
                    items.append({"name": r[1], "price": r[2]})
            return {"items": items}, 200
        except Exception as e:
            logging.error(f"Error {e}")
            return INTERNAL_SERVER_ERROR