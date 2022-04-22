import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Config:
    # TEMPLATES_FOLDER = os.environ.get('TEMPLATES_FOLDER')
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG', False)
    FLASK_ENV = os.environ.get('FLASK_ENV_DEV')
    # SERVER_NAME = os.environ.get('SERVER_NAME')
    

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}