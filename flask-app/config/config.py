from os import environ, path
from dotenv import load_dotenv

# get path
base_dir = path.abspath(path.dirname(__file__))

# load info
load_dotenv(path.join(base_dir, ".env"))


class BaseConfig:
    SECRET_KEY = environ.get("SECRET_KEY")
    TEMPLATES_FOLDER = environ.get("TEMPLATES_FOLDER")
    STATIC_FOLDER = environ.get("STATIC_FOLDER")


class DevConfig(BaseConfig):
    SERVER_NAME = environ.get("SERVER_NAME")
    DEBUG = environ.get("DEBUG")
    FLASK_ENV = environ.get("FLASK_ENV")
    TESTING = environ.get("TESTING")
