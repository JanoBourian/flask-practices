from user import User
from werkzeug.security import safe_str_cmp
import logging

# users = [{"id": 1, "username": "bob", "password": "asdf"}]
users = [User(1, "bob", "asdf")]

# username_mapping = {"bob": {"id": 1, "username": "bob", "password": "asdf"}}
username_mapping = {u.username: u for u in users}

# userid_mapping = {1: {"id": 1, "username": "bob", "password": "asdf"}}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    try: 
        user = username_mapping.get(username, None)
        # if user and user.password == password:
        if user and safe_str_cmp(user.password, password):
            return user
    except Exception as e:
        logging.error(f"Error {e}")
        
    
def identity(payload):
    try: 
        user_id = payload['identity']
        return userid_mapping.get(user_id, None)
    except Exception as e:
        logging.error(f"Error {e}")