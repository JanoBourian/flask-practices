import os

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "data.db"
FILE = PATH + "\\" + DATABASE
INTERNAL_SERVER_ERROR = {"Error": "Internal Server Error"}
ITEM_NOT_EXIST = {"message": "Item not exists"}, 409