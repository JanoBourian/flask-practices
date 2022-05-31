import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = os.environ.get('FLASKY_MAIL_SUBJECT_PREFIX')
    FLASKY_MAIL_SENDER = os.environ.get('FLASKY_MAIL_SENDER')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALchemy_TRACK_MODIFICATIONS')
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    TESTING = os.environ.get('TESTING_DEV', True)
    ENV = os.environ.get('ENV_DEV', 'development')
    DEBUG = os.environ.get('DEBUG_DEV', True)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_PREFIX') + os.path.join(basedir, os.environ.get('DATABASE_NAME_DEV'))

class TestingConfig(Config):
    TESTING = os.environ.get('TESTING_TEST', True)
    ENV = os.environ.get('ENV_TEST', 'testing')
    DEBUG = os.environ.get('DEBUG_TESTING', True)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_PREFIX') + os.path.join(basedir, os.environ.get('DATABASE_NAME_TESTING'))

class ProductionConfig(Config):
    TESTING = os.environ.get('TESTING_PRODUCTION', False)
    ENV = os.environ.get('ENV_PRODUCTION', 'production')
    DEBUG = os.environ.get('DEBUG_PRODUCTION')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_PREFIX') + os.path.join(basedir, os.environ.get('DATABASE_NAME_PRODUCTION'))

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default' : DevelopmentConfig
}