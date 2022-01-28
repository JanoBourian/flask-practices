from resources.User import User
from werkzeug.security import safe_str_cmp
import logging


def authenticate(username, password):
    try:
        user = User.find_by_username(username)
        # if user and user.password == password:
        if user and safe_str_cmp(user.password, password):
            return user
    except Exception as e:
        logging.error(f"Error {e}")


def identity(payload):
    try:
        user_id = payload["identity"]
        return User.find_by_id(user_id)
    except Exception as e:
        logging.error(f"Error {e}")
