import sqlite3 
import os 

PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = "data.db"
FILE = PATH + "\\" + DATABASE

connection = sqlite3.connect(FILE)
cursor = connection.cursor()

if os.path.isfile(FILE):
    create_table = "CREATE TABLE users(id int, username text, password text)"
    cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users (id, username, password) VALUES (?, ?, ?)"
cursor.execute(insert_query, user) 

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
info = cursor.execute(select_query)
print(info)

connection.commit()
connection.close()