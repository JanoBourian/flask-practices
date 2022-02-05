import sqlite3
import logging 
from constants import (FILE, )

def create_tables():
    logging.warning("Creating tables")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()

    create_table = "CREATE TABLE IF NOT EXISTS users( \
        id INTEGER PRIMARY KEY, username text UNIQUE, password text )"

    cursor.execute(create_table)
    connection.commit()

    create_table = "CREATE TABLE IF NOT EXISTS items( \
        id INTEGER PRIMARY KEY, name text UNIQUE, price real)"

    cursor.execute(create_table)
    connection.commit()

    connection.close()
